---
id: sql-quickstart
title: SQL Quickstart
layout: docs.mustache
---

This walkthrough provides an introduction to the power of SQL and Transposit's relational engine. It covers a number of topics, but please see the [SQL operation reference](/docs/references/sql-operations) for a full view of how you can use SQL in Transposit.

## Get set up

* You'll need a Slack account for the steps in this guide.
* Make sure you've gone through the [Quickstart](/docs/get-started/quickstart).
* Create a new application in Transposit, and add the **Slack** data connection with operation `list_conversations`.
* Click through and add Slack credentials. Note that if desired, you can adjust the permissions scope by clicking on the Slack connector you just added, then clicking **Configuration > Edit** and entering `channels:history channels:read` in the Scope field. (If you change the scope after you have authorized, you'll want to delete your key and authorize again).

## Understanding operations

You can use the documentation tab in the bottom half of the code console. If you browse to **Slack > list_conversations**, you'll see documentation for the operation and its parameters. Notice that next to the operation name, there is a _pagination_ flag. This flag indicates that Transposit will automatically paginate the API for you. More on this in a bit.

## SELECT statements

Let's query Slack for 10 of your channels.

* Navigate to your `list_conversations` operation.
* The parameters for this operation are optional. If you didn't want to use them, you could delete or comment them out. Transposit supports SQL style comments `/* */` or line comments prefixed by `--`.
* With paginated operations, you should always specify a `LIMIT` or Transposit will continue to fetch more results until it either runs out of results or hits the [rate limit](/docs/references/faq).

Let's fetch a few public, non-archived channels. Your SQL should look like the following:

```sql
SELECT * FROM slack.list_conversations
  WHERE types='public_channel'
  AND exclude_archived=true
  LIMIT 10
```

Click the **Run** button to run your operation. You should see a number of results that look like the following:

```json
[
  {
    "id": "C262LCPME",
    "name": "general",
    "is_channel": true,
    "is_group": false,
    "is_im": false,
    "created": 1472492750,
    "is_archived": false,
    "is_general": true,
    "unlinked": 0,
    "name_normalized": "general",
    "is_shared": false,
    "parent_conversation": null,
    "creator": "U2615V61Z",
    "is_ext_shared": false,
    "is_org_shared": false,
    "shared_team_ids": [
      "T2615V5UK"
    ]
  }
  ...
]
```
(For some reason the Slack API often returns one less than the limit specified)

## Filtering results

In addition to passing parameters to an operation through the `WHERE` clause, you can also filter results. Try the following (you may need to use a different value depending on the size of your Slack org):

```sql
SELECT * FROM slack.list_conversations
  WHERE types='public_channel'
  AND exclude_archived=true
  AND num_members < 20
  LIMIT 10
```

## Parameters

One of the challenges of working with APIs is that we often need to combine data across multiple APIs in order to make use of them. In this case, we need to do a separate API call to retrieve any messages for our Slack channels.

Let's create an operation that takes a channel id and returns the details for that channel.

* Create a new SQL operation, selecting the `get_channels_history` operation.
* In the right side of the editor, create a new parameter and name it `channelId`. You can now reference this parameter in the SQL with `@channelId`.
* Set the value of `channel` to be `@channelId` and remove the optional parameters. Your SQL should look like the following:

```sql
SELECT * FROM slack.get_channels_history
  WHERE channel=@channelId
  LIMIT 10
```

To test it, grab one of the IDs from the previous request above, set it as the `channelId` in the parameters panel, and run the operation. You should see a result similar to:

```json
[
  {
    "client_msg_id": "e97092af-540c-496f-b471-b51ba8fde632",
    "type": "message",
    "text": "Hello world!",
    "user": "U27R7G7HD",
    "ts": "1553104938.072400",
    "reactions": [
      {
        "name": "wave",
        "users": [
          "UGH99TGBZ",
          "UH3H388DV"
        ],
        "count": 2
      }]
      ...
  }
]
```

## Column selection and JSON templating

Similar to SQL, you can easily select individual columns.

To limit the results to the timestamp and messages, try modifying your SQL to the following:

```sql
SELECT ts, text FROM slack.get_channels_history
  WHERE channel=@channelId
  LIMIT 10
```

One of the additions we've made to SQL is what we call JSON templating, which you can use to rename variables, concatenate strings, and so forth. Try modifying your SQL to the following:

```sql
SELECT {timestamp: "time: " + ts, last_message: text} FROM slack.get_channels_history
  WHERE channel=@channelId
  LIMIT 1
```

## Joins

Transposit makes it easy to join data across APIs in a single data source as well as different data sources. The basic form of a SQL join is:

```sql
SELECT *
  FROM connection.operation_1 AS <operation-alias-1>
  JOIN connection.operation_2 AS <operation-alias-2>
  ON <predicate>
```

Let's use a join to combine the two operations we've created so we can get the last message for each of your Slack channels.
* Create a new blank SQL operation. In the data connection picker, there's an option for `None (blank, no templated code)`.
* Use a `JOIN` to combine the two operations you've created. You can reference operations in your current application using the `this` syntax.

Your SQL should look like:

```sql
 SELECT name, last_message
  FROM this.list_conversations AS LIST
  JOIN this.get_channels_history AS DETAIL
  ON LIST.id = DETAIL.channelId
```

For a closer look at using SQL in Transposit, see the [SQL reference](/docs/references/sql-operations). 
