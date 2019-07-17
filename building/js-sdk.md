---
id: js-sdk
title: JavaScript SDK
layout: docs.mustache
tags: doc
---

Use the [Transposit JavaScript SDK](https://github.com/transposit/transposit-js-sdk) to call operations from a web app.

## Configure user sign-in

1. Navigate to **Users &gt; User Configuration**
2. Specify **Successful sign-in URIs**. Transposit allows redirection only to these URIs during sign-in. Leave this list empty to redirect users to the  [user settings page](/docs/building/user-config) after signing in.
3. Optionally, provide a custom **Client ID** and **Client Secret** pair
4. Save the configuration

# Restrict sign-in

You can restrict sign-in to specific users or criteria. For Google, restrict based on GSuite domain or email address. For Slack, restrict based on workspace.

1. Navigate to **Users &gt; User Configuration &gt; Registration and Login**
2. Specify your restrictions

## Slack workspace id restrictions

You can restrict Slack sign-in by workspace id. To easily find a workspace's id, sign in to your app.

1. Sign in to your app using Slack
2. Navigate to **Users &gt; Registered Users**
3. Find your workspace id. It is formatted T1234ABCD.

## Deploy endpoints

Deploy the operations you want to call from your web app as endpoints.

1. Navigate to **Deploy &gt; Endpoints**
2. Find the operation you want to deploy
3. Choose **Deployed** from the dropdown menu
4. Check only **Require user sign-in**
5. Save your changes

## Read the SDK documentation

Once you have configured user sign-in and deployed endpoints, use the SDK to build your web app. Follow our [SDK documentation on GitHub](https://github.com/transposit/transposit-js-sdk).
