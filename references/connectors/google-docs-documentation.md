---
id: google-docs-documentation
title: Google Docs (version v1.*.*)
sidebar_label: Google Docs
layout: docs.mustache
---

## batch_update_document

Applies one or more updates to the document. Each request is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests. For example, suppose you call batchUpdate with four updates, and only the third one returns information. The response would have two empty replies, the reply to the third request, and another empty reply, in that order. Because other users may be editing the document, the document might not exactly reflect your changes: your changes may be altered with respect to collaborator changes. If there are no collaborators, the document should reflect your changes. In any case, the updates in your request are guaranteed to be applied together atomically.

<details><summary>Parameters</summary>

#### documentId (required)

The ID of the document to update.

**Type:** string

#### $body

Request message for BatchUpdateDocument.

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

## create_document

Creates a blank document using the title given in the request. Other fields in the request, including any provided content, are ignored. Returns the created document.

<details><summary>Parameters</summary>

#### $body

A Google Docs document.

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

## get_document

Gets the latest version of the specified document.

<details><summary>Parameters</summary>

#### documentId (required)

The ID of the document to retrieve.

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

#### suggestionsViewMode

The suggestions view mode to apply to the document. This allows viewing the document with all suggestions inline, accepted or rejected. If one is not specified, DEFAULT_FOR_CURRENT_ACCESS is used.

**Type:** string

**Potential values:** DEFAULT_FOR_CURRENT_ACCESS, SUGGESTIONS_INLINE, PREVIEW_SUGGESTIONS_ACCEPTED, PREVIEW_WITHOUT_SUGGESTIONS

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

