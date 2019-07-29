---
id: aws-ses-documentation
title: AWS SES (version v3.*.*)
sidebar_label: AWS SES
layout: docs.mustache
---

## clone_receipt_rule_set

Creates a receipt rule set by cloning an existing one. All receipt rules and configurations are copied to the new receipt rule set and are completely independent of the source rule set. 
For information about setting up rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to create a receipt rule set by cloning an existing one. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "OriginalRuleSetName" : "The name of the rule set to clone.",
  "RuleSetName" : "The name of the rule set to create. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Start and end with a letter or number.  \n Contain less than 64 characters. "
}
```

</details>

## create_configuration_set

Creates a configuration set. 
Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to create a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "ConfigurationSet" : {
    "Name" : "The name of the configuration set. The name must meet the following requirements:  \n Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain 64 characters or fewer. "
  }
}
```

</details>

## create_configuration_set_event_destination

Creates a configuration set event destination.  
When you create or update an event destination, you must provide one, and only one, destination. The destination can be CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).  
An event destination is the AWS service to which Amazon SES publishes the email sending events associated with a configuration set. For information about using configuration sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to create a configuration set event destination. A configuration set event destination, which can be either Amazon CloudWatch or Amazon Kinesis Firehose, describes an AWS service in which Amazon SES publishes the email sending events associated with a configuration set. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "ConfigurationSetName" : "The name of the configuration set that the event destination should be associated with.",
  "EventDestination" : {
    "CloudWatchDestination" : {
      "DimensionConfigurations" : [ {
        "CloudWatchDimensionConfiguration" : {
          "DimensionValueSource" : "The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon SES to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose messageTag. If you want Amazon SES to use your own email headers, choose emailHeader.",
          "DefaultDimensionValue" : "The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. ",
          "DimensionName" : "The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. "
        }
      } ]
    },
    "Enabled" : "Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to true to enable publishing to this destination; set to false to prevent publishing to this destination. The default value is false.",
    "MatchingEventTypes" : [ "string. Possible values: send | reject | bounce | complaint | delivery | open | click | renderingFailure" ],
    "SNSDestination" : {
      "TopicARN" : "The ARN of the Amazon SNS topic that email sending events will be published to. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide."
    },
    "Name" : "The name of the event destination. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 64 characters. ",
    "KinesisFirehoseDestination" : {
      "IAMRoleARN" : "The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.",
      "DeliveryStreamARN" : "The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to."
    }
  }
}
```

</details>

## create_configuration_set_tracking_options

Creates an association between a configuration set and a custom domain for open and click event tracking.  
By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents a request to create an open and click tracking option object in a configuration set. 

**Type:** object

```json
{
  "TrackingOptions" : {
    "CustomRedirectDomain" : "The custom subdomain that will be used to redirect email recipients to the Amazon SES event tracking domain."
  },
  "ConfigurationSetName" : "The name of the configuration set that the tracking options should be associated with."
}
```

</details>

## create_custom_verification_email_template

Creates a new custom verification email template. 
For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to create a custom verification email template.

**Type:** object

```json
{
  "FromEmailAddress" : "The email address that the custom verification email is sent from.",
  "TemplateContent" : "The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see Custom Verification Email Frequently Asked Questions in the Amazon SES Developer Guide.",
  "SuccessRedirectionURL" : "The URL that the recipient of the verification email is sent to if his or her address is successfully verified.",
  "TemplateName" : "The name of the custom verification email template.",
  "FailureRedirectionURL" : "The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.",
  "TemplateSubject" : "The subject line of the custom verification email."
}
```

</details>

## create_receipt_filter

Creates a new IP address filter. 
For information about setting up IP address filters, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to create a new IP address filter. You use IP address filters when you receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Filter" : {
    "IpFilter" : {
      "Policy" : "Indicates whether to block or allow incoming mail from the specified IP addresses.",
      "Cidr" : "A single IP address or a range of IP addresses that you want to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see RFC 2317."
    },
    "Name" : "The name of the IP address filter. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Start and end with a letter or number.  \n Contain less than 64 characters. "
  }
}
```

</details>

## create_receipt_rule

Creates a receipt rule. 
For information about setting up receipt rules, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to create a receipt rule. You use receipt rules to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "After" : "The name of an existing rule after which the new rule will be placed. If this parameter is null, the new rule will be inserted at the beginning of the rule list.",
  "Rule" : {
    "ScanEnabled" : "If true, then messages that this receipt rule applies to are scanned for spam and viruses. The default value is false.",
    "Recipients" : [ "string" ],
    "Actions" : [ {
      "ReceiptAction" : {
        "BounceAction" : {
          "SmtpReplyCode" : "The SMTP reply code, as defined by RFC 5321.",
          "Sender" : "The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.",
          "TopicArn" : "The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide.",
          "Message" : "Human-readable text to include in the bounce message.",
          "StatusCode" : "The SMTP enhanced status code, as defined by RFC 3463."
        },
        "S3Action" : {
          "BucketName" : "The name of the Amazon S3 bucket that incoming email will be saved to.",
          "TopicArn" : "The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide.",
          "KmsKeyArn" : "The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key you created in AWS KMS as follows:  \n To use the default master key, provide an ARN in the form of arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses. For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be arn:aws:kms:us-west-2:123456789012:alias/aws/ses. If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key.  \n To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the Amazon SES Developer Guide.   \nFor more information about key policies, see the AWS KMS Developer Guide. If you do not specify a master key, Amazon SES will not encrypt your emails.  \nYour mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the AWS SDK for Java and AWS SDK for Ruby only. For more information about client-side encryption using AWS KMS master keys, see the Amazon S3 Developer Guide.",
          "ObjectKeyPrefix" : "The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket."
        },
        "StopAction" : {
          "Scope" : "The name of the RuleSet that is being stopped.",
          "TopicArn" : "The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide."
        },
        "WorkmailAction" : {
          "TopicArn" : "The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide.",
          "OrganizationArn" : "The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7. For information about Amazon WorkMail organizations, see the Amazon WorkMail Administrator Guide."
        },
        "SNSAction" : {
          "TopicArn" : "The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide.",
          "Encoding" : "The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8."
        },
        "AddHeaderAction" : {
          "HeaderValue" : "Must be less than 2048 characters, and must not contain newline characters (\"\\r\" or \"\\n\").",
          "HeaderName" : "The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only."
        },
        "LambdaAction" : {
          "FunctionArn" : "The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is arn:aws:lambda:us-west-2:account-id:function:MyFunction. For more information about AWS Lambda, see the AWS Lambda Developer Guide.",
          "TopicArn" : "The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide.",
          "InvocationType" : "The invocation type of the AWS Lambda function. An invocation type of RequestResponse means that the execution of the function will immediately result in a response, and a value of Event means that the function will be invoked asynchronously. The default value is Event. For information about AWS Lambda invocation types, see the AWS Lambda Developer Guide.  \nThere is a 30-second timeout on RequestResponse invocations. You should use Event invocation in most cases. Use RequestResponse only when you want to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set."
        }
      }
    } ],
    "Enabled" : "If true, the receipt rule is active. The default value is false.",
    "Name" : "The name of the receipt rule. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Start and end with a letter or number.  \n Contain less than 64 characters. ",
    "TlsPolicy" : "Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to Require, Amazon SES will bounce emails that are not received over TLS. The default is Optional."
  },
  "RuleSetName" : "The name of the rule set that the receipt rule will be added to."
}
```

</details>

## create_receipt_rule_set

Creates an empty receipt rule set. 
For information about setting up receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to create an empty receipt rule set. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "RuleSetName" : "The name of the rule set to create. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Start and end with a letter or number.  \n Contain less than 64 characters. "
}
```

</details>

## create_template

Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to create an email template. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Template" : {
    "HtmlPart" : "The HTML body of the email.",
    "TextPart" : "The email body that will be visible to recipients whose email clients do not display HTML.",
    "TemplateName" : "The name of the template. You will refer to this name when you send email using the SendTemplatedEmail or SendBulkTemplatedEmail operations.",
    "SubjectPart" : "The subject line of the email."
  }
}
```

</details>

## delete_configuration_set

Deletes a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to delete a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "ConfigurationSetName" : "The name of the configuration set to delete."
}
```

</details>

## delete_configuration_set_event_destination

Deletes a configuration set event destination. Configuration set event destinations are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to delete a configuration set event destination. Configuration set event destinations are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "EventDestinationName" : "The name of the event destination to delete.",
  "ConfigurationSetName" : "The name of the configuration set from which to delete the event destination."
}
```

</details>

## delete_configuration_set_tracking_options

Deletes an association between a configuration set and a custom domain for open and click event tracking. 
By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the Amazon SES Developer Guide.  
Deleting this kind of association will result in emails sent using the specified configuration set to capture open and click events using the standard, Amazon SES-operated domains.

<details><summary>Parameters</summary>

### $body

Represents a request to delete open and click tracking options in a configuration set. 

**Type:** object

```json
{
  "ConfigurationSetName" : "The name of the configuration set from which you want to delete the tracking options."
}
```

</details>

## delete_custom_verification_email_template

Deletes an existing custom verification email template.  
For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to delete an existing custom verification email template.

**Type:** object

```json
{
  "TemplateName" : "The name of the custom verification email template that you want to delete."
}
```

</details>

## delete_identity

Deletes the specified identity (an email address or a domain) from the list of verified identities. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to delete one of your Amazon SES identities (an email address or domain).

**Type:** object

```json
{
  "Identity" : "The identity to be removed from the list of identities for the AWS Account."
}
```

</details>

## delete_identity_policy

Deletes the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.  
This API is for the identity owner only. If you have not verified the identity, this API will return an error.  
Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to delete a sending authorization policy for an identity. Sending authorization is an Amazon SES feature that enables you to authorize other senders to use your identities. For information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "PolicyName" : "The name of the policy to be deleted.",
  "Identity" : "The identity that is associated with the policy that you want to delete. You can specify the identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com. \nTo successfully call this API, you must own the identity."
}
```

</details>

## delete_receipt_filter

Deletes the specified IP address filter. 
For information about managing IP address filters, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to delete an IP address filter. You use IP address filters when you receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "FilterName" : "The name of the IP address filter to delete."
}
```

</details>

## delete_receipt_rule

Deletes the specified receipt rule. 
For information about managing receipt rules, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to delete a receipt rule. You use receipt rules to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "RuleSetName" : "The name of the receipt rule set that contains the receipt rule to delete.",
  "RuleName" : "The name of the receipt rule to delete."
}
```

</details>

## delete_receipt_rule_set

Deletes the specified receipt rule set and all of the receipt rules it contains.  
The currently active rule set cannot be deleted.  
For information about managing receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to delete a receipt rule set and all of the receipt rules it contains. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "RuleSetName" : "The name of the receipt rule set to delete."
}
```

</details>

## delete_template

Deletes an email template. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to delete an email template. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "TemplateName" : "The name of the template to be deleted."
}
```

</details>

## delete_verified_email_address

Deprecated. Use the DeleteIdentity operation to delete email addresses and domains.

<details><summary>Parameters</summary>

### $body

Represents a request to delete an email address from the list of email addresses you have attempted to verify under your AWS account.

**Type:** object

```json
{
  "EmailAddress" : "An email address to be removed from the list of verified addresses."
}
```

</details>

## describe_active_receipt_rule_set

Returns the metadata and receipt rules for the receipt rule set that is currently active. 
For information about setting up receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to return the metadata and receipt rules for the receipt rule set that is currently active. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{ }
```

</details>

## describe_configuration_set

Returns the details of the specified configuration set. For information about using configuration sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to return the details of a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "ConfigurationSetAttributeNames" : [ "string. Possible values: eventDestinations | trackingOptions | reputationOptions" ],
  "ConfigurationSetName" : "The name of the configuration set to describe."
}
```

</details>

## describe_receipt_rule

Returns the details of the specified receipt rule. 
For information about setting up receipt rules, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to return the details of a receipt rule. You use receipt rules to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "RuleSetName" : "The name of the receipt rule set that the receipt rule belongs to.",
  "RuleName" : "The name of the receipt rule."
}
```

</details>

## describe_receipt_rule_set

Returns the details of the specified receipt rule set. 
For information about managing receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to return the details of a receipt rule set. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "RuleSetName" : "The name of the receipt rule set to describe."
}
```

</details>

## get_account_sending_enabled

Returns the email sending status of the Amazon SES account for the current region. 
You can execute this operation no more than once per second.

*This operation has no parameters*

## get_custom_verification_email_template

Returns the custom email verification template for the template name you specify. 
For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to retrieve an existing custom verification email template.

**Type:** object

```json
{
  "TemplateName" : "The name of the custom verification email template that you want to retrieve."
}
```

</details>

## get_identity_dkim_attributes

Returns the current status of Easy DKIM signing for an entity. For domain name identities, this operation also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES has successfully verified that these tokens have been published. 
This operation takes a list of identities as input and returns the following information for each:  
 Whether Easy DKIM signing is enabled or disabled.  
 A set of DKIM tokens that represent the identity. If the identity is an email address, the tokens represent the domain of that address.  
 Whether Amazon SES has successfully verified the DKIM tokens published in the domain's DNS. This information is only returned for domain name identities, not for email addresses.   
This operation is throttled at one request per second and can only get DKIM attributes for up to 100 identities at a time. 
For more information about creating DNS records using DKIM tokens, go to the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents a request for the status of Amazon SES Easy DKIM signing for an identity. For domain identities, this request also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES successfully verified that these tokens were published. For more information about Easy DKIM, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Identities" : [ "string" ]
}
```

</details>

## get_identity_mail_from_domain_attributes

Returns the custom MAIL FROM attributes for a list of identities (email addresses : domains). 
This operation is throttled at one request per second and can only get custom MAIL FROM attributes for up to 100 identities at a time.

<details><summary>Parameters</summary>

### $body

Represents a request to return the Amazon SES custom MAIL FROM attributes for a list of identities. For information about using a custom MAIL FROM domain, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Identities" : [ "string" ]
}
```

</details>

## get_identity_notification_attributes

Given a list of verified identities (email addresses and/or domains), returns a structure describing identity notification attributes. 
This operation is throttled at one request per second and can only get notification attributes for up to 100 identities at a time. 
For more information about using notifications with Amazon SES, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents a request to return the notification attributes for a list of identities you verified with Amazon SES. For information about Amazon SES notifications, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Identities" : [ "string" ]
}
```

</details>

## get_identity_policies

Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.  
This API is for the identity owner only. If you have not verified the identity, this API will return an error.  
Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to return the requested sending authorization policies for an identity. Sending authorization is an Amazon SES feature that enables you to authorize other senders to use your identities. For information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "PolicyNames" : [ "string" ],
  "Identity" : "The identity for which the policies will be retrieved. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com. \nTo successfully call this API, you must own the identity."
}
```

</details>

## get_identity_verification_attributes

Given a list of identities (email addresses and/or domains), returns the verification status and (for domain identities) the verification token for each identity. 
The verification status of an email address is "Pending" until the email address owner clicks the link within the verification email that Amazon SES sent to that address. If the email address owner clicks the link within 24 hours, the verification status of the email address changes to "Success". If the link is not clicked within 24 hours, the verification status changes to "Failed." In that case, if you still want to verify the email address, you must restart the verification process from the beginning. 
For domain identities, the domain's verification status is "Pending" as Amazon SES searches for the required TXT record in the DNS settings of the domain. When Amazon SES detects the record, the domain's verification status changes to "Success". If Amazon SES is unable to detect the record within 72 hours, the domain's verification status changes to "Failed." In that case, if you still want to verify the domain, you must restart the verification process from the beginning. 
This operation is throttled at one request per second and can only get verification attributes for up to 100 identities at a time.

<details><summary>Parameters</summary>

### $body

Represents a request to return the Amazon SES verification status of a list of identities. For domain identities, this request also returns the verification token. For information about verifying identities with Amazon SES, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Identities" : [ "string" ]
}
```

</details>

## get_send_quota

Provides the sending limits for the Amazon SES account.  
You can execute this operation no more than once per second.

*This operation has no parameters*

## get_send_statistics

Provides sending statistics for the current AWS Region. The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute period of time. 
You can execute this operation no more than once per second.

*This operation has no parameters*

## get_template

Displays the template object (which includes the Subject line, HTML part and text part) for the template you specify. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "TemplateName" : "The name of the template you want to retrieve."
}
```

</details>

## list_configuration_sets

Provides a list of the configuration sets associated with your Amazon SES account in the current AWS Region. For information about using configuration sets, see Monitoring Your Amazon SES Sending Activity in the Amazon SES Developer Guide.  
You can execute this operation no more than once per second. This operation will return up to 1,000 configuration sets each time it is run. If your Amazon SES account has more than 1,000 configuration sets, this operation will also return a NextToken element. You can then execute the ListConfigurationSets operation again, passing the NextToken parameter and the value of the NextToken element to retrieve additional results.

<details><summary>Parameters</summary>

### $body

Represents a request to list the configuration sets associated with your AWS account. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "NextToken" : "A token returned from a previous call to ListConfigurationSets to indicate the position of the configuration set in the configuration set list.",
  "MaxItems" : "The number of configuration sets to return."
}
```

</details>

## list_custom_verification_email_templates

Lists the existing custom verification email templates for your account in the current AWS Region. 
For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

*This operation has no parameters*

## list_identities

Returns a list containing all of the identities (email addresses and domains) for your AWS account in the current AWS Region, regardless of verification status. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to return a list of all identities (email addresses and domains) that you have attempted to verify under your AWS account, regardless of verification status.

**Type:** object

```json
{
  "IdentityType" : "The type of the identities to list. Possible values are \"EmailAddress\" and \"Domain\". If this parameter is omitted, then all identities will be listed."
}
```

</details>

## list_identity_policies

Returns a list of sending authorization policies that are attached to the given identity (an email address or a domain). This API returns only a list. If you want the actual policy content, you can use GetIdentityPolicies.  
This API is for the identity owner only. If you have not verified the identity, this API will return an error.  
Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to return a list of sending authorization policies that are attached to an identity. Sending authorization is an Amazon SES feature that enables you to authorize other senders to use your identities. For information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Identity" : "The identity that is associated with the policy for which the policies will be listed. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com. \nTo successfully call this API, you must own the identity."
}
```

</details>

## list_receipt_filters

Lists the IP address filters associated with your AWS account in the current AWS Region. 
For information about managing IP address filters, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to list the IP address filters that exist under your AWS account. You use IP address filters when you receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{ }
```

</details>

## list_receipt_rule_sets

Lists the receipt rule sets that exist under your AWS account in the current AWS Region. If there are additional receipt rule sets to be retrieved, you will receive a NextToken that you can provide to the next call to ListReceiptRuleSets to retrieve the additional entries. 
For information about managing receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to list the receipt rule sets that exist under your AWS account. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "NextToken" : "A token returned from a previous call to ListReceiptRuleSets to indicate the position in the receipt rule set list."
}
```

</details>

## list_templates

Lists the email templates present in your Amazon SES account in the current AWS Region. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "A token returned from a previous call to ListTemplates to indicate the position in the list of email templates.",
  "MaxItems" : "The maximum number of templates to return. This value must be at least 1 and less than or equal to 10. If you do not specify a value, or if you specify a value less than 1 or greater than 10, the operation will return up to 10 results."
}
```

</details>

## list_verified_email_addresses

Deprecated. Use the ListIdentities operation to list the email addresses and domains associated with your account.

*This operation has no parameters*

## put_identity_policy

Adds or updates a sending authorization policy for the specified identity (an email address or a domain).  
This API is for the identity owner only. If you have not verified the identity, this API will return an error.  
Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to add or update a sending authorization policy for an identity. Sending authorization is an Amazon SES feature that enables you to authorize other senders to use your identities. For information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Policy" : "The text of the policy in JSON format. The policy cannot exceed 4 KB. \nFor information about the syntax of sending authorization policies, see the Amazon SES Developer Guide. ",
  "PolicyName" : "The name of the policy. \nThe policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.",
  "Identity" : "The identity that the policy will apply to. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: user@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com. \nTo successfully call this API, you must own the identity."
}
```

</details>

## reorder_receipt_rule_set

Reorders the receipt rules within a receipt rule set.  
All of the rules in the rule set must be represented in this request. That is, this API will return an error if the reorder request doesn't explicitly position all of the rules.  
For information about managing receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to reorder the receipt rules within a receipt rule set. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "RuleNames" : [ "string" ],
  "RuleSetName" : "The name of the receipt rule set to reorder."
}
```

</details>

## send_bounce

Generates and sends a bounce message to the sender of an email you received through Amazon SES. You can only use this API on an email up to 24 hours after you receive it.  
You cannot use this API to send generic bounces for mail that was not received by Amazon SES.  
For information about receiving email through Amazon SES, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to send a bounce message to the sender of an email you received through Amazon SES.

**Type:** object

```json
{
  "BounceSender" : "The address to use in the \"From\" header of the bounce message. This must be an identity that you have verified with Amazon SES.",
  "MessageDsn" : {
    "ArrivalDate" : "When the message was received by the reporting mail transfer agent (MTA), in RFC 822 date-time format.",
    "ExtensionFields" : [ {
      "ExtensionField" : {
        "Value" : "The value of the header to add. Must be less than 2048 characters, and must not contain newline characters (\"\\r\" or \"\\n\").",
        "Name" : "The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only."
      }
    } ],
    "ReportingMta" : "The reporting MTA that attempted to deliver the message, formatted as specified in RFC 3464 (mta-name-type; mta-name). The default value is dns; inbound-smtp.[region].amazonaws.com."
  },
  "Explanation" : "Human-readable text for the bounce message to explain the failure. If not specified, the text will be auto-generated based on the bounced recipient information.",
  "BouncedRecipientInfoList" : [ {
    "BouncedRecipientInfo" : {
      "RecipientDsnFields" : {
        "Status" : "The status code that indicates what went wrong. This is required by RFC 3464.",
        "RemoteMta" : "The MTA to which the remote MTA attempted to deliver the message, formatted as specified in RFC 3464 (mta-name-type; mta-name). This parameter typically applies only to propagating synchronous bounces.",
        "Action" : "The action performed by the reporting mail transfer agent (MTA) as a result of its attempt to deliver the message to the recipient address. This is required by RFC 3464.",
        "ExtensionFields" : [ {
          "ExtensionField" : {
            "Value" : "The value of the header to add. Must be less than 2048 characters, and must not contain newline characters (\"\\r\" or \"\\n\").",
            "Name" : "The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only."
          }
        } ],
        "LastAttemptDate" : "The time the final delivery attempt was made, in RFC 822 date-time format.",
        "DiagnosticCode" : "An extended explanation of what went wrong; this is usually an SMTP response. See RFC 3463 for the correct formatting of this parameter.",
        "FinalRecipient" : "The email address that the message was ultimately delivered to. This corresponds to the Final-Recipient in the DSN. If not specified, FinalRecipient will be set to the Recipient specified in the BouncedRecipientInfo structure. Either FinalRecipient or the recipient in BouncedRecipientInfo must be a recipient of the original bounced message.  \nDo not prepend the FinalRecipient email address with rfc 822;, as described in RFC 3798."
      },
      "Recipient" : "The email address of the recipient of the bounced email.",
      "BounceType" : "The reason for the bounce. You must provide either this parameter or RecipientDsnFields.",
      "RecipientArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to receive email for the recipient of the bounced email. For more information about sending authorization, see the Amazon SES Developer Guide."
    }
  } ],
  "BounceSenderArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the address in the \"From\" header of the bounce. For more information about sending authorization, see the Amazon SES Developer Guide.",
  "OriginalMessageId" : "The message ID of the message to be bounced."
}
```

</details>

## send_bulk_templated_email

Composes an email message to multiple destinations. The message body is created using an email template. 
In order to send email using the SendBulkTemplatedEmail operation, your call to the API must meet the following requirements:  
 The call must refer to an existing email template. You can create email templates using the CreateTemplate operation.  
 The message must be sent from a verified email address or domain.  
 If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see Verifying Email Addresses and Domains in the Amazon SES Developer Guide.   
 The maximum message size is 10 MB.  
 Each Destination parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format UserName@[SubDomain.]Domain.TopLevelDomain), the entire message will be rejected, even if the message contains other recipients that are valid.  
 The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the SendBulkTemplatedEmail operation several times to send the message to each group.  
 The number of destinations you can contact in a single call to the API may be limited by your account's maximum sending rate. 

<details><summary>Parameters</summary>

### $body

Represents a request to send a templated email to multiple destinations using Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "TemplateArn" : "The ARN of the template to use when sending this email.",
  "SourceArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter. \nFor example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to send from user@example.com, then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the Source to be user@example.com. \nFor more information about sending authorization, see the Amazon SES Developer Guide.",
  "DefaultTags" : [ {
    "MessageTag" : {
      "Value" : "The value of the tag. The value must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. ",
      "Name" : "The name of the tag. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. "
    }
  } ],
  "ReturnPath" : "The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. ",
  "DefaultTemplateData" : "A list of replacement values to apply to the template when replacement data is not specified in a Destination object. These values act as a default or fallback option when no other data is available. \nThe template data is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.",
  "ReplyToAddresses" : [ "string" ],
  "Destinations" : [ {
    "BulkEmailDestination" : {
      "Destination" : {
        "ToAddresses" : [ "string" ],
        "CcAddresses" : [ "string" ],
        "BccAddresses" : [ "string" ]
      },
      "ReplacementTemplateData" : "A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.",
      "ReplacementTags" : [ {
        "MessageTag" : {
          "Value" : "The value of the tag. The value must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. ",
          "Name" : "The name of the tag. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. "
        }
      } ]
    }
  } ],
  "ConfigurationSetName" : "The name of the configuration set to use when you send an email using SendBulkTemplatedEmail.",
  "Source" : "The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide. \nIf you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide.  \nAmazon SES does not support the SMTPUTF8 extension, as described in RFC6531. For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters. If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492. The sender name (also known as the friendly name) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047. MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?=.",
  "ReturnPathArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter. \nFor example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the ReturnPath to be feedback@example.com. \nFor more information about sending authorization, see the Amazon SES Developer Guide.",
  "Template" : "The template to use when sending this email."
}
```

</details>

## send_custom_verification_email

Adds an email address to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address. 
To use this operation, you must first create a custom verification email template. For more information about creating and using custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to send a custom verification email to a specified recipient.

**Type:** object

```json
{
  "TemplateName" : "The name of the custom verification email template to use when sending the verification email.",
  "ConfigurationSetName" : "Name of a configuration set to use when sending the verification email.",
  "EmailAddress" : "The email address to verify."
}
```

</details>

## send_email

Composes an email message and immediately queues it for sending. In order to send email using the SendEmail operation, your message must meet the following requirements:  
 The message must be sent from a verified email address or domain. If you attempt to send email using a non-verified address or domain, the operation will result in an "Email address not verified" error.   
 If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see Verifying Email Addresses and Domains in the Amazon SES Developer Guide.   
 The maximum message size is 10 MB.  
 The message must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format UserName@[SubDomain.]Domain.TopLevelDomain), the entire message will be rejected, even if the message contains other recipients that are valid.  
 The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the SendEmail operation several times to send the message to each group.    
For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your sending quota). For more information about sending quotas in Amazon SES, see Managing Your Amazon SES Sending Limits in the Amazon SES Developer Guide. 

<details><summary>Parameters</summary>

### $body

Represents a request to send a single formatted email using Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Destination" : {
    "ToAddresses" : [ "string" ],
    "CcAddresses" : [ "string" ],
    "BccAddresses" : [ "string" ]
  },
  "Message" : {
    "Body" : {
      "Html" : {
        "Charset" : "The character set of the content.",
        "Data" : "The textual data of the content."
      },
      "Text" : {
        "Charset" : "The character set of the content.",
        "Data" : "The textual data of the content."
      }
    },
    "Subject" : {
      "Charset" : "The character set of the content.",
      "Data" : "The textual data of the content."
    }
  },
  "SourceArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter. \nFor example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to send from user@example.com, then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the Source to be user@example.com. \nFor more information about sending authorization, see the Amazon SES Developer Guide.",
  "ReturnPath" : "The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. ",
  "ReplyToAddresses" : [ "string" ],
  "ConfigurationSetName" : "The name of the configuration set to use when you send an email using SendEmail.",
  "Source" : "The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide. \nIf you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide.  \nAmazon SES does not support the SMTPUTF8 extension, as described in RFC6531. For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters. If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492. The sender name (also known as the friendly name) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047. MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?=.",
  "ReturnPathArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter. \nFor example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the ReturnPath to be feedback@example.com. \nFor more information about sending authorization, see the Amazon SES Developer Guide.",
  "Tags" : [ {
    "MessageTag" : {
      "Value" : "The value of the tag. The value must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. ",
      "Name" : "The name of the tag. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. "
    }
  } ]
}
```

</details>

## send_raw_email

Composes an email message and immediately queues it for sending. 
This operation is more flexible than the SendEmail API operation. When you use the SendRawEmail operation, you can specify the headers of the message as well as its content. This flexibility is useful, for example, when you want to send a multipart MIME email (such a message that contains both a text and an HTML version). You can also use this operation to send messages that include attachments. 
The SendRawEmail operation has the following requirements:  
 You can only send email from verified email addresses or domains. If you try to send email from an address that isn't verified, the operation results in an "Email address not verified" error.  
 If your account is still in the Amazon SES sandbox, you can only send email to other verified addresses in your account, or to addresses that are associated with the Amazon SES mailbox simulator.  
 The maximum message size, including attachments, is 10 MB.  
 Each message has to include at least one recipient address. A recipient address includes any address on the To:, CC:, or BCC: lines.  
 If you send a single message to more than one recipient address, and one of the recipient addresses isn't in a valid format (that is, it's not in the format UserName@[SubDomain.]Domain.TopLevelDomain), Amazon SES rejects the entire message, even if the other addresses are valid.  
 Each message can include up to 50 recipient addresses across the To:, CC:, or BCC: lines. If you need to send a single message to more than 50 recipients, you have to split the list of recipient addresses into groups of less than 50 recipients, and send separate messages to each group.  
 Amazon SES allows you to specify 8-bit Content-Transfer-Encoding for MIME message parts. However, if Amazon SES has to modify the contents of your message (for example, if you use open and click tracking), 8-bit content isn't preserved. For this reason, we highly recommend that you encode all content that isn't 7-bit ASCII. For more information, see MIME Encoding in the Amazon SES Developer Guide.   
Additionally, keep the following considerations in mind when using the SendRawEmail operation:  
 Although you can customize the message headers when using the SendRawEmail operation, Amazon SES will automatically apply its own Message-ID and Date headers; if you passed these headers when creating the message, they will be overwritten by the values that Amazon SES provides.  
 If you are using sending authorization to send on behalf of another user, SendRawEmail enables you to specify the cross-account identity for the email's Source, From, and Return-Path parameters in one of two ways: you can pass optional parameters SourceArn, FromArn, and/or ReturnPathArn to the API, or you can include the following X-headers in the header of your raw email:    X-SES-SOURCE-ARN     X-SES-FROM-ARN     X-SES-RETURN-PATH-ARN     Do not include these X-headers in the DKIM signature; Amazon SES will remove them before sending the email.  For most common sending authorization scenarios, we recommend that you specify the SourceIdentityArn parameter and not the FromIdentityArn or ReturnPathIdentityArn parameters. If you only specify the SourceIdentityArn parameter, Amazon SES will set the From and Return Path addresses to the identity specified in SourceIdentityArn. For more information about sending authorization, see the Using Sending Authorization with Amazon SES in the Amazon SES Developer Guide.   
 For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your sending quota). For more information about sending quotas in Amazon SES, see Managing Your Amazon SES Sending Limits in the Amazon SES Developer Guide.  

<details><summary>Parameters</summary>

### $body

Represents a request to send a single raw email using Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "SourceArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter. \nFor example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to send from user@example.com, then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the Source to be user@example.com. \nInstead of using this parameter, you can use the X-header X-SES-SOURCE-ARN in the raw message of the email. If you use both the SourceArn parameter and the corresponding X-header, Amazon SES uses the value of the SourceArn parameter.  \nFor information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide.",
  "Destinations" : [ "string" ],
  "FromArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to specify a particular \"From\" address in the header of the raw email. \nInstead of using this parameter, you can use the X-header X-SES-FROM-ARN in the raw message of the email. If you use both the FromArn parameter and the corresponding X-header, Amazon SES uses the value of the FromArn parameter.  \nFor information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide.",
  "ConfigurationSetName" : "The name of the configuration set to use when you send an email using SendRawEmail.",
  "RawMessage" : {
    "Data" : "The raw data of the message. This data needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an AWS SDK, the SDK takes care of the base 64-encoding for you. In all cases, the client must ensure that the message format complies with Internet email standards regarding email header fields, MIME types, and MIME encoding. \nThe To:, CC:, and BCC: headers in the raw message can contain a group list. \nIf you are using SendRawEmail with sending authorization, you can include X-headers in the raw message to specify the \"Source,\" \"From,\" and \"Return-Path\" addresses. For more information, see the documentation for SendRawEmail.   \nDo not include these X-headers in the DKIM signature, because they are removed by Amazon SES before sending the email.  \nFor more information, go to the Amazon SES Developer Guide."
  },
  "Source" : "The identity's email address. If you do not provide a value for this parameter, you must specify a \"From\" address in the raw text of the message. (You can also specify both.)  \nAmazon SES does not support the SMTPUTF8 extension, as described inRFC6531. For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters. If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492. The sender name (also known as the friendly name) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described in RFC 2047. MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?=.  \nIf you specify the Source parameter and have feedback forwarding enabled, then bounces and complaints will be sent to this email address. This takes precedence over any Return-Path header that you might include in the raw text of the message.",
  "ReturnPathArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter. \nFor example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the ReturnPath to be feedback@example.com. \nInstead of using this parameter, you can use the X-header X-SES-RETURN-PATH-ARN in the raw message of the email. If you use both the ReturnPathArn parameter and the corresponding X-header, Amazon SES uses the value of the ReturnPathArn parameter.  \nFor information about when to use this parameter, see the description of SendRawEmail in this guide, or see the Amazon SES Developer Guide.",
  "Tags" : [ {
    "MessageTag" : {
      "Value" : "The value of the tag. The value must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. ",
      "Name" : "The name of the tag. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. "
    }
  } ]
}
```

</details>

## send_templated_email

Composes an email message using an email template and immediately queues it for sending. 
In order to send email using the SendTemplatedEmail operation, your call to the API must meet the following requirements:  
 The call must refer to an existing email template. You can create email templates using the CreateTemplate operation.  
 The message must be sent from a verified email address or domain.  
 If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see Verifying Email Addresses and Domains in the Amazon SES Developer Guide.   
 The maximum message size is 10 MB.  
 Calls to the SendTemplatedEmail operation may only include one Destination parameter. A destination is a set of recipients who will receive the same version of the email. The Destination parameter can include up to 50 recipients, across the To:, CC: and BCC: fields.  
 The Destination parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format UserName@[SubDomain.]Domain.TopLevelDomain), the entire message will be rejected, even if the message contains other recipients that are valid.    
If your call to the SendTemplatedEmail operation includes all of the required parameters, Amazon SES accepts it and returns a Message ID. However, if Amazon SES can't render the email because the template contains errors, it doesn't send the email. Additionally, because it already accepted the message, Amazon SES doesn't return a message stating that it was unable to send the email. 
For these reasons, we highly recommend that you set up Amazon SES to send you notifications when Rendering Failure events occur. For more information, see Sending Personalized Email Using the Amazon SES API in the Amazon Simple Email Service Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents a request to send a templated email using Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "TemplateArn" : "The ARN of the template to use when sending this email.",
  "Destination" : {
    "ToAddresses" : [ "string" ],
    "CcAddresses" : [ "string" ],
    "BccAddresses" : [ "string" ]
  },
  "TemplateData" : "A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.",
  "SourceArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the Source parameter. \nFor example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to send from user@example.com, then you would specify the SourceArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the Source to be user@example.com. \nFor more information about sending authorization, see the Amazon SES Developer Guide.",
  "ReturnPath" : "The email address that bounces and complaints will be forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message will be returned from the recipient's ISP; this message will then be forwarded to the email address specified by the ReturnPath parameter. The ReturnPath parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. ",
  "ReplyToAddresses" : [ "string" ],
  "ConfigurationSetName" : "The name of the configuration set to use when you send an email using SendTemplatedEmail.",
  "Source" : "The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the Amazon SES Developer Guide. \nIf you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the SourceArn parameter. For more information about sending authorization, see the Amazon SES Developer Guide.  \nAmazon SES does not support the SMTPUTF8 extension, as described in RFC6531. For this reason, the local part of a source email address (the part of the email address that precedes the @ sign) may only contain 7-bit ASCII characters. If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in RFC3492. The sender name (also known as the friendly name) may contain non-ASCII characters. These characters must be encoded using MIME encoded-word syntax, as described inRFC 2047. MIME encoded-word syntax uses the following form: =?charset?encoding?encoded-text?=.",
  "ReturnPathArn" : "This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the ReturnPath parameter. \nFor example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the ReturnPathArn to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the ReturnPath to be feedback@example.com. \nFor more information about sending authorization, see the Amazon SES Developer Guide.",
  "Tags" : [ {
    "MessageTag" : {
      "Value" : "The value of the tag. The value must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. ",
      "Name" : "The name of the tag. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. "
    }
  } ],
  "Template" : "The template to use when sending this email."
}
```

</details>

## set_active_receipt_rule_set

Sets the specified receipt rule set as the active receipt rule set.  
To disable your email-receiving through Amazon SES completely, you can call this API with RuleSetName set to null.  
For information about managing receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to set a receipt rule set as the active receipt rule set. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "RuleSetName" : "The name of the receipt rule set to make active. Setting this value to null disables all email receiving."
}
```

</details>

## set_identity_dkim_enabled

Enables or disables Easy DKIM signing of email sent from an identity:  
 If Easy DKIM signing is enabled for a domain name identity (such as example.com), then Amazon SES will DKIM-sign all email sent by addresses under that domain name (for example, user@example.com).  
 If Easy DKIM signing is enabled for an email address, then Amazon SES will DKIM-sign all email sent by that email address.   
For email addresses (for example, user@example.com), you can only enable Easy DKIM signing if the corresponding domain (in this case, example.com) has been set up for Easy DKIM using the AWS Console or the VerifyDomainDkim operation. 
You can execute this operation no more than once per second. 
For more information about Easy DKIM signing, go to the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents a request to enable or disable Amazon SES Easy DKIM signing for an identity. For more information about setting up Easy DKIM, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Identity" : "The identity for which DKIM signing should be enabled or disabled.",
  "DkimEnabled" : "Sets whether DKIM signing is enabled for an identity. Set to true to enable DKIM signing for this identity; false to disable it. "
}
```

</details>

## set_identity_feedback_forwarding_enabled

Given an identity (an email address or a domain), enables or disables whether Amazon SES forwards bounce and complaint notifications as email. Feedback forwarding can only be disabled when Amazon Simple Notification Service (Amazon SNS) topics are specified for both bounces and complaints.  
Feedback forwarding does not apply to delivery notifications. Delivery notifications are only available through Amazon SNS.  
You can execute this operation no more than once per second. 
For more information about using notifications with Amazon SES, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents a request to enable or disable whether Amazon SES forwards you bounce and complaint notifications through email. For information about email feedback forwarding, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "ForwardingEnabled" : "Sets whether Amazon SES will forward bounce and complaint notifications as email. true specifies that Amazon SES will forward bounce and complaint notifications as email, in addition to any Amazon SNS topic publishing otherwise specified. false specifies that Amazon SES will publish bounce and complaint notifications only through Amazon SNS. This value can only be set to false when Amazon SNS topics are set for both Bounce and Complaint notification types.",
  "Identity" : "The identity for which to set bounce and complaint notification forwarding. Examples: user@example.com, example.com."
}
```

</details>

## set_identity_headers_in_notifications_enabled

Given an identity (an email address or a domain), sets whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type. 
You can execute this operation no more than once per second. 
For more information about using notifications with Amazon SES, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents a request to set whether Amazon SES includes the original email headers in the Amazon SNS notifications of a specified type. For information about notifications, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "NotificationType" : "The notification type for which to enable or disable headers in notifications. ",
  "Enabled" : "Sets whether Amazon SES includes the original email headers in Amazon SNS notifications of the specified notification type. A value of true specifies that Amazon SES will include headers in notifications, and a value of false specifies that Amazon SES will not include headers in notifications. \nThis value can only be set when NotificationType is already set to use a particular Amazon SNS topic.",
  "Identity" : "The identity for which to enable or disable headers in notifications. Examples: user@example.com, example.com."
}
```

</details>

## set_identity_mail_from_domain

Enables or disables the custom MAIL FROM domain setup for a verified identity (an email address or a domain).  
To send emails using the specified MAIL FROM domain, you must add an MX record to your MAIL FROM domain's DNS settings. If you want your emails to pass Sender Policy Framework (SPF) checks, you must also add or update an SPF record. For more information, see the Amazon SES Developer Guide.  
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to enable or disable the Amazon SES custom MAIL FROM domain setup for a verified identity. For information about using a custom MAIL FROM domain, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "MailFromDomain" : "The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must 1) be a subdomain of the verified identity, 2) not be used in a \"From\" address if the MAIL FROM domain is the destination of email feedback forwarding (for more information, see the Amazon SES Developer Guide), and 3) not be used to receive emails. A value of null disables the custom MAIL FROM setting for the identity.",
  "BehaviorOnMXFailure" : "The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. If you choose UseDefaultValue, Amazon SES will use amazonses.com (or a subdomain of that) as the MAIL FROM domain. If you choose RejectMessage, Amazon SES will return a MailFromDomainNotVerified error and not send the email. \nThe action specified in BehaviorOnMXFailure is taken when the custom MAIL FROM domain setup is in the Pending, Failed, and TemporaryFailure states.",
  "Identity" : "The verified identity for which you want to enable or disable the specified custom MAIL FROM domain."
}
```

</details>

## set_identity_notification_topic

Sets an Amazon Simple Notification Service (Amazon SNS) topic to use when delivering notifications. When you use this operation, you specify a verified identity, such as an email address or domain. When you send an email that uses the chosen identity in the Source field, Amazon SES sends notifications to the topic you specified. You can send bounce, complaint, or delivery notifications (or any combination of the three) to the Amazon SNS topic that you specify. 
You can execute this operation no more than once per second. 
For more information about feedback notification, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents a request to specify the Amazon SNS topic to which Amazon SES will publish bounce, complaint, or delivery notifications for emails sent with that identity as the Source. For information about Amazon SES notifications, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "NotificationType" : "The type of notifications that will be published to the specified Amazon SNS topic.",
  "SnsTopic" : "The Amazon Resource Name (ARN) of the Amazon SNS topic. If the parameter is omitted from the request or a null value is passed, SnsTopic is cleared and publishing is disabled.",
  "Identity" : "The identity (email address or domain) that you want to set the Amazon SNS topic for.  \nYou can only specify a verified identity for this parameter.  \nYou can specify an identity by using its name or by using its Amazon Resource Name (ARN). The following examples are all valid identities: sender@example.com, example.com, arn:aws:ses:us-east-1:123456789012:identity/example.com."
}
```

</details>

## set_receipt_rule_position

Sets the position of the specified receipt rule in the receipt rule set. 
For information about managing receipt rules, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to set the position of a receipt rule in a receipt rule set. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "After" : "The name of the receipt rule after which to place the specified receipt rule.",
  "RuleSetName" : "The name of the receipt rule set that contains the receipt rule to reposition.",
  "RuleName" : "The name of the receipt rule to reposition."
}
```

</details>

## test_render_template

Creates a preview of the MIME content of an email when provided with a template and a set of replacement data. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "TemplateData" : "A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.",
  "TemplateName" : "The name of the template that you want to render."
}
```

</details>

## update_account_sending_enabled

Enables or disables email sending across your entire Amazon SES account in the current AWS Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending across your Amazon SES account in a given AWS Region when reputation metrics (such as your bounce or complaint rates) reach certain thresholds. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to enable or disable the email sending capabilities for your entire Amazon SES account.

**Type:** object

```json
{
  "Enabled" : "Describes whether email sending is enabled or disabled for your Amazon SES account in the current AWS Region."
}
```

</details>

## update_configuration_set_event_destination

Updates the event destination of a configuration set. Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see Monitoring Your Amazon SES Sending Activity in the Amazon SES Developer Guide.   
When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).  
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to update the event destination of a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "ConfigurationSetName" : "The name of the configuration set that contains the event destination that you want to update.",
  "EventDestination" : {
    "CloudWatchDestination" : {
      "DimensionConfigurations" : [ {
        "CloudWatchDimensionConfiguration" : {
          "DimensionValueSource" : "The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. If you want Amazon SES to use the message tags that you specify using an X-SES-MESSAGE-TAGS header or a parameter to the SendEmail/SendRawEmail API, choose messageTag. If you want Amazon SES to use your own email headers, choose emailHeader.",
          "DefaultDimensionValue" : "The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. ",
          "DimensionName" : "The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 256 characters. "
        }
      } ]
    },
    "Enabled" : "Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to true to enable publishing to this destination; set to false to prevent publishing to this destination. The default value is false.",
    "MatchingEventTypes" : [ "string. Possible values: send | reject | bounce | complaint | delivery | open | click | renderingFailure" ],
    "SNSDestination" : {
      "TopicARN" : "The ARN of the Amazon SNS topic that email sending events will be published to. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide."
    },
    "Name" : "The name of the event destination. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Contain less than 64 characters. ",
    "KinesisFirehoseDestination" : {
      "IAMRoleARN" : "The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.",
      "DeliveryStreamARN" : "The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to."
    }
  }
}
```

</details>

## update_configuration_set_reputation_metrics_enabled

Enables or disables the publishing of reputation metrics for emails sent using a specific configuration set in a given AWS Region. Reputation metrics include bounce and complaint rates. These metrics are published to Amazon CloudWatch. By using CloudWatch, you can create alarms when bounce or complaint rates exceed certain thresholds. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to modify the reputation metric publishing settings for a configuration set.

**Type:** object

```json
{
  "ConfigurationSetName" : "The name of the configuration set that you want to update.",
  "Enabled" : "Describes whether or not Amazon SES will publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch."
}
```

</details>

## update_configuration_set_sending_enabled

Enables or disables email sending for messages sent using a specific configuration set in a given AWS Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending for a configuration set when the reputation metrics for that configuration set (such as your bounce on complaint rate) exceed certain thresholds. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to enable or disable the email sending capabilities for a specific configuration set.

**Type:** object

```json
{
  "ConfigurationSetName" : "The name of the configuration set that you want to update.",
  "Enabled" : "Describes whether email sending is enabled or disabled for the configuration set. "
}
```

</details>

## update_configuration_set_tracking_options

Modifies an association between a configuration set and a custom domain for open and click event tracking.  
By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents a request to update the tracking options for a configuration set. 

**Type:** object

```json
{
  "TrackingOptions" : {
    "CustomRedirectDomain" : "The custom subdomain that will be used to redirect email recipients to the Amazon SES event tracking domain."
  },
  "ConfigurationSetName" : "The name of the configuration set for which you want to update the custom tracking domain."
}
```

</details>

## update_custom_verification_email_template

Updates an existing custom verification email template. 
For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to update an existing custom verification email template.

**Type:** object

```json
{
  "FromEmailAddress" : "The email address that the custom verification email is sent from.",
  "TemplateContent" : "The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see Custom Verification Email Frequently Asked Questions in the Amazon SES Developer Guide.",
  "SuccessRedirectionURL" : "The URL that the recipient of the verification email is sent to if his or her address is successfully verified.",
  "TemplateName" : "The name of the custom verification email template that you want to update.",
  "FailureRedirectionURL" : "The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.",
  "TemplateSubject" : "The subject line of the custom verification email."
}
```

</details>

## update_receipt_rule

Updates a receipt rule. 
For information about managing receipt rules, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to update a receipt rule. You use receipt rules to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Rule" : {
    "ScanEnabled" : "If true, then messages that this receipt rule applies to are scanned for spam and viruses. The default value is false.",
    "Recipients" : [ "string" ],
    "Actions" : [ {
      "ReceiptAction" : {
        "BounceAction" : {
          "SmtpReplyCode" : "The SMTP reply code, as defined by RFC 5321.",
          "Sender" : "The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.",
          "TopicArn" : "The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide.",
          "Message" : "Human-readable text to include in the bounce message.",
          "StatusCode" : "The SMTP enhanced status code, as defined by RFC 3463."
        },
        "S3Action" : {
          "BucketName" : "The name of the Amazon S3 bucket that incoming email will be saved to.",
          "TopicArn" : "The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide.",
          "KmsKeyArn" : "The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key you created in AWS KMS as follows:  \n To use the default master key, provide an ARN in the form of arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses. For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) region, the ARN of the default master key would be arn:aws:kms:us-west-2:123456789012:alias/aws/ses. If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key.  \n To use a custom master key you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the Amazon SES Developer Guide.   \nFor more information about key policies, see the AWS KMS Developer Guide. If you do not specify a master key, Amazon SES will not encrypt your emails.  \nYour mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the AWS SDK for Java and AWS SDK for Ruby only. For more information about client-side encryption using AWS KMS master keys, see the Amazon S3 Developer Guide.",
          "ObjectKeyPrefix" : "The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket."
        },
        "StopAction" : {
          "Scope" : "The name of the RuleSet that is being stopped.",
          "TopicArn" : "The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide."
        },
        "WorkmailAction" : {
          "TopicArn" : "The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide.",
          "OrganizationArn" : "The ARN of the Amazon WorkMail organization. An example of an Amazon WorkMail organization ARN is arn:aws:workmail:us-west-2:123456789012:organization/m-68755160c4cb4e29a2b2f8fb58f359d7. For information about Amazon WorkMail organizations, see the Amazon WorkMail Administrator Guide."
        },
        "SNSAction" : {
          "TopicArn" : "The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide.",
          "Encoding" : "The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8."
        },
        "AddHeaderAction" : {
          "HeaderValue" : "Must be less than 2048 characters, and must not contain newline characters (\"\\r\" or \"\\n\").",
          "HeaderName" : "The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only."
        },
        "LambdaAction" : {
          "FunctionArn" : "The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is arn:aws:lambda:us-west-2:account-id:function:MyFunction. For more information about AWS Lambda, see the AWS Lambda Developer Guide.",
          "TopicArn" : "The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is taken. An example of an Amazon SNS topic ARN is arn:aws:sns:us-west-2:123456789012:MyTopic. For more information about Amazon SNS topics, see the Amazon SNS Developer Guide.",
          "InvocationType" : "The invocation type of the AWS Lambda function. An invocation type of RequestResponse means that the execution of the function will immediately result in a response, and a value of Event means that the function will be invoked asynchronously. The default value is Event. For information about AWS Lambda invocation types, see the AWS Lambda Developer Guide.  \nThere is a 30-second timeout on RequestResponse invocations. You should use Event invocation in most cases. Use RequestResponse only when you want to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set."
        }
      }
    } ],
    "Enabled" : "If true, the receipt rule is active. The default value is false.",
    "Name" : "The name of the receipt rule. The name must:  \n This value can only contain ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).  \n Start and end with a letter or number.  \n Contain less than 64 characters. ",
    "TlsPolicy" : "Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to Require, Amazon SES will bounce emails that are not received over TLS. The default is Optional."
  },
  "RuleSetName" : "The name of the receipt rule set that the receipt rule belongs to."
}
```

</details>

## update_template

Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "Template" : {
    "HtmlPart" : "The HTML body of the email.",
    "TextPart" : "The email body that will be visible to recipients whose email clients do not display HTML.",
    "TemplateName" : "The name of the template. You will refer to this name when you send email using the SendTemplatedEmail or SendBulkTemplatedEmail operations.",
    "SubjectPart" : "The subject line of the email."
  }
}
```

</details>

## verify_domain_dkim

Returns a set of DKIM tokens for a domain. DKIM tokens are character strings that represent your domain's identity. Using these tokens, you will need to create DNS CNAME records that point to DKIM public keys hosted by Amazon SES. Amazon Web Services will eventually detect that you have updated your DNS records; this detection process may take up to 72 hours. Upon successful detection, Amazon SES will be able to DKIM-sign email originating from that domain. 
You can execute this operation no more than once per second. 
To enable or disable Easy DKIM signing for a domain, use the SetIdentityDkimEnabled operation. 
For more information about creating DNS records using DKIM tokens, go to the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents a request to generate the CNAME records needed to set up Easy DKIM with Amazon SES. For more information about setting up Easy DKIM, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Domain" : "The name of the domain to be verified for Easy DKIM signing."
}
```

</details>

## verify_domain_identity

Adds a domain to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. For more information about verifying domains, see Verifying Email Addresses and Domains in the Amazon SES Developer Guide.  
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to begin Amazon SES domain verification and to generate the TXT records that you must publish to the DNS server of your domain to complete the verification. For information about domain verification, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "Domain" : "The domain to be verified."
}
```

</details>

## verify_email_address

Deprecated. Use the VerifyEmailIdentity operation to verify a new email address.

<details><summary>Parameters</summary>

### $body

Represents a request to begin email address verification with Amazon SES. For information about email address verification, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "EmailAddress" : "The email address to be verified."
}
```

</details>

## verify_email_identity

Adds an email address to the list of identities for your Amazon SES account in the current AWS region and attempts to verify it. As a result of executing this operation, a verification email is sent to the specified address. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

### $body

Represents a request to begin email address verification with Amazon SES. For information about email address verification, see the Amazon SES Developer Guide.

**Type:** object

```json
{
  "EmailAddress" : "The email address to be verified."
}
```

</details>

