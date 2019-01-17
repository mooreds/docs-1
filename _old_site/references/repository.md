# Application Code Repository
Your application's code is stored and versioned in a git repository. You can clone the repository to view diffs or use your own editor tools to modify your application.

## File structure
* **manifest.json**: the main configuration for your application
* **public/index.html**: the HTML for your hosted app
* **\*.js**: The JavaScript files for your JavaScript operations

## Cloning Your repository
* Go to **Settings > App Info**.
* Grab the URL under **Source code**.
* Click the link to your **account settings page** or go to the dropdown for your username in the upper right hand  corner and click **Settings**.
* Copy the **Git access token** from this page
* Clone your repository using your username and your git access token. For convenience, you can also create a *.netrc* file in your home directory that stores these credentials. The file will have an entry that looks like the following:
```
machine console.transposit.com
        login <YOUR USER NAME>
        password <YOUR GIT ACCESS TOKEN>
```
