---
id: aws-cloudwatch-logs-documentation
title: AWS Cloudwatch Logs (version v2.*.*)
sidebar_label: AWS Cloudwatch Logs
---

## associate_kms_key

Associates the specified AWS Key Management Service (AWS KMS) customer master key (CMK) with the specified log group.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_AssociateKmsKey.html

<details><summary>Parameters</summary>

#### kmsKeyId (required)

The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.  For more information, see Amazon Resource Names - AWS Key Management Service (AWS KMS).

**Type:** STRING

#### logGroupName (required)

The name of the log group.

**Type:** STRING

</details>

## cancel_export_task

Cancels the specified export task. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CancelExportTask.html

<details><summary>Parameters</summary>

#### taskId (required)

The ID of the export task.

**Type:** STRING

</details>

## create_export_task

Creates an export task, which allows you to efficiently export data from a log group to an Amazon S3 bucket.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateExportTask.html

<details><summary>Parameters</summary>

#### destination (required)

The name of S3 bucket for the exported log data. The bucket must be in the same AWS region.

**Type:** STRING

#### from (required)

The start time of the range for the request, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a timestamp earlier than this time are not exported.

**Type:** NUMBER

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### to (required)

The end time of the range for the request, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a timestamp later than this time are not exported.

**Type:** NUMBER

#### destinationPrefix

The prefix used as the start of the key for every object exported. If you don't specify a value, the default is exportedlogs.

**Type:** STRING

#### logStreamNamePrefix

Export only log streams that match the provided prefix. If you don't specify a value, no prefix filter is applied.

**Type:** STRING

#### taskName

The name of the export task.

**Type:** STRING

</details>

## create_log_group

Creates a log group with the specified name. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### kmsKeyId

The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.  For more information, see Amazon Resource Names - AWS Key Management Service (AWS KMS).

**Type:** STRING

#### tags

The key-value pairs to use for the tags.

**Type:** OBJECT

</details>

## create_log_stream

Creates a log stream for the specified log group. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### logStreamName (required)

The name of the log stream.

**Type:** STRING

</details>

## delete_destination

Deletes the specified destination, and eventually disables all the subscription filters that publish to it. This operation does not delete the physical resource encapsulated by the destination.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteDestination.html

<details><summary>Parameters</summary>

#### destinationName (required)

The name of the destination.

**Type:** STRING

</details>

## delete_log_group

Deletes the specified log group and permanently deletes all the archived log events associated with the log group.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogGroup.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

</details>

## delete_log_stream

Deletes the specified log stream and permanently deletes all the archived log events associated with the log stream.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogStream.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### logStreamName (required)

The name of the log stream.

**Type:** STRING

</details>

## delete_metric_filter

Deletes the specified metric filter. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteMetricFilter.html

<details><summary>Parameters</summary>

#### filterName (required)

The name of the metric filter.

**Type:** STRING

#### logGroupName (required)

The name of the log group.

**Type:** STRING

</details>

## delete_resource_policy

Deletes a resource policy from this account. This revokes the access of the identities in that policy to put log events to this account.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteResourcePolicy.html

<details><summary>Parameters</summary>

#### policyName

The name of the policy to be revoked. This parameter is required.

**Type:** STRING

</details>

## delete_retention_policy

Deletes the specified retention policy. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

</details>

## delete_subscription_filter

Deletes the specified subscription filter. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteSubscriptionFilter.html

<details><summary>Parameters</summary>

#### filterName (required)

The name of the subscription filter.

**Type:** STRING

#### logGroupName (required)

The name of the log group.

**Type:** STRING

</details>

## disassociate_kms_key

Disassociates the associated AWS Key Management Service (AWS KMS) customer master key (CMK) from the specified log group.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DisassociateKmsKey.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

</details>

## filter_log_events

Lists log events from the specified log group. You can list all the log events or filter the results using a filter pattern, a time range, and the name of the log stream.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group to search.

**Type:** STRING

#### endTime

The end of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a timestamp later than this time are not returned.

**Type:** NUMBER

#### filterPattern

The filter pattern to use. For more information, see Filter and Pattern Syntax. If not provided, all the events are matched.

**Type:** STRING

#### interleaved

If the value is true, the operation makes a best effort to provide responses that contain events from multiple log streams within the log group, interleaved in a single response. If the value is false, all the matched log events in the first log stream are searched first, then those in the next log stream, and so on. The default is false.

**Type:** BOOLEAN

#### limit

The maximum number of events to return. The default is 10,000 events.

**Type:** INTEGER

#### logStreamNamePrefix

Filters the results to include only events from log streams that have names starting with this prefix. If you specify a value for both logStreamNamePrefix and logStreamNames, but the value for logStreamNamePrefix does not match any log stream names specified in logStreamNames, the action returns an InvalidParameterException error.

**Type:** STRING

#### logStreamNames

Filters the results to only logs from the log streams in this list. If you specify a value for both logStreamNamePrefix and logStreamNames, the action returns an InvalidParameterException error.

**Type:** ARRAY

#### nextToken

The token for the next set of events to return. (You received this token from a previous call.)

**Type:** STRING

#### startTime

The start of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a timestamp before this time are not returned.

**Type:** NUMBER

</details>

## get_log_group_fields

Returns a list of the fields that are included in log events in the specified log group, along with the percentage of log events that contain each field. The search is limited to a time period that you specify.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group to search.

**Type:** STRING

#### time

The time to set as the center of the query. If you specify time, the 8 minutes before and 8 minutes after this time are searched. If you omit time, the past 15 minutes are queried. The time value is specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC.

**Type:** NUMBER

</details>

## get_log_record

Retrieves all the fields and values of a single log event. All fields are retrieved, even if the original query that produced the logRecordPointer retrieved only a subset of fields. Fields are returned as field name/field value pairs.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogRecord.html

<details><summary>Parameters</summary>

#### logRecordPointer (required)

The pointer corresponding to the log event record you want to retrieve. You get this from the response of a GetQueryResults operation. In that response, the value of the @ptr field for a log event is the value to use as logRecordPointer to retrieve that complete log event record.

**Type:** STRING

</details>

## get_query_results

Returns the results from the specified query. If the query is in progress, partial results of that current execution are returned. Only the fields requested in the query are returned.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html

<details><summary>Parameters</summary>

#### queryId (required)

The ID number of the query.

**Type:** STRING

</details>

## list_destinations

Lists all your destinations. The results are ASCII-sorted by destination name. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDestinations.html

<details><summary>Parameters</summary>

#### DestinationNamePrefix

The prefix to match. If you don't specify a value, no prefix filter is applied.

**Type:** STRING

</details>

## list_export_tasks

Lists the specified export tasks. You can list all your export tasks or filter the results based on task ID or task status.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeExportTasks.html

<details><summary>Parameters</summary>

#### statusCode

The status code of the export task. Specifying a status code filters the results to zero or more export tasks.

**Type:** STRING

#### taskId

The ID of the export task. Specifying a task ID filters the results to zero or one export tasks.

**Type:** STRING

</details>

## list_log_events

Lists log events from the specified log stream. You can list all the log events or filter using a time range.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### logStreamName (required)

The name of the log stream.

**Type:** STRING

#### endTime

The end of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a timestamp equal to or later than this time are not included.

**Type:** NUMBER

#### startFromHead

If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. The default value is false.

**Type:** BOOLEAN

#### startTime

The start of the time range, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. Events with a timestamp equal to this time or later than this time are included. Events with a timestamp earlier than this time are not included.

**Type:** NUMBER

</details>

## list_log_groups

Lists the specified log groups. You can list all your log groups or filter the results by prefix. The results are ASCII-sorted by log group name.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.html

<details><summary>Parameters</summary>

#### logGroupNamePrefix

The prefix to match.

**Type:** STRING

</details>

## list_log_streams

Lists the log streams for the specified log group. You can list all the log streams or filter the results by prefix. You can also control how the results are ordered.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogStreams.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### descending

If the value is true, results are returned in descending order.  If the value is to false, results are returned in ascending order. The default value is false.

**Type:** BOOLEAN

#### logStreamNamePrefix

The prefix to match. If orderBy is LastEventTime,you cannot specify this parameter.

**Type:** STRING

#### orderBy

If the value is LogStreamName, the results are ordered by log stream name. If the value is LastEventTime, the results are ordered by the event time.  The default value is LogStreamName. If you order the results by event time, you cannot specify the logStreamNamePrefix parameter. lastEventTimestamp represents the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC. lastEventTimeStamp updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but may take longer in some rare situations.

**Type:** STRING

</details>

## list_metric_filters

Lists the specified metric filters. You can list all the metric filters or filter the results by log name, prefix, metric name, or metric namespace. The results are ASCII-sorted by filter name.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeMetricFilters.html

<details><summary>Parameters</summary>

#### filterNamePrefix

The prefix to match.

**Type:** STRING

#### logGroupName

The name of the log group.

**Type:** STRING

#### metricName

Filters results to include only those with the specified metric name. If you include this parameter in your request, you  must also include the metricNamespace parameter.

**Type:** STRING

#### metricNamespace

Filters results to include only those in the specified namespace. If you include this parameter in your request, you  must also include the metricName parameter.

**Type:** STRING

</details>

## list_queries

Returns a list of CloudWatch Logs Insights queries that are scheduled, executing, or have been executed recently in this account. You can request all queries, or limit it to queries of a specific log group or queries with a certain status.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueries.html

<details><summary>Parameters</summary>

#### logGroupName

Limits the returned queries to only those for the specified log group.

**Type:** STRING

#### status

Limits the returned queries to only those that have the specified status. Valid values are Cancelled,  Complete, Failed, Running, and Scheduled.

**Type:** STRING

</details>

## list_resource_policies



*This operation has no parameters*

## list_subscription_filters

Lists the subscription filters for the specified log group. You can list all the subscription filters or filter the results by prefix. The results are ASCII-sorted by filter name.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeSubscriptionFilters.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### filterNamePrefix

The prefix to match. If you don't specify a value, no prefix filter is applied.

**Type:** STRING

</details>

## list_tags_log_group

Lists the tags for the specified log group. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsLogGroup.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

</details>

## put_destination

Creates or updates a destination. A destination encapsulates a physical resource (such as an Amazon Kinesis stream) and enables you to subscribe to a real-time stream of log events for a different account, ingested using PutLogEvents. Currently, the only supported physical resource is a Kinesis stream belonging to the same account as the destination.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html

<details><summary>Parameters</summary>

#### destinationName (required)

A name for the destination.

**Type:** STRING

#### roleArn (required)

The ARN of an IAM role that grants CloudWatch Logs permissions to call the Amazon Kinesis PutRecord operation on the destination stream.

**Type:** STRING

#### targetArn (required)

The ARN of an Amazon Kinesis stream to which to deliver matching log events.

**Type:** STRING

</details>

## put_destination_policy

Creates or updates an access policy associated with an existing destination. An access policy is an IAM policy document that is used to authorize claims to register a subscription filter against a given destination.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.html

<details><summary>Parameters</summary>

#### accessPolicy (required)

An IAM policy document that authorizes cross-account users to deliver their log events to the associated destination.

**Type:** STRING

#### destinationName (required)

A name for an existing destination.

**Type:** STRING

</details>

## put_log_events

Uploads a batch of log events to the specified log stream. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html

<details><summary>Parameters</summary>

#### logEvents (required)

The log events.

**Type:** ARRAY

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### logStreamName (required)

The name of the log stream.

**Type:** STRING

#### sequenceToken

The sequence token obtained from the response of the previous PutLogEvents call. An upload in a newly created log stream does not require a sequence token. You can also get the sequence token using DescribeLogStreams. If you call PutLogEvents twice within a narrow time period using the same value for sequenceToken, both calls may be successful, or one may be rejected.

**Type:** STRING

</details>

## put_metric_filter

Creates or updates a metric filter and associates it with the specified log group. Metric filters allow you to configure rules to extract metric data from log events ingested through PutLogEvents.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutMetricFilter.html

<details><summary>Parameters</summary>

#### filterName (required)

A name for the metric filter.

**Type:** STRING

#### filterPattern (required)

A filter pattern for extracting metric data out of ingested log events.

**Type:** STRING

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### metricTransformations (required)

A collection of information that defines how metric data gets emitted.

**Type:** ARRAY

</details>

## put_resource_policy

Creates or updates a resource policy allowing other AWS services to put log events to this account, such as Amazon Route 53. An account can have up to 10 resource policies per region.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.html

<details><summary>Parameters</summary>

#### policyDocument

Details of the new policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. The following example creates a resource policy enabling the Route 53 service to put DNS query logs in to the specified log group. Replace "logArn" with the ARN of your CloudWatch Logs resource, such as a log group or log stream. {  "Version": "2012-10-17", "Statement": [ { "Sid": "Route53LogsToCloudWatchLogs",  "Effect": "Allow",  "Principal": { "Service": [ "route53.amazonaws.com" ] },  "Action":"logs:PutLogEvents",  "Resource": "logArn" } ] }

**Type:** STRING

#### policyName

Name of the new policy. This parameter is required.

**Type:** STRING

</details>

## put_retention_policy

Sets the retention of the specified log group. A retention policy allows you to configure the number of days for which to retain log events in the specified log group.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### retentionInDays (required)

The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653.

**Type:** INTEGER

</details>

## put_subscription_filter

Creates or updates a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events ingested through PutLogEvents and have them delivered to a specific destination. Currently, the supported destinations are:  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.html

<details><summary>Parameters</summary>

#### destinationArn (required)

The ARN of the destination to deliver matching log events to. Currently, the supported destinations are: An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery. A logical destination (specified using an ARN) belonging to a different account,  for cross-account delivery. An Amazon Kinesis Firehose delivery stream belonging to the same account as the subscription filter, for same-account delivery. An AWS Lambda function belonging to the same account as the subscription filter, for same-account delivery.

**Type:** STRING

#### filterName (required)

A name for the subscription filter. If you are updating an existing filter, you must specify the correct name in filterName. Otherwise, the call fails because you cannot associate a second filter with a log group. To find the name of the filter currently associated with a log group, use DescribeSubscriptionFilters.

**Type:** STRING

#### filterPattern (required)

A filter pattern for subscribing to a filtered stream of log events.

**Type:** STRING

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### distribution

The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream.

**Type:** STRING

#### roleArn

The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.

**Type:** STRING

</details>

## start_query

Schedules a query of a log group using CloudWatch Logs Insights. You specify the log group and time range to query, and the query string to use.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html

<details><summary>Parameters</summary>

#### endTime (required)

The end of the time range to query. The range is inclusive, so the specified end time is included in the query. Specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC.

**Type:** NUMBER

#### logGroupName (required)

The log group on which to perform the query.

**Type:** STRING

#### queryString (required)

The query string to use. For more information, see CloudWatch Logs Insights Query Syntax.

**Type:** STRING

#### startTime (required)

The beginning of the time range to query. The range is inclusive, so the specified start time is included in the query. Specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC.

**Type:** NUMBER

#### limit

The maximum number of log events to return in the query. If the query string uses the fields command, only the specified fields and their values are returned.

**Type:** INTEGER

</details>

## stop_query

Stops a CloudWatch Logs Insights query that is in progress. If the query has already ended, the operation returns an error indicating that the specified query is not running.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StopQuery.html

<details><summary>Parameters</summary>

#### queryId (required)

The ID number of the query to stop. If necessary, you can use DescribeQueries to find this ID number.

**Type:** STRING

</details>

## tag_log_group

Adds or updates the specified tags for the specified log group. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagLogGroup.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### tags (required)

The key-value pairs to use for the tags.

**Type:** OBJECT

</details>

## test_metric_filter

Tests the filter pattern of a metric filter against a sample of log event messages. You can use this operation to validate the correctness of a metric filter pattern.  https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TestMetricFilter.html

<details><summary>Parameters</summary>

#### filterPattern (required)

A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event may contain timestamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message.

**Type:** STRING

#### logEventMessages (required)

The log event messages to test.

**Type:** ARRAY

</details>

## untag_log_group

Removes the specified tags from the specified log group. https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagLogGroup.html

<details><summary>Parameters</summary>

#### logGroupName (required)

The name of the log group.

**Type:** STRING

#### tags (required)

The tag keys. The corresponding tags are removed from the log group.

**Type:** ARRAY

</details>

