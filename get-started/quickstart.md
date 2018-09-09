# Quickstart

## Problem
In this demo, I’m going to build a data-driven application using Transposit.

Sometimes you have a spreadsheets where one of the columns is an email address indicating the owner of the data in that row. And you want to give access to only the rows that belong to the owner. Google sheets does not offer this sort of functionality, but we can easily build this kind of customizable logic with Transposit.

## Prerequisites
- A google account
- A google spreadsheet with content similar to  [form](https://docs.google.com/spreadsheets/d/1zwe5BJV8QrCK-WEGw5dt_kOPIRGmI_0Qw757bym21ow/edit#gid=0)... where each row has an email address for the owner who has access

## Things not covered in this quickstart but you might be interested in
- Allowing user specified auths through our managed connect page
- Integrating multiple data sources together

## Building in Transposit

### Create a new application
Building a new application is simple. Create a new application, give it a name, and pick a template. For this demo, we will use the "Simple app" template.

#### Hosted applications
With Transposit we automatically set up a hosted application for you to build and test but also share with friends to get instant feedback while you are developing your application. We've provided a gated front door so that only you and the people you've authorized have access to view your application.
- If you look at the `documentation` tab in the lower half of the code window, you can see in the quickstart manual that there is a link to the hosted app page. If you click it, it will populate your published and available application with the gated front-door that only you have access to.
- If you login with the same google account as your Transposit development account, you can access the app.
- Once logged in you will see some stub data displayed
- If you go back to the Transposit code editor and select the `helloworld` operation, you will see the operation the hosted application calls.
- Try adding italian to the list of languages:
```
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
- Hit the `Commit code` button in the upper right.
- Go to the other tab where your hosted app is open and reload to see the new data.

#### Populating the data
We want to fetch the values from the google spreadsheet. Then we can filter those values to only return the rows owned by a given email address in the form that the hosted application expects.

#### Adding data connectors
- Click on the plus icon next to `Data connections` to add a new data connector.
- Search for `Google sheets` and add the data connector.
- Notice you'll be prompted to authorize. We allow you to use our oauth application credentials so that you can get instant access to your data. But you can [supply your own credentials](TODO) in the future to customize the authorization screen.

#### Using SQL to query your data
- Add a new operation by clicking the plus icon next to `Operations`
- Choose `SQL from template` and then choose the scaffold operation `get_sheet_values`.
- You only need to specify a spreadsheetId and range. You can fill in the information for the private spreadsheet you created, but it should look something like:
```
SELECT * FROM google_sheets.get_sheet_values
  WHERE range='Sheet1'
  AND spreadsheetId='1zwe5BJV8QrCK-WEGw5dt_kOPIRGmI_0Qw757bym21ow' EXPAND BY `values`
```
TODO: remove the EXPAND BY once https://transposit.atlassian.net/browse/TR-2150 is done
- Click the run button and you should see your results

> _Note that in addition to passing through parameters in your SQL statement, you can also filter out the result values in the WHERE clause. See our [SQL tutorial](TODO) and our [SQL reference](TODO) for more information_

#### Mixing in JavaScript
Sometimes it is easiest to use a bit of JavaScript to manipulate data and encode some business logic. In this case since the result of the google sheets call is fairly unstructured, we are going to use JavaScript to give it a bit of structure.
- Click the new operation button and select JavaScript

Notice in the comment that there is a method called `api.run` that is available for you to call other operations. This can include data sources (e.g. google_sheets, similar to the SQL interface) as well as other operations in your application using the `this` syntax. You can also do things like access the current user using `api.user()`. See our [JavaScript Operations Reference](TODO) for more information.
- Replace the return in your JavaScript operation with the following to filter out only rows that match
```
return api.run('this.get_sheet_values_1').filter(function(item) {
  return item.values[0] === api.user().email;
}).map(function(item) {
  return {
    message: item.values[1]
  }
});
```
- You can give this operation a friendlier name like `get_user_messages` by clicking on the `Properties` tab.
- Commit all your code by clicking the `Commit code` button one more time

#### Deploying your operation
By default the http endpoints for your operations (other than the default helloworld operation we created for you) are private. Since we want our hosted app to be able to hit our newly created operation, we need to deploy that operation.
- Click the `Deploy` menu item
- Find your `get_user_messages` operation and select `Deployed`
- Since we require user information (i.e. the user's email), check the `Require user sign-in` checkbox.
- Click the `Save` button to save your configuration changes.

#### Setting production credentials
The credentials you add in the development console is only for development. You can choose to either have your users provide credentials or provide them for all your users. In this case since only you have access to your spreadsheet, you will provide the credentials for your user. To learn more about the various managed auth, you can read our [overview of the auth features we provide](TODO).
- Click the `Authentication` menu item
- Select the `Production Keys ` sub-menu
- Click the `Add key` button, select `google_sheets`, and authorize

#### Putting it all together
- Go back to the `Code` tab
- Go to your hosted app template by clicking on the `Page template` sub-menu
- Replace the line `var operation = "helloworld";` with `var operation = "get_user_messages";`
- Click the `Preview` button to preview the results. Note that anytime you make a change, you need to click this preview button to see the changes. Reloading the preview will not work.
- Now that you see that it works, go back to Transposit and commit your code changes so that you'll see it in the public link that you can once again access in your documentation manual.

#### Making it available to everyone
By default your hosted app is only available to you. To make it available to more people, you need to either add users to the whitelist or make it public.
- Click the `Authentication` tab
- Either click `Allow sign in from any Google account` or else add your GSuite domain name or individual emails to the whitelist.
