---
id: user-config
title: User configuration
layout: docs.mustache
tags: doc
---

On the User Configuration page, you can specify how users will interact with your app.

## Configure user sign-in

Your application is protected by sign-in. You can restrict sign-in to specific Google GSuite domains and users, or Slack workspaces.

1. Navigate to **Users &gt; User Configuration &gt; Registration and Login**
2. Specify who is allowed to sign in
3. Click **Save**

## Select a sign-in provider

Choose whether users authenticate through Google or Slack when signing in to your app. Choose carefully: you can change your sign-in provider later, but all user data will be deleted.

1. Navigate to **Users &gt; User Configuration &gt; Registration and Login**
2. Click **Change** found at the end of "Users authenticate with their Google/Slack account" 
3. Select a provider from the pop-up form
4. Click **Change**

## Manage users

You can view and administer registered users in **Users &gt; Registered Users**. You can delete users, remove authorizations, or add user settings as necessary.

## Manage keys

Each data connection in your application can either reference a production key that you have provided or expect signed-in users to provide their own key. Check the appropriate boxes under **Require users to authenticate with these data connections**. For the rest, navigate to **Deploy &gt; Production Keys** and click **Add key**.

## User settings schema

For applications requiring user-specific configuration, you can define a user settings schema at **Users &gt; User Configuration &gt; User settings schema**. Settings marked with `Show on user settings page` will be displayed on the app's user settings page, along with any required data connector authentication.

Below are examples of how you might use different types of inputs:

* String type: Your application modifies a Google spreadsheet and a spreadsheet id is provided by each user.
* Number type: Your application provides email digests to your users and you want each user to specify how many times a week to be emailed.
* Boolean type: Your application is the same as above, and you want the user to select whether or not their emails should contain gifs.
* Options type (see below): Your application posts Slack messages and you want the user to select which of their Slack channels to post to.

Settings can be hidden from the user by unchecking `Show on user settings page`. Some example use cases for hidden settings are: programmatically storing the user's Slack username from their credential, or having a hidden setting to mark certain users as power users (and using the **Registered Users** interface to manually toggle the setting).

Your development environment interface for these settings, identical to what your users will see, is found under **Code &gt; Development &gt; Auth & user settings**.

Visit the [JavaScript operation documentation](/docs/references/js-operations) for info on programmatically accessing user settings.

## Operation-generated settings

Use an `options` type to limit the user's input to a set of options. The selected operation will return an array of objects, each with properties `displayName` and `value`. The set of options can be static — a list of colors mapped to hex codes, for example. They can also be dynamic — generating a list of the user's Slack channels mapped to channel IDs, for example. In the dynamic case, you can check (in JavaScript) if the user is authenticated by calling `api.isAuthed("<data connection>")` and throwing an error if they are not.

1. Navigate to **Code &gt; Operations** and create an operation with the `User Setting Options` template
2. Commit your code
3. Create a user setting of type `options`
4. Select your newly-created operation in the dropdown
5. Save your changes

## Custom display of operation results

If your application requires more customization than the automatically-generated user settings page provides, you can select `Use a custom page template (advanced)`.

With a custom page template, you can supply HTML and JavaScript in **Code &gt; Page template** to invoke operations and display results. This can be a great starting point for prototyping application UI.

For even more control, it is possible to host your app's frontend with a third party and use Transposit as a backend. Apps can interface with Transposit via the [JavaScript SDK](/docs/building/js-sdk) or by directly invoking [HTTP endpoints](/docs/building/endpoints).