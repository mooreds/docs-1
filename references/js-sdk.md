# JavaScript SDK

The Transposit JavaScript SDK makes it simple to deal with login, authentication, and running operations in your application. For instructions on implementing the SDK and basic usage, see this guide:

{% page-ref page="../building/js-sdk.md" %}

## Reference

### `transposit.handleLogin([callback])`

Reads login information from the url and stores the claims object in localStorage for use in subsequent api calls. This is used after google login redirect. This function redirects the user to authenticate if they are missing credentials.

If a callback is provided, it will be called after successful login .

**Returns** void

**Example**

```javascript
// call this when your handle-redirect page loads
try {
  transposit.handleLogin(({needsKeys}) => {
    if (needsKeys === true) {
      // user has not yet provided all credentials
    }
  });
} catch (err) {
  // do nothing if this page is viewable when you are not logging in
}
```

### `transposit.isLoggedIn()`

**Returns** \(boolean\): True if there exists login information \(does not check if the token is expired\).

### `transposit.logOut()`

Invalidates stored claims and clears them from localStorage.

**Returns**: Promise&lt;void&gt;

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

### `transposit.getUserName()`

Returns the full name of the logged-in user.

**Returns** \(String\): The full name of the logged-in user

**Example**

```javascript
transposit.getUserName();
// => "Pat Jones"
```

### `transposit.getUserEmail()`

Returns the email address of the signed-in user.

**Returns** \(String\): The email address of the signed-in user

**Example**

```javascript
transposit.getUserEmail();
// => "patjones@gmail.com"
```

## EndRequestLog format

The full format of the return object for `transposit.runOperation`

```javascript
export interface EndRequestLog {
  status: "SUCCESS" | "ERROR" | "CANCELLED" | "TIMEOUT";
  requestId: string;
  result: EndRequestLogResult;
}

export interface EndRequestLogResult {
  results?: any[];
  exceptionLog?: ExceptionLog;
}

export interface ExceptionLog {
  message?: string;
}
```
