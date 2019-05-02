---
id: endpoints
title: Endpoints
layout: docs.mustache
nav-dark: true
---

Deploy an operation as an endpoint to make it callable over HTTP. Optionally, configure the endpoint to require authentication or act as a [webhook](./webhooks.md).

## Deploy an operation

1. Navigate to **Deploy &gt; Endpoints**.
2. Find the operation you want to deploy.
3. Choose **Deployed** from the dropdown menu.
4. Save your changes.

The HTTP path, method, body, and query parameters for calling your endpoint will vary with configuration. Consult the inline documentation on the **Endpoints** page to call your endpoint.

## Authentication

An endpoint can be publicly available, protected by sign-in, or protected by an API key.

### Publicly available

Publicly available endpoints are callable without any form of authentication. They are typically called from client-side code like a web app or mobile app.

To configure your endpoint as publicly available, do _not_ select **Require API key** or **Require user sign-in**.

### Require API key

Endpoints protected by an API key are authenticated by a query parameter `api_key`. They are typically called from server-side code.

To protect your endpoint with an API key, select **Require API key**.

To manage your API key, navigate to **Deploy &gt; API Key**.

### Require user sign-in

Endpoints protected by user sign-in are authenticated by session cookies. They must be called from a web page where a user is signed-in.

To protect your endpoint with user sign-in, select **Require user sign-in**.

If you are developing a [hosted app](./hosted-apps.md), configure sign-in to call these endpoints. If you are hosting your own web page, use the [JavaScript SDK](./js-sdk.md).

### Webhook

Some third-party services offer to send a HTTP request to a custom URL when an event occurs. This interaction is commonly referred to as a webhook.

To receive these HTTP requests, select **Deploy as webhook**. The inline documentation on the **Endpoints** page will include the URL to provide to the third-party.

Read more about deploying an operation as a webhook on our [webhooks documentation](./webhooks.md).