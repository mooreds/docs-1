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

#### $body

Represents a request to create a receipt rule set by cloning an existing one. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## create_configuration_set

Creates a configuration set. 
Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to create a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

</details>

## create_configuration_set_event_destination

Creates a configuration set event destination.  
When you create or update an event destination, you must provide one, and only one, destination. The destination can be CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).  
An event destination is the AWS service to which Amazon SES publishes the email sending events associated with a configuration set. For information about using configuration sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to create a configuration set event destination. A configuration set event destination, which can be either Amazon CloudWatch or Amazon Kinesis Firehose, describes an AWS service in which Amazon SES publishes the email sending events associated with a configuration set. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

</details>

## create_configuration_set_tracking_options

Creates an association between a configuration set and a custom domain for open and click event tracking.  
By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

#### $body

Represents a request to create an open and click tracking option object in a configuration set. 

**Type:** object

</details>

## create_custom_verification_email_template

Creates a new custom verification email template. 
For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to create a custom verification email template.

**Type:** object

</details>

## create_receipt_filter

Creates a new IP address filter. 
For information about setting up IP address filters, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to create a new IP address filter. You use IP address filters when you receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## create_receipt_rule

Creates a receipt rule. 
For information about setting up receipt rules, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to create a receipt rule. You use receipt rules to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## create_receipt_rule_set

Creates an empty receipt rule set. 
For information about setting up receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to create an empty receipt rule set. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## create_template

Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to create an email template. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## delete_configuration_set

Deletes a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

</details>

## delete_configuration_set_event_destination

Deletes a configuration set event destination. Configuration set event destinations are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete a configuration set event destination. Configuration set event destinations are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

</details>

## delete_configuration_set_tracking_options

Deletes an association between a configuration set and a custom domain for open and click event tracking. 
By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the Amazon SES Developer Guide.  
Deleting this kind of association will result in emails sent using the specified configuration set to capture open and click events using the standard, Amazon SES-operated domains.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete open and click tracking options in a configuration set. 

**Type:** object

</details>

## delete_custom_verification_email_template

Deletes an existing custom verification email template.  
For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete an existing custom verification email template.

**Type:** object

</details>

## delete_identity

Deletes the specified identity (an email address or a domain) from the list of verified identities. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete one of your Amazon SES identities (an email address or domain).

**Type:** object

</details>

## delete_identity_policy

Deletes the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.  
This API is for the identity owner only. If you have not verified the identity, this API will return an error.  
Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete a sending authorization policy for an identity. Sending authorization is an Amazon SES feature that enables you to authorize other senders to use your identities. For information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## delete_receipt_filter

Deletes the specified IP address filter. 
For information about managing IP address filters, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete an IP address filter. You use IP address filters when you receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## delete_receipt_rule

Deletes the specified receipt rule. 
For information about managing receipt rules, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete a receipt rule. You use receipt rules to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## delete_receipt_rule_set

Deletes the specified receipt rule set and all of the receipt rules it contains.  
The currently active rule set cannot be deleted.  
For information about managing receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete a receipt rule set and all of the receipt rules it contains. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## delete_template

Deletes an email template. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete an email template. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## delete_verified_email_address

Deprecated. Use the DeleteIdentity operation to delete email addresses and domains.

<details><summary>Parameters</summary>

#### $body

Represents a request to delete an email address from the list of email addresses you have attempted to verify under your AWS account.

**Type:** object

</details>

## describe_active_receipt_rule_set

Returns the metadata and receipt rules for the receipt rule set that is currently active. 
For information about setting up receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to return the metadata and receipt rules for the receipt rule set that is currently active. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## describe_configuration_set

Returns the details of the specified configuration set. For information about using configuration sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to return the details of a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

</details>

## describe_receipt_rule

Returns the details of the specified receipt rule. 
For information about setting up receipt rules, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to return the details of a receipt rule. You use receipt rules to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## describe_receipt_rule_set

Returns the details of the specified receipt rule set. 
For information about managing receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to return the details of a receipt rule set. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

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

#### $body

Represents a request to retrieve an existing custom verification email template.

**Type:** object

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

#### $body

Represents a request for the status of Amazon SES Easy DKIM signing for an identity. For domain identities, this request also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES successfully verified that these tokens were published. For more information about Easy DKIM, see the Amazon SES Developer Guide.

**Type:** object

</details>

## get_identity_mail_from_domain_attributes

Returns the custom MAIL FROM attributes for a list of identities (email addresses : domains). 
This operation is throttled at one request per second and can only get custom MAIL FROM attributes for up to 100 identities at a time.

<details><summary>Parameters</summary>

#### $body

Represents a request to return the Amazon SES custom MAIL FROM attributes for a list of identities. For information about using a custom MAIL FROM domain, see the Amazon SES Developer Guide.

**Type:** object

</details>

## get_identity_notification_attributes

Given a list of verified identities (email addresses and/or domains), returns a structure describing identity notification attributes. 
This operation is throttled at one request per second and can only get notification attributes for up to 100 identities at a time. 
For more information about using notifications with Amazon SES, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

#### $body

Represents a request to return the notification attributes for a list of identities you verified with Amazon SES. For information about Amazon SES notifications, see the Amazon SES Developer Guide.

**Type:** object

</details>

## get_identity_policies

Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.  
This API is for the identity owner only. If you have not verified the identity, this API will return an error.  
Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to return the requested sending authorization policies for an identity. Sending authorization is an Amazon SES feature that enables you to authorize other senders to use your identities. For information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## get_identity_verification_attributes

Given a list of identities (email addresses and/or domains), returns the verification status and (for domain identities) the verification token for each identity. 
The verification status of an email address is "Pending" until the email address owner clicks the link within the verification email that Amazon SES sent to that address. If the email address owner clicks the link within 24 hours, the verification status of the email address changes to "Success". If the link is not clicked within 24 hours, the verification status changes to "Failed." In that case, if you still want to verify the email address, you must restart the verification process from the beginning. 
For domain identities, the domain's verification status is "Pending" as Amazon SES searches for the required TXT record in the DNS settings of the domain. When Amazon SES detects the record, the domain's verification status changes to "Success". If Amazon SES is unable to detect the record within 72 hours, the domain's verification status changes to "Failed." In that case, if you still want to verify the domain, you must restart the verification process from the beginning. 
This operation is throttled at one request per second and can only get verification attributes for up to 100 identities at a time.

<details><summary>Parameters</summary>

#### $body

Represents a request to return the Amazon SES verification status of a list of identities. For domain identities, this request also returns the verification token. For information about verifying identities with Amazon SES, see the Amazon SES Developer Guide.

**Type:** object

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

#### $body

**Type:** object

</details>

## list_configuration_sets

Provides a list of the configuration sets associated with your Amazon SES account in the current AWS Region. For information about using configuration sets, see Monitoring Your Amazon SES Sending Activity in the Amazon SES Developer Guide.  
You can execute this operation no more than once per second. This operation will return up to 1,000 configuration sets each time it is run. If your Amazon SES account has more than 1,000 configuration sets, this operation will also return a NextToken element. You can then execute the ListConfigurationSets operation again, passing the NextToken parameter and the value of the NextToken element to retrieve additional results.

<details><summary>Parameters</summary>

#### $body

Represents a request to list the configuration sets associated with your AWS account. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

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

#### $body

Represents a request to return a list of all identities (email addresses and domains) that you have attempted to verify under your AWS account, regardless of verification status.

**Type:** object

</details>

## list_identity_policies

Returns a list of sending authorization policies that are attached to the given identity (an email address or a domain). This API returns only a list. If you want the actual policy content, you can use GetIdentityPolicies.  
This API is for the identity owner only. If you have not verified the identity, this API will return an error.  
Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to return a list of sending authorization policies that are attached to an identity. Sending authorization is an Amazon SES feature that enables you to authorize other senders to use your identities. For information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## list_receipt_filters

Lists the IP address filters associated with your AWS account in the current AWS Region. 
For information about managing IP address filters, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to list the IP address filters that exist under your AWS account. You use IP address filters when you receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## list_receipt_rule_sets

Lists the receipt rule sets that exist under your AWS account in the current AWS Region. If there are additional receipt rule sets to be retrieved, you will receive a NextToken that you can provide to the next call to ListReceiptRuleSets to retrieve the additional entries. 
For information about managing receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to list the receipt rule sets that exist under your AWS account. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## list_templates

Lists the email templates present in your Amazon SES account in the current AWS Region. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

**Type:** object

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

#### $body

Represents a request to add or update a sending authorization policy for an identity. Sending authorization is an Amazon SES feature that enables you to authorize other senders to use your identities. For information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## reorder_receipt_rule_set

Reorders the receipt rules within a receipt rule set.  
All of the rules in the rule set must be represented in this request. That is, this API will return an error if the reorder request doesn't explicitly position all of the rules.  
For information about managing receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to reorder the receipt rules within a receipt rule set. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## send_bounce

Generates and sends a bounce message to the sender of an email you received through Amazon SES. You can only use this API on an email up to 24 hours after you receive it.  
You cannot use this API to send generic bounces for mail that was not received by Amazon SES.  
For information about receiving email through Amazon SES, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to send a bounce message to the sender of an email you received through Amazon SES.

**Type:** object

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

#### $body

Represents a request to send a templated email to multiple destinations using Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## send_custom_verification_email

Adds an email address to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address. 
To use this operation, you must first create a custom verification email template. For more information about creating and using custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to send a custom verification email to a specified recipient.

**Type:** object

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

#### $body

Represents a request to send a single formatted email using Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

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

#### $body

Represents a request to send a single raw email using Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

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

#### $body

Represents a request to send a templated email using Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## set_active_receipt_rule_set

Sets the specified receipt rule set as the active receipt rule set.  
To disable your email-receiving through Amazon SES completely, you can call this API with RuleSetName set to null.  
For information about managing receipt rule sets, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to set a receipt rule set as the active receipt rule set. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## set_identity_dkim_enabled

Enables or disables Easy DKIM signing of email sent from an identity:  
 If Easy DKIM signing is enabled for a domain name identity (such as example.com), then Amazon SES will DKIM-sign all email sent by addresses under that domain name (for example, user@example.com).  
 If Easy DKIM signing is enabled for an email address, then Amazon SES will DKIM-sign all email sent by that email address.   
For email addresses (for example, user@example.com), you can only enable Easy DKIM signing if the corresponding domain (in this case, example.com) has been set up for Easy DKIM using the AWS Console or the VerifyDomainDkim operation. 
You can execute this operation no more than once per second. 
For more information about Easy DKIM signing, go to the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

#### $body

Represents a request to enable or disable Amazon SES Easy DKIM signing for an identity. For more information about setting up Easy DKIM, see the Amazon SES Developer Guide.

**Type:** object

</details>

## set_identity_feedback_forwarding_enabled

Given an identity (an email address or a domain), enables or disables whether Amazon SES forwards bounce and complaint notifications as email. Feedback forwarding can only be disabled when Amazon Simple Notification Service (Amazon SNS) topics are specified for both bounces and complaints.  
Feedback forwarding does not apply to delivery notifications. Delivery notifications are only available through Amazon SNS.  
You can execute this operation no more than once per second. 
For more information about using notifications with Amazon SES, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

#### $body

Represents a request to enable or disable whether Amazon SES forwards you bounce and complaint notifications through email. For information about email feedback forwarding, see the Amazon SES Developer Guide.

**Type:** object

</details>

## set_identity_headers_in_notifications_enabled

Given an identity (an email address or a domain), sets whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type. 
You can execute this operation no more than once per second. 
For more information about using notifications with Amazon SES, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

#### $body

Represents a request to set whether Amazon SES includes the original email headers in the Amazon SNS notifications of a specified type. For information about notifications, see the Amazon SES Developer Guide.

**Type:** object

</details>

## set_identity_mail_from_domain

Enables or disables the custom MAIL FROM domain setup for a verified identity (an email address or a domain).  
To send emails using the specified MAIL FROM domain, you must add an MX record to your MAIL FROM domain's DNS settings. If you want your emails to pass Sender Policy Framework (SPF) checks, you must also add or update an SPF record. For more information, see the Amazon SES Developer Guide.  
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to enable or disable the Amazon SES custom MAIL FROM domain setup for a verified identity. For information about using a custom MAIL FROM domain, see the Amazon SES Developer Guide.

**Type:** object

</details>

## set_identity_notification_topic

Sets an Amazon Simple Notification Service (Amazon SNS) topic to use when delivering notifications. When you use this operation, you specify a verified identity, such as an email address or domain. When you send an email that uses the chosen identity in the Source field, Amazon SES sends notifications to the topic you specified. You can send bounce, complaint, or delivery notifications (or any combination of the three) to the Amazon SNS topic that you specify. 
You can execute this operation no more than once per second. 
For more information about feedback notification, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

#### $body

Represents a request to specify the Amazon SNS topic to which Amazon SES will publish bounce, complaint, or delivery notifications for emails sent with that identity as the Source. For information about Amazon SES notifications, see the Amazon SES Developer Guide.

**Type:** object

</details>

## set_receipt_rule_position

Sets the position of the specified receipt rule in the receipt rule set. 
For information about managing receipt rules, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to set the position of a receipt rule in a receipt rule set. You use receipt rule sets to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## test_render_template

Creates a preview of the MIME content of an email when provided with a template and a set of replacement data. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## update_account_sending_enabled

Enables or disables email sending across your entire Amazon SES account in the current AWS Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending across your Amazon SES account in a given AWS Region when reputation metrics (such as your bounce or complaint rates) reach certain thresholds. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to enable or disable the email sending capabilities for your entire Amazon SES account.

**Type:** object

</details>

## update_configuration_set_event_destination

Updates the event destination of a configuration set. Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see Monitoring Your Amazon SES Sending Activity in the Amazon SES Developer Guide.   
When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS).  
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to update the event destination of a configuration set. Configuration sets enable you to publish email sending events. For information about using configuration sets, see the Amazon SES Developer Guide.

**Type:** object

</details>

## update_configuration_set_reputation_metrics_enabled

Enables or disables the publishing of reputation metrics for emails sent using a specific configuration set in a given AWS Region. Reputation metrics include bounce and complaint rates. These metrics are published to Amazon CloudWatch. By using CloudWatch, you can create alarms when bounce or complaint rates exceed certain thresholds. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to modify the reputation metric publishing settings for a configuration set.

**Type:** object

</details>

## update_configuration_set_sending_enabled

Enables or disables email sending for messages sent using a specific configuration set in a given AWS Region. You can use this operation in conjunction with Amazon CloudWatch alarms to temporarily pause email sending for a configuration set when the reputation metrics for that configuration set (such as your bounce on complaint rate) exceed certain thresholds. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to enable or disable the email sending capabilities for a specific configuration set.

**Type:** object

</details>

## update_configuration_set_tracking_options

Modifies an association between a configuration set and a custom domain for open and click event tracking.  
By default, images and links used for tracking open and click events are hosted on domains operated by Amazon SES. You can configure a subdomain of your own to handle these events. For information about using custom domains, see the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

#### $body

Represents a request to update the tracking options for a configuration set. 

**Type:** object

</details>

## update_custom_verification_email_template

Updates an existing custom verification email template. 
For more information about custom verification email templates, see Using Custom Verification Email Templates in the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to update an existing custom verification email template.

**Type:** object

</details>

## update_receipt_rule

Updates a receipt rule. 
For information about managing receipt rules, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to update a receipt rule. You use receipt rules to receive email with Amazon SES. For more information, see the Amazon SES Developer Guide.

**Type:** object

</details>

## update_template

Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the Amazon SES Developer Guide. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## verify_domain_dkim

Returns a set of DKIM tokens for a domain. DKIM tokens are character strings that represent your domain's identity. Using these tokens, you will need to create DNS CNAME records that point to DKIM public keys hosted by Amazon SES. Amazon Web Services will eventually detect that you have updated your DNS records; this detection process may take up to 72 hours. Upon successful detection, Amazon SES will be able to DKIM-sign email originating from that domain. 
You can execute this operation no more than once per second. 
To enable or disable Easy DKIM signing for a domain, use the SetIdentityDkimEnabled operation. 
For more information about creating DNS records using DKIM tokens, go to the Amazon SES Developer Guide.

<details><summary>Parameters</summary>

#### $body

Represents a request to generate the CNAME records needed to set up Easy DKIM with Amazon SES. For more information about setting up Easy DKIM, see the Amazon SES Developer Guide.

**Type:** object

</details>

## verify_domain_identity

Adds a domain to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it. For more information about verifying domains, see Verifying Email Addresses and Domains in the Amazon SES Developer Guide.  
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to begin Amazon SES domain verification and to generate the TXT records that you must publish to the DNS server of your domain to complete the verification. For information about domain verification, see the Amazon SES Developer Guide.

**Type:** object

</details>

## verify_email_address

Deprecated. Use the VerifyEmailIdentity operation to verify a new email address.

<details><summary>Parameters</summary>

#### $body

Represents a request to begin email address verification with Amazon SES. For information about email address verification, see the Amazon SES Developer Guide.

**Type:** object

</details>

## verify_email_identity

Adds an email address to the list of identities for your Amazon SES account in the current AWS region and attempts to verify it. As a result of executing this operation, a verification email is sent to the specified address. 
You can execute this operation no more than once per second.

<details><summary>Parameters</summary>

#### $body

Represents a request to begin email address verification with Amazon SES. For information about email address verification, see the Amazon SES Developer Guide.

**Type:** object

</details>

