---
description: >-
  Reference for JavaScript syntax supported in the Transposit editor, return
  formats, and example code.
---

# JavaScript operations

### `api.run(operation, [params={}], [options={}])`

Runs an operation.

| Argument | Type |  |
| :--- | :--- | :--- |
| operation | String | the name of the operation to be run |
| \[params={}\] | Object | an object containing any operation-defined parameters |
| \[options={}\] | Object | additional options - `limit`: limits the number of results returned. Infinity if undefined. |

**Returns** \(Array\): Returns the operation results or throws any operation failure.

**Example**

```javascript
api.run("this.helloworld");
// => [{"Hello": "World"}]

api.run("source.users", { id: params.userId });
// => [{id:1234, ...}]

api.run("connection.many_results", {}, {limit: 10});
// => returns result array of size 10
```

### `api.query(query, [params={}])`

Run a SQL query

| Argument | Type |  |
| :--- | :--- | :--- |
| query | String | The SQL query to be run |
| \[params={}\] | Object | an object containing any operation-defined parameters |

**Returns** \(Array\): Returns the query results or throws any query failure.

**Example**

```javascript
api.query("select * from this.helloworld")
// => [{"Hello": "World"}]

api.query("select * from source.users where id=@userId", {userId: params.userId});
// => [{id:1234, ...}]
```

### `api.user()`

Get the logged-in user information

**Returns** \(Object\): An object that includes the user's `fullName` and `email`

**Example**

```javascript
api.user()
// => {"fullName":"iggy","email":"iggy@transposit.com"}
```

### `api.log([objects])`

Logs to the console.

| Argument | Type |  |
| :--- | :--- | :--- |
| \[objects\] | String or Object | One or more objects or strings to log. Objects are automatically serialized. |

**Returns** null

**Example**

```javascript
api.log("logging the following greeting:", {"Hello", "World"})
// => logging the following greeting: { Hello: World }
```

## Available JavaScript Libraries

Transposit provides you access to a few different popular JavaScript libraries.

* [qs \(v6.5.2\)](https://github.com/ljharb/qs)
* [underscore](https://underscorejs.org/)
* [jsonpath](https://github.com/dchester/jsonpath)
* [moment](https://momentjs.com/timezone/)
* [moment-timezone](https://momentjs.com/timezone/)
* [moment-timezone-with-data](https://momentjs.com/timezone/)

Example usage:

```javascript
var qs = require('qs.js');
var limited = qs.parse('a=b&c=d', { parameterLimit: 1 });
```

```javascript
var moment = require('moment-timezone-with-data.js');
var jun = moment("2014-06-01T12:00:00Z");
api.log(jun.clone().tz('America/New_York').format('ha z')); // 8am EDT
```

