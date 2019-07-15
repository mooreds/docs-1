---
id: gcp-cloud-vision-documentation
title: GCP Cloud Vision (version v1.*.*)
sidebar_label: GCP Cloud Vision
layout: docs.mustache
---

## annotate_image

Run image detection and annotation for a batch of images.

<details><summary>Parameters</summary>

#### $body

Multiple image annotation requests are batched into a single service call.

**Type:** object

#### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

#### callback

JSONP

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## async_batch_annotate_files

Run asynchronous image detection and annotation for a list of generic files, such as PDF files, which may contain multiple pages and multiple images per page. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).

<details><summary>Parameters</summary>

#### $body

Multiple async file annotation requests are batched into a single service call.

**Type:** object

#### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

#### callback

JSONP

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## async_batch_annotate_images

Run asynchronous image detection and annotation for a list of generic files, such as PDF files, which may contain multiple pages and multiple images per page. Progress and results can be retrieved through the `google.longrunning.Operations` interface. `Operation.metadata` contains `OperationMetadata` (metadata). `Operation.response` contains `AsyncBatchAnnotateImagesResponse` (results).

<details><summary>Parameters</summary>

#### $body

Multiple async image annotation requests are batched into a single service call.

**Type:** object

#### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

#### callback

JSONP

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## cancel_operation

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

<details><summary>Parameters</summary>

#### name (required)

The name of the operation resource to be cancelled.

**Type:** string

#### operation_id (required)

Operation ID

**Type:** string

#### $body

The request message for Operations.CancelOperation.

**Type:** object

#### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

#### callback

JSONP

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## delete_operation

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

<details><summary>Parameters</summary>

#### operation_id (required)

Operation ID

**Type:** string

#### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

#### callback

JSONP

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## get_operation

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

<details><summary>Parameters</summary>

#### operation_id (required)

Operation ID

**Type:** string

#### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

#### callback

JSONP

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## list_operations

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.

<details><summary>Parameters</summary>

#### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

#### callback

JSONP

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

