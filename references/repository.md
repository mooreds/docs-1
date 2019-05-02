---
id: repository
title: Application code repository
layout: docs.mustache
nav-dark: true
---

Your application's code is stored and versioned in a git repository. You can clone the repository to view diffs or use your own editor tools to modify your application.

## File structure
* Metadata files
  * **manifest.json**: the main configuration for your application; notably, the location of your application's source code is defined in this file (e.g. `"source": "src"`)
  * **README.md**: the optional README for your application
  * **LICENSE**: the optional LICENSE for your application
* Source code files
  * **public/index.html**: the HTML for your hosted app
  * **\*.js**: The JavaScript files for your JavaScript operations

```text
.
├── LICENSE
├── README.md
├── manifest.json
└── src
    ├── hello_world.js
    └── public
        └── index.html
```

## Cloning Your repository
* Go to **Settings > App Info**.
* Grab the URL under **Source code**.
* Click the link to your **account settings page** or go to the dropdown for your username in the upper right hand  corner and click **Settings**.
* Copy the **Git access token** from this page
* Clone your repository using your username and your git access token. For convenience, you can also create a `.netrc` file in your home directory that stores these credentials. The file will have an entry like the following:

```text
machine console.transposit.com
        login &lt;YOUR USER NAME&gt;
        password &lt;YOUR GIT ACCESS TOKEN&gt;
```
