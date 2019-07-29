---
id: aws-cloudwatch-documentation
title: AWS Cloudwatch (version v2.*.*)
sidebar_label: AWS Cloudwatch
layout: docs.mustache
---

## delete_alarms

Deletes the specified alarms. In the event of an error, no alarms are deleted.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AlarmNames" : [ "string" ]
}
```

</details>

## delete_dashboards

Deletes all dashboards that you specify. You may specify up to 100 dashboards to delete. If there is an error during this call, no dashboards are deleted.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DashboardNames" : [ "string" ]
}
```

</details>

## describe_alarm_history

Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for all alarms are returned. 
CloudWatch retains the history of an alarm even if you delete the alarm.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "StartDate" : "The starting date to retrieve alarm history.",
  "AlarmName" : "The name of the alarm.",
  "HistoryItemType" : "The type of alarm histories to retrieve.",
  "EndDate" : "The ending date to retrieve alarm history."
}
```

</details>

## describe_alarms

Retrieves the specified alarms. If no alarms are specified, all alarms are returned. Alarms can be retrieved by using only a prefix for the alarm name, the alarm state, or a prefix for any action.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AlarmNames" : [ "string" ],
  "ActionPrefix" : "The action name prefix.",
  "StateValue" : "The state value to be used in matching alarms.",
  "AlarmNamePrefix" : "The alarm name prefix. If this parameter is specified, you cannot specify AlarmNames."
}
```

</details>

## describe_alarms_for_metric

Retrieves the alarms for the specified metric. To filter the results, specify a statistic, period, or unit.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "MetricName" : "The name of the metric.",
  "ExtendedStatistic" : "The percentile statistic for the metric. Specify a value between p0.0 and p100.",
  "Statistic" : "The statistic for the metric, other than percentiles. For percentile statistics, use ExtendedStatistics.",
  "Dimensions" : [ {
    "Dimension" : {
      "Value" : "The value representing the dimension measurement.",
      "Name" : "The name of the dimension."
    }
  } ],
  "Period" : "The period, in seconds, over which the statistic is applied.",
  "Unit" : "The unit for the metric.",
  "Namespace" : "The namespace of the metric."
}
```

</details>

## disable_alarm_actions

Disables the actions for the specified alarms. When an alarm's actions are disabled, the alarm actions do not execute when the alarm state changes.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AlarmNames" : [ "string" ]
}
```

</details>

## enable_alarm_actions

Enables the actions for the specified alarms.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "AlarmNames" : [ "string" ]
}
```

</details>

## get_dashboard

Displays the details of the dashboard that you specify. 
To copy an existing dashboard, use GetDashboard, and then use the data returned within DashboardBody as the template for the new dashboard when you call PutDashboard to create the copy.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DashboardName" : "The name of the dashboard to be described."
}
```

</details>

## get_metric_data

You can use the GetMetricData API to retrieve as many as 100 different metrics in a single request, with a total of as many as 100,800 datapoints. You can also optionally perform math expressions on the values of the returned statistics, to create new time series that represent new insights into your data. For example, using Lambda metrics, you could divide the Errors metric by the Invocations metric to get an error rate time series. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide. 
Calls to the GetMetricData API have a different pricing structure than calls to GetMetricStatistics. For more information about pricing, see Amazon CloudWatch Pricing. 
Amazon CloudWatch retains metric data as follows:  
 Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a StorageResolution of 1.  
 Data points with a period of 60 seconds (1-minute) are available for 15 days.  
 Data points with a period of 300 seconds (5-minute) are available for 63 days.  
 Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).   
Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "EndTime" : "The time stamp indicating the latest data to be returned. \nFor better performance, specify StartTime and EndTime values that align with the value of the metric's Period and sync up with the beginning and end of an hour. For example, if the Period of a metric is 5 minutes, specifying 12:05 or 12:30 as EndTime can get a faster response from CloudWatch then setting 12:07 or 12:29 as the EndTime.",
  "NextToken" : "Include this value, if it was returned by the previous call, to get the next set of data points.",
  "ScanBy" : "The order in which data points should be returned. TimestampDescending returns the newest data first and paginates when the MaxDatapoints limit is reached. TimestampAscending returns the oldest data first and paginates when the MaxDatapoints limit is reached.",
  "StartTime" : "The time stamp indicating the earliest data to be returned. \nFor better performance, specify StartTime and EndTime values that align with the value of the metric's Period and sync up with the beginning and end of an hour. For example, if the Period of a metric is 5 minutes, specifying 12:05 or 12:30 as StartTime can get a faster response from CloudWatch then setting 12:07 or 12:29 as the StartTime.",
  "MetricDataQueries" : [ {
    "MetricDataQuery" : {
      "ReturnData" : "Indicates whether to return the time stamps and raw data values of this metric. If you are performing this call just to do math expressions and do not also need the raw data returned, you can specify False. If you omit this, the default of True is used.",
      "Expression" : "The math expression to be performed on the returned data, if this structure is performing a math expression. For more information about metric math expressions, see Metric Math Syntax and Functions in the Amazon CloudWatch User Guide. \nWithin one MetricDataQuery structure, you must specify either Expression or MetricStat but not both.",
      "MetricStat" : {
        "Stat" : "The statistic to return. It can include any CloudWatch statistic or extended statistic.",
        "Period" : "The period to use when retrieving the metric.",
        "Metric" : {
          "MetricName" : "The name of the metric.",
          "Dimensions" : [ {
            "Dimension" : {
              "Value" : "The value representing the dimension measurement.",
              "Name" : "The name of the dimension."
            }
          } ],
          "Namespace" : "The namespace of the metric."
        },
        "Unit" : "The unit to use for the returned data points."
      },
      "Label" : "A human-readable label for this metric or expression. This is especially useful if this is an expression, so that you know what the value represents. If the metric or expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is omitted, CloudWatch generates a default.",
      "Id" : "A short name used to tie this structure to the results in the response. This name must be unique within a single call to GetMetricData. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscore. The first character must be a lowercase letter."
    }
  } ],
  "MaxDatapoints" : "The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used."
}
```

</details>

## get_metric_statistics

Gets statistics for the specified metric. 
The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, CloudWatch returns an error. To reduce the number of data points, you can narrow the specified time range and make multiple requests across adjacent time ranges, or you can increase the specified period. Data points are not returned in chronological order. 
CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-hour period, CloudWatch aggregates all data points with time stamps that fall within each one-hour period. Therefore, the number of values aggregated by CloudWatch is larger than the number of data points returned. 
CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:  
 The SampleCount value of the statistic set is 1.  
 The Min and the Max values of the statistic set are equal.   
Percentile statistics are not available for metrics when any of the metric values are negative numbers. 
Amazon CloudWatch retains metric data as follows:  
 Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a StorageResolution of 1.  
 Data points with a period of 60 seconds (1-minute) are available for 15 days.  
 Data points with a period of 300 seconds (5-minute) are available for 63 days.  
 Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).   
Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour. 
CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016. 
For information about metrics and dimensions supported by AWS services, see the Amazon CloudWatch Metrics and Dimensions Reference in the Amazon CloudWatch User Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "MetricName" : "The name of the metric, with or without spaces.",
  "EndTime" : "The time stamp that determines the last data point to return. \nThe value specified is exclusive; results include data points up to the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).",
  "StartTime" : "The time stamp that determines the first data point to return. Start times are evaluated relative to the time that CloudWatch receives the request. \nThe value specified is inclusive; results include data points with the specified time stamp. The time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z). \nCloudWatch rounds the specified time stamp as follows:  \n Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.  \n Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.  \n Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.   \nIf you set Period to 5, 10, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15. ",
  "Dimensions" : [ {
    "Dimension" : {
      "Value" : "The value representing the dimension measurement.",
      "Name" : "The name of the dimension."
    }
  } ],
  "Period" : "The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a PutMetricData call that includes a StorageResolution of 1 second. \nIf the StartTime parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:  \n Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).  \n Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).  \n Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour). ",
  "Unit" : "The unit for a given metric. Metrics may be reported in multiple units. Not supplying a unit results in all units being returned. If you specify only a unit that the metric does not report, the results of the call are null.",
  "Statistics" : [ "string. Possible values: SampleCount | Average | Sum | Minimum | Maximum" ],
  "ExtendedStatistics" : [ "string" ],
  "Namespace" : "The namespace of the metric, with or without spaces."
}
```

</details>

## get_metric_widget_image

You can use the GetMetricWidgetImage API to retrieve a snapshot graph of one or more Amazon CloudWatch metrics as a bitmap image. You can then embed this image into your services and products, such as wiki pages, reports, and documents. You could also retrieve images regularly, such as every minute, and create your own custom live dashboard. 
The graph you retrieve can include all CloudWatch metric graph features, including metric math and horizontal and vertical annotations. 
There is a limit of 20 transactions per second for this API. Each GetMetricWidgetImage action has the following limits:  
 As many as 100 metrics in the graph.  
 Up to 100 KB uncompressed payload. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "OutputFormat" : "The format of the resulting image. Only PNG images are supported. \nThe default is png. If you specify png, the API returns an HTTP response with the content-type set to text/xml. The image data is in a MetricWidgetImage field. For example: \n  &lt;GetMetricWidgetImageResponse xmlns=\"http://monitoring.amazonaws.com/doc/2010-08-01/\"&gt;  \n  &lt;GetMetricWidgetImageResult&gt;  \n  &lt;MetricWidgetImage&gt;  \n  iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQEAYAAAAip...  \n  &lt;/MetricWidgetImage&gt;  \n  &lt;/GetMetricWidgetImageResult&gt;  \n  &lt;ResponseMetadata&gt;  \n  &lt;RequestId&gt;6f0d4192-4d42-11e8-82c1-f539a07e0e3b&lt;/RequestId&gt;  \n  &lt;/ResponseMetadata&gt;  \n &lt;/GetMetricWidgetImageResponse&gt;  \nThe image/png setting is intended only for custom HTTP requests. For most use cases, and all actions using an AWS SDK, you should use png. If you specify image/png, the HTTP response has a content-type set to image/png, and the body of the response is a PNG image. ",
  "MetricWidget" : "A JSON string that defines the bitmap graph to be retrieved. The string includes the metrics to include in the graph, statistics, annotations, title, axis limits, and so on. You can include only one MetricWidget parameter in each GetMetricWidgetImage call. \nFor more information about the syntax of MetricWidget see CloudWatch-Metric-Widget-Structure. \nIf any metric on the graph could not load all the requested data points, an orange triangle with an exclamation point appears next to the graph legend."
}
```

</details>

## list_dashboards

Returns a list of the dashboards for your account. If you include DashboardNamePrefix, only those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your account are listed.  
 ListDashboards returns up to 1000 results on one page. If there are more than 1000 dashboards, you can call ListDashboards again and include the value you received for NextToken in the first call, to receive the next 1000 results.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DashboardNamePrefix" : "If you specify this parameter, only the dashboards with names starting with the specified string are listed. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, \".\", \"-\", and \"_\". "
}
```

</details>

## list_metrics

List the specified metrics. You can use the returned metrics with GetMetricData or GetMetricStatistics to obtain statistical data. 
Up to 500 results are returned for any one call. To retrieve additional results, use the returned token with subsequent calls. 
After you create a metric, allow up to fifteen minutes before the metric appears. Statistics about the metric, however, are available sooner using GetMetricData or GetMetricStatistics.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "MetricName" : "The name of the metric to filter against.",
  "Dimensions" : [ {
    "DimensionFilter" : {
      "Value" : "The value of the dimension to be matched.",
      "Name" : "The dimension name to be matched."
    }
  } ],
  "Namespace" : "The namespace to filter against."
}
```

</details>

## put_dashboard

Creates a dashboard if it does not already exist, or updates an existing dashboard. If you update a dashboard, the entire contents are replaced with what you specify here. 
There is no limit to the number of dashboards in your account. All dashboards in your account are global, not region-specific. 
A simple way to create a dashboard using PutDashboard is to copy an existing dashboard. To copy an existing dashboard using the console, you can load the dashboard and then use the View/edit source command in the Actions menu to display the JSON block for that dashboard. Another way to copy a dashboard is to use GetDashboard, and then use the data returned within DashboardBody as the template for the new dashboard when you call PutDashboard. 
When you create a dashboard with PutDashboard, a good practice is to add a text widget at the top of the dashboard with a message that the dashboard was created by script and should not be changed in the console. This message could also point console users to the location of the DashboardBody script or the CloudFormation template used to create the dashboard.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DashboardName" : "The name of the dashboard. If a dashboard with this name already exists, this call modifies that dashboard, replacing its current contents. Otherwise, a new dashboard is created. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, \"-\", and \"_\". This parameter is required.",
  "DashboardBody" : "The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required. \nFor more information about the syntax, see CloudWatch-Dashboard-Body-Structure."
}
```

</details>

## put_metric_alarm

Creates or updates an alarm and associates it with the specified metric. Optionally, this operation can associate one or more Amazon SNS resources with the alarm. 
When this operation creates an alarm, the alarm state is immediately set to INSUFFICIENT_DATA. The alarm is evaluated and its state is set appropriately. Any actions associated with the state are then executed. 
When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm. 
If you are an IAM user, you must have Amazon EC2 permissions for some operations:  
  iam:CreateServiceLinkedRole for all alarms with EC2 actions  
  ec2:DescribeInstanceStatus and ec2:DescribeInstances for all alarms on EC2 instance status metrics  
  ec2:StopInstances for alarms with stop actions  
  ec2:TerminateInstances for alarms with terminate actions  
  ec2:DescribeInstanceRecoveryAttribute and ec2:RecoverInstances for alarms with recover actions   
If you have read/write permissions for Amazon CloudWatch but not for Amazon EC2, you can still create an alarm, but the stop or terminate actions are not performed. However, if you are later granted the required permissions, the alarm actions that you created earlier are performed. 
If you are using an IAM role (for example, an EC2 instance profile), you cannot stop or terminate the instance using alarm actions. However, you can still see the alarm state and perform any other actions such as Amazon SNS notifications or Auto Scaling policies. 
If you are using temporary security credentials granted using AWS STS, you cannot stop or terminate an EC2 instance using alarm actions. 
The first time you create an alarm in the AWS Management Console, the CLI, or by using the PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The service-linked role is called AWSServiceRoleForCloudWatchEvents. For more information about service-linked roles, see AWS service-linked role.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ExtendedStatistic" : "The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100. When you call PutMetricAlarm, you must specify either Statistic or ExtendedStatistic, but not both.",
  "EvaluateLowSampleCountPercentile" : " Used only for alarms based on percentiles. If you specify ignore, the alarm state does not change during periods with too few data points to be statistically significant. If you specify evaluate or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see Percentile-Based CloudWatch Alarms and Low Data Samples. \nValid Values: evaluate | ignore ",
  "ComparisonOperator" : " The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.",
  "TreatMissingData" : " Sets how this alarm is to handle missing data points. If TreatMissingData is omitted, the default behavior of missing is used. For more information, see Configuring How CloudWatch Alarms Treats Missing Data. \nValid Values: breaching | notBreaching | ignore | missing ",
  "Dimensions" : [ {
    "Dimension" : {
      "Value" : "The value representing the dimension measurement.",
      "Name" : "The name of the dimension."
    }
  } ],
  "Period" : "The period, in seconds, over which the specified statistic is applied. Valid values are 10, 30, and any multiple of 60. \nBe sure to specify 10 or 30 only for metrics that are stored by a PutMetricData call with a StorageResolution of 1. If you specify a period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm may often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see Amazon CloudWatch Pricing. \nAn alarm's total current evaluation period can be no longer than one day, so Period multiplied by EvaluationPeriods cannot be more than 86,400 seconds.",
  "EvaluationPeriods" : "The number of periods over which data is compared to the specified threshold. If you are setting an alarm which requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an \"M out of N\" alarm, this value is the N. \nAn alarm's total current evaluation period can be no longer than one day, so this number multiplied by Period cannot be more than 86,400 seconds.",
  "Unit" : "The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately. \nIf you specify a unit, you must use a unit that is appropriate for the metric. Otherwise, the CloudWatch alarm can get stuck in the INSUFFICIENT DATA state. ",
  "OKActions" : [ "string" ],
  "Namespace" : "The namespace for the metric associated with the alarm.",
  "AlarmActions" : [ "string" ],
  "MetricName" : "The name for the metric associated with the alarm.",
  "ActionsEnabled" : "Indicates whether actions should be executed during any changes to the alarm state.",
  "AlarmName" : "The name for the alarm. This name must be unique within the AWS account.",
  "AlarmDescription" : "The description for the alarm.",
  "Statistic" : "The statistic for the metric associated with the alarm, other than percentile. For percentile statistics, use ExtendedStatistic. When you call PutMetricAlarm, you must specify either Statistic or ExtendedStatistic, but not both.",
  "InsufficientDataActions" : [ "string" ],
  "DatapointsToAlarm" : "The number of datapoints that must be breaching to trigger the alarm. This is used only if you are setting an \"M out of N\" alarm. In that case, this value is the M. For more information, see Evaluating an Alarm in the Amazon CloudWatch User Guide.",
  "Threshold" : "The value against which the specified statistic is compared."
}
```

</details>

## put_metric_data

Publishes metric data to Amazon CloudWatch. CloudWatch associates the data with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to ListMetrics. 
You can publish either individual data points in the Value field, or arrays of values and the number of times each value occurred during the period by using the Values and Counts fields in the MetricDatum structure. Using the Values and Counts method enables you to publish up to 150 values per metric with one PutMetricData request, and supports retrieving percentile statistics on this data. 
Each PutMetricData request is limited to 40 KB in size for HTTP POST requests. You can send a payload compressed by gzip. Each request is also limited to no more than 20 different metrics. 
Although the Value parameter accepts numbers of type Double, CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported. 
You can use up to 10 dimensions per metric to further clarify what data the metric collects. For more information about specifying dimensions, see Publishing Metrics in the Amazon CloudWatch User Guide. 
Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for GetMetricData or GetMetricStatistics from the time they are submitted. 
CloudWatch needs raw data points to calculate percentile statistics. These raw data points could be published individually or as part of Values and Counts arrays. If you publish data using statistic sets in the StatisticValues field instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:  
 The SampleCount value of the statistic set is 1 and Min, Max, and Sum are all equal.  
 The Min and Max are equal, and Sum is equal to Min multiplied by SampleCount. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Namespace" : "The namespace for the metric data. \nYou cannot specify a namespace that begins with \"AWS/\". Namespaces that begin with \"AWS/\" are reserved for use by Amazon Web Services products.",
  "MetricData" : [ {
    "MetricDatum" : {
      "MetricName" : "The name of the metric.",
      "StatisticValues" : {
        "Minimum" : "The minimum value of the sample set.",
        "Maximum" : "The maximum value of the sample set.",
        "SampleCount" : "The number of samples used for the statistic set.",
        "Sum" : "The sum of values for the sample set."
      },
      "Counts" : [ "number" ],
      "Value" : "The value for the metric. \nAlthough the parameter accepts numbers of type Double, CloudWatch rejects values that are either too small or too large. Values must be in the range of 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2). In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.",
      "Values" : [ "number" ],
      "StorageResolution" : "Valid values are 1 and 60. Setting this to 1 specifies this metric as a high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution down to one second. Setting this to 60 specifies this metric as a regular-resolution metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is available only for custom metrics. For more information about high-resolution metrics, see High-Resolution Metrics in the Amazon CloudWatch User Guide.  \nThis field is optional, if you do not specify it the default of 60 is used.",
      "Dimensions" : [ {
        "Dimension" : {
          "Value" : "The value representing the dimension measurement.",
          "Name" : "The name of the dimension."
        }
      } ],
      "Unit" : "The unit of the metric.",
      "Timestamp" : "The time the metric data was received, expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC."
    }
  } ]
}
```

</details>

## set_alarm_state

Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to ALARM sends an SNS message. The alarm returns to its actual state (often within seconds). Because the alarm state change happens quickly, it is typically only visible in the alarm's History tab in the Amazon CloudWatch console or through DescribeAlarmHistory.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "StateReasonData" : "The reason that this alarm is set to this specific state, in JSON format.",
  "AlarmName" : "The name for the alarm. This name must be unique within the AWS account. The maximum length is 255 characters.",
  "StateReason" : "The reason that this alarm is set to this specific state, in text format.",
  "StateValue" : "The value of the state."
}
```

</details>

