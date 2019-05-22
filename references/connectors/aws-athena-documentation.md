---
id: aws-athena-documentation
title: AWS Athena (version v1.*.*)
sidebar_label: AWS Athena
layout: docs.mustache
---

## batch_get_named_query

Returns the details of a single named query or a list of up to 50 queries, which you provide as an array of query ID strings. Requires you to have access to the workgroup in which the queries were saved. Use ListNamedQueriesInput to get the list of named query IDs in the specified workgroup. If information could not be retrieved for a submitted query ID, information about the query ID submitted is listed under UnprocessedNamedQueryId. Named queries differ from executed queries. Use BatchGetQueryExecutionInput to get details about each unique query execution, and ListQueryExecutionsInput to get a list of query execution IDs.  https://docs.aws.amazon.com/athena/latest/APIReference/API_BatchGetNamedQuery.html

<details><summary>Parameters</summary>

#### NamedQueryIds (required)

An array of query IDs.

**Type:** ARRAY

</details>

## batch_get_query_execution

Returns the details of a single query execution or a list of up to 50 query executions, which you provide as an array of query execution ID strings. Requires you to have access to the workgroup in which the queries ran. To get a list of query execution IDs, use ListQueryExecutions:WorkGroup. Query executions differ from named (saved) queries. Use BatchGetNamedQueryInput to get details about named queries.  https://docs.aws.amazon.com/athena/latest/APIReference/API_BatchGetQueryExecution.html

<details><summary>Parameters</summary>

#### QueryExecutionIds (required)

An array of query execution IDs.

**Type:** ARRAY

</details>

## create_named_query

Creates a named query in the specified workgroup. Requires that you have access to the workgroup.  https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateNamedQuery.html

<details><summary>Parameters</summary>

#### ClientRequestToken (required)

A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another CreateNamedQuery request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the QueryString, an error is returned. Important This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.

**Type:** STRING

#### Database (required)

The database to which the query belongs.

**Type:** STRING

#### Name (required)

The query name.

**Type:** STRING

#### QueryString (required)

The contents of the query with all query statements.

**Type:** STRING

#### Description

The query description.

**Type:** STRING

#### WorkGroup

The name of the workgroup in which the named query is being created.

**Type:** STRING

</details>

## create_workgroup

Creates a workgroup with the specified name. https://docs.aws.amazon.com/athena/latest/APIReference/API_CreateWorkGroup.html

<details><summary>Parameters</summary>

#### Name (required)

The workgroup name.

**Type:** STRING

#### Configuration

The configuration for the workgroup, which includes the location in Amazon S3  where query results are stored, the encryption configuration, if any, used for encrypting query results,  whether the Amazon CloudWatch Metrics are enabled for the workgroup,   the limit for the amount of bytes scanned (cutoff) per query, if it is specified, and whether workgroup's settings (specified with EnforceWorkGroupConfiguration) in the WorkGroupConfiguration override client-side settings.  See WorkGroupConfiguration:EnforceWorkGroupConfiguration.

**Type:** OBJECT

#### Description

The workgroup description.

**Type:** STRING

#### Tags

One or more tags, separated by commas, that you want to attach to the workgroup as you create it.

**Type:** ARRAY

</details>

## delete_named_query

Deletes the named query if you have access to the workgroup in which the query was saved.  https://docs.aws.amazon.com/athena/latest/APIReference/API_DeleteNamedQuery.html

<details><summary>Parameters</summary>

#### NamedQueryId (required)

The unique ID of the query to delete.

**Type:** STRING

</details>

## delete_workgroup

Deletes the workgroup with the specified name. The primary workgroup cannot be deleted. https://docs.aws.amazon.com/athena/latest/APIReference/API_DeleteWorkGroup.html

<details><summary>Parameters</summary>

#### WorkGroup (required)

The unique name of the workgroup to delete.

**Type:** STRING

#### RecursiveDeleteOption

The option to delete the workgroup and its contents even if the workgroup contains any named queries.

**Type:** BOOLEAN

</details>

## get_named_query

Returns information about a single query. Requires that you have access to the workgroup in which the query was saved.  https://docs.aws.amazon.com/athena/latest/APIReference/API_GetNamedQuery.html

<details><summary>Parameters</summary>

#### NamedQueryId (required)

The unique ID of the query. Use ListNamedQueries to get query IDs.

**Type:** STRING

</details>

## get_query_execution

Returns information about a single execution of a query if you have access to the workgroup in which the query ran. Each time a query executes, information about the query execution is saved with a unique ID.  https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryExecution.html

<details><summary>Parameters</summary>

#### QueryExecutionId (required)

The unique ID of the query execution.

**Type:** STRING

</details>

## get_query_results

Returns the results of a single query execution specified by QueryExecutionId if you have access to the workgroup in which the query ran. This request does not execute the query but returns results. Use StartQueryExecution to run a query.  https://docs.aws.amazon.com/athena/latest/APIReference/API_GetQueryResults.html

<details><summary>Parameters</summary>

#### QueryExecutionId (required)

The unique ID of the query execution.

**Type:** STRING

</details>

## get_workgroup

Returns information about the workgroup with the specified name. https://docs.aws.amazon.com/athena/latest/APIReference/API_GetWorkGroup.html

<details><summary>Parameters</summary>

#### WorkGroup (required)

The name of the workgroup.

**Type:** STRING

</details>

## list_named_queries

Provides a list of available query IDs only for queries saved in the specified workgroup. Requires that you have access to the workgroup.  https://docs.aws.amazon.com/athena/latest/APIReference/API_ListNamedQueries.html

<details><summary>Parameters</summary>

#### WorkGroup

The name of the workgroup from which the named queries are being returned.

**Type:** STRING

</details>

## list_query_executions

Provides a list of available query execution IDs for the queries in the specified workgroup. Requires you to have access to the workgroup in which the queries ran.  https://docs.aws.amazon.com/athena/latest/APIReference/API_ListQueryExecutions.html

<details><summary>Parameters</summary>

#### WorkGroup

The name of the workgroup from which queries are being returned.

**Type:** STRING

</details>

## list_tags_for_resource

Lists the tags associated with this workgroup. https://docs.aws.amazon.com/athena/latest/APIReference/API_ListTagsForResource.html

<details><summary>Parameters</summary>

#### ResourceARN (required)

Lists the tags for the workgroup resource with the specified ARN.

**Type:** STRING

</details>

## list_workgroups

Lists available workgroups for the account. https://docs.aws.amazon.com/athena/latest/APIReference/API_ListWorkGroups.html

*This operation has no parameters*

## start_query_execution

Runs the SQL query statements contained in the Query. Requires you to have access to the workgroup in which the query ran.  https://docs.aws.amazon.com/athena/latest/APIReference/API_StartQueryExecution.html

<details><summary>Parameters</summary>

#### QueryString (required)

The SQL query statements to be executed.

**Type:** STRING

#### ClientRequestToken

A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another StartQueryExecution request is received, the same response is returned and another query is not created. If a parameter has changed, for example, the QueryString, an error is returned. Important This token is listed as not required because AWS SDKs (for example the AWS SDK for Java) auto-generate the token for users. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the action will fail.

**Type:** STRING

#### QueryExecutionContext

The database within which the query executes.

**Type:** OBJECT

#### ResultConfiguration

Specifies information about where and how to save the results of the query execution. If the query runs in a workgroup, then workgroup's settings may override query settings. This affects the query results location. The workgroup settings override is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration.  See WorkGroupConfiguration:EnforceWorkGroupConfiguration.

**Type:** OBJECT

#### WorkGroup

The name of the workgroup in which the query is being started.

**Type:** STRING

</details>

## stop_query_execution

Stops a query execution. Requires you to have access to the workgroup in which the query ran.  https://docs.aws.amazon.com/athena/latest/APIReference/API_StopQueryExecution.html

<details><summary>Parameters</summary>

#### QueryExecutionId (required)

The unique ID of the query execution to stop.

**Type:** STRING

</details>

## tag_resource

Adds one or more tags to the resource, such as a workgroup. A tag is a label that you assign to an AWS Athena resource (a workgroup). Each tag consists of a key and an optional value, both of which you define. Tags enable you to categorize resources (workgroups) in Athena, for example, by purpose, owner, or environment. Use a consistent set of tag keys to make it easier to search and filter workgroups in your account. For best practices, see AWS Tagging Strategies. The key length is from 1 (minimum) to 128 (maximum) Unicode characters in UTF-8. The tag value length is from 0 (minimum) to 256 (maximum) Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys and values are case-sensitive. Tag keys must be unique per resource. If you specify more than one, separate them by commas.  https://docs.aws.amazon.com/athena/latest/APIReference/API_TagResource.html

<details><summary>Parameters</summary>

#### ResourceARN (required)

Requests that one or more tags are added to the resource (such as a workgroup) for the specified ARN.

**Type:** STRING

#### Tags (required)

One or more tags, separated by commas, to be added to the resource, such as a workgroup.

**Type:** ARRAY

</details>

## untag_resource

Removes one or more tags from the workgroup resource. Takes as an input a list of TagKey Strings separated by commas, and removes their tags at the same time.  https://docs.aws.amazon.com/athena/latest/APIReference/API_UntagResource.html

<details><summary>Parameters</summary>

#### ResourceARN (required)

Removes one or more tags from the workgroup resource for the specified ARN.

**Type:** STRING

#### TagKeys (required)

Removes the tags associated with one or more tag keys from the workgroup resource.

**Type:** ARRAY

</details>

## update_workgroup

Updates the workgroup with the specified name. The workgroup's name cannot be changed. https://docs.aws.amazon.com/athena/latest/APIReference/API_UpdateWorkGroup.html

<details><summary>Parameters</summary>

#### WorkGroup (required)

The specified workgroup that will be updated.

**Type:** STRING

#### ConfigurationUpdates

The workgroup configuration that will be updated for the given workgroup.

**Type:** OBJECT

#### Description

The workgroup description.

**Type:** STRING

#### State

The workgroup state that will be updated for the given workgroup.

**Type:** STRING

</details>

