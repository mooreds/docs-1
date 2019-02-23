---
id: quickstart
title: Quickstart
---

Transposit is a zero-ops platform that lets developers instantly connect to and compose with APIs.

In this quickstart, we’re going to build a slash command in slack that connects to an external data source. Slack commands trigger an app and display a custom response. Our command will display a random image of a dog--you can modify it later to work with cats, Pokemon, your calendar, updates from Github, or whatever data you want.

TODO: embed video in the Quickstart

## What you'll need

You'll need a Transposit account and a slack account for this quickstart.

## 1. Create a new application

To begin a new project, [sign in to Transposit](http://console.transposit.com), and create a new _application_. A Transposit application is our unit of work -- it holds the logic we'll build, connections to other APIs, authorization keys, user management, and deployment configuration.

Create your new application and name it _slack_dog_. Now you should see the Transposit code editor and tools you’ll be using to build with Transposit.

## 2. Create a new webhook

You will use a webhook operation to receive events from slack. Slack will invoke this when a user types your slash command

* Click on the plus icon next to **Operations** and select webhook.
Transposit's hosting also requires sign-in by default so that only you and the people you've authorized can view your application.

Webhook operations are pre-configured with an http_event parameter that contains information from the HTTP event such as body and query parameters.

## 3. Add a data connection

Transposit comes with a number of pre-built data connectors, including one to the dog api. To give your application access to the dog api, you first need to add it as a data connector.

* Click on the plus icon next to **Data connections** to add a data connection.
* Search for _dog_ceo_ and select that connector.
* Select operation none since you will be using the javascript API in our webhook for this example
* Save

If a data connector requires auth, you'd be instantly prompted to authenticate, but this one is public.

## 4. Implement your webhook

Next you’re going to modify your webhook operation to return a slack message with a random dog image as an attachment. You will use the slack image_url attachment type to post the dog image. The api.run() method lets you invoke operations in your own application or data connections. Here you’ll use it on dog_ceo’s operation “get_random_dog”.

* Select your newly created webhook operation
* Replace the JavaScript with the following code:
```javascript
({ http_event }) => {
  return {
    status_code: 200,
    headers: { "Content-Type": "application/json" },
    body: {
      attachments: [{
        image_url: api.run('dog_ceo.get_random_dog')[0].message
      }]
    }
  };
}
```

* Click the **Run** button to test your operation.
* Click the **Commit** button to commit your code.

## 4. Deploy your operation

You'll need to deploy your operation so that the http endpoint is publicly available

* Navigate to the **Deploy** tab.
* Find your webhook operation and select Deploy.
* Check the _Require API Key_ checkbox for additional security as well as _Deploy as webhook_.
* Save your changes.
* Copy the URL for the deployed endpoint so that we can configure it in slack.

## 5. Setup the Slack application

You will need to create a new Slack app to call our webhook.

* Go to [slack's application page](https://api.slack.com/apps)
* Create a new slack app and name it _dog_app_
* Select “Slash commands” from the list of features
* Create a new command and name it _/dog_.
* Where it asks for a Request URL, paste the url for our webhook from the previous step.
* Optionally set a description such as _Give me a random dog pic please!_
* Save your new command
* Install the application into your workspace

## 6. Putting it all together

Now go to slack to see it in action.

* Go to your slack workspace where you installed your dog app.
* Type _/dog_ in any channel.
* See a random picture of a dog!

## 7. Beyond the Quickstart

See how easy it is to build a simple app. But, there is a lot more you can do with Transposit’s powerful relational engine. Please check out our docs to learn more!

* [Integrating multiple data sources together](sql-quickstart.md)
* [Data connectors currently available](../references/data-connectors.md)
