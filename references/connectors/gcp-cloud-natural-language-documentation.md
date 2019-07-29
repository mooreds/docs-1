---
id: gcp-cloud-natural-language-documentation
title: GCP Cloud Natural Language (version v1.*.*)
sidebar_label: GCP Cloud Natural Language
layout: docs.mustache
---

## analyze_entities

Finds named entities (currently proper names and common nouns) in the text
along with entity types, salience, mentions for each entity, and
other properties.

<details><summary>Parameters</summary>

### $body

The entity analysis request message.

**Type:** object

```json
{
  "document" : {
    "gcsContentUri" : "The Google Cloud Storage URI where the file content is located.\nThis URI must be of the form: gs://bucket_name/object_name. For more\ndetails, see https://cloud.google.com/storage/docs/reference-uris.\nNOTE: Cloud Storage object versioning is not supported.",
    "language" : "The language of the document (if not specified, the language is\nautomatically detected). Both ISO and BCP-47 language codes are\naccepted.\n[Language Support](/natural-language/docs/languages)\nlists currently supported languages for each API method.\nIf the language (either specified by the caller or automatically detected)\nis not supported by the called API method, an `INVALID_ARGUMENT` error\nis returned.",
    "type" : "Required. If the type is not set or is `TYPE_UNSPECIFIED`,\nreturns an `INVALID_ARGUMENT` error.",
    "content" : "The content of the input in string format.\nCloud audit logging exempt since it is based on user data."
  },
  "encodingType" : "The encoding type used by the API to calculate offsets."
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

## analyze_entity_sentiment

Finds entities, similar to AnalyzeEntities in the text and analyzes
sentiment associated with each entity and its mentions.

<details><summary>Parameters</summary>

### $body

The entity-level sentiment analysis request message.

**Type:** object

```json
{
  "document" : {
    "gcsContentUri" : "The Google Cloud Storage URI where the file content is located.\nThis URI must be of the form: gs://bucket_name/object_name. For more\ndetails, see https://cloud.google.com/storage/docs/reference-uris.\nNOTE: Cloud Storage object versioning is not supported.",
    "language" : "The language of the document (if not specified, the language is\nautomatically detected). Both ISO and BCP-47 language codes are\naccepted.\n[Language Support](/natural-language/docs/languages)\nlists currently supported languages for each API method.\nIf the language (either specified by the caller or automatically detected)\nis not supported by the called API method, an `INVALID_ARGUMENT` error\nis returned.",
    "type" : "Required. If the type is not set or is `TYPE_UNSPECIFIED`,\nreturns an `INVALID_ARGUMENT` error.",
    "content" : "The content of the input in string format.\nCloud audit logging exempt since it is based on user data."
  },
  "encodingType" : "The encoding type used by the API to calculate offsets."
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

## analyze_sentiment

Analyzes the sentiment of the provided text.

<details><summary>Parameters</summary>

### $body

The sentiment analysis request message.

**Type:** object

```json
{
  "document" : {
    "gcsContentUri" : "The Google Cloud Storage URI where the file content is located.\nThis URI must be of the form: gs://bucket_name/object_name. For more\ndetails, see https://cloud.google.com/storage/docs/reference-uris.\nNOTE: Cloud Storage object versioning is not supported.",
    "language" : "The language of the document (if not specified, the language is\nautomatically detected). Both ISO and BCP-47 language codes are\naccepted.\n[Language Support](/natural-language/docs/languages)\nlists currently supported languages for each API method.\nIf the language (either specified by the caller or automatically detected)\nis not supported by the called API method, an `INVALID_ARGUMENT` error\nis returned.",
    "type" : "Required. If the type is not set or is `TYPE_UNSPECIFIED`,\nreturns an `INVALID_ARGUMENT` error.",
    "content" : "The content of the input in string format.\nCloud audit logging exempt since it is based on user data."
  },
  "encodingType" : "The encoding type used by the API to calculate sentence offsets."
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

## analyze_syntax

Analyzes the syntax of the text and provides sentence boundaries and
tokenization along with part of speech tags, dependency trees, and other
properties.

<details><summary>Parameters</summary>

### $body

The syntax analysis request message.

**Type:** object

```json
{
  "document" : {
    "gcsContentUri" : "The Google Cloud Storage URI where the file content is located.\nThis URI must be of the form: gs://bucket_name/object_name. For more\ndetails, see https://cloud.google.com/storage/docs/reference-uris.\nNOTE: Cloud Storage object versioning is not supported.",
    "language" : "The language of the document (if not specified, the language is\nautomatically detected). Both ISO and BCP-47 language codes are\naccepted.\n[Language Support](/natural-language/docs/languages)\nlists currently supported languages for each API method.\nIf the language (either specified by the caller or automatically detected)\nis not supported by the called API method, an `INVALID_ARGUMENT` error\nis returned.",
    "type" : "Required. If the type is not set or is `TYPE_UNSPECIFIED`,\nreturns an `INVALID_ARGUMENT` error.",
    "content" : "The content of the input in string format.\nCloud audit logging exempt since it is based on user data."
  },
  "encodingType" : "The encoding type used by the API to calculate offsets."
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

## annotate_text

A convenience method that provides all the features that analyzeSentiment,
analyzeEntities, and analyzeSyntax provide in one call.

<details><summary>Parameters</summary>

### $body

The request message for the text annotation API, which can perform multiple
analysis types (sentiment, entities, and syntax) in one call.

**Type:** object

```json
{
  "features" : {
    "extractEntities" : "Extract entities.",
    "extractSyntax" : "Extract syntax information.",
    "classifyText" : "Classify the full document into categories.",
    "extractDocumentSentiment" : "Extract document-level sentiment.",
    "extractEntitySentiment" : "Extract entities and their associated sentiment."
  },
  "document" : {
    "gcsContentUri" : "The Google Cloud Storage URI where the file content is located.\nThis URI must be of the form: gs://bucket_name/object_name. For more\ndetails, see https://cloud.google.com/storage/docs/reference-uris.\nNOTE: Cloud Storage object versioning is not supported.",
    "language" : "The language of the document (if not specified, the language is\nautomatically detected). Both ISO and BCP-47 language codes are\naccepted.\n[Language Support](/natural-language/docs/languages)\nlists currently supported languages for each API method.\nIf the language (either specified by the caller or automatically detected)\nis not supported by the called API method, an `INVALID_ARGUMENT` error\nis returned.",
    "type" : "Required. If the type is not set or is `TYPE_UNSPECIFIED`,\nreturns an `INVALID_ARGUMENT` error.",
    "content" : "The content of the input in string format.\nCloud audit logging exempt since it is based on user data."
  },
  "encodingType" : "The encoding type used by the API to calculate offsets."
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

## classify_text

Classifies a document into categories.

<details><summary>Parameters</summary>

### $body

The document classification request message.

**Type:** object

```json
{
  "document" : {
    "gcsContentUri" : "The Google Cloud Storage URI where the file content is located.\nThis URI must be of the form: gs://bucket_name/object_name. For more\ndetails, see https://cloud.google.com/storage/docs/reference-uris.\nNOTE: Cloud Storage object versioning is not supported.",
    "language" : "The language of the document (if not specified, the language is\nautomatically detected). Both ISO and BCP-47 language codes are\naccepted.\n[Language Support](/natural-language/docs/languages)\nlists currently supported languages for each API method.\nIf the language (either specified by the caller or automatically detected)\nis not supported by the called API method, an `INVALID_ARGUMENT` error\nis returned.",
    "type" : "Required. If the type is not set or is `TYPE_UNSPECIFIED`,\nreturns an `INVALID_ARGUMENT` error.",
    "content" : "The content of the input in string format.\nCloud audit logging exempt since it is based on user data."
  }
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

