---
id: aws-lambda-documentation
title: AWS Lambda (version v3.*.*)
sidebar_label: AWS Lambda
layout: docs.mustache
---

## add_permission

Adds a permission to the resource policy associated with the specified AWS Lambda function. You use resource policies to grant permissions to event sources that use the push model. In a push model, event sources (such as Amazon S3 and custom applications) invoke your Lambda function. Each permission you add to the resource policy allows an event source permission to invoke the Lambda function.  
Permissions apply to the Amazon Resource Name (ARN) used to invoke the function, which can be unqualified (the unpublished version of the function), or include a version or alias. If a client uses a version or alias to invoke a function, use the Qualifier parameter to apply permissions to that ARN. For more information about versioning, see AWS Lambda Function Versioning and Aliases.  
This operation requires permission for the lambda:AddPermission action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### $body

**Type:** object

```json
{
  "Action" : "The AWS Lambda action you want to allow in this statement. Each Lambda action is a string starting with lambda: followed by the API name . For example, lambda:CreateFunction. You can use wildcard (lambda:*) to grant permission for all AWS Lambda actions. ",
  "SourceArn" : "The Amazon Resource Name of the invoker.   \nIf you add a permission to a service principal without providing the source ARN, any AWS account that creates a mapping to your function ARN can invoke your Lambda function.",
  "EventSourceToken" : "A unique token that must be supplied by the principal invoking the function. This is currently only used for Alexa Smart Home functions.",
  "StatementId" : "A unique statement identifier.",
  "SourceAccount" : "This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner. For example, if the SourceArn identifies a bucket, then this is the bucket owner's account ID. You can use this additional condition to ensure the bucket you specify is owned by a specific account (it is possible the bucket owner deleted the bucket and some other AWS account created the bucket). You can also use this condition to specify all sources (that is, you don't specify the SourceArn) owned by a specific account. ",
  "Principal" : "The principal who is getting this permission. The principal can be an AWS service (e.g. s3.amazonaws.com or sns.amazonaws.com) for service triggers, or an account ID for cross-account access. If you specify a service as a principal, use the SourceArn parameter to limit who can invoke the function through that service.",
  "RevisionId" : "An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias RevisionID using either GetFunction or GetAlias "
}
```

### Qualifier

Specify a version or alias to add permissions to a published version of the function.

**Type:** string

</details>

## create_alias

Creates an alias that points to the specified Lambda function version. For more information, see Introduction to AWS Lambda Aliases. 
Alias names are unique for a given function. This requires permission for the lambda:CreateAlias action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### $body

**Type:** object

```json
{
  "Description" : "Description of the alias.",
  "FunctionVersion" : "Lambda function version for which you are creating the alias.",
  "RoutingConfig" : {
    "AdditionalVersionWeights" : "The name of the second alias, and the percentage of traffic that is routed to it."
  },
  "Name" : "Name for the alias you are creating."
}
```

</details>

## create_event_source_mapping

Identifies a poll-based event source for a Lambda function. It can be either an Amazon Kinesis or DynamoDB stream. AWS Lambda invokes the specified function when records are posted to the event source. 
This association between a poll-based source and a Lambda function is called the event source mapping. 
You provide mapping information (for example, which stream or SQS queue to read from and which Lambda function to invoke) in the request body. 
Amazon Kinesis or DynamoDB stream event sources can be associated with multiple AWS Lambda functions and a given Lambda function can be associated with multiple AWS event sources. For Amazon SQS, you can configure multiple queues as event sources for a single Lambda function, but an SQS queue can be mapped only to a single Lambda function. 
You can configure an SQS queue in an account separate from your Lambda function's account. Also the queue needs to reside in the same AWS region as your function.  
If you are using versioning, you can specify a specific function version or an alias via the function name parameter. For more information about versioning, see AWS Lambda Function Versioning and Aliases.  
This operation requires permission for the lambda:CreateEventSourceMapping action.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "StartingPosition" : "The position in the DynamoDB or Kinesis stream where AWS Lambda should start reading. For more information, see GetShardIterator in the Amazon Kinesis API Reference Guide or GetShardIterator in the Amazon DynamoDB API Reference Guide. The AT_TIMESTAMP value is supported only for Kinesis streams. ",
  "FunctionName" : "The name of the lambda function. \n Name formats   \n  Function name - MyFunction.  \n  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  \n  Version or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD.  \n  Partial ARN - 123456789012:function:MyFunction.   \nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.",
  "BatchSize" : "The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records. The default for Amazon Kinesis and Amazon DynamoDB is 100 records. Both the default and maximum for Amazon SQS are 10 messages.",
  "StartingPositionTimestamp" : "The timestamp of the data record from which to start reading. Used with shard iterator type AT_TIMESTAMP. If a record with this exact timestamp does not exist, the iterator returned is for the next (later) record. If the timestamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON). Valid only for Kinesis streams. ",
  "Enabled" : "Set to false to disable the event source upon creation. ",
  "EventSourceArn" : "The Amazon Resource Name (ARN) of the event source."
}
```

</details>

## create_function

Creates a new Lambda function. The function configuration is created from the request parameters, and the code for the function is provided by a .zip file. The function name is case-sensitive. 
This operation requires permission for the lambda:CreateFunction action.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "MemorySize" : "The amount of memory that your function has access to. Increasing the function's memory also increases it's CPU allocation. The default value is 128 MB. The value must be a multiple of 64 MB.",
  "KMSKeyArn" : "The ARN of the KMS key used to encrypt your function's environment variables. If not provided, AWS Lambda will use a default service key.",
  "Description" : "A description of the function.",
  "VpcConfig" : {
    "SubnetIds" : [ "string" ],
    "SecurityGroupIds" : [ "string" ]
  },
  "TracingConfig" : {
    "Mode" : "The tracing mode."
  },
  "Timeout" : "The amount of time that Lambda allows a function to run before terminating it. The default is 3 seconds. The maximum allowed value is 900 seconds.",
  "DeadLetterConfig" : {
    "TargetArn" : "The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic."
  },
  "Handler" : "The name of the method within your code that Lambda calls to execute your function. For more information, see Programming Model.",
  "Code" : {
    "S3ObjectVersion" : "For versioned objects, the version of the deployment package object to use.",
    "ZipFile" : "The base64-encoded contents of your zip file containing your deployment package. AWS SDK and AWS CLI clients handle the encoding for you.",
    "S3Bucket" : "An Amazon S3 bucket in the same region as your function.",
    "S3Key" : "The Amazon S3 key of the deployment package."
  },
  "Role" : "The Amazon Resource Name (ARN) of the function's execution role.",
  "FunctionName" : "The name of the lambda function. \n Name formats   \n  Function name - MyFunction.  \n  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  \n  Partial ARN - 123456789012:function:MyFunction.   \nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.",
  "Runtime" : "The runtime version for the function.",
  "Environment" : {
    "Variables" : "Environment variable key-value pairs."
  },
  "Publish" : "Set to true to publish the first version of the function during creation.",
  "Tags" : "The list of tags (key-value pairs) assigned to the new function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide."
}
```

</details>

## delete_alias

Deletes the specified Lambda function alias. For more information, see Introduction to AWS Lambda Aliases. 
This requires permission for the lambda:DeleteAlias action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### Name (required)

Name of the alias to delete.

**Type:** string

</details>

## delete_event_source_mapping

Removes an event source mapping. This means AWS Lambda will no longer invoke the function for events in the associated source. 
This operation requires permission for the lambda:DeleteEventSourceMapping action.

<details><summary>Parameters</summary>

### UUID (required)

The event source mapping ID.

**Type:** string

</details>

## delete_function

Deletes a Lambda function. To delete a specific function version, use the Qualifier parameter. Otherwise, all versions and aliases are deleted. Event source mappings are not deleted. 
This operation requires permission for the lambda:DeleteFunction action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### Qualifier

Specify a version to delete. You cannot delete a version that is referenced by an alias.

**Type:** string

</details>

## delete_function_concurrency

Removes concurrent execution limits from this function. For more information, see Managing Concurrency.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

</details>

## get_account_settings

Retrieves details about your account's limits and usage in a region.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## get_alias

Returns the specified alias information such as the alias ARN, description, and function version it is pointing to. For more information, see Introduction to AWS Lambda Aliases. 
This requires permission for the lambda:GetAlias action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### Name (required)

Name of the alias for which you want to retrieve information.

**Type:** string

</details>

## get_event_source_mapping

Returns configuration information for the specified event source mapping (see CreateEventSourceMapping). 
This operation requires permission for the lambda:GetEventSourceMapping action.

<details><summary>Parameters</summary>

### UUID (required)

The AWS Lambda assigned ID of the event source mapping.

**Type:** string

</details>

## get_function

Returns the configuration information of the Lambda function and a presigned URL link to the .zip file you uploaded with CreateFunction so you can download the .zip file. Note that the URL is valid for up to 10 minutes. The configuration information is the same information you provided as parameters when uploading the function. 
Use the Qualifier parameter to retrieve a published version of the function. Otherwise, returns the unpublished version ($LATEST). For more information, see AWS Lambda Function Versioning and Aliases. 
This operation requires permission for the lambda:GetFunction action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### Qualifier

Specify a version or alias to get details about a published version of the function.

**Type:** string

</details>

## get_function_configuration

Returns the configuration information of the Lambda function. This the same information you provided as parameters when uploading the function by using CreateFunction. 
If you are using the versioning feature, you can retrieve this information for a specific function version by using the optional Qualifier parameter and specifying the function version or alias that points to it. If you don't provide it, the API returns information about the $LATEST version of the function. For more information about versioning, see AWS Lambda Function Versioning and Aliases. 
This operation requires permission for the lambda:GetFunctionConfiguration operation.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### Qualifier

Specify a version or alias to get details about a published version of the function.

**Type:** string

</details>

## get_policy

Returns the resource policy associated with the specified Lambda function. 
This action requires permission for the lambda:GetPolicy action. 

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### Qualifier

You can specify this optional query parameter to specify a function version or an alias name in which case this API will return all permissions associated with the specific qualified ARN. If you don't provide this parameter, the API will return permissions that apply to the unqualified function ARN.

**Type:** string

</details>

## invoke

Invokes a Lambda function. For an example, see Create the Lambda Function and Test It Manually.  
Specify just a function name to invoke the latest version of the function. To invoke a published version, use the Qualifier parameter to specify a version or alias. 
If you use the RequestResponse (synchronous) invocation option, the function will be invoked only once. If you use the Event (asynchronous) invocation option, the function will be invoked at least once in response to an event and the function must be idempotent to handle this. 
For functions with a long timeout, your client may be disconnected during synchronous invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy, or operating system to allow for long connections with timeout or keep-alive settings. 
This operation requires permission for the lambda:InvokeFunction action. 
The TooManyRequestsException noted below will return the following: ConcurrentInvocationLimitExceeded will be returned if you have no functions with reserved concurrency and have exceeded your account concurrent limit or if a function without reserved concurrency exceeds the account's unreserved concurrency limit. ReservedFunctionConcurrentInvocationLimitExceeded will be returned when a function with reserved concurrency exceeds its configured concurrency limit. 

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### $body

JSON that you want to provide to your Lambda function as input.

**Type:** blob

### Qualifier

Specify a version or alias to invoke a published version of the function.

**Type:** string

### X-Amz-Client-Context

Using the ClientContext you can pass client-specific information to the Lambda function you are invoking. You can then process the client information in your Lambda function as you choose through the context variable. For an example of a ClientContext JSON, see PutEvents in the Amazon Mobile Analytics API Reference and User Guide. 
The ClientContext JSON must be base64-encoded and has a maximum size of 3583 bytes.  
 ClientContext information is returned only if you use the synchronous (RequestResponse) invocation type.

**Type:** string

### X-Amz-Invocation-Type

Choose from the following options.  
  RequestResponse (default) - Invoke the function synchronously. Keep the connection open until the function returns a response or times out.  
  Event - Invoke the function asynchronously. Send events that fail multiple times to the function's dead-letter queue (if configured).  
  DryRun - Validate parameter values and verify that the user or role has permission to invoke the function. 

**Type:** string

**Potential values:** Event, RequestResponse, DryRun

### X-Amz-Log-Type

You can set this optional parameter to Tail in the request only if you specify the InvocationType parameter with value RequestResponse. In this case, AWS Lambda returns the base64-encoded last 4 KB of log data produced by your Lambda function in the x-amz-log-result header. 

**Type:** string

**Potential values:** None, Tail

</details>

## invoke_async

For asynchronous function invocation, use Invoke.  
Submits an invocation request to AWS Lambda. Upon receiving the request, Lambda executes the specified function asynchronously. To see the logs generated by the Lambda function execution, see the CloudWatch Logs console. 
This operation requires permission for the lambda:InvokeFunction action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### $body

JSON that you want to provide to your Lambda function as input.

**Type:** blob

</details>

## list_aliases

Returns list of aliases created for a Lambda function. For each alias, the response includes information such as the alias ARN, description, alias name, and the function version to which it points. For more information, see Introduction to AWS Lambda Aliases. 
This requires permission for the lambda:ListAliases action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### FunctionVersion

If you specify this optional parameter, the API returns only the aliases that are pointing to the specific Lambda function version, otherwise the API returns all of the aliases created for the Lambda function.

**Type:** string

</details>

## list_event_source_mappings

Returns a list of event source mappings you created using the CreateEventSourceMapping (see CreateEventSourceMapping).  
For each mapping, the API returns configuration information. You can optionally specify filters to retrieve specific event source mappings. 
This operation requires permission for the lambda:ListEventSourceMappings action.

<details><summary>Parameters</summary>

### EventSourceArn

The Amazon Resource Name (ARN) of the Amazon Kinesis or DynamoDB stream. (This parameter is optional.)

**Type:** string

### FunctionName

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Version or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

</details>

## list_functions

Returns a list of your Lambda functions. For each function, the response includes the function configuration information. You must use GetFunction to retrieve the code for your function. 
This operation requires permission for the lambda:ListFunctions action. 
If you are using the versioning feature, you can list all of your functions or only $LATEST versions. For information about the versioning feature, see AWS Lambda Function Versioning and Aliases. 

<details><summary>Parameters</summary>

### FunctionVersion

Set to ALL to list all published versions. If not specified, only the latest unpublished version ARN is returned.

**Type:** string

**Potential values:** ALL

### MasterRegion

Specify a region (e.g. us-east-2) to only list functions that were created in that region, or ALL to include functions replicated from any region. If specified, you also must specify the FunctionVersion.

**Type:** string

</details>

## list_tags

Returns a list of tags assigned to a function when supplied the function ARN (Amazon Resource Name). For more information on Tagging, see Tagging Lambda Functions in the AWS Lambda Developer Guide.

<details><summary>Parameters</summary>

### ARN (required)

The ARN (Amazon Resource Name) of the function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide.

**Type:** string

</details>

## list_versions_by_function

Lists all versions of a function. For information about versioning, see AWS Lambda Function Versioning and Aliases. 

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### Marker

 Optional string. An opaque pagination token returned from a previous ListVersionsByFunction operation. If present, indicates where to continue the listing. 

**Type:** string

### MaxItems

Optional integer. Specifies the maximum number of AWS Lambda function versions to return in response. This parameter value must be greater than 0.

**Type:** integer

</details>

## publish_version

Publishes a version of your function from the current snapshot of $LATEST. That is, AWS Lambda takes a snapshot of the function code and configuration information from $LATEST and publishes a new version. The code and configuration cannot be modified after publication. For information about the versioning feature, see AWS Lambda Function Versioning and Aliases. 

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### $body

**Type:** object

```json
{
  "Description" : "The description for the version you are publishing. If not provided, AWS Lambda copies the description from the $LATEST version.",
  "CodeSha256" : "The SHA256 hash of the deployment package you want to publish. This provides validation on the code you are publishing. If you provide this parameter, the value must match the SHA256 of the $LATEST version for the publication to succeed. You can use the DryRun parameter of UpdateFunctionCode to verify the hash value that will be returned before publishing your new version.",
  "RevisionId" : "An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you retrieve the latest function version or alias RevisionID using either GetFunction or GetAlias."
}
```

</details>

## put_function_concurrency

Sets a limit on the number of concurrent executions available to this function. It is a subset of your account's total concurrent execution limit per region. Note that Lambda automatically reserves a buffer of 100 concurrent executions for functions without any reserved concurrency limit. This means if your account limit is 1000, you have a total of 900 available to allocate to individual functions. For more information, see Managing Concurrency.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### $body

**Type:** object

```json
{
  "ReservedConcurrentExecutions" : "The concurrent execution limit reserved for this function."
}
```

</details>

## remove_permission

Removes permissions from a function. You can remove individual permissions from an resource policy associated with a Lambda function by providing a statement ID that you provided when you added the permission. When you remove permissions, disable the event source mapping or trigger configuration first to avoid errors. 
Permissions apply to the Amazon Resource Name (ARN) used to invoke the function, which can be unqualified (the unpublished version of the function), or include a version or alias. If a client uses a version or alias to invoke a function, use the Qualifier parameter to apply permissions to that ARN. For more information about versioning, see AWS Lambda Function Versioning and Aliases.  
You need permission for the lambda:RemovePermission action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### StatementId (required)

Statement ID of the permission to remove.

**Type:** string

### Qualifier

Specify a version or alias to remove permissions from a published version of the function.

**Type:** string

### RevisionId

An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias RevisionID using either GetFunction or GetAlias.

**Type:** string

</details>

## tag_resource

Creates a list of tags (key-value pairs) on the Lambda function. Requires the Lambda function ARN (Amazon Resource Name). If a key is specified without a value, Lambda creates a tag with the specified key and a value of null. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide. 

<details><summary>Parameters</summary>

### ARN (required)

The ARN (Amazon Resource Name) of the Lambda function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide.

**Type:** string

### $body

**Type:** object

```json
{
  "Tags" : "The list of tags (key-value pairs) you are assigning to the Lambda function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide."
}
```

</details>

## untag_resource

Removes tags from a Lambda function. Requires the function ARN (Amazon Resource Name). For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide. 

<details><summary>Parameters</summary>

### ARN (required)

The ARN (Amazon Resource Name) of the function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide.

**Type:** string

### tagKeys (required)

The list of tag keys to be deleted from the function. For more information, see Tagging Lambda Functions in the AWS Lambda Developer Guide.

**Type:** array

```json
[ "string" ]
```

</details>

## update_alias

Using this API you can update the function version to which the alias points and the alias description. For more information, see Introduction to AWS Lambda Aliases. 
This requires permission for the lambda:UpdateAlias action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### Name (required)

The alias name.

**Type:** string

### $body

**Type:** object

```json
{
  "Description" : "You can change the description of the alias using this parameter.",
  "FunctionVersion" : "Using this parameter you can change the Lambda function version to which the alias points.",
  "RoutingConfig" : {
    "AdditionalVersionWeights" : "The name of the second alias, and the percentage of traffic that is routed to it."
  },
  "RevisionId" : "An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you retrieve the latest function version or alias RevisionID using either GetFunction or GetAlias."
}
```

</details>

## update_event_source_mapping

You can update an event source mapping. This is useful if you want to change the parameters of the existing mapping without losing your position in the stream. You can change which function will receive the stream records, but to change the stream itself, you must create a new mapping. 
If you disable the event source mapping, AWS Lambda stops polling. If you enable again, it will resume polling from the time it had stopped polling, so you don't lose processing of any records. However, if you delete event source mapping and create it again, it will reset. 
This operation requires permission for the lambda:UpdateEventSourceMapping action.

<details><summary>Parameters</summary>

### UUID (required)

The event source mapping identifier.

**Type:** string

### $body

**Type:** object

```json
{
  "FunctionName" : "The name of the lambda function. \n Name formats   \n  Function name - MyFunction.  \n  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  \n  Version or Alias ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD.  \n  Partial ARN - 123456789012:function:MyFunction.   \nThe length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.",
  "BatchSize" : "The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function. Your function receives an event with all the retrieved records.",
  "Enabled" : "Specifies whether AWS Lambda should actively poll the stream or not. If disabled, AWS Lambda will not poll the stream."
}
```

</details>

## update_function_code

Updates the code for the specified Lambda function. This operation must only be used on an existing Lambda function and cannot be used to update the function configuration. 
If you are using the versioning feature, note this API will always update the $LATEST version of your Lambda function. For information about the versioning feature, see AWS Lambda Function Versioning and Aliases.  
This operation requires permission for the lambda:UpdateFunctionCode action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### $body

**Type:** object

```json
{
  "S3ObjectVersion" : "The Amazon S3 object (the deployment package) version you want to upload.",
  "ZipFile" : "The contents of your zip file containing your deployment package. If you are using the web API directly, the contents of the zip file must be base64-encoded. If you are using the AWS SDKs or the AWS CLI, the SDKs or CLI will do the encoding for you. For more information about creating a .zip file, see Execution Permissions. ",
  "S3Bucket" : "Amazon S3 bucket name where the .zip file containing your deployment package is stored. This bucket must reside in the same AWS Region where you are creating the Lambda function.",
  "S3Key" : "The Amazon S3 object (the deployment package) key name you want to upload.",
  "DryRun" : "This boolean parameter can be used to test your request to AWS Lambda to update the Lambda function and publish a version as an atomic operation. It will do all necessary computation and validation of your code but will not upload it or a publish a version. Each time this operation is invoked, the CodeSha256 hash value of the provided code will also be computed and returned in the response.",
  "Publish" : "This boolean parameter can be used to request AWS Lambda to update the Lambda function and publish a version as an atomic operation.",
  "RevisionId" : "An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias RevisionID using either using using either GetFunction or GetAlias."
}
```

</details>

## update_function_configuration

Updates the configuration parameters for the specified Lambda function by using the values provided in the request. You provide only the parameters you want to change. This operation must only be used on an existing Lambda function and cannot be used to update the function's code. 
If you are using the versioning feature, note this API will always update the $LATEST version of your Lambda function. For information about the versioning feature, see AWS Lambda Function Versioning and Aliases.  
This operation requires permission for the lambda:UpdateFunctionConfiguration action.

<details><summary>Parameters</summary>

### FunctionName (required)

The name of the lambda function. 
 Name formats   
  Function name - MyFunction.  
  Function ARN - arn:aws:lambda:us-west-2:123456789012:function:MyFunction.  
  Partial ARN - 123456789012:function:MyFunction.   
The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.

**Type:** string

### $body

**Type:** object

```json
{
  "Role" : "The Amazon Resource Name (ARN) of the IAM role that Lambda will assume when it executes your function.",
  "MemorySize" : "The amount of memory, in MB, your Lambda function is given. AWS Lambda uses this memory size to infer the amount of CPU allocated to your function. Your function use-case determines your CPU and memory requirements. For example, a database operation might need less memory compared to an image processing function. The default value is 128 MB. The value must be a multiple of 64 MB.",
  "KMSKeyArn" : "The Amazon Resource Name (ARN) of the KMS key used to encrypt your function's environment variables. If you elect to use the AWS Lambda default service key, pass in an empty string (\"\") for this parameter.",
  "Runtime" : "The runtime version for the function.",
  "Description" : "A short user-defined function description. AWS Lambda does not use this value. Assign a meaningful description as you see fit.",
  "VpcConfig" : {
    "SubnetIds" : [ "string" ],
    "SecurityGroupIds" : [ "string" ]
  },
  "TracingConfig" : {
    "Mode" : "The tracing mode."
  },
  "Timeout" : "The amount of time that Lambda allows a function to run before terminating it. The default is 3 seconds. The maximum allowed value is 900 seconds.",
  "DeadLetterConfig" : {
    "TargetArn" : "The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic."
  },
  "Handler" : "The function that Lambda calls to begin executing your function. For Node.js, it is the module-name.export value in your function. ",
  "Environment" : {
    "Variables" : "Environment variable key-value pairs."
  },
  "RevisionId" : "An optional value you can use to ensure you are updating the latest update of the function version or alias. If the RevisionID you pass doesn't match the latest RevisionId of the function or alias, it will fail with an error message, advising you to retrieve the latest function version or alias RevisionID using either GetFunction or GetAlias."
}
```

</details>

