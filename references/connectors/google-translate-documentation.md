---
id: google-translate-documentation
title: Google Translate (version v1.*.*)
sidebar_label: Google Translate
layout: docs.mustache
---

## detect_language

Detects the language of text within a request.

<details><summary>Parameters</summary>

#### $body

The request message for language detection.

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## list_languages

Returns a list of supported languages for translation.

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

#### model

The model type for which supported languages should be returned.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### target

The language to use to return localized, human readable names of supported
languages.

**Type:** string

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## translate

Translates input text, returning translated text.

<details><summary>Parameters</summary>

#### $body

The main translation request message for the Cloud Translation API.

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

#### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>
