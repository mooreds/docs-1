## Google Calendar and Google Drive
To use Google's push notifications, you need to do a few things:

### Prerequisites
* A project in [google cloud](https://console.cloud.google.com)
* An application in Transposit

### Register your Transposit application domain with Google
* Follow the instructions at `Deploy > Site Verification`
* Add your newly verified domain: Use the same app url (e.g. https://api.transposit.com/app/org/app/) from the previous step and add it [here](https://console.cloud.google.com/apis/credentials/domainverification)

### Setup your OAuth2 credentials and enable the service API
You can use a Transposit operation to watch google events and register your previously
created webhook as the callback. However, the OAuth2 credentials must match the project
where you registered Transposit as a domain above. Google provides instructions for [set up OAuth 2.0](https://support.google.com/cloud/answer/6158849).
* Go to [Google Cloud Platform Console](https://console.cloud.google.com/) and select an
  existing project or create a new one.
* Select `APIs & services > Credentials`
* Click  `New Credentials > OAuth client ID`
* Either configure a consent screen if this is your first time or modify your existing consent screen to add `transposit.com` as an Authorized domain
* Select `Web application`
* Remember the Client ID and Client secret to be used in the next step and click Save.
* Select the credential you just created and add `https://api.transposit.com/oauthCallback` as an authorized redirect URI. If you did not properly set up your authorized domain in your consent screen in the earlier step, you may get an error `Invalid Redirect`. If so, follow the link and add `transposit.com` to the authorized domains list.
* Go to `APIs & Services > Library`, search for the correct API (e.g. Google mail, Google calendar, or Google Drive), and enable the API.

### Tell Transposit to use those OAuth2 Credentials
* In your Transposit application, add the data connector for the correct Google service
* Go to `Settings > Data Connections` and find your data connector under `Authentication`.
* Click `Configure`, replace the Client ID and Client secret with the values from the previous step.
* Save your changes
* Go back to `Code`, hover over your key and select remove key from the context menu.
* Add the key again with the your new credentials. You should now see your Google project's consent screen.

### Create a Webhook in Transposit to receive the callback
* Create a new application in Transposit
* Create a new operation, select `Webhook`, and commit the code
* Grab the http endpoint for the webhook under `Deploy > Endpoints`. Under the webhook there will be the deployed url.

### Watch
* Create a new SQL operation to initiate the watch.

Google Calendar Example:
TODO: this needs a random UUID...
```
SELECT * FROM google_calendar.watch_calendar_events
  WHERE calendarId='primary'
  AND $body='{
    "id" : "test",
    "address" : "https://api.transposit.com/app/name/app_name/api/v1/execute-http/webhook?api_key=XXX",
    "params" : {
      "ttl" : "86400"
    },
    "type" : "web_hook",
    "token" : "test-token"
  }'
```

### Schedule a task to refresh the watch
If you used the above ttl (which is in milliseconds), that means you will need to refresh the watch every day.

* Go to Deploy > Scheduled Tasks
* Create a new scheduled task
* Choose the watch operation you created above
* Use a cron schedule similar to `0 0 1 ? * * `
* Save the scheduled task

## FAQ
### I received an error: Unauthorized WebHook callback channel
This probably means you did not register your Transposit application domain with Google properly.
