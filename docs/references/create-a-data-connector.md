---
id: create-a-data-connector
title: Creating a basic data connector
sidebar_label: Creating connectors
---

Suppose you have a public JSON bin with data accessible at [the following URL](https://api.jsonbin.io/b/5c5cded2e9e7c118390e07d5): `https://api.jsonbin.io/b/5c5cded2e9e7c118390e07d5`.

Using SwaggerHub or similar editor, you can implement a Swagger file representing this single API endpoint.

To turn a Swagger file into a basic data connector in Transposit:

## 1. Create an application

Create a new Transposit application with a sensible name, e.g. `yourname/bare_bones`.

## 2. Clone the respository

Clone the application's code respository, e.g.:

```shell
  git clone https://console.transposit.com/git/yourname/bare_bones
```

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

Commit your changes and push back to Transposit.

You can now add your data connector `yourname/bare_bones` as a dependency in another application, and invoke the `getFunData` operation.

