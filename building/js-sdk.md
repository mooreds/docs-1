---
id: js-sdk
title: JavaScript SDK
layout: docs.mustache
tags: doc
---

Use the [Transposit JavaScript SDK](https://github.com/transposit/transposit-js-sdk) to call operations from a web app.

## Configure user sign-in

1. Navigate to **Users &gt; User Configuration &gt; User settings page**
2. Select **Advanced (custom page template)**
3. Specify **Successful sign-in URIs**.
Transposit only allows redirection to these URIs during sign-in. This list should be empty if you are only using [hosted apps](/docs/building/hosted-apps).
4. Optionally, provide a custom **Google Client ID** and **Google Client Secret** pair
5. Save the configuration

# Restrict sign-in

You can restrict sign-in to specific Google GSuite domains or users.

1. Navigate to **Users &gt; User Configuration &gt; Registration and Login**
2. Select **Restrict to specific whitelisted domains and users**
3. Specify your restrictions

## Deploy endpoints

Deploy the operations you want to call from your web app as endpoints.

1. Navigate to **Deploy &gt; Endpoints**
2. Find the operation you want to deploy
3. Choose **Deployed** from the dropdown menu
4. Check only **Require user sign-in**
5. Save your changes

## Read the SDK documentation

Once you have configured user sign-in and deployed endpoints, use the SDK to build your web app. Follow our [SDK documentation on GitHub](https://github.com/transposit/transposit-js-sdk).
