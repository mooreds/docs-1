---
id: gcp-bigquery-documentation
title: GCP BigQuery (version v1.*.*)
sidebar_label: GCP BigQuery
layout: docs.mustache
---

## cancel_job

Requests that a job be cancelled. This call will return immediately, and the client will need to poll for the job status to see if the cancel completed successfully. Cancelled jobs may still incur costs.

<details><summary>Parameters</summary>

#### jobId (required)

[Required] Job ID of the job to cancel

**Type:** string

#### projectId (required)

[Required] Project ID of the job to cancel

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### location

The geographic location of the job. Required except for US and EU. See details at https://cloud.google.com/bigquery/docs/locations#specifying_your_location.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_dataset

Creates a new empty dataset.

<details><summary>Parameters</summary>

#### projectId (required)

Project ID of the new dataset

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_table

Creates a new, empty table in the dataset.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the new table

**Type:** string

#### projectId (required)

Project ID of the new table

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_dataset

Deletes the dataset specified by the datasetId value. Before you can delete a dataset, you must delete all its tables, either manually or by specifying deleteContents. Immediately after deletion, you can create another dataset with the same name.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of dataset being deleted

**Type:** string

#### projectId (required)

Project ID of the dataset being deleted

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### deleteContents

If True, delete all the tables in the dataset. If False and the dataset contains tables, the request will fail. Default is False

**Type:** boolean

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_table

Deletes the table specified by tableId from the dataset. If the table contains data, all the data will be deleted.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the table to delete

**Type:** string

#### projectId (required)

Project ID of the table to delete

**Type:** string

#### tableId (required)

Table ID of the table to delete

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## execute_query

Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout.

<details><summary>Parameters</summary>

#### projectId (required)

Project ID of the project billed for the query

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_dataset

Returns the dataset specified by datasetID.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the requested dataset

**Type:** string

#### projectId (required)

Project ID of the requested dataset

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_job

Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role.

<details><summary>Parameters</summary>

#### jobId (required)

[Required] Job ID of the requested job

**Type:** string

#### projectId (required)

[Required] Project ID of the requested job

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### location

The geographic location of the job. Required except for US and EU. See details at https://cloud.google.com/bigquery/docs/locations#specifying_your_location.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_query_results

Retrieves the results of a query job.

<details><summary>Parameters</summary>

#### jobId (required)

[Required] Job ID of the query job

**Type:** string

#### projectId (required)

[Required] Project ID of the query job

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### location

The geographic location where the job should run. Required except for US and EU. See details at https://cloud.google.com/bigquery/docs/locations#specifying_your_location.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### startIndex

Zero-based index of the starting row

**Type:** string

#### timeoutMs

How long to wait for the query to complete, in milliseconds, before returning. Default is 10 seconds. If the timeout passes before the job completes, the 'jobComplete' field in the response will be false

**Type:** integer

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_service_account

Returns the email address of the service account for your project used for interactions with Google Cloud KMS.

<details><summary>Parameters</summary>

#### projectId (required)

Project ID for which the service account is requested.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_table

Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the requested table

**Type:** string

#### projectId (required)

Project ID of the requested table

**Type:** string

#### tableId (required)

Table ID of the requested table

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### selectedFields

List of fields to return (comma-separated). If unspecified, all fields are returned

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_datasets

Lists all datasets in the specified project to which you have been granted the READER dataset role.

<details><summary>Parameters</summary>

#### projectId (required)

Project ID of the datasets to be listed

**Type:** string

#### all

Whether to list all datasets, including hidden ones

**Type:** boolean

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### filter

An expression for filtering the results of the request by label. The syntax is "labels.[:]". Multiple filters can be ANDed together by connecting with a space. Example: "labels.department:receiving labels.active". See Filtering datasets using labels for details.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_jobs

Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property.

<details><summary>Parameters</summary>

#### projectId (required)

Project ID of the jobs to list

**Type:** string

#### allUsers

Whether to display jobs owned by all users in the project. Default false

**Type:** boolean

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### maxCreationTime

Max value for job creation time, in milliseconds since the POSIX epoch. If set, only jobs created before or at this timestamp are returned

**Type:** string

#### minCreationTime

Min value for job creation time, in milliseconds since the POSIX epoch. If set, only jobs created after or at this timestamp are returned

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Restrict information returned to a set of selected fields

**Type:** string

**Potential values:** full, minimal

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### stateFilter

Filter for job state

**Type:** array

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_projects

Lists all projects to which you have been granted any project role.

<details><summary>Parameters</summary>

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_tables

Lists all tables in the specified dataset. Requires the READER dataset role.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the tables to list

**Type:** string

#### projectId (required)

Project ID of the tables to list

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## patch_dataset

Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource. This method supports patch semantics.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the dataset being updated

**Type:** string

#### projectId (required)

Project ID of the dataset being updated

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## patch_table

Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports patch semantics.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the table to update

**Type:** string

#### projectId (required)

Project ID of the table to update

**Type:** string

#### tableId (required)

Table ID of the table to update

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## start_job



*This operation has no parameters*

## stream_data_to_table

Streams data into BigQuery one record at a time without needing to run a load job. Requires the WRITER dataset role.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the destination table.

**Type:** string

#### projectId (required)

Project ID of the destination table.

**Type:** string

#### tableId (required)

Table ID of the destination table.

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## tabledata.list

Retrieves table data from a specified set of rows. Requires the READER dataset role.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the table to read

**Type:** string

#### projectId (required)

Project ID of the table to read

**Type:** string

#### tableId (required)

Table ID of the table to read

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### selectedFields

List of fields to return (comma-separated). If unspecified, all fields are returned

**Type:** string

#### startIndex

Zero-based index of the starting row to read

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_dataset

Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the dataset being updated

**Type:** string

#### projectId (required)

Project ID of the dataset being updated

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_table

Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID of the table to update

**Type:** string

#### projectId (required)

Project ID of the table to update

**Type:** string

#### tableId (required)

Table ID of the table to update

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

