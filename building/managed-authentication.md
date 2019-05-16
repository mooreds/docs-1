---
id: managed-authentication
title: Managed authentication
layout: docs.mustache
---

One of Transposit’s powerful features is the way it can manage authentication for you, the app developer, and for your app's end users. Here are high-level explanations for what's meant by _managed auth_ and how it gives you freedom to develop applications without the burden of hard-coding authentication logic into every app.

If you'd like to jump straight to all authentication options, see [Connector authentication page](/docs/references/connector-authentication).

## What is managed auth in Transposit?

Transposit gives you tooling to centrally manage all the aspects of authentication you might require while building a data-driven application with a "front door" for user sign-in.

Imagine the following scenario: You are building an application that allows users to sign in (via Google) and connect their own data from other services your app integrates with (e.g. GMail, Slack, Salesforce). You also want to connect your application to data sources needed by _all_ app users&mdash;but requiring your own credentials (e.g. APIs, databases, spreadsheets, etc).

Here's what this process looks like when building with Transposit:

1. **Developer-provided authentication**
   1. You authenticate any data connections requiring developer permissions through Transposit
   2. Transposit stores and updates your developer-authenticated connections
2. **User-provided authentication**
   1. You enable single sign-on with Transposit for users to sign in to the application
   2. You customize a Transposit-hosted connect page allowing users to authenticate their own data connections
3. **User management**
   1. Transposit creates a list of user records mapping user accounts to their data connections
   2. You can manage your application's users and their data connections in Transposit

Here's a visualization of what Transposit's authentication solution looks like from the perspective of managing multiple, authenticated data connections, both developer and user-provided:

![](/docs/assets/managed-auth-1.png)

And here's a visualization of how Transposit can manage your application's "front door" sign-in and user records:

![](/docs/assets/managed-auth-2.png)

## Why is managed authentication useful?

Generally, you may build apps using frameworks or platforms that provide you with generic identity management solutions. You may also use data integration services that handle how you authenticate with third party APIs. By having both those aspects of authentication managed by Transposit, you'll no longer have the headache of handling them with custom code in your application _and_ you can take advantage of having them managed in one place.

This makes it easier to create and share **full application experiences** for your end users, with simple authentication flows. Instead of sharing an automation workflow with a coworker by creating a long wiki page explaining how they can replicate it using their own credentials, you can just build an application instead.

Finally, Transposit allows you to do all this while securely managing access to sensitive business data. You can safely share workflows and applications powered by data living in critical spreadsheets or databases, instead of managing multiple data sources for different audiences.

## How does Transposit-managed authentication work in practice?

To use Transposit as an authentication provider in your app, you’d copy/paste provided code into your app’s logic. Your app should also have a **connection settings** section which links to a Transposit-hosted page (which you can customize) providing the end user a way to connect and disconnect authenticated data sources.

In Transposit, if you’re using sign-in identity management, you can manage a whitelist of app users, inspect user records, see what connections and authentications exist, and modify these as an admin.

For more documentation about how to use authentication in Transposit in any of these cases, take a look at the detailed [Keychains reference](/docs/references/keys-and-keychains).

