---
id: environment-variables
title: Environment variables
layout: docs.mustache
tags: doc
---

Application-specific settings can be stored in environment variables. Environment variables are great for storing values that shouldn’t be kept directly in the code for security or code hygiene reasons, and which shouldn’t transfer with the source code when the app is forked.

Environment variables are stored encrypted-at-rest.

## Programmatic interface

Please see the [JavaScript operation documentation](/docs/references/js-operations#environment-variables) for information on programmatically accessing environment variables.

## Development context

When running operations through the Transposit console the development context is used.

Each developer has their own development context per application in the Transposit console. The environment variables set in that context can be managed under **Code &gt; Auth &amp; settings**. A developer can only see their own settings.

## Production context

When deployed operations are executed through deployment or a scheduled task, the production context is used.

The environment variables in the production context can be viewed and managed under **Deploy &gt; Environment Variables**.
