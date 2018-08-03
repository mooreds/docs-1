# Webhooks

### Operation Deployment
A Transposit operation can be deployed to consumers through an API endpoint, or it can be deployed as a webhook. The operation can only be in one deployment state at any given time, and there are two distinct URLs for each deployment state.

Once a Transposit operation is deployed as a webhook, it can be executed at the designated URL with either a simple `HTTP GET`, or with an `HTTP POST` that may include payload data.

Deployed non-webhook Transposit operation URL:
- https://api.transposit.com/app/v1/{maintainer}/{serviceName}/api/execute/{operationId}

Deployed webhook Transposit operation URL:
- https://api.transposit.com/app/v1/{maintainer}/{serviceName}/api/execute-http/{operationId}

### HTTP Event Information
When deployed as a webhook, the HTTP event information corresponding to the incoming HTTP request _(i.e. the webhook callback)_ can be made available to the Transposit operation. To gain access to the HTTP event information, the Transposit webhook operation must be implemented with exactly one special `'object'` type parameter that is exactly named `'http_event'`. If the deployed webhook is not implemented with this special parameter, then the webhook can still be invoked, but the HTTP event information will not be available to the operation.

The incoming HTTP event information includes the method type, header parameters, query parameters, and body parameter, e.g.

```
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

### Webhook Return Value
The return value of a Transposit webhook operation must be an object containing a status code, header parameters, and a body parameter, e.g.
```
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

### Webhook Execution
The return value of the Transposit operation will be repackaged as a standard HTTP response to the HTTP request that executed the webhook, e.g.

```
$ curl -i -X POST https://api.transposit.com/app/v1/{maintainer}/{serviceName}/api/execute-http/{operationId}?api_key=abc123xyz -H "Content-Type: text/plain" -d "Hello World"
```
```
HTTP/1.1 200 OK
Date: Fri, 03 Aug 2018 21:46:06 GMT
Content-Type: application/json
Content-Length: 25
Connection: keep-alive

{"message":"Hello World"}
```

In the HTTP response, the `"Content-Type"` header will default to `"application/json"` if nothing is provided by the Transposit webhook operation, and the `"Content-Length"` header will automatically be updated to match the final HTTP response entity--the HTTP response entity will closely resemble the body value that is returned from the Transposit webhook operation, but it will not necessarily be exactly the same due to JSON serialization/deserialization.
