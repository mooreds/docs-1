---
id: apify-v2-documentation
title: Apify v2 (version v1.*.*)
sidebar_label: Apify v2
layout: docs.mustache
---

## abort_build

Aborts an actor build and returns an object that contains all the details about the build. Only builds that are starting or running are aborted. For builds with status `FINISHED`, `FAILED`, `ABORTING` and `TIMED-OUT` this call does nothing.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### buildId (required)

Build ID.

**Type:** string

</details>

## abort_last_run

Aborts the actor's last run and returns an object that contains all the details about the run. Only runs that are starting or running are aborted. For runs with status `FINISHED`, `FAILED`, `ABORTING` and `TIMED-OUT` this call does nothing.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## abort_run

Aborts an actor run and returns an object that contains all the details about the run. Only runs that are starting or running are aborted. For runs with status `FINISHED`, `FAILED`, `ABORTING` and `TIMED-OUT` this call does nothing.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### runId (required)

Run ID.

**Type:** string

</details>

## add_record_to_actor_last_run_store

Stores a value under a specific key to the actor's last run's key-value store.
The value is passed as the PUT payload and it is stored with a MIME content type defined by the `Content-Type` request header.

**IMPORTANT:** The limit of the request payload is 9 MB. If you want to upload a larger record
or speed up your upload, use the [Direct upload URL](#reference/key-value-stores/direct-upload-url) endpoint instead.

To save bandwidth and speed up your upload, send the request payload compressed with Gzip compression and
add the `Content-Encoding: gzip` header.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### recordKey (required)

Key of the record.

**Type:** string

#### $body

**Type:** object

#### status

Filter for the run status.

**Type:** string

</details>

## add_record_to_store

Stores a value under a specific key to the key-value store.
The value is passed as the PUT payload and it is stored with a MIME content type defined by the `Content-Type` request header.

**IMPORTANT:** The limit of the request payload is 9 MB. If you want to upload a larger record
or speed up your upload, use the [Direct upload URL](#reference/key-value-stores/direct-upload-url) endpoint instead.

To save bandwidth and speed up your upload, send the request payload compressed with Gzip compression and
add the `Content-Encoding: gzip` header.

<details><summary>Parameters</summary>

#### recordKey (required)

Key of the record.

**Type:** string

#### storeId (required)

Key-value store ID or `username~store-name`.

**Type:** string

#### $body

**Type:** object

</details>

## add_record_to_task_last_run_store

Stores a value under a specific key to the task's last run's key-value store.
The value is passed as the PUT payload and it is stored with a MIME content type defined by the `Content-Type` request header.

**IMPORTANT:** The limit of the request payload is 9 MB. If you want to upload a larger record
or speed up your upload, use the [Direct upload URL](#reference/key-value-stores/direct-upload-url) endpoint instead.

To save bandwidth and speed up your upload, send the request payload compressed with Gzip compression and
add the `Content-Encoding: gzip` header.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### recordKey (required)

Key of the record.

**Type:** string

#### $body

**Type:** object

#### status

Filter for the run status.

**Type:** string

</details>

## add_request_to_queue

Adds request to the queue. Response contains ID of the request and info if request was already present in the queue or handled. If request with same `uniqueKey` was already present in the queue then returns an ID of existing request.

<details><summary>Parameters</summary>

#### queueId (required)

Queue ID or `username~queue-name`.

**Type:** string

#### $body

**Type:** object

#### clientKey

A unique identifier of the client accessing the request queue. It must be a string between 1 and 32 characters long. This identifier is used to determine whether the queue was accessed by multiple clients. If `clientKey` is not provided, the system considers this API call to come from a new client.

**Type:** string

#### forefront

Determines if request should be added to the head of the queue or to the end. Default value is `false` (end of queue).

**Type:** boolean

</details>

## add_request_to_queue_for_actor_last_run

Adds request to actor's last run's queue. Response contains ID of the request and info if request was already present in the queue or handled. If request with same `uniqueKey` was already present in the queue then returns an ID of existing request.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### $body

**Type:** object

#### clientKey

A unique identifier of the client accessing the request queue. It must be a string between 1 and 32 characters long. This identifier is used to determine whether the queue was accessed by multiple clients. If `clientKey` is not provided, the system considers this API call to come from a new client.

**Type:** string

#### forefront

Determines if request should be added to the head of the queue or to the end. Default value is `false` (end of queue).

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

</details>

## add_request_to_queue_for_task_last_run

Adds request to task's last run's queue. Response contains ID of the request and info if request was already present in the queue or handled. If request with same `uniqueKey` was already present in the queue then returns an ID of existing request.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### $body

**Type:** object

#### clientKey

A unique identifier of the client accessing the request queue. It must be a string between 1 and 32 characters long. This identifier is used to determine whether the queue was accessed by multiple clients. If `clientKey` is not provided, the system considers this API call to come from a new client.

**Type:** string

#### forefront

Determines if request should be added to the head of the queue or to the end. Default value is `false` (end of queue).

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

</details>

## build_actor

Builds an actor.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### betaPackages

If `true` or `1` then the actor is built with beta versions of Apify NPM packages. By default, the build uses `latest` packages.

**Type:** boolean

#### tag

Tag to be applied to the build on success. By default, the tag is taken from actor version's `buildTag` property.

**Type:** string

#### useCache

If `true` or `1`, the system will use a cache to speed up the build process. By default, cache is not used.

**Type:** boolean

#### version

Actor version number to be built.

**Type:** string

#### waitForFinish

The maximum number of seconds the server waits for the build to finish. By default it is `0`, the maximum value is `300`.

**Type:** integer

</details>

## create_actor

Creates a new actor with settings specified by the actor object passed as JSON in the POST payload. The response is the full actor object.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_dataset

Creates dataset of given name and returns its object. If dataset with given name already exists then returns its object.

<details><summary>Parameters</summary>

#### name

Custom unique name to easily identify the store in the future.

**Type:** string

</details>

## create_key_value_store

Creates a key-value store with a specific name. The response is the same object
as returned by the [Get store](#reference/key-value-stores/store-object/get-store) endpoint.

If there is another store with the same name, the endpoint does not create a new one and returns the existing object instead.

<details><summary>Parameters</summary>

#### name

Custom unique name to easily identify the store in the future.

**Type:** string

</details>

## create_request_queue

Creates queue of given name and returns its object. If a queue with the given name already exists then the endpoint returns its object.

<details><summary>Parameters</summary>

#### name

Custom unique name to easily identify the store in the future.

**Type:** string

</details>

## create_task

Create a new task with settings specified by the object passed as JSON in the POST payload.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_version

Creates actor version.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### $body

**Type:** object

</details>

## create_webhook

Creates a new webhook with settings provided by the webhook object passed as JSON in the payload.
The response is the created webhook object.

To make sure that the same webhook is not created twice, use the `idempotencyKey` parameter.
Multiple calls to create webhook with the same idempotency key will only create the webhook
with the first call and return the existing webhook on subsequent calls. Idempotency keys
must be unique, so use a UUID or another random string with enough entropy.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_actor

Deletes an actor.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

</details>

## delete_actor_last_run_key_value_store

Deletes an actor's last run's key-value store.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## delete_dataset

Deletes given dataset.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID or `username~dataset-name`.

**Type:** string

</details>

## delete_dataset_for_actor_last_run

Deletes actor's last run's dataset.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## delete_dataset_for_task_last_run

Deletes task's last run's dataset.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## delete_key_value_store

Deletes a key-value store.

<details><summary>Parameters</summary>

#### storeId (required)

Key-value store ID or `username~store-name`.

**Type:** string

</details>

## delete_last_run_key_value_store

Deletes an actor's last run's key-value store.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## delete_request_from_queue

Deletes given request from queue.

<details><summary>Parameters</summary>

#### queueId (required)

Queue ID or `username~queue-name`.

**Type:** string

#### requestId (required)

Request ID.

**Type:** string

#### clientKey

A unique identifier of the client accessing the request queue. It must be a string between 1 and 32 characters long. This identifier is used to determine whether the queue was accessed by multiple clients. If `clientKey` is not provided, the system considers this API call to come from a new client.

**Type:** string

</details>

## delete_request_from_queue_for_actor_last_run

Deletes given request from actor's last run's queue.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### requestId (required)

Request ID.

**Type:** string

#### clientKey

A unique identifier of the client accessing the request queue. It must be a string between 1 and 32 characters long. This identifier is used to determine whether the queue was accessed by multiple clients. If `clientKey` is not provided, the system considers this API call to come from a new client.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## delete_request_from_queue_for_task_last_run

Deletes given request from task's last run's queue.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### requestId (required)

Request ID.

**Type:** string

#### clientKey

A unique identifier of the client accessing the request queue. It must be a string between 1 and 32 characters long. This identifier is used to determine whether the queue was accessed by multiple clients. If `clientKey` is not provided, the system considers this API call to come from a new client.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## delete_request_queue

Deletes given queue.

<details><summary>Parameters</summary>

#### queueId (required)

Queue ID or `username~queue-name`.

**Type:** string

</details>

## delete_request_queue_for_actor_last_run

Deletes actor's last_run's request queue.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## delete_request_queue_for_task_last_run

Deletes task's last_run's request queue.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## delete_task

Delete the task specified through the `actorTaskId` parameter.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

</details>

## delete_version_for_actor

Deletes a version for an actor.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### versionNumber (required)

Actor major and minor version of the actor.

**Type:** string

</details>

## delete_webhook

Deletes an webhook.

<details><summary>Parameters</summary>

#### webhookId (required)

Webhook ID.

**Type:** string

</details>

## get_actor

Gets an object that contains all the details about a specific actor.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

</details>

## get_actor_last_run_direct_upload_url

Generates a unique URL that can be used to upload a record under a specific key to the actor's last run's key-value store.
The record must be uploaded to the resulting URL using a PUT request.

This endpoint is useful if your record is larger than the limit
imposed by the [Put record](#reference/key-value-stores/record/put-record) endpoint
(i.e. 9 MB) or if you want to get the maximum speed for your upload.

To save bandwidth and speed up your upload, send the request payload compressed with Gzip compression and
add the `Content-Encoding: gzip` header to your request.

**IMPORTANT:** The `Content-Type` and `Content-Encoding` headers sent in both requests must match!

<details><summary>Parameters</summary>

#### Content-Type (required)

**Type:** string

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### recordKey (required)

Key of the record.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_actor_last_run_key_value_store

Gets an object that contains all the details about an actor's last run's key-value store.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_build_for_actor

Gets an object that contains all the details about a specific build of an actor.

By passing the optional `waitForFinish=1` parameter the API endpoint will synchronously wait for the build to finish.
This is useful to avoid periodic polling when waiting for an actor build to finish.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### buildId (required)

Build ID.

**Type:** string

#### waitForFinish

The maximum number of seconds the server waits for the build to finish. By default it is `0`, the maximum value is `300`.

**Type:** integer

</details>

## get_current_user_data



*This operation has no parameters*

## get_dataset

Returns dataset object for given dataset ID.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID or `username~dataset-name`.

**Type:** string

</details>

## get_dataset_for_actor_last_run

Returns dataset object for the actor's last run.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_dataset_for_task_last_run

Returns dataset object for the task's last run.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_direct_upload_url

Generates a unique URL that can be used to upload a record under a specific key to the key-value store.
The record must be uploaded to the resulting URL using a PUT request.

This endpoint is useful if your record is larger than the limit
imposed by the [Put record](#reference/key-value-stores/record/put-record) endpoint
(i.e. 9 MB) or if you want to get the maximum speed for your upload.

To save bandwidth and speed up your upload, send the request payload compressed with Gzip compression and
add the `Content-Encoding: gzip` header to your request.

**IMPORTANT:** The `Content-Type` and `Content-Encoding` headers sent in both requests must match!

<details><summary>Parameters</summary>

#### Content-Type (required)

**Type:** string

#### recordKey (required)

Key of the record.

**Type:** string

#### storeId (required)

Key-value store ID or `username~store-name`.

**Type:** string

</details>

## get_head_of_queue

Returns given number of first requests from the queue.

<details><summary>Parameters</summary>

#### queueId (required)

Queue ID or `username~queue-name`.

**Type:** string

#### hadMultipleClients

Is `true` if the queue was accessed by more than one clients (with unique or empty `clientKey`). This field is used by [Apify SDK](https://sdk.apify.com) to determine whether the local cache is consistent with the remote storage, and thus optimize certain operations.

**Type:** boolean

</details>

## get_head_of_queue_for_actor_last_run

Returns given number of first requests from the actor's last run's queue.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### hadMultipleClients

Is `true` if the queue was accessed by more than one clients (with unique or empty `clientKey`). This field is used by [Apify SDK](https://sdk.apify.com) to determine whether the local cache is consistent with the remote storage, and thus optimize certain operations.

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

</details>

## get_head_of_queue_for_task_last_run

Returns given number of first requests from the task's last run's queue.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### hadMultipleClients

Is `true` if the queue was accessed by more than one clients (with unique or empty `clientKey`). This field is used by [Apify SDK](https://sdk.apify.com) to determine whether the local cache is consistent with the remote storage, and thus optimize certain operations.

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

</details>

## get_items_in_actor_last_run_dataset

Returns data stored in the actor's last run's dataset in a desired format. The format of the response depends on "format" query parameter. Note that CSV, XLSX and HTML tables are limited to 500 columns and the column names cannot be longer than 200 characters. JSON, XML and RSS formats do not have such restrictions.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### attachment

If true or 1 then the response will define the Content-Disposition: attachment header, forcing a web browser to download the file rather than to display it. By default this header is not present.

**Type:** boolean

#### bom

All text responses are encoded in UTF-8 encoding. By default, the format=csv files are prefixed with the UTF-8 Byte Order Mark (BOM), while json, jsonl, xml, html and rss files are not. If you want to override this default behavior, specify bom=1 query parameter to include the BOM or bom=0 to skip it.

**Type:** boolean

#### delimiter

A delimiter character for CSV files, only used if format=csv. The default delimiter is a simple comma (,).

**Type:** string

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

#### fields

A comma-separated list of fields which should be picked from the items, only these fields will remain in the resulting record objects. Note that the fields in the outputted items are sorted the same way as they are specified in the fields query parameter. You can use this feature to effectively fix the output format.

**Type:** array

#### format

Format of the results.

**Type:** string

**Potential values:** json, jsonl, csv, html, xlsx, xml, rss

#### omit

A comma-separated list of fields which should be omitted from the items.

**Type:** array

#### skipHeaderRow

If true or 1 then header row in the csv format is skipped.

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

#### unwind

Name of a field which should be unwound. If the field is an array then every element of the array will become a separate record and merged with parent object. If the unwound field is an object then it is merged with the parent object If the unwound field is missing or its value is neither an array nor an object and therefore cannot be merged with a parent object then the item gets preserved as it is. Note that the unwound items ignore the desc parameter.

**Type:** string

#### xmlRoot

Overrides default root element name of xml output. By default the root element is items.

**Type:** string

#### xmlRow

Overrides default element name that wraps each page or page function result object in xml output. By default the element name is item.

**Type:** string

</details>

## get_items_in_dataset

Returns data stored in the dataset in a desired format. The format of the response depends on "format" query parameter. Note that CSV, XLSX and HTML tables are limited to 500 columns and the column names cannot be longer than 200 characters. JSON, XML and RSS formats do not have such restrictions.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID or `username~dataset-name`.

**Type:** string

#### attachment

If true or 1 then the response will define the Content-Disposition: attachment header, forcing a web browser to download the file rather than to display it. By default this header is not present.

**Type:** boolean

#### bom

All text responses are encoded in UTF-8 encoding. By default, the format=csv files are prefixed with the UTF-8 Byte Order Mark (BOM), while json, jsonl, xml, html and rss files are not. If you want to override this default behavior, specify bom=1 query parameter to include the BOM or bom=0 to skip it.

**Type:** boolean

#### delimiter

A delimiter character for CSV files, only used if format=csv. The default delimiter is a simple comma (,).

**Type:** string

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

#### fields

A comma-separated list of fields which should be picked from the items, only these fields will remain in the resulting record objects. Note that the fields in the outputted items are sorted the same way as they are specified in the fields query parameter. You can use this feature to effectively fix the output format.

**Type:** array

#### format

Format of the results.

**Type:** string

**Potential values:** json, jsonl, csv, html, xlsx, xml, rss

#### omit

A comma-separated list of fields which should be omitted from the items.

**Type:** array

#### skipHeaderRow

If true or 1 then header row in the csv format is skipped.

**Type:** boolean

#### unwind

Name of a field which should be unwound. If the field is an array then every element of the array will become a separate record and merged with parent object. If the unwound field is an object then it is merged with the parent object If the unwound field is missing or its value is neither an array nor an object and therefore cannot be merged with a parent object then the item gets preserved as it is. Note that the unwound items ignore the desc parameter.

**Type:** string

#### xmlRoot

Overrides default root element name of xml output. By default the root element is items.

**Type:** string

#### xmlRow

Overrides default element name that wraps each page or page function result object in xml output. By default the element name is item.

**Type:** string

</details>

## get_items_in_task_last_run_dataset

Returns data stored in the task's last run's dataset in a desired format. The format of the response depends on "format" query parameter. Note that CSV, XLSX and HTML tables are limited to 500 columns and the column names cannot be longer than 200 characters. JSON, XML and RSS formats do not have such restrictions.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### attachment

If true or 1 then the response will define the Content-Disposition: attachment header, forcing a web browser to download the file rather than to display it. By default this header is not present.

**Type:** boolean

#### bom

All text responses are encoded in UTF-8 encoding. By default, the format=csv files are prefixed with the UTF-8 Byte Order Mark (BOM), while json, jsonl, xml, html and rss files are not. If you want to override this default behavior, specify bom=1 query parameter to include the BOM or bom=0 to skip it.

**Type:** boolean

#### delimiter

A delimiter character for CSV files, only used if format=csv. The default delimiter is a simple comma (,).

**Type:** string

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

#### fields

A comma-separated list of fields which should be picked from the items, only these fields will remain in the resulting record objects. Note that the fields in the outputted items are sorted the same way as they are specified in the fields query parameter. You can use this feature to effectively fix the output format.

**Type:** array

#### format

Format of the results.

**Type:** string

**Potential values:** json, jsonl, csv, html, xlsx, xml, rss

#### omit

A comma-separated list of fields which should be omitted from the items.

**Type:** array

#### skipHeaderRow

If true or 1 then header row in the csv format is skipped.

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

#### unwind

Name of a field which should be unwound. If the field is an array then every element of the array will become a separate record and merged with parent object. If the unwound field is an object then it is merged with the parent object If the unwound field is missing or its value is neither an array nor an object and therefore cannot be merged with a parent object then the item gets preserved as it is. Note that the unwound items ignore the desc parameter.

**Type:** string

#### xmlRoot

Overrides default root element name of xml output. By default the root element is items.

**Type:** string

#### xmlRow

Overrides default element name that wraps each page or page function result object in xml output. By default the element name is item.

**Type:** string

</details>

## get_key_value_store

Gets an object that contains all the details about a specific key-value store.

<details><summary>Parameters</summary>

#### storeId (required)

Key-value store ID or `username~store-name`.

**Type:** string

</details>

## get_last_run_for_actor

Gets an object that contains all the details about the actor's last run.

By passing the optional `waitForFinish=1` parameter the API endpoint will synchronously wait for the build to finish.
This is useful to avoid periodic polling when waiting for actor build to complete.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_last_run_for_task

Gets an object that contains all the details about the task's last run.

By passing the optional `waitForFinish=1` parameter the API endpoint will synchronously wait for the build to finish.
This is useful to avoid periodic polling when waiting for actor build to complete.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_log

Responds with HTTP status 302 to redirect to an URL containing the requested log. The log has a content type `text/plain` and it is encoded as `gzip` returned with appropriate HTTP headers.

<details><summary>Parameters</summary>

#### buildOrRunId (required)

ID of the actor build or run.

**Type:** string

#### download

If `true` or `1` then the web browser will download the log file rather than open it in a tab.

**Type:** boolean

#### stream

If `true` or `1` then the logs will be streamed as long as the run or build is running.

**Type:** boolean

</details>

## get_log_for_actor_last_run

Responds with HTTP status 302 to redirect to an URL containing the actor's last run's log. The log has a content type `text/plain` and it is encoded as `gzip` returned with appropriate HTTP headers.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### download

If `true` or `1` then the web browser will download the log file rather than open it in a tab.

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

#### stream

If `true` or `1` then the logs will be streamed as long as the run or build is running.

**Type:** boolean

</details>

## get_log_for_task_last_run

Responds with HTTP status 302 to redirect to an URL containing the task's last run's log. The log has a content type `text/plain` and it is encoded as `gzip` returned with appropriate HTTP headers.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### download

If `true` or `1` then the web browser will download the log file rather than open it in a tab.

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

#### stream

If `true` or `1` then the logs will be streamed as long as the run or build is running.

**Type:** boolean

</details>

## get_public_user_data

Returns public information about a specific user account, similar to what can be seen on public profile pages (e.g. https://apify.com/apify).

<details><summary>Parameters</summary>

#### userId (required)

User ID or username.

**Type:** string

</details>

## get_record_from_actor_last_run_store

Gets a value stored in the actor's last run's key-value store under a specific key. If the request defines the `Accept-Encoding: gzip` HTTP header then the response will be gzipped.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### recordKey (required)

Key of the record.

**Type:** string

#### disableRedirect

By default, the API responds with the HTTP 302 status to redirect the client to another URL for faster download of the record. You can set `disableRedirect=1` to prevent this behavior and return the record directly.

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

</details>

## get_record_from_store

Gets a value stored in the key-value store under a specific key. If the request defines the `Accept-Encoding: gzip` HTTP header then the response will be gzipped.

<details><summary>Parameters</summary>

#### recordKey (required)

Key of the record.

**Type:** string

#### storeId (required)

Key-value store ID or `username~store-name`.

**Type:** string

#### disableRedirect

By default, the API responds with the HTTP 302 status to redirect the client to another URL for faster download of the record. You can set `disableRedirect=1` to prevent this behavior and return the record directly.

**Type:** boolean

</details>

## get_record_from_task_last_run_store

Gets a value stored in the task's last run's key-value store under a specific key. If the request defines the `Accept-Encoding: gzip` HTTP header then the response will be gzipped.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### recordKey (required)

Key of the record.

**Type:** string

#### disableRedirect

By default, the API responds with the HTTP 302 status to redirect the client to another URL for faster download of the record. You can set `disableRedirect=1` to prevent this behavior and return the record directly.

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

</details>

## get_request_from_queue

Returns request from queue.

<details><summary>Parameters</summary>

#### queueId (required)

Queue ID or `username~queue-name`.

**Type:** string

#### requestId (required)

Request ID.

**Type:** string

</details>

## get_request_from_queue_for_actor_last_run

Returns request from actor's last run's queue.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### requestId (required)

Request ID.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_request_from_queue_for_task_last_run

Returns request from task's last run's queue.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### requestId (required)

Request ID.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_request_queue

Returns queue object for given queue ID.

<details><summary>Parameters</summary>

#### queueId (required)

Queue ID or `username~queue-name`.

**Type:** string

</details>

## get_request_queue_for_actor_last_run

Returns queue object for actor's last run's request queue.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_request_queue_for_task_last_run

Returns queue object for task's run's request queue.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_run_for_actor

Gets an object that contains all the details about a specific run of an actor.

By passing the optional `waitForFinish=1` parameter the API endpoint will synchronously wait for the build to finish.
This is useful to avoid periodic polling when waiting for actor build to complete.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### runId (required)

Run ID.

**Type:** string

#### waitForFinish

The maximum number of seconds the server waits for the build to finish. By default it is `0`, the maximum value is `300`.

**Type:** integer

</details>

## get_task

Get an object that contains all the details about a task.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

</details>

## get_task_last_run_direct_upload_url

Generates a unique URL that can be used to upload a record under a specific key to the task's last run's key-value store.
The record must be uploaded to the resulting URL using a PUT request.

This endpoint is useful if your record is larger than the limit
imposed by the [Put record](#reference/key-value-stores/record/put-record) endpoint
(i.e. 9 MB) or if you want to get the maximum speed for your upload.

To save bandwidth and speed up your upload, send the request payload compressed with Gzip compression and
add the `Content-Encoding: gzip` header to your request.

**IMPORTANT:** The `Content-Type` and `Content-Encoding` headers sent in both requests must match!

<details><summary>Parameters</summary>

#### Content-Type (required)

**Type:** string

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### recordKey (required)

Key of the record.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_task_last_run_key_value_store

Gets an object that contains all the details about an task's last run's key-value store.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## get_version_for_actor

Gets an object that contains all the details about a specific version of an actor.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### versionNumber (required)

Actor major and minor version of the actor.

**Type:** string

</details>

## get_webhook

Gets webhook object with all details.

<details><summary>Parameters</summary>

#### webhookId (required)

Webhook ID.

**Type:** string

</details>

## get_webhook_dispatch

Gets webhook dispatch object with all details.

<details><summary>Parameters</summary>

#### dispatchId (required)

Webhook dispatch ID.

**Type:** string

</details>

## list_actor_last_run_keys_in_store

Returns a list of objects describing keys of an actor's last run's key-value store, as well as some information about the values (e.g. size). This endpoint is paginated using `exclusiveStartKey` and `limit` parameters.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## list_actors

Gets the list of all actors that the user created or used. The response is a list of objects where each object
contains a basic information about a single actor.
To only get actors created by the user, add the `my=1` query parameter. 
The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records.
By default, the records are sorted by the `createdAt` field in ascending order,
therefore you can use pagination to incrementally fetch all actors while new
ones are still being created. To sort the records in descending order, use the `desc=1` parameter.

<details><summary>Parameters</summary>

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

#### my

If `true` or `1` then the returned list only contains items owned by the user.

**Type:** boolean

</details>

## list_all_webhook_dispatches

Gets the list of webhook dispatches that the user have. The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records. By default, the records are sorted by the `createdAt` field in ascending order. To sort the records in descending order, use the `desc=1` parameter.

<details><summary>Parameters</summary>

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

</details>

## list_builds_for_actor

Gets the list of builds of a specific actor. The response is a JSON with the list of objects where each object
contains basic information about a single build.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records.

By default, the records are sorted by the `startedAt` field in ascending order,
therefore you can use pagination to incrementally fetch all builds while new
ones are still being started. To sort the records in descending order, use the `desc=1`
parameter.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

</details>

## list_datasets

Lists datasets of user. Response is a JSON array of objects where each object
contains basic information about one dataset.

By default, the objects are sorted by the `createdAt` field in ascending order,
therefore you can use pagination to incrementally fetch all datasets while new
ones are still being created. To sort them in descending order, use `desc=1`
parameter. The endpoint supports pagination using `limit` and `offset` parameters and it will not return more than 1000
array elements.

<details><summary>Parameters</summary>

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

#### unnamed

If `true` then all the items are returned. By default only named items are returned.

**Type:** boolean

</details>

## list_dispatches_for_webhook

Gets list of dispatches of a given webhook.

<details><summary>Parameters</summary>

#### webhookId (required)

Webhook ID.

**Type:** string

</details>

## list_key_value_stores

Gets the list of key-value stores owned by the user.
The response is a list of objects where each objects contains a basic information about a single key-value store.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000
array elements.

By default, the records are sorted by the `createdAt` field in ascending order,
therefore you can use pagination to incrementally fetch all key-value stores while new
ones are still being created. To sort the records in descending order, use the `desc=1`
parameter.

<details><summary>Parameters</summary>

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

#### unnamed

If `true` then all the items are returned. By default only named items are returned.

**Type:** boolean

</details>

## list_keys_in_store

Returns a list of objects describing keys of a given key-value store, as well as some information about the values (e.g. size). This endpoint is paginated using `exclusiveStartKey` and `limit` parameters.

<details><summary>Parameters</summary>

#### storeId (required)

Key-value store ID or `username~store-name`.

**Type:** string

</details>

## list_request_queues

Lists request queues of user. Response is a JSON array of objects where each object
contains basic information about one queue.

By default, the objects are sorted by the `createdAt` field in ascending order,
therefore you can use pagination to incrementally fetch all queues while new
ones are still being created. To sort them in descending order, use `desc=1`
parameter. The endpoint supports pagination using `limit` and `offset` parameters and it will not return more than 1000
array elements.

<details><summary>Parameters</summary>

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

#### unnamed

If `true` then all the items are returned. By default only named items are returned.

**Type:** boolean

</details>

## list_runs_for_actor

Gets the list of runs of a specific actor. The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 array elements. By default, the records are sorted by the `startedAt` field in ascending order, therefore you can use pagination to incrementally fetch all records while new ones are still being created. To sort the records in descending order, use `desc=1` parameter.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

</details>

## list_runs_for_task

Get a list of runs of a specific task. The endpoint supports pagination using the `limit` and `offset` parameters, and it does not return more than 1000 array elements. By default, the records are sorted by the `startedAt` field in ascending order; therefore you can use pagination to incrementally fetch all records while new ones are still being created. To sort the records in descending order, use the `desc=1` parameter.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

</details>

## list_task_last_run_keys_in_store

Returns a list of objects describing keys of a task's last run's key-value store, as well as some information about the values (e.g. size). This endpoint is paginated using `exclusiveStartKey` and `limit` parameters.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## list_tasks

Gets the list of all tasks that the user created or used. The response is a list of objects where each object
contains essential information about a single task.

The endpoint supports pagination using the `limit` and `offset` parameters, and it does not return more than a 1000 records.

By default, the records are sorted by the `createdAt` field in ascending order;
therefore you can use pagination to incrementally fetch all tasks while new
ones are still being created. To sort the records in descending order, use the `desc=1`
parameter.

<details><summary>Parameters</summary>

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

</details>

## list_versions

Gets the list of versions of a specific actor. The response is a JSON with the list of objects where each object contains basic information about a single version.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

</details>

## list_webhooks

Gets the list of webhooks that the user created. The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records. By default, the records are sorted by the `createdAt` field in ascending order. To sort the records in descending order, use the `desc=1` parameter.

<details><summary>Parameters</summary>

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

</details>

## list_webhooks_for_actor

Gets the list of webhooks of a specific actor. The response is a JSON with the list of objects where each object
contains basic information about a single webhook.

The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records.

By default, the records are sorted by the `createdAt` field in ascending order,
to sort the records in descending order, use the `desc=1` parameter.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

</details>

## list_webhooks_for_task

Gets the list of webhooks of a specific actor task. The endpoint supports pagination using the `limit` and `offset` parameters and it will not return more than 1000 records. By default, the records are sorted by the `createdAt` field in ascending order; to sort the records in descending order, use the `desc=1` parameter.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### desc

If `true` or `1` then the items are sorted by the `createdAt` field in descending order.

**Type:** boolean

</details>

## metamorph_last_run

Transforms the actor's last run into a run of another actor with a new input.
This is useful if you want to use another actor to finish the work
of your current actor run, without the need to create a completely new run and waiting for its finish.
For the users of your actors, the metamorph operation is transparent, they will just see your actor got the work done.

Internally, the system stops the Docker container corresponding to the actor run
and starts a new container using a different Docker image.
All the default storages are preserved and the new input is stored under the `INPUT-METAMORPH-1` key in the same default key-value store.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### targetActorId (required)

ID of a target actor that the run should be transformed into.

**Type:** string

#### build

Specifies the actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the default run configuration for the actor (typically `latest`).

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## metamorph_run

Transforms an actor run into a run of another actor with a new input.
This is useful if you want to use another actor to finish the work
of your current actor run, without the need to create a completely new run and waiting for its finish.
For the users of your actors, the metamorph operation is transparent, they will just see your actor got the work done.

Internally, the system stops the Docker container corresponding to the actor run
and starts a new container using a different Docker image.
All the default storages are preserved and the new input is stored under the `INPUT-METAMORPH-1` key in the same default key-value store.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### runId (required)

Run ID.

**Type:** string

#### targetActorId (required)

ID of a target actor that the run should be transformed into.

**Type:** string

#### build

Specifies the actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the default run configuration for the actor (typically `latest`).

**Type:** string

</details>

## put_items_into_actor_last_run_dataset

Saves an item or an array of items into the actor's last run's dataset. The limit of request payload for dataset is 5mb.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### $body

**Type:** object

#### status

Filter for the run status.

**Type:** string

</details>

## put_items_into_dataset

Saves an item or an array of items into dataset. The limit of request payload for dataset is 5mb.

<details><summary>Parameters</summary>

#### datasetId (required)

Dataset ID or `username~dataset-name`.

**Type:** string

#### $body

**Type:** object

</details>

## put_items_into_task_last_run_dataset

Saves an item or an array of items into the actor's last run's dataset. The limit of request payload for dataset is 5mb.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### $body

**Type:** object

#### status

Filter for the run status.

**Type:** string

</details>

## remove_record_from_actor_last_run_store

Removes a record specified by a key from the actor's last run's key-value store.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### recordKey (required)

Key of the record.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## remove_record_from_store

Removes a record specified by a key from the key-value store.

<details><summary>Parameters</summary>

#### recordKey (required)

Key of the record.

**Type:** string

#### storeId (required)

Key-value store ID or `username~store-name`.

**Type:** string

</details>

## remove_record_from_task_last_run_store

Removes a record specified by a key from the task's last run's key-value store.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### recordKey (required)

Key of the record.

**Type:** string

#### status

Filter for the run status.

**Type:** string

</details>

## run_actor

Runs an actor and immediately returns without waiting for the run to finish.
The POST payload including its `Content-Type` header is passed as `INPUT` to the actor (usually application/json).
The actor is started with the default options; you can override them using various URL query parameters.
The response is the Run object as returned by the [Get run](#reference/actors/run-object/get-run) API endpoint.
If you want to wait for the run to finish and receive the actual output of the actor as the response,
please use one of the [Run actor synchronously](#reference/actors/run-actor-synchronously) API endpoints instead.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### $body

**Type:** object

#### build

Specifies the actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the default run configuration for the actor (typically `latest`).

**Type:** string

#### memory

Memory limit for the run, in megabytes. By default, the run uses a memory limit specified in the default run configuration for the actor.

**Type:** integer

#### timeout

Optional timeout for the run, in seconds. By default, the run uses a timeout specified in the default run configuration for the actor.

**Type:** integer

#### waitForFinish

The maximum number of seconds the server waits for the build to finish. By default it is `0`, the maximum value is `300`.

**Type:** integer

#### webhooks

Specifies optional webhooks associated with the actor run, which can be used to receive a notification e.g. when the actor finished or failed. The value is a Base64-encoded JSON array of objects defining the webhooks.

**Type:** string

</details>

## run_task

Runs an actor task and immediately returns without waiting for the run to finish.

Optionally, you can override the actor input configuration by passing a JSON object as the POST payload
and setting the `Content-Type: application/json` HTTP header.
Note that if the object in the POST payload does not define a particular input property,
the actor run uses the default value defined by the task (or actor's input schema if not defined by the task).

The response is the actor Run object as returned by the [Get run](#reference/actors/run-object/get-run) endpoint.
If you want to wait for the run to finish and receive the actual output of the actor run as the response,
use one of the [Run task synchronously](#/reference/actor-tasks/run-task-synchronously) API endpoints instead.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### $body

**Type:** object

#### waitForFinish

The maximum number of seconds the server waits for the build to finish. By default it is `0`, the maximum value is `300`.

**Type:** integer

#### webhooks

Specifies optional webhooks associated with the actor run, which can be used to receive a notification e.g. when the actor finished or failed. The value is a Base64-encoded JSON array of objects defining the webhooks.

**Type:** string

</details>

## sync_run_actor_with_input

Runs a specific actor and returns its output.

The POST payload including its `Content-Type` header is passed as `INPUT` to the actor (usually application/json).
The HTTP response contains actor's `OUTPUT` record from its default key-value store.

The actor is started with the default options; you can override them using various URL query parameters.
If the actor run exceeds 300 seconds,
the HTTP response will have status 408 (Request Timeout).

Beware that it might be impossible to maintain an idle HTTP connection for a long period of time,
due to client timeout or network conditions. Make sure your HTTP client is configured to have a long enough connection timeout.
If the connection breaks, you will not receive any information about the run and its status.

To run the actor asynchronously, use the [Run actor](#reference/actors/run-collection/run-actor) API endpoint instead.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### $body

**Type:** object

#### build

Specifies the actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the default run configuration for the actor (typically `latest`).

**Type:** string

#### memory

Memory limit for the run, in megabytes. By default, the run uses a memory limit specified in the default run configuration for the actor.

**Type:** integer

#### outputRecordKey

Key of the record from run's default key-value store to be returned in the response. By default, it is `OUTPUT`.

**Type:** string

#### timeout

Optional timeout for the run, in seconds. By default, the run uses a timeout specified in the default run configuration for the actor.

**Type:** integer

#### webhooks

Specifies optional webhooks associated with the actor run, which can be used to receive a notification e.g. when the actor finished or failed. The value is a Base64-encoded JSON array of objects defining the webhooks.

**Type:** string

</details>

## sync_run_actor_without_input

Runs a specific actor and returns its output.
The run must finish in 300 seconds otherwise the API endpoint returns a timeout error.
The actor is not passed any input.

Beware that it might be impossible to maintain an idle HTTP connection for a long period of time,
due to client timeout or network conditions. Make sure your HTTP client is configured to have a long enough connection timeout.
If the connection breaks, you will not receive any information about the run and its status.

To run the actor asynchronously, use the [Run actor](#reference/actors/run-collection/run-actor) API endpoint instead.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### build

Specifies the actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the default run configuration for the actor (typically `latest`).

**Type:** string

#### memory

Memory limit for the run, in megabytes. By default, the run uses a memory limit specified in the default run configuration for the actor.

**Type:** integer

#### outputRecordKey

Key of the record from run's default key-value store to be returned in the response. By default, it is `OUTPUT`.

**Type:** string

#### timeout

Optional timeout for the run, in seconds. By default, the run uses a timeout specified in the default run configuration for the actor.

**Type:** integer

#### webhooks

Specifies optional webhooks associated with the actor run, which can be used to receive a notification e.g. when the actor finished or failed. The value is a Base64-encoded JSON array of objects defining the webhooks.

**Type:** string

</details>

## sync_run_task_no_input

Run a specific task and return its output.
The run must finish in 300 seconds otherwise the API endpoint returns a timeout error.

Beware that it might be impossible to maintain an idle HTTP connection for an extended period,
due to client timeout or network conditions. Make sure your HTTP client is configured to have a long enough connection timeout.
If the connection breaks, you will not receive any information about the run and its status.

To run the Task asynchronously, use the [Run task asynchronously](#reference/actor-tasks/run-collection/run-task) endpoint instead.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### outputRecordKey

Key of the record from run's default key-value store to be returned in the response. By default, it is `OUTPUT`.

**Type:** string

#### webhooks

Specifies optional webhooks associated with the actor run, which can be used to receive a notification e.g. when the actor finished or failed. The value is a Base64-encoded JSON array of objects defining the webhooks.

**Type:** string

</details>

## sync_run_task_with_input

Runs an actor task and synchronously returns its output.
The run must finish in 300 seconds otherwise the API endpoint returns a timeout error.

Optionally, you can override the actor input configuration by passing a JSON object as the POST payload
and setting the `Content-Type: application/json` HTTP header.
Note that if the object in the POST payload does not define a particular input property,
the actor run uses the default value defined by the task (or actor's input schema if not defined by the task).

Beware that it might be impossible to maintain an idle HTTP connection for an extended period,
due to client timeout or network conditions. Make sure your HTTP client is configured to have a long enough connection timeout.
If the connection breaks, you will not receive any information about the run and its status.

Input fields from actor task configuration can be overloaded with values passed as the POST payload.
Just make sure to specify `Content-Type` header to be `application/json` and input to be an object.

To run the task asynchronously, use the [Run task](#/reference/actor-tasks/run-collection/run-task) API endpoint instead.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### $body

**Type:** object

#### outputRecordKey

Key of the record from run's default key-value store to be returned in the response. By default, it is `OUTPUT`.

**Type:** string

#### webhooks

Specifies optional webhooks associated with the actor run, which can be used to receive a notification e.g. when the actor finished or failed. The value is a Base64-encoded JSON array of objects defining the webhooks.

**Type:** string

</details>

## update_actor

Updates settings of an actor using values specified by an actor object passed as JSON in the POST payload. If the object does not define a specific property, its value will not be updated.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### $body

**Type:** object

</details>

## update_request_in_queue

Updates request in queue. Mark request as handled by setting `request.handledAt = new Date()`. If `handledAt` is set then request will be removed from head of the queue.

<details><summary>Parameters</summary>

#### queueId (required)

Queue ID or `username~queue-name`.

**Type:** string

#### requestId (required)

Request ID.

**Type:** string

#### $body

**Type:** object

#### clientKey

A unique identifier of the client accessing the request queue. It must be a string between 1 and 32 characters long. This identifier is used to determine whether the queue was accessed by multiple clients. If `clientKey` is not provided, the system considers this API call to come from a new client.

**Type:** string

#### forefront

Determines if request should be added to the head of the queue or to the end. Default value is `false` (end of queue).

**Type:** boolean

</details>

## update_request_in_queue_for_actor_last_run

Updates request in actor's last run's queue. Mark request as handled by setting `request.handledAt = new Date()`. If `handledAt` is set then request will be removed from head of the queue.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### requestId (required)

Request ID.

**Type:** string

#### $body

**Type:** object

#### clientKey

A unique identifier of the client accessing the request queue. It must be a string between 1 and 32 characters long. This identifier is used to determine whether the queue was accessed by multiple clients. If `clientKey` is not provided, the system considers this API call to come from a new client.

**Type:** string

#### forefront

Determines if request should be added to the head of the queue or to the end. Default value is `false` (end of queue).

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

</details>

## update_request_in_queue_for_taskt_run

Updates request in task's last run's queue. Mark request as handled by setting `request.handledAt = new Date()`. If `handledAt` is set then request will be removed from head of the queue.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### requestId (required)

Request ID.

**Type:** string

#### $body

**Type:** object

#### clientKey

A unique identifier of the client accessing the request queue. It must be a string between 1 and 32 characters long. This identifier is used to determine whether the queue was accessed by multiple clients. If `clientKey` is not provided, the system considers this API call to come from a new client.

**Type:** string

#### forefront

Determines if request should be added to the head of the queue or to the end. Default value is `false` (end of queue).

**Type:** boolean

#### status

Filter for the run status.

**Type:** string

</details>

## update_task

Update settings of a task using values specified by an object passed as JSON in the POST payload. If the object does not define a specific property, its value is not updated.

<details><summary>Parameters</summary>

#### actorTaskId (required)

Task ID or a tilde-separated owner's username and task's name.

**Type:** string

#### $body

**Type:** object

</details>

## update_version_for_actor

Updates actor version using values specified by an version object passed as JSON in the POST payload. If the object does not define a specific property, its value will not be updated.

<details><summary>Parameters</summary>

#### actorId (required)

Actor ID or a tilde-separated owner's username and actor name.

**Type:** string

#### versionNumber (required)

Actor major and minor version of the actor.

**Type:** string

#### $body

**Type:** object

</details>

## update_webhook

Updates a webhook using values specified by a webhook object passed as JSON in the POST payload. If the object does not define a specific property, its value will not be updated.

<details><summary>Parameters</summary>

#### webhookId (required)

Webhook ID.

**Type:** string

#### $body

**Type:** object

</details>

