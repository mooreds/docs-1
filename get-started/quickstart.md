---
id: quickstart
title: Quickstart
layout: docs.mustache
tags: doc
---

Transposit is an API composition platform that brings the power of a relational database to the API ecosystem.

In this short guide, you'll use Transposit to build a custom Slack bot that provides a personalized experience with Google Calendar for your entire team.

You can also [watch this in a short video](https://youtu.be/98yMQpSjQIc):

<div class="iframe-container">
<iframe src="https://www.youtube.com/embed/98yMQpSjQIc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## What you'll need

To begin, you'll need a Transposit account and a Slack account.

## Create a new Transposit application

Sign in to Transposit and go to [your list of applications](https://console.transposit.com/)

Click **New Slack app** and title your app `calendar_bot`.

Next, in the new app's **Auth &amp; user settings** view, click Connect to authorize the Slack data connection.

## Set up Slack

On the Slack API website, go to [your apps list](https://api.slack.com/apps) and create a new app. Name the new app `calendar_helper`.

Select **Slash Commands** from the list of Slack features, and create a new command named `/calendar`.

To get the **Request URL**, return to Transposit, go to **Deploy &gt; Endpoints**, and copy the webhook URL. Paste this into the Slack command's **Request URL** field. Give it a short description and usage hint if desired.

Next, click **Install App** and install it into your workspace.

To test the app: in your Slack workspace, try running the `/calendar` slash command and you should receive a "Hello World!" message.

## Connect with Google Calendar

Go to your Transposit app's Code section, add the `transposit/google_calendar` data connection. Choose the `get_calendar_events` operation as the code template. Be sure to authorize the connection.

Next, create a new JavaScript operation and name it `get_day_start_end`:

```javascript
(params) => {
  let moment = require('moment-timezone-with-data.js');
  let today = moment().tz('America/Los_Angeles');
  return {
    start: today.startOf('day').format(),
    end: today.endOf('day').format()
  }}
  ```

This will calculate the day's start end end time. Run the operation and make sure it works.

## User configuration

This application should require users to supply their own credentials for Google Calendar. In **Users &gt; User Configuration** check the box next to the `google_calendar` data connection.

## Put it all together

Create an operation named `get_calendar_events` to join together the start and end time from `get_day_start_end`:

```sql
SELECT summary FROM google_calendar.get_calendar_events as E
  JOIN this.get_day_start_end AS T
  ON E.timeMin=T.start
  AND E.timeMax=T.end
  AND E.singleEvents=true
  WHERE E.calendarId='primary'
  LIMIT 100
```

Edit the `get_slack_message` operation so it returns calendar events for the day:

```javascript
({user}) => {
  let events =
      api.run('this.get_calendar_events').map((e) => e.summary).join('\n');
  return {
    // Blocks get displayed in the actual message. 
    // You can play with block kit here: https://api.slack.com/tools/block-kit-builder
    blocks: [{
      "type": "section",
      "text": {
          "type": "mrkdwn",
          "text": events === '' ? 'You have no events today' : events
      }
    }],
    // The text content gets displayed in the notification
    text: 'A message from Transposit!'
  };
}
```

Now, commit the code, and try it out: visit the app's user configuration page to connect Slack as an application user. Anyone in your Slack workspace can visit this page to connect their own Google Calendar and customize their experience.

Test things out in Slack by running the `/calendar` slash command again.

## What's next

There's a lot you can do with Transposit’s powerful relational engine; imagine connecting in APIs from JIRA, AWS, GitHub, Airtable and more.

Check out other [sample apps](https://www.transposit.com/apps/) and [documentation](https://www.transposit.com/docs/) to learn more, including:

* [Integrating multiple data sources together](/docs/get-started/sql-quickstart)
* [Data connectors currently available](/docs/references/data-connectors)
