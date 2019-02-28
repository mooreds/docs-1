---
id: aws-lambda-documentation
title: AWS Lambda (version v1.*.*)
sidebar_label: AWS Lambda
---

## add_policy_to_function

Grants an AWS service or another account permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN) of that version or alias to invoke the function. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### $body

**Type:** object

</details>

## add_policy_to_layer

Adds permissions to the resource-based policy of a version of an AWS Lambda layer. Use this action to grant layer usage permission to other accounts. You can grant permission to a single account, all AWS accounts, or all accounts in an organization. 

<details><summary>Parameters</summary>

#### layerName (required)

The name or Amazon Resource Name (ARN) of the layer. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+

**Type:** string

#### versionNumber (required)

The version number.

**Type:** string

#### $body

**Type:** object

</details>

## add_tag_to_function

Adds tags to a function. 

<details><summary>Parameters</summary>

#### resource (required)

The function's Amazon Resource Name (ARN). Pattern: arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### $body

**Type:** object

</details>

## create_alias_for_function

Creates an alias for a Lambda function version. Use aliases to provide clients with a function identifier that you can update to invoke a different version. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### $body

**Type:** object

</details>

## create_function



*This operation has no parameters*

## create_lambda_from_zip

Creates an AWS Lambda layer from a ZIP archive. Each time you call PublishLayerVersion with the same version name, a new version is created. 

<details><summary>Parameters</summary>

#### layerName (required)

The name or Amazon Resource Name (ARN) of the layer. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+

**Type:** string

#### $body

**Type:** object

</details>

## create_version_of_function

Creates a version from the current code and configuration of a function. Use versions to create a snapshot of your function code and configuration that doesn't change. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### $body

**Type:** object

</details>

## delete_alias_for_function

Deletes a Lambda function alias. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### name (required)

The name of the alias. Length Constraints: Minimum length of 1. Maximum length of 128. Pattern: (?!^[0-9]+$)([a-zA-Z0-9-_]+)

**Type:** string

</details>

## delete_event_source_mapping

Deletes an event source mapping. You can get the identifier of a mapping from the output of ListEventSourceMappings. 

<details><summary>Parameters</summary>

#### uUID (required)

The identifier of the event source mapping.

**Type:** string

</details>

## delete_function

Deletes a Lambda function. To delete a specific function version, use the Qualifier parameter. Otherwise, all versions and aliases are deleted. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

</details>

## delete_statement_from_policy

Removes a statement from the permissions policy for a version of an AWS Lambda layer. For more information, see AddLayerVersionPermission. 

<details><summary>Parameters</summary>

#### layerName (required)

The name or Amazon Resource Name (ARN) of the layer. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+

**Type:** string

#### statementId (required)

The identifier that was specified when the statement was added. Length Constraints: Minimum length of 1. Maximum length of 100. Pattern: ([a-zA-Z0-9-_]+)

**Type:** string

#### versionNumber (required)

The version number.

**Type:** string

</details>

## delete_tags

Removes tags from a function. 

<details><summary>Parameters</summary>

#### resource (required)

The function's Amazon Resource Name (ARN). Pattern: arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

</details>

## delete_version_of_layer

Deletes a version of an AWS Lambda layer. Deleted versions can no longer be viewed or added to functions. To avoid breaking functions, a copy of the version remains in Lambda until no functions refer to it. 

<details><summary>Parameters</summary>

#### layerName (required)

The name or Amazon Resource Name (ARN) of the layer. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+

**Type:** string

#### versionNumber (required)

The version number.

**Type:** string

</details>

## get_account_settings



*This operation has no parameters*

## get_alias_details

Returns details about a Lambda function alias. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### name (required)

The name of the alias. Length Constraints: Minimum length of 1. Maximum length of 128. Pattern: (?!^[0-9]+$)([a-zA-Z0-9-_]+)

**Type:** string

</details>

## get_event_source_mapping

Returns details about an event source mapping. You can get the identifier of a mapping from the output of ListEventSourceMappings. 

<details><summary>Parameters</summary>

#### uUID (required)

The identifier of the event source mapping.

**Type:** string

</details>

## get_function

Returns information about function or function version, with a link to download the deployment package that's valid for 10 minutes. If you specify a function version, only details specific to that version are returned. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

</details>

## get_policy_for_function

Returns the resource-based IAM policy for a function, version, or alias. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

</details>

## get_policy_for_version_of_layer

Returns the permission policy for a version of an AWS Lambda layer. For more information, see AddLayerVersionPermission. 

<details><summary>Parameters</summary>

#### layerName (required)

The name or Amazon Resource Name (ARN) of the layer. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+

**Type:** string

#### versionNumber (required)

The version number.

**Type:** string

</details>

## get_settings_for_function

Returns a the version-specific settings of a Lambda function or version. The output includes only options that can vary between versions of a function. To modify these settings, use UpdateFunctionConfiguration. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

</details>

## get_tags_for_function

Returns a function's tags. You can also view tags with GetFunction. 

<details><summary>Parameters</summary>

#### resource (required)

The function's Amazon Resource Name (ARN). Pattern: arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_]+(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

</details>

## get_version_of_layer

Returns information about a version of an AWS Lambda layer, with a link to download the layer archive that's valid for 10 minutes. 

<details><summary>Parameters</summary>

#### layerName (required)

The name or Amazon Resource Name (ARN) of the layer. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+

**Type:** string

#### versionNumber (required)

The version number.

**Type:** string

</details>

## invoke_function

Invokes a Lambda function. You can invoke a function synchronously and wait for the response, or asynchronously. To invoke a function asynchronously, set InvocationType to Event. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### $body

**Type:** object

#### X-Amz-Client-Context

Up to 3583 bytes of base64-encoded data about the invoking client to pass to the function in the context object.

**Type:** string

#### X-Amz-Invocation-Type

Choose from the following options.
RequestResponse (default) - Invoke the function synchronously. Keep the connection open until
the function returns a response or times out. The API response includes the function
response and additional
data.
Event - Invoke the function asynchronously. Send events that fail multiple times to the
function's dead-letter queue (if configured). The API response only includes a status
code.
DryRun - Validate parameter values and verify that the user or role has permission to invoke
the function.

**Type:** string

**Potential values:** RequestResponse, Event, DryRun

#### X-Amz-Log-Type

Set to Tail to include the execution log in the response.
Valid Values: None | Tail

**Type:** string

**Potential values:** None, Tail

</details>

## list_aliases_for_function

Returns a list of aliases for a Lambda function. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

</details>

## list_event_source_mappings

Lists event source mappings. Specify an EventSourceArn to only show event source mappings for a single event source. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

</details>

## list_functions

Returns a list of Lambda functions, with the version-specific configuration of each.

<details><summary>Parameters</summary>

#### FunctionVersion

Specify a function version to only list aliases that invoke that version. Length Constraints: Minimum length of 1. Maximum length of 1024. Pattern: (\$LATEST|[0-9]+)

**Type:** string

#### Marker

Specify the pagination token returned by a previous request to retrieve the next page of results.

**Type:** string

#### MasterRegion

For Lambda@Edge functions, the region of the master function. For example, us-east-2 or ALL. If specified, you must set FunctionVersion to ALL. Pattern: ALL|[a-z]{2}(-gov)?-[a-z]+-\d{1}

**Type:** string

#### MaxItems

The maximum number of event source mappings to return. Valid Range: Minimum value of 1. Maximum value of 10000.

**Type:** string

</details>

## list_layers

Lists AWS Lambda layers and shows information about the latest version of each. Specify a runtime identifier to list only layers that indicate that they're compatible with that runtime. 

*This operation has no parameters*

## list_versions_of_function

Returns a list of versions, with the version-specific configuration of each. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

</details>

## list_versions_of_layer

Lists the versions of an AWS Lambda layer. Versions that have been deleted aren't listed. Specify a runtime identifier to list only versions that indicate that they're compatible with that runtime. 

<details><summary>Parameters</summary>

#### layerName (required)

The name or Amazon Resource Name (ARN) of the layer. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+

**Type:** string

</details>

## map_event_source_to_function



*This operation has no parameters*

## remove_concurrent_limit

Removes a concurrent execution limit from a function.

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

</details>

## revoke_permission_for_function

Revokes function use permission from an AWS service or another account. You can get the ID of the statement from the output of GetPolicy. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### statementId (required)

The identifier that was specified when the statement was added. Length Constraints: Minimum length of 1. Maximum length of 100. Pattern: ([a-zA-Z0-9-_]+)

**Type:** string

</details>

## set_concurrent_limit

Sets the maximum number of simultaneous executions for a function, and reserves capacity for that concurrency level. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### $body

**Type:** object

</details>

## update_alias_for_function

Updates the configuration of a Lambda function alias. 

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### name (required)

The name of the alias. Length Constraints: Minimum length of 1. Maximum length of 128. Pattern: (?!^[0-9]+$)([a-zA-Z0-9-_]+)

**Type:** string

#### $body

**Type:** object

</details>

## update_code_for_function

Updates a Lambda function's code.

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### $body

**Type:** object

</details>

## update_event_source_mapping

Updates an event source mapping. You can change the function that AWS Lambda invokes, or pause invocation and resume later from the same location. 

<details><summary>Parameters</summary>

#### uUID (required)

The identifier of the event source mapping.

**Type:** string

#### $body

**Type:** object

</details>

## update_version_settings_for_function

Modify the version-specifc settings of a Lambda function.

<details><summary>Parameters</summary>

#### functionName (required)

The name of the Lambda function or version. Name formats Function name - my-function (name-only), my-function:1 (with version). Function ARN - arn:aws:lambda:us-west-2:123456789012:function:my-function. Partial ARN - 123456789012:function:my-function. You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length. Length Constraints: Minimum length of 1. Maximum length of 140. Pattern: (arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?

**Type:** string

#### $body

**Type:** object

</details>

