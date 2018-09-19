# Hosted apps

Transposit offers web hosting facilities, _hosted apps_, for exposing functionality to your users. They are a simple alternative to using a third-party hosting service.

Hosted app pages are written in HTML and JavaScript, and do not require much code to make useful. Transposit manages user sign-in and settings, provides the scaffolding for connecting to your Transposit backend, and suggests some basic interfaces for rendering operation results. Even for complex frontends, these facilities can be a great starting point when prototyping.

For more granular control, it is possible to host your app with a third-party and use Transposit as a backend. These apps can interface with Transposit via our [JavaScript SDK](../references/js-sdk.md) or by directly invoking [http endpoints](endpoints.md).

## Modify page template

1. Navigate to **Code &gt; Page template**.
2. Modify the HTML and JavaScript.
3. Click **Preview** to preview your changes in the browser.
4. Click **Commit code** to persist your changes and deploy them.

### Development process

Click **Preview** to preview uncommitted page changes in your browser. You will need to click **Preview** every time you make a new change; reloading an old preview will not load new changes.

A preview of your hosted app interacts with committed operations&mdash;You must commit changes to operation code before these changes will be reflected in a preview. A preview obeys the same configuration as your deployment, so if your hosted app has sign-in enabled, you will need to sign in to interact with the preview.

A preview is not accessible to others and only exists for one minute. After one minute, loading a preview will merely load the committed page.

You can access previews at:

```text
https://api.transposit.com/app/{maintainer}/{applicationName}/preview
```

### Deployment process

Click **Commit code** to persist your changes and deploy them. A hosted app always serves the most recently committed code.

Sign-in and authentication for data connections can be configured under **Authentication**.

Your hosted app can be accessed at:

```text
https://api.transposit.com/app/{maintainer}/{applicationName}
```

## Configure sign-in

Hosted apps can be shared publicly or protected by sign-in. Hosted apps protected by sign-in can whitelist specific GSuite domains or users.

1. Navigate to **Authentication &gt; User Sign-in**.
2. Check the box requiring users to sign in with Google.
3. Specify who is allowed to sign in.

## Manage keys

Each data connection in your application can either reference a production key or expect signed-in users to provide their own key.

1. Navigate to **Authentication &gt; Production Keys**.
2. Add a production key for each data connection that should share a key across users.
3. Check the box for each data connection that should expect a user to provide their own key.

## Manage users

You can view and administer registered users in **Authentication &gt; Registered Users**. You can delete users or their keys if necessary.
