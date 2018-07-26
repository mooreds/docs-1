# TQL Reference

## Terms and symbols

TODO - table/service, column/field, <>, [], data source, results JSON object
TODO: string quotes

## Select

TODO: general description - manipulation of list of json objects, etc...

Select statement syntax:

```
SELECT <* or columns selection or JSON template>
FROM <table or subquery or join>
WHERE <one or more expressions>
EXPAND BY <columns>
LIMIT <number>
```

The `SELECT` clause is the only required clause.<br/>
The clauses `WHERE`, `EXPAND BY` and `LIMIT` can be used only if `FROM` clause is used.

The clauses must appear in the order that was specific above.

### Select

The `SELECT` clause support three types of selections:

- [Select star](#select-star)
- [Columns selection](#columns-selection)
- [JSON template](#json-template)

#### Select star

If you want to keep the 'data source' as-is, you can use the `*` symbol:

```
SELECT *
FROM source.service
```

Will not modify the results from `source.service`

#### Columns selection

Columns selection can be used to construct a results JSON object with specific keys that will appear in the top level of the object.

The syntax for columns selection is:

```
SELECT <path> [AS <alias_name>] [, <path> [AS <alias_name>] ...]
```

`<path>` is composed of one or more `<component>`s that describe the location of the key inside the source JSON object. Each `component` is separated with a `.` (dot).

`<component>` is a string (TODO: add the valid characters). If the `<component>` is a keyword or contains spaces or other illegal characters, the `<component>` or the entire `<path>` can be escaped (see [Escaping](#escaping) section)

(TODO: need to update this when we support bracket syntax (TR-1540))

`AS <alias_name>` is optional, in columns selection this alias is called 'column alias'.

TODO: describe - `nested.object.*`

TODO: describe expression

TODO: table alias

##### Object construction

Columns selection construct a JSON object for each item in the 'data source' based on the specified `<path>`s and column aliases.

The `<path>`s and column aliases are used in the same order as they appear in the query.
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

### From

#### Select from table/service

TODO - table/service, sub query, table alias, join (with/without input params, AND/OR)

### Where

TODO - filters, input params, $body, AND/OR, IN, subquery, expressions

### Expand by

TODO - column, nested path, alias, multiple columns

### Limit

TODO

### Expressions

TODO (maybe this is not needed and we will talk about expressions in the relevant sections)

## Insert

TODO

## Update

TODO

## Delete

TODO

## External parameters

TODO (@userId)

## Escaping

TODO - list of keywords, valid/invalid characters, how to escape
