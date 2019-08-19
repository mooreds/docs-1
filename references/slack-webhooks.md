---
id: slack-webhooks
title: Slack Webhooks
layout: docs.mustache
tags: doc
---

When building a Slack app, you will need to communicate between Slack and Transposit through webhooks. Slack has multiple different components that will all need to interact this way, where it is important to know how to manage your webhooks between Slack and Transposit.

## Prerequisites

- A [Slack App](https://api.slack.com/apps)
- An application in Transposit

## Create a webhook in Transposit

- Follow the instructions at the [webhooks docs page](https://www.transposit.com/docs/building/webhooks) to create a webhook operation.
- Commit your code.
- Navigate to **Deploy > Endpoints** and change the operation _webhook_ from **Not deployed** to **Deployed**.
- Check the box for **Deploy as webhook** and copy the deployed URL it produces.

## Setting up a Slack app to POST to your webhook

- In your Slack App configure page, select one feature that you would like to use in your app.
- Under _Request URL_, paste in the URL you copied from Transposit.
  - If you are using _Event Subscriptions_, you need to modify your webhook code to pass a challenge. You can see an example of this at [Dynamic Challenges](https://www.transposit.com/docs/building/webhooks/#dynamic-challenges).
- Install the app with proper permissions into your workspace.

## Parsing webhook data

Transposit has a built in function that will automatically parse a Slack webhook into workable JSON, which is useful, as different webhooks they sent were in different formats.

```js
let body = http_event.parsed_body;
```

Calling `body` as your webhook object over `http_event` will all you to access all of the webhook data with simple commands. You can view the formatted data in Transposit by calling `return body;`.

## Example webhook contents

### Interactive Components

```json
    "type": "dialog_submission",
    "token": "<token>",
    "action_ts": "XXXXXXXXX.XXXXX",
    "team": {
      "id": "XXXXXXXXX",
      "domain": "test-domain"
    },
    "user": {
      "id": "XXXXXXXXX",
      "name": "user"
    },
    "channel": {
      "id": "XXXXXXXXX",
      "name": "general"
    },
    "submission": {
      "message": "message_body",
      "send_by": "workspace_user",
      "option": "option1"
    },
    "callback_id": "webhook",
    "response_url": "https://hooks.slack.com/app/<reponse_url>",
    "state": ""
```

Interactive components consist of multiple different "types" that will call a webhook to the same URL. This can include a dialog submission (shown in the example), a message action, message buttons, and message menus all with slightly different parameters based on how they are set up.

One way to differentiate between them in your webhook function is to do a simple if statement, such as `if (body.type == 'message_action)` to call for a message action.

### Slash Commands

```json
    "channel_name": "general",
    "user_id": "XXXXXXXXX",
    "user_name": "user",
    "trigger_id": "<trigger_id>",
    "team_domain": "test_domain",
    "team_id": "XXXXXXXXX",
    "text": "help",
    "channel_id": "XXXXXXXXX",
    "command": "/helpdesk",
    "token": "<token>",
    "response_url": "https://hooks.slack.com/commands/<response_url>"
```

Slash Commands, along with other types such as message actions are particularly useful for the `trigger_id` they pass, as this allows you to call APIs such as `slack.open_dialog`. `trigger_id` must be used within the first few seconds the webhook has been POSTed.

### Event Subscriptions

```json
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
        "profile": {
          "title": "",
          "phone": "",
          "skype": "",
          "real_name": "name",
          "real_name_normalized": "name",
          "display_name": "name",
          "display_name_normalized": "name",
          "fields": null,
          "status_text": "",
          "status_emoji": "",
          "status_expiration": 0,
          "avatar_hash": "g77f450b8308",
          "email": "user@example.com",
          "image_24": "https://secure.gravatar.com/avatar/77f450b83082005cf526d669cb7cb862.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2F00b63%2Fimg%2Favatars%2Fava_0008-24.png",
          "image_32": "https://secure.gravatar.com/avatar/77f450b83082005cf526d669cb7cb862.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2F00b63%2Fimg%2Favatars%2Fava_0008-32.png",
          "image_48": "https://secure.gravatar.com/avatar/77f450b83082005cf526d669cb7cb862.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2F00b63%2Fimg%2Favatars%2Fava_0008-48.png",
          "image_72": "https://secure.gravatar.com/avatar/77f450b83082005cf526d669cb7cb862.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2F00b63%2Fimg%2Favatars%2Fava_0008-72.png",
          "image_192": "https://secure.gravatar.com/avatar/77f450b83082005cf526d669cb7cb862.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2F00b63%2Fimg%2Favatars%2Fava_0008-192.png",
          "image_512": "https://secure.gravatar.com/avatar/77f450b83082005cf526d669cb7cb862.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2F00b63%2Fimg%2Favatars%2Fava_0008-512.png",
          "status_text_canonical": "",
          "team": "XXXXXXXXX"
        },
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
```

In order to use Event Subscriptions, you must include the following code in your webhook function.

```js
if (body.challenge) {
  return {
    status_code: 200,
    headers: { "Content-Type": "text/plain" },
    body: body.challenge
  };
}
```

Event subscriptions can be linked to multiple different event types. One way to differentiate between them in your webhook function is to do a simple if statement, such as `if (body.type == 'group_open)` to call when a new group DM is opened.
