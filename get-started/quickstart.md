---
id: quickstart
title: Quickstart
layout: docs.mustache
---

Transposit is an API composition platform that brings the power of a relational database to the API ecosystem.

In this quickstart guide, you'll use Transposit to build a custom Slack bot that provides a personalized experience with Google Calendar for your team.

## What you'll need

Before you get building, you'll need a Transposit account and a Slack account.

## Create a new application

To begin, [visit this list of sample apps](https://www.transposit.com/apps/), choose **Slackbot helper**, fork it and name your new copy `calendar_bot`.

## Add a production key

Add a credential available to all users of your app: go to **Deploy > Production Keys** and add a production key for the data connection `slack_bot`.

## Prepare a webhook

Next, go to **Deploy > Endpoints**, and copy the webhook URL for the operation `webhook`. You'll need this to configure Slack in the next step.

## Set up the Slack slash command

Visit [the Slack apps page](https://api.slack.com/apps), and create a new app. Give the new app a name something like **Calendar Helper**.

Select **Slash Commands** from the list of features, choose **Create New Comamnd** and create a new command called `/calendar`.

For the **Request URL**. paste in the webhook URL copied in the previous step, give the command a short description such as "List my day's events", and be sure to save.

When your slash command is created, choose **Install App** and install the Slack app into your workspace.

## Test in Slack

Back in your Slack workspace, you can now type `/calendar` (or whatever you titled the command) and see that it's installed and working, and that some additional setup is needed.

## Set up user configuration

Return to Transposit, and navigate to **User > User Configuration**. Here you can specify who has access to the app, and choose what data connections users must authenticate. Ensure that the `slack_identity` connection is set to require user authentication.

At the top, you'll see the URL for the app's user configuration page. 

## Authorize as a user

Visit the app's user configuration page the URL above, sign in, and connect Slack.

Return to your Slack workspace, type the slash command again, and you'll see that the app knows who you are on Transposit.

## Connect your calendar

Now that the Slack bot is working, get it talking to calendars.

Return to the app's code in the Transposit console, and add the Google Calendar data connector, with the operation `get_calendar_events`. The new operation contains a scaffold for how to use SQL to get calendar events. Note that you need to supply the calendar ID, start time, and end time.

In this app, we want the user to select which calendar to use, so add a new operation that's a **User Setting Options** type, paste in the following code, and commit to save:

```javascript
(params) => {
  if (api.isAuthed('google_calendar')) {
    return api.run('google_calendar.get_calendarlist').map((l) => {
      return {value: l.id, displayName: l.summary};
    });
  } else {
    return [
      {
        "value": "primary",
        "displayName": "Primary"
      }
    ];
  }
}
```

Then, go to **Users > User Configuration** and check the box to require users to authenticate with Google Calendar.

At the bottom of the page in the user settings schema, add a new item of type Options, set the **Name** to `calendar_id`, and specify that it use the `options` operation just previously created.

To try this out, visit the user configuration page again, refresh, and if your calendar connection is authorized you'll see a list of your calendars to select.

## Specify start and end times

Create a new JavaScript operation that you'll use to specify calendar start and end time. In the operation properties, name the operation `get_day_start_end`.

You can use the `api.run` command to call Google Calendar to get the calendar timezone, and you can access the configured `calendar_id` through the `user_setting` API. Paste this code into the new operation:

```javascript
(params) => {
  let moment = require('moment-timezone-with-data.js');  
  let timezone = api.run('google_calendar.get_calendar',
 {calendarId: user_setting.get('calendar_id')})[0].timeZone;
  let today = moment().tz(timezone);
  return {
    start: today.startOf('day').format(),
    end: today.endOf('day').format()    
  }
}
```

> **Note:** When you're in development mode, you must to provide authorizations and settings separate from those used in production. To do this, go to the **Auths and User Settings** section in the Code view. 

When you've added authorizations for using the data connections in development, run the operation to make sure it works.

## Putting it all together

Go back to the `get_calendar_events` operation you created earlier, add a parameter with the name `calendarId` and a default value of “primary", and then paste the following operation code:

```sql
SELECT summary FROM google_calendar.get_calendar_events as E
  JOIN this.get_day_start_end AS T
  ON E.timeMin=T.start
  AND E.timeMax=T.end
  AND E.singleEvents=true
  WHERE E.calendarId=@calendarId
  LIMIT 100
```

Next, edit the `found` operation (already in the application when you forked it) so it returns calendar events for the day, or tells you if you have no events:

```javascript
({slackBody}) => {
  let events = api.run('this.get_calendar_events', {
  calendarId: user_setting.get('calendar_id')
}).map((e) => e.summary).join('\n');
  let post = {
    channel: slackBody.channel_id,
    user: slackBody.user_id,
    text: `You've run the slack command`,
    blocks: [{
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": events === '' ? 'You have no events today' : events
      },
    }]
  }
  return api.run('slack_bot.post_chat_ephemeral', {$body: post});
}
```

Commit the code, return to your Slack workspace, and try it out. You should receive a list of the day's calendar events, or a message saying you don't have any events.

## Beyond the Quickstart

It's easy to build bots for your team, but there's a lot more you can do with Transposit’s powerful relational engine; imagine connecting in APIs from JIRA, AWS, GitHub, Airtable and more.

Check out other [sample apps](https://www.transposit.com/apps/) and [documentation](https://www.transposit.com/docs/) to learn more, including:

* [Integrating multiple data sources together](/docs/get-started/sql-quickstart)
* [Data connectors currently available](/docs/references/data-connectors)
