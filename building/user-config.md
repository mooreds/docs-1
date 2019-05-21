---
id: user-config
title: User Configuration
layout: docs.mustache
---

On the User Configuration page, you can specify how users will interact with your app.

## Configure sign-in

Your application can be shared publicly or protected by sign-in. Applications protected by sign-in can whitelist specific Google GSuite domains or specific users.

1. Navigate to **Users &gt; User Configuration &gt; Registration and Login**.
2. Click **Restrict to specific whitelisted domains and users**.
3. Specify who is allowed to sign in.
4. Click **Save**.

## Manage users

You can view and administer registered users in **Users &gt; Registered Users**. You can delete users, remove authorizations, or add user settings as necessary.

## Manage keys

Each data connection in your application can either reference a production key that you have provided or expect signed-in users to provide their own key. Check the appropriate boxes under **Require users to authenticate with these data connections**. For the rest, navigate to **Deploy &gt; Production Keys** and click **Add key**. 

## Custom UI for user settings

An automatically generated user settings page will be sufficient for most of your Transposit use cases. If your application requires a UI, you'll want to select the **Advanced (custom page template)** option.

With the "Advanced" user settings page, you will modify the HTML and JavaScript provided in **Code &gt; Page template** to create your own form for accepting user settings input and calling Transposit operations. For complex frontends, this mode can be a great starting point when prototyping.

For even more control, it is possible to host your app with a third-party and use Transposit as a backend. These apps can interface with Transposit via our [JavaScript SDK](/docs/building/js-sdk) or by directly invoking [HTTP endpoints](/docs/building/endpoints).

## User settings schema

For applications requiring user-specific input, you can create a user settings schema under **User &gt; User Configuration &gt; User settings schema**

Below are examples of how you would use the different types of schemas:

1. String type: Your application modifies a Google spreadsheet and a spreadsheet id is provided by each user.
2. Number type: Your application provides email digests to your users and you want each user to specify how many times a week to be emailed.
3. Boolean type: Your application is the same as above, and you want the user to select whether or not their emails should contain gifs.
4. Options type (see below): Your application posts Slack messages and you want the user to select which of their Slack channels to post to.

Settings can be hidden from the user by unchecking the `Show on user settings page` box. You would do this if you want to set the setting yourself. For example, you could programmatically store the user's Slack username from their credential. You could also have a hidden setting to mark certain users as power users of your application, and use the **Registered Users** interface to manually set this setting.

You will have your development copy of these settings, identical to what your users will see, under **Code &gt; Development &gt; Auth & user settings**
If you don't see your expected settings, go back to **User Configuration** and double check that the setting was saved and its visibility is as expected.

Visit [the JavaScript operation documentation](/docs/references/js-operations.md) on how to programmatically access a user setting.

## Operation-generated settings 

Use an options type schema if you would like to limit the user's input to a set of options. The selected operation will return an array of objects, each with properties `displayName` and `value`. The set of options can be static; for example, a list of colors mapped to hex codes. They can also be dynamic; for example, generating a list of the user's slack channels mapped to channel ids. In the dynamic case, you can first check (in JavaScript) if the user is authenticated by calling `api.isAuthed(<data connection>)` and throwing an error if they are not.

1. Navigate to **Code &gt; Operations** and create operation of `User Setting Options` type
2. Commit your code
3. Create a user setting schema of type `options`
4. Select your newly-created operation in the dropdown
5. Save your changes by clicking **Save All**.