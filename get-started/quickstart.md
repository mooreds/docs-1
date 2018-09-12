# Quickstart

In this guide, you'll build a data-driven application using Transposit.

TO DO: add in real-world context; keep a lot of data in a spreadsheet you maintain in one place. want to create an interface that allows people to view data that they specifically have access to, not the entire sheet, without having to manually create other data sources that are hard to maintain. access to specific pieces. departments, for example. one way to designate ownership of particular rows could be to specificy owner email in a column in a spreadsheet.  

Suppose you have a spreadsheet where the first column is an email address indicating the owner of the data in that row. You want to give access to only the rows that belong to the owner. Google sheets does not offer this sort of functionality, but we can easily build this kind of customizable logic with Transposit.

## What you'll need

You'll need a Google account with access to Google Docs, and a Google Docs spreadsheet where each row has an email address for the person who has access to that row.

To make it easy, you can [copy this sample spreadsheet](https://docs.google.com/spreadsheets/d/1zwe5BJV8QrCK-WEGw5dt_kOPIRGmI_0Qw757bym21ow/copy) for use in this guide. **Note:** you can copy the `spreadsheetId` [from the document's URL](https://stackoverflow.com/questions/36061433/how-to-do-i-locate-a-google-spreadsheet-id).

TO DO: screenshot of spreadsheet URL with ID highlighted

Here's the format of the spreadsheet, with data owner email addresses in the left column, and the data you want them to have access to in the right column:


| Email address       | Data                                       |
|---------------------|--------------------------------------------|
| you@domain.com      | This is some sample data that is available |
| you@domain.com      | Some more data that is available           |
| iggy@transposit.com | Iggy's data you can't see                  |
| iggy@transposit.com | Iggy's data in this row too                |

{% hint style="info" %}
Be sure to replace some of these email addresses with your own in one or more of the spreadsheet rows.
{% endhint %}

## 1. Create a new application

TO DO: To build anything in Transposit, you'll need to first create a new application - this is our unit of work. 

Create a new application, give it a name, and pick the "Simple app" template for use in this guide.

## 2. View your app live

TO DO: add in context around why we want people to be able to see their app live as they develop and why we've baked that into the quickstart
- transposit lets you easily leverage templates to get the job done and hosting comes baked in from the very beginning
- we want you to see what your changes look like to your end users as you develop and add meaningful data

If you look at the **Documentation** tab in the lower half of the code window, you can see in the  manual that there's a link to the hosted app page. If you click it, it will populate your published and available application, accessible to you only, by signing in with your Google account.

Once signed in, you'll see some stub data displayed.

If you go back to the Transposit code editor and select the `helloworld` operation, you will see the operation the hosted application calls.

TO DO: change above sentence ^; our hosted apps are set up to call the hello world operation, so any changes you make to the operation here will be reflected in your hosted app. lets try that our by adding...

Try adding Italian to the list of languages by replacing the code in this operation with the sample below:

TO DO (tina): change code sample to include all code

```javascript
return [
  {
    "message": "Hello World"
  },
  {
    "message": "Hola Mundo"
  },
  {
    "message": "Ciao mondo"
  }
];
```

Click the **Commit code** button in the upper right to commit the changes. If you then go to the browser tab where your hosted app is open and refresh the page, you'll see the new data.

TO DO: hint around commit code vs run code (in this quickstart, we'll ask you to either commit or run code, here's how those are different

TO DO: see if below hint should be moved up to "hosted app" section

{% hint style="info" %}
Transposit automatically enables basic hosting, for building and testing and also to share with friends to get feedback while you're mid the development process. There's a gated front door (sign in is required) so that only you and the people you've authorized have access to view your application.
{% endhint %}

## 3. Add a data connector

TO DO: In order to get data from sources outside Transposit, you need to add them as a data connector. This is how you'll be able to import the data stored in that spreadsheet. 

Next we'll fetch the values from the spreadsheet, then filter those values to only return the rows owned by a given email address in the form that the hosted application expects.

* Click on the plus icon next to **Data connections** to add a data connector.
* Search for **Google Sheets** and add it.

Notice that you'll be prompted to authorize. Transposit allows you to use our oAuth application credentials so you can get instant access to your data. But you can also supply your own credentials later on to customize the authorization screen.

TO DO: clarify above: what is the difference between our and your credentials (see tina's screenshot example for slack) - but also keep in mind that this is just a "dont worry"; maybe make it a hint box

## 4. Use SQL to query your data

TO DO: what is an operation and why are we creating it. Now that you've connected your sheets data and given your application access to it, you want to add functionality that allows your application to query the contents of this sheet and view/explore it from within Transposit.  

* Add a new operation by clicking the plus icon next to **Operations**.
* Choose **SQL from template** and then choose the template operation `get_sheet_values`.

TO DO: What this template is doing is showing you all of the possible options that you can call for this operation. Roughly, it's showing you what parameters are available to the API, without having to go to the docs. Some are required, and some are optional.  

Here, you only need to specify `spreadsheetId` and `range`. You can fill in the information for the private spreadsheet you created or copied, and it should look something like this:

```SQL
SELECT * FROM google_sheets.get_sheet_values
  WHERE range='Sheet1'
  AND spreadsheetId='<INSERT YOUR SPREADSHEET ID>'
```

TO DO (tina): add information about being able to delete or comment out any additional parameters; or do a "replace that code with this code"

* Now click the **Run** button and you should see your results.
* You'll notice that the results are something like the following, showing you your sheet data row by row (TO DO):


```text
[
  {
    "range": "Sheet1!A1:Z999",
    "majorDimension": "ROWS",
    "values": [
      [
        "hello@transposit.com",
        "This is some sample data that is available"
      ],
      ...
    ]
  }
]
```

Transposit introduces a few conveniences to SQL for working with JSON, including [EXPAND BY](references/sql-operations.md). If you want to extract the items in the values array to ... (TO DO: add real life result), you can use the `EXPAND BY` syntax. However, since `values` is a SQL keyword, it must be escaped  with backticks.

Try expanding the results using something similar to the following:

```sql
SELECT * FROM google_sheets.get_sheet_values
  WHERE range='Sheet1'
  AND spreadsheetId='<INSERT YOUR SPREADSHEET ID>' EXPAND BY `values`
```

{% hint style="info" %}Note that in addition to passing through parameters in your SQL statement, you can also filter out the result values in the `WHERE` clause. See the [SQL quickstart](get-started/sql-quickstart.md) and the [SQL reference](references/sql-operations.md) for more information.
{% endhint %}

## 5. Mixing in JavaScript

Sometimes it's easiest to use a bit of JavaScript to manipulate data and encode some business logic. In this case since the result of the Google Sheets call is fairly unstructured, let's  use JavaScript to give it a bit of structure.

* Click the new operation button and select JavaScript
* Replace your JavaScript operation with the following code to filter out rows that match:

```javascript
function run(params) {
  var results = api.run('this.get_sheet_values_1').filter(function(item) {
    return item.values[0] === api.user().email;
  }).map(function(item) {
    return {
      message: item.values[1]
    }
  });
  if (results.length === 0) {
    return {
      message: 'There are no spreadsheet rows available to ' + api.user().email
    };
  } else {
    return results;
  }
}
```

* You can give this operation a friendlier name like `get_user_messages` by clicking on the **Properties** tab.
* Commit all your code by clicking the **Commit code** button one more time.

{% hint style="info" %}
In the commented code there's a method named `api.run` that is available for you to call other operations. This can include data sources (e.g. google_sheets, similar to the SQL interface) as well as other operations in your application using the `this` syntax. You can also do things like access the current user using `api.user()`. See the [JavaScript Operations Reference](references/js-operations.md) for more information.
{% endhint %}

## 6. Deploying your operation

By default, the HTTP endpoints for your operations (other than the default `helloworld` operation we created for you) are private. TO DO: segue -- how does private have to do with deploying operation? Since this hosted app should be able to hit our newly created operation, we need to deploy that new operation.

* Click the **Deploy**  in the navigation menu.
* Find your `get_user_messages` operation and select **Deployed**
* Since we require user information (i.e. the user's email), ensure the **Require user sign-in** checkbox is checked.
* Click the **Save** button to save your configuration changes.

## 7. Setting production keys

TO DO: Now that you've deployed, you need to give your users access to the spreadsheet data. or something???

The credentials you add in the development console are for use in development only. You can choose to have your users provide required credentials, or provide them for all your users. In this case, since only you have access to your spreadsheet, you will provide the required credentials for your users.

* Click **Authentication** in the navigation.
* Select the **Production Keys** section.
* Click the **Add key** button, select `google_sheets`, and authorize.

This uses the keys you've just personally provided in the context of running the application in production for other users.

TO DO: does his apply to all of your applications in transposit? 

To learn more about authentication options, see [Authentication](building/authentication.md).

## 8. Putting it all together

TO DO: what we're doing here

* Return to your application's code
* Go to your hosted app template by clicking on the **Page template** section
* Replace `var operation = "helloworld";` with `var operation = "get_user_messages";` (line 42 in the hosted app page markup).
* Click **Preview** to see the results. Note that any time you make a change to code or to the template, you need to click this preview button to see the changes. Reloading the preview will not work.
* Now that you see that it working in the preview, return to Transposit and commit your code changes so that you'll see it in the public link that you can once again access from your application manual.

TO DO: if you get the following error, you've probably forgotten to add your own emails to the spreadsheet. steps to do that and try again

## 9. Making it available to everyone

By default your hosted app is available to only you. To make it available to more people, either add users to the whitelist or make it public.

* Click **Authentication** in the navigation.
* You can choose **Allow sign in from any Google account**, or add your GSuite domain name, or add individual email addresses to the whitelist.
* Click the **Save** button to save any changes you've made.

Your app is now live!

## Related topics

* [Allowing user-supplied keys through the managed connect page](building/authentication.md)
* [Integrating multiple data sources together](building/sql-quickstart.md)
