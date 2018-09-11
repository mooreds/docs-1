# Javascript client

How-to. How to implement in your external app, sample code.

Our javascript SDK makes it simple to deal with login, auths and run operations in your application.

Install with npm:

```text
npm install transposit
```

or with yarn:

```text
yarn add transposit
```

or as a script tag:

```text
<script src="https://unpkg.com/transposit@0.2.1/dist/bundle.prod.js" /></script>
```

## Usage

### Initialization

In order to use the SDK, you'll need to create an instance and give it information about your application.

If you're using a bundler:

esmodules:

```text
import { Transposit } from "transposit";

const transposit = new Transposit(serviceMaintainer, serviceName, transpositUrl);
```

commonjs modules:

```text
const transposit = require("transposit");

const transposit = new Transposit(serviceMaintainer, serviceName, transpositUrl);
```

Or, if you have made the library globally available via a script tag:

```text
var transposit = new Transposit.Transposit(serviceMaintainer, serviceName, transpositUrl);
```

### Login

Once you have configured login for your application \(TODO link to how to configure?\), the JavaScript SDK makes it easy to add login to your application. You'll first want to add a link to start the login process:

```text
<button type="button" onclick="loginWithGoogle()">Login</button>
...
function loginWithGoogle() {
  window.location.href = host + "/app/v1/" + maintainer + "/" + serviceName + "/login/google?redirectUri=" + window.location.origin + window.location.pathname;
    }
```

This kicks off the login flow with Transposit and Google. Note the `redirectUri` query parameter in the url above. This tells Transposit where to send the user after a successful login. This is where the SDK comes into the picture. On the page that the user has been redirected to, simply call

```text
transposit.handleLogin();
```

Under the hood, this goes through a number of steps to ensure your session is set up correctly in the browser. You are now ready to authorize and run operations!

### Authorizations

If your application requires user credentials for data connections, send users to the Transposit-hosted data connections page. You can get the url for this page from the SDK:

```text
transposit.getConnectionLocation();
```

### Running deployed operation

Use the `runOperation()` method to run a deployed operation in your application:

```text
transposit.runOperation("myOperation")
  .then(function(response) {
    // response.result.results contains the results
    // TODO document handling errors
  })
```

`runOperation()` returns a promise which is fulfilled with the results of your operation. If your operation expects parameters, you can pass them in as the second argument:

```text
transposit.runOperation("myOperation", { param1: "hello", param2: "world" })
```

### Log out

Use

```text
transposit.logout();
```

to log the user out of your application.

## API reference

### `transposit.handleLogin()`

Reads login information from the url and stores the claims object in localStorage for use in subsequent api calls. This is used after google login redirect.

**Returns** \(String\): The subject for which the claim was issued

**Example**

```javascript
transposit.handleLogin()
// => "yoko"
```

### `transposit.isLoggedIn()`

**Returns** \(boolean\): True if there exists login information \(does not check if the token is expired\).

### `transposit.logOut()`

Invalidates stored claims and clears them from localStorage.

**Returns**: null

### `transposit.runOperation(operation, [params={}])`

Runs an operation.

| Argument | Type |  |
| :--- | :--- | :--- |
| operation | String | the name of the operation to be run |
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

| Argument | Type |  |
| :--- | :--- | :--- |
| \[redirectUri=window.location.href\] | String | an optional param to specify an alternate redirectUri |

**Returns** \(String\): A url to redirect to for user authorization.

**Example**

```javascript
transposit.getConnectLocation("localhost");
// => "https://api.transposit.com/app/v1/gardener/hose/connect?redirectUri=localhost"
```

### `transposit.getGoogleLoginLocation([redirectUri=window.location.href])`

Runs an operation.

| Argument | Type |  |
| :--- | :--- | :--- |
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
transposit.getUserInfo()
// => "yoko"
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

