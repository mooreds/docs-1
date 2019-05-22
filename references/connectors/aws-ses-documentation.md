---
id: aws-ses-documentation
title: AWS SES (version v2.*.*)
sidebar_label: AWS SES
layout: docs.mustache
---

## clone_receipt_rule_set

Creates a receipt rule set by cloning an existing one. All receipt rules and configurations are copied to the new receipt rule set and are completely independent of the source rule set.  https://docs.aws.amazon.com/ses/latest/APIReference/API_CloneReceiptRuleSet.html

<details><summary>Parameters</summary>

#### OriginalRuleSetName (required)

The name of the rule set to clone.

**Type:** STRING

#### RuleSetName (required)

The name of the rule set to create. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). Start and end with a letter or number. Contain less than 64 characters.

**Type:** STRING

</details>

## create_configuration_set

Creates a configuration set. https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSet.html

<details><summary>Parameters</summary>

#### ConfigurationSet.Name

A data structure that contains the name of the configuration set. The name of the configuration set. The name must meet the following requirements:#Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes#(-).#Contain 64 characters or fewer.

**Type:** STRING

</details>

## create_configuration_set_event_destination

Creates a configuration set event destination. https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSetEventDestination.html

<details><summary>Parameters</summary>

#### ConfigurationSetName (required)

The name of the configuration set that the event destination should be associated with.

**Type:** STRING

#### EventDestination.CloudWatchDestination.DimensionConfigurations.member.N.DefaultDimensionValue

An object that describes the AWS service that email sending event information will be published to. An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination. A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch. The default value of the dimension that is published to Amazon CloudWatch if you do not provide#the value of the dimension when you send an email. The default value must:#This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

#### EventDestination.CloudWatchDestination.DimensionConfigurations.member.N.DimensionName

An object that describes the AWS service that email sending event information will be published to. An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination. A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch. The name of an Amazon CloudWatch dimension associated with an email sending metric. The name#must:#This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

#### EventDestination.CloudWatchDestination.DimensionConfigurations.member.N.DimensionValueSource

An object that describes the AWS service that email sending event information will be published to. An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination. A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch. The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon SES to use the message tags that you specify using an#X-SES-MESSAGE-TAGS header or a parameter to the#SendEmail/SendRawEmail API, choose#messageTag. If you want Amazon SES to use your own email headers, choose#emailHeader. Valid Values: messageTag | emailHeader | linkTag

**Type:** ARRAY

#### EventDestination.Enabled

An object that describes the AWS service that email sending event information will be published to. Sets whether Amazon SES publishes events to this destination when you send an email with#the associated configuration set. Set to true to enable publishing to this#destination; set to false to prevent publishing to this destination. The#default value is false.

**Type:** BOOLEAN

#### EventDestination.KinesisFirehoseDestination.DeliveryStreamARN

An object that describes the AWS service that email sending event information will be published to. An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination. The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.

**Type:** STRING

#### EventDestination.KinesisFirehoseDestination.IAMRoleARN

An object that describes the AWS service that email sending event information will be published to. An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination. The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose#stream.

**Type:** STRING

#### EventDestination.MatchingEventTypes.member

An object that describes the AWS service that email sending event information will be published to. The type of email sending events to publish to the event destination. Valid Values: send | reject | bounce | complaint | delivery | open | click | renderingFailure

**Type:** ARRAY

#### EventDestination.Name

An object that describes the AWS service that email sending event information will be published to. The name of the event destination. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 64 characters.

**Type:** STRING

#### EventDestination.SNSDestination.TopicARN

An object that describes the AWS service that email sending event information will be published to. An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event#destination. The ARN of the Amazon SNS topic that email sending events will be published to. An example#of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For#more information about Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** STRING

</details>

## create_configuration_set_tracking_options

Creates an association between a configuration set and a custom domain for open and click event tracking.  https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSetTrackingOptions.html

<details><summary>Parameters</summary>

#### ConfigurationSetName (required)

The name of the configuration set that the tracking options should be associated with.

**Type:** STRING

#### TrackingOptions.CustomRedirectDomain

A domain that is used to redirect email recipients to an Amazon SES-operated domain. This domain captures open and click events generated by Amazon SES emails. For more information, see Configuring Custom Domains to Handle Open and Click Tracking in the Amazon SES Developer Guide. The custom subdomain that will be used to redirect email recipients to the Amazon SES#event tracking domain.

**Type:** STRING

</details>

## create_custom_verification_email_template

Creates a new custom verification email template. https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateCustomVerificationEmailTemplate.html

<details><summary>Parameters</summary>

#### FailureRedirectionURL (required)

The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.

**Type:** STRING

#### FromEmailAddress (required)

The email address that the custom verification email is sent from.

**Type:** STRING

#### SuccessRedirectionURL (required)

The URL that the recipient of the verification email is sent to if his or her address is successfully verified.

**Type:** STRING

#### TemplateContent (required)

The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see Custom Verification Email Frequently Asked Questions in the Amazon SES Developer Guide.

**Type:** STRING

#### TemplateName (required)

The name of the custom verification email template.

**Type:** STRING

#### TemplateSubject (required)

The subject line of the custom verification email.

**Type:** STRING

</details>

## create_receipt_filter

Creates a new IP address filter. https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptFilter.html

<details><summary>Parameters</summary>

#### Filter.IpFilter.Cidr

A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it. A structure that provides the IP addresses to block or allow, and whether to block or#allow incoming mail from them. A single IP address or a range of IP addresses that you want to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single#email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For#more information about CIDR notation, see RFC 2317.

**Type:** STRING

#### Filter.IpFilter.Policy

A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it. A structure that provides the IP addresses to block or allow, and whether to block or#allow incoming mail from them. Indicates whether to block or allow incoming mail from the specified IP addresses. Valid Values: Block | Allow

**Type:** STRING

#### Filter.Name

A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it. The name of the IP address filter. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Start and end with a letter or number.#Contain less than 64 characters.

**Type:** STRING

</details>

## create_receipt_rule

Creates a receipt rule. https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRule.html

<details><summary>Parameters</summary>

#### RuleSetName (required)

The name of the rule set that the receipt rule will be added to.

**Type:** STRING

#### After

The name of an existing rule after which the new rule will be placed. If this parameter is null, the new rule will be inserted at the beginning of the rule list.

**Type:** STRING

#### Rule.Actions.member.N.AddHeaderAction.HeaderName

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Adds a header to the received email. The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

**Type:** ARRAY

#### Rule.Actions.member.N.AddHeaderAction.HeaderValue

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Adds a header to the received email. Must be less than 2048 characters, and must not contain newline characters ("\r" or "\n").

**Type:** ARRAY

#### Rule.Actions.member.N.BounceAction.Message

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon#SNS). Human-readable text to include in the bounce message.

**Type:** ARRAY

#### Rule.Actions.member.N.BounceAction.Sender

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon#SNS). The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.

**Type:** ARRAY

#### Rule.Actions.member.N.BounceAction.SmtpReplyCode

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon#SNS). The SMTP reply code, as defined by RFC 5321.

**Type:** ARRAY

#### Rule.Actions.member.N.BounceAction.StatusCode

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon#SNS). The SMTP enhanced status code, as defined by RFC 3463.

**Type:** ARRAY

#### Rule.Actions.member.N.BounceAction.TopicArn

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon#SNS). The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is#taken. An example of an Amazon SNS topic ARN is#arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about#Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.LambdaAction.FunctionArn

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS. The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is arn:aws:lambda:us-west-2:account-id:function:MyFunction.#For more information about AWS Lambda, see the AWS Lambda Developer Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.LambdaAction.InvocationType

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS. The invocation type of the AWS Lambda function. An invocation type of RequestResponse means that the execution of the function will immediately result in a response, and a value of Event means that the#function will be invoked asynchronously. The default value is Event. For#information about AWS Lambda invocation types, see the AWS Lambda Developer Guide.#Important#There is a 30-second timeout on RequestResponse invocations. You#should use Event invocation in most cases. Use#RequestResponse only when you want to make a mail flow decision,#such as whether to stop the receipt rule or the receipt rule set. Valid Values: Event | RequestResponse

**Type:** ARRAY

#### Rule.Actions.member.N.LambdaAction.TopicArn

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS. The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is#taken. An example of an Amazon SNS topic ARN is#arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about#Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.S3Action

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a#notification to Amazon SNS.

**Type:** ARRAY

#### Rule.Actions.member.N.SNSAction.Encoding

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Publishes the email content within a notification to Amazon SNS. The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a#different encoding format. Base64 preserves all special characters. The default value#is#UTF-8. Valid Values: UTF-8 | Base64

**Type:** ARRAY

#### Rule.Actions.member.N.SNSAction.TopicArn

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Publishes the email content within a notification to Amazon SNS. The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS#topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more#information about Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.StopAction.Scope

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS. The name of the RuleSet that is being stopped. Valid Values: RuleSet

**Type:** ARRAY

#### Rule.Actions.member.N.StopAction.TopicArn

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS. The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is#taken. An example of an Amazon SNS topic ARN is#arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about#Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.WorkmailAction.OrganizationArn

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS. The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is#arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7.#For information about Amazon WorkMail organizations, see the Amazon WorkMail#Administrator Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.WorkmailAction.TopicArn

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS. The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action#is called. An example of an Amazon SNS topic ARN is#arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about#Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** ARRAY

#### Rule.Enabled

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. If true, the receipt rule is active. The default value is false.

**Type:** BOOLEAN

#### Rule.Name

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. The name of the receipt rule. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Start and end with a letter or number.#Contain less than 64 characters.

**Type:** STRING

#### Rule.Recipients.member

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule will match all recipients under all verified#domains.

**Type:** ARRAY

#### Rule.ScanEnabled

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. If true, then messages that this receipt rule applies to are scanned for spam and viruses. The default value is false.

**Type:** BOOLEAN

#### Rule.TlsPolicy

A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy. Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set#to#Require, Amazon SES will bounce emails that are not received over TLS. The#default is Optional. Valid Values: Require | Optional

**Type:** STRING

</details>

## create_receipt_rule_set

Creates an empty receipt rule set. https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRuleSet.html

<details><summary>Parameters</summary>

#### RuleSetName (required)

The name of the rule set to create. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). Start and end with a letter or number. Contain less than 64 characters.

**Type:** STRING

</details>

## create_template

Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the Amazon SES Developer Guide.  https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateTemplate.html

<details><summary>Parameters</summary>

#### Template.HtmlPart

The content of the email, composed of a subject line, an HTML part, and a text-only part. The HTML body of the email.

**Type:** STRING

#### Template.SubjectPart

The content of the email, composed of a subject line, an HTML part, and a text-only part. The subject line of the email.

**Type:** STRING

#### Template.TemplateName

The content of the email, composed of a subject line, an HTML part, and a text-only part. The name of the template. You will refer to this name when you send email using the SendTemplatedEmail or SendBulkTemplatedEmail#operations.

**Type:** STRING

#### Template.TextPart

The content of the email, composed of a subject line, an HTML part, and a text-only part. The email body that will be visible to recipients whose email clients do not display HTML.

**Type:** STRING

</details>

## delete_configuration_set

Deletes a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.  https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSet.html

<details><summary>Parameters</summary>

#### ConfigurationSetName (required)

The name of the configuration set to delete.

**Type:** STRING

</details>

## delete_configuration_set_event_destination

Deletes a configuration set event destination. Configuration set event destinations are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.  https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSetEventDestination.html

<details><summary>Parameters</summary>

#### ConfigurationSetName (required)

The name of the configuration set from which to delete the event destination.

**Type:** STRING

#### EventDestinationName (required)

The name of the event destination to delete.

**Type:** STRING

</details>

## delete_configuration_set_tracking_options

Deletes an association between a configuration set and a custom domain for open and click event tracking.  https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSetTrackingOptions.html

<details><summary>Parameters</summary>

#### ConfigurationSetName (required)

The name of the configuration set from which you want to delete the tracking options.

**Type:** STRING

</details>

## delete_custom_verification_email_template

Deletes an existing custom verification email template.  https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteCustomVerificationEmailTemplate.html

<details><summary>Parameters</summary>

#### TemplateName (required)

The name of the custom verification email template that you want to delete.

**Type:** STRING

</details>

## delete_identity

Deletes the specified identity (an email address or a domain) from the list of verified identities.  https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentity.html

<details><summary>Parameters</summary>

#### Identity (required)

The identity to be removed from the list of identities for the AWS Account.

**Type:** STRING

</details>

## delete_identity_policy

Deletes the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.  https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentityPolicy.html

<details><summary>Parameters</summary>

#### Identity (required)

The identity that is associated with the policy that you want to delete. You can specify the identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com. To successfully call this API, you must own the identity.

**Type:** STRING

#### PolicyName (required)

The name of the policy to be deleted.

**Type:** STRING

</details>

## delete_receipt_filter

Deletes the specified IP address filter. https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptFilter.html

<details><summary>Parameters</summary>

#### FilterName (required)

The name of the IP address filter to delete.

**Type:** STRING

</details>

## delete_receipt_rule

Deletes the specified receipt rule. https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptRule.html

<details><summary>Parameters</summary>

#### RuleName (required)

The name of the receipt rule to delete.

**Type:** STRING

#### RuleSetName (required)

The name of the receipt rule set that contains the receipt rule to delete.

**Type:** STRING

</details>

## delete_receipt_rule_set

Deletes the specified receipt rule set and all of the receipt rules it contains.  https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptRuleSet.html

<details><summary>Parameters</summary>

#### RuleSetName (required)

The name of the receipt rule set to delete.

**Type:** STRING

</details>

## delete_template

Deletes an email template. https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteTemplate.html

<details><summary>Parameters</summary>

#### TemplateName (required)

The name of the template to be deleted.

**Type:** STRING

</details>

## delete_verified_email_address

Deprecated. Use the DeleteIdentity operation to delete email addresses and domains.  https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteVerifiedEmailAddress.html

<details><summary>Parameters</summary>

#### EmailAddress (required)

An email address to be removed from the list of verified addresses.

**Type:** STRING

</details>

## describe_active_receipt_rule_set



*This operation has no parameters*

## describe_configuration_set

Returns the details of the specified configuration set. For information about using configuration sets, see the Amazon SES Developer Guide.  https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeConfigurationSet.html

<details><summary>Parameters</summary>

#### ConfigurationSetName (required)

The name of the configuration set to describe.

**Type:** STRING

#### ConfigurationSetAttributeNames.member.N

A list of configuration set attributes to return.

**Type:** ARRAY

</details>

## describe_receipt_rule

Returns the details of the specified receipt rule. https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRule.html

<details><summary>Parameters</summary>

#### RuleName (required)

The name of the receipt rule.

**Type:** STRING

#### RuleSetName (required)

The name of the receipt rule set that the receipt rule belongs to.

**Type:** STRING

</details>

## describe_receipt_rule_set

Returns the details of the specified receipt rule set. https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRuleSet.html

<details><summary>Parameters</summary>

#### RuleSetName (required)

The name of the receipt rule set to describe.

**Type:** STRING

</details>

## get_account_sending_enabled



*This operation has no parameters*

## get_custom_verification_email_template

Returns the custom email verification template for the template name you specify.  https://docs.aws.amazon.com/ses/latest/APIReference/API_GetCustomVerificationEmailTemplate.html

<details><summary>Parameters</summary>

#### TemplateName (required)

The name of the custom verification email template that you want to retrieve.

**Type:** STRING

</details>

## get_identity_dkim_attributes

Returns the current status of Easy DKIM signing for an entity. For domain name identities, this operation also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES has successfully verified that these tokens have been published.  https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityDkimAttributes.html

<details><summary>Parameters</summary>

#### Identities.member.N (required)

A list of one or more verified identities - email addresses, domains, or both.

**Type:** ARRAY

</details>

## get_identity_mail_from_domain_attributes

Returns the custom MAIL FROM attributes for a list of identities (email addresses : domains).  https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityMailFromDomainAttributes.html

<details><summary>Parameters</summary>

#### Identities.member.N (required)

A list of one or more identities.

**Type:** ARRAY

</details>

## get_identity_notification_attributes

Given a list of verified identities (email addresses and/or domains), returns a structure describing identity notification attributes.  https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityNotificationAttributes.html

<details><summary>Parameters</summary>

#### Identities.member.N (required)

A list of one or more identities. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com.

**Type:** ARRAY

</details>

## get_identity_policies

Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.  https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityPolicies.html

<details><summary>Parameters</summary>

#### Identity (required)

The identity for which the policies will be retrieved. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com. To successfully call this API, you must own the identity.

**Type:** STRING

#### PolicyNames.member.N (required)

A list of the names of policies to be retrieved. You can retrieve a maximum of 20 policies at a time. If you do not know the names of the policies that are attached to the identity, you can use ListIdentityPolicies.

**Type:** ARRAY

</details>

## get_identity_verification_attributes

Given a list of identities (email addresses and/or domains), returns the verification status and (for domain identities) the verification token for each identity.  https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityVerificationAttributes.html

<details><summary>Parameters</summary>

#### Identities.member.N (required)

A list of identities.

**Type:** ARRAY

</details>

## get_send_quota



*This operation has no parameters*

## get_send_statistics



*This operation has no parameters*

## get_template

Displays the template object (which includes the Subject line, HTML part and text part) for the template you specify.  https://docs.aws.amazon.com/ses/latest/APIReference/API_GetTemplate.html

<details><summary>Parameters</summary>

#### TemplateName (required)

The name of the template you want to retrieve.

**Type:** STRING

</details>

## list_configuration_sets

Provides a list of the configuration sets associated with your Amazon SES account in the current AWS Region. For information about using configuration sets, see Monitoring Your Amazon SES Sending Activity in the Amazon SES Developer Guide.  https://docs.aws.amazon.com/ses/latest/APIReference/API_ListConfigurationSets.html

*This operation has no parameters*

## list_custom_verification_email_templates

Lists the existing custom verification email templates for your account in the current AWS Region.  https://docs.aws.amazon.com/ses/latest/APIReference/API_ListCustomVerificationEmailTemplates.html

*This operation has no parameters*

## list_identities

Returns a list containing all of the identities (email addresses and domains) for your AWS account in the current AWS Region, regardless of verification status.  https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentities.html

<details><summary>Parameters</summary>

#### IdentityType

The type of the identities to list. Possible values are "EmailAddress" and "Domain". If this parameter is omitted, then all identities will be listed.

**Type:** STRING

</details>

## list_identity_policies

Returns a list of sending authorization policies that are attached to the given identity (an email address or a domain). This API returns only a list. If you want the actual policy content, you can use GetIdentityPolicies.  https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentityPolicies.html

<details><summary>Parameters</summary>

#### Identity (required)

The identity that is associated with the policy for which the policies will be listed. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com. To successfully call this API, you must own the identity.

**Type:** STRING

</details>

## list_receipt_filters



*This operation has no parameters*

## list_receipt_rule_sets

Lists the receipt rule sets that exist under your AWS account in the current AWS Region. If there are additional receipt rule sets to be retrieved, you will receive a NextToken that you can provide to the next call to ListReceiptRuleSets to retrieve the additional entries.  https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptRuleSets.html

*This operation has no parameters*

## list_templates

Lists the email templates present in your Amazon SES account in the current AWS Region.  https://docs.aws.amazon.com/ses/latest/APIReference/API_ListTemplates.html

*This operation has no parameters*

## list_verified_email_addresses



*This operation has no parameters*

## put_identity_policy

Adds or updates a sending authorization policy for the specified identity (an email address or a domain).  https://docs.aws.amazon.com/ses/latest/APIReference/API_PutIdentityPolicy.html

<details><summary>Parameters</summary>

#### Identity (required)

The identity that the policy will apply to. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com. To successfully call this API, you must own the identity.

**Type:** STRING

#### Policy (required)

The text of the policy in JSON format. The policy cannot exceed 4 KB. For information about the syntax of sending authorization policies, see the Amazon SES Developer Guide.

**Type:** STRING

#### PolicyName (required)

The name of the policy. The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.

**Type:** STRING

</details>

## reorder_receipt_rule_set

Reorders the receipt rules within a receipt rule set. https://docs.aws.amazon.com/ses/latest/APIReference/API_ReorderReceiptRuleSet.html

<details><summary>Parameters</summary>

#### RuleNames.member.N (required)

A list of the specified receipt rule set's receipt rules in the order that you want to put them.

**Type:** ARRAY

#### RuleSetName (required)

The name of the receipt rule set to reorder.

**Type:** STRING

</details>

## send_bounce

Generates and sends a bounce message to the sender of an email you received through Amazon SES. You can only use this API on an email up to 24 hours after you receive it.  https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBounce.html

<details><summary>Parameters</summary>

#### BounceSender (required)

The address to use in the "From" header of the bounce message. This must be an identity that you have verified with Amazon SES.

**Type:** STRING

#### OriginalMessageId (required)

The message ID of the message to be bounced.

**Type:** STRING

#### BounceSenderArn

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the address in the "From" header of the bounce. For more information about sending authorization, see the Amazon SES Developer Guide.

**Type:** STRING

#### BouncedRecipientInfoList.member.N.BounceType

A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list. The reason for the bounce. You must provide either this parameter or RecipientDsnFields. Valid Values: DoesNotExist | MessageTooLarge | ExceededQuota | ContentRejected | Undefined | TemporaryFailure

**Type:** ARRAY

#### BouncedRecipientInfoList.member.N.Recipient

A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list. The email address of the recipient of the bounced email.

**Type:** ARRAY

#### BouncedRecipientInfoList.member.N.RecipientArn

A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list. This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to receive#email for the recipient of the bounced email. For more information about sending#authorization, see the Amazon SES Developer#Guide.

**Type:** ARRAY

#### BouncedRecipientInfoList.member.N.RecipientDsnFields.Action

A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list. Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a BounceType. You must provide either this parameter or#BounceType. The action performed by the reporting mail transfer agent (MTA) as a result of its attempt to deliver the message to the recipient address. This is required by RFC 3464. Valid Values: failed | delayed | delivered | relayed | expanded

**Type:** ARRAY

#### BouncedRecipientInfoList.member.N.RecipientDsnFields.DiagnosticCode

A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list. Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a BounceType. You must provide either this parameter or#BounceType. An extended explanation of what went wrong; this is usually an SMTP response. See RFC 3463 for the correct#formatting of this parameter.

**Type:** ARRAY

#### BouncedRecipientInfoList.member.N.RecipientDsnFields.FinalRecipient

A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list. Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a BounceType. You must provide either this parameter or#BounceType. The email address that the message was ultimately delivered to. This corresponds to the Final-Recipient in the DSN. If not specified,#FinalRecipient will be set to the Recipient specified in#the BouncedRecipientInfo structure. Either FinalRecipient or#the recipient in BouncedRecipientInfo must be a recipient of the original#bounced message.#Note#Do not prepend the FinalRecipient email address with rfc#822;, as described in RFC 3798.

**Type:** ARRAY

#### BouncedRecipientInfoList.member.N.RecipientDsnFields.LastAttemptDate

A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list. Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a BounceType. You must provide either this parameter or#BounceType. The time the final delivery attempt was made, in RFC 822 date-time format.

**Type:** ARRAY

#### BouncedRecipientInfoList.member.N.RecipientDsnFields.RemoteMta

A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list. Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a BounceType. You must provide either this parameter or#BounceType. The MTA to which the remote MTA attempted to deliver the message, formatted as specified in RFC 3464#(mta-name-type; mta-name). This parameter typically applies only to#propagating synchronous bounces.

**Type:** ARRAY

#### BouncedRecipientInfoList.member.N.RecipientDsnFields.Status

A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one BouncedRecipientInfo in the list. Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a BounceType. You must provide either this parameter or#BounceType. The status code that indicates what went wrong. This is required by RFC 3464.

**Type:** ARRAY

#### Explanation

Human-readable text for the bounce message to explain the failure. If not specified, the text will be auto-generated based on the bounced recipient information.

**Type:** STRING

#### MessageDsn.ArrivalDate

Message-related DSN fields. If not specified, Amazon SES will choose the values. When the message was received by the reporting mail transfer agent (MTA), in RFC 822 date-time format.

**Type:** STRING

#### MessageDsn.ExtensionFields.member.N.Name

Message-related DSN fields. If not specified, Amazon SES will choose the values. Additional X-headers to include in the DSN. The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

**Type:** ARRAY

#### MessageDsn.ExtensionFields.member.N.Value

Message-related DSN fields. If not specified, Amazon SES will choose the values. Additional X-headers to include in the DSN. The value of the header to add. Must be less than 2048 characters, and must not contain newline characters ("\r" or "\n").

**Type:** ARRAY

#### MessageDsn.ReportingMta

Message-related DSN fields. If not specified, Amazon SES will choose the values. The reporting MTA that attempted to deliver the message, formatted as specified in RFC 3464#(mta-name-type; mta-name). The default value is dns;#inbound-smtp.[region].amazonaws.com.

**Type:** STRING

</details>

## send_bulk_templated_email

Composes an email message to multiple destinations. The message body is created using an email template.  https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBulkTemplatedEmail.html

<details><summary>Parameters</summary>

#### Source (required)

The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide. If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide. Note Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531. For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters. If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492. The sender name (also known as the friendly name) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047. MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?=.

**Type:** STRING

#### Template (required)

The template to use when sending this email.

**Type:** STRING

#### ConfigurationSetName

The name of the configuration set to use when you send an email using SendBulkTemplatedEmail.

**Type:** STRING

#### DefaultTags.member.N.Name

A list of tags, in the form of name/value pairs, to apply to an email that you send to a destination using SendBulkTemplatedEmail. The name of the tag. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

#### DefaultTags.member.N.Value

A list of tags, in the form of name/value pairs, to apply to an email that you send to a destination using SendBulkTemplatedEmail. The value of the tag. The value must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

#### DefaultTemplateData

A list of replacement values to apply to the template when replacement data is not specified in a Destination object. These values act as a default or fallback option when no other data is available. The template data is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

**Type:** STRING

#### Destinations.member.N.Destination.BccAddresses.member.1

The BCC: field(s) of the message.

**Type:** ARRAY

#### Destinations.member.N.Destination.CcAddresses.member.1

The CC: field(s) of the message.

**Type:** ARRAY

#### Destinations.member.N.Destination.ToAddresses.member.1

The To: field(s) of the message.

**Type:** ARRAY

#### Destinations.member.N.ReplacementTags.member.1.Name

The name of the tag. This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). Contains less than 256 characters.

**Type:** ARRAY

#### Destinations.member.N.ReplacementTags.member.1.Value

The value of the tag. This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). Contains less than 256 characters.

**Type:** ARRAY

#### Destinations.member.N.ReplacementTemplateData

A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template. Length Constraints: Maximum length of 262144.

**Type:** ARRAY

#### ReplyToAddresses.member.N

The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.

**Type:** ARRAY

#### ReturnPath

The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

**Type:** STRING

#### ReturnPathArn

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter. For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the ReturnPath to be feedback@example.com. For more information about sending authorization, see the Amazon SES Developer Guide.

**Type:** STRING

#### SourceArn

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter. For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to send from user@example.com, then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the Source to be user@example.com. For more information about sending authorization, see the Amazon SES Developer Guide.

**Type:** STRING

#### TemplateArn

The ARN of the template to use when sending this email.

**Type:** STRING

</details>

## send_custom_verification_email

Adds an email address to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address.  https://docs.aws.amazon.com/ses/latest/APIReference/API_SendCustomVerificationEmail.html

<details><summary>Parameters</summary>

#### EmailAddress (required)

The email address to verify.

**Type:** STRING

#### TemplateName (required)

The name of the custom verification email template to use when sending the verification email.

**Type:** STRING

#### ConfigurationSetName

Name of a configuration set to use when sending the verification email.

**Type:** STRING

</details>

## send_email

Composes an email message and immediately queues it for sending. In order to send email using the SendEmail operation, your message must meet the following requirements:  https://docs.aws.amazon.com/ses/latest/APIReference/API_SendEmail.html

<details><summary>Parameters</summary>

#### Source (required)

The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide. If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide. Note Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531. For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters. If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492. The sender name (also known as the friendly name) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047. MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?=.

**Type:** STRING

#### ConfigurationSetName

The name of the configuration set to use when you send an email using SendEmail.

**Type:** STRING

#### Destination.BccAddresses.member

The destination for this email, composed of To:, CC:, and BCC: fields. The BCC: field(s) of the message.

**Type:** ARRAY

#### Destination.CcAddresses.member

The destination for this email, composed of To:, CC:, and BCC: fields. The CC: field(s) of the message.

**Type:** ARRAY

#### Destination.ToAddresses.member

The destination for this email, composed of To:, CC:, and BCC: fields. The To: field(s) of the message.

**Type:** ARRAY

#### Message.Body.Html.Charset

The message to be sent. The message body. The content of the message, in HTML format. Use this for email clients that can process HTML. You can include clickable links, formatted text, and much more in an#HTML#message. The character set of the content.

**Type:** STRING

#### Message.Body.Html.Data

The message to be sent. The message body. The content of the message, in HTML format. Use this for email clients that can process HTML. You can include clickable links, formatted text, and much more in an#HTML#message. The textual data of the content.

**Type:** STRING

#### Message.Body.Text.Charset

The message to be sent. The message body. The content of the message, in text format. Use this for text-based email clients, or#clients on high-latency networks (such as mobile devices). The character set of the content.

**Type:** STRING

#### Message.Body.Text.Data

The message to be sent. The message body. The content of the message, in text format. Use this for text-based email clients, or#clients on high-latency networks (such as mobile devices). The textual data of the content.

**Type:** STRING

#### Message.Subject.Charset

The message to be sent. The subject of the message: A short summary of the content, which will appear in the recipient's inbox. The character set of the content.

**Type:** STRING

#### Message.Subject.Data

The message to be sent. The subject of the message: A short summary of the content, which will appear in the recipient's inbox. The textual data of the content.

**Type:** STRING

#### ReplyToAddresses.member.N

The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.

**Type:** ARRAY

#### ReturnPath

The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

**Type:** STRING

#### ReturnPathArn

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter. For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the ReturnPath to be feedback@example.com. For more information about sending authorization, see the Amazon SES Developer Guide.

**Type:** STRING

#### SourceArn

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter. For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to send from user@example.com, then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the Source to be user@example.com. For more information about sending authorization, see the Amazon SES Developer Guide.

**Type:** STRING

#### Tags.member.N.Name

A list of tags, in the form of name/value pairs, to apply to an email that you send using SendEmail. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. The name of the tag. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

#### Tags.member.N.Value

A list of tags, in the form of name/value pairs, to apply to an email that you send using SendEmail. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. The value of the tag. The value must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

</details>

## send_raw_email

Composes an email message and immediately queues it for sending. https://docs.aws.amazon.com/ses/latest/APIReference/API_SendRawEmail.html

<details><summary>Parameters</summary>

#### ConfigurationSetName

The name of the configuration set to use when you send an email using SendRawEmail.

**Type:** STRING

#### Destinations.member.N

A list of destinations for the message, consisting of To:, CC:, and BCC: addresses.

**Type:** ARRAY

#### FromArn

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to specify a particular "From" address in the header of the raw email. Instead of using this parameter, you can use the X-header X-SES-FROM-ARN in the raw message of the email. If you use both the FromArn parameter and the corresponding X-header, Amazon SES uses the value of the FromArn parameter. Note For information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide.

**Type:** STRING

#### RawMessage.Data

The raw email message itself. The message has to meet the following criteria: The message has to contain a header and a body, separated by a blank line. All of the required header fields must be present in the message. Each part of a multipart MIME message must be formatted properly. Attachments must be of a content type that Amazon SES supports. For a list on unsupported content types, see Unsupported Attachment Types in the Amazon SES Developer Guide. The entire message must be base64-encoded. If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, we highly recommend that you encode that content. For more information, see Sending Raw Email in the Amazon SES Developer Guide. Per RFC 5321, the maximum length of each line of text, including the <CRLF>, must not exceed 1,000 characters. The raw data of the message. This data needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using#an AWS#SDK, the SDK takes care of the base 64-encoding for you. In all cases, the client#must#ensure that the message format complies with Internet email standards regarding email#header fields, MIME types, and MIME encoding.#The To:, CC:, and BCC: headers in the raw message can contain a group list.#If you are using SendRawEmail with sending authorization, you can include#X-headers in the raw message to specify the "Source," "From," and "Return-Path"#addresses. For more information, see the documentation for SendRawEmail. #Important#Do not include these X-headers in the DKIM signature, because they are removed by#Amazon SES before sending the email.#For more information, go to the Amazon SES Developer#Guide.

**Type:** OBJECT

#### ReturnPathArn

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter. For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the ReturnPath to be feedback@example.com. Instead of using this parameter, you can use the X-header X-SES-RETURN-PATH-ARN in the raw message of the email. If you use both the ReturnPathArn parameter and the corresponding X-header, Amazon SES uses the value of the ReturnPathArn parameter. Note For information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide.

**Type:** STRING

#### Source

The identity's email address. If you do not provide a value for this parameter, you must specify a "From" address in the raw text of the message. (You can also specify both.) Note Amazon SES does not support the SMTPUTF8 extension, as described inRFC6531. For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters. If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492. The sender name (also known as the friendly name) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047. MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?=. If you specify the Source parameter and have feedback forwarding enabled, then bounces and complaints will be sent to this email address. This takes precedence over any Return-Path header that you might include in the raw text of the message.

**Type:** STRING

#### SourceArn

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter. For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to send from user@example.com, then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the Source to be user@example.com. Instead of using this parameter, you can use the X-header X-SES-SOURCE-ARN in the raw message of the email. If you use both the SourceArn parameter and the corresponding X-header, Amazon SES uses the value of the SourceArn parameter. Note For information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide.

**Type:** STRING

#### Tags.member.N.Name

A list of tags, in the form of name/value pairs, to apply to an email that you send using SendRawEmail. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. The name of the tag. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

#### Tags.member.N.Value

A list of tags, in the form of name/value pairs, to apply to an email that you send using SendRawEmail. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. The value of the tag. The value must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

</details>

## send_templated_email

Composes an email message using an email template and immediately queues it for sending.  https://docs.aws.amazon.com/ses/latest/APIReference/API_SendTemplatedEmail.html

<details><summary>Parameters</summary>

#### Source (required)

The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide. If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide. Note Amazon SES does not support the SMTPUTF8 extension, as described in RFC6531. For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters. If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492. The sender name (also known as the friendly name) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described inRFC 2047. MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?=.

**Type:** STRING

#### Template (required)

The template to use when sending this email.

**Type:** STRING

#### TemplateData (required)

A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

**Type:** STRING

#### ConfigurationSetName

The name of the configuration set to use when you send an email using SendTemplatedEmail.

**Type:** STRING

#### Destination.BccAddresses.member

The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields. The BCC: field(s) of the message.

**Type:** ARRAY

#### Destination.CcAddresses.member

The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields. The CC: field(s) of the message.

**Type:** ARRAY

#### Destination.ToAddresses.member

The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields. The To: field(s) of the message.

**Type:** ARRAY

#### ReplyToAddresses.member.N

The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address will receive the reply.

**Type:** ARRAY

#### ReturnPath

The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

**Type:** STRING

#### ReturnPathArn

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter. For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the ReturnPath to be feedback@example.com. For more information about sending authorization, see the Amazon SES Developer Guide.

**Type:** STRING

#### SourceArn

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter. For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to send from user@example.com, then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the Source to be user@example.com. For more information about sending authorization, see the Amazon SES Developer Guide.

**Type:** STRING

#### Tags.member.N.Name

A list of tags, in the form of name/value pairs, to apply to an email that you send using SendTemplatedEmail. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. The name of the tag. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

#### Tags.member.N.Value

A list of tags, in the form of name/value pairs, to apply to an email that you send using SendTemplatedEmail. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. The value of the tag. The value must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

#### TemplateArn

The ARN of the template to use when sending this email.

**Type:** STRING

</details>

## set_active_receipt_rule_set

Sets the specified receipt rule set as the active receipt rule set. https://docs.aws.amazon.com/ses/latest/APIReference/API_SetActiveReceiptRuleSet.html

<details><summary>Parameters</summary>

#### RuleSetName

The name of the receipt rule set to make active. Setting this value to null disables all email receiving.

**Type:** STRING

</details>

## set_identity_dkim_enabled

Enables or disables Easy DKIM signing of email sent from an identity: https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityDkimEnabled.html

<details><summary>Parameters</summary>

#### DkimEnabled (required)

Sets whether DKIM signing is enabled for an identity. Set to true to enable DKIM signing for this identity; false to disable it.

**Type:** BOOLEAN

#### Identity (required)

The identity for which DKIM signing should be enabled or disabled.

**Type:** STRING

</details>

## set_identity_feedback_forwarding_enabled

Given an identity (an email address or a domain), enables or disables whether Amazon SES forwards bounce and complaint notifications as email. Feedback forwarding can only be disabled when Amazon Simple Notification Service (Amazon SNS) topics are specified for both bounces and complaints.  https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityFeedbackForwardingEnabled.html

<details><summary>Parameters</summary>

#### ForwardingEnabled (required)

Sets whether Amazon SES will forward bounce and complaint notifications as email. true specifies that Amazon SES will forward bounce and complaint notifications as email, in addition to any Amazon SNS topic publishing otherwise specified. false specifies that Amazon SES will publish bounce and complaint notifications only through Amazon SNS. This value can only be set to false when Amazon SNS topics are set for both Bounce and Complaint notification types.

**Type:** BOOLEAN

#### Identity (required)

The identity for which to set bounce and complaint notification forwarding. Examples: user@example.com, example.com.

**Type:** STRING

</details>

## set_identity_headers_in_notifications_enabled

Given an identity (an email address or a domain), sets whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type.  https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityHeadersInNotificationsEnabled.html

<details><summary>Parameters</summary>

#### Enabled (required)

Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of true specifies that Amazon SES will include headers in notifications, and a value of false specifies that Amazon SES will not include headers in notifications. This value can only be set when NotificationType is already set to use a particular Amazon SNS topic.

**Type:** BOOLEAN

#### Identity (required)

The identity for which to enable or disable headers in notifications. Examples: user@example.com, example.com.

**Type:** STRING

#### NotificationType (required)

The notification type for which to enable or disable headers in notifications.

**Type:** STRING

</details>

## set_identity_mail_from_domain

Enables or disables the custom MAIL FROM domain setup for a verified identity (an email address or a domain).  https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html

<details><summary>Parameters</summary>

#### Identity (required)

The verified identity for which you want to enable or disable the specified custom MAIL FROM domain.

**Type:** STRING

#### BehaviorOnMXFailure

The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. If you choose UseDefaultValue, Amazon SES will use amazonses.com (or a subdomain of that) as the MAIL FROM domain. If you choose RejectMessage, Amazon SES will return a MailFromDomainNotVerified error and not send the email. The action specified in BehaviorOnMXFailure is taken when the custom MAIL FROM domain setup is in the Pending, Failed, and TemporaryFailure states.

**Type:** STRING

#### MailFromDomain

The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must 1) be a subdomain of the verified identity, 2) not be used in a "From" address if the MAIL FROM domain is the destination of email feedback forwarding (for more information, see the Amazon SES Developer Guide), and 3) not be used to receive emails. A value of null disables the custom MAIL FROM setting for the identity.

**Type:** STRING

</details>

## set_identity_notification_topic

Sets an Amazon Simple Notification Service (Amazon SNS) topic to use when delivering notifications. When you use this operation, you specify a verified identity, such as an email address or domain. When you send an email that uses the chosen identity in the Source field, Amazon SES sends notifications to the topic you specified. You can send bounce, complaint, or delivery notifications (or any combination of the three) to the Amazon SNS topic that you specify.  https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityNotificationTopic.html

<details><summary>Parameters</summary>

#### Identity (required)

The identity (email address or domain) that you want to set the Amazon SNS topic for. Important You can only specify a verified identity for this parameter. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). The following examples are all valid identities: sender@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com.

**Type:** STRING

#### NotificationType (required)

The type of notifications that will be published to the specified Amazon SNS topic.

**Type:** STRING

#### SnsTopic

The Amazon Resource Name (ARN) of the Amazon SNS topic. If the parameter is omitted from the request or a null value is passed, SnsTopic is cleared and publishing is disabled.

**Type:** STRING

</details>

## set_receipt_rule_position

Sets the position of the specified receipt rule in the receipt rule set. https://docs.aws.amazon.com/ses/latest/APIReference/API_SetReceiptRulePosition.html

<details><summary>Parameters</summary>

#### RuleName (required)

The name of the receipt rule to reposition.

**Type:** STRING

#### RuleSetName (required)

The name of the receipt rule set that contains the receipt rule to reposition.

**Type:** STRING

#### After

The name of the receipt rule after which to place the specified receipt rule.

**Type:** STRING

</details>

## test_render_template

Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.  https://docs.aws.amazon.com/ses/latest/APIReference/API_TestRenderTemplate.html

<details><summary>Parameters</summary>

#### TemplateData (required)

A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

**Type:** STRING

#### TemplateName (required)

The name of the template that you want to render.

**Type:** STRING

</details>

## update_account_sending_enabled

Enables or disables email sending across your entire Amazon SES account in the current AWS Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending across your Amazon SES account in a given AWS Region when reputation metrics (such as your bounce or complaint rates) reach certain thresholds.  https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateAccountSendingEnabled.html

<details><summary>Parameters</summary>

#### Enabled

Describes whether email sending is enabled or disabled for your Amazon SES account in the current AWS Region.

**Type:** BOOLEAN

</details>

## update_configuration_set_event_destination

Updates the event destination of a configuration set. Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see Monitoring Your Amazon SES Sending Activity in the Amazon SES Developer Guide.  https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetEventDestination.html

<details><summary>Parameters</summary>

#### ConfigurationSetName (required)

The name of the configuration set that contains the event destination that you want to update.

**Type:** STRING

#### EventDestination.CloudWatchDestination.DimensionConfigurations.member.N.DefaultDimensionValue

The event destination object that you want to apply to the specified configuration set. An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination. A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch. The default value of the dimension that is published to Amazon CloudWatch if you do not provide#the value of the dimension when you send an email. The default value must:#This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

#### EventDestination.CloudWatchDestination.DimensionConfigurations.member.N.DimensionName

The event destination object that you want to apply to the specified configuration set. An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination. A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch. The name of an Amazon CloudWatch dimension associated with an email sending metric. The name#must:#This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 256 characters.

**Type:** ARRAY

#### EventDestination.CloudWatchDestination.DimensionConfigurations.member.N.DimensionValueSource

The event destination object that you want to apply to the specified configuration set. An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination. A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch. The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon SES to use the message tags that you specify using an#X-SES-MESSAGE-TAGS header or a parameter to the#SendEmail/SendRawEmail API, choose#messageTag. If you want Amazon SES to use your own email headers, choose#emailHeader. Valid Values: messageTag | emailHeader | linkTag

**Type:** ARRAY

#### EventDestination.Enabled

The event destination object that you want to apply to the specified configuration set. Sets whether Amazon SES publishes events to this destination when you send an email with#the associated configuration set. Set to true to enable publishing to this#destination; set to false to prevent publishing to this destination. The#default value is false.

**Type:** BOOLEAN

#### EventDestination.KinesisFirehoseDestination.DeliveryStreamARN

The event destination object that you want to apply to the specified configuration set. An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination. The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.

**Type:** STRING

#### EventDestination.KinesisFirehoseDestination.IAMRoleARN

The event destination object that you want to apply to the specified configuration set. An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination. The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose#stream.

**Type:** STRING

#### EventDestination.MatchingEventTypes.member

The event destination object that you want to apply to the specified configuration set. The type of email sending events to publish to the event destination. Valid Values: send | reject | bounce | complaint | delivery | open | click | renderingFailure

**Type:** ARRAY

#### EventDestination.Name

The event destination object that you want to apply to the specified configuration set. The name of the event destination. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Contain less than 64 characters.

**Type:** STRING

#### EventDestination.SNSDestination.TopicARN

The event destination object that you want to apply to the specified configuration set. An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event#destination. The ARN of the Amazon SNS topic that email sending events will be published to. An example#of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For#more information about Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** STRING

</details>

## update_configuration_set_reputation_metrics_enabled

Enables or disables the publishing of reputation metrics for emails sent using a specific configuration set in a given AWS Region. Reputation metrics include bounce and complaint rates. These metrics are published to Amazon CloudWatch. By using CloudWatch, you can create alarms when bounce or complaint rates exceed certain thresholds.  https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetReputationMetricsEnabled.html

<details><summary>Parameters</summary>

#### ConfigurationSetName (required)

The name of the configuration set that you want to update.

**Type:** STRING

#### Enabled (required)

Describes whether or not Amazon SES will publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.

**Type:** BOOLEAN

</details>

## update_configuration_set_sending_enabled

Enables or disables email sending for messages sent using a specific configuration set in a given AWS Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending for a configuration set when the reputation metrics for that configuration set (such as your bounce on complaint rate) exceed certain thresholds.  https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetSendingEnabled.html

<details><summary>Parameters</summary>

#### ConfigurationSetName (required)

The name of the configuration set that you want to update.

**Type:** STRING

#### Enabled (required)

Describes whether email sending is enabled or disabled for the configuration set.

**Type:** BOOLEAN

</details>

## update_configuration_set_tracking_options

Modifies an association between a configuration set and a custom domain for open and click event tracking.  https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetTrackingOptions.html

<details><summary>Parameters</summary>

#### ConfigurationSetName (required)

The name of the configuration set for which you want to update the custom tracking domain.

**Type:** STRING

#### TrackingOptions.CustomRedirectDomain

A domain that is used to redirect email recipients to an Amazon SES-operated domain. This domain captures open and click events generated by Amazon SES emails. For more information, see Configuring Custom Domains to Handle Open and Click Tracking in the Amazon SES Developer Guide. The custom subdomain that will be used to redirect email recipients to the Amazon SES#event tracking domain.

**Type:** STRING

</details>

## update_custom_verification_email_template

Updates an existing custom verification email template. https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateCustomVerificationEmailTemplate.html

<details><summary>Parameters</summary>

#### TemplateName (required)

The name of the custom verification email template that you want to update.

**Type:** STRING

#### FailureRedirectionURL

The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.

**Type:** STRING

#### FromEmailAddress

The email address that the custom verification email is sent from.

**Type:** STRING

#### SuccessRedirectionURL

The URL that the recipient of the verification email is sent to if his or her address is successfully verified.

**Type:** STRING

#### TemplateContent

The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see Custom Verification Email Frequently Asked Questions in the Amazon SES Developer Guide.

**Type:** STRING

#### TemplateSubject

The subject line of the custom verification email.

**Type:** STRING

</details>

## update_receipt_rule

Updates a receipt rule. https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateReceiptRule.html

<details><summary>Parameters</summary>

#### RuleSetName (required)

The name of the receipt rule set that the receipt rule belongs to.

**Type:** STRING

#### Rule.Actions.member.N.AddHeaderAction.HeaderName

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Adds a header to the received email. The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

**Type:** ARRAY

#### Rule.Actions.member.N.AddHeaderAction.HeaderValue

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Adds a header to the received email. Must be less than 2048 characters, and must not contain newline characters ("\r" or "\n").

**Type:** ARRAY

#### Rule.Actions.member.N.BounceAction.Message

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon#SNS). Human-readable text to include in the bounce message.

**Type:** ARRAY

#### Rule.Actions.member.N.BounceAction.Sender

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon#SNS). The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.

**Type:** ARRAY

#### Rule.Actions.member.N.BounceAction.SmtpReplyCode

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon#SNS). The SMTP reply code, as defined by RFC 5321.

**Type:** ARRAY

#### Rule.Actions.member.N.BounceAction.StatusCode

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon#SNS). The SMTP enhanced status code, as defined by RFC 3463.

**Type:** ARRAY

#### Rule.Actions.member.N.BounceAction.TopicArn

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon#SNS). The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is#taken. An example of an Amazon SNS topic ARN is#arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about#Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.LambdaAction.FunctionArn

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS. The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is arn:aws:lambda:us-west-2:account-id:function:MyFunction.#For more information about AWS Lambda, see the AWS Lambda Developer Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.LambdaAction.InvocationType

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS. The invocation type of the AWS Lambda function. An invocation type of RequestResponse means that the execution of the function will immediately result in a response, and a value of Event means that the#function will be invoked asynchronously. The default value is Event. For#information about AWS Lambda invocation types, see the AWS Lambda Developer Guide.#Important#There is a 30-second timeout on RequestResponse invocations. You#should use Event invocation in most cases. Use#RequestResponse only when you want to make a mail flow decision,#such as whether to stop the receipt rule or the receipt rule set. Valid Values: Event | RequestResponse

**Type:** ARRAY

#### Rule.Actions.member.N.LambdaAction.TopicArn

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS. The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is#taken. An example of an Amazon SNS topic ARN is#arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about#Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.S3Action

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a#notification to Amazon SNS.

**Type:** ARRAY

#### Rule.Actions.member.N.SNSAction.Encoding

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Publishes the email content within a notification to Amazon SNS. The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a#different encoding format. Base64 preserves all special characters. The default value#is#UTF-8. Valid Values: UTF-8 | Base64

**Type:** ARRAY

#### Rule.Actions.member.N.SNSAction.TopicArn

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Publishes the email content within a notification to Amazon SNS. The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS#topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more#information about Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.StopAction.Scope

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS. The name of the RuleSet that is being stopped. Valid Values: RuleSet

**Type:** ARRAY

#### Rule.Actions.member.N.StopAction.TopicArn

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS. The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is#taken. An example of an Amazon SNS topic ARN is#arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about#Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.WorkmailAction.OrganizationArn

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS. The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is#arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7.#For information about Amazon WorkMail organizations, see the Amazon WorkMail#Administrator Guide.

**Type:** ARRAY

#### Rule.Actions.member.N.WorkmailAction.TopicArn

A data structure that contains the updated receipt rule information. An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS. The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action#is called. An example of an Amazon SNS topic ARN is#arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about#Amazon SNS topics, see the Amazon SNS Developer Guide.

**Type:** ARRAY

#### Rule.Enabled

A data structure that contains the updated receipt rule information. If true, the receipt rule is active. The default value is false.

**Type:** BOOLEAN

#### Rule.Name

A data structure that contains the updated receipt rule information. The name of the receipt rule. The name must: This value can only contain ASCII letters (a-z, A-Z), numbers (0-9),#underscores (_), or dashes (-).#Start and end with a letter or number.#Contain less than 64 characters.

**Type:** STRING

#### Rule.Recipients.member

A data structure that contains the updated receipt rule information. The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule will match all recipients under all verified#domains.

**Type:** ARRAY

#### Rule.ScanEnabled

A data structure that contains the updated receipt rule information. If true, then messages that this receipt rule applies to are scanned for spam and viruses. The default value is false.

**Type:** BOOLEAN

#### Rule.TlsPolicy

A data structure that contains the updated receipt rule information. Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set#to#Require, Amazon SES will bounce emails that are not received over TLS. The#default is Optional. Valid Values: Require | Optional

**Type:** STRING

</details>

## update_template

Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the Amazon SES Developer Guide.  https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateTemplate.html

<details><summary>Parameters</summary>

#### Template.HtmlPart

The content of the email, composed of a subject line, an HTML part, and a text-only part. The HTML body of the email.

**Type:** STRING

#### Template.SubjectPart

The content of the email, composed of a subject line, an HTML part, and a text-only part. The subject line of the email.

**Type:** STRING

#### Template.TemplateName

The content of the email, composed of a subject line, an HTML part, and a text-only part. The name of the template. You will refer to this name when you send email using the SendTemplatedEmail or SendBulkTemplatedEmail#operations.

**Type:** STRING

#### Template.TextPart

The content of the email, composed of a subject line, an HTML part, and a text-only part. The email body that will be visible to recipients whose email clients do not display HTML.

**Type:** STRING

</details>

## verify_domain_dkim

Returns a set of DKIM tokens for a domain identity. https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyDomainDkim.html

<details><summary>Parameters</summary>

#### Domain (required)

The name of the domain to be verified for Easy DKIM signing.

**Type:** STRING

</details>

## verify_domain_identity

Adds a domain to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. For more information about verifying domains, see Verifying Email Addresses and Domains in the Amazon SES Developer Guide.  https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyDomainIdentity.html

<details><summary>Parameters</summary>

#### Domain (required)

The domain to be verified.

**Type:** STRING

</details>

## verify_email_address

Deprecated. Use the VerifyEmailIdentity operation to verify a new email address.  https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyEmailAddress.html

<details><summary>Parameters</summary>

#### EmailAddress (required)

The email address to be verified.

**Type:** STRING

</details>

## verify_email_identity

Adds an email address to the list of identities for your Amazon SES account in the current AWS region and attempts to verify it. As a result of executing this operation, a verification email is sent to the specified address.  https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyEmailIdentity.html

<details><summary>Parameters</summary>

#### EmailAddress (required)

The email address to be verified.

**Type:** STRING

</details>

