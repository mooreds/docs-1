# Hosted apps

Transposit proivides lightweight page hosting facilities for creating simple application frontends. Even for applications that have more complex hosting needs, they can be a great starting point when prototyping.

Transposit manages the interface for user sign-in and settings, provides the scaffolding for connecting to your Transposit backend, plus some basic interfaces for rendering operation results. For more granular control, you can either use the [JavaScript SDK](../references/js-sdk.md) or directly call [http endpoints](endpoints.md).

You can access your hosted app using:

```text
https://api.transposit.com/app/{maintainer}/{applicationName}
```

This URL can also be found on the Documentation tab \(under your application's manual page\), and under under **Settings &gt; Hosting**.

## Modifying the page template

1. Navigate to **Code &gt; Page template**
2. Modify the HTML
3. Click **Preview** to see the results. \(Note that any time you make a change to code or to the template, you need to click Preview again to see the changes in the preview. Reloading the preview will not work.\)
4. Once you see it working in the preview, return to Transposit and commit your code changes so that you'll see it in the public link that you can once again access from your application manual.

## Controlling user access

1. Navigate to **Authentication &gt; User Sign-in**
2. You have 3 options:  Allow sign in from any Google account, add your GSuite domain name, or add individual email addresses to the whitelist.

