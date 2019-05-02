---
id: connector-authentication
title: Authenticating with Data Connectors
layout: docs.mustache
nav-dark: true
---

This page will explain how to provide authentication for Transposit's data connectors.

## Auth via OAuth 1.0 and 2.0

Given OAuth settings (i.e. client IDs and secrets), Transposit will automatically handle the OAuth 1.0 and 2.0 authentication flows to procure an access token and refresh as needed. For most data connections that require OAuth, Transposit provides these settings for limited use. For these data connections, no further setup is required for authorization after the connection is added. 

### Custom OAuth settings

If you do not want to use the Transposit-provided OAuth settings, you always have the option to overwrite the configuration with your own custom OAuth settings. A small subset of data connections will require you to provide custom OAuth settings because no feasible Transposit-provided OAuth settings exist for those connections.

To use your own client ID and secret:
* Set up a developer app using the connector's platform. Add `https://console.transposit.com/oauthCallback` as a Redirect URI (use `/oauthV1Callback` for OAuth 1.0).
* Go to **Code > Data Connections** in Transposit and select your data connector. 
* Under  **Authentication > Configure**, add the client ID and secret from your created developer app.
* If you'd like, customize the [scope](#custom-oauth-scope) under **Configuration**

 You can configure your own client ID and secret under **Authentication > Configure** or customize the scope (what permissions your users will be allowing with the connector when they authenticate with your app) under **Configuration**. 


The following connectors require custom OAuth settings. When you add the connector to your service, you will be prompted to add these settings. Follow the links to create your own developer apps:
* [Google Mail](#generating-a-client-id-and-secret-with-google-connectors)
* [Jira](/references/connect-to-jira)
* [Salesforce](https://na50.lightning.force.com/lightning/setup/NavigationMenus/home) 
* [Shopify](https://partners.shopify.com/organizations) (Select an account and click on the "Apps" link in the dashboard)
* [Survey Monkey](https://developer.surveymonkey.com/apps/) 

Below are links to create developer apps (to generate your own OAuth settings) if you do not want to use the Transposit-provided settings:
* [Github](https://github.com/settings/developers)
* [Lyft](https://www.lyft.com/developers/apps)
* [Slack](https://api.slack.com/apps)
* [Spotify](https://developer.spotify.com/dashboard/applications)
* [Strava](https://www.strava.com/settings/api)

### Generating a client ID and secret with Google connectors 

* Go to the [Google Cloud Platform Console](https://console.cloud.google.com/) and select a project or create a new one.
* Select **APIs & services > Credentials**.
* Click  **New Credentials > OAuth client ID**.
* Either configure a consent screen if this is your first time, or modify your existing consent screen to add `transposit.com` as an authorized domain.
* Select **Web application**.
* Note the Client ID and Client Secret to be used in the next step, and click Save.
* Select the credential you just created and add `https://console.transposit.com/oauthCallback` as an authorized redirect URI. If you did not properly set up your authorized domain in your consent screen, you may get an `Invalid Redirect` error. If so, follow the link and add `transposit.com` to the authorized domains list.
* Go to **APIs & Services > Library**, search for the correct API (e.g. Google Mail, Google Calendar, or Google Drive), and enable the API.

If you would like others to use your application, you may need to get it [verified by Google](https://support.google.com/cloud/answer/9110914?hl=en&ref_topic=3473162). 

### Custom OAuth scope

The scope of a data connector defines what permissions your users will be allowing your app. By default, the range of scopes for each data connector is fairly permissive. You can add or remove scopes for your data connectiors as you see fit.

## Auth via header parameters

For data connections that implement authentication with header parameters, such as PagerDuty, the header parameter name (as documented by the external API site) and header parameter value (typically a secret token distributed by the external API site) must be provided when adding the connection to an application.

Example: [PagerDuty](https://support.pagerduty.com/docs/using-the-api#section-generating-a-general-access-rest-api-key)

![](/assets/auth-exemplary-pagerduty.png)

* [PagerDuty](https://support.pagerduty.com/docs/using-the-api#section-generating-a-general-access-rest-api-key)
* [Yelp](https://www.yelp.com/developers/v3/manage_app)

## Auth via query parameters

For data connections that implement authentication with query parameters, such as Zoom, only the query parameter value (typically a secret distributed by the external API site) must be provided when adding the connection to an application.

Example: [Zoom](https://marketplace.zoom.us/develop/create)

![](/assets/auth-exemplary-zoom.png)

* [Airtable](https://airtable.com/account)
* [Apify Crawler](https://my.apify.com/account#/api)
* [Giphy](https://developers.giphy.com/dashboard/)
* [Zoom](https://marketplace.zoom.us/develop/create)

## Auth via AWS parameters

For AWS data connections, such as Lambda, the required combination of authentication parameters 'Access Key', 'Secret Key', and 'Role' depends on the authentication setup of your particular AWS service being connected to. The pair of 'Access Key' and 'Secret Key' authenticates you as an [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), and the 'Role' can be used to specify the ARN of an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

Example: Lambda with all three parameters provided (i.e. authentication as an IAM user assuming an IAM role)

![](/assets/auth-exemplary-lambda.png)

* AWS Basic
* Elastic
* Lambda

