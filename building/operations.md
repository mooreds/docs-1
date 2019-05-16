---
id: operations
title: SQL & JavaScript operations
layout: docs.mustache
---

Operations are callable units of work. Operations can be written in [JavaScript](/docs/references/js-operations) or [SQL](/docs/references/sql-operations), and they may be private (e.g. used only for development, or called by other operations within the application), [scheduled for periodic execution](/docs/building/scheduled-tasks), or deployed as [endpoints](/docs/building/endpoints). Here's a quick look at why Transposit supports SQL, when to use JavaScript instead, and basic usage examples for each.

## Why use SQL?

We believe SQL is the most efficient way of exploring and transforming your application data.

SQL is designed to easily join, filter, and organize your data in the way you need it. It abstracts away the details of data representation and allows you, the developer, to express your intent, while the relational engine translates that intent, optimizes it, and executes it. In this way, SQL offers a simpler way of stating this intent than you would ever get writing your own custom code.

SQL is also a standard language familiar to many developers. Its simplicity and power means it’s the best database technology a majority of the time.

Additionally, you don’t need to be a SQL expert to use and take full advantage of Transposit&mdash; knowing how to write a select, join, and where clause is all you need in most cases. If you ever need to do something more advanced, just take a look in our [SQL reference](/docs/references/sql-operations) or [get support from our team](mailto:support@transposit.com).

## Why use JavaScript?

Our execution engine also supports JavaScript, so you can use both SQL and JavaScript for what they’re best at. When you’re looking to make complicated data manipulations that would be awkward and hard to debug with SQL, you can fall back to JavaScript. This is helpful when you need to write additional business logic or quickly transform the data resulting from one of your SQL queries.

## SQL Operations

A primary use of SQL operations is querying data. Here's an example of a basic `SELECT` statement:

```sql
SELECT * FROM database.get_users WHERE lastName='smith' LIMIT 50
```

Data can be joined, as you'd expect in SQL:

```sql
SELECT * FROM database.get_users
AS A JOIN database.get_user as B ON A.id = B.id
WHERE A.lastName='smith' LIMIT 50
```

Creating SQL operations from a template (choose **SQL from template** in the menu) starts you off with scaffolded code based on the syntax and parameters of a given data connection operation.

Learn more in the [SQL operations reference](/docs/references/sql-operations).

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

```javascript
api.run("connection.operation", {});
```

To run a SQL statement inside a JavaScript operation, use the `query` method:

```javascript
api.query("select * from connection.operation");
```

To print to the console, use `console.log`, which accepts any number of arguments:

```javascript
console.log("hello world");
```

Learn more in the [JavaScript operations reference](/docs/references/js-operations).

## Usage limits for operations

Transposit enforces usage limits on your operations. This helps to protect our infrastructure as well as your API rate limits.

### Memory

* Each request is given a quota of 1 GB of memory allocated
* This is not configurable by the developer

### Cpu time

* Each request is given a quota of 1 minute of cpu time
* This is not configurable by the developer

### API call limits

To make sure you don't accidentally run through your API rate limits for your data connections, Transposit limits the number of API calls.
* By default, the limit is 500 per data connection per request.
* This can be changed for a particular data connector by the data connector's author.
* This can be further overridden in your application in the settings for the data connection. Navigate to **Data connection > Configure**, and edit the value under **Max API calls**.
