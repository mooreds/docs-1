---
id: aws-cloudwatch-events-documentation
title: AWS Cloudwatch Events (version v1.*.*)
sidebar_label: AWS Cloudwatch Events
layout: docs.mustache
---

## delete_rule

Deletes the specified rule. 
Before you can delete the rule, you must remove all targets, using RemoveTargets. 
When you delete a rule, incoming events might continue to match to the deleted rule. Allow a short period of time for changes to take effect.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Name" : "The name of the rule."
}
```

</details>

## describe_event_bus

Displays the external AWS accounts that are permitted to write events to your account using your account's event bus, and the associated policy. To enable your account to receive events from other accounts, use PutPermission.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## describe_rule

Describes the specified rule. 
DescribeRule does not list the targets of a rule. To see the targets associated with a rule, use ListTargetsByRule.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Name" : "The name of the rule."
}
```

</details>

## disable_rule

Disables the specified rule. A disabled rule won't match any events, and won't self-trigger if it has a schedule expression. 
When you disable a rule, incoming events might continue to match to the disabled rule. Allow a short period of time for changes to take effect.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Name" : "The name of the rule."
}
```

</details>

## enable_rule

Enables the specified rule. If the rule does not exist, the operation fails. 
When you enable a rule, incoming events might not immediately start matching to a newly enabled rule. Allow a short period of time for changes to take effect.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Name" : "The name of the rule."
}
```

</details>

## list_rule_names_by_target

Lists the rules for the specified target. You can see which of the rules in Amazon CloudWatch Events can invoke a specific target in your account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token returned by a previous call to retrieve the next set of results.",
  "TargetArn" : "The Amazon Resource Name (ARN) of the target resource.",
  "Limit" : "The maximum number of results to return."
}
```

</details>

## list_rules

Lists your Amazon CloudWatch Events rules. You can either list all the rules or you can provide a prefix to match to the rule names. 
ListRules does not list the targets of a rule. To see the targets associated with a rule, use ListTargetsByRule.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NamePrefix" : "The prefix matching the rule name.",
  "NextToken" : "The token returned by a previous call to retrieve the next set of results.",
  "Limit" : "The maximum number of results to return."
}
```

</details>

## list_targets_by_rule

Lists the targets assigned to the specified rule.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "The token returned by a previous call to retrieve the next set of results.",
  "Rule" : "The name of the rule.",
  "Limit" : "The maximum number of results to return."
}
```

</details>

## put_events

Sends custom events to Amazon CloudWatch Events so that they can be matched to rules.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Entries" : [ {
    "DetailType" : "Free-form string used to decide what fields to expect in the event detail.",
    "Time" : "The time stamp of the event, per RFC3339. If no time stamp is provided, the time stamp of the PutEvents call is used.",
    "Resources" : [ "string" ],
    "Source" : "The source of the event. This field is required.",
    "Detail" : "A valid JSON string. There is no other schema imposed. The JSON string may contain fields and nested subobjects."
  } ]
}
```

</details>

## put_permission

Running PutPermission permits the specified AWS account to put events to your account's default event bus. CloudWatch Events rules in your account are triggered by these events arriving to your default event bus.  
For another account to send events to your account, that external account must have a CloudWatch Events rule with your account's default event bus as a target. 
To enable multiple AWS accounts to put events to your default event bus, run PutPermission once for each of these accounts. 
The permission policy on the default event bus cannot exceed 10 KB in size.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Action" : "The action that you are enabling the other account to perform. Currently, this must be events:PutEvents.",
  "StatementId" : "An identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this StatementId when you run RemovePermission.",
  "Principal" : "The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify \"*\" to permit any account to put events to your default event bus. \nIf you specify \"*\", avoid creating rules that may match undesirable events. To create more secure rules, make sure that the event pattern for each rule contains an account field with a specific account ID from which to receive events. Rules with an account field do not match any events sent from other accounts."
}
```

</details>

## put_rule

Creates or updates the specified rule. Rules are enabled by default, or based on value of the state. You can disable a rule using DisableRule. 
If you are updating an existing rule, the rule is replaced with what you specify in this PutRule command. If you omit arguments in PutRule, the old values for those arguments are not kept. Instead, they are replaced with null values. 
When you create or update a rule, incoming events might not immediately start matching to new or updated rules. Allow a short period of time for changes to take effect. 
A rule must contain at least an EventPattern or ScheduleExpression. Rules with EventPatterns are triggered when a matching event is observed. Rules with ScheduleExpressions self-trigger based on the given schedule. A rule can have both an EventPattern and a ScheduleExpression, in which case the rule triggers on matching events as well as on a schedule. 
Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, CloudWatch Events uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ScheduleExpression" : "The scheduling expression. For example, \"cron(0 20 * * ? *)\" or \"rate(5 minutes)\".",
  "EventPattern" : "The event pattern. For more information, see Events and Event Patterns in the Amazon CloudWatch Events User Guide.",
  "Description" : "A description of the rule.",
  "State" : "Indicates whether the rule is enabled or disabled.",
  "RoleArn" : "The Amazon Resource Name (ARN) of the IAM role associated with the rule.",
  "Name" : "The name of the rule that you are creating or updating."
}
```

</details>

## put_targets

Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule. 
Targets are the resources that are invoked when a rule is triggered. 
You can configure the following as targets for CloudWatch Events:  
 EC2 instances  
 SSM Run Command  
 SSM Automation  
 AWS Lambda functions  
 Data streams in Amazon Kinesis Data Streams  
 Data delivery streams in Amazon Kinesis Data Firehose  
 Amazon ECS tasks  
 AWS Step Functions state machines  
 AWS Batch jobs  
 AWS CodeBuild projects  
 Pipelines in AWS CodePipeline  
 Amazon Inspector assessment templates  
 Amazon SNS topics  
 Amazon SQS queues, including FIFO queues  
 The default event bus of another AWS account   
Creating rules with built-in targets is supported only in the AWS Management Console. The built-in targets are EC2 CreateSnapshot API call, EC2 RebootInstances API call, EC2 StopInstances API call, and EC2 TerminateInstances API call.  
For some target types, PutTargets provides target-specific parameters. If the target is a Kinesis data stream, you can optionally specify which shard the event goes to by using the KinesisParameters argument. To invoke a command on multiple EC2 instances with one rule, you can use the RunCommandParameters field. 
To be able to make API calls against the resources that you own, Amazon CloudWatch Events needs the appropriate permissions. For AWS Lambda and Amazon SNS resources, CloudWatch Events relies on resource-based policies. For EC2 instances, Kinesis data streams, and AWS Step Functions state machines, CloudWatch Events relies on IAM roles that you specify in the RoleARN argument in PutTargets. For more information, see Authentication and Access Control in the Amazon CloudWatch Events User Guide. 
If another AWS account is in the same region and has granted you permission (using PutPermission), you can send events to that account. Set that account's event bus as a target of the rules in your account. To send the matched events to the other account, specify that account's event bus as the Arn value when you run PutTargets. If your account sends events to another account, your account is charged for each sent event. Each event sent to another account is charged as a custom event. The account receiving the event is not charged. For more information, see Amazon CloudWatch Pricing. 
For more information about enabling cross-account events, see PutPermission. 
 Input, InputPath, and InputTransformer are mutually exclusive and optional parameters of a target. When a rule is triggered due to a matched event:  
 If none of the following arguments are specified for a target, then the entire event is passed to the target in JSON format (unless the target is Amazon EC2 Run Command or Amazon ECS task, in which case nothing from the event is passed to the target).  
 If Input is specified in the form of valid JSON, then the matched event is overridden with this constant.  
 If InputPath is specified in the form of JSONPath (for example, $.detail), then only the part of the event specified in the path is passed to the target (for example, only the detail part of the event is passed).  
 If InputTransformer is specified, then one or more specified JSONPaths are extracted from the event and used as values in a template that you specify as the input to the target.   
When you specify InputPath or InputTransformer, you must use JSON dot notation, not bracket notation. 
When you add targets to a rule and the associated rule triggers soon after, new or updated targets might not be immediately invoked. Allow a short period of time for changes to take effect. 
This action can partially fail if too many requests are made at the same time. If that happens, FailedEntryCount is non-zero in the response and each entry in FailedEntries provides the ID of the failed target and the error code.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Targets" : [ {
    "InputPath" : "The value of the JSONPath that is used for extracting part of the matched event when passing it to the target. You must use JSON dot notation, not bracket notation. For more information about JSON paths, see JSONPath.",
    "Input" : "Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see The JavaScript Object Notation (JSON) Data Interchange Format.",
    "SqsParameters" : {
      "MessageGroupId" : "The FIFO message group ID to use as the target."
    },
    "EcsParameters" : {
      "PlatformVersion" : "Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. \nThis structure is used only if LaunchType is FARGATE. For more information about valid platform versions, see AWS Fargate Platform Versions in the Amazon Elastic Container Service Developer Guide.",
      "Group" : "Specifies an ECS task group for the task. The maximum length is 255 characters.",
      "TaskCount" : "The number of tasks to create based on TaskDefinition. The default is 1.",
      "NetworkConfiguration" : {
        "awsvpcConfiguration" : {
          "SecurityGroups" : [ "string" ],
          "Subnets" : [ "string" ],
          "AssignPublicIp" : "Specifies whether the task's elastic network interface receives a public IP address. You can specify ENABLED only when LaunchType in EcsParameters is set to FARGATE."
        }
      },
      "LaunchType" : "Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The FARGATE value is supported only in the Regions where AWS Fargate with Amazon ECS is supported. For more information, see AWS Fargate on Amazon ECS in the Amazon Elastic Container Service Developer Guide.",
      "TaskDefinitionArn" : "The ARN of the task definition to use if the event target is an Amazon ECS task. "
    },
    "RunCommandParameters" : {
      "RunCommandTargets" : [ {
        "Values" : [ "string" ],
        "Key" : "Can be either tag: tag-key or InstanceIds."
      } ]
    },
    "BatchParameters" : {
      "ArrayProperties" : {
        "Size" : "The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000."
      },
      "JobName" : "The name to use for this execution of the job, if the target is an AWS Batch job.",
      "RetryStrategy" : {
        "Attempts" : "The number of times to attempt to retry, if the job fails. Valid values are 1–10."
      },
      "JobDefinition" : "The ARN or name of the job definition to use if the event target is an AWS Batch job. This job definition must already exist."
    },
    "Id" : "The ID of the target.",
    "Arn" : "The Amazon Resource Name (ARN) of the target.",
    "InputTransformer" : {
      "InputPathsMap" : "Map of JSON paths to be extracted from the event. You can then insert these in the template in InputTemplate to produce the output you want to be sent to the target. \n InputPathsMap is an array key-value pairs, where each value is a valid JSON path. You can have as many as 10 key-value pairs. You must use JSON dot notation, not bracket notation. \nThe keys cannot start with \"AWS.\" ",
      "InputTemplate" : "Input template where you specify placeholders that will be filled with the values of the keys from InputPathsMap to customize the data sent to the target. Enclose each InputPathsMaps value in brackets: &lt;value&gt; The InputTemplate must be valid JSON. \nIf InputTemplate is a JSON object (surrounded by curly braces), the following restrictions apply:  \n The placeholder cannot be used as an object key.  \n Object values cannot include quote marks.   \nThe following example shows the syntax for using InputPathsMap and InputTemplate. \n  \"InputTransformer\":  \n {  \n \"InputPathsMap\": {\"instance\": \"$.detail.instance\",\"status\": \"$.detail.status\"},  \n \"InputTemplate\": \"&lt;instance&gt; is in state &lt;status&gt;\"  \n }  \nTo have the InputTemplate include quote marks within a JSON string, escape each quote marks with a slash, as in the following example: \n  \"InputTransformer\":  \n {  \n \"InputPathsMap\": {\"instance\": \"$.detail.instance\",\"status\": \"$.detail.status\"},  \n \"InputTemplate\": \"&lt;instance&gt; is in state \\\"&lt;status&gt;\\\"\"  \n } "
    },
    "KinesisParameters" : {
      "PartitionKeyPath" : "The JSON path to be extracted from the event and used as the partition key. For more information, see Amazon Kinesis Streams Key Concepts in the Amazon Kinesis Streams Developer Guide."
    },
    "RoleArn" : "The Amazon Resource Name (ARN) of the IAM role to be used for this target when the rule is triggered. If one rule triggers multiple targets, you can use a different IAM role for each target."
  } ],
  "Rule" : "The name of the rule."
}
```

</details>

## remove_permission

Revokes the permission of another AWS account to be able to put events to your default event bus. Specify the account to revoke by the StatementId value that you associated with the account when you granted it permission with PutPermission. You can find the StatementId by using DescribeEventBus.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "StatementId" : "The statement ID corresponding to the account that is no longer allowed to put events to the default event bus."
}
```

</details>

## remove_targets

Removes the specified targets from the specified rule. When the rule is triggered, those targets are no longer be invoked. 
When you remove a target, when the associated rule triggers, removed targets might continue to be invoked. Allow a short period of time for changes to take effect. 
This action can partially fail if too many requests are made at the same time. If that happens, FailedEntryCount is non-zero in the response and each entry in FailedEntries provides the ID of the failed target and the error code.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Ids" : [ "string" ],
  "Rule" : "The name of the rule."
}
```

</details>

## test_event_pattern

Tests whether the specified event pattern matches the provided event. 
Most services in AWS treat : or / as the same character in Amazon Resource Names (ARNs). However, CloudWatch Events uses an exact match in event patterns and rules. Be sure to use the correct ARN characters when creating event patterns so that they match the ARN syntax in the event you want to match.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "EventPattern" : "The event pattern. For more information, see Events and Event Patterns in the Amazon CloudWatch Events User Guide.",
  "Event" : "The event, in JSON format, to test against the event pattern."
}
```

</details>

