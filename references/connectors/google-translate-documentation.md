---
id: google-translate-documentation
title: Google Translate (version v1.*.*)
sidebar_label: Google Translate
layout: docs.mustache
---

## detect_language

Detects the language of text within a request.

<details><summary>Parameters</summary>

### $body

The request message for language detection.

**Type:** object

```json
{
  "q" : [ "string" ]
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

### pp

Pretty-print response.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## list_languages

Returns a list of supported languages for translation.

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

### model

The model type for which supported languages should be returned.

**Type:** string

### pp

Pretty-print response.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### target

The language to use to return localized, human readable names of supported
languages.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## translate

Translates input text, returning translated text.

<details><summary>Parameters</summary>

### $body

The main translation request message for the Cloud Translation API.

**Type:** object

```json
{
  "q" : [ "string" ],
  "format" : "The format of the source text, in either HTML (default) or plain-text. A\nvalue of \"html\" indicates HTML and a value of \"text\" indicates plain-text.",
  "model" : "The `model` type requested for this translation. Valid values are\nlisted in public documentation.",
  "source" : "The language of the source text, set to one of the language codes listed in\nLanguage Support. If the source language is not specified, the API will\nattempt to identify the source language automatically and return it within\nthe response.",
  "target" : "The language to use for translation of the input text, set to one of the\nlanguage codes listed in Language Support."
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

### pp

Pretty-print response.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

