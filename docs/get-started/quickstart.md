---
id: quickstart
title: Quickstart
---

Transposit is a zero-ops platform that lets developers instantly connect to and compose with APIs.

In this quickstart, we’re going to build a slash command in Slack that connects to an external data source. Slack commands trigger an app and display a custom response. Our command will display a random image of a dog&mdash;you can modify it later to work with cats, Pokemon, your calendar, updates from Github, or whatever data you want.

You can also [watch this in a short video](https://www.youtube.com/watch?v=6yfJWwA22oA).

## What you'll need

You'll need a Transposit account and a Slack account for this quickstart.

## 1. Create a new application

To begin a new project, [sign in to Transposit](http://console.transposit.com), and create a new _application_. A Transposit application is our unit of work&mdash;it holds the logic we'll build, connections to other APIs, authorization keys, user management, and deployment configuration.

Create your new application and name it _slack_dog_. Now you should see the Transposit code editor and tools you’ll be using to build with Transposit.

## 2. Create a new webhook

We'll use a webhook operation to receive events from Slack. Slack will invoke this when a user types your slash command.

* Click on the plus icon next to **Operations** and select webhook.

Transposit's hosting also requires sign-in by default so that only you and the people you've authorized can view your application.

Webhook operations are pre-configured with an `http_event` parameter that contains information from the HTTP event such as body and query parameters.

## 3. Add a data connection

Transposit comes with a number of pre-built data connectors, including one to the dog API. To give your application access to the dog API, you first need to add a data connection.

* Click on the plus icon next to **Data connections** to add a data connection.
* Search for _dog_ceo_ and select it.
* Select operation none since you will be using the javascript API in our webhook for this example
* Save

If a data connetion requires authentication, you'd be prompted to authenticate, but this one is public.

## 4. Implement your webhook

Next you’re going to modify your webhook operation to return a Slack message with a random dog image as an attachment. You will use the Slack `image_url` attachment type to post the image. The `api.run()` method lets you invoke operations in your own application or data connections. Here you’ll use it on dog_ceo’s operation `get_random_dog`.

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

You'll need to deploy your operation so that the http endpoint is publicly available.

* Navigate to the **Deploy** tab.
* Find your webhook operation and select Deploy.
* Check the _Require API Key_ checkbox for additional security as well as _Deploy as webhook_.
* Save your changes.
* Copy the URL for the deployed endpoint so that we can configure it in Slack.

## 5. Setup the Slack application

Next, let's create a new Slack app to call our webhook.

* Go to [slack's application page](https://api.slack.com/apps).
* Create a new slack app and name it _dog_app_.
* Select “Slash commands” from the list of features.
* Create a new command and name it _/dog_.
* Where it asks for a Request URL, paste the url for our webhook from the previous step.
* Optionally set a description such as _Give me a random dog image please!_.
* Save your new command.
* Install the application into your workspace.

## 6. Putting it all together

Now go to Slack to see it in action.

* Go to the Slack workspace where you installed your dog app.
* Type `/dog` in any channel.
* See a random picture of a dog!

## 7. Beyond the Quickstart

There's a lot more you can do with Transposit’s powerful relational engine. Please check out our docs to learn more!

* [Integrating multiple data sources together](sql-quickstart.md)
* [Data connectors currently available](../references/data-connectors.md)
