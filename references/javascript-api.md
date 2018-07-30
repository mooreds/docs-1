# JavaScript API


## Available JavaScript Libraries
Transposit provides you access to a few different popular JavaScript libraries.
- [qs (v6.5.2)](https://github.com/ljharb/qs)
- [underscore](https://underscorejs.org/)
- [jsonpath](https://github.com/dchester/jsonpath)
- [moment](https://momentjs.com/timezone/)
- [moment-timezone](https://momentjs.com/timezone/)
- [moment-timezone-with-data](https://momentjs.com/timezone/)

Example usage:
```
var qs = require('qs.js');
var limited = qs.parse('a=b&c=d', { parameterLimit: 1 });
```

```
var moment = require('moment-timezone-with-data.js');
var jun = moment("2014-06-01T12:00:00Z");
api.log(jun.clone().tz('America/New_York').format('ha z')); // 8am EDT
```
