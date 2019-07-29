---
id: aws-cloudwatch-logs-documentation
title: AWS Cloudwatch Logs (version v3.*.*)
sidebar_label: AWS Cloudwatch Logs
layout: docs.mustache
---

## associate_kms_key

Associates the specified AWS Key Management Service (AWS KMS) customer master key (CMK) with the specified log group. 
Associating an AWS KMS CMK with a log group overrides any existing associations between the log group and a CMK. After a CMK is associated with a log group, all newly ingested data for the log group is encrypted using the CMK. This association is stored as long as the data encrypted with the CMK is still within Amazon CloudWatch Logs. This enables Amazon CloudWatch Logs to decrypt this data whenever it is requested. 
Note that it can take up to 5 minutes for this operation to take effect. 
If you attempt to associate a CMK with a log group but the CMK does not exist or the CMK is disabled, you will receive an InvalidParameterException error. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "kmsKeyId" : "The Amazon Resource Name (ARN) of the CMK to use when encrypting log data. For more information, see Amazon Resource Names - AWS Key Management Service (AWS KMS)."
}
```

</details>

## cancel_export_task

Cancels the specified export task. 
The task must be in the PENDING or RUNNING state.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "taskId" : "The ID of the export task."
}
```

</details>

## create_export_task

Creates an export task, which allows you to efficiently export data from a log group to an Amazon S3 bucket. 
This is an asynchronous call. If all the required information is provided, this operation initiates an export task and responds with the ID of the task. After the task has started, you can use DescribeExportTasks to get the status of the export task. Each account can only have one active (RUNNING or PENDING) export task at a time. To cancel an export task, use CancelExportTask. 
You can export logs from multiple log groups or multiple time ranges to the same S3 bucket. To separate out log data for each export task, you can specify a prefix to be used as the Amazon S3 key prefix for all exported objects.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "destinationPrefix" : "The prefix used as the start of the key for every object exported. If you don't specify a value, the default is exportedlogs.",
  "logStreamNamePrefix" : "Export only log streams that match the provided prefix. If you don't specify a value, no prefix filter is applied.",
  "destination" : "The name of S3 bucket for the exported log data. The bucket must be in the same AWS region.",
  "taskName" : "The name of the export task.",
  "from" : "The start time of the range for the request, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp earlier than this time are not exported.",
  "to" : "The end time of the range for the request, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp later than this time are not exported."
}
```

</details>

## create_log_group

Creates a log group with the specified name. 
You can create up to 5000 log groups per account. 
You must use the following guidelines when naming a log group:  
 Log group names must be unique within a region for an AWS account.  
 Log group names can be between 1 and 512 characters long.  
 Log group names consist of the following characters: a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).   
If you associate a AWS Key Management Service (AWS KMS) customer master key (CMK) with the log group, ingested data is encrypted using the CMK. This association is stored as long as the data encrypted with the CMK is still within Amazon CloudWatch Logs. This enables Amazon CloudWatch Logs to decrypt this data whenever it is requested. 
If you attempt to associate a CMK with the log group but the CMK does not exist or the CMK is disabled, you will receive an InvalidParameterException error. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "kmsKeyId" : "The Amazon Resource Name (ARN) of the CMK to use when encrypting log data. For more information, see Amazon Resource Names - AWS Key Management Service (AWS KMS).",
  "tags" : "The key-value pairs to use for the tags."
}
```

</details>

## create_log_stream

Creates a log stream for the specified log group. 
There is no limit on the number of log streams that you can create for a log group. 
You must use the following guidelines when naming a log stream:  
 Log stream names must be unique within the log group.  
 Log stream names can be between 1 and 512 characters long.  
 The ':' (colon) and '*' (asterisk) characters are not allowed. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "logStreamName" : "The name of the log stream."
}
```

</details>

## delete_destination

Deletes the specified destination, and eventually disables all the subscription filters that publish to it. This operation does not delete the physical resource encapsulated by the destination.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "destinationName" : "The name of the destination."
}
```

</details>

## delete_log_group

Deletes the specified log group and permanently deletes all the archived log events associated with the log group.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group."
}
```

</details>

## delete_log_stream

Deletes the specified log stream and permanently deletes all the archived log events associated with the log stream.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "logStreamName" : "The name of the log stream."
}
```

</details>

## delete_metric_filter

Deletes the specified metric filter.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "filterName" : "The name of the metric filter."
}
```

</details>

## delete_resource_policy

Deletes a resource policy from this account. This revokes the access of the identities in that policy to put log events to this account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "policyName" : "The name of the policy to be revoked. This parameter is required."
}
```

</details>

## delete_retention_policy

Deletes the specified retention policy. 
Log events do not expire if they belong to log groups without a retention policy.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group."
}
```

</details>

## delete_subscription_filter

Deletes the specified subscription filter.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "filterName" : "The name of the subscription filter."
}
```

</details>

## describe_destinations

Lists all your destinations. The results are ASCII-sorted by destination name.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DestinationNamePrefix" : "The prefix to match. If you don't specify a value, no prefix filter is applied."
}
```

</details>

## describe_export_tasks

Lists the specified export tasks. You can list all your export tasks or filter the results based on task ID or task status.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "nextToken" : "The token for the next set of items to return. (You received this token from a previous call.)",
  "limit" : "The maximum number of items returned. If you don't specify a value, the default is up to 50 items.",
  "taskId" : "The ID of the export task. Specifying a task ID filters the results to zero or one export tasks.",
  "statusCode" : "The status code of the export task. Specifying a status code filters the results to zero or more export tasks."
}
```

</details>

## describe_log_groups

Lists the specified log groups. You can list all your log groups or filter the results by prefix. The results are ASCII-sorted by log group name.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupNamePrefix" : "The prefix to match."
}
```

</details>

## describe_log_streams

Lists the log streams for the specified log group. You can list all the log streams or filter the results by prefix. You can also control how the results are ordered. 
This operation has a limit of five transactions per second, after which transactions are throttled.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "logStreamNamePrefix" : "The prefix to match. \nIf orderBy is LastEventTime,you cannot specify this parameter.",
  "orderBy" : "If the value is LogStreamName, the results are ordered by log stream name. If the value is LastEventTime, the results are ordered by the event time. The default value is LogStreamName. \nIf you order the results by event time, you cannot specify the logStreamNamePrefix parameter. \nlastEventTimestamp represents the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. lastEventTimeStamp updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but may take longer in some rare situations.",
  "descending" : "If the value is true, results are returned in descending order. If the value is to false, results are returned in ascending order. The default value is false."
}
```

</details>

## describe_metric_filters

Lists the specified metric filters. You can list all the metric filters or filter the results by log name, prefix, metric name, or metric namespace. The results are ASCII-sorted by filter name.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "metricName" : "Filters results to include only those with the specified metric name. If you include this parameter in your request, you must also include the metricNamespace parameter.",
  "logGroupName" : "The name of the log group.",
  "metricNamespace" : "Filters results to include only those in the specified namespace. If you include this parameter in your request, you must also include the metricName parameter.",
  "filterNamePrefix" : "The prefix to match."
}
```

</details>

## describe_resource_policies

Lists the resource policies in this account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "nextToken" : "string",
  "limit" : "The maximum number of resource policies to be displayed with one call of this API."
}
```

</details>

## describe_subscription_filters

Lists the subscription filters for the specified log group. You can list all the subscription filters or filter the results by prefix. The results are ASCII-sorted by filter name.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "filterNamePrefix" : "The prefix to match. If you don't specify a value, no prefix filter is applied."
}
```

</details>

## disassociate_kms_key

Disassociates the associated AWS Key Management Service (AWS KMS) customer master key (CMK) from the specified log group. 
After the AWS KMS CMK is disassociated from the log group, AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires permissions for the CMK whenever the encrypted data is requested. 
Note that it can take up to 5 minutes for this operation to take effect.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group."
}
```

</details>

## filter_log_events

Lists log events from the specified log group. You can list all the log events or filter the results using a filter pattern, a time range, and the name of the log stream. 
By default, this operation returns as many log events as can fit in 1 MB (up to 10,000 log events), or all the events found within the time range that you specify. If the results include a token, then there are more log events available, and you can get additional results by specifying the token in a subsequent call.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "filterPattern" : "The filter pattern to use. For more information, see Filter and Pattern Syntax. \nIf not provided, all the events are matched.",
  "logGroupName" : "The name of the log group to search.",
  "logStreamNamePrefix" : "Filters the results to include only events from log streams that have names starting with this prefix. \nIf you specify a value for both logStreamNamePrefix and logStreamNames, but the value for logStreamNamePrefix does not match any log stream names specified in logStreamNames, the action returns an InvalidParameterException error.",
  "logStreamNames" : [ "string" ],
  "startTime" : "The start of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp before this time are not returned.",
  "interleaved" : "If the value is true, the operation makes a best effort to provide responses that contain events from multiple log streams within the log group, interleaved in a single response. If the value is false, all the matched log events in the first log stream are searched first, then those in the next log stream, and so on. The default is false.",
  "endTime" : "The end of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp later than this time are not returned."
}
```

</details>

## get_log_events

Lists log events from the specified log stream. You can list all the log events or filter using a time range. 
By default, this operation returns as many log events as can fit in a response size of 1MB (up to 10,000 log events). You can get additional log events by specifying one of the tokens in a subsequent call.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "startFromHead" : "If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. The default value is false.",
  "logGroupName" : "The name of the log group.",
  "logStreamName" : "The name of the log stream.",
  "nextToken" : "The token for the next set of items to return. (You received this token from a previous call.)",
  "limit" : "The maximum number of log events returned. If you don't specify a value, the maximum is as many log events as can fit in a response size of 1 MB, up to 10,000 log events.",
  "startTime" : "The start of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp equal to this time or later than this time are included. Events with a time stamp earlier than this time are not included.",
  "endTime" : "The end of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a time stamp equal to or later than this time are not included."
}
```

</details>

## list_tags_log_group

Lists the tags for the specified log group.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group."
}
```

</details>

## put_destination

Creates or updates a destination. A destination encapsulates a physical resource (such as an Amazon Kinesis stream) and enables you to subscribe to a real-time stream of log events for a different account, ingested using PutLogEvents. Currently, the only supported physical resource is a Kinesis stream belonging to the same account as the destination. 
Through an access policy, a destination controls what is written to its Kinesis stream. By default, PutDestination does not set any access policy with the destination, which means a cross-account user cannot call PutSubscriptionFilter against this destination. To enable this, the destination owner must call PutDestinationPolicy after PutDestination.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "roleArn" : "The ARN of an IAM role that grants CloudWatch Logs permissions to call the Amazon Kinesis PutRecord operation on the destination stream.",
  "destinationName" : "A name for the destination.",
  "targetArn" : "The ARN of an Amazon Kinesis stream to which to deliver matching log events."
}
```

</details>

## put_destination_policy

Creates or updates an access policy associated with an existing destination. An access policy is an IAM policy document that is used to authorize claims to register a subscription filter against a given destination.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "destinationName" : "A name for an existing destination.",
  "accessPolicy" : "An IAM policy document that authorizes cross-account users to deliver their log events to the associated destination."
}
```

</details>

## put_log_events

Uploads a batch of log events to the specified log stream. 
You must include the sequence token obtained from the response of the previous call. An upload in a newly created log stream does not require a sequence token. You can also get the sequence token using DescribeLogStreams. If you call PutLogEvents twice within a narrow time period using the same value for sequenceToken, both calls may be successful, or one may be rejected. 
The batch of events must satisfy the following constraints:  
 The maximum batch size is 1,048,576 bytes, and this size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.  
 None of the log events in the batch can be more than 2 hours in the future.  
 None of the log events in the batch can be older than 14 days or the retention period of the log group.  
 The log events in the batch must be in chronological ordered by their time stamp. The time stamp is the time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. (In AWS Tools for PowerShell and the AWS SDK for .NET, the timestamp is specified in .NET format: yyyy-mm-ddThh:mm:ss. For example, 2017-09-15T13:45:30.)   
 The maximum number of log events in a batch is 10,000.  
 A batch of log events in a single request cannot span more than 24 hours. Otherwise, the operation fails.   
If a call to PutLogEvents returns "UnrecognizedClientException" the most likely cause is an invalid AWS access key ID or secret key. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logEvents" : [ {
    "message" : "The raw event message.",
    "timestamp" : "The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC."
  } ],
  "logGroupName" : "The name of the log group.",
  "sequenceToken" : "The sequence token obtained from the response of the previous PutLogEvents call. An upload in a newly created log stream does not require a sequence token. You can also get the sequence token using DescribeLogStreams. If you call PutLogEvents twice within a narrow time period using the same value for sequenceToken, both calls may be successful, or one may be rejected.",
  "logStreamName" : "The name of the log stream."
}
```

</details>

## put_metric_filter

Creates or updates a metric filter and associates it with the specified log group. Metric filters allow you to configure rules to extract metric data from log events ingested through PutLogEvents. 
The maximum number of metric filters that can be associated with a log group is 100.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "filterPattern" : "A filter pattern for extracting metric data out of ingested log events.",
  "metricTransformations" : [ {
    "metricName" : "The name of the CloudWatch metric.",
    "defaultValue" : "(Optional) The value to emit when a filter pattern does not match a log event. This value can be null.",
    "metricValue" : "The value to publish to the CloudWatch metric when a filter pattern matches a log event.",
    "metricNamespace" : "The namespace of the CloudWatch metric."
  } ],
  "logGroupName" : "The name of the log group.",
  "filterName" : "A name for the metric filter."
}
```

</details>

## put_resource_policy

Creates or updates a resource policy allowing other AWS services to put log events to this account, such as Amazon Route 53. An account can have up to 10 resource policies per region.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "policyDocument" : "Details of the new policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. \nThe following example creates a resource policy enabling the Route 53 service to put DNS query logs in to the specified log group. Replace \"logArn\" with the ARN of your CloudWatch Logs resource, such as a log group or log stream. \n { \"Version\": \"2012-10-17\", \"Statement\": [ { \"Sid\": \"Route53LogsToCloudWatchLogs\", \"Effect\": \"Allow\", \"Principal\": { \"Service\": [ \"route53.amazonaws.com\" ] }, \"Action\":\"logs:PutLogEvents\", \"Resource\": \"logArn\" } ] }  ",
  "policyName" : "Name of the new policy. This parameter is required."
}
```

</details>

## put_retention_policy

Sets the retention of the specified log group. A retention policy allows you to configure the number of days for which to retain log events in the specified log group.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "retentionInDays" : "Required integer",
  "logGroupName" : "The name of the log group."
}
```

</details>

## put_subscription_filter

Creates or updates a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events ingested through PutLogEvents and have them delivered to a specific destination. Currently, the supported destinations are:  
 An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.  
 A logical destination that belongs to a different account, for cross-account delivery.  
 An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.  
 An AWS Lambda function that belongs to the same account as the subscription filter, for same-account delivery.   
There can only be one subscription filter associated with a log group. If you are updating an existing filter, you must specify the correct name in filterName. Otherwise, the call fails because you cannot associate a second filter with a log group.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "filterPattern" : "A filter pattern for subscribing to a filtered stream of log events.",
  "logGroupName" : "The name of the log group.",
  "destinationArn" : "The ARN of the destination to deliver matching log events to. Currently, the supported destinations are:  \n An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.  \n A logical destination (specified using an ARN) belonging to a different account, for cross-account delivery.  \n An Amazon Kinesis Firehose delivery stream belonging to the same account as the subscription filter, for same-account delivery.  \n An AWS Lambda function belonging to the same account as the subscription filter, for same-account delivery. ",
  "roleArn" : "The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.",
  "filterName" : "A name for the subscription filter. If you are updating an existing filter, you must specify the correct name in filterName. Otherwise, the call fails because you cannot associate a second filter with a log group. To find the name of the filter currently associated with a log group, use DescribeSubscriptionFilters.",
  "distribution" : "The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. "
}
```

</details>

## tag_log_group

Adds or updates the specified tags for the specified log group. 
To list the tags for a log group, use ListTagsLogGroup. To remove tags, use UntagLogGroup. 
For more information about tags, see Tag Log Groups in Amazon CloudWatch Logs in the Amazon CloudWatch Logs User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "tags" : "The key-value pairs to use for the tags."
}
```

</details>

## test_metric_filter

Tests the filter pattern of a metric filter against a sample of log event messages. You can use this operation to validate the correctness of a metric filter pattern.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "filterPattern" : "Required string",
  "logEventMessages" : [ "string" ]
}
```

</details>

## untag_log_group

Removes the specified tags from the specified log group. 
To list the tags for a log group, use ListTagsLogGroup. To add tags, use UntagLogGroup.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "logGroupName" : "The name of the log group.",
  "tags" : [ "string" ]
}
```

</details>

