---
id: create-a-data-connector
title: Creating a basic data connector
layout: docs.mustache
tags: doc
---

Suppose you have a public API with JSON data accessible at [a URL like this](https://api.jsonbin.io/b/5c5cded2e9e7c118390e07d5): `https://api.jsonbin.io/b/5c5cded2e9e7c118390e07d5`.

Using SwaggerHub or similar editor, you can implement an OpenAPI (f.k.a. Swagger) file representing this single API endpoint.

To turn an OpenAPI file into a basic data connector in Transposit:

## 1. Create an application

Create a new Transposit application with a sensible name, e.g. `yourname/bare_bones`.

## 2. Clone the repository

Clone the application's code repository, e.g.:

```bash
  git clone https://console.transposit.com/git/yourname/bare_bones
```

If you are using SSO (e.g. Google, Slack, GitHub) to sign in to Transposit, you will need to use your **Git access token** located [here](https://console.transposit.com/settings) as your password when using Git with Transposit. 

## 3. Modify the source code

Update the application's source code tree to contain two files, `manifest.json` and `bare_bones.yaml`. Note that this may require deleting existing boilerplate code.
      
`manifest.json`

```json
{
  "v2": {
    "swagger": {
      "source": "bare_bones.yaml"
    }
  }
}
```

You will also need to specify what authentication the API uses (e.g. OAuth, query or path parameters, basic, etc.) in your `manifest.json`. See the [Connector Authentication](#connector-authentication) section for more info. 

`bare_bones.yaml`

```yaml
openapi: 3.0.0
servers:
  - url: https://api.jsonbin.io
info:
  version: "1.0.0"
  title: Exemplary Bare Bones API
paths:
  /b/5c5cded2e9e7c118390e07d5:
    get:
      operationId: getFunData
      responses:
        '200':
          description: Easy
```

## 4. Commit and push

Commit your changes and push back to Transposit. Transposit will run some validation on your OpenAPI file. 

## 5. Add the data connector to an existing application

You can now add your data connector `yourname/bare_bones` as a dependency in another Transposit application. Then you can invoke the `getFunData` operation.

## Connector Authentication

Specify the type of authentication your data connector uses in your `manifest.json`. Use the appropriate authentication described in the sections below. 

### Auth via HTTP basic authentication

For data connectors that implement authentication with HTTP basic authentication, Transposit will ask for the username/password, Base64 encode the concatenation of the two, and dump that into an `Authorization: Basic` header.

In your `manifest.json`, you will need to set the `type` value to `"BASIC"`. For example: 

```json
"auth": {
  "description": "Find your username and password at ...",
  "type": "BASIC"
}
```

### Auth via header parameters

For data connections that implement authentication with header parameters, the header parameter name (as documented by the external API site) and header parameter value (typically a secret token distributed by the external API site) must be provided when adding the connection to an application.

In your `manifest.json`, you will need to set the `type` value to `"HEADER"`. For example, the below code will send a header with the key `"Authorization"` (i.e. `-H "Authorization: <token>"`): 

```json
"auth" {
    "description": "Find your token here! http://myservice.io",
    "type": "HEADER",
    "params": {
        "header": {
            "string": "Authorization"
        }
    }
}
```

The `description` field will show for all non-OAuth types in the auth modal within Transposit. It is recommended to include information about where to get the token and how to format it.

### Auth via query parameters

For data connections that implement authentication with query parameters, only the query parameter value (typically a secret distributed by the external API site) must be provided when adding the connection to an application.

For example, if the URL in your OpenAPI file is something like: `/getapps?api_key=<token>`

In your `manifest.json`, you will need to set the `type` value to `"PARAMETER"`. For example: 

```json
"auth": { 
    "type": "PARAMETER",
    "params": {
        "name": {
            "string": "api_key"
        }
    }
}
```

Make sure to change the `string` value to what the API uses. 

### Auth via path parameters

For data connections that implement authentication with path parameters, only the path parameter value (typically a secret distributed by the external API site) must be provided when adding the connection to an application. 

For example, if the URL in your OpenAPI file is something like: `/v1/myapi/{api_key}/create`

In your `manifest.json`, you will need to set the `type` value to `"PATH"`. For example: 

```json
"auth": {
    "type": "PATH",
        "params": {
        "path": {
            "string": "api_key"
        }
    }
}
```

Make sure to change the `string` value to what the API uses. 

### Auth via OAuth 2.0

For data connections that implement authentication with OAuth 2.0, Transposit uses a combination of the `OAuthConfig` and a `params` property as described below to indicate how to send the access token in the second leg of OAuth.

In your `manifest.json`, you will need to set the `type` value to `"OAUTH"`. For example, this code will send a header of the form `Authorization: Bearer <token>`:

```json
"auth": {
  "type": "OAUTH",
  "params": {
      "header": {
        "string": "Authorization"
      },
      "type": {
        "string": "Bearer"
      }
  },
  "oauthConfig": {
    "name": "",  // The name of the data connector
    "authUri": "",  // URL to request authorization, probably has /authorize in its path
    "accessTokenUri": "",  // URL to request the token, probably has /token in its path
    "responseType": "code",  // This will send "response_type: code" in the access request
    "oauthDocumentation": "",  // Link to the documentation, not required
    "scope": "",  // The access scopes you're requesting for your app
    "parameterLocation": "",  // Where to send the client id / secret. Either "QUERY" or "BODY" (form parameters), defaults to QUERY
    "needsBasicAuthHeader": "",  // If the connector needs its client id and secret sent in the form Authorization: Basic base64(client_id:client_secret)
    "accessType": "offline",  // empirically only for Google apis
    "prompt": "select_account consent",  //empirically only for Google apis
    "accessTokenMethod": "GET", // GET or POST to make to the oauth endpoint
    "accessTokenPath": "access_token" // What value in the returned map holds the access token
  }  
}
```

Some service might require [parameter auth](#Auth-via-query-parameters) instead.

### Auth via password

For data connections that implement authentication with a username and password, when users add a credential, Transposit does a POST to the login form and extracts out a response, usually from a set-cookie header. This way Transposit can use an auth token for future API requests.

In your `manifest.json`, you will need to set the `type` value to `"PASSWORD"`. For example:

```json
"auth": {
  "type": "PASSWORD",
    "params": {
      "form": {
        "url": {
          "string": "https://api.example.com/v1/authentication/login"
        },
        "form": {
          "value": [
            {
              "key": "username",
              "type": "STRING",
              "val": "{{{username}}}"
            },
            {
              "key": "password",
              "type": "STRING",
              "val": "{{{password}}}"
            },
            {
              "key": "persistLogin",
              "type": "BOOLEAN",
              "val": "true"
            }
          ]
        }
      },
      "extract": {
        "string": "$.headers.Set-Cookie.['EqAuth.v1']"
      },
      "header": {
        "string": "Cookie"
      }
    }
}
```
The various pieces include:

- `url`: This is the URL that the login form posts to. Usually, you can find this as the form action.
- `form`: These are the form values Transposit posts to the login URL. They typically include username, password, and a rememberMe boolean. The username and password form that the user sees returns variables for username and password, so you can use mustache style templating (e.g. `{{{example}}}`) to use those values in the post.
- `extract`: Transposit uses a JSON path extractor to extract the cookie or token from the response. You can use any standard JSON path syntax to extract (e.g. notice the escape syntax in the example above to escape a dot in one of the keys).
- `header`: The header you want to send with following authorized requests. Usually, this is `"Cookie"`.

### Auth via runtime

Runtime auth can be used for connectors that require an authentication configuration that does not match the other authentication styles that Transposit supports. Unlike the other authentication styles that have a predefined way of consuming credentials (e.g. Transposit knows to take a Header auth type credential and pass it into the HTTP request as a header parameter), the runtime authentication type leaves consumption of the credential up to you.

In your `manifest.json`, you will need to set the `type` value to `"RUNTIME"`. For example:

```json 
"auth": {
  "type": "RUNTIME",
  "params": {
      "runtime": {
          "runtimeAuth": {
              "paramNames": ["api_key", "client_secret"]
          }
      }
  }
}
```

In this example, the runtime auth includes two parameters that the user will be prompted to provide values for in the UI, similar to other form-like auth types.

Transposit will not automatically do anything with the runtime authentication credential as part of invoking the data connector's operations; instead, the user can retrieve the credential values through a JavaScript operation by invoking the special API method:

```javascript
function example() {
    return api.auths("connectorAlias");
}
```

Which will return a JavaScript object with the credential values:

```json
{
    "api_key": "abc123",
    "client_secret": "def456"
}
```

The user can now retrieve these credential values in the Transposit operation code, form them into whatever auth configuration style the data connector expects, and then pass them into the data connector's operations just like any other parameters.
