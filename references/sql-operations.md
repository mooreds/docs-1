---
id: sql-operations
title:  SQL operations
layout: docs.mustache
tags: doc
---

## Terms

Operation: An [operation](/docs/building/operations) in a data connection. This takes the place of a "table" in SQL for relational databases.

Data source: part of a query that generates results. This is either an operation, a subquery, or a join statement.

Result set: the list of results, or rows, produced by a query. In Transposit, each result is a JSON object or array.

Column: a field in a result.

## Select statement

Select queries return data from one or more data sources. In Transposit, nearly all queries will be select queries, regardless of what the underlying API HTTP method is.

Select statement syntax:

```sql
SELECT <* or column selection or JSON template>
FROM <operation or subquery or join>
WHERE <predicate>
EXPAND BY <columns>
UNION <select statement>
LIMIT <number>
```

The `SELECT` clause is required.

The clauses `WHERE`, `EXPAND BY` and `LIMIT` can be used only if a `FROM` clause is used.

The `UNION` keyword allows a statement to combine multiple SELECT statements together into a single statement.

The clauses must appear in the order specified above.

### Order of execution

1. `FROM`
2. `WHERE`
3. `EXPAND BY`
4. `UNION`
5. `LIMIT`
6. `SELECT`

### Select clause

The `SELECT` clause can be used for manipulating the structure and values of each item in the data source.

The `SELECT` clause gets as input a JSON object or JSON array from the data source and produces a JSON object or a JSON array.

The `SELECT` clause supports three ways to manipulate an item:

* [Select star](/docs/references/sql-operations#select-star)
* [Column selection](/docs/references/sql-operations#column-selection)
* [JSON template](/docs/references/sql-operations#json-templates)

#### Select star

The `*` symbol selects the entire result without modifying it:

```sql
SELECT *
FROM connection.operation
```

#### Column selection

Column selection can be used to construct a JSON object with specific keys that will appear in the top level of the object.

Column selection cannot construct a nested JSON object or a JSON array; to construct these items use a [JSON template](/docs/references/sql-operations#json-templates).

The syntax for column selection is:

```sql
SELECT <column-expression> AS <column-alias>, <column-expression> AS <column-alias>, ...
```

`<column-expression>` describes how to construct a value in the output JSON object and can be one of the following:

* `<path>`
* `<operation-alias>.<path>`
* `<literal-value>`
* `<binary-expression>`

`<path>` describes the location of a value inside a JSON object or array. `<path>` contains one or more dot-separated keys/field names that describe the lookup chain of fields inside the input JSON object. The last item in `<path>` can be `.*`. Bracket notation with array indexes and string keys is also supported.

Examples of valid `<path>`s:

* `<key>`
* `<key-1>.<key-2>.` ... `<key-N>`
* `<key>.*`
* `<key-1>.<key-2>.` ... `<key-N>.*`
* `<key>[0]`
* `<key-1>[0].<key-2>`
* `<key-1>[0].<key-2>.*`
* `<key-1>[0].<key-2>[1].<key-3>`
* `[<key>]`

`<key>` is an identifier.

`<operation-alias>` is an identifier.

`<literal-value>` is a number, string or boolean value.

`<binary-expression>` represents basic math operations (for numbers) or string concatenation (of strings) and can be one of the following:

* `<column-expression>` + `<column-expression>`
* `<column-expression>` - `<column-expression>`
* `<column-expression>` \* `<column-expression>`
* `<column-expression>` / `<column-expression>`

`AS <column-alias>` is optional. `<column-alias>` is an identifier.

##### Result construction

Column selection constructs a JSON object for each item in the data source based on the specified `<column-expression>`s and `<column-alias>`s.

The `<column-expression>`s and `<column-alias>`s are used in the same order as they appear in the query.

Each `<column-expression>` will be calculated and resolved to a value. The resolved value can be a scalar value (number, string or boolean), JSON object or JSON array.

When resolving a `<path>`, lookups are done recursively into the JSON object for each path component. If no value is found at that `<path>`, the value is considered 'not found'.

A `.*` at the end of a `<path>` works as a 'spread' operator, copying each key at the current location into the result object.

For `<operation-alias>.<path>` the resolve process will resolve the specified `<path>` only under the results from the operation that was marked with the specified alias.

If no operation was marked with `<operation-alias>` the resolve will stop and the value will be considered as 'not found'.

For `<binary-expression>` the resolve process will evaluate the expression to produce a value.

If the types of the operands is not the same the resolve process will produce an error and the entire query will fail.

If the types of the operand is string, only the `+` operator is allowed, if a different operator is used the resolve process will produce an error and the entire query will fail.

If the resolve process produces a valid value, this value will be added to the output JSON object with a key, the key is selected in the following way:

* If `<column-alias>` is specified it will be used as the key.
* If `<column-expression>` is a `<path>` that does not end with `.*`, the last `<key>` will be used as the key.
* If `<column-expression>` is a `<path>` that ends with `.*`, the keys and values under the last `<key>` will all be copied into the result object.
* Otherwise the entire `<column-expression>` will be used as the key. It's recommended to use `<column-alias>` in this case.


> If the same key is used more than once the last value will be used and will override any previous values that had the same key.

If the value is resolved to `null` or 'not found' this value will not be added it to the output JSON object.

##### Examples

_Selecting a single value:_

```sql
SELECT col1
FROM connection.operation
```

Will generate an array with one element: a JSON object with a single key:

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
FROM connection.operation
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

_Selecting a nested value:_

To access a value inside a nested object you can use a `.` (dot) or `[<key>]` (bracket notation) as a separator between the nested object keys.

For the following result:

```javascript
[
  {
    "nested": {
      "object": {
        "value": "myValue"
      }
    }
  }
]
```

The queries:

```sql
SELECT nested.object.value
FROM connection.operation
```

```sql
SELECT nested['object']['value']
FROM connection.operation
```

Will generate a JSON object with the key and value of the item at the specific path:

```javascript
 [
   {
     "value": "myValue"
   },
   ...
 ]
```

Array indexing is also supported. For example, for the following result:

```javascript
[
  {
    "nested": ["value0", "value1", "value2"]
  }
]
```

The query:
```sql
SELECT nested[0], nested[1]
FROM connection.operation
```

Will generate a JSON object of:

```javascript
[
  {
    "0": "value0",
    "1": "value1"
  }
]
```

_Changing the key:_

You can use column alias to change the key of a value:

```sql
SELECT col1 AS foo
FROM connection.operation
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

_Using operation aliases:_

When an operation (or subquery) is named with an [alias](/docs/references/sql-operations#operation-alias), the alias can later be used as a qualifier at the beginning of the path to define exactly where to do the lookup for the path (the results of which operation or subquery to use). This is particularly useful in [join queries](/docs/references/sql-operations#join-query), where the query has more than one data source.

```sql
SELECT T.col1
FROM connection.operation AS T
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

Numbers, strings and booleans can be used directly in a column selector. If no alias is provided, the literal value is used as both the key and value:

```sql
SELECT 7, 7 as value1, 'seven' as value2, true as value3
```

Will generate:

```javascript
[
  {
    "7": 7,
    "value1": 7,
    "value2": "seven",
    "value3": true
  }
]
```

_Binary expressions:_

Binary expressions can be used for basic math operation (for numbers) or string concatenation (of strings). Binary expressions can use any combination of paths, literal values, and nested binary expressions. Parentheses can be used to define the order of operations.

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
FROM connection.operation
```

Will use the values of `col1` and `nested.object.value1` to calculate the value of the expression.

_Selecting all values in an object:_

To access all key/value in a nested object you can use a `.*` in the end of the path that contains the values.

If the result has the format:

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
FROM connection.operation
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

#### JSON templates

JSON templates are a more generic way to construct JSON objects or arrays as the output item.

To construct a JSON object use the syntax:

```sql
SELECT { <key>: <json-value>, ... }
```

To construct a JSON array use the syntax:

```sql
SELECT [ <json-value>, ... ]
```

`<key>` is an identifier. For convenience, JSON templates do not require the use of string quotes around the key unless the `<key>` contains spaces, illegal characters or keywords.

`<json-value>` can be one of the following:

* `<path>` - a column selection
* `<operation-alias>.<path>` - a column selection with operation alias qualifier
* `<literal-value>` - number, string or boolean
* `<binary-expression>` - a calculated expression
* `<json-object>` - construct a nested object
* `<json-array>` - construct a nested array

`<path>`, `<operation-alias>.<path>`, `<literal-value>` and `<binary-expression>` are the same as in [column selection](/docs/references/sql-operations#column-selection). The only difference is that `.*` at the end of `<path>` is not allowed in JSON templates; use the [spread operator](/docs/references/sql-operations#spread-operator) instead.

`<json-object>` constructs a JSON object, the syntax is:

```javascript
{ <key-1>: <json-value-1>, <key-2>: <json-value-2>, ... <key-N>: <json-value-N> }
```

`<json-array>` constructs a JSON array, the syntax is:

```javascript
[ <json-value-1>,  <json-value-2>, ... <json-value-N>]
```

#### Spread operator

The spread operator expands a JSON object into a JSON object or a JSON array into a JSON array (similar to `<path>.*` in [column selection](/docs/references/sql-operations#column-selection)).

Spread JSON object use:

```sql
SELECT { ... obj }
```

Spread JSON array use:

```sql
SELECT [ ... arr ]
```

The spread operator can be mixed with any other JSON template features.

#### Object construction

A JSON template constructs a JSON object or array for each item from the data source based on the specified template.

If the outer template is a `<json-object>` the item will be JSON object.

If the outer template is a `<json-array>` the item will be JSON array.

The values inside the outer template can be any type.

The `<key>`s and `<json-value>`s are used in the same order as they appear in the template.

Each `<json-value>` will be calculated and resolved. The resolved value can be a scalar value (number, string or boolean), JSON object or JSON array.

`<path>`, `<operation-alias>.<path>`, `<immediate-value>` and `<binary-expression>` are resolved the same as in [column selection](/docs/references/sql-operations#columns-selection).

`<json-object>` and `<json-array>` are resolved recursively.

If the resolve process finds a valid value, this value will be added to the output JSON object or array. If the output item is a JSON object, the specified `<key>` will be used.

> If the same key is used more than once, the last value will be used and will override any previous values that had the same key.

If the value is resolved to `null` or 'not found':

* If the output item is a JSON object, this value will not be added it to the output item.
* If the output item is a JSON array, this value will be added it to the output item as `null`.

**Examples**

_Selecting a single value:_

```sql
SELECT { col1: col1 }
FROM connection.operation
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
FROM connection.operation
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

_Selecting a nested value:_

To access a value inside a nested object you can use a `.` (dot) as separator between the nested object keys.

For the following result:

```javascript
[
  {
    "nested": {
      "object": {
        "value": "myValue"
      }
    }
  }
]
```

The query:

```sql
SELECT { value: nested.object.value }
FROM connection.operation
```

Will generate a JSON object with the key and value of the item in the specific path:

```javascript
[
  {
    "value": "myValue"
  },
  ...
]
```

_Changing the key:_

The key is a part of the JSON template, so the same syntax can be used even if you want to use a different key:

```sql
SELECT { foo: col1 }
FROM connection.operation
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
FROM connection.operation
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

_Using an operation alias:_

When an operation (or subquery) is named with an [alias](/docs/references/sql-operations#operation-alias), the alias can later be used as a qualifier at the beginning of the path to define exactly where to do the lookup for the path (the results of which operation or subquery to use). This is particularly useful in [join queries](/docs/references/sql-operations#join-query), where the query has more than one data source.

```sql
SELECT { col1: T.col1 }
FROM connection.operation AS T
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

Numbers, strings and booleans can be used as the value in a JSON template:

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

Binary expressions can be used for basic math operation (for numbers) or string concatenation (of strings). Binary expressions can use any combination of path, immediate values and nested binary expressions. Parentheses can be used to define the order of operations.

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
FROM connection.operation
```

Will use the values of `col1` and `nested.object.value1` to calculate the value of the expression.

_Constructing an array:_

The previous examples showed how to construct an object as the output item. With JSON templates you can also construct an array as the output item.

```sql
SELECT [ col1 ]
FROM connection.operation
```

Will generate a JSON array with a single item (the item is the value of `col1`):

```javascript
[
  [
    <VALUE OF col1>
  ],
  ...
]
```

All expressions shown in the previous examples can also be used: nested object, operation alias, immediate values, and binary expressions:

```sql
SELECT [ (col1 + 10) * nested.object.value1, T.col2, 7, 'seven', true ]
FROM connection.operation AS T
```

_Constructing nested objects:_

You can use JSON object and array templates recursively and construct any nested structure:

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
FROM connection.operation
```

_Selecting all values in an object or array:_

To access all the values inside an object or array you can use the spread operator (`...`). Note that the inner type and the outer type must be the same: an object can be spread into a JSON object template and an array can be spread into a JSON array template:

If the results have the format:

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
FROM connection.operation
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
FROM connection.operation
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

### From clause

The `FROM` clause of a query creates the result set that the other parts of the query will use. When the query is executed, the `FROM` clause runs first.

The `FROM` clause supports three types of data sources:

* [Operation](/docs/references/sql-operations#operation)
* [Subquery](/docs/references/sql-operations#subquery)
* [Join](/docs/references/sql-operations#join)

#### Operation

To get data from a single operation, you can use the operation directly in the `FROM` clause:

```sql
SELECT *
FROM connection.operation AS <operation-alias>
```

`AS <operation-alias>` is optional. `<operation-alias>` is an identifier.

#### Subquery

To manipulate the data set in multiple steps, you can use a subquery in the `FROM` clause:

```sql
SELECT *
FROM (SELECT * FROM connection.operation) AS <operation-alias>
```

`AS <operation-alias>` is optional. `<operation-alias>` is an identifier.

Both the outer and the inner queries can use any of the other clauses - `FROM`, `WHERE`, `EXPAND BY`, `LIMIT`, `SELECT`.

### Join

Joins can be used to merge the results of two or more operations that are related in some way.

```sql
SELECT *
FROM connection.operation_1 AS <operation-alias-1>
<join-type> JOIN connection.operation_2 AS <operation-alias-2>
ON <predicate>
```

`<join-type>` is optional and can be one of:

* `INNER`
* `LEFT OUTER`
* `RIGHT OUTER`
* `FULL OUTER`

If `<join-type>` is not specified the default is `INNER`.

In joins, `AS <column-alias>` is required. `<operation-alias>` is an identifier.

### Where clause

The `WHERE` clause is used to specify input parameters to operations and filters on results. The syntax for the `WHERE` clause is:

```sql
WHERE <predicate>
```

A `<predicate>` describes the sequence of conditions that are applied to the data sources. Multiple `<predicate>`s can be recursively combined with boolean `AND`, `OR`, and `NOT` operators in the following format:

* `<condition>`
* `<predicate> AND <predicate>`
* `<predicate> OR <predicate>`
* `NOT <predicate>`

For instance:

```sql
SELECT * FROM <connection.operation>
WHERE <condition-1> AND NOT <condition-2> OR <condition-3> ...
```

Parentheses can also be used for grouping.

Each condition can be one of the following:

* `<name>` `<operator>` `<column-expression>`
* `<name>` `<operator>` `<subquery>`
* `<name>` `IN` `<literal-tuple>`
* `<name-tuple>` `IN` `<nested-literal-tuple>`

The `<operator>` can be one of the following:

* `=` - equal to
* `!=` - not equal to
* `>` - greater than
* `>=` - greater than or equal to
* `<` - less than
* `<=` - less than or equal to
* `IN` - equal to any in a list of values.

The `<column-expression>` is the same as what is used in [column selection](/docs/references/sql-operations#column-selection).

If a subquery is used, the `<operator>` must be `=` or `IN`. If the operator is `=`, the subquery must return a single result.

#### Input parameters and filters

A condition in a `WHERE` clause may either be passed as an input parameter or treated as a filter on the output of the data source. There is no difference in the syntax; Transposit automatically makes the determination based on the `<name>` of the condition: if it is defined as a parameter for the operation, the condition will be passed into the operation. Otherwise, the condition is treated as a filter and will remove rows from the result set that do not match the criteria.

When two input parameters are combined with an `AND`, both are passed to the underlying operation. However, if two input parameters are combined with an `OR`, it will result in two invocations of the operation. For instance:

```sql
SELECT * FROM <connection.operation> WHERE param1 = 'val1' AND param2 = 'val2'
```

Results in a single invocation of the operation that is passed `'val1'` as `param1` and `'val2'` as `param2`.

```sql
SELECT * FROM <connection.operation> WHERE param1 = 'val1' OR param2 = 'val2'
```

Results in two invocations of the operation that are run in parallel. The first is passed `'val1'` as `param1` and is not passed a value for `param2`. The second invocation is passed `'val2'` as `param2` and is not passed a value for `param1`. When both invocations are complete, the result sets from each are concatenated together before other parts of the query are run.

Note that `IN` is equivalent to `OR`s of `=` operators, and thus may also result in multiple invocations of an operation. For instance:

```sql
SELECT * FROM <connection.operation> WHERE param1 IN ('val1', 'val2', 'val3')
```

Is equivalent to:

```sql
SELECT * FROM <connection.operation> WHERE param1 = 'val1' OR param1 = 'val2' OR param1 = 'val3'
```

Both will result in three parallel invocations of the operation.

#### Mapping and Tuples

The `<literal-tuple>` is one of:

* `(<val-1>, <val-2>, ...)` - a list of literal values
* `((<val-1-a>, <val-1-b>, ...), (<val-2-a>, <val-2-b>, ...), ...)` - a list of nested tuples

The first can be used with the `IN` operator to map to a single parameter or result column:

```sql
WHERE col1 IN (<val-1>, <val-2>, ...)
```

The latter can be used to map to multiple parameters or result columns using a `<name-tuple>`:

```sql
WHERE (col1, col2) IN ((<col1-val1>, <col2-val1>), (<col1-val2>, <col2-val2>), ...)
```

The number of items in each nested tuple on the right side of the `IN` must match the number of items in the `<name-tuple>` on the left.

This sort of column mapping is also possible with subqueries.

```sql
WHERE (col1, col2, ..., colN) IN (SELECT col1, col2, ... colN FROM <connection.operation>)
```

The mapping is positional (first column is mapped to the first name in the tuple, and so on), so the names of the subquery columns do not have to match the names in the `<name-tuple>`. However, the number of columns in the subquery must match the number of items in the `<name-tuple>`.

#### Operation aliases

Like the `<path>` in [column selection](/docs/references/sql-operations#column-selection), the `<name>` in a `WHERE` condition can be prefixed with an [operation alias](/docs/references/sql-operations#operation-alias) to refer to the results of a named data source.

### Expand by clause

The `EXPAND BY` clause expands (flattens) the items in a JSON array. This tends to be useful when working with APIs, where the relevant results may be nested inside one or more JSON objects.

The syntax for `EXPAND BY` is:

```sql
SELECT * FROM <connection.operation>
WHERE <predicate>
EXPAND BY <path-1> AS <column-alias>, <path-2> AS <column-alias>, ..., <path-N> AS <column-alias>
```

`<column-path>`

`EXPAND BY` works something like this:

For each result in the result set, for each `<path>` in the list of paths:

1. Resolve the value at the path using the same mechanism as in [column-selection](/docs/references/sql-operations#result-construction).
2. Check that this value is an array of items, otherwise skip this result.
3. Create a new result for each item in the array. If there is no `<column-alias>`, the item is placed in the same position as the array it came from (replacing the array). Otherwise, the alias is used to place the item and the original array is left intact.
4. Replace the top-level result set with this new list of results

**Examples**

_Expand by a single column_

If the results of `connection.operation` have the format:

```javascript
[
  {
    "id": 1,
    "vals": [1, 2]
  },
  {
    "id": 2,
    "vals": [3, 4]
  }
]
```

The query:

```sql
SELECT * FROM connection.operation
EXPAND BY vals
```

Will create a row for each item in `vals`:

```javascript
[
  { "id": 1, "vals": 1 },
  { "id": 1, "vals": 2 },
  { "id": 2, "vals": 3 },
  { "id": 2, "vals": 4 }
]
```

_Expand by a single column with an alias_

If the results of `connection.operation` have the format:

```javascript
[
  {
    "id": 1,
    "vals": [1, 2]
  },
  {
    "id": 2,
    "vals": [3, 4]
  }
]
```

The query:

```sql
SELECT * FROM connection.operation
EXPAND BY vals as aliasedVals
```

Will create the following result set:

```javascript
[
  {
    "id": 1,
    "vals": [1, 2],
    "aliasedVals": 1
  },
  {
    "id": 1,
    "vals": [1, 2],
    "aliasedVals": 2
  },
  {
    "id": 2,
    "vals": [3, 4],
    "aliasedVals": 3
  },
  {
    "id": 2,
    "vals": [3, 4],
    "aliasedVals": 4
  }
]
```

Notice that when an alias is used, the original array is left in the results.

_Expand by a nested field_

If the results of `connection.operation` have the format:

```javascript
[
  {
    "id": 1,
    "nested": {
      "vals": [1, 2] 
    }
  },
  {
    "id": 2,
    "nested": {
      "vals": [3, 4] 
    }
  }
]
```

The query:

```sql
SELECT * FROM connection.operation
EXPAND BY nested.vals
```

Will create the following result set:

```javascript
[
  {
    "id": 1,
    "nested": {
      "vals": 1
    }
  },
  {
    "id": 1,
    "nested": {
      "vals": 2
    }
  },
  {
    "id": 2,
    "nested": {
      "vals": 3
    }
  },
  {
    "id": 2,
    "nested": {
      "vals": 4
    }
  }
]
```

Notice that the nested structure is maintained.

_Expand by multiple fields_

If the results of `connection.operation` have the format:

```javascript
[
  {
    "id": 1,
    "letters": ["a", "b"],
    "numbers": [1, 2] 
  },
  {
    "id": 2,
    "letters": ["c", "d"],
    "numbers": [3, 4] 
  }
]
```

The query:

```sql
SELECT * FROM connection.operation
EXPAND BY letters, numbers
```

Will create the following result set:

```javascript
[
  {
    "id": 1,
    "letters": "a",
    "numbers": 1
  },
  {
    "id": 1,
    "letters": "a",
    "numbers": 2
  },
  {
    "id": 1,
    "letters": "b",
    "numbers": 1
  },
  {
    "id": 1,
    "letters": "b",
    "numbers": 2
  },
  {
    "id": 2,
    "letters": "c",
    "numbers": 3
  },
  {
    "id": 2,
    "letters": "c",
    "numbers": 4
  },
  {
    "id": 2,
    "letters": "d",
    "numbers": 3
  },
  {
    "id": 2,
    "letters": "d",
    "numbers": 4
  }
]
```

_Expand by with missing fields_

If the results of `connection.operation` have the format where `vals` is missing from one of the rows:

```javascript
[
  {
    "id": 1,
    "vals": [1, 2] 
  },
  {
    "id": 2,
  },
  {
    "id": 3,
    "vals": [3, 4] 
  }
]
```

The query:

```sql
SELECT * FROM connection.operation
EXPAND BY vals
```

Will create the following result set:

```javascript
[
  {
    "id": 1,
    "vals": 1
  },
  {
    "id": 1,
    "vals": 2
  },
  {
    "id": 3,
    "vals": 3
  },
  {
    "id": 3,
    "vals": 4
  }
]
```

Notice that because the item with `id: 2` did not have a field at the path `vals`, it does not show up in the result set.

### Union

The `UNION` keyword combines the results of two `SELECT` statements together.
```sql
SELECT *
FROM connection.operation_1
UNION <union-type>
SELECT *
FROM connection.operation_2
```

`<union-type>` is optional and can be one of:
* `ALL`
* `DISTINCT`

If `<union-type>` is not specified, the default is `DISTINCT`.

The statements can include `SELECT`, `FROM`, `WHERE`, and `EXPAND BY` clauses. A `LIMIT` can be applied by surrounding the statement in parentheses.

```sql
(SELECT * FROM connection.operation_1 LIMIT 10)
UNION ALL
SELECT *
FROM connection.operation_2
```

`UNION ALL` will return all results from both selections. `UNION DISTINCT` will return only unique results, removing any rows with the same data.

A `SELECT` statement can use multiple `UNION`s to combine three or more statements together. These can have different union types. A `UNION DISTINCT` will remove duplicate elements from the `SELECT` after it and from _all_ `SELECT`s before it.

### Limit clause

The limit clause specifies the maximum number of results to return in the query. The syntax is:

```sql
LIMIT <number>
```

### External parameters

To access the value of a parameter defined on the SQL operation, use the following syntax:

```sql
@<param-name>
```

The `<param-name>` has the same restrictions as operations: it must start with an underscore or letter, after which letters, digits, underscores, and dashes are allowed.

External parameters can be used anywhere literal values are allowed, including column selection and the WHERE clause.

**Examples**

_Using parameters in WHERE clause:_

In the following query:

```sql
SELECT * FROM connection.operation
WHERE input1 = @myParam
```

The value of the parameter `myParam` will be passed to `input1`.

_Using parameters with string concatenation:_

Because parameters get replaced with their value at runtime, they can be used in binary expressions. In the following query, if `myParam` is a string, it can be used in string concatenation:

```sql
SELECT * FROM connection.operation
WHERE input1 = 'foo ' + @myParam
```

_Using parameters in a JSON template:_

The following query again shows a parameter being used in a binary expression, but this time in column selection:

```sql
SELECT { foo: @myParam + 1 }
```

### Keywords and escaping

Transposit has a number of keywords and reserved words in SQL. In order to use a reserved word as an identifier in a query, it is necessary to escape it using backticks: 
```
`<keyword>`
```

Escaping is necessary when the identifier is used in many parts of the query, including column selection, WHERE clauses, and EXPAND BY. However, it is not necessary to escape operation names or external variables.

**Examples**

In these examples, we will use the reserved word "values" to demonstrate when it is necessary to escape identifiers.

_Keywords in column selection_

It is necessary to escape column names in the SELECT clause.

```sql
SELECT `values` FROM connection.operation
```

_Keywords in the WHERE clause_

It is necessary to escape column names on both sides of a condition in a WHERE clause.

```sql
SELECT * FROM connection.operation
WHERE `values`=foo
```

```sql
SELECT * FROM connection.operation
WHERE foo=`values`
```

However, it is not necessary if the keyword is part of a longer path.

```sql
SELECT * FROM connection.operation
WHERE foo=path.to.values
```

_Keywords in the EXPAND BY clause_

It is necessary to escape column names in the EXPAND BY clause.

```sql
SELECT * FROM connection.operation
EXPAND BY `values`
```

Like with the WHERE clause, it is not necessary to escape if part of a longer path.

```sql
SELECT * FROM connection.operation
EXPAND BY path.to.values
```

_Keywords in the connection or operation name_

It is not necessary to escape keywords in the connection name.

```sql
SELECT * FROM values.operation
```

Similarly, it is not necessary to escape keywords in the operation name.

```sql
SELECT * FROM connection.values
```

_Keywords in external parameters_

It is not necessary to escape external parameters, as they are already denoted by the @ symbol.

```sql
SELECT * FROM connection.operation
WHERE foo=@values
```

_Keywords in literal strings_

It is not necessary to escape keywords when they are used in a string literal.

```sql
SELECT * FROM connection.operation
WHERE foo='values'
```

### Comments

Transposit supports block comments using `/* */` or single line comments using the `--` prefix.

**Examples**

_Line comment_

```sql
SELECT *  -- the rest of the line is a comment
FROM connection.operation
WHERE foo=bar
```

_Block comment_

```sql
SELECT * /* 
 everything in here is a comment 
*/ FROM connection.operation
WHERE foo=bar
```

### Pagination and streaming

Transposit automatically paginates many APIs (see the [FAQ](/docs/references/faq#automatic-pagination)). This feature is deeply integrated with our SQL engine, allowing a query to dynamically pull more results from data connectors until it has reached the desired limit.

For example, if we have the following query:
```sql
SELECT * FROM connection.operation LIMIT 10
```
Assume `operation` is paginated and has a parameter called `pageSize` to control the number of results from the API. In this case, Transposit is smart enough to set the `pageSize` to 10 based on the desired limit.

This is easy for a simple query, but imagine a more complex query that filters the results of the API:
```sql
SELECT * FROM connection.operation
WHERE foo='bar'
LIMIT 10
```
The where clause may filter out some of the results of the API call, leaving us with fewer than ten results. When this happens, the query will iterate and fetch the next page of results from the API. This continues until the query has accumulated ten total results, or the API indicates it is done paginating.

The value that gets passed to the paginated operation is determined by the limit and may propagate to subqueries. For instance,
```sql
SELECT * FROM
  (SELECT * FROM connection.operation)
LIMIT 10
```
Even though there is no explicit limit in the inner query, the limit of 10 from the outer query is passed down to the subquery and ultimately to the paginated operation.

If the subquery does have an explicit limit, the minimum of the two limits is used. For instance,
```sql
SELECT * FROM
  (SELECT * FROM connection.operation LIMIT 8)
LIMIT 10
```
In this case, the limit passed to `connection.operation`'s `pageSize` parameter is 8.

## INSERT, UPDATE and DELETE Statements

In Transposit when you use SQL to execute operations we use SELECT for all queries. This can be a little confusing when the underlying operation modifies or deletes data. Rather than trying to guess the most natural command, we picked SELECT — but provide a helpful conversion from other commands if you happen to try one. SQL is a powerful language for working with APIs, but the concepts don’t always mesh cleanly. SELECT provides a simple mapping on APIs and allows for powerful use of JOIN syntax, not typically available for other SQL commands.

Additional notes:

* What about mapping HTTP methods to SQL commands? When you think about SQL and APIs it’s tempting to draw a relationship between SQL commands and API HTTP methods: GET is a natural match for SELECT; DELETE for DELETE. POST is probably closest to INSERT and PATCH and PUT map to UPDATE. This demonstrates the first obvious problem: HTTP methods are not always used consistently and what makes sense to the API vendor might surprise the API consumer (and us too!). We might reasonably expect to see a PUT as an INSERT or a POST as an UPDATE. Some APIs use POST to fetch data, a situation where you might expect to use SELECT. There’s no translation that’s obviously right for all APIs and in all circumstances.
* In the same way that you execute API requests from SQL operations, you can also execute other Transposit operations, and these other operations can execute different APIs based on custom logic — for example, an operation can create or update an item based on an input parameter or based on another API call — and therefore Transposit operations are not mapped to individual HTTP methods.
