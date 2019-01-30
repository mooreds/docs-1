---
id: salesforce-documentation
title: Salesforce (version v1.*.*)
sidebar_label: Salesforce
---

## delete_apex

Calling DELETE on your apex endpoint

<details><summary>Parameters</summary>

#### apexPath (required)

Path to reach your REST Apex resource. E.g Account/accountId

**Type:** string

#### $body

entity data

**Type:** string

</details>

## delete_sobject_record

deletes an SObject instance

<details><summary>Parameters</summary>

#### apiVersion (required)

Version of API you are calling

**Type:** string

#### id (required)

The ID of the SObject to delete

**Type:** array

#### sobjectName (required)

Name of the salesforce Object

**Type:** string

</details>

## describe_sobject

describe a new instance of SObject entity

<details><summary>Parameters</summary>

#### apiVersion (required)

Version of API you are calling

**Type:** string

#### sobjectName (required)

Name of the salesforce Object

**Type:** string

</details>

## get_apex

Calling GET on your apex endpoint

<details><summary>Parameters</summary>

#### apexPath (required)

Path to reach your REST Apex resource. E.g Account/accountId

**Type:** string

#### $body

entity data

**Type:** string

</details>

## get_deleted_sobject

Retrieves the list of individual records that have been deleted within the given timespan for SObject

<details><summary>Parameters</summary>

#### apiVersion (required)

Version of API you are calling

**Type:** string

#### end (required)

The end time of the timespan for which to retrieve data. eg 2013-05-07T22:07:19.000+0000

**Type:** string

#### sobjectName (required)

Name of the salesforce Object

**Type:** string

#### start (required)

The start time of the timespan for which to retrieve data. eg 2013-05-07T22:07:19.000+0000

**Type:** string

</details>

## get_sobject_record

Returns sf instances by id

<details><summary>Parameters</summary>

#### apiVersion (required)

Version of API you are calling

**Type:** string

#### id (required)

The ID of the SObject to get

**Type:** array

#### sobjectName (required)

Name of the salesforce Object

**Type:** string

</details>

## get_sobjects

Lists the available objects and their metadata for your organization’s data.

<details><summary>Parameters</summary>

#### apiVersion (required)

Version of API you are calling

**Type:** string

</details>

## get_updated_sobjects

Retrieves the list of individual records that have been deleted within the given timespan for sobject

<details><summary>Parameters</summary>

#### apiVersion (required)

Version of API you are calling

**Type:** string

#### end (required)

The end time of the timespan for which to retrieve data. eg 2013-05-07T22:07:19.000+0000

**Type:** string

#### sobjectName (required)

Name of the salesforce Object

**Type:** string

#### start (required)

The start time of the timespan for which to retrieve data. eg 2013-05-07T22:07:19.000+0000

**Type:** string

</details>

## post_apex

Calling POST on your apex endpoint

<details><summary>Parameters</summary>

#### apexPath (required)

Path to reach your REST Apex resource. E.g Account/accountId

**Type:** string

#### $body

entity data

**Type:** string

</details>

## put_apex

Calling PUT on your apex endpoint

<details><summary>Parameters</summary>

#### apexPath (required)

Path to reach your REST Apex resource. E.g Account/accountId

**Type:** string

#### $body

entity data

**Type:** string

</details>

## put_sobject_record

updates an SObject instance

<details><summary>Parameters</summary>

#### apiVersion (required)

Version of API you are calling

**Type:** string

#### id (required)

The ID of the SObject to update

**Type:** array

#### sobjectName (required)

Name of the salesforce Object

**Type:** string

#### $body

entity data

**Type:** string

</details>

## query

Executes the specified SOQL query.If the query results are too large, the response contains the first batch of results and a query identifier in the nextRecordsUrl field of the response. The identifier can be used in an additional request to retrieve the next batch.

<details><summary>Parameters</summary>

#### apiVersion (required)

**Type:** string

#### q (required)

A SOQL query.

**Type:** string

#### explain

A SOQL query to get performance feedback on. Use explain instead of q to get a response that details how Salesforce will process your query.

**Type:** string

</details>

## query_all

Executes the specified SOQL query. Unlike the Query resource, QueryAll will return records that have been deleted because of a merge or delete. QueryAll will also return information about archived Task and Event records. QueryAll is available in API version 29.0 and later.

<details><summary>Parameters</summary>

#### apiVersion (required)

**Type:** string

#### q (required)

A SOQL query.

**Type:** string

</details>

