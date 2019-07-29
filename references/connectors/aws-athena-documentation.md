---
id: aws-athena-documentation
title: AWS Athena (version v2.*.*)
sidebar_label: AWS Athena
layout: docs.mustache
---

## batch_get_named_query

Returns the details of a single named query or a list of up to 50 queries, which you provide as an array of query ID strings. Use ListNamedQueries to get the list of named query IDs. If information could not be retrieved for a submitted query ID, information about the query ID submitted is listed under UnprocessedNamedQueryId. Named queries are different from executed queries. Use BatchGetQueryExecution to get details about each unique query execution, and ListQueryExecutions to get a list of query execution IDs.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NamedQueryIds" : [ "string" ]
}
```

</details>

## batch_get_query_execution

Returns the details of a single query execution or a list of up to 50 query executions, which you provide as an array of query execution ID strings. To get a list of query execution IDs, use ListQueryExecutions. Query executions are different from named (saved) queries. Use BatchGetNamedQuery to get details about named queries.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "QueryExecutionIds" : [ "string" ]
}
```

</details>

## create_named_query

Creates a named query. 
For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ClientRequestToken" : "A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another CreateNamedQuery request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the QueryString, an error is returned.  \nThis token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.",
  "Description" : "A brief explanation of the query.",
  "QueryString" : "The text of the query itself. In other words, all query statements.",
  "Database" : "The database to which the query belongs.",
  "Name" : "The plain language name for the query."
}
```

</details>

## delete_named_query

Deletes a named query. 
For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NamedQueryId" : "The unique ID of the query to delete."
}
```

</details>

## get_named_query

Returns information about a single query.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NamedQueryId" : "The unique ID of the query. Use ListNamedQueries to get query IDs."
}
```

</details>

## get_query_execution

Returns information about a single execution of a query. Each time a query executes, information about the query execution is saved with a unique ID.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "QueryExecutionId" : "The unique ID of the query execution."
}
```

</details>

## get_query_results

Returns the results of a single query execution specified by QueryExecutionId. This request does not execute the query but returns results. Use StartQueryExecution to run a query.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "QueryExecutionId" : "The unique ID of the query execution."
}
```

</details>

## list_named_queries

Provides a list of all available query IDs. 
For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide.

*This operation has no parameters*

## list_query_executions

Provides a list of all available query execution IDs. 
For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide.

*This operation has no parameters*

## start_query_execution

Runs (executes) the SQL query statements contained in the Query string. 
For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ClientRequestToken" : "A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another StartQueryExecution request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the QueryString, an error is returned.  \nThis token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.",
  "ResultConfiguration" : {
    "EncryptionConfiguration" : {
      "EncryptionOption" : "Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (SSE-S3), server-side encryption with KMS-managed keys (SSE-KMS), or client-side encryption with KMS-managed keys (CSE-KMS) is used.",
      "KmsKey" : "For SSE-KMS and CSE-KMS, this is the KMS key ARN or ID."
    },
    "OutputLocation" : "The location in Amazon S3 where your query results are stored, such as s3://path/to/query/bucket/. For more information, see Queries and Query Result Files.  "
  },
  "QueryExecutionContext" : {
    "Database" : "The name of the database."
  },
  "QueryString" : "The SQL query statements to be executed."
}
```

</details>

## stop_query_execution

Stops a query execution. 
For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "QueryExecutionId" : "The unique ID of the query execution to stop."
}
```

</details>

