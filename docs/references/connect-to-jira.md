---
id: connect-to-jira
title:  Connect a Transposit application to Jira
sidebar_label: Connect to Jira 
---

You will need to register your Transposit application as an OAuth consumer to connect it to Jira. After, you can authenticate with your Jira account and interact with the Jira API.

## Create a new OAuth consumer in Jira

Follow **Step 1. Configure client application as an OAuth consumer** in [Jira's OAuth documentation](https://developer.atlassian.com/server/jira/platform/oauth/). This process includes a couple tasks:
- Generate an RSA public/private key pair. Skip the steps asking you to edit the sample OAuth client project. Instead, you will store the private key in Transposit and share the public key with Jira.
- Create an application link. Use _https://www.transposit.com_ as the value for all URL parameters since you only need an one-way (incoming) link. Use _transposit_ as the value of **Consumer key** and **Shared secret**.

Once you have successfully created an application link, keep your RSA private key available for the next step.

## Configure Transposit's Jira connection

Navigate to your Transposit application. Add _transposit/jira_ as a data connection.

Configure this data connection. You will need to specify a couple values specific to your Jira instance:
- Set the **Base URL** to _https://&lt;instance&gt;.atlassian.net/rest/_. Replace _&lt;instance&gt;_ with the name of your Jira instance (this value appears in the URL you use to access Jira normally).
- Set the **OAuthV1 Config** values. Replace _&lt;instance&gt;_ as you did in the previous step.

|            |           |
|------------|-----------|
|**Auth URI**|_https://&lt;instance&gt;.atlassian.net/plugins/servlet/oauth/authorize_|
|**Access Token URI**|_https://&lt;instance&gt;.atlassian.net/plugins/servlet/oauth/access-token_|
|**Request Token URI**|_https://&lt;instance&gt;.atlassian.net/plugins/servlet/oauth/request-token_|


Configure **Authentication** for this data connection. The **Consumer Key** should always be _OauthKey_. The **Private Key** should be a processed version of the RSA private key you generated previously. Specifically, remove the header and footer from the key, and then remove all line breaks from the body.

```
-----BEGIN PRIVATE KEY----- <--- remove this
... <--- remove line breaks from this and copy it
-----END PRIVATE KEY----- <--- remove this
```

Save this configuration.

You should now be able to authenticate with your Jira account through Transposit.

## Authenticate with your Jira instance

Navigate to your Transposit application. Add a key for your Jira data connection. Allow your Transposit application to access your Jira data.

Delete the public and private keys you generated on your local machine. You no longer need them now that you've confirmed the integration is working.

That's it! You should now be able to query the Jira API using Transposit.
