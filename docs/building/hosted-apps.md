---
id: hosted-apps
title: Hosted apps
---

Transposit offers web hosting facilities, _hosted apps_, for exposing functionality to your users. They are a simple alternative to using a third-party hosting service.

Hosted app pages are written in HTML and JavaScript, and do not require much code to make useful. Transposit manages user sign-in and settings, provides the scaffolding for connecting to your Transposit backend, and suggests some basic interfaces for rendering operation results. Even for complex frontends, these facilities can be a great starting point when prototyping.

For more granular control, it is possible to host your app with a third-party and use Transposit as a backend. These apps can interface with Transposit via our [JavaScript SDK](js-sdk.md) or by directly invoking [http endpoints](endpoints.md).

### Deployment process

Click **Commit code** to persist your changes and deploy them. A hosted app always serves the most recently committed code.

Sign-in and authentication for data connections can be configured under **Users &gt; User Configuration**.

## Configure sign-in

Hosted apps can be shared publicly or protected by sign-in. Hosted apps protected by sign-in can whitelist specific Google GSuite domains or specific users.

1. Navigate to **Users &gt; User Configuration**.
2. Click Restrict to specific whitelisted domains and users.
3. Specify who is allowed to sign in.
4. Click **Save**

## Manage keys

Each data connection in your application can either reference a production key or expect signed-in users to provide their own key.

1. Navigate to **Deploy &gt; Production Keys**.
2. Click **Add key**

## Manage users

You can view and administer registered users in **Users &gt; Registered Users**. You can delete users or their keys as necessary.

## Advanced

You can customize user settings schema for your users. Users can provide their key to work with your app.
To check the changes have been applied correctly, go back to code editor, click Development under Auth & settings.
Under your API connector status, you should see the schema.
If you don't see your user schema, go back to User Configuration and make sure you saved the changes.

## Customize User Configuration

1. Navigate to User > User Configuration.
2. Under User settings schema, click **Add**.
3. Fill in the information.
4. Save your changes by clicking **Save All**.
