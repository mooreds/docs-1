---
id: aws-cloudwatch-events-documentation
title: AWS Cloudwatch Events (version v2.*.*)
sidebar_label: AWS Cloudwatch Events
---

## delete_rule

Deletes the specified rule. https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DeleteRule.html

<details><summary>Parameters</summary>

#### Name (required)

The name of the rule.

**Type:** STRING

#### Force

If this is a managed rule, created by an AWS service on your behalf, you must specify Force as True to delete the rule. This parameter is ignored for rules that are not managed rules. You can check  whether a rule is a managed rule by using DescribeRule or ListRules and checking the  ManagedBy field of the response.

**Type:** OBJECT

</details>

## describe_event_bus



*This operation has no parameters*

## describe_rule

Describes the specified rule. https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DescribeRule.html

<details><summary>Parameters</summary>

#### Name (required)

The name of the rule.

**Type:** STRING

</details>

## disable_rule

Disables the specified rule. A disabled rule won't match any events, and won't self-trigger if it has a schedule expression.  https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_DisableRule.html

<details><summary>Parameters</summary>

#### Name (required)

The name of the rule.

**Type:** STRING

</details>

## enable_rule

Enables the specified rule. If the rule does not exist, the operation fails. https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_EnableRule.html

<details><summary>Parameters</summary>

#### Name (required)

The name of the rule.

**Type:** STRING

</details>

## list_rule_names_by_target

Lists the rules for the specified target. You can see which of the rules in Amazon CloudWatch Events can invoke a specific target in your account.  https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListRuleNamesByTarget.html

<details><summary>Parameters</summary>

#### TargetArn (required)

The Amazon Resource Name (ARN) of the target resource.

**Type:** STRING

</details>

## list_rules

Lists your Amazon CloudWatch Events rules. You can either list all the rules or you can provide a prefix to match to the rule names.  https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListRules.html

<details><summary>Parameters</summary>

#### NamePrefix

The prefix matching the rule name.

**Type:** STRING

</details>

## list_targets_by_rule

Lists the targets assigned to the specified rule. https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_ListTargetsByRule.html

<details><summary>Parameters</summary>

#### Rule (required)

The name of the rule.

**Type:** STRING

</details>

## put_events

Sends custom events to Amazon CloudWatch Events so that they can be matched to rules. https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutEvents.html

<details><summary>Parameters</summary>

#### Entries (required)

The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.

**Type:** ARRAY

</details>

## put_permission

Running PutPermission permits the specified AWS account or AWS organization to put events to your account's default event bus. CloudWatch Events rules in your account are triggered by these events arriving to your default event bus.  https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutPermission.html

<details><summary>Parameters</summary>

#### Action (required)

The action that you are enabling the other account to perform. Currently, this must be events:PutEvents.

**Type:** STRING

#### Principal (required)

The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify "*" to permit any account to put events to your default event bus. If you specify "*" without specifying Condition, avoid creating rules that may match undesirable events. To create  more secure rules, make sure that the event pattern for each rule contains an account  field with a specific account ID from which to receive events. Rules with an account field do not match any events sent from other accounts.

**Type:** STRING

#### StatementId (required)

An identifier string for the external account that you are granting permissions to. If you later want to revoke the permission for this external account, specify this StatementId when you run RemovePermission.

**Type:** STRING

#### Condition

This parameter enables you to limit the permission to accounts that  fulfill a certain condition, such as being a member of a certain AWS organization. For more information about AWS Organizations,  see What Is AWS Organizations in the AWS Organizations User Guide. If you specify Condition with an AWS organization ID, and specify "*" as the value for Principal, you grant permission to all the accounts in the named organization. The Condition is a JSON string which must contain Type, Key, and Value fields.

**Type:** OBJECT

</details>

## put_rule

Creates or updates the specified rule. Rules are enabled by default, or based on value of the state. You can disable a rule using DisableRule.  https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutRule.html

<details><summary>Parameters</summary>

#### Name (required)

The name of the rule that you are creating or updating.

**Type:** STRING

#### Description

A description of the rule.

**Type:** STRING

#### EventPattern

The event pattern. For more information, see Events and Event Patterns in the Amazon CloudWatch Events User Guide.

**Type:** STRING

#### RoleArn

The Amazon Resource Name (ARN) of the IAM role associated with the rule.

**Type:** STRING

#### ScheduleExpression

The scheduling expression. For example, "cron(0 20 * * ? *)" or "rate(5 minutes)".

**Type:** STRING

#### State

Indicates whether the rule is enabled or disabled.

**Type:** STRING

</details>

## put_targets

Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.  https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_PutTargets.html

<details><summary>Parameters</summary>

#### Rule (required)

The name of the rule.

**Type:** STRING

#### Targets (required)

The targets to update or add to the rule.

**Type:** ARRAY

</details>

## remove_permission

Revokes the permission of another AWS account to be able to put events to your default event bus. Specify the account to revoke by the StatementId value that you associated with the account when you granted it permission with PutPermission. You can find the StatementId by using DescribeEventBus.  https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_RemovePermission.html

<details><summary>Parameters</summary>

#### StatementId (required)

The statement ID corresponding to the account that is no longer allowed to put events to the default event bus.

**Type:** STRING

</details>

## remove_targets

Removes the specified targets from the specified rule. When the rule is triggered, those targets are no longer be invoked.  https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_RemoveTargets.html

<details><summary>Parameters</summary>

#### Ids (required)

The IDs of the targets to remove from the rule.

**Type:** ARRAY

#### Rule (required)

The name of the rule.

**Type:** STRING

#### Force

If this is a managed rule, created by an AWS service on your behalf, you must specify Force as True to remove targets. This parameter is ignored for rules that are not managed rules. You can check whether a rule is a managed rule by using DescribeRule or ListRules and checking the ManagedBy field of the response.

**Type:** OBJECT

</details>

## test_event_pattern

Tests whether the specified event pattern matches the provided event. https://docs.aws.amazon.com/AmazonCloudWatchEvents/latest/APIReference/API_TestEventPattern.html

<details><summary>Parameters</summary>

#### Event (required)

The event, in JSON format, to test against the event pattern.

**Type:** STRING

#### EventPattern (required)

The event pattern. For more information, see Events and Event Patterns in the Amazon CloudWatch Events User Guide.

**Type:** STRING

</details>

