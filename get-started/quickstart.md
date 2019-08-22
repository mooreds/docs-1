---
id: quickstart
title: Quickstart
layout: docs.mustache
tags: doc
---

In this short guide, you'll build a custom Slack command that helps anyone in your workspace list their day's events from their own Google calendar.

## Before you start

You'll need:

* To be able to create applications in your Slack workspace. You can set up a free Slack workspace to use if you don't have the rights.
* A Google calendar account.
* A free Transposit developer account. 

You can also [watch this in a short video](https://youtu.be/D-yfw057uGk):

<div class="video-container">
<iframe src="https://www.youtube.com/embed/D-yfw057uGk"  frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Create a new Transposit application

- [Sign in to Transposit](https://console.transposit.com/).
- Click **New app** and give it a name, such as `calendar_bot`.

## Set up Slack

- Go to [your Slack apps](https://api.slack.com/apps) and create a new app.
- Select **Slash Commands** from the list of Slack features. Create a new command named `/calendar`.
- Go back to Transposit to get the Request URL. Go to **Deploy &gt; Endpoints** and copy the webhook URL. Paste this into the Slack command's **Request URL** field. Give it a short description and usage hint if desired.
- Save your command.
- Click **Install App** in the sidebar to install it into your workspace. (You can ignore any OAuth token messages.)
- Test the app in Slack by typing `/calendar`. You should receive the "Please configure your user" message.

## Connect to Google Calendar

- Go to your Transposit app's Code section.
- Add a new Data Connection and select `transposit/google_calendar`.
- Choose the `get_calendar_events` operation as the code template.
- Click **Save** and authorize Google Calendar.

## Get the day's start and end time

- Create a new JavaScript operation and name it `get_day_start_end`.
- Replace the code with the following to use the `moment.js` library to get the day's start and end time (replace `America/Los_Angeles` with your timezone if desired):

```javascript
params => {
  let moment = require("moment-timezone-with-data.js");
  let today = moment().tz("America/Los_Angeles");
  return {
    start: today.startOf("day").format(),
    end: today.endOf("day").format()
  };
}
```

- Click the **Run** button to make sure it works. You should see something like this if you click the 'Raw' tab of the Results pane.

```json
[
  {
    "start": "2019-08-20T00:00:00-07:00",
    "end": "2019-08-20T23:59:59-07:00"
  }
]
```

## Set up the user configuration page

- Go to **Users &gt; User Configuration** and check the box next to `google_calendar` to allow users to connect their Google Calendar to their slack account.

## Get your slack command to return calendar events

- Go to your operation `get_calendar_events` and replace the SQL with the following to transparently join together the start and end time from the `get_day_start_end` operation with the Google Calendar call.

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
}
```

- Click the **Commit code** button to commit the code.

## Configuring your production user

- Go to **Users &gt; User Configuration** to get the URL for your hosted user configuration page (e.g. https://calendar-bot-XXXXX.transposit.io). Anyone in your Slack workspace can visit this page to configure their slack user to use this slash command.
- Login with your Slack account.
- Connect your Google Calendar.

## Use it in Slack

- Go to Slack and run `/calendar`. You should now see a list of your day's events.

## What's next with your calendar application

There are a lot of ways to extend this application. Here are some things you can try:

* Share the Transposit application with other users on your Slack (they can already run `/calendar` since you installed it in the workspace). Don't they deserve to know what they have on the calendar from the comfort of their Slack command line? They can sign up with their Slack credentials at the same url: https://calendar-bot-XXXXX.transposit.io
* Edit and rename the `get_day_start_end` operation so that you display events from today and tomorrow.
* Review the [Google Calendar docs](/docs/references/connectors/google-calendar-documentation/). Include the location as well as the summary of the event. (Hint, change the Google Calendar operation to `select * from google_calendar.get_calendar_events ...` and see what comes back.)
* Include a list of the attendees when displaying events.
* Format the return values to look better with a section for each event. Explore Slack's block format: https://api.slack.com/tools/block-kit-builder and modify the JSON returned by `get_slack_message`.
* If you want to use other Slack APIs to extend the command (to do something like create a reminder based on upcoming events) then authorize the Slack data connection and explore [the Slack docs](/docs/references/connectors/slack-documentation/).

## What's next with Transposit

There's a lot you can do with Transposit’s powerful relational engine; imagine connecting APIs from JIRA, AWS, GitHub, Airtable and more.

Check out other [sample apps](/apps/) and [documentation](/docs/) to learn more, including:

- [Integrating multiple data sources together.](/docs/get-started/sql-quickstart)
- [Data connectors currently available.](/docs/references/data-connectors)
- [Creating your own data connector](/docs/references/create-a-data-connector/) to pull in your own OpenAPI compatible data.
- [Running a task on a schedule.](/docs/building/scheduled-tasks/)
