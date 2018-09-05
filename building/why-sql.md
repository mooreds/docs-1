# Query across all your data

The goal of Transposit is to make building API-driven applications as easy as if all your data were in a single, relational database. You authenticate with the data connections you want, and Transposit presents each of those as a virtual table \(to do: as if it were in a relational db\) that you interact with using **SQL** \(or JavaScript\). You can start invoking and exploring APIs within seconds--we’ve dealt with all the authentication, boilerplate and overhead. In Transposit, you build your application backend by transforming and composing data to create new APIs that Transposit hosts and scales for you.

### Why SQL?

We believe SQL is the most efficient way of exploring and transforming your application data.

SQL is designed to easily join, filter, and organize your data in the way you need it. It abstracts away the details of data representation and allows you, the developer, to express your intent, while the relational engine translates that intent, optimizes it, and executes it. You can now focus on what you want to do with your core app data, not on how.

SQL offers a simpler way of stating this intent than you would ever get writing your own custom code. \[example of a SQL query that shows off the simplicity here?\]

SQL is a standard language familiar to many developers, and we believe it’s here to stay. Its simplicity and power means it’s the best database technology a majority of the time, which counts for a lot in a ecosystem where new tools are appearing faster than you can learn to use them.

Finally, you don’t need to be a SQL expert to use and take full advantage of Transposit -- knowing how to write a select, join, and where clause is all you need in most cases. If you ever need to do something more advanced, just take a look in our \[SQL reference\] or \[get support from our team\].

### **The power of the Transposit relational engine**

Transposit gives you the ability to simply write SQL queries to transform and explore your data, as if each data connection you authenticate is a virtual table in a relational database containing all your app data. In order to make this work under the hood, we’be built Transposit to know how to securely communicate with APIs, optimize performance around network calls, and account for the unreliable nature of modern APIs.

Here are some of the tasks Transposit deals with, so you don’t have to:

* **Authentication**
* **Caching**
* **Rate-limiting**
* **Retries**
* **Pagination**

To demonstrate how much time and complexity Transposit’s relational engine saves you, let’s compare how you might perform a generic \[task\] in your app with two data sources, both with and without Transposit.

Imagine you are trying to use the Google Sheets and Twitter APIs to get a list of tweets with more than 3 retweets from a set of Twitter profiles stored in a Google sheet, with a limit of 1,000 results..  


With Transposit, you could simple write a SQL query to get these results, without worrying about managing authentication, pagination, retries, or anything other than what you are looking for:  


`SELECT * from sheets.get_items as A JOIN twitter.get_status as B on A.col = B.status_id WHERE retweet_count > 3 LIMIT 1000`

If you were writing custom code to handle this same query without Transposit, it would look something like this:

1. `Grab the first page of twitter handles from the spreadsheet`
2. `For each of those handles, grab the first page of statuses from their twitter account (N lists)`
3. `Filter those lists for those tweets that have a retweet count > 3`
4. `If you still don’t have 1000 tweets, then grab the next page of handles from the spreadsheet`
5. `Repeat from 2`
6. `When you run out of pages from the spreadsheet, then go back to the first set of handles (step 2) and grab the second page of statuses from each of those handles,`
7. `Repeat 3 - 6`

This example is complicated enough, but still doesn’t account for time spent managing authentication and retries, securely handling this data, and a lot more. On top of that, you’d have to entirely replicate your code every time you want to perform this task in another app. In Transposit, you’d instead….

### **JavaScript when you need it**

Our execution engine also supports JavaScript, so you can use both SQL and JavaScript for what they’re best at. When you’re looking to make complicated data manipulations that would be awkward and hard to debug with SQL, you can fall back to the JavaScript you’re likely more familiar with. This will be helpful when you need to write additional business logic or quickly transform \(eg string manipulation\) the data resulting from one of your SQL queries.  


Here’s an example of how you might use JavaScript with a SQL query in Transposit:

```text
function(params) {
  Return api.query(‘SELECT * FROM twitter.get_statuses’).map(
function(item) {
  Return (‘this is a ‘: item.message);
})
}
```

### **Using SQL in Transposit**

To learn more about using SQL in Transposit and the syntax we support, we recommend you try out our \[Getting started tutorial\]. If you want to skip straight to the nitty-gritty, check out our SQL reference docs:

{% page-ref page="../transposit-101/getting-started-with-tql.md" %}

{% page-ref page="../references/tql-reference.md" %}



