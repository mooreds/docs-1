# SQL quickstart

This walkthrough provides an introduction to the power of SQL and Transposit's relational engine. It covers a number of topics, but please see to the [SQL operation reference](references/sql-operations.md) for a full view of how you can use SQL in Transposit.

## Get set up

* You'll need a a Gmail account for the steps in this guide.
* Make sure you've gone through the [Quickstart](get-started/quickstart.md).
* Create a new application in Transposit, and add the **google_mail** data connector.

## Understanding operations

You can use the documentation tab in the bottom half of the code console. If you browse to **google_mail > get_messages**, you'll notice a few things. First, the required `userId` parameter has a special value `me`, indicating the current authenticated user. Second, next to the operation name, there is a _pagination_ flag. This flag indicates that you can ask Transposit to automatically paginate for you. More on this in a bit.

## SQL select statements

Let's query Gmail for your 10 most recent messages.

* Create a new SQL operation from template and select `get_messages`.
* For the required userId, set it `me`.
* You can remove or comment out the other optional parameters. We support SQL style comments `/* */` or line comments prefixed by `--`.
* With paginated operations, you should always specify a `LIMIT` or Transposit will continue to fetch more results until it either runs out of results or hits the [rate limit](references/faq.md).

Your SQL should look like the following:

```sql
SELECT * FROM google_mail.get_messages
  WHERE userId='me'
  LIMIT 10
```

Click the **Run** button to run your operation. You should see a number of results that look like the following:

```text
[
  {
    "id": "165ca58935a38c30",
    "threadId": "165ca4b175ba5be5"
  },
  {
    "id": "165ca5311c9d0730",
    "threadId": "165ca5311c9d0730"
  },
  ...
]
```

## Filtering results

In addition to passing parameters to an operation through the `WHERE` clause, you can also filter results. Try the following, but be sure to reduce the `LIMIT` or else Transposit will keep fetching until the rate limit is hit if you don't have enough messages in the given thread.

```sql
SELECT * FROM google_mail.get_messages
  WHERE userId='me' AND threadId='THREAD_ID_FROM_PREVIOUS_RUN'
  LIMIT 1
```

## Parameters

One of the challenges of working with APIs is that you often need to combine data across multiple APIs in order to make use of them. In this case, we need to do a separate API call to retrieve any useful information about the email messages.

Let's create an operation that takes a message id and returns the ???

* Create a new SQL operation from template, but this time select the `get_message` template.
* In the right side of the editor, create a new parameter and name it `messageId`. You can now reference this parameter in the SQL with `@messageId`.
* Set the `userId` to `me`, the `id` to use `@messageId` and remove the optional parameters. Your SQL should look like the following:

  ```sql
  SELECT * FROM google_mail.get_message
  WHERE id=@messageId
  AND userId='me'
  ```

To test it, grab one of the IDs from the previous request above, set it as the `messageId` in the parameters panel, and run the operation. You should see a result similar to:

  ```text
  [
  {
    "id": "165caab0c1a7c2c2",
    "threadId": "165c97321cbdb7cb",
    "labelIds": [
      "INBOX"
    ],
    "snippet": "Transposit makes APIs fun!",
    "historyId": "17433647",
    ...
  }
  ]
  ```

## Column selection and JSON templating

Similar to SQL, you can easily select individual columns.

To limit the results to the ID and the snippet, try modifying your SQL to the following:

```sql
SELECT id, snippet FROM google_mail.get_message
  WHERE id=@messageId
  AND userId='me'
```

One of the additions we've made to SQL is what we call JSON templating. You can use it to rename variables, do some string concatenation, etc. Please see [the SQL reference](references/sql-operations.md) for more information, but to give you a flavor of what you can do, try modifying your SQL to the following:

```sql
SELECT {id: id, message: 'gmail created snippet: ' + snippet} FROM google_mail.get_message
  WHERE id=@messageId
  AND userId='me'
```

## Joins

Transposit makes it easy to join data across APIs in a single data source as well as different data sources. The basic form of a SQL join is:

```sql
SELECT *
  FROM connector.operation_1 AS <operation-alias-1>
  JOIN connector.operation_2 AS <operation-alias-2>
  ON <predicate>
```

Let's use a join to combine the two operations we've created so we can get the snippet for your first 10 messages.

* Create a new blank SQL operation.
* Use a join to combine the two operations you've created. You can reference operations in your current application using the `this` syntax.

Your SQL should look like:

```sql
SELECT *
  FROM this.get_messages_1 AS LIST
  JOIN this.get_message_1 AS DETAIL
  ON LIST.id = DETAIL.messageId
  LIMIT 10
```

