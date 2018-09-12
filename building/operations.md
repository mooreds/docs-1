# Building operations

Operations are callable units of work. Operations can be written in [JavaScript](/references/js-operations.md) or [SQL](/references/sql-operations.md), and they may be private (e.g. used only for development, or called by other operations within the application), [scheduled for periodic execution](/building/scheduled-tasks.md), or deployed as [endpoints](/building/endpoints.md).

## SQL Operations

A primary use of SQL operations is querying data. Here's an example of a basic `SELECT` statement:

```sql
SELECT * FROM database.get_users WHERE lastName='smith' LIMIT 50
```

Data can be joined, as you'd expect in SQL:

```sql
SELECT * FROM database.get_users AS A JOIN database.get_user as B ON A.id = B.id WHERE A.lastName='smith' LIMIT 50
```

Creating SQL operations from a template (choose **SQL from template** in the menu) starts you off with scaffolded code based on the syntax and parameters of a given data connection operation.

{% page-ref page="references/sql-operations.md" %}

## JavaScript Operations

JavaScript operations are useful for manipulating data or encoding business logic, and can themselves run queries.

A basic example of a JavaScript operation:

```javascript
function run(params) {
  api.log("hello world");
  return {
    "mission": "complete"
};
}
```
To run another operation from inside a JavaScript operation, use the `run` method. The first argument is the operation reference; the second argument is a map of operation parameters to run with:

```JavaScript
api.run("connector.operation", {});
```

To run a SQL statement inside a JavaScript operation, use the `query` method:

```JavaScript
api.query("select * from connector.operation");
```

To print to the console, use the `log` method; `log` accepts any number of arguments:

```JavaScript
api.log("hello world");
```

{% page-ref page="references/js-operations.md" %}

## Smart Operations

@tina @thea — TODO
