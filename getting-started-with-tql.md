# Using SQL in Transposit

### The basics {#GettingStartedwithTQL-Thebasics}

Basic TQL select:

```sql
select * from slack_channels.channelslist
```

To simplify the following, let's assume you set the above to be a TQL operation called "getChannels". You can now filter columns and rows with something like the following:

```sql
select id, channel from this.getChannels where name='build'
```

You can parameterize your TQL like the following:

```sql
select id, channel from this.getChannels where name=@name
```

### Expand by

Expand by syntax can be used to expand arrays. It is not standard SQL, but can be very useful when working with JSON data.

Let's say you're working with data of the form:

```sql
[{ id: 1, vals: [1, 2] }, { id: 2, vals: [3, 4] }]\
```

You can expand the values with:

```sql
select * from this.sampleValues expand by vals
```

which results in:

```sql
[{ id: 1, vals: 1 }, { id: 1, vals: 2 }, { id: 2, vals: 3 }, { id: 2, vals: 4 }]
```

Expand by also supports expanding by multiple paths, nested paths, and aliasing. For example, let's say your data looks like:

```sql
[{ id: 1,
   vals: [1, 2],
   nested: {
     moreVals: ["a", "b"]
   }
}, ...]
```

You can write:

```sql
select * from this.sampleValues expand by vals as foo, nested.moreVals
```

Which results in:

```sql
[
  {
    "id": 1,
    "vals": [1, 2],
    "nested": {
      "moreVals": "a"
    },
    "foo": 1
  },
  {
    "id": 1,
    "vals": [1, 2],
    "nested": {
      "moreVals": "b"
    },
    "foo": 1
  },
  {
    "id": 1,
    "vals": [1, 2],
    "nested": {
      "moreVals": "a"
    },
    "foo": 2
  },
  {
    "id": 1,
    "vals": [1, 2],
    "nested": {
      "moreVals": "b"
    },
    "foo": 2
  }
]
```

### Advanced column selection

Basic math operations, string concatenation, and variables can all be used in column selection. Continuing with the sample data from above, 

| `select nested.moreVals, id * 4 / 2, 'hello ' + 'world' from this.sampleValues` |
| --- |


Which results in output like:

| `[  {    "moreVals": [      "a",      "b"    ],    "id*4/2": 2,    "'hello '+'world'": "hello world"  },  {    "moreVals": [      "c",      "d"    ],    "id*4/2": 4,    "'hello '+'world'": "hello world"  }]` |
| --- |


Note that the name of the column is generated from the text of the selector when using this syntax. Also note that the selector "nested.moreVals" maps to the column name "moreVals" in the output. That is, it is moved to the top level of the results and is no longer nested. One consequence of this is that "select bar, foo.bar from ..." will conflict (last one wins). Here you are encouraged to alias the columns to avoid any conflicts.

An alternative to column selection is to use the JSON templating syntax to build your columns:

| `select {  nested: {    moreVals: nested.moreVals  },  foo: [id * 4` `/ 2, 'hello '` `+ 'world']} from this.sampleValues` |
| --- |


Which results in:

| `[  {    "nested": {      "moreVals": [        "a",        "b"      ]    },    "foo": [      2,      "hello world"    ]  },  {    "nested": {      "moreVals": [        "c",        "d"      ]    },    "foo": [      4,      "hello world"    ]  }]` |
| --- |


Note that you can arbitrarily nest objects and arrays with this syntax, making it the most flexible option for column selection.

Warning: there is a subtle difference between a result set and a JSON array. For instance,

| `select * from mytable.op where id in (select [1, 2, 3])` |
| --- |


will result in `mytable.op` getting called once, where `id` is passed an array with the value `[1, 2, 3]`. Contrast this with the use of tuples:

| `select * from mytable.op where id in (1, 2, 3)` |
| --- |


This results in `mytable.op` getting called three times, with `id` getting passed one of the integers from the tuple. 

functions.flatten (deprecated)

Before expand by and JSON templating were introduced, the best way to achieve this functionality was to add the transposit/functions application.

Notice that that returns a nested JSON that contains the list of channels. To flatten, call functions.flatten (which uses the JSON path syntax):

| `select * from functions.flatten where input=(select * from slack_channels.channelslist) and cols='[{"path": "$.channels.*", "alias": "*"}]'` |
| --- |


  
You can also pass an item from the top level into each item. For example, the following will pass the "ok" status from the parent to each item as "status":

| `select * from functions.flatten where input=(select * from slack_channels.channelslist) and cols='[{"path": "$.channels.*", "alias": "*"}, {"path": "$.ok", "alias": "status"}]'` |
| --- |


### Joins {#GettingStartedwithTQL-Joins}

The current join syntax looks something like the following:

| `select * from slack_channels.channelshistory where channel in (select id join * as channel_info from this.getChannels where name='build')` |
| --- |


Note that plans are in the works to implement a more standard SQL join, at which point the current syntax will be removed.  
  


