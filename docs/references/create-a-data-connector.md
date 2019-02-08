---
id: create-a-data-connector
title: Creating a simple data connector in Transposit
sidebar_label: Create a data connector
---

Imagine you have a public JSON bin with fun data accessible at this URL: https://api.jsonbin.io/b/5c5cded2e9e7c118390e07d5.
You can implement a very bare Swagger file (below) representing this single API endpoint using SwaggerHub or some other online editor.
To turn this Swagger file into a simple data connector in Transposit:
1. Create a new Transposit application with the desired name, e.g. `you/bare_bones`
2. Clone the application's source code, e.g. `git clone https://console.transposit.com/git/you/bare_bones`
3. Update the application's source code tree to contain only these two files _(this may require deleting existing, boilerplate code)_:
    * `manifest.json`
        ```
        {
          "v2": {
            "swagger": {
              "source": "bare_bones.yaml"
            }
          }
        }
        ```
    * `bare_bones.yaml`
        ```
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
4. Commit and push the changes back to Transposit

Now you can add your simple data connector `you/bare_bones` as a dependency to another application and invoke its `getFunData` operation!

