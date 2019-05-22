---
id: aws-cloudwatch-documentation
title: AWS Cloudwatch (version v1.*.*)
sidebar_label: AWS Cloudwatch
layout: docs.mustache
---

## delete_alarms

Deletes the specified alarms. In the event of an error, no alarms are deleted.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteAlarms.html

<details><summary>Parameters</summary>

#### AlarmNames (required)

The alarms to be deleted.

**Type:** ARRAY

</details>

## delete_dashboards

Deletes all dashboards that you specify. You may specify up to 100 dashboards to delete. If there is an error during this call, no dashboards are deleted.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteDashboards.html

<details><summary>Parameters</summary>

#### DashboardNames (required)

The dashboards to be deleted. This parameter is required.

**Type:** ARRAY

</details>

## describe_alarm_history

Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for all alarms are returned.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html

<details><summary>Parameters</summary>

#### AlarmName

The name of the alarm.

**Type:** STRING

#### EndDate

The ending date to retrieve alarm history.

**Type:** STRING

#### HistoryItemType

The type of alarm histories to retrieve. Valid Values: ConfigurationUpdate | StateUpdate | Action

**Type:** STRING

#### MaxRecords

The maximum number of alarm history records to retrieve.

**Type:** INTEGER

#### NextToken

The token returned by a previous call to indicate that there is more data available.

**Type:** STRING

#### StartDate

The starting date to retrieve alarm history.

**Type:** STRING

</details>

## describe_alarms

Retrieves the specified alarms. If no alarms are specified, all alarms are returned. Alarms can be retrieved by using only a prefix for the alarm name, the alarm state, or a prefix for any action.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html

<details><summary>Parameters</summary>

#### ActionPrefix

The action name prefix.

**Type:** STRING

#### AlarmNamePrefix

The alarm name prefix. If this parameter is specified, you cannot specify AlarmNames.

**Type:** STRING

#### AlarmNames

The names of the alarms.

**Type:** ARRAY

#### MaxRecords

The maximum number of alarm descriptions to retrieve.

**Type:** INTEGER

#### NextToken

The token returned by a previous call to indicate that there is more data available.

**Type:** STRING

#### StateValue

The state value to be used in matching alarms. Valid Values: OK | ALARM | INSUFFICIENT_DATA

**Type:** STRING

</details>

## describe_alarms_for_metric

Retrieves the alarms for the specified metric. To filter the results, specify a statistic, period, or unit.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmsForMetric.html

<details><summary>Parameters</summary>

#### MetricName (required)

The name of the metric.

**Type:** STRING

#### Namespace (required)

The namespace of the metric.

**Type:** STRING

#### Dimensions

The dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the call to succeed.

**Type:** ARRAY

#### ExtendedStatistic

The percentile statistic for the metric. Specify a value between p0.0 and p100.

**Type:** STRING

#### Period

The period, in seconds, over which the statistic is applied.

**Type:** INTEGER

#### Statistic

The statistic for the metric, other than percentiles. For percentile statistics, use ExtendedStatistics.

**Type:** STRING

#### Unit

The unit for the metric.

**Type:** STRING

</details>

## disable_alarm_actions

Disables the actions for the specified alarms. When an alarm's actions are disabled, the alarm actions do not execute when the alarm state changes.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisableAlarmActions.html

<details><summary>Parameters</summary>

#### AlarmNames (required)

The names of the alarms.

**Type:** ARRAY

</details>

## enable_alarm_actions

Enables the actions for the specified alarms. https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableAlarmActions.html

<details><summary>Parameters</summary>

#### AlarmNames (required)

The names of the alarms.

**Type:** ARRAY

</details>

## get_dashboard

Displays the details of the dashboard that you specify. https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDashboard.html

<details><summary>Parameters</summary>

#### DashboardName (required)

The name of the dashboard to be described.

**Type:** STRING

</details>

## get_metric_data

You can use the GetMetricData API to retrieve as many as 100 different metrics in a single request, with a total of as many as 100,800 datapoints. You can also optionally perform math expressions on the values of the returned statistics, to create new time series that represent new insights into your data. For example, using Lambda metrics, you could divide the Errors metric by the Invocations metric to get an error rate time series. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html

<details><summary>Parameters</summary>

#### EndTime (required)

The time stamp indicating the latest data to be returned. For better performance, specify StartTime and EndTime values that align with the value of the metric's Period and sync up with the beginning and end of an hour. For example, if the Period of a metric is 5 minutes, specifying 12:05 or 12:30 as EndTime can get a faster response from CloudWatch than setting 12:07 or 12:29 as the EndTime.

**Type:** STRING

#### MetricDataQueries (required)

The metric queries to be returned. A single GetMetricData call can include as many as 100 MetricDataQuery structures. Each of these structures can specify either a metric to retrieve, or a math expression to perform on retrieved data.

**Type:** ARRAY

#### StartTime (required)

The time stamp indicating the earliest data to be returned. For better performance, specify StartTime and EndTime values that align with the value of the metric's Period and sync up with the beginning and end of an hour. For example, if the Period of a metric is 5 minutes, specifying 12:05 or 12:30 as StartTime can get a faster response from CloudWatch than setting 12:07 or 12:29 as the StartTime.

**Type:** STRING

#### MaxDatapoints

The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used.

**Type:** INTEGER

#### NextToken

Include this value, if it was returned by the previous call, to get the next set of data points.

**Type:** STRING

#### ScanBy

The order in which data points should be returned. TimestampDescending returns the newest data first and paginates when the MaxDatapoints limit is reached. TimestampAscending returns the oldest data first and paginates when the MaxDatapoints limit is reached.

**Type:** STRING

</details>

## get_metric_statistics

Gets statistics for the specified metric. https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html

<details><summary>Parameters</summary>

#### EndTime (required)

The time stamp that determines the last data point to return. The value specified is exclusive; results include data points up to the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).

**Type:** STRING

#### MetricName (required)

The name of the metric, with or without spaces.

**Type:** STRING

#### Namespace (required)

The namespace of the metric, with or without spaces.

**Type:** STRING

#### Period (required)

The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second. If the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned: Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute). Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes). Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).

**Type:** INTEGER

#### StartTime (required)

The time stamp that determines the first data point to return. Start times are  evaluated relative to the time that CloudWatch receives the request. The value specified is inclusive; results include data points with the specified time stamp.  The time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z). CloudWatch rounds the specified time stamp as follows: Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00. Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00. Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00. If you set Period to 5, 10, or 30, the start time of your request is  rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to  01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a  period of 5 seconds, you receive data  timestamped between 15:02:15 and 15:07:15.

**Type:** STRING

#### Dimensions

The dimensions. If the metric contains multiple dimensions, you must include a value for each dimension. CloudWatch treats each unique combination of dimensions as a separate metric. If a specific combination of dimensions was not published, you can't retrieve statistics for it. You must specify the same dimensions that were used when the metrics were created. For an example, see Dimension Combinations in the Amazon CloudWatch User Guide. For more information about specifying dimensions, see Publishing Metrics in the Amazon CloudWatch User Guide. The name of the dimension. Length Constraints: Minimum length of 1. Maximum length of 255.

**Type:** ARRAY

#### ExtendedStatistics

The percentile statistics. Specify values between p0.0 and p100. When calling GetMetricStatistics, you must  specify either Statistics or ExtendedStatistics, but not both. Percentile statistics are not  available for metrics when any of the metric values are negative numbers. Minimum number of 1 item. Maximum number of 10 items.

**Type:** ARRAY

#### Statistics

The metric statistics, other than percentile. For percentile statistics, use ExtendedStatistics. When calling GetMetricStatistics, you must  specify either Statistics or ExtendedStatistics, but not both. Minimum number of 1 item. Maximum number of 5 items. Valid Values: SampleCount | Average | Sum | Minimum | Maximum

**Type:** ARRAY

#### Unit

The unit for a given metric. Metrics may be reported in multiple units. Not supplying a unit results in all units being returned. If you specify only a unit that  the metric does not report, the results of the call are null. Valid Values: Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None

**Type:** STRING

</details>

## get_metric_widget_image

You can use the GetMetricWidgetImage API to retrieve a snapshot graph of one or more Amazon CloudWatch metrics as a bitmap image. You can then embed this image into your services and products, such as wiki pages, reports, and documents. You could also retrieve images regularly, such as every minute, and create your own custom live dashboard.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricWidgetImage.html

<details><summary>Parameters</summary>

#### MetricWidget (required)

A JSON string that defines the bitmap graph to be retrieved. The string includes the metrics to include in the graph, statistics, annotations, title, axis limits, and so on.  You can include only one MetricWidget parameter in each GetMetricWidgetImage call. For more information about the syntax of MetricWidget see GetMetricWidgetImage: Metric Widget Structure and Syntax. If any metric on the graph could not load all the requested data points, an orange triangle with an exclamation point appears next to the graph legend.

**Type:** STRING

#### OutputFormat

The format of the resulting image. Only PNG images are supported. The default is png. If you specify png, the API returns an HTTP response with the  content-type set to text/xml. The image data is in a MetricWidgetImage  field. For example: <GetMetricWidgetImageResponse xmlns=<URLstring>> <GetMetricWidgetImageResult> <MetricWidgetImage> iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQEAYAAAAip... </MetricWidgetImage> </GetMetricWidgetImageResult> <ResponseMetadata> <RequestId>6f0d4192-4d42-11e8-82c1-f539a07e0e3b</RequestId> </ResponseMetadata> </GetMetricWidgetImageResponse> The image/png setting is intended only for custom HTTP requests. For most use cases, and all actions using an AWS SDK, you should use png. If you specify  image/png, the HTTP response has a content-type set to image/png,  and the body of the response is a PNG image.

**Type:** STRING

</details>

## list_dashboards

Returns a list of the dashboards for your account. If you include DashboardNamePrefix, only those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your account are listed.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListDashboards.html

<details><summary>Parameters</summary>

#### DashboardNamePrefix

If you specify this parameter, only the dashboards with names starting with the specified string are listed. The maximum length is 255, and  valid characters are A-Z, a-z, 0-9, ".", "-", and "_".

**Type:** STRING

#### NextToken

The token returned by a previous call to indicate that there is more data available.

**Type:** STRING

</details>

## list_metrics

List the specified metrics. You can use the returned metrics with GetMetricData or GetMetricStatistics to obtain statistical data.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html

<details><summary>Parameters</summary>

#### Dimensions

The dimensions to filter against. 

**Type:** ARRAY

#### MetricName

The name of the metric to filter against.

**Type:** STRING

#### Namespace

The namespace to filter against.

**Type:** STRING

#### NextToken

The token returned by a previous call to indicate that there is more data available.

**Type:** STRING

</details>

## list_tags_for_resource

Displays the tags associated with a CloudWatch resource. Alarms support tagging. https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListTagsForResource.html

<details><summary>Parameters</summary>

#### ResourceARN (required)

The ARN of the CloudWatch resource that you want to view tags for. For more information on ARN format, see  Example ARNs in the Amazon Web Services General Reference.

**Type:** STRING

</details>

## put_dashboard

Creates a dashboard if it does not already exist, or updates an existing dashboard. If you update a dashboard, the entire contents are replaced with what you specify here.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutDashboard.html

<details><summary>Parameters</summary>

#### DashboardBody (required)

The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard.  This parameter is required. For more information about the syntax,  see Dashboard Body Structure and Syntax.

**Type:** STRING

#### DashboardName (required)

The name of the dashboard. If a dashboard with this name already exists, this call modifies that dashboard, replacing its current contents. Otherwise, a new dashboard is created. The maximum length is 255, and valid characters are  A-Z, a-z, 0-9, "-", and "_".  This parameter is required.

**Type:** STRING

</details>

## put_metric_alarm

Creates or updates an alarm and associates it with the specified metric or metric math expression.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html

<details><summary>Parameters</summary>

#### AlarmName (required)

The name for the alarm. This name must be unique within your AWS account.

**Type:** STRING

#### ComparisonOperator (required)

The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.

**Type:** STRING

#### EvaluationPeriods (required)

The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an "M out of N" alarm, this value is the N. An alarm's total current evaluation period can be no longer than one day, so this number multiplied by Period cannot be more than 86,400 seconds.

**Type:** INTEGER

#### Threshold (required)

The value against which the specified statistic is compared.

**Type:** NUMBER

#### ActionsEnabled

Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.

**Type:** BOOLEAN

#### AlarmActions

The actions to execute when this alarm transitions to the ALARM state from any other state.  Each action is specified as an Amazon Resource Name (ARN). Valid Values: arn:aws:automate:region:ec2:stop |  arn:aws:automate:region:ec2:terminate |  arn:aws:automate:region:ec2:recover | arn:aws:automate:region:ec2:reboot | arn:aws:sns:region:account-id:sns-topic-name | arn:aws:autoscaling:region:account-id:scalingPolicy:policy-idautoScalingGroupName/group-friendly-name:policyName/policy-friendly-name Valid Values (for use with IAM roles): arn:aws:swf:region:account-id:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:region:account-id:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:region:account-id:action/actions/AWS_EC2.InstanceId.Reboot/1.0

**Type:** ARRAY

#### AlarmDescription

The description for the alarm.

**Type:** STRING

#### DatapointsToAlarm

The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting  an "M out of N" alarm. In that case, this value is the M. For more information, see  Evaluating an Alarm in the Amazon CloudWatch User Guide.

**Type:** INTEGER

#### Dimensions

The dimensions for the metric specified in MetricName.

**Type:** ARRAY

#### EvaluateLowSampleCountPercentile

Used only for alarms based on percentiles. If you specify ignore, the alarm state does not change during periods with too few data points to be  statistically significant. If you specify evaluate or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see Percentile-Based CloudWatch Alarms and Low Data Samples. Valid Values: evaluate | ignore

**Type:** STRING

#### ExtendedStatistic

The percentile statistic for the metric specified in MetricName. Specify a value  between p0.0 and p100. When you call PutMetricAlarm and specify  a MetricName, you must  specify either Statistic or ExtendedStatistic, but not both.

**Type:** STRING

#### InsufficientDataActions

The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.  Each action is specified as an Amazon Resource Name (ARN). Valid Values: arn:aws:automate:region:ec2:stop |  arn:aws:automate:region:ec2:terminate |  arn:aws:automate:region:ec2:recover | arn:aws:automate:region:ec2:reboot | arn:aws:sns:region:account-id:sns-topic-name | arn:aws:autoscaling:region:account-id:scalingPolicy:policy-idautoScalingGroupName/group-friendly-name:policyName/policy-friendly-name Valid Values (for use with IAM roles): >arn:aws:swf:region:account-id:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:region:account-id:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:region:account-id:action/actions/AWS_EC2.InstanceId.Reboot/1.0

**Type:** ARRAY

#### MetricName

The name for the metric associated with the alarm. If you are creating an alarm based on a math expression, you cannot specify this parameter, or any of the  Dimensions, Period, Namespace, Statistic, or ExtendedStatistic parameters. Instead, you specify  all this information in the Metrics array.

**Type:** STRING

#### Metrics

An array of MetricDataQuery structures that enable you to create an alarm based on the result of a metric math expression. Each item in the Metrics array either retrieves a metric or performs a math expression. One item in the Metrics array is the expression that the alarm watches. You designate this expression  by setting ReturnValue to true for this object in the array. For more information, see MetricDataQuery. If you use the Metrics parameter, you cannot include the MetricName, Dimensions, Period, Namespace, Statistic, or ExtendedStatistic parameters of PutMetricAlarm in the same operation.  Instead, you retrieve the metrics you are using in your math expression as part of the Metrics array.

**Type:** ARRAY

#### Namespace

The namespace for the metric associated specified in MetricName.

**Type:** STRING

#### OKActions

The actions to execute when this alarm transitions to an OK state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid Values: arn:aws:automate:region:ec2:stop |  arn:aws:automate:region:ec2:terminate |  arn:aws:automate:region:ec2:recover | arn:aws:automate:region:ec2:reboot | arn:aws:sns:region:account-id:sns-topic-name | arn:aws:autoscaling:region:account-id:scalingPolicy:policy-idautoScalingGroupName/group-friendly-name:policyName/policy-friendly-name Valid Values (for use with IAM roles): arn:aws:swf:region:account-id:action/actions/AWS_EC2.InstanceId.Stop/1.0 | arn:aws:swf:region:account-id:action/actions/AWS_EC2.InstanceId.Terminate/1.0 | arn:aws:swf:region:account-id:action/actions/AWS_EC2.InstanceId.Reboot/1.0

**Type:** ARRAY

#### Period

The length, in seconds, used each time the metric specified in MetricName is evaluated. Valid values are 10, 30, and any multiple of 60. Be sure to specify 10 or 30 only for metrics that are stored by a PutMetricData call with a StorageResolution of 1. If you specify a period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm may often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see Amazon CloudWatch Pricing. An alarm's total current evaluation period can be no longer than one day, so Period multiplied by EvaluationPeriods cannot be more than 86,400 seconds.

**Type:** INTEGER

#### Statistic

The statistic for the metric specified in MetricName, other than percentile. For percentile statistics, use ExtendedStatistic. When you call PutMetricAlarm and specify  a MetricName, you must  specify either Statistic or ExtendedStatistic, but not both.

**Type:** STRING

#### Tags

A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.

**Type:** ARRAY

#### TreatMissingData

Sets how this alarm is to handle missing data points. If TreatMissingData is omitted, the default behavior of missing is used.  For more information, see Configuring How CloudWatch  Alarms Treats Missing Data. Valid Values: breaching | notBreaching | ignore | missing

**Type:** STRING

#### Unit

The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately. If you specify a unit, you must use a unit that is appropriate for the metric.  Otherwise, the CloudWatch alarm can get stuck in the INSUFFICIENT DATA state.

**Type:** STRING

</details>

## put_metric_data

Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to ListMetrics.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricData.html

<details><summary>Parameters</summary>

#### Namespace (required)

The namespace for the metric data. You cannot specify a namespace that begins with "AWS/". Namespaces that begin with "AWS/" are reserved for use by Amazon Web Services products.

**Type:** STRING

#### MetricData

The data for the metric. The array can include no more than 20 metrics per call.

**Type:** ARRAY

</details>

## set_alarm_state

Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to ALARM sends an SNS message. The alarm returns to its actual state (often within seconds). Because the alarm state change happens quickly, it is typically only visible in the alarm's History tab in the Amazon CloudWatch console or through DescribeAlarmHistory.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_SetAlarmState.html

<details><summary>Parameters</summary>

#### AlarmName (required)

The name for the alarm. This name must be unique within the AWS account. The maximum length is 255 characters.

**Type:** STRING

#### StateReason (required)

The reason that this alarm is set to this specific state, in text format.

**Type:** STRING

#### StateValue (required)

The value of the state.

**Type:** STRING

#### StateReasonData

The reason that this alarm is set to this specific state, in JSON format.

**Type:** STRING

</details>

## tag_resource

Assigns one or more tags (key-value pairs) to the specified CloudWatch resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values. In CloudWatch, alarms can be tagged.  https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html

<details><summary>Parameters</summary>

#### ResourceARN (required)

The ARN of the CloudWatch resource that you're adding tags to. For more information on ARN format, see  Example ARNs in the Amazon Web Services General Reference.

**Type:** STRING

#### Tags

The list of key-value pairs to associate with the resource.

**Type:** ARRAY

</details>

## untag_resource

Removes one or more tags from the specified resource. https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html

<details><summary>Parameters</summary>

#### ResourceARN (required)

The ARN of the CloudWatch resource that you're removing tags from. For more information on ARN format, see  Example ARNs in the Amazon Web Services General Reference.

**Type:** STRING

#### TagKeys (required)

The list of tag keys to remove from the resource.

**Type:** ARRAY

</details>

