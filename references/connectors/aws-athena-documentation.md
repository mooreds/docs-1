---
id: aws-athena-documentation
title: AWS Athena (version v2.*.*)
sidebar_label: AWS Athena
layout: docs.mustache
---

## batch_get_named_query

Returns the details of a single named query or a list of up to 50 queries, which you provide as an array of query ID strings. Use ListNamedQueries to get the list of named query IDs. If information could not be retrieved for a submitted query ID, information about the query ID submitted is listed under UnprocessedNamedQueryId. Named queries are different from executed queries. Use BatchGetQueryExecution to get details about each unique query execution, and ListQueryExecutions to get a list of query execution IDs.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## batch_get_query_execution

Returns the details of a single query execution or a list of up to 50 query executions, which you provide as an array of query execution ID strings. To get a list of query execution IDs, use ListQueryExecutions. Query executions are different from named (saved) queries. Use BatchGetNamedQuery to get details about named queries.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_named_query

Creates a named query. 
For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_named_query

Deletes a named query. 
For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_named_query

Returns information about a single query.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_query_execution

Returns information about a single execution of a query. Each time a query executes, information about the query execution is saved with a unique ID.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_query_results

Returns the results of a single query execution specified by QueryExecutionId. This request does not execute the query but returns results. Use StartQueryExecution to run a query.

<details><summary>Parameters</summary>

#### $body

**Type:** object

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

#### $body

**Type:** object

</details>

## stop_query_execution

Stops a query execution. 
For code samples using the AWS SDK for Java, see Examples and Code Samples in the Amazon Athena User Guide.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

