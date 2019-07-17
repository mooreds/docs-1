---
id: quickstart
title: Quickstart
layout: docs.mustache
tags: doc
---

In this short guide, you'll build a custom Slack command that lets anyone in your workspace list their day's events.

## Create a new Transposit application

- [Sign in to Transposit](https://console.transposit.com/).
- Click **New Slack app** and give it a name, such as `calendar_bot`.
- _Optional_: If you want to use other Slack APIs, such as post message for testing, then click `Connect` to authorize the Slack data connection.

## Set up Slack

- Go to [your Slack apps](https://api.slack.com/apps) and create a new app.
- Select **Slash Commands** from the list of Slack features. Create a new command named `/calendar`.
- Go back to Transposit to get the Request URL. Go to **Deploy &gt; Endpoints** (the rocket icon) and copy the webhook URL. Paste this into the Slack command's **Request URL** field. Give it a short description and usage hint if desired.
- Save your command.
- Click **Install App** in the sidebar to install it into your workspace.
- Test the app in Slack by typing `/calendar`. You should receive the "Please configure your user" message.

## Connect to Google Calendar

- Go to your Transposit app's Code section.
- Click the plus icon next to **Data Connections** and add `transposit/google_calendar`.
- Choose the `get_calendar_events` operation as the code template.
- Click **Save** and authorize Google Calendar.

## Get the day's start and end time

- Create a new JavaScript operation by clicking the plus icon next to **Operations**, and name it `get_day_start_end` in the **Properties** tab.
- Replace the code with the following to use the `moment.js` library to get the day's start and end time:

```javascript
params => {
  let moment = require("moment-timezone-with-data.js");
  let today = moment().tz("America/Los_Angeles");
  return {
    start: today.startOf("day").format(),
    end: today.endOf("day").format()
  };
};
```

- Click the **Run** button to make sure it works.

## Set up the user configuration page

- Go to **Users &gt; User Configuration** (the badge icon) and check the box next to `google_calendar` to allow users to connect their Google Calendar to their slack account.

## Get your slack command to return calendar events

- Go to your operation `get_calendar_events` and replace the SQL with the following to join together the start and end time from `get_day_start_end` with the Google Calendar call.

```sql
SELECT summary FROM google_calendar.get_calendar_events as E
  JOIN this.get_day_start_end AS T
  ON E.timeMin=T.start
  AND E.timeMax=T.end
  AND E.singleEvents=true
  WHERE E.calendarId='primary'
  LIMIT 100
```

- Edit the `get_slack_message` operation so it returns calendar events for the day.

```javascript
({ user }) => {
  let events = api
    .run("this.get_calendar_events")
    .map(e => e.summary)
    .join("\n");
  return {
    // Blocks get displayed in the actual message.
    // You can play with block kit here: https://api.slack.com/tools/block-kit-builder
    blocks: [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: events === "" ? "You have no events today" : events
        }
      }
    ],
    // The text content gets displayed in the notification
    text: "A message from Transposit!"
  };
};
```

- Click the **Commit code** button to commit the code.

## Configuring your production user

- Go to **Users &gt; User Configuration** to get the URL for your hosted user configuration page (e.g. https://calendar-bot-a1vud.transposit.io). Anyone in your Slack workspace can visit this page to configure their slack user to use this slash command.
- Login with your Slack account.
- Connect your Google Calendar.

## Use it in Slack

- Go to Slack and run `/calendar`. You should now see a list of your day's events.

## What's next

There's a lot you can do with Transposit’s powerful relational engine; imagine connecting in APIs from JIRA, AWS, GitHub, Airtable and more.

Check out other [sample apps](https://www.transposit.com/apps/) and [documentation](https://www.transposit.com/docs/) to learn more, including:

- [Integrating multiple data sources together](/docs/get-started/sql-quickstart)
- [Data connectors currently available](/docs/references/data-connectors)
