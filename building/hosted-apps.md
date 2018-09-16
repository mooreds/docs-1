# Hosted apps

Hosted apps are a lightweight hosting solution for creating simple application frontends built on Transposit. Even for applications that have more complex hosting needs, they can be a great starting point when prototyping. With hosted apps, we manage the interface around login and settings, and we provide the scaffolding for connecting to your Transposit backend and some basic interfaces for rendering the results. For those who need more fine-grain control, you can either use our [JavaScript SDK](../references/js-sdk.md) or directly call our [http endpoints](endpoints.md).

You can access your hosted app using:
```text
https://demo.transposit.com/app/v1/{maintainer}/{applicationName}/public/
```

This URL is also available to you at any time in the Documentation tab under application manual or else under **Settings &gt; Hosting**

## Modifying the content
1. Navigate to **Code &gt; Page template**
2. Modify the HTML
3. Click **Preview** to see the results. \(Note that any time you make a change to code or to the template, you need to click this button again to see the changes in the preview. Reloading the preview will not work.\)
4. Now that you see that it working in the preview, return to Transposit and commit your code changes so that you'll see it in the public link that you can once again access from your application manual.

## Controlling user access
1. Navigate to **Authentication &gt; User Sign-in**
2. You have 3 options:   **Allow sign in from any Google account**, add your GSuite domain name, or add individual email addresses to the whitelist.
