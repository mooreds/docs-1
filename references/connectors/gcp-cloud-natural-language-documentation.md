---
id: gcp-cloud-natural-language-documentation
title: GCP Cloud Natural Language (version v1.*.*)
sidebar_label: GCP Cloud Natural Language
layout: docs.mustache
---

## analyze_entities

Finds named entities (currently proper names and common nouns) in the text along with entity types, salience, mentions for each entity, and other properties.

<details><summary>Parameters</summary>

#### $body

The entity analysis request message.

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

## analyze_entity_sentiment

Finds entities, similar to AnalyzeEntities in the text and analyzes sentiment associated with each entity and its mentions.

<details><summary>Parameters</summary>

#### $body

The entity-level sentiment analysis request message.

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

## analyze_sentiment

Analyzes the sentiment of the provided text.

<details><summary>Parameters</summary>

#### $body

The sentiment analysis request message.

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

## analyze_syntax

Analyzes the syntax of the text and provides sentence boundaries and tokenization along with part of speech tags, dependency trees, and other properties.

<details><summary>Parameters</summary>

#### $body

The syntax analysis request message.

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

## annotate_text

A convenience method that provides all the features that analyzeSentiment, analyzeEntities, and analyzeSyntax provide in one call.

<details><summary>Parameters</summary>

#### $body

The request message for the text annotation API, which can perform multiple analysis types (sentiment, entities, and syntax) in one call.

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

## classify_text

Classifies a document into categories.

<details><summary>Parameters</summary>

#### $body

The document classification request message.

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

