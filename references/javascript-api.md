# JavaScript API


## Available JavaScript Libraries
Transposit provides you access to a few different popular JavaScript libraries.
- [qs (v6.5.2)](https://github.com/ljharb/qs)
- [underscore](https://underscorejs.org/)
- [jsonpath](https://github.com/dchester/jsonpath)

Example usage:
```
var qs = require('qs.js');
var limited = qs.parse('a=b&c=d', { parameterLimit: 1 });
```
