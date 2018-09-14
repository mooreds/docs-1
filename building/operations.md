# SQL & JavaScript operations

Operations are callable units of work. Operations can be written in [JavaScript](../references/js-operations.md) or [SQL](../references/sql-operations.md), and they may be private \(e.g. used only for development, or called by other operations within the application\), [scheduled for periodic execution](scheduled-tasks.md), or deployed as [endpoints](endpoints.md). Here's a quick look at why Transposit supports SQL, when to use JavaScript instead, and basic usage examples for each. 

## Why use SQL?

We believe SQL is the most efficient way of exploring and transforming your application data.

SQL is designed to easily join, filter, and organize your data in the way you need it. It abstracts away the details of data representation and allows you, the developer, to express your intent, while the relational engine translates that intent, optimizes it, and executes it. In this way, SQL offers a simpler way of stating this intent than you would ever get writing your own custom code.

SQL is also a standard language familiar to many developers. Its simplicity and power means it’s the best database technology a majority of the time.

Finally, you don’t need to be a SQL expert to use and take full advantage of Transposit -- knowing how to write a select, join, and where clause is all you need in most cases. If you ever need to do something more advanced, just take a look in our [SQL reference](../references/sql-operations.md) or [get support from our team](mailto:support@transposit.com).

## Why use JavaScript?

Our execution engine also supports JavaScript, so you can use both SQL and JavaScript for what they’re best at. When you’re looking to make complicated data manipulations that would be awkward and hard to debug with SQL, you can fall back to the JavaScript you’re likely more familiar with. This will be helpful when you need to write additional business logic or quickly transform \(e.g. string manipulation\) the data resulting from one of your SQL queries.

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

Creating SQL operations from a template \(choose **SQL from template** in the menu\) starts you off with scaffolded code based on the syntax and parameters of a given data connection operation.

Learn more in the SQL operations reference:

{% page-ref page="../references/sql-operations.md" %}

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
api.run("connector.operation", {});
```

To run a SQL statement inside a JavaScript operation, use the `query` method:

```javascript
api.query("select * from connector.operation");
```

To print to the console, use the `log` method; `log` accepts any number of arguments:

```javascript
api.log("hello world");
```

Learn more in the JavaScript operations reference:

{% page-ref page="../references/js-operations.md" %}

