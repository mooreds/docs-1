# Endpoints

By default, operations are private. In order to make endpoints publicly accessible via HTTP, they must be explicitly deployed.

The exception to this: operations bundled as part of [hosted app templates](hosted-apps.md) are by default deployed at the time of app creation.

Deployed Transposit operation URL:

```text
https://api.transposit.com/app/{maintainer}/{serviceName}/api/v1/execute/{operationId}
```

Additional parameters and headers may be required depending on how endpoints are comfigured, so the easiest way to determine how to call an endpoint is to visit **Deploy &gt; Setup** and select the operation for your endpoint.

## Deploying an endpoint

1. Navigate to **Deploy &gt; Endpoints**
2. Find the operation you want to deploy
3. Choose **Deployed** from the dropdown menu

Once you select **Deployed**, you have a few different options, outlined below:

### Require API key

API keys are a simple, hard-to-guess string that can be used to protect your endpoint. You can find your application's API key by visiting **Deploy &gt; API Key**. If you have an API key enabled, you must provide it as a query parameter:

```text
https://api.transposit.com/app/{maintainer}/{serviceName}/api/v1/execute/{operationId}?api_key={API_KEY}
```

### Require user sign-in

Requiromg user sign-in allows you to identify the user calling your endpoint. The best way to call an endpoint requiring sign in is to use the [JavaScript SDK](../references/js-sdk.md).

### Deploy as webhook

Change the deployment configuration to [webhook](https://github.com/transposit/docs/tree/a08ea2ce45c6152d6b4be267b492e9ebdbb07806/building/webhook.md).

