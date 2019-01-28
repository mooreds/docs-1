---

id: apify_crawler_documentation

title: Apify Crawler

version: v1.*.*

---

## create_crawler

Creates a new crawler with settings from a JSON object in the POST payload.
See [main documentation](https://www.apify.com/docs/crawler#basic-settings) for detailed description of crawler settings.
Unknown properties in the object are silently ignored.
The response is the full **Crawler settings** object as returned by the [Get crawler settings](#reference/crawlers/crawler-settings/get-crawler-settings) endpoint.
Note that there can be at most 100 crawlers per user account.
If you need more crawlers, please contact Apify support.

<details><summary>Parameters</summary>

#### user_id (required)

User ID. This value can be found under Account > Integrations. Note that this value is different from the username.

**Type:** string

#### $body

**Type:** object

#### desc

By default, records are sorted in the order in which they were created or added. This property is useful when fetching all the records, because it ensures that records that were created after the client started the pagination will not be skipped. If you specify desc=1 parameter, the records will be returned in the reverse order, i.e. from newest to oldest records.

**Type:** number

</details>

## delete_crawler

Deletes a specific crawler.
If the crawler was successfully deleted
the response will be empty with `204 (No Content)` status code,
otherwise [an error](#introduction/errors) is returned.

<details><summary>Parameters</summary>

#### crawler_id (required)

Custom or internal ID of the crawler. This value can be found under the crawler's Basic Settings.

**Type:** string

#### user_id (required)

User ID. This value can be found under Account > Integrations. Note that this value is different from the username.

**Type:** string

#### executionId

Crawler execution ID for which the crawler settings should be returned.

**Type:** string

#### noSecrets

If `1` then the response will only contain crawler settings and no sensitive data such as links to API related endpoints that contain authentication tokens.
This option is used to export crawler configuration to JSON file that can be shared with other users.

**Type:** string

</details>

## execute_crawler

Starts execution of a specific crawler. In order to override crawler settings, include a **Crawler settings** JSON object as the POST payload.
Note that if the POST payload is empty or does not define particular properties, the properties from the stored crawler settings are used by default.
See [main documentation](https://www.apify.com/docs/crawler#basic-settings) for detailed description of the crawlers settings.
The response is an **Execution details** object.
There are basically three ways to determine that the crawler execution finished:
1. For short executions, you can pass a `wait=N` query parameter to the request which will cause the server to synchronously wait for the execution to finish. If the execution does not finish in `N` or 120 seconds (whichever is smaller), the endpoint will return an **Execution details** object with status `RUNNING`, similarly as if the `wait` query parameter was not provided. Make sure your HTTP client has a long enough timeout or it will disconnect before the server sends the response. 2. For longer executions, you can periodically poll the corresponding [Execution details](#reference/executions/execution-details) API endpoint until the execution finishes (i.e. `finishedAt` becomes not null). When you send a `GET` request to that endpoint, the response will contain the same **Execution details** object as the original response but with up-to-date values. For your convenience, the URL to the endpoint is provided as the `detailsUrl` attribute in the responses. **IMPORTANT:** You must always wait between the polling requests for a reasonable period of time (e.g. 60 seconds) or your requests will be throttled and you will start receiving errors. 3. You can also use the [Finish webhook](https://www.apify.com/docs/crawler#finishWebhookUrl) crawler setting to automatically receive a HTTP request to your own endpoint when the crawler execution finishes. Note that it is possible to tag the crawler execution with a custom string by adding a `tag` query parameter (e.g. `tag=my_test_run`). The tag will be included in the **Execution details** object and it can be used for bookkeeping. The maximum length of the tag is 64 characters.
Please also note that if you override `proxyGroups` parameter of crawler that does not have `proxyType` parameter set and you do not provide this parameter yourself, it will automaticaly be set to `SELECTED_PROXY_GROUPS`.

<details><summary>Parameters</summary>

#### crawler_id (required)

Custom or internal ID of the crawler. This value can be found under the crawler's Basic Settings.

**Type:** string

#### user_id (required)

User ID. This value can be found under Account > Integrations. Note that this value is different from the username.

**Type:** string

#### $body

**Type:** object

#### tag

Custom tag for the execution. It cannot be longer than 64 characters.

**Type:** string

#### wait

The maximum number of seconds the server waits for the execution to finish. By default it is `0`, the maximum value is `120`.

**Type:** string

</details>

## get_crawler

Gets full details and settings of a specific crawler.
The response is a **Crawler settings** object - see [main documentation](https://www.apify.com/docs/crawler#basic-settings) for a detailed description of the settings.

<details><summary>Parameters</summary>

#### crawler_id (required)

Custom or internal ID of the crawler. This value can be found under the crawler's Basic Settings.

**Type:** string

#### user_id (required)

User ID. This value can be found under Account > Integrations. Note that this value is different from the username.

**Type:** string

#### executionId

Crawler execution ID for which the crawler settings should be returned.

**Type:** string

#### noSecrets

If `1` then the response will only contain crawler settings and no sensitive data such as links to API related endpoints that contain authentication tokens.
This option is used to export crawler configuration to JSON file that can be shared with other users.

**Type:** string

</details>

## get_crawler_executions

Gets a list of executions of a specific crawler. Optionally, you can use `status` parameter to filter the list to only contain executions with a specific status (for example, `status=RUNNING` will only return executions that are still running). The response is a JSON array of objects which describe details of the particular executions. By default, the objects are sorted by the `startedAt` field in ascending order, therefore you can use pagination to incrementally fetch all executions while new ones are still being started. To sort them in descending order, use `desc=1` parameter. The endpoint supports [pagination](#introduction/pagination). A single response will not return more than 1000 array elements.

<details><summary>Parameters</summary>

#### crawler_id (required)

Custom or internal ID of the crawler. This value can be found under the crawler's Basic Settings.

**Type:** string

#### user_id (required)

User ID. This value can be found under Account > Integrations. Note that this value is different from the username.

**Type:** string

#### desc

By default, records are sorted in the order in which they were created or added. This property is useful when fetching all the records, because it ensures that records that were created after the client started the pagination will not be skipped. If you specify desc=1 parameter, the records will be returned in the reverse order, i.e. from newest to oldest records.

**Type:** number

#### status

Filter for the execution status.

**Type:** string

</details>

## get_crawler_last_execution_details

Gets information about the last execution of a specific crawler.
Optionally, you can use `status` parameter to only get the last execution with a specific status, e.g. `status=SUCCEEDED`.
The response is an **Execution details** object corresponding to the last execution, or empty response with `204 (No content)` status code if there is no matching execution.

<details><summary>Parameters</summary>

#### crawler_id (required)

Custom or internal ID of the crawler. This value can be found under the crawler's Basic Settings.

**Type:** string

#### user_id (required)

User ID. This value can be found under Account > Integrations. Note that this value is different from the username.

**Type:** string

#### status

Filter for the execution status.

**Type:** string

</details>

## get_crawler_last_execution_results

Gets results from the last crawler execution, i.e. an execution with the latest start time regardless of its status.
Optionally, you can provide the `status` parameter to only get the last execution with a specific status (e.g. `status=SUCCEEDED`).
The response contains results which are formatted and paginated as described in the [beginning of this section](#reference/results).
Note that the results might be incomplete if the execution is still running.
If there is no matching execution or the last execution still has no results, the response will be empty with `204 (No Content)` status code.

<details><summary>Parameters</summary>

#### crawler_id (required)

Custom or internal ID of the crawler. This value can be found under the crawler's Basic Settings.

**Type:** string

#### user_id (required)

User ID. This value can be found under Account > Integrations. Note that this value is different from the username.

**Type:** string

#### bom

All responses are encoded in UTF-8 encoding. By default, the `csv` files are prefixed with
the UTF-8 Byte Order Mark (BOM), while `json`, `jsonl`, `xml`, `html` and `rss` files are not.
If you want to override this default behavior, specify `bom=1` query parameter to include the BOM or `bom=0` to skip it.

**Type:** number

#### hideUrl

If set to `1` then `url` field will not be added to each page function result object. By default each page function result object contains `url` field.

**Type:** number

#### simplified

If `1` then the results will be returned in a simplified form without crawling metadata. By default full results are returned.

**Type:** number

#### skipFailedPages

If set to `1` then pages with non-empty `errorInfo` property are skipped from the output and the `errorInfo` property is hidden. Note that the skipped pages are still counted in the pagination.

**Type:** number

#### status

Filter for the execution status.

**Type:** string

</details>

## get_crawlers_by_user

Gets a list of crawlers belonging to a specific user.
The response is a JSON array, where each element is an object with basic information about one crawler.
By default, the objects are sorted by the `createdAt` field in ascending order, therefore you can use pagination to incrementally fetch all crawlers while new ones are still being created.
To sort them in descending order, use `desc=1` parameter.
The endpoint supports [pagination](#introduction/pagination).
A single response will not return more than 1000 array elements.

<details><summary>Parameters</summary>

#### user_id (required)

User ID. This value can be found under Account > Integrations. Note that this value is different from the username.

**Type:** string

#### desc

By default, records are sorted in the order in which they were created or added. This property is useful when fetching all the records, because it ensures that records that were created after the client started the pagination will not be skipped. If you specify desc=1 parameter, the records will be returned in the reverse order, i.e. from newest to oldest records.

**Type:** number

</details>

## get_execution_details

Gets details of a single crawler execution. The response is an **Execution details** object which contains information about the execution.
This API endpoint does not use any authentication token.
The caller only needs to know a hard-to-guess crawler execution ID, which will not grant them any other privileges except to view execution details, stop execution if still running and access its results.

<details><summary>Parameters</summary>

#### execution_id (required)

Crawler execution ID. This value can be found under the crawler's Runs tab. Click on a specific run to find the execution ID under Info.

**Type:** string

</details>

## get_execution_results

Gets results from a specific crawler execution.
The response contains results which are formatted and paginated as described in the [beginning of this section](#reference/results). Note that the results might be incomplete if the execution is still running.
This API endpoint does not use any authentication token.
The caller only needs to know a hard-to-guess crawler execution ID, which will not grant them any other privileges except to view execution details, stop execution if still running and access its results.

<details><summary>Parameters</summary>

#### execution_id (required)

Crawler execution ID. This value can be found under the crawler's Runs tab. Click on a specific run to find the execution ID under Info.

**Type:** string

#### bom

All responses are encoded in UTF-8 encoding. By default, the `csv` files are prefixed with
the UTF-8 Byte Order Mark (BOM), while `json`, `jsonl`, `xml`, `html` and `rss` files are not.
If you want to override this default behavior, specify `bom=1` query parameter to include the BOM or `bom=0` to skip it.

**Type:** number

#### desc

By default, records are sorted in the order in which they were created or added. This property is useful when fetching all the records, because it ensures that records that were created after the client started the pagination will not be skipped. If you specify desc=1 parameter, the records will be returned in the reverse order, i.e. from newest to oldest records.

**Type:** number

#### hideUrl

If set to `1` then `url` field will not be added to each page function result object. By default each page function result object contains `url` field.

**Type:** number

#### simplified

If `1` then the results will be returned in a simplified form without crawling metadata. By default full results are returned.

**Type:** number

#### skipFailedPages

If set to `1` then pages with non-empty `errorInfo` property are skipped from the output and the `errorInfo` property is hidden. Note that the skipped pages are still counted in the pagination.

**Type:** number

</details>

## stop_crawler_execution

Stops a specific crawler execution. The response is an **Execution details** object. Note that if the execution was already stopped or finished, the operation has no effect and returns the **Execution details** object unchanged. This API endpoint does not use any authentication token.
The caller only needs to know a hard-to-guess crawler execution ID, which will not grant them any other privileges except to view execution details, stop execution if still running and access its results.

<details><summary>Parameters</summary>

#### execution_id (required)

Crawler execution ID. This value can be found under the crawler's Runs tab. Click on a specific run to find the execution ID under Info.

**Type:** string

</details>

## update_crawler

Updates a specific crawler with settings from a JSON object in the PUT payload.
See [main documentation](https://www.apify.com/docs/crawler#basic-settings) for a detailed description of the settings.
The input object might be a subset of the **Crawler settings** object.
If the input object does not define a certain property, the corresponding setting will not be updated and will keep its existing value.
Note that the `null` value will set the corresponding setting to `null`.
Unexpected properties in the object are silently ignored.
The response is the full **Crawler settings** object as returned by the [Get crawler settings](#reference/crawlers/crawler-settings/get-crawler-settings) endpoint.

<details><summary>Parameters</summary>

#### crawler_id (required)

Custom or internal ID of the crawler. This value can be found under the crawler's Basic Settings.

**Type:** string

#### user_id (required)

User ID. This value can be found under Account > Integrations. Note that this value is different from the username.

**Type:** string

#### $body

**Type:** object

#### executionId

Crawler execution ID for which the crawler settings should be returned.

**Type:** string

#### noSecrets

If `1` then the response will only contain crawler settings and no sensitive data such as links to API related endpoints that contain authentication tokens.
This option is used to export crawler configuration to JSON file that can be shared with other users.

**Type:** string

</details>

