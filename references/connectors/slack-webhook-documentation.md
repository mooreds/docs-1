---
id: slack-webhook-documentation
title: Slack Webhook (version v1.*.*)
sidebar_label: Slack Webhook
layout: docs.mustache
---

## post_to_response_url

Posts to the slack-provided response_url. 

<details><summary>Parameters</summary>

### response_url (required)

The response_url to post to, given by Slack. This will look something like https://hooks.slack.com/...

**Type:** STRING

### attachments

A JSON-based array of structured attachments.

**Type:** ARRAY

### post_body

Optional. Message arguments in JSON object form as defined here (except for token and channel): https://api.slack.com/methods/chat.postMessage#formatting. The "text" and "attachments" parameters will be appended to this object and sent.

**Type:** OBJECT

### text

Text of the message to send. This field is usually required, unless you're providing only attachments.

**Type:** STRING

</details>

