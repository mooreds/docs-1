---
id: aws-sns-documentation
title: AWS SNS (version v2.*.*)
sidebar_label: AWS SNS
layout: docs.mustache
---

## add_permission

Adds a statement to a topic's access control policy, granting access for the specified AWS accounts to the specified actions.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ActionName" : [ "string" ],
  "TopicArn" : "The ARN of the topic whose access control policy you wish to modify.",
  "AWSAccountId" : [ "string" ],
  "Label" : "A unique identifier for the new policy statement."
}
```

</details>

## check_if_phone_number_is_opted_out

Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your account. You cannot send SMS messages to a number that is opted out. 
To resume sending messages, you can opt in the number by using the OptInPhoneNumber action.

<details><summary>Parameters</summary>

### $body

The input for the CheckIfPhoneNumberIsOptedOut action.

**Type:** object

```json
{
  "phoneNumber" : "The phone number for which you want to check the opt out status."
}
```

</details>

## confirm_subscription

Verifies an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the AuthenticateOnUnsubscribe flag is set to "true".

<details><summary>Parameters</summary>

### $body

Input for ConfirmSubscription action.

**Type:** object

```json
{
  "TopicArn" : "The ARN of the topic for which you wish to confirm a subscription.",
  "AuthenticateOnUnsubscribe" : "Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter is true and the request has an AWS signature, then only the topic owner and the subscription owner can unsubscribe the endpoint. The unsubscribe action requires AWS authentication. ",
  "Token" : "Short-lived token sent to an endpoint during the Subscribe action."
}
```

</details>

## create_platform_application

Creates a platform application object for one of the supported push notification services, such as APNS and GCM, to which devices and mobile apps may register. You must specify PlatformPrincipal and PlatformCredential attributes when using the CreatePlatformApplication action. The PlatformPrincipal is received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is "SSL certificate". For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is "client id". The PlatformCredential is also received from the notification service. For WNS, PlatformPrincipal is "Package Security Identifier". For MPNS, PlatformPrincipal is "TLS certificate". For Baidu, PlatformPrincipal is "API key". 
For APNS/APNS_SANDBOX, PlatformCredential is "private key". For GCM, PlatformCredential is "API key". For ADM, PlatformCredential is "client secret". For WNS, PlatformCredential is "secret key". For MPNS, PlatformCredential is "private key". For Baidu, PlatformCredential is "secret key". The PlatformApplicationArn that is returned when using CreatePlatformApplication is then used as an attribute for the CreatePlatformEndpoint action. For more information, see Using Amazon SNS Mobile Push Notifications. For more information about obtaining the PlatformPrincipal and PlatformCredential for each of the supported push notification services, see Getting Started with Apple Push Notification Service, Getting Started with Amazon Device Messaging, Getting Started with Baidu Cloud Push, Getting Started with Google Cloud Messaging for Android, Getting Started with MPNS, or Getting Started with WNS. 

<details><summary>Parameters</summary>

### $body

Input for CreatePlatformApplication action.

**Type:** object

```json
{
  "Platform" : "The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and GCM (Google Cloud Messaging).",
  "Attributes" : "For a list of attributes, see SetPlatformApplicationAttributes ",
  "Name" : "Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long."
}
```

</details>

## create_platform_endpoint

Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM and APNS. CreatePlatformEndpoint requires the PlatformApplicationArn that is returned from CreatePlatformApplication. The EndpointArn that is returned when using CreatePlatformEndpoint can then be used by the Publish action to send a message to a mobile app or by the Subscribe action for subscription to a topic. The CreatePlatformEndpoint action is idempotent, so if the requester already owns an endpoint with the same device token and attributes, that endpoint's ARN is returned without creating a new endpoint. For more information, see Using Amazon SNS Mobile Push Notifications.  
When using CreatePlatformEndpoint with Baidu, two attributes must be provided: ChannelId and UserId. The token field must also contain the ChannelId. For more information, see Creating an Amazon SNS Endpoint for Baidu. 

<details><summary>Parameters</summary>

### $body

Input for CreatePlatformEndpoint action.

**Type:** object

```json
{
  "Attributes" : "For a list of attributes, see SetEndpointAttributes.",
  "Token" : "Unique identifier created by the notification service for an app on a device. The specific name for Token will vary, depending on which notification service is being used. For example, when using APNS as the notification service, you need the device token. Alternatively, when using GCM or ADM, the device token equivalent is called the registration ID.",
  "PlatformApplicationArn" : "PlatformApplicationArn returned from CreatePlatformApplication is used to create a an endpoint.",
  "CustomUserData" : "Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB."
}
```

</details>

## create_topic

Creates a topic to which notifications can be published. Users can create at most 100,000 topics. For more information, see http://aws.amazon.com/sns. This action is idempotent, so if the requester already owns a topic with the specified name, that topic's ARN is returned without creating a new topic.

<details><summary>Parameters</summary>

### $body

Input for CreateTopic action.

**Type:** object

```json
{
  "Name" : "The name of the topic you want to create. \nConstraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long."
}
```

</details>

## delete_endpoint

Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent. For more information, see Using Amazon SNS Mobile Push Notifications.  
When you delete an endpoint that is also subscribed to a topic, then you must also unsubscribe the endpoint from the topic.

<details><summary>Parameters</summary>

### $body

Input for DeleteEndpoint action.

**Type:** object

```json
{
  "EndpointArn" : "EndpointArn of endpoint to delete."
}
```

</details>

## delete_platform_application

Deletes a platform application object for one of the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications. 

<details><summary>Parameters</summary>

### $body

Input for DeletePlatformApplication action.

**Type:** object

```json
{
  "PlatformApplicationArn" : "PlatformApplicationArn of platform application object to delete."
}
```

</details>

## delete_topic

Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages previously sent to the topic from being delivered to subscribers. This action is idempotent, so deleting a topic that does not exist does not result in an error.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "TopicArn" : "The ARN of the topic you want to delete."
}
```

</details>

## get_endpoint_attributes

Retrieves the endpoint attributes for a device on one of the supported push notification services, such as GCM and APNS. For more information, see Using Amazon SNS Mobile Push Notifications. 

<details><summary>Parameters</summary>

### $body

Input for GetEndpointAttributes action.

**Type:** object

```json
{
  "EndpointArn" : "EndpointArn for GetEndpointAttributes input."
}
```

</details>

## get_platform_application_attributes

Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications. 

<details><summary>Parameters</summary>

### $body

Input for GetPlatformApplicationAttributes action.

**Type:** object

```json
{
  "PlatformApplicationArn" : "PlatformApplicationArn for GetPlatformApplicationAttributesInput."
}
```

</details>

## get_sms_attributes

Returns the settings for sending SMS messages from your account. 
These settings are set with the SetSMSAttributes action.

<details><summary>Parameters</summary>

### $body

The input for the GetSMSAttributes request.

**Type:** object

```json
{
  "attributes" : [ "string" ]
}
```

</details>

## get_subscription_attributes

Returns all of the properties of a subscription.

<details><summary>Parameters</summary>

### $body

Input for GetSubscriptionAttributes.

**Type:** object

```json
{
  "SubscriptionArn" : "The ARN of the subscription whose properties you want to get."
}
```

</details>

## get_topic_attributes

Returns all of the properties of a topic. Topic properties returned might differ based on the authorization of the user.

<details><summary>Parameters</summary>

### $body

Input for GetTopicAttributes action.

**Type:** object

```json
{
  "TopicArn" : "The ARN of the topic whose properties you want to get."
}
```

</details>

## list_endpoints_by_platform_application

Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM and APNS. The results for ListEndpointsByPlatformApplication are paginated and return a limited list of endpoints, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call ListEndpointsByPlatformApplication again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see Using Amazon SNS Mobile Push Notifications.  
This action is throttled at 30 transactions per second (TPS).

<details><summary>Parameters</summary>

### $body

Input for ListEndpointsByPlatformApplication action.

**Type:** object

```json
{
  "PlatformApplicationArn" : "PlatformApplicationArn for ListEndpointsByPlatformApplicationInput action."
}
```

</details>

## list_phone_numbers_opted_out

Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to them. 
The results for ListPhoneNumbersOptedOut are paginated, and each page returns up to 100 phone numbers. If additional phone numbers are available after the first page of results, then a NextToken string will be returned. To receive the next page, you call ListPhoneNumbersOptedOut again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null.

<details><summary>Parameters</summary>

### $body

The input for the ListPhoneNumbersOptedOut action.

**Type:** object

```json
{
  "nextToken" : "A NextToken string is used when you call the ListPhoneNumbersOptedOut action to retrieve additional records that are available after the first page of results."
}
```

</details>

## list_platform_applications

Lists the platform application objects for the supported push notification services, such as APNS and GCM. The results for ListPlatformApplications are paginated and return a limited list of applications, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call ListPlatformApplications using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see Using Amazon SNS Mobile Push Notifications.  
This action is throttled at 15 transactions per second (TPS).

*This operation has no parameters*

## list_subscriptions

Returns a list of the requester's subscriptions. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a NextToken is also returned. Use the NextToken parameter in a new ListSubscriptions call to get further results. 
This action is throttled at 30 transactions per second (TPS).

*This operation has no parameters*

## list_subscriptions_by_topic

Returns a list of the subscriptions to a specific topic. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a NextToken is also returned. Use the NextToken parameter in a new ListSubscriptionsByTopic call to get further results. 
This action is throttled at 30 transactions per second (TPS).

<details><summary>Parameters</summary>

### $body

Input for ListSubscriptionsByTopic action.

**Type:** object

```json
{
  "TopicArn" : "The ARN of the topic for which you wish to find subscriptions."
}
```

</details>

## list_topics

Returns a list of the requester's topics. Each call returns a limited list of topics, up to 100. If there are more topics, a NextToken is also returned. Use the NextToken parameter in a new ListTopics call to get further results. 
This action is throttled at 30 transactions per second (TPS).

*This operation has no parameters*

## opt_in_phone_number

Use this request to opt in a phone number that is opted out, which enables you to resume sending SMS messages to the number. 
You can opt in a phone number only once every 30 days.

<details><summary>Parameters</summary>

### $body

Input for the OptInPhoneNumber action.

**Type:** object

```json
{
  "phoneNumber" : "The phone number to opt in."
}
```

</details>

## publish

Sends a message to an Amazon SNS topic or sends a text message (SMS message) directly to a phone number.  
If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint. 
When a messageId is returned, the message has been saved and Amazon SNS will attempt to deliver it shortly. 
To use the Publish action for sending a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the CreatePlatformEndpoint action.  
For more information about formatting messages, see Send Custom Platform-Specific Payloads in Messages to Mobile Devices. 

<details><summary>Parameters</summary>

### $body

Input for Publish action.

**Type:** object

```json
{
  "MessageAttributes" : "Message attributes for Publish action.",
  "TopicArn" : "The topic you want to publish to. \nIf you don't specify a value for the TopicArn parameter, you must specify a value for the PhoneNumber or TargetArn parameters.",
  "Message" : "The message you want to send. \nIf you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the MessageStructure parameter to json and use a JSON object for the Message parameter.  \n \nConstraints:  \n With the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in size (262144 bytes, not 262144 characters).  \n For SMS, each message can contain up to 140 bytes, and the character limit depends on the encoding scheme. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters. If you publish a message that exceeds the size limit, Amazon SNS sends it as multiple messages, each fitting within the size limit. Messages are not cut off in the middle of a word but on whole-word boundaries. The total size limit for a single SMS publish action is 1600 bytes.   \nJSON-specific constraints:  \n Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.  \n The values will be parsed (unescaped) before they are used in outgoing messages.  \n Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).  \n Values have a minimum length of 0 (the empty string, \"\", is allowed).  \n Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).  \n Non-string values will cause the key to be ignored.  \n Keys that do not correspond to supported transport protocols are ignored.  \n Duplicate keys are not allowed.  \n Failure to parse or validate any key or value in the message will cause the Publish call to return an error (no partial delivery). ",
  "MessageStructure" : "Set MessageStructure to json if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set MessageStructure to json, the value of the Message parameter must:   \n be a syntactically valid JSON object; and  \n contain at least a top-level JSON key of \"default\" with a value that is a string.   \nYou can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., \"http\"). \nFor information about sending different messages for each protocol using the AWS Management Console, go to Create Different Messages for Each Protocol in the Amazon Simple Notification Service Getting Started Guide.  \nValid value: json ",
  "TargetArn" : "Either TopicArn or EndpointArn, but not both. \nIf you don't specify a value for the TargetArn parameter, you must specify a value for the PhoneNumber or TopicArn parameters.",
  "PhoneNumber" : "The phone number to which you want to deliver an SMS message. Use E.164 format. \nIf you don't specify a value for the PhoneNumber parameter, you must specify a value for the TargetArn or TopicArn parameters.",
  "Subject" : "Optional parameter to be used as the \"Subject\" line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints. \nConstraints: Subjects must be ASCII text that begins with a letter, number, or punctuation mark; must not include line breaks or control characters; and must be less than 100 characters long."
}
```

</details>

## remove_permission

Removes a statement from a topic's access control policy.

<details><summary>Parameters</summary>

### $body

Input for RemovePermission action.

**Type:** object

```json
{
  "TopicArn" : "The ARN of the topic whose access control policy you wish to modify.",
  "Label" : "The unique label of the statement you want to remove."
}
```

</details>

## set_endpoint_attributes

Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM and APNS. For more information, see Using Amazon SNS Mobile Push Notifications. 

<details><summary>Parameters</summary>

### $body

Input for SetEndpointAttributes action.

**Type:** object

```json
{
  "Attributes" : "A map of the endpoint attributes. Attributes in this map include the following:  \n  CustomUserData -- arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.  \n  Enabled -- flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.  \n  Token -- device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service. ",
  "EndpointArn" : "EndpointArn used for SetEndpointAttributes action."
}
```

</details>

## set_platform_application_attributes

Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications. For information on configuring attributes for message delivery status, see Using Amazon SNS Application Attributes for Message Delivery Status. 

<details><summary>Parameters</summary>

### $body

Input for SetPlatformApplicationAttributes action.

**Type:** object

```json
{
  "Attributes" : "A map of the platform application attributes. Attributes in this map include the following:  \n  PlatformCredential -- The credential received from the notification service. For APNS/APNS_SANDBOX, PlatformCredential is private key. For GCM, PlatformCredential is \"API key\". For ADM, PlatformCredential is \"client secret\".  \n  PlatformPrincipal -- The principal received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is SSL certificate. For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is \"client id\".  \n  EventEndpointCreated -- Topic ARN to which EndpointCreated event notifications should be sent.  \n  EventEndpointDeleted -- Topic ARN to which EndpointDeleted event notifications should be sent.  \n  EventEndpointUpdated -- Topic ARN to which EndpointUpdate event notifications should be sent.  \n  EventDeliveryFailure -- Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints.  \n  SuccessFeedbackRoleArn -- IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.  \n  FailureFeedbackRoleArn -- IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf.  \n  SuccessFeedbackSampleRate -- Sample rate percentage (0-100) of successfully delivered messages. ",
  "PlatformApplicationArn" : "PlatformApplicationArn for SetPlatformApplicationAttributes action."
}
```

</details>

## set_sms_attributes

Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports. 
You can override some of these settings for a single message when you use the Publish action with the MessageAttributes.entry.N parameter. For more information, see Sending an SMS Message in the Amazon SNS Developer Guide.

<details><summary>Parameters</summary>

### $body

The input for the SetSMSAttributes action.

**Type:** object

```json
{
  "attributes" : "The default settings for sending SMS messages from your account. You can set values for the following attribute names: \n MonthlySpendLimit – The maximum amount in USD that you are willing to spend each month to send SMS messages. When Amazon SNS determines that sending an SMS message would incur a cost that exceeds this limit, it stops sending SMS messages within minutes.  \nAmazon SNS stops sending SMS messages within minutes of the limit being crossed. During that interval, if you continue to send SMS messages, you will incur costs that exceed your limit.  \nBy default, the spend limit is set to the maximum allowed by Amazon SNS. If you want to raise the limit, submit an SNS Limit Increase case. For New limit value, enter your desired monthly spend limit. In the Use Case Description field, explain that you are requesting an SMS monthly spend limit increase. \n DeliveryStatusIAMRole – The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs. For each SMS message that you send, Amazon SNS writes a log that includes the message price, the success or failure status, the reason for failure (if the message failed), the message dwell time, and other information. \n DeliveryStatusSuccessSamplingRate – The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value can be an integer from 0 - 100. For example, to write logs only for failed deliveries, set this value to 0. To write logs for 10% of your successful deliveries, set it to 10. \n DefaultSenderID – A string, such as your business brand, that is displayed as the sender on the receiving device. Support for sender IDs varies by country. The sender ID can be 1 - 11 alphanumeric characters, and it must contain at least one letter. \n DefaultSMSType – The type of SMS message that you will send by default. You can assign the following values:  \n  Promotional – (Default) Noncritical messages, such as marketing messages. Amazon SNS optimizes the message delivery to incur the lowest cost.  \n  Transactional – Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message delivery to achieve the highest reliability.   \n UsageReportS3Bucket – The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS. Each day, Amazon SNS will deliver a usage report as a CSV file to the bucket. The report includes the following information for each SMS message that was successfully delivered by your account:  \n Time that the message was published (in UTC)  \n Message ID  \n Destination phone number  \n Message type  \n Delivery status  \n Message price (in USD)  \n Part number (a message is split into multiple parts if it is too long for a single message)  \n Total number of parts   \nTo receive the report, the bucket must have a policy that allows the Amazon SNS service principle to perform the s3:PutObject and s3:GetBucketLocation actions. \nFor an example bucket policy and usage report, see Monitoring SMS Activity in the Amazon SNS Developer Guide."
}
```

</details>

## set_subscription_attributes

Allows a subscription owner to set an attribute of the subscription to a new value.

<details><summary>Parameters</summary>

### $body

Input for SetSubscriptionAttributes action.

**Type:** object

```json
{
  "AttributeValue" : "The new value for the attribute in JSON format.",
  "AttributeName" : "The name of the attribute you want to set. Only a subset of the subscriptions attributes are mutable. \nValid values: DeliveryPolicy | FilterPolicy | RawMessageDelivery ",
  "SubscriptionArn" : "The ARN of the subscription to modify."
}
```

</details>

## set_topic_attributes

Allows a topic owner to set an attribute of the topic to a new value.

<details><summary>Parameters</summary>

### $body

Input for SetTopicAttributes action.

**Type:** object

```json
{
  "AttributeValue" : "The new value for the attribute.",
  "TopicArn" : "The ARN of the topic to modify.",
  "AttributeName" : "The name of the attribute you want to set. Only a subset of the topic's attributes are mutable. \nValid values: Policy | DisplayName | DeliveryPolicy "
}
```

</details>

## subscribe

Prepares to subscribe an endpoint by sending the endpoint a confirmation message. To actually create a subscription, the endpoint owner must call the ConfirmSubscription action with the token from the confirmation message. Confirmation tokens are valid for three days. 
This action is throttled at 100 transactions per second (TPS).

<details><summary>Parameters</summary>

### $body

Input for Subscribe action.

**Type:** object

```json
{
  "TopicArn" : "The ARN of the topic you want to subscribe to.",
  "Endpoint" : "The endpoint that you want to receive notifications. Endpoints vary by protocol:  \n For the http protocol, the endpoint is an URL beginning with \"http://\"  \n For the https protocol, the endpoint is a URL beginning with \"https://\"  \n For the email protocol, the endpoint is an email address  \n For the email-json protocol, the endpoint is an email address  \n For the sms protocol, the endpoint is a phone number of an SMS-enabled device  \n For the sqs protocol, the endpoint is the ARN of an Amazon SQS queue  \n For the application protocol, the endpoint is the EndpointArn of a mobile app and device.  \n For the lambda protocol, the endpoint is the ARN of an AWS Lambda function. ",
  "Attributes" : "Assigns attributes to the subscription as a map of key-value pairs. You can assign any attribute that is supported by the SetSubscriptionAttributes action.",
  "ReturnSubscriptionArn" : "Sets whether the response from the Subscribe request includes the subscription ARN, even if the subscription is not yet confirmed. \nIf you set this parameter to false, the response includes the ARN for confirmed subscriptions, but it includes an ARN value of \"pending subscription\" for subscriptions that are not yet confirmed. A subscription becomes confirmed when the subscriber calls the ConfirmSubscription action with a confirmation token. \nIf you set this parameter to true, the response includes the ARN in all cases, even if the subscription is not yet confirmed. \nThe default value is false.",
  "Protocol" : "The protocol you want to use. Supported protocols include:  \n  http -- delivery of JSON-encoded message via HTTP POST  \n  https -- delivery of JSON-encoded message via HTTPS POST  \n  email -- delivery of message via SMTP  \n  email-json -- delivery of JSON-encoded message via SMTP  \n  sms -- delivery of message via SMS  \n  sqs -- delivery of JSON-encoded message to an Amazon SQS queue  \n  application -- delivery of JSON-encoded message to an EndpointArn for a mobile app and device.  \n  lambda -- delivery of JSON-encoded message to an AWS Lambda function. "
}
```

</details>

## unsubscribe

Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic's owner can unsubscribe, and an AWS signature is required. If the Unsubscribe call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint, so that the endpoint owner can easily resubscribe to the topic if the Unsubscribe request was unintended. 
This action is throttled at 100 transactions per second (TPS).

<details><summary>Parameters</summary>

### $body

Input for Unsubscribe action.

**Type:** object

```json
{
  "SubscriptionArn" : "The ARN of the subscription to be deleted."
}
```

</details>

