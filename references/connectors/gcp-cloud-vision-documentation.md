---
id: gcp-cloud-vision-documentation
title: GCP Cloud Vision (version v1.*.*)
sidebar_label: GCP Cloud Vision
layout: docs.mustache
---

## annotate_image

Run image detection and annotation for a batch of images.

<details><summary>Parameters</summary>

### $body

Multiple image annotation requests are batched into a single service call.

**Type:** object

```json
{
  "requests" : [ {
    "features" : [ {
      "maxResults" : "Maximum number of results of this type. Does not apply to\n`TEXT_DETECTION`, `DOCUMENT_TEXT_DETECTION`, or `CROP_HINTS`.",
      "model" : "Model to use for the feature.\nSupported values: \"builtin/stable\" (the default if unset) and\n\"builtin/latest\".",
      "type" : "The feature type."
    } ],
    "image" : {
      "source" : {
        "imageUri" : "The URI of the source image. Can be either:\n\n1. A Google Cloud Storage URI of the form\n   `gs://bucket_name/object_name`. Object versioning is not supported. See\n   [Google Cloud Storage Request\n   URIs](https://cloud.google.com/storage/docs/reference-uris) for more\n   info.\n\n2. A publicly-accessible image HTTP/HTTPS URL. When fetching images from\n   HTTP/HTTPS URLs, Google cannot guarantee that the request will be\n   completed. Your request may fail if the specified host denies the\n   request (e.g. due to request throttling or DOS prevention), or if Google\n   throttles requests to the site for abuse prevention. You should not\n   depend on externally-hosted images for production applications.\n\nWhen both `gcs_image_uri` and `image_uri` are specified, `image_uri` takes\nprecedence.",
        "gcsImageUri" : "**Use `image_uri` instead.**\n\nThe Google Cloud Storage  URI of the form\n`gs://bucket_name/object_name`. Object versioning is not supported. See\n[Google Cloud Storage Request\nURIs](https://cloud.google.com/storage/docs/reference-uris) for more info."
      },
      "content" : "Image content, represented as a stream of bytes.\nNote: As with all `bytes` fields, protobuffers use a pure binary\nrepresentation, whereas JSON representations use base64."
    },
    "imageContext" : {
      "webDetectionParams" : {
        "includeGeoResults" : "Whether to include results derived from the geo information in the image."
      },
      "cropHintsParams" : {
        "aspectRatios" : [ "number" ]
      },
      "productSearchParams" : {
        "filter" : "The filtering expression. This can be used to restrict search results based\non Product labels. We currently support an AND of OR of key-value\nexpressions, where each expression within an OR must have the same key.\n\nFor example, \"(color = red OR color = blue) AND brand = Google\" is\nacceptable, but not \"(color = red OR brand = Google)\" or \"color: red\".",
        "productCategories" : [ "string" ],
        "boundingPoly" : {
          "vertices" : [ {
            "x" : "X coordinate.",
            "y" : "Y coordinate."
          } ],
          "normalizedVertices" : [ {
            "x" : "X coordinate.",
            "y" : "Y coordinate."
          } ]
        },
        "productSet" : "The resource name of a ProductSet to be searched for similar images.\n\nFormat is:\n`projects/{project_id}/locations/{location_id}/productSets/{product_set_id}`."
      },
      "languageHints" : [ "string" ],
      "latLongRect" : {
        "minLatLng" : {
          "latitude" : "The latitude in degrees. It must be in the range [-90.0, +90.0].",
          "longitude" : "The longitude in degrees. It must be in the range [-180.0, +180.0]."
        },
        "maxLatLng" : {
          "latitude" : "The latitude in degrees. It must be in the range [-90.0, +90.0].",
          "longitude" : "The longitude in degrees. It must be in the range [-180.0, +180.0]."
        }
      }
    }
  } ]
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## async_batch_annotate_files

Run asynchronous image detection and annotation for a list of generic
files, such as PDF files, which may contain multiple pages and multiple
images per page. Progress and results can be retrieved through the
`google.longrunning.Operations` interface.
`Operation.metadata` contains `OperationMetadata` (metadata).
`Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).

<details><summary>Parameters</summary>

### $body

Multiple async file annotation requests are batched into a single service
call.

**Type:** object

```json
{
  "requests" : [ {
    "features" : [ {
      "maxResults" : "Maximum number of results of this type. Does not apply to\n`TEXT_DETECTION`, `DOCUMENT_TEXT_DETECTION`, or `CROP_HINTS`.",
      "model" : "Model to use for the feature.\nSupported values: \"builtin/stable\" (the default if unset) and\n\"builtin/latest\".",
      "type" : "The feature type."
    } ],
    "inputConfig" : {
      "mimeType" : "The type of the file. Currently only \"application/pdf\" and \"image/tiff\"\nare supported. Wildcards are not supported.",
      "gcsSource" : {
        "uri" : "Google Cloud Storage URI for the input file. This must only be a\nGoogle Cloud Storage object. Wildcards are not currently supported."
      }
    },
    "outputConfig" : {
      "gcsDestination" : {
        "uri" : "Google Cloud Storage URI where the results will be stored. Results will\nbe in JSON format and preceded by its corresponding input URI. This field\ncan either represent a single file, or a prefix for multiple outputs.\nPrefixes must end in a `/`.\n\nExamples:\n\n*    File: gs://bucket-name/filename.json\n*    Prefix: gs://bucket-name/prefix/here/\n*    File: gs://bucket-name/prefix/here\n\nIf multiple outputs, each response is still AnnotateFileResponse, each of\nwhich contains some subset of the full list of AnnotateImageResponse.\nMultiple outputs can happen if, for example, the output JSON is too large\nand overflows into multiple sharded files."
      },
      "batchSize" : "The max number of response protos to put into each output JSON file on\nGoogle Cloud Storage.\nThe valid range is [1, 100]. If not specified, the default value is 20.\n\nFor example, for one pdf file with 100 pages, 100 response protos will\nbe generated. If `batch_size` = 20, then 5 json files each\ncontaining 20 response protos will be written under the prefix\n`gcs_destination`.`uri`.\n\nCurrently, batch_size only applies to GcsDestination, with potential future\nsupport for other output configurations."
    },
    "imageContext" : {
      "webDetectionParams" : {
        "includeGeoResults" : "Whether to include results derived from the geo information in the image."
      },
      "cropHintsParams" : {
        "aspectRatios" : [ "number" ]
      },
      "productSearchParams" : {
        "filter" : "The filtering expression. This can be used to restrict search results based\non Product labels. We currently support an AND of OR of key-value\nexpressions, where each expression within an OR must have the same key.\n\nFor example, \"(color = red OR color = blue) AND brand = Google\" is\nacceptable, but not \"(color = red OR brand = Google)\" or \"color: red\".",
        "productCategories" : [ "string" ],
        "boundingPoly" : {
          "vertices" : [ {
            "x" : "X coordinate.",
            "y" : "Y coordinate."
          } ],
          "normalizedVertices" : [ {
            "x" : "X coordinate.",
            "y" : "Y coordinate."
          } ]
        },
        "productSet" : "The resource name of a ProductSet to be searched for similar images.\n\nFormat is:\n`projects/{project_id}/locations/{location_id}/productSets/{product_set_id}`."
      },
      "languageHints" : [ "string" ],
      "latLongRect" : {
        "minLatLng" : {
          "latitude" : "The latitude in degrees. It must be in the range [-90.0, +90.0].",
          "longitude" : "The longitude in degrees. It must be in the range [-180.0, +180.0]."
        },
        "maxLatLng" : {
          "latitude" : "The latitude in degrees. It must be in the range [-90.0, +90.0].",
          "longitude" : "The longitude in degrees. It must be in the range [-180.0, +180.0]."
        }
      }
    }
  } ]
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## async_batch_annotate_images

Run asynchronous image detection and annotation for a list of generic
files, such as PDF files, which may contain multiple pages and multiple
images per page. Progress and results can be retrieved through the
`google.longrunning.Operations` interface.
`Operation.metadata` contains `OperationMetadata` (metadata).
`Operation.response` contains `AsyncBatchAnnotateImagesResponse` (results).

<details><summary>Parameters</summary>

### $body

Multiple async image annotation requests are batched into a single service
call.

**Type:** object

```json
{
  "outputConfig" : {
    "gcsDestination" : {
      "uri" : "Google Cloud Storage URI where the results will be stored. Results will\nbe in JSON format and preceded by its corresponding input URI. This field\ncan either represent a single file, or a prefix for multiple outputs.\nPrefixes must end in a `/`.\n\nExamples:\n\n*    File: gs://bucket-name/filename.json\n*    Prefix: gs://bucket-name/prefix/here/\n*    File: gs://bucket-name/prefix/here\n\nIf multiple outputs, each response is still AnnotateFileResponse, each of\nwhich contains some subset of the full list of AnnotateImageResponse.\nMultiple outputs can happen if, for example, the output JSON is too large\nand overflows into multiple sharded files."
    },
    "batchSize" : "The max number of response protos to put into each output JSON file on\nGoogle Cloud Storage.\nThe valid range is [1, 100]. If not specified, the default value is 20.\n\nFor example, for one pdf file with 100 pages, 100 response protos will\nbe generated. If `batch_size` = 20, then 5 json files each\ncontaining 20 response protos will be written under the prefix\n`gcs_destination`.`uri`.\n\nCurrently, batch_size only applies to GcsDestination, with potential future\nsupport for other output configurations."
  },
  "requests" : [ {
    "features" : [ {
      "maxResults" : "Maximum number of results of this type. Does not apply to\n`TEXT_DETECTION`, `DOCUMENT_TEXT_DETECTION`, or `CROP_HINTS`.",
      "model" : "Model to use for the feature.\nSupported values: \"builtin/stable\" (the default if unset) and\n\"builtin/latest\".",
      "type" : "The feature type."
    } ],
    "inputConfig" : {
      "mimeType" : "The type of the file. Currently only \"application/pdf\" and \"image/tiff\"\nare supported. Wildcards are not supported.",
      "gcsSource" : {
        "uri" : "Google Cloud Storage URI for the input file. This must only be a\nGoogle Cloud Storage object. Wildcards are not currently supported."
      }
    },
    "outputConfig" : {
      "gcsDestination" : {
        "uri" : "Google Cloud Storage URI where the results will be stored. Results will\nbe in JSON format and preceded by its corresponding input URI. This field\ncan either represent a single file, or a prefix for multiple outputs.\nPrefixes must end in a `/`.\n\nExamples:\n\n*    File: gs://bucket-name/filename.json\n*    Prefix: gs://bucket-name/prefix/here/\n*    File: gs://bucket-name/prefix/here\n\nIf multiple outputs, each response is still AnnotateFileResponse, each of\nwhich contains some subset of the full list of AnnotateImageResponse.\nMultiple outputs can happen if, for example, the output JSON is too large\nand overflows into multiple sharded files."
      },
      "batchSize" : "The max number of response protos to put into each output JSON file on\nGoogle Cloud Storage.\nThe valid range is [1, 100]. If not specified, the default value is 20.\n\nFor example, for one pdf file with 100 pages, 100 response protos will\nbe generated. If `batch_size` = 20, then 5 json files each\ncontaining 20 response protos will be written under the prefix\n`gcs_destination`.`uri`.\n\nCurrently, batch_size only applies to GcsDestination, with potential future\nsupport for other output configurations."
    },
    "imageContext" : {
      "webDetectionParams" : {
        "includeGeoResults" : "Whether to include results derived from the geo information in the image."
      },
      "cropHintsParams" : {
        "aspectRatios" : [ "number" ]
      },
      "productSearchParams" : {
        "filter" : "The filtering expression. This can be used to restrict search results based\non Product labels. We currently support an AND of OR of key-value\nexpressions, where each expression within an OR must have the same key.\n\nFor example, \"(color = red OR color = blue) AND brand = Google\" is\nacceptable, but not \"(color = red OR brand = Google)\" or \"color: red\".",
        "productCategories" : [ "string" ],
        "boundingPoly" : {
          "vertices" : [ {
            "x" : "X coordinate.",
            "y" : "Y coordinate."
          } ],
          "normalizedVertices" : [ {
            "x" : "X coordinate.",
            "y" : "Y coordinate."
          } ]
        },
        "productSet" : "The resource name of a ProductSet to be searched for similar images.\n\nFormat is:\n`projects/{project_id}/locations/{location_id}/productSets/{product_set_id}`."
      },
      "languageHints" : [ "string" ],
      "latLongRect" : {
        "minLatLng" : {
          "latitude" : "The latitude in degrees. It must be in the range [-90.0, +90.0].",
          "longitude" : "The longitude in degrees. It must be in the range [-180.0, +180.0]."
        },
        "maxLatLng" : {
          "latitude" : "The latitude in degrees. It must be in the range [-90.0, +90.0].",
          "longitude" : "The longitude in degrees. It must be in the range [-180.0, +180.0]."
        }
      }
    }
  } ]
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## cancel_operation

Starts asynchronous cancellation on a long-running operation.  The server
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

<details><summary>Parameters</summary>

### name (required)

The name of the operation resource to be cancelled.

**Type:** string

### operation_id (required)

Operation ID

**Type:** string

### $body

The request message for Operations.CancelOperation.

**Type:** object

```json
{ }
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## delete_operation

Deletes a long-running operation. This method indicates that the client is
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

<details><summary>Parameters</summary>

### operation_id (required)

Operation ID

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## get_operation

Gets the latest state of a long-running operation.  Clients can use this
method to poll the operation result at intervals as recommended by the API
service.

<details><summary>Parameters</summary>

### operation_id (required)

Operation ID

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## list_operations

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.

<details><summary>Parameters</summary>

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

