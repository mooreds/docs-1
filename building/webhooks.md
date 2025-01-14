---
id: webhooks
title: Webhooks
layout: docs.mustache
tags: doc
---

A Transposit operation can be deployed to consumers as an [HTTP endpoint](/docs/building/endpoints) or as a webhook. The easiest way to create a webhook in Transposit is to:

1. Navigate to **Code**.
2. Create a new operation using the plus icon in the operations list.
3. Select **Webhook** to create a new operation as a webhook.

> You can also manually configure an existing operation to be a webhook by going to **Deploy &gt; Endpoints**. The operation may be in either a normal HTTP endpoint state or the webhook state, but not both at the same time. It is advisable to protect your webhook with an API key.

Once a Transposit operation is deployed as a webhook, it can be executed at the designated URL with either a simple `HTTP GET`, or with an `HTTP POST` that may include payload data.

Deployed webhook Transposit operation URL:

```text
https://{app}.transposit.io/api/v1/execute-http/{operationId}
```

## HTTP Event Information

When deployed as a webhook, the HTTP event information corresponding to the incoming HTTP request (i.e. the webhook callback) can be made available to the Transposit operation. To gain access to the HTTP event information, the Transposit webhook operation must be implemented with exactly one special `'object'` type parameter that is named `'http_event'`. If the deployed webhook is not implemented with this special parameter, then the webhook can still be invoked, but the HTTP event information will not be available to the operation.

The incoming HTTP event information includes the method type, header parameters, query parameters, and body parameter:

```json
{
  "http_method": "POST",
  "body": "Hello World",
  "query_parameters": {
    "api_key": "abc123xyz",
    ...
  },
  "headers": {
    "Content-Type": "text/plain",
    ...
  }
}
```

If the Content-Type is application/xml, application/x-www-form-urlencoded, or text/xml, the event will
also include a key called `parsed_body`, which will contain a JSON representation of the query's body:

```json
{
  "http_method": "POST",
  "body": "key1=value1&key2=value2&key3=value%24",
  "parsed_body": {
    "key1": "value1",
    "key2": "value2",
    "key3": "value&",
  }
  "query_parameters": {
    "api_key": "abc123xyz",
    ...
  },
  "headers": {
    "Content-Type": "application/x-www-form-urlencoded",
    ...
  }
}
```

## Webhook Return Value

The return value of a Transposit webhook operation must be an object containing a status code, header parameters, and a body parameter:

```javascript
function run(params) {
  var entity = {};
  entity["message"] = params.http_event.body;

  return {
    "status_code": 200,
    "headers": {
      "Content-Type": "application/json",
      ...
    },
    "body": entity
  };
}
```

## Webhook Execution

The return value of the Transposit operation will be repackaged as a standard HTTP response to the HTTP request that executed the webhook:

```text
$ curl -i -X POST https://{app}.transposit.io/api/v1/execute-http/{operationId}?api_key=abc123xyz -H "Content-Type: text/plain" -d "Hello World"
```

```text
HTTP/1.1 200 OK
Date: Fri, 03 Aug 2018 21:46:06 GMT
Content-Type: application/json
Content-Length: 25
Connection: keep-alive

{"message":"Hello World"}
```

In the HTTP response, the `"Content-Type"` header will default to `"application/json"` if nothing is provided by the Transposit webhook operation, and the `"Content-Length"` header will automatically be updated to match the final HTTP response entity. The HTTP response entity will closely resemble the body value that is returned from the Transposit webhook operation, but it will not necessarily be identical due to JSON serialization/deserialization.

## Returning Early

It is possible to return early from a deployed webhook and execute additional work asynchronously by leveraging the timing events available in [JavaScript operations](../references/js-operations.md), e.g.

```javascript
function run(params) {
  setImmediate(() => {
    // Do work asynchronously
  });

  var entity = {};
  entity["message"] = "Returning early!";
  return {
    "status_code": 200,
    "headers": {
      "Content-Type": "application/json",
      ...
    },
    "body": entity
  };
}
```

## Dynamic Challenges

Some applications that send HTTP events to a webhook require you to validate ownership of the webhook first before being able to use it in production. This is often done by returning a string that is passed in through a test HTTP event to be verified. A common example of this is [Slack's Events API](https://api.slack.com/events/url_verification) requiring a challenge to be passed before it will send true events to the webhook URL. One can write a statement into a webhook operation that will detect if the event is a challenge, and react accordingly. e.g.

```javascript
let body = http_event.parsed_body;
if (body.challenge) {
  return {
    status_code: 200,
    headers: { "Content-Type": "text/plain" },
    body: body.challenge
  };
}
```
