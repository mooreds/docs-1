# Managed auth

One of Transposit’s most powerful features is the way we manage authentication for you \(**the developer**\) and your apps’ end users \(**the consumer**\). Here are our high-level explanations for what exactly we mean when we say “managed auth” and how that allows you the freedom to develop applications without the burden of hard-coding authentication logic into every app.

## **What is managed auth?**

Managed auth means you don’t need to write your own identity management solution or worry about building the underlying data conduits for consumers of your app. You can plug in Transposit, and use third identity services \(for now, just Google auth\) to control access to your app, as well as give customers an easy way to authenticate, using their own credentials, with the services your app depends on. Transposit still allows you to customize the flows your user will authenticate through.  


When we refer to managed auth, we are actually talking about three separate experiences:  


1. **Third-party integrations:** When you, the **developer** provision data integrations for use with a particular Transposit service.
2.  **Managed identity:** When you, the **developer**, are building services, you specify which consumer’s credentials you’d like the consumer to supply. Additionally, you authenticate users of your app through Transposit.
3. **Consumer-supplied authentication \(or user login\):** When your app **consumers** easily sign in to Transposit-powered apps using various identity providers and easily provide that app with data from other sources.

Here's a model of how these are handled behind the scenes: 

\[Insert diagram\]  


## **Why is Transposit-managed authentication useful?**

Generally, you may build apps using services \(a Backend-as-a-Service, for example\) that provide you with managed identity solutions and user management. You may also use data integration services that handle how you authenticate with third party APIs. By having both those managed by Transposit, however, you now have the freedom to make your consumer-provided authentication to third party APIs that power your app’s personalized experiences without managing that in your application code. Once Transposit knows……

/// this is the part where I'm trying to explain why having them in the same place provides a more elegant, powerful end-to-end auth solution that skips a lot of back and forth. 

This also gives you more freedom to create and share full application experiences for your app consumers \(be they customers or co-workers\) that serves them easy authentication flows with minimal. Without Transposit, or a lot custom code for that application, that would previously require them to follow complex authentication instructions to replicate a workflow with their own credentials. We want you to build apps, not wiki walkthroughs.

Finally, you can do all this while easily managing who has access to sensitive business data, with Transposit taking care of the security around that access. This can be useful for safely sharing workflows and applications powered by data living in sources important to your business, like Google Sheets and Airtable.  
****

## **How does Transposit-managed authentication work in practice?** 

Each of your Transposit services have settings for ways to :

1. Control an app’s “front door” by requiring consumers to sign up, sign in, create a user record as a user of the app.
2. Specify which dependencies use auth provisioned for use by the service, and which should require consumer-supplied authentication.
3. Manage the user records, see what authorized connections exist, expire them, so forth.

To use Transposit as an authentication provider in your app, you’d copy/paste provided code into your app’s logic. Your app should also have a “connection settings” section which links out to a Transposit-hosted page \(that you can customize\) that gives the user a way to connect and disconnect authed services.

In Transposit, if you’re using “front door” identity management, there should be a way to manage a white list of users of your app, inspect user records, see what connections and authentications exist, and modify these as an admin.

To get more granular documentation around how to use authentication in Transposit in any of these cases, take a look at our Authentication section. 

{% page-ref page="../authentication/" %}

