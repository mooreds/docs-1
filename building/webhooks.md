# Webhooks

A Transposit operation can be deployed to consumers as an API endpoint, or it can be deployed as a webhook. The operation may be in either of these deployment states, but not both at the same time, and there is a distinct URL for each deployment state.

Once a Transposit operation is deployed as a webhook, it can be executed at the designated URL with either a simple `HTTP GET`, or with an `HTTP POST` that may include payload data.

Deployed non-webhook Transposit operation URL:

```text
https://api.transposit.com/app/v1/{maintainer}/{serviceName}/api/execute/{operationId}
```

Deployed webhook Transposit operation URL:

```text
https://api.transposit.com/app/v1/{maintainer}/{serviceName}/api/execute-http/{operationId}
```

## HTTP Event Information

When deployed as a webhook, the HTTP event information corresponding to the incoming HTTP request (i.e. the webhook callback) can be made available to the Transposit operation. To gain access to the HTTP event information, the Transposit webhook operation must be implemented with exactly one special `'object'` type parameter that is named `'http_event'`. If the deployed webhook is not implemented with this special parameter, then the webhook can still be invoked, but the HTTP event information will not be available to the operation.

The incoming HTTP event information includes the method type, header parameters, query parameters, and body parameter:

```text
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

## Webhook Return Value

The return value of a Transposit webhook operation must be an object containing a status code, header parameters, and a body parameter:

```text
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
$ curl -i -X POST https://api.transposit.com/app/v1/{maintainer}/{serviceName}/api/execute-http/{operationId}?api_key=abc123xyz -H "Content-Type: text/plain" -d "Hello World"
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
