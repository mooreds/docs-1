---
id: google-push-notifications
title: Google push notifications
layout: docs.mustache
---

To use Google's push notifications, use the instructions below.

## Prerequisites

* A project in [Google Cloud](https://console.cloud.google.com)
* An application in Transposit

## Register your Transposit application domain with Google

* Follow the instructions at **Deploy > Site Verification**.
* Add your newly verified domain: Use the same app url (e.g. `https://console.transposit.com/app/org/app/`) from the previous step and add it [here](https://console.cloud.google.com/apis/credentials/domainverification).

## Set up your OAuth2 credentials and enable the service API

You can use a Transposit operation to watch Google events and register your previously
created webhook as the callback. However, the OAuth2 credentials must match the project
where you registered Transposit as a domain above. This means that you cannot use the Tranpsosit-provided OAuth settings, and [must provide your own client ID and secret](/docs/references/connector-authentication.md#generating-a-client-id-and-secret-with-google-connectors).

## Tell Transposit to use those OAuth2 credentials

* In your Transposit application, add the data connector for the desired Google service.
* If not prompted with a button to configure Authentication, click `Cancel` and go to **Code > Data Connections** and find your data connector. 
* Click **Authentication > Configure**, replace the Client ID and Client secret with the values from the previous step. 
* Save your changes.
* Click `Add Key` for your connector. You should now see your Google project's consent screen.

## Create a webhook in Transposit to receive the callback

* Create a new application in Transposit
* Create a new operation, select **Webhook**, and commit the code.
* Grab the http endpoint for the webhook under **Deploy > Endpoints**. Under the webhook you will find the deployed URL.

## Watch

Create a new SQL operation to initiate the watch.

Google Calendar example. The `@id` parameter should be a UUID or similar unique string that identifies this channel.

```
SELECT * FROM google_calendar.watch_calendar_events
  WHERE calendarId='primary'
  AND $body=(SELECT {
    "address" : "https://api.transposit.com/app/name/app_name/api/v1/execute-http/webhook?api_key=XXX",
    "type" : "web_hook",
    "token" : "test-token"
  })
  AND $body.id = @id
  AND $body.params.ttl = "86400" 
```

## Schedule a task to refresh the watch

If you used the above TTL (in seconds), you will need to refresh the watch every day.

* Go to **Deploy > Scheduled Tasks**.
* Create a new scheduled task.
* Choose the watch operation you created above.
* Use a cron schedule similar to `0 0 1 ? * * `.
* Save the scheduled task.

## Unauthorized webhook callback channel errors

If you receive this error, it probably means you did not register your Transposit application domain with Google properly.
