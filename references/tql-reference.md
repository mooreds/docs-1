# TQL Reference

## Terms and symbols

TODO - table/service, column/field, <>, data source, results JSON object
TODO: string quotes, identifier (and escaping), immediate value

## Select statement

TODO: general description - manipulation of list of json objects, etc...

Select statement syntax:

```
SELECT <* or columns selection or JSON template>
FROM <table or subquery or join>
WHERE <one or more expressions>
EXPAND BY <columns>
LIMIT <number>
```

The `SELECT` clause is required.<br/>
The clauses `WHERE`, `EXPAND BY` and `LIMIT` can be used only if `FROM` clause is used.

The clauses must appear in the order that was specific above.

### Order of execution

1.  `FROM`
2.  `WHERE`
3.  `EXPAND BY`
4.  `LIMIT`
5.  `SELECT`

### Select clause

The `SELECT` clause is used for manipulating the structure and values of each item in the 'data source'.

The `SELECT` clause gets as input a JSON object or JSON array from the 'data source' and produce a JSON object or a JSON array.

The `SELECT` clause supports three to ways to manipulate an item:

- [Select star](#select-star)
- [Columns selection](#columns-selection)
- [JSON template](#json-template)

#### Select star

The `*` symbol will keep the items from 'data source' without changes:

```
SELECT *
FROM source.service
```

#### Columns selection

Columns selection can be used to construct a JSON object with specific keys that will appear in the top level of the object.

Columns selection cannot construct a nested JSON object or a JSON array, to construct such items use [JSON template](#json-template).

The syntax for columns selection is:

```
SELECT <column-expression> AS <column-alias>, <column-expression> AS <column-alias>, ...
```

`<column-expression>` describes how to construct a value in the output JSON object and can be one of the following:

- `<path>`
- `<path>`.\*
- `<table-alias>`.`<path>`
- `<table-alias>`.`<path>`.\*
- `<immediate-value>`
- `<binary-expression>`

`<path>` describes a nested location of a value inside a JSON object or a JSON array and can be one of the following:

- `<key>`
- `<path>`.`<key>`

(TODO: need to update this when we support bracket syntax (TR-1540))

`<key>` is an identifier.

`<table-alias>` is an identifier.

`<immediate-value>` is a number, string or boolean value.

`<binary-expression>` describe basic math operation (for numbers) or string concatenation (of strings) and can be one of the following:

- `<column-expression>` + `<column-expression>`
- `<column-expression>` - `<column-expression>`
- `<column-expression>` \* `<column-expression>`
- `<column-expression>` / `<column-expression>`

`AS <column-alias>` is optional. `<column-alias>` is an identifier.

##### Object construction

Columns selection construct a JSON object for each item in the 'data source' based on the specified `<column-expression>`s and `<column-alias>`s.

The `<column-expression>`s and `<column-alias>`s are used in the same order as they appear in the query.

Each `<column-expression>` will be calculated and resolved. The output can be immediate value (number, string or boolean), JSON object or JSON array.<br/>

For `<path>` the resolve process will do a lookup for each `<key>` in the current location in the JSON object. The final value that was found will be used as the resolved value.<br>
If a `<key>` is being resolved but the current item is not a JSON object, the resolve will stop and the `<path>` will be considered as 'not found'.
If a `<key>` is being resolved and the current item is a JSON object that doesn't contain the same key, the resolve will stop and the `<path>` will be considered as 'not found'.

For `<path>`.\* - TODO

For `<table-alias>`.`<path>` - TODO

For `<table-alias>`.`<path>`.\* - TODO

For `<binary-expression>` the resolve process will deconstruct the expression and will resolved each part and then will reconstruct the resolved parts to produce immediate value.

For each one we will do a lookup in the current item from the 'data source', if the `<path>` was found we will add the matching value to the results JSON object. If 'column alias' was specified we will use that as the key of the value, otherwise we will use the last `<component>` of the `<path>` as the key.

If the same key is used more than once the last value will be used and will override the previous value.

If the value of a `<path>` is `null` or does not exists we will not add it to the results JSON object.

##### Examples:

_Selecting a single value:_

```
SELECT col1
FROM source.service
```

Will generate a JSON object with a single key:

```
[
  {
    "col1": ...
  },
  ...
]
```

_Selecting multiple values:_

```
SELECT col1, col2, col3
FROM source.service
```

Will generate a JSON object with multiple keys:

```
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

To access a value inside a nested object you can use a `.` (dot) as separator between the nested object keys.

For example, if the 'data source' is in the format:

```
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

```
SELECT nested.object.value
FROM source.service
```

Will generate a JSON object with the key and value of the item in the specific path:

```
[
  {
    "value": ...
  },
  ...
]
```

TODO - examples for `<path>`.\*, table alias, immediate value, binary expression

#### JSON template

JSON template is a more generic way to construct a JSON object or a JSON array as the results item.

To construct a JSON object use the syntax:

```
SELECT { <key>: <json-value>, ... }
```

To construct a JSON array use the syntax:

```
SELECT [ <json-value>, ... ]
```

In both cases, `<json-value>` can be one of the following:

- `<json-object>` - construct a nested object
- `<json-array>` - construct a nested array
- `<expression>` - a calculated expression
- `<path>` - a column selection
- `<immediate-value>` - number, string or boolean

`<key>` is a \_\_\_, for convenience JSON template doesn't require to use string quotes around the key but it should be used if the `<key>` contains spaces or other illegal characters.

TODO - spread, table alias

#### Immediate values

TODO - select without FROM

### From clause

#### Select from table/service

TODO - table/service, sub query, table alias, join (with/without input params, AND/OR)

### Where clause

TODO - filters, input params, $body, AND/OR, IN, subquery, expressions

### Expand by clause

TODO - column, nested path, alias, multiple columns

### Limit clause

TODO

### Expressions

TODO (maybe this is not needed and we will talk about expressions in the relevant sections)

## Insert statement

TODO

## Update statement

TODO

## Delete statement

TODO

## External parameters

TODO (@userId)

## Escaping

TODO - list of keywords, valid/invalid characters, how to escape
