# Endpoints

By default, operations other than default operations created for you by the hosted app templates are private. In order to make them publicly accessible via HTTP endpoints, you need to explicitly deploy them.

Deployed Transposit operation URL:

```text
https://api.transposit.com/app/v1/{maintainer}/{serviceName}/api/execute/{operationId}
```

However, additional parameters and headers may be required depending on how you configure your endpoint, so the easiest way to determine how to call your endpoint is to visit **Deploy &gt; Setup** and select the operation for your endpoint.

## Deploying an endpoint
1. Navigate to **Deploy &gt; Endpoints**
2. Find the operation you want to deploy
3. Choose **Deployed** from the dropdown

Once you select the **Deployed** option, you have a few different options.

#### Require API key
API keys are a simple hard to guess string that can be used to protect your endpoint. You can find your application's API key by visiting **Deploy &gt; API Key**. If you have an API key enabled, you need to provide it as a query parameter:

```text
https://api.transposit.com/app/v1/{maintainer}/{serviceName}/api/execute/{operationId}?api_key={API_KEY}
```

#### Require user sign-in
Require user sign-in allows you to identify the user calling your endpoint. The best way to call an endpoint requiring sign in is to use the [JavaScript SDK](../references/js-sdk.md).

#### Deploy as webhook
Change the deployment style to [webhook](webhook.md)
