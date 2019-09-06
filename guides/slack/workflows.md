---
id: slack-workflows
title: Automating workflows with Slack
layout: docs.mustache
tags: doc
description: "Workflows in Slack use Interactive Components to send user entered data to your apps within Slack"
---

Workflows are the go to way for users to interact with your Slack apps in a guided fashion. In many cases, this involves using an interactive component in Slack, such as a button or menu within a message or dialog. Manage these event triggers with Transposit.

## Prerequisites

- A [Slack App](https://api.slack.com/apps)
- An application in Transposit

## Create a webhook in Transposit

- Follow the instructions at the [webhooks docs page](/docs/building/webhooks) to create a webhook operation.
- Commit your code.
- Navigate to **Deploy > Endpoints** and change the operation _webhook_ from **Not deployed** to **Deployed**.
- Check the box for **Deploy as webhook** and copy the deployed URL it produces.

## Setting up your Slack app to detect Interactive Components

- In your Slack App configure page, select Interactive Components, and turn it on.
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

Interactive components can be linked to multiple different event types, which means every single button, action, and menu will call the same webhook function. One way to differentiate between them in your webhook function is to do a simple if statement, such as `if (body.type == 'dialog_submission)` to call when a dialog form has been submitted. Learn more at the [Slack docs page](https://api.slack.com/interactive-messages).

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
 },
```

You can invoke this body in your code by calling:

```js
let body = http_event.parsed_body;
```

where if you wanted to grab a variable such as the channel id you could call `http_event.parsed_body.channel_id`.

Interactive components consist of multiple different "types" that will call a webhook to the same URL. This can include a dialog submission (shown in the example), a message action, message buttons, message menus, and so on all with slightly different parameters based on how they are set up.

## Triggered workflows

Certain types of Slack triggers such as message actions and slash commands are particularly useful for the `trigger_id` they pass, as this allows you to call APIs such as `slack.open_dialog`. `trigger_id` must be used within the first few seconds the webhook has been POSTed, otherwise it will not function as desired.

<a class="action-btn-blue br1 f5 fw5 ph4 pv3 dib mt2" href="/docs/guides/slack/">Return to Slack landing page</a>
