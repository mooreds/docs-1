# JavaScript SDK

The Transposit JavaScript SDK makes it simple to deal with login, authentication, and running operations in your application. For instructions on implementing the SDK and basic usage, see this guide:

{% page-ref page="../building/js-sdk.md" %}

## Reference

### `transposit.handleLogin()`

Reads login information from the url and stores the claims object in localStorage for use in subsequent api calls. This is used after google login redirect.

**Returns** \(String\): The subject for which the claim was issued

**Example**

```javascript
transposit.handleLogin();
// => "patjones"
```

### `transposit.isLoggedIn()`

**Returns** \(boolean\): True if there exists login information \(does not check if the token is expired\).

### `transposit.logOut()`

Invalidates stored claims and clears them from localStorage.

**Returns**: null

### `transposit.runOperation(operation, [params={}])`

Runs an operation.

| Argument      | Type   |                                                       |
| :------------ | :----- | :---------------------------------------------------- |
| operation     | String | the name of the operation to be run                   |
| \[params={}\] | Object | an object containing any operation-defined parameters |

**Returns** \(EndRequestLog\): Returns the operation results and metadata about that result

**Example**

```javascript
transposit.runOperation("this.helloworld");
// => { status: "SUCCESS", result: { results: [{"Hello": "World"}] } }

transposit.runOperation("source.users", { id: params.userId });
// => { status: "ERROR", result: { exceptionLog: { message: "Failed to find user 123" } } }
```

### `transposit.getConnectLocation([redirectUri=window.location.href])`

| Argument                             | Type   |                                                       |
| :----------------------------------- | :----- | :---------------------------------------------------- |
| \[redirectUri=window.location.href\] | String | an optional param to specify an alternate redirectUri |

**Returns** \(String\): A url to redirect to for user authorization.

**Example**

```javascript
transposit.getConnectLocation("localhost");
// => "https://api.transposit.com/app/v1/gardener/hose/connect?redirectUri=localhost"
```

### `transposit.getGoogleLoginLocation([redirectUri=window.location.href])`

Runs an operation.

| Argument                             | Type   |                                                       |
| :----------------------------------- | :----- | :---------------------------------------------------- |
| \[redirectUri=window.location.href\] | String | an optional param to specify an alternate redirectUri |

**Returns** \(String\): A url to redirect to for google login.

**Example**

```javascript
transposit.getConnectLocation("localhost");
// => "https://api.transposit.com/app/v1/gardener/hose/login/google?redirectUri=localhost"
```

### `transposit.getUserInfo()`

Returns available user information.

**Returns** \(String\): The subject for which the claim was issued

**Example**

```javascript
transposit.getUserInfo();
// => "patjones"
```

## EndRequestLog format

The full format of the return object for `transposit.runOperation`

```javascript
export interface EndRequestLog {
  status: "SUCCESS" | "ERROR";
  requestId: string;
  timestamp: string;
  serviceName: string;
  serviceMaintainer: string;
  operationId: string;
  resultActionId?: string;
  result: EndRequestLogResult;
}

export interface EndRequestLogResult {
  results?: any[];
  exceptionLog?: ExceptionLog;
}

export interface ExceptionLog {
  message?: string;
  stackTrace?: string;
  exceptionClass?: string;
  details?: ExceptionLogDetails;
}

export interface ExceptionLogDetails {
  httpLog?: HttpLog;
  scriptExceptionLog?: ScriptExceptionLog;
  type: "HTTP" | "SCRIPTEXCEPTION" | "DETAILSNOTSET";
}

export interface HttpLog {
  uri: string;
  statusCode: number;
  response?: string;
  curlCommand?: string;
}

export interface ScriptExceptionLog {
  line: number;
  column?: number;
}
```
