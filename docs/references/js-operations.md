---
id: js-operations
title: JavaScript operations
---

### `api.run(operation, [parameters={}], [options={}])`

Runs an operation.

| Argument | Type |  |
| :--- | :--- | :--- |
| operation | String | the name of the operation to be run |
| [parameters={}] | Object | an object containing any operation-defined parameters |
| [options={}] | Object | additional options - `limit`: limits the number of results returned. Infinity if undefined. |

**Returns** (Array): Returns the operation results or throws any operation failure.

**Example**

```javascript
api.run("this.helloworld");
// => [{"Hello": "World"}]

api.run("source.users", { id: params.userId });
// => [{id:1234, ...}]

api.run("connection.many_results", {}, {limit: 10});
// => returns result array of size 10
```

### `api.runBulk(operations)`

Runs any number of operations in parallel and waits for all to complete, or any to fail, before returning.

| Argument | Type |  |
| :--- | :--- | :--- |
| operations | Array<Object> | an array of descriptor objects, each describing one of the operations to run in parallel |
  
Each descriptor object has the following properties:

| Field | Type |  |
| :--- | :--- | :--- |
| operation | String | the name of the operation to be run |
| [parameters={}] | Object | an object containing any operation-defined parameters |
| [options={}] | Object | additional options - `limit`: limits the number of results returned. Infinity if undefined. |

**Returns** (Array): Returns an array where each element is the result set from one of the parallel operations. If any fail, the error is thrown.

**Example**

```javascript
var results = api.runBulk([{
  operation: "this.helloworld"
}, {
  operation: "source.users",
  parameters: { id: params.userId }
}, {
  operation: "connection.many_results",
  options: { limit: 10 }
}]);

results[0] // => [{"Hello": "World"}]
results[1] // => [{id:1234, ...}]
results[2] // => result array of size 10
```

### `api.query(query, [parameters={}])`

Run a SQL query

| Argument | Type |  |
| :--- | :--- | :--- |
| query | String | The SQL query to be run |
| [parameters={}] | Object | an object containing any operation-defined parameters |

**Returns** (Array): Returns the query results or throws any query failure.

**Example**

```javascript
api.query("select * from this.helloworld")
// => [{"Hello": "World"}]

api.query("select * from source.users where id=@userId", {userId: params.userId});
// => [{id:1234, ...}]
```

### `api.user()`

Get the logged-in user information

**Returns** (Object): An object that includes the user's `fullName` and `email`

**Example**

```javascript
api.user()
// => {"fullName":"iggy","email":"iggy@transposit.com"}
```

### `api.log([objects])`

Prints to the debug tab. `console.log()` can also be used.

| Argument | Type |  |
| :--- | :--- | :--- |
| [objects] | String or Object | One or more objects or strings to log. Objects are automatically serialized. |

**Returns** null

**Example**

```javascript
api.log("logging the following greeting:", {"Hello", "World"})
// => logging the following greeting: { Hello: World }
```

## Available JavaScript Libraries

Transposit provides you access to a few different popular JavaScript libraries.

* [qs (v6.5.2)](https://github.com/ljharb/qs)
```javascript
var qs = require('qs.js');
var limited = qs.parse('a=b&c=d', { parameterLimit: 1 });
```

* [underscore](https://underscorejs.org/)
```javascript
var _ = require('underscore.js');
return _.map([1, 2, 3], function(num){ return num * 3; });
```

* [moment](https://momentjs.com/timezone/)
* [moment-timezone](https://momentjs.com/timezone/)
* [moment-timezone-with-data](https://momentjs.com/timezone/)
```javascript
var moment = require('moment-timezone-with-data.js');
var jun = moment("2014-06-01T12:00:00Z");
api.log(jun.clone().tz('America/New_York').format('ha z')); // 8am EDT
```

* [mustache](https://github.com/janl/mustache.js)
```javascript
var mustache = require('mustache.js');
var view = {
  title: "Joe",
  calc: function () {
    return 2 + 4;
  }
};
var output = mustache.render("{{title}} spends {{calc}}", view);
```

* [jsonpath](https://github.com/dchester/jsonpath)
* [crypto-js](https://github.com/brix/crypto-js)
```javascript
const CryptoJS = require("crypto-js");
const parsedWordArray = CryptoJS.enc.Base64.parse(params.str);
const decoded = parsedWordArray.toString(CryptoJS.enc.Utf8);
return decoded;
```
