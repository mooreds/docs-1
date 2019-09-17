---
id: slack-chatbots
title: Building Slack bots
layout: docs.mustache
tags: doc
description: "Chatbots use event subscriptions to automate your Slack workspace and act as a bot user"
---

Slackbots are a great way to automate your app based on events happening in your workspace. Additionally, they are another way to interact with users in a more personal way. Create your bot easier with Transposit.

## Prerequisites

- A [Slack App](https://api.slack.com/apps)
- An application in Transposit

## Create a webhook in Transposit

- Follow the instructions at the [webhooks docs page](/docs/building/webhooks) to create a webhook operation.
- If planning on using [event subscriptions](https://api.slack.com/events-api), add code into the `http_event` function to pass the [url_verification event](https://api.slack.com/events/url_verification). This is due to [Dynamic Challenges](/docs/building/webhooks/#dynamic-challenges).

```js
if (http_event.parsed_body.challenge) {
  return {
    status_code: 200,
    headers: { "Content-Type": "text/plain" },
    body: http_event.parsed_body.challenge
  };
}
```

- Commit your code.
- Navigate to **Deploy > Endpoints** and change the operation _webhook_ from **Not deployed** to **Deployed** if needed.
- Check the box for **Deploy as webhook** and copy the deployed URL it produces.

## Setting up a Slack event to POST to your webhook

- In your Slack App configure page, select Event Subscriptions, and paste in the URL you copied from Transposit. If you copied the Dynamic Challenge code correctly, it should automatically verify that the function is valid.
- Install the Slack app with proper permissions into your workspace.

## Sample webhooks

The challenge response is a goode example of a simple webhook function. You can also create a webhook function in SQL if you prefer.

```sql
SELECT {
    status_code: 200,
    headers: { "Content-Type": "application/json" },
    body: {
    	text: "Hello World, from SQL!"
    }
}
```

Your webhook function will be called whenever the events you decide to follow occur in your workspace. Adding helper functions and other API calls before the return statement can add to the ability to customize output.

## Selecting events to follow

Bot users aren't just another face to post a message as, they can be used to scan for many events in the organization as a way to trigger your webhook function. [Slack Events API](https://api.slack.com/events-api) contains a large number of events that can either happen in your workspace, or your bot is a part of to POST. Additionally, can you use App Unfurl Domains to have the event trigger upon a user posting a link from a select domain. Some common events to use are:

- `message.channels`
- `message.im`
- `app_mention`
- `reaction_added`
- `team_join`

## Acting as your bot user

While Transposit makes it easy to authenticate with your Slack account, in order to act as your bot, we need to manually input the credentials of the bot. Otherwise the application will continue to execute as you.

- Find your Client ID and Secret in your Slack app under **Basic Information > App Credentials**.
- In your Transposit app, go to **Data connections > Slack > Authentication** and change the values to your Slack app's Client ID and Secret.
- On the same page, edit the **Configuration** with AccessTokenPath `bot.bot_access_token`, and Scope equal to the scopes you have selected in **OAuth & Permissions** in Slack.
- In **OAuth & Permissions** still, add `https://accounts.transposit.com/oauth/v2/handle-redirect` as a redirect URL.
- Reinstall your app in Slack.
- Reauthenticate Slack in Transposit. If done correctly, it should try to authenticate your bot user, instead of you.

## Viewing POSTed data

You can view the data sent to your webhook from Slack in the **Monitor** tab, or by returning the data in the response.

```js
({ http_event }) => {
  return {
    status_code: 200,
    headers: { "Content-Type": "application/json" },
    body: { text: JSON.stringify(http_event, null, 2) }
  };
};
```

This gives us the full HTTP request; most of what we are interested in is in the body. Transposit parses the body according to the type specified in the headers. You'll see something like this:

```json
 "parsed_body": {
    "token": "<token>",
    "team_id": "XXXXXXXXX",
    "api_app_id": "XXXXXXXXX",
    "event": {
      "type": "team_join",
      "user": {
        "id": "XXXXXXXXX",
        "team_id": "XXXXXXXXX",
        "name": "user",
        "deleted": false,
        "color": "ea2977",
        "real_name": "name",
        "tz": "America/Los_Angeles",
        "tz_label": "Pacific Daylight Time",
        "tz_offset": -25200,
        ...
        "is_admin": false,
        "is_owner": false,
        "is_primary_owner": false,
        "is_restricted": false,
        "is_ultra_restricted": false,
        "is_bot": false,
        "is_app_user": false,
        "updated": 1565992213,
        "presence": "away"
      },
      "cache_ts": 1565992213,
      "event_ts": "1565992213.000800"
    },
    "type": "event_callback",
    "event_id": "XXXXXXXXX",
    "event_time": 1565992213,
    "authed_users": [
      "XXXXXXXXX"
    ]
 },
```

We already set this to pass the challenge back to Slack above, where we used `http_event.parsed_body.challenge`. This can be done with any of the labels in the webhook.

<a class="action-btn-blue br1 f5 fw5 ph4 pv3 dib mt2" href="/docs/guides/slack/">Return to Slack landing page</a>
