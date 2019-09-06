---
id: slack-notifications
title: Routing notifications through Slack
layout: docs.mustache
tags: doc
description: "Notifications allow you to display information in Slack through scheduled tasks or webhooks"
---

Notifications are a great way to display information in Slack from sources outside of your Slack workspace, like your Google Calendar. Using the Slack API to create a message in a channel or direct message with contents from another service is made easy in Transposit.

## Creating a notification trigger

In order to be useful, Notifications are best done as an automated process. In Transposit, there are two major ways to do this.

### Scheduled Tasks

If your notification needs to happen at a specified time on a regular basis, such as weekly, monthly, and so on, scheduled tasks are what you are looking for.

Scheduled Tasks can either be used only with Slack for something like a weekly reminder to update your sprint board, or with other integrations to help you with tasks such as relaying the weather for the day with Dark Sky. Learn more at the [Scheduled Tasks docs page](/building/scheduled-tasks/).

### Webhooks

If your notification has no scheduled time and instead needs to happen as soon as another activity has happened, webhooks are what you need.

To start a webhook operation, you will need to select a service that has webhook POSTing built in. Examples of services that do this are [Twilio](https://support.twilio.com/hc/en-us/articles/223136047-Configuring-Phone-Numbers-to-Receive-and-Respond-to-SMS-and-MMS-Messages), [Jira](https://developer.atlassian.com/server/jira/platform/webhooks/), and [GitHub](https://developer.github.com/webhooks). Learn more about creating webhooks in Transposit at our [docs page](/building/webhooks). Through a webhook, you can get data about what happened in the event, when it happened, and more, which can be passed into your notification.

## Sending a notification in Slack

To send your notification in Slack, you can use a few different Slack API calls.

- `post_chat_message` is the standard message that will be viewed by everyone in the channel.
- `post_chat_me_message` is functionally the same as above but in "/me" formatting.
- `post_chat_ephemeral` is an [ephemeral](https://api.slack.com/methods/chat.postEphemeral) chat message that will only be visible to a specified user, and will not persist across multiple Slack sessions.

Follow our [Quickstart](https://www.transposit.com/docs/get-started/quickstart/) for an example of sending a Slack message through Transposit. You can customize your message with [Slack Block Kit](https://api.slack.com/tools/block-kit-builder) to have it look the way you want it to.

### Further reading

If you would like to send your message as a bot user, look at our documentation for [chatbots](/docs/guides/slack/chatbots).

To create workflows through your notifications, look at our documentation for [workflows](/docs/guides/slack/workflows).

<a class="action-btn-blue br1 f5 fw5 ph4 pv3 dib mt2" href="/docs/guides/slack/">Return to Slack landing page</a>
