---
id: user-config
title: User configuration
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

An automatically generated user settings page will be sufficient for many Transposit applications. If your application requires custom UI for app settings, you have the option of selecting **Advanced (custom page template)**.

With the advanced user settings page, you can modify the HTML and JavaScript provided in **Code &gt; Page template** to create your own forms for accepting user settings input and calling Transposit operations. For complex front ends, this can be a great starting point when prototyping.

For even more control, it is possible to host your app's frontend with a third party and use Transposit as a backend. Apps can interface with Transposit via the [JavaScript SDK](/docs/building/js-sdk) or by directly invoking [HTTP endpoints](/docs/building/endpoints).

## User settings schema

For applications requiring user-specific input, you can create a user settings schema under **User &gt; User Configuration &gt; User settings schema**

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