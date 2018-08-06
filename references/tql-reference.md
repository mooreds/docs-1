# SQL reference

## Terms and symbols

TODO - table/service, column/field, &lt;&gt;, data source, results JSON object TODO: string quotes, identifier \(and escaping\), immediate value

## Select statement

TODO: general description - manipulation of list of json objects, etc...

Select statement syntax:

```text
SELECT <* or columns selection or JSON template>
FROM <table or subquery or join>
WHERE <one or more expressions>
EXPAND BY <columns>
LIMIT <number>
```

The `SELECT` clause is required.  
 The clauses `WHERE`, `EXPAND BY` and `LIMIT` can be used only if `FROM` clause is used.

The clauses must appear in the order that was specific above.

### Order of execution

1.  `FROM`
2.  `WHERE`
3.  `EXPAND BY`
4.  `LIMIT`
5.  `SELECT`

### Select clause

The `SELECT` clause can be used for manipulating the structure and values of each item in the 'data source'.

The `SELECT` clause gets as input a JSON object or JSON array from the 'data source' and produce a JSON object or a JSON array.

The `SELECT` clause supports three to ways to manipulate an item:

- [Select star](tql-reference.md#select-star)
- [Columns selection](tql-reference.md#columns-selection)
- [JSON template](tql-reference.md#json-template)

#### Select star

The `*` symbol will keep the items from 'data source' without changes:

```text
SELECT *
FROM source.service
```

#### Columns selection

Columns selection can be used to construct a JSON object with specific keys that will appear in the top level of the object.

Columns selection cannot construct a nested JSON object or a JSON array, to construct these items use [JSON template](tql-reference.md#json-template).

The syntax for columns selection is:

```text
SELECT <column-expression> AS <column-alias>, <column-expression> AS <column-alias>, ...
```

`<column-expression>` describes how to construct a value in the output JSON object and can be one of the following:

- `<path>`
- `<table-alias>.<path>`
- `<immediate-value>`
- `<binary-expression>`

`<path>` describes the location of a value inside a JSON object or a JSON array. `<path>` contains one or more keys/field names that describe the lookup chain of fields inside the input JSON object - each `<key>` gets the inner JSON object/array and the lookup continues from that JSON object/array. The last item in `<path>` can be `.*`.

`<path>` can be one of the following:

- `<key>`
- `<key-1>.<key-2>.` ... `<key-N>`
- `<key>.*`
- `<key-1>.<key-2>.` ... `<key-N>.*`

\(TODO: need to update this when we support bracket syntax \(TR-1540\)\)

`<key>` is an identifier.

`<table-alias>` is an identifier.

`<immediate-value>` is a number, string or boolean value.

`<binary-expression>` describe basic math operation \(for numbers\) or string concatenation \(of strings\) and can be one of the following:

- `<column-expression>` + `<column-expression>`
- `<column-expression>` - `<column-expression>`
- `<column-expression>` \* `<column-expression>`
- `<column-expression>` / `<column-expression>`

`AS <column-alias>` is optional. `<column-alias>` is an identifier.

**Object construction**

Columns selection construct a JSON object for each item in the 'data source' based on the specified `<column-expression>`s and `<column-alias>`s.

The `<column-expression>`s and `<column-alias>`s are used in the same order as they appear in the query.

Each `<column-expression>` will be calculated and resolved. The resolved value can be immediate value \(number, string or boolean\), JSON object or JSON array.

For `<path>` the resolve process will do a lookup for each `<key>` in the current location in the JSON object. The value that is found will be used as the resolved value. if `<path>` ends with `.*` - the value will be all the fields that were found under the last `<key>`  
 If a `<key>` is being resolved but the current item is not a JSON object, the resolve will stop and the value will be considered as 'not found'.  
 If a `<key>` is being resolved and the current item is a JSON object that doesn't contain the same key, the resolve will stop and the value will be considered as 'not found'.

For `<table-alias>.<path>` - the resolve process will resolve the specified `<path>` only under the results from the table that was marked with the specified alias.  
 If no table was marked with `<table-alias>` the resolve will stop and the value will be considered as 'not found'.

For `<binary-expression>` the resolve process will deconstruct the expression and will resolved each part and then will reconstruct the resolved parts to produce immediate value.  
 If the types of the operands is not the same the resolve process will produce an error and the entire query will fail.  
 If the types of the operands is string, only the `+` operator is allowed, if a different operator is use the resolve process will produce an error and the entire query will fail.

If the resolve process found a valid value, this value will be added to the output JSON object with a key, the key is selected in the following way:

- If `<column-alias>` is specified it will be used as the key.
- If `<column-expression>` is `<path>` that does not ends with `.*` - the last `<key>` will be used as the key.
- If `<column-expression>` is `<path>` that ends with `.*` - the key and values under the last `<key>` will be used without change.
- Otherwise the entire `<column-expression>` will be used as the key. It's recommended to use `<column-alias>` in this case.

If the same key is used more than once the last value will be used and will override any previous values that had the same key.

If the value is resolved to `null` or 'not found' this value will not be added it to the output JSON object.

**Examples:**

_Selecting a single value:_

```text
SELECT col1
FROM source.service
```

Will generate a JSON object with a single key:

```text
[
  {
    "col1": ...
  },
  ...
]
```

_Selecting multiple values:_

```text
SELECT col1, col2, col3
FROM source.service
```

Will generate a JSON object with multiple keys:

```text
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

```text
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

```text
SELECT nested.object.value
FROM source.service
```

Will generate a JSON object with the key and value of the item in the specific path:

```text
[
  {
    "value": ...
  },
  ...
]
```

_Selecting all values under a nested object:_

To access all values inside a nested object you can use a `.*` in the end of the path that contains the values.

If the 'data source' is in the format:

```text
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

```text
SELECT nested.object.*
FROM source.service
```

Will generate a JSON object with the all the keys and values in the specific path:

```text
[
  {
    "value1": ...,
    "value2": ...,
    "value3": ...
  },
  ...
]
```

_Using table alias:_

When a table is marked with alias \(see [table alias](tql-reference.md#table-alias)\) the same table alias can be used as a qualifier in the beginning of the path to define exactly where to do the lookup for the path \(the results of which table to use\). This is useful when the query contains more than one table \(for example in [join query](tql-reference.md#join-query)\).

```text
SELECT T.col1
FROM source.service AS T
```

Will generate a JSON object with a single key:

```text
[
  {
    "col1": ...
  },
  ...
]
```

_Immediate value:_

Any value of the types number, string or boolean can be used as an immediate value.

```text
select 7 as value1, 'seven' as value2, true as value3
```

Will generate:

```text
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

```text
select (20 + 3) * 2 as value
```

Will generate:

```text
[
  {
    "value": 46
  }
]
```

With columns:

```text
select (col1 + 10) * nested.object.value1 as value
FROM source.service
```

Will use the values of `col1` and `nested.object.value1` to calculate the value of the expression.

#### JSON template

JSON template is a more generic way to construct a JSON object or a JSON array as the output item.

To construct a JSON object use the syntax:

```text
SELECT { <key>: <json-value>, ... }
```

To construct a JSON array use the syntax:

```text
SELECT [ <json-value>, ... ]
```

`<key>` is an identifier. For convenience JSON template doesn't require to use string quotes around the key but it should be used if the `<key>` contains spaces, illegal characters or keywords.

`<json-value>` can be one of the following:

- `<path>` - a column selection
- `<table-alias>.<path>` - a column selection with table alias qualifier
- `<immediate-value>` - number, string or boolean
- `<binary-expression>` - a calculated expression
- `<json-object>` - construct a nested object
- `<json-array>` - construct a nested array

`<path>`, `<table-alias>.<path>`, `<immediate-value>` and `<binary-expression>` are the same as in [columns selection](tql-reference.md#columns-selection). The only difference is that `.*` in the end of `<path>` is not allowed in JSON template, use [spread operator](tql-reference.md#spread-operator) instead.

`<json-object>` constructs a JSON object, the syntax is:

```text
{ <key-1>: <json-value-1>, <key-2>: <json-value-2>, ... <key-N>: <json-value-N> }
```

`<json-array>` constructs a JSON array, the syntax is:

```text
[ <json-value-1>,  <json-value-2>, ... <json-value-N>]
```

**Spread operator**

The spread operator expands a JSON object into JSON object or JSON array into a JSON array \(similar to `<path>.*` in [columns selection](tql-reference.md#columns-selection)\).

The spread JSON object use:

```text
SELECT { ... obj }
```

The spread JSON array use:

```text
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

`<path>`, `<table-alias>.<path>`, `<immediate-value>` and `<binary-expression>` are resolved the same as in [columns selection](tql-reference.md#columns-selection).

`<json-object>` and `<json-array>` are resolved recursively.

If the resolve process found a valid value, this value will be added to the output JSON object or array. If the output item is a JSON object the specified `<key>` will be used.

If the same key is used more than once the last value will be used and will override any previous values that had the same key.

If the value is resolved to `null` or 'not found':

- If the output item is JSON object this value will not be added it to the output item.
- if the output item is JSON array this value will be added it to the output item as `null`.

**Examples**

TODO - add examples for JSON template

#### Immediate values

TODO - select without FROM

### From clause

#### Select from table/service

TODO - table/service, sub query, table alias, join \(with/without input params, AND/OR\)

### Where clause

TODO - filters, input params, $body, AND/OR, IN, subquery, expressions

### Expand by clause

TODO - column, nested path, alias, multiple columns

### Limit clause

TODO

### Expressions

TODO \(maybe this is not needed and we will talk about expressions in the relevant sections\)

## External parameters

TODO \(@userId\)

## Escaping

TODO - list of keywords, valid/invalid characters, how to escape

```text

```
