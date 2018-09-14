# SQL Operations Reference

## Terms

TODO - table/service, column/field, input parameters, data source/set, results JSON object
Data source: part of a query that generates results. This is either an operation in a data connector, a subquery, or a join statement.
Result set - the list of results, or rows, produced by a query. In Transposit, each result is a JSON object or array.


TODO: string quotes, identifier \(and escaping\), immediate value

## Select statement

Select queries return data from one or more data sources. In Transposit, nearly all queries will be select queries, regardless of what the underlying API HTTP method is.

Select statement syntax:

```sql
SELECT <* or columns selection or JSON template>
FROM <operation or subquery or join>
WHERE <predicate>
EXPAND BY <columns>
LIMIT <number>
```

The `SELECT` clause is required.  
The clauses `WHERE`, `EXPAND BY` and `LIMIT` can be used only if a `FROM` clause is used.

The clauses must appear in the order that was specific above.

### Order of execution

1. `FROM`
2. `WHERE`
3. `EXPAND BY`
4. `LIMIT`
5. `SELECT`

### Select clause

The `SELECT` clause can be used for manipulating the structure and values of each item in the 'data source'.

The `SELECT` clause gets as input a JSON object or JSON array from the data source and produces a JSON object or a JSON array.

The `SELECT` clause supports three to ways to manipulate an item:

* [Select star](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#select-star)
* [Columns selection](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#columns-selection)
* [JSON template](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#json-template)

#### Select star

The `*` symbol selects the entire result without modifying it:

```sql
SELECT *
FROM connector.operation
```

#### Column selection

Column selection can be used to construct a JSON object with specific keys that will appear in the top level of the object.

Columns selection cannot construct a nested JSON object or a JSON array; to construct these items use [JSON template](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#json-template).

The syntax for columns selection is:

```sql
SELECT <column-expression> AS <column-alias>, <column-expression> AS <column-alias>, ...
```

`<column-expression>` describes how to construct a value in the output JSON object and can be one of the following:

* `<path>`
* `<connector-alias>.<path>`
* `<literal-value>`
* `<binary-expression>`

`<path>` describes the location of a value inside a JSON object or array. `<path>` contains one or more dot-separated keys/field names that describe the lookup chain of fields inside the input JSON object. The last item in `<path>` can be `.*`.

`<path>` can be one of the following:

* `<key>`
* `<key-1>.<key-2>.` ... `<key-N>`
* `<key>.*`
* `<key-1>.<key-2>.` ... `<key-N>.*`

`<key>` is an identifier.

`<connector-alias>` is an identifier.

`<literal-value>` is a number, string or boolean value.

`<binary-expression>` represents basic math operations \(for numbers\) or string concatenation \(of strings\) and can be one of the following:

* `<column-expression>` + `<column-expression>`
* `<column-expression>` - `<column-expression>`
* `<column-expression>` \* `<column-expression>`
* `<column-expression>` / `<column-expression>`

`AS <column-alias>` is optional. `<column-alias>` is an identifier.

**Object construction**

Column selection constructs a JSON object for each item in the data source based on the specified `<column-expression>`s and `<column-alias>`s.

The `<column-expression>`s and `<column-alias>`s are used in the same order as they appear in the query.

Each `<column-expression>` will be calculated and resolved to a value. The resolved value can be a scalar value \(number, string or boolean\), JSON object or JSON array.

When resolving a `<path>`, lookups are done recursively into the JSON object for each path component. If no value is found at that `<path>`, the field is not included in the output result.

A `.*` at the end of a `<path>` works as a 'spread' operator, copying each key at the current location into the result object.

For `<connector-alias>.<path>` - the resolve process will resolve the specified `<path>` only under the results from the table that was marked with the specified alias.  
If no table was marked with `<connector-alias>` the resolve will stop and the value will be considered as 'not found'.

For `<binary-expression>` the resolve process will deconstruct the expression and will resolved each part and then will reconstruct the resolved parts to produce immediate value.  
If the types of the operands is not the same the resolve process will produce an error and the entire query will fail.  
If the types of the operands is string, only the `+` operator is allowed, if a different operator is use the resolve process will produce an error and the entire query will fail.

If the resolve process found a valid value, this value will be added to the output JSON object with a key, the key is selected in the following way:

* If `<column-alias>` is specified it will be used as the key.
* If `<column-expression>` is `<path>` that does not ends with `.*` - the last `<key>` will be used as the key.
* If `<column-expression>` is `<path>` that ends with `.*` - the key and values under the last `<key>` will be used without change.
* Otherwise the entire `<column-expression>` will be used as the key. It's recommended to use `<column-alias>` in this case.

If the same key is used more than once the last value will be used and will override any previous values that had the same key.

If the value is resolved to `null` or 'not found' this value will not be added it to the output JSON object.

**Examples:**

_Selecting a single value:_

```sql
SELECT col1
FROM connector.operation
```

Will generate a JSON object with a single key:

```javascript
[
  {
    "col1": ...
  },
  ...
]
```

_Selecting multiple values:_

```sql
SELECT col1, col2, col3
FROM connector.operation
```

Will generate a JSON object with multiple keys:

```javascript
[
  {
    "col1": ...,
    "col2": ...,
    "col3": ...
  },
  ...
]
```

_Selecting nested value:_

To access a value inside a nested object you can use a `.` \(dot\) as separator between the nested object keys.

If the 'data source' is in the format:

```javascript
[
  {
    "nested": {
      "object": {
        "value": ...
      }
    }
  }
]
```

The query:

```sql
SELECT nested.object.value
FROM connector.operation
```

Will generate a JSON object with the key and value of the item in the specific path:

```javascript
[
  {
    "value": ...
  },
  ...
]
```

_Changing the key:_

You can use column alias to change the key of a value:

```sql
SELECT col1 AS foo
FROM connector.operation
```

Will generate a JSON object with the key `foo`, the value will be the value of `col1`:

```javascript
[
  {
    "foo": ...
  },
  ...
]
```

_Using table aliases:_

When a table is marked with alias \(see [table alias](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#connector-alias)\) the same table alias can be used as a qualifier in the beginning of the path to define exactly where to do the lookup for the path \(the results of which table to use\). This is useful when the query contains more than one table \(for example in [join query](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#join-query)\).

```sql
SELECT T.col1
FROM connector.operation AS T
```

Will generate a JSON object with a single key:

```javascript
[
  {
    "col1": ...
  },
  ...
]
```

_Literal value:_

Any value of the types number, string or boolean can be used as an immediate value.

```sql
SELECT 7 as value1, 'seven' as value2, true as value3
```

Will generate:

```javascript
[
  {
    "value1": 7,
    "value2": "seven",
    "value3": true
  }
]
```

_Binary expressions:_

Binary expressions can be used for basic math operation \(for numbers\) or string concatenation \(of strings\).  
Binary expressions can use any combination of path, immediate values and nested binary expressions.  
Parentheses can be used to define the order of operations.

The query:

```sql
SELECT (20 + 3) * 2 as value
```

Will generate:

```javascript
[
  {
    "value": 46
  }
]
```

With columns:

```sql
SELECT (col1 + 10) * nested.object.value1 as value
FROM connector.operation
```

Will use the values of `col1` and `nested.object.value1` to calculate the value of the expression.

_Selecting all values under an object:_

To access all values inside a nested object you can use a `.*` in the end of the path that contains the values.

If the 'data source' is in the format:

```javascript
[
  {
    "nested": {
      "object": {
        "value1": ...,
        "value2": ...,
        "value3": ...
      }
    }
  }
]
```

The query:

```sql
SELECT nested.object.*
FROM connector.operation
```

Will generate a JSON object with the all the keys and values in the specific path:

```javascript
[
  {
    "value1": ...,
    "value2": ...,
    "value3": ...
  },
  ...
]
```

#### JSON template

JSON template is a more generic way to construct a JSON object or a JSON array as the output item.

To construct a JSON object use the syntax:

```sql
SELECT { <key>: <json-value>, ... }
```

To construct a JSON array use the syntax:

```sql
SELECT [ <json-value>, ... ]
```

`<key>` is an identifier. For convenience JSON template doesn't require to use string quotes around the key but it should be used if the `<key>` contains spaces, illegal characters or keywords.

`<json-value>` can be one of the following:

* `<path>` - a column selection
* `<connector-alias>.<path>` - a column selection with table alias qualifier
* `<immediate-value>` - number, string or boolean
* `<binary-expression>` - a calculated expression
* `<json-object>` - construct a nested object
* `<json-array>` - construct a nested array

`<path>`, `<connector-alias>.<path>`, `<immediate-value>` and `<binary-expression>` are the same as in [columns selection](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#columns-selection). The only difference is that `.*` in the end of `<path>` is not allowed in JSON template, use [spread operator](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#spread-operator) instead.

`<json-object>` constructs a JSON object, the syntax is:

```javascript
{ <key-1>: <json-value-1>, <key-2>: <json-value-2>, ... <key-N>: <json-value-N> }
```

`<json-array>` constructs a JSON array, the syntax is:

```javascript
[ <json-value-1>,  <json-value-2>, ... <json-value-N>]
```

**Spread operator**

The spread operator expands a JSON object into JSON object or JSON array into a JSON array \(similar to `<path>.*` in [columns selection](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#columns-selection)\).

The spread JSON object use:

```sql
SELECT { ... obj }
```

The spread JSON array use:

```sql
SELECT [ ... arr ]
```

The spread operator can be mixed with any other JSON template features.

**Object construction**

JSON template construct a JSON object or array for each item in the 'data source' based on the specified template.  
If the outer template is a `<json-object>` the item will be JSON object.  
If the outer template is a `<json-array>` the item will be JSON array.  
The values inside the outer template can be any type.

The `<key>`s and `<json-value>`s are used in the same order as they appear in the template.

Each `<json-value>` will be calculated and resolved. The resolved value can be immediate value \(number, string or boolean\), JSON object or JSON array.

`<path>`, `<connector-alias>.<path>`, `<immediate-value>` and `<binary-expression>` are resolved the same as in [columns selection](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#columns-selection).

`<json-object>` and `<json-array>` are resolved recursively.

If the resolve process found a valid value, this value will be added to the output JSON object or array. If the output item is a JSON object the specified `<key>` will be used.

If the same key is used more than once the last value will be used and will override any previous values that had the same key.

If the value is resolved to `null` or 'not found':

* If the output item is JSON object this value will not be added it to the output item.
* if the output item is JSON array this value will be added it to the output item as `null`.

**Examples**

_Selecting a single value:_

```sql
SELECT { col1: col1 }
FROM connector.operation
```

Will generate a JSON object with a single key:

```javascript
[
  {
    "col1": ...
  },
  ...
]
```

_Selecting multiple values:_

```sql
SELECT { col1: col1, col2: col2, col3: col3 }
FROM connector.operation
```

Will generate a JSON object with multiple keys:

```javascript
[
  {
    "col1": ...,
    "col2": ...,
    "col3": ...
  },
  ...
]
```

_Selecting nested value:_

To access a value inside a nested object you can use a `.` \(dot\) as separator between the nested object keys.

If the 'data source' is in the format:

```javascript
[
  {
    "nested": {
      "object": {
        "value": ...
      }
    }
  }
]
```

The query:

```sql
SELECT { value: nested.object.value }
FROM connector.operation
```

Will generate a JSON object with the key and value of the item in the specific path:

```javascript
[
  {
    "value": ...
  },
  ...
]
```

_Changing the key:_

JSON template requires a key, so the same syntax can be used even if you want to use a different key:

```sql
SELECT { foo: col1 }
FROM connector.operation
```

Will generate a JSON object with the key `foo`, the value will be the value of `col1`:

```javascript
[
  {
    "foo": ...
  },
  ...
]
```

If the key contains spaces, illegal characters or is a keyword, it must be escaped:

```sql
SELECT { `key with spaces`: col1 }
FROM connector.operation
```

Will generate

```javascript
[
  {
    "key with spaces": ...
  },
  ...
]
```

_Using table alias:_

When a table is marked with alias \(see [table alias](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#connector-alias)\) the same table alias can be used as a qualifier in the beginning of the path to define exactly where to do the lookup for the path \(the results of which table to use\). This is useful when the query contains more than one table \(for example in [join query](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#join-query)\).

```sql
SELECT { col1: T.col1 }
FROM connector.operation AS T
```

Will generate a JSON object with a single key:

```javascript
[
  {
    "col1": ...
  },
  ...
]
```

_Immediate value:_

Any value of the types number, string or boolean can be used as an immediate value.

```sql
SELECT { value1: 7, value2: 'seven', value3: true }
```

Will generate:

```javascript
[
  {
    "value1": 7,
    "value2": "seven",
    "value3": true
  }
]
```

_Binary expressions:_

Binary expressions can be used for basic math operation \(for numbers\) or string concatenation \(of strings\).  
Binary expressions can use any combination of path, immediate values and nested binary expressions.  
Parentheses can be used to define the order of operations.

The query:

```sql
SELECT { value: (20 + 3) * 2 }
```

Will generate:

```javascript
[
  {
    "value": 46
  }
]
```

With columns:

```sql
SELECT { value: (col1 + 10) * nested.object.value1 }
FROM connector.operation
```

Will use the values of `col1` and `nested.object.value1` to calculate the value of the expression.

_Constructing an array:_

The previous examples showed how to construct an object as the output item. With JSON template you can also construct an array as the output item.

```sql
SELECT [ col1 ]
FROM connector.operation
```

Will generate a JSON array with a single item \(the item is the value of `col1`\):

```javascript
[
  [
    <VALUE OF col1>
  ],
  ...
]
```

And you can use all the other expressions as in the previous examples - nested object, table alias, immediate values and binary expressions:

```sql
SELECT [ (col1 + 10) * nested.object.value1, T.col2, 7, 'seven', true ]
FROM connector.operation AS T
```

_Constructing nested template:_

You can use the JSON object and array templates recursively and construct any nested structure:

```javascript
SELECT {
  arr1: [ { col1: col1 }, { col2: col2 } ],
  obj: {
    bar: [
      col3.nested.value1,
      col3.nested.value2,
      col3.nested.value3
      ]
    }
  }
FROM connector.operation
```

_Selecting all values under an object or array:_

To access all the values inside an object or array you can use the spread operator \(`...`\). Note that the inner type and the outer type must be the same: an object can be spread into a JSON object template and an array can be spread into JSON array template:

If the 'data source' is in the format:

```javascript
[
  {
    "object": {
      "value1": ...,
      "value2": ...,
      "value3": ...
    },
    "array": [ { "val1": ... }, { "val2": ... }, { "val3": ... } ]
  }
]
```

The query:

```sql
SELECT { ... object }
FROM connector.operation
```

Will generate a JSON object with the all the keys and values under `object`:

```javascript
[
  {
    "value1": ...,
    "value2": ...,
    "value3": ...
  },
  ...
]
```

The query:

```sql
SELECT [ ... array ]
FROM connector.operation
```

Will generate a JSON array with the all the values under `array`:

```javascript
[
  [
    { "val1": ... },
    { "val2": ... },
    { "val3": ... }
  ],
  ...
]
```

#### Immediate values

TODO: maybe we don't need this section.

Immediate values can be use with and without `FROM` clause.

Immediate value is an expression with the type: number, string or boolean value, or a boolean expression that can be resolved to one of these types, i.e. the expression doesn't contain `<path>`.

Immediate values can be used in columns selection or in JSON template.

**Examples:**

```sql
SELECT 1 AS number, 'one' AS string, true AS boolean, (1 + 2) * 3 AS expression
```

Will generate:

```javascript
[
  {
    "number": 1,
    "string": "one",
    "boolean": true,
    "expression": 9
  }
]
```

```sql
SELECT { number: 1, string: 'one', boolean: true, expression: (1 + 2) * 3 }
```

Will generate:

```javascript
[
  {
    "number": 1,
    "string": "one",
    "boolean": true,
    "expression": 9
  }
]
```

```sql
SELECT [ 1, 'one', true, (1 + 2) * 3 ]
```

Will generate:

```javascript
[[1, "one", true, 9]]
```

### From clause

The `FROM` clause of a query creates the data set that the other parts of the query will use.

The `FROM` clause is the first part that is running when the query is executed.

The `FROM` clause support three types of data sources:

* [Table](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#table)
* [Sub query](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#sub-query)
* [Join](https://github.com/transposit/docs/tree/052cc31e86f4f0cb3c4c208bac0f55fd4ad10d9b/references/tql-reference.md#join)

#### Table

To get data from a single service you can use the service directly in the `FROM` clause:

```sql
SELECT *
FROM connector.operation AS <connector-alias>
```

`AS <column-alias>` is optional. `<connector-alias>` is an identifier.

#### Sub query

In some case when you want to manipulate the data set in multiple steps, you can use a sub query in the `FROM` clause:

```sql
SELECT *
FROM (SELECT * FROM connector.operation) AS <operation-alias>
```

`AS <column-alias>` is optional. `<operation-alias>` is an identifier.

Both the outer and the inner queries can use any of the other clauses - `FROM`, `WHERE`, `EXPAND BY`, `LIMIT`, `SELECT`.

#### Join

Join can be used to merge the results of two or more tables that share some common data.

```sql
SELECT *
FROM connector.operation_1 AS <operation-alias-1>
<join-type> JOIN connector.operation_2 AS <operation-alias-2>
ON <predicate>
```

`<join-type>` is optional and can be one of:

* `INNER`
* `LEFT OUTER`
* `RIGHT OUTER`
* `FULL OUTER`

If `<join-type>` is not specified the default is `INNER`.

In joins `AS <column-alias>` is required. `<operation-alias>` is an identifier.

TODO - , add examples for join

### Where clause

TODO - filters, input params, $body, AND/OR, IN, subquery, expressions

### Expand by clause

TODO - column, nested path, alias, multiple columns

### Limit clause

TODO

TODO: Document the pagination bubble that gets shown in the documentation viewer to indicate that we support pagination with the LIMIT

### Expressions

TODO \(maybe this is not needed and we will talk about expressions in the relevant sections\)

## External parameters

TODO \(@userId\)

## Escaping

TODO - list of keywords, valid/invalid characters, how to escape

### Comments

We support multi-line comments using `/* */` or single line comments using the `--` prefix

