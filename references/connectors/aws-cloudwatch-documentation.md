---
id: aws-cloudwatch-documentation
title: AWS Cloudwatch (version v2.*.*)
sidebar_label: AWS Cloudwatch
layout: docs.mustache
---

## delete_alarms

Deletes the specified alarms. In the event of an error, no alarms are deleted.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_dashboards

Deletes all dashboards that you specify. You may specify up to 100 dashboards to delete. If there is an error during this call, no dashboards are deleted.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## describe_alarm_history

Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for all alarms are returned. 
CloudWatch retains the history of an alarm even if you delete the alarm.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## describe_alarms

Retrieves the specified alarms. If no alarms are specified, all alarms are returned. Alarms can be retrieved by using only a prefix for the alarm name, the alarm state, or a prefix for any action.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## describe_alarms_for_metric

Retrieves the alarms for the specified metric. To filter the results, specify a statistic, period, or unit.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## disable_alarm_actions

Disables the actions for the specified alarms. When an alarm's actions are disabled, the alarm actions do not execute when the alarm state changes.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## enable_alarm_actions

Enables the actions for the specified alarms.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_dashboard

Displays the details of the dashboard that you specify. 
To copy an existing dashboard, use GetDashboard, and then use the data returned within DashboardBody as the template for the new dashboard when you call PutDashboard to create the copy.

<details><summary>Parameters</summary>

#### $body

**Type:** object

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

#### $body

**Type:** object

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

#### $body

**Type:** object

</details>

## get_metric_widget_image

You can use the GetMetricWidgetImage API to retrieve a snapshot graph of one or more Amazon CloudWatch metrics as a bitmap image. You can then embed this image into your services and products, such as wiki pages, reports, and documents. You could also retrieve images regularly, such as every minute, and create your own custom live dashboard. 
The graph you retrieve can include all CloudWatch metric graph features, including metric math and horizontal and vertical annotations. 
There is a limit of 20 transactions per second for this API. Each GetMetricWidgetImage action has the following limits:  
 As many as 100 metrics in the graph.  
 Up to 100 KB uncompressed payload. 

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## list_dashboards

Returns a list of the dashboards for your account. If you include DashboardNamePrefix, only those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your account are listed.  
 ListDashboards returns up to 1000 results on one page. If there are more than 1000 dashboards, you can call ListDashboards again and include the value you received for NextToken in the first call, to receive the next 1000 results.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## list_metrics

List the specified metrics. You can use the returned metrics with GetMetricData or GetMetricStatistics to obtain statistical data. 
Up to 500 results are returned for any one call. To retrieve additional results, use the returned token with subsequent calls. 
After you create a metric, allow up to fifteen minutes before the metric appears. Statistics about the metric, however, are available sooner using GetMetricData or GetMetricStatistics.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## put_dashboard

Creates a dashboard if it does not already exist, or updates an existing dashboard. If you update a dashboard, the entire contents are replaced with what you specify here. 
There is no limit to the number of dashboards in your account. All dashboards in your account are global, not region-specific. 
A simple way to create a dashboard using PutDashboard is to copy an existing dashboard. To copy an existing dashboard using the console, you can load the dashboard and then use the View/edit source command in the Actions menu to display the JSON block for that dashboard. Another way to copy a dashboard is to use GetDashboard, and then use the data returned within DashboardBody as the template for the new dashboard when you call PutDashboard. 
When you create a dashboard with PutDashboard, a good practice is to add a text widget at the top of the dashboard with a message that the dashboard was created by script and should not be changed in the console. This message could also point console users to the location of the DashboardBody script or the CloudFormation template used to create the dashboard.

<details><summary>Parameters</summary>

#### $body

**Type:** object

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

#### $body

**Type:** object

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

#### $body

**Type:** object

</details>

## set_alarm_state

Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to ALARM sends an SNS message. The alarm returns to its actual state (often within seconds). Because the alarm state change happens quickly, it is typically only visible in the alarm's History tab in the Amazon CloudWatch console or through DescribeAlarmHistory.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

