---
id: slack-slash-commands
title: Building Slack slash commands
layout: docs.mustache
tags: doc
description: "Slash commands allow you to call your automations within Slack"
---

Slash Commands are an easy way to create a user-facing trigger for your Transposit Slack app.

## Prerequisites

- A [Slack App](https://api.slack.com/apps)
- An application in Transposit

## Create a webhook in Transposit

- Follow the instructions at the [webhooks docs page](/docs/building/webhooks) to create a webhook operation.
- Commit your code.
- Navigate to **Deploy > Endpoints** and change the operation _webhook_ from **Not deployed** to **Deployed** if needed.
- Check the box for **Deploy as webhook** and copy the deployed URL it produces.

## Setting up a Slack slash command to POST to your webhook

- In your Slack App configure page, select Slash Commands, and create a new one.
- Under _Request URL_, paste in the URL you copied from Transposit, and save.
- Install the Slack app with proper permissions into your workspace.

## Sample webhooks

### A simple webhook

```js
({ http_event }) => {
  return {
    status_code: 200,
    headers: { "Content-Type": "application/json" },
    body: { text: "Hello World" }
  };
};
```

### In SQL

```sql
SELECT {
    status_code: 200,
    headers: { "Content-Type": "application/json" },
    body: {
    	text: "Hello World, from SQL!"
    }
}
```

Your webhook function will be called whenever the slash command you created is invoked in your workspace. Adding helper functions and other API calls before the return statement can add to the ability to customize output.

## Viewing POSTed data

You can view the data sent to your webhook from Slack in the Monitor tab, or by returning the data in the response.

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
    "channel_name": "general",
    "user_id": "XXXXXXXXX",
    "user_name": "user",
    "trigger_id": "<trigger_id>",
    "team_domain": "test_domain",
    "team_id": "XXXXXXXXX",
    "text": "demo",
    "channel_id": "XXXXXXXXX",
    "command": "/slashcommand",
    "token": "<token>",
    "response_url": "https://hooks.slack.com/commands/<response_url>"
 },
```

You can invoke this body in your code by calling:

```js
let body = http_event.parsed_body;
```

where if you wanted to grab a variable such as the channel id you could call `http_event.parsed_body.channel_id`.

## Slack webhook operation_timeout

Slack has a 3 second rule for webhooks, where if we don't respond quickly enough it will tell the user that the slash command failed. 3 seconds is an eternity, but if your slash command starts doing something complex or needs to talk to a bunch of APIs, it can go by in a flash. To avoid problems in the future, it's a good idea to return quickly and keep working in the background. We can do this easily using JavaScript's `setImmediate`:

```js
({ http_event }) => {
  setImmediate(() => {
    api.run("slack_webhook.post_to_response_url", {
      post_body: {
        text: "Don't call me; I'll call you."
      },
      response_url: http_event.parsed_body.response_url
    });
  });

  return { status_code: 200 };
};
```

Here, we return immediately from our webhook, and then asynchronously sent back the text "Don't call me; I'll call you". If we were gathering data from a number of slow APIs, this would avoid the three second limit (though you are still limited by the [usage limits](/docs/building/operations/#usage-limits-for-operations).

<a class="action-btn-blue br1 f5 fw5 ph4 pv3 dib mt2" href="/docs/guides/slack/">Return to Slack landing page</a>
