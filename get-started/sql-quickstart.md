# SQL quickstart

This walkthrough gives you a brief introduction to the power of SQL and Transposit's relational engine. We will cover a number of topics, but please go to the [SQL operation reference](https://github.com/transposit/docs/tree/858f21e930dcd3fb82dc32880087431acd81a13c/get-started/TODO/README.md) to view the full power of how you can use SQL in Transposit.

### Prerequisites

* A Gmail account
* You've done the [Transposit Quickstart](https://github.com/transposit/docs/tree/858f21e930dcd3fb82dc32880087431acd81a13c/get-started/TODO/README.md)

### Setup

* Create a new blank application in Transposit
* Add the google\_mail data connector

### Understanding operations

You can use the documentation tab in the bottom half of the code console. If you navigate to google_mail -&gt; getmessages, you'll notice a few things. First off the required userId parameter has a special value **me** indicating the authenticated user. Secondly, next to the operation name, there is a \_\_pagination_ flag. This flag indicates that you can ask Transposit to automatically paginate for you. More on this in a bit.

### SQL select statements

Let's query google mail for your 10 most recent messages.

* Create a new SQL operation from template and select get\_messages
* For the required userId let's set it to be `me`
* You can remove or comment out the other optional parameters. We support SQL style comments `/* */` or line comments prefixed by `--`.
* With paginated operations, you should always specify a LIMIT or else we will continue to fetch more results until we either run out of results or hit our [rate limit](https://github.com/transposit/docs/tree/858f21e930dcd3fb82dc32880087431acd81a13c/get-started/%20Link%20to%20the%20FAQ%20about%20rate%20limits/README.md).

Your SQL should look like the following:

```text
SELECT * FROM google_mail.get_messages
  WHERE userId='me'
  LIMIT 10
```

* Click the run button to run your operation

You should see a number of results that look like the following:

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

In addition to passing parameters to an operation through the WHERE clause, you can also filter your results. Try the following, but be sure to reduce the LIMIT or else we will keep on fetching until we hit our rate limit if you don't have enough messages in the given thread.

```text
SELECT * FROM google_mail.get_messages
  WHERE userId='me' AND threadId='THREAD_ID_FROM_PREVIOUS_RUN'
  LIMIT 1
```

### Parameters

One of the challenges of working with APIs is that often times you need to combine data across multiple APIs in order to make use of them. In this case, we need to do a separate API call to retrieve any useful information about the email messages.

Let's create an operation that takes a message id and returns the

* Create a new SQL operation from template, but this time select the get\_message template
* In the right hand column, create a new parameter and name it `messageId`. You can now reference this parameter in the SQL with `@messageId`.
* Set the userId to be `me`, the id to use `@messageId` and remove the optional parameters. Your SQL should look like the following:

  ```text
  SELECT * FROM google_mail.get_message
  WHERE id=@messageId
  AND userId='me'
  ```

* To test it, grab one of the IDs from the previous request above, set it as the messageId in the parameters panel, and run the operation. You should see a result similar to:

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

### Column selection and json templating

Similar to SQL, you can easily select individual columns.

To limit the results to the id and the snippet, try modifying your SQL to the following:

```text
SELECT id, snippet FROM google_mail.get_message
  WHERE id=@messageId
  AND userId='me'
```

One of the additions we've made to SQL is what we call json templating. You can use it to rename variables, do some string concatenation, etc. Please visit [the reference](https://github.com/transposit/docs/tree/858f21e930dcd3fb82dc32880087431acd81a13c/get-started/%20link%20to%20SQL%20ref%20at%20the%20json%20templating%20section/README.md) for more information, but to give you a flavor of what you can do, try modifying your SQL to the following:

```text
SELECT {id: id, message: 'gmail created snippet: ' + snippet} FROM google_mail.get_message
  WHERE id=@messageId
  AND userId='me'
```

### Joins

Transposit makes it easy to join data across APIs in a single data source as well as different data sources. The basic form of a SQL join is as follows:

```text
SELECT *
  FROM connector.operation_1 AS <operation-alias-1>
  JOIN connector.operation_2 AS <operation-alias-2>
  ON <predicate>
```

Let's use a join to combine the two operations we've created so we can get the snippet for your first 10 messages.

* Create a new blank SQL operation
* Use a join to combine the two operations you've created. Remember, you can reference operations in your current application using the `this` syntax. Your SQL should look like:

```text
SELECT *
  FROM this.get_messages_1 AS LIST
  JOIN this.get_message_1 AS DETAIL
  ON LIST.id = DETAIL.messageId
  LIMIT 10
```

