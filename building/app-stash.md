---
id: app-stash
title: Application stash
layout: docs.mustache
tags: doc
---

Transposit operations can store and read data from a key-value stash during the operation runtime.

## Programmatic interface

Visit the [JavaScript operation documentation](/docs/references/js-operations#stash) for information on programmatically accessing the application stash.

## Development context

When running operations through the Transposit console, e.g. while developing an application, the development context stash is used.

Each developer has their own development context per application in the Transposit console. This means that when two developers `devA` and `devB` both view the same application `transposit/sample` in the Transposit console and both run operations that read from and write to the development stash, all of their stashed data is isolated in such a way that they cannot access each other's stashed values, much like how your credentials for an application in the development context are not ever viewable by other developers.

The contents in the development context stash can be viewed and managed under **Code &gt; Development &gt; Stash**; a developer can only see the contents of their own development context stash.

## Production context

When deployed operations are executed in the production context (e.g. a deployed webhook), the production context stash is used. The production context stash is not specific to any developer. The production context stash is also used when operations run as part of scheduled tasks.

The contents in the production context stash can be viewed and managed under **Deploy &gt; Production Stash**; only editors of the application have access to the production context stash.

## Limits

Each stash in an application (e.g. the production context stash, the development context stash for `devA`, or the development context stash for `devB`) is subject to a size limit of 64 KB. This size limit includes key values as well as key names.

An operation will fail if it tries to write to a full stash. In order to free up stash space, data needs to be deleted either programmatically through an operation or manually through the appropriate management UI.

## Feature boundaries

The functionality of the application stash can be entirely replaced by a third party data connector like Airtable or Google Spreadsheet. As such, the application stash exists purely for convenience and to reduce friction in the early application development cycle. Advanced developers with more complex use cases may end up "graduating out" of using the application stash if the feature boundaries are insufficient for their needs.

- There are no guarantees about behavior during concurrent execution, e.g. if two webhooks trigger at the same time and both simultaneously write different values to the same stash key, the behavior is non-deterministic.
- While data stored in the application stash will be encrypted-at-rest, storing sensitive information is at the discretion of the developer.
