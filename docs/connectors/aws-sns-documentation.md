---
id: aws-sns-documentation
title: AWS SNS (version v1.*.*)
sidebar_label: AWS SNS
---

## add_permission

Adds a statement to a topic's access control policy, granting access for the specified AWS accounts to the specified actions.  https://docs.aws.amazon.com/sns/latest/api/API_AddPermission.html

<details><summary>Parameters</summary>

#### AWSAccountId.member.N (required)

The AWS account IDs of the users (principals) who will be given access to the specified actions. The users must have AWS accounts, but do not need to be signed up for this service.

**Type:** ARRAY

#### ActionName.member.N (required)

The action you want to allow for the specified principal(s). Valid values: any Amazon SNS action name.

**Type:** ARRAY

#### Label (required)

A unique identifier for the new policy statement.

**Type:** STRING

#### TopicArn (required)

The ARN of the topic whose access control policy you wish to modify.

**Type:** STRING

</details>

## check_if_phone_number_is_opted_out

Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your account. You cannot send SMS messages to a number that is opted out.  https://docs.aws.amazon.com/sns/latest/api/API_CheckIfPhoneNumberIsOptedOut.html

<details><summary>Parameters</summary>

#### phoneNumber (required)

The phone number for which you want to check the opt out status.

**Type:** STRING

</details>

## confirm_subscription

Verifies an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the AuthenticateOnUnsubscribe flag is set to "true".  https://docs.aws.amazon.com/sns/latest/api/API_ConfirmSubscription.html

<details><summary>Parameters</summary>

#### Token (required)

Short-lived token sent to an endpoint during the Subscribe action.

**Type:** STRING

#### TopicArn (required)

The ARN of the topic for which you wish to confirm a subscription.

**Type:** STRING

#### AuthenticateOnUnsubscribe

Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter is true and the request has an AWS signature, then only the topic owner and the subscription owner can unsubscribe the endpoint. The unsubscribe action requires AWS authentication.

**Type:** BOOLEAN

</details>

## create_platform_application

Creates a platform application object for one of the supported push notification services, such as APNS and FCM, to which devices and mobile apps may register. You must specify PlatformPrincipal and PlatformCredential attributes when using the CreatePlatformApplication action. The PlatformPrincipal is received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is "SSL certificate". For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is "client id". The PlatformCredential is also received from the notification service. For WNS, PlatformPrincipal is "Package Security Identifier". For MPNS, PlatformPrincipal is "TLS certificate". For Baidu, PlatformPrincipal is "API key".  https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformApplication.html

<details><summary>Parameters</summary>

#### Attributes.entry.N.key (required)

Array of names of attributes. For a list of attributes, see SetPlatformApplicationAttributes

**Type:** ARRAY

#### Attributes.entry.N.value (required)

Array of values of corresponding attributes. For a list of attributes, see SetPlatformApplicationAttributes

**Type:** ARRAY

#### Name (required)

Application names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, hyphens, and periods, and must be between 1 and 256 characters long.

**Type:** STRING

#### Platform (required)

The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push Notification Service), APNS_SANDBOX, and GCM (Google Cloud Messaging).

**Type:** STRING

</details>

## create_platform_endpoint

Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM and APNS. CreatePlatformEndpoint requires the PlatformApplicationArn that is returned from CreatePlatformApplication. The EndpointArn that is returned when using CreatePlatformEndpoint can then be used by the Publish action to send a message to a mobile app or by the Subscribe action for subscription to a topic. The CreatePlatformEndpoint action is idempotent, so if the requester already owns an endpoint with the same device token and attributes, that endpoint's ARN is returned without creating a new endpoint. For more information, see Using Amazon SNS Mobile Push Notifications.  https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformEndpoint.html

<details><summary>Parameters</summary>

#### PlatformApplicationArn (required)

PlatformApplicationArn returned from CreatePlatformApplication is used to create a an endpoint.

**Type:** STRING

#### Token (required)

Unique identifier created by the notification service for an app on a device. The specific name for Token will vary, depending on which notification service is being used. For example, when using APNS as the notification service, you need the device token. Alternatively, when using GCM or ADM, the device token equivalent is called the registration ID.

**Type:** STRING

#### Attributes.entry.N.key

Array of names of attributes. For a list of attributes, see SetEndpointAttributes.

**Type:** ARRAY

#### Attributes.entry.N.value

Array of values of corresponding attributes. For a list of attributes, see SetEndpointAttributes.

**Type:** ARRAY

#### CustomUserData

Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.

**Type:** STRING

</details>

## create_topic

Creates a topic to which notifications can be published. Users can create at most 100,000 topics. For more information, see https://aws.amazon.com/sns. This action is idempotent, so if the requester already owns a topic with the specified name, that topic's ARN is returned without creating a new topic.  https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html

<details><summary>Parameters</summary>

#### Name (required)

The name of the topic you want to create. Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.

**Type:** STRING

#### Attributes.entry.N.key

Array of names of attributes. A map of attributes with their corresponding values. The following lists the names, descriptions, and values of the special request parameters that the CreateTopic action uses: DeliveryPolicy – The policy that defines how Amazon SNS retries failed deliveries  to HTTP/S endpoints. DisplayName – The display name to use for a topic with SMS subscriptions. Policy – The policy that defines who can access your topic. By default,  only the topic owner can publish or subscribe to the topic. The following attribute applies only to server-side-encryption: KmsMasterKeyId - The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see  Key Terms. For more examples, see KeyId  in the AWS Key Management Service API Reference.

**Type:** ARRAY

#### Attributes.entry.N.value

Array of values of corresponding attributes. The following lists the names, descriptions, and values of the special request parameters that the CreateTopic action uses: DeliveryPolicy – The policy that defines how Amazon SNS retries failed deliveries  to HTTP/S endpoints. DisplayName – The display name to use for a topic with SMS subscriptions. Policy – The policy that defines who can access your topic. By default,  only the topic owner can publish or subscribe to the topic. The following attribute applies only to server-side-encryption: KmsMasterKeyId - The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see  Key Terms. For more examples, see KeyId  in the AWS Key Management Service API Reference.

**Type:** ARRAY

</details>

## delete_endpoint

Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent. For more information, see Using Amazon SNS Mobile Push Notifications.  https://docs.aws.amazon.com/sns/latest/api/API_DeleteEndpoint.html

<details><summary>Parameters</summary>

#### EndpointArn (required)

EndpointArn of endpoint to delete.

**Type:** STRING

</details>

## delete_platform_application

Deletes a platform application object for one of the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications.  https://docs.aws.amazon.com/sns/latest/api/API_DeletePlatformApplication.html

<details><summary>Parameters</summary>

#### PlatformApplicationArn (required)

PlatformApplicationArn of platform application object to delete.

**Type:** STRING

</details>

## delete_topic

Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages previously sent to the topic from being delivered to subscribers. This action is idempotent, so deleting a topic that does not exist does not result in an error.  https://docs.aws.amazon.com/sns/latest/api/API_DeleteTopic.html

<details><summary>Parameters</summary>

#### TopicArn (required)

The ARN of the topic you want to delete.

**Type:** STRING

</details>

## get_endpoint_attributes

Retrieves the endpoint attributes for a device on one of the supported push notification services, such as GCM and APNS. For more information, see Using Amazon SNS Mobile Push Notifications.  https://docs.aws.amazon.com/sns/latest/api/API_GetEndpointAttributes.html

<details><summary>Parameters</summary>

#### EndpointArn (required)

EndpointArn for GetEndpointAttributes input.

**Type:** STRING

</details>

## get_platform_application_attributes

Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications.  https://docs.aws.amazon.com/sns/latest/api/API_GetPlatformApplicationAttributes.html

<details><summary>Parameters</summary>

#### PlatformApplicationArn (required)

PlatformApplicationArn for GetPlatformApplicationAttributesInput.

**Type:** STRING

</details>

## get_sms_attributes

Returns the settings for sending SMS messages from your account. https://docs.aws.amazon.com/sns/latest/api/API_GetSMSAttributes.html

<details><summary>Parameters</summary>

#### attributes.member.N

A list of the individual attribute names, such as MonthlySpendLimit, for which you want values. For all attribute names, see SetSMSAttributes. If you don't use this parameter, Amazon SNS returns all SMS attributes.

**Type:** ARRAY

</details>

## get_subscription_attributes

Returns all of the properties of a subscription. https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html

<details><summary>Parameters</summary>

#### SubscriptionArn (required)

The ARN of the subscription whose properties you want to get.

**Type:** STRING

</details>

## get_topic_attributes

Returns all of the properties of a topic. Topic properties returned might differ based on the authorization of the user.  https://docs.aws.amazon.com/sns/latest/api/API_GetTopicAttributes.html

<details><summary>Parameters</summary>

#### TopicArn (required)

The ARN of the topic whose properties you want to get.

**Type:** STRING

</details>

## list_endpoints_by_platform_application

Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM and APNS. The results for ListEndpointsByPlatformApplication are paginated and return a limited list of endpoints, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call ListEndpointsByPlatformApplication again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see Using Amazon SNS Mobile Push Notifications.  https://docs.aws.amazon.com/sns/latest/api/API_ListEndpointsByPlatformApplication.html

<details><summary>Parameters</summary>

#### PlatformApplicationArn (required)

PlatformApplicationArn for ListEndpointsByPlatformApplicationInput action.

**Type:** STRING

</details>

## list_phone_numbers_opted_out



*This operation has no parameters*

## list_platform_applications



*This operation has no parameters*

## list_subscriptions

Returns a list of the requester's subscriptions. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a NextToken is also returned. Use the NextToken parameter in a new ListSubscriptions call to get further results.  https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptions.html

<details><summary>Parameters</summary>

#### NextToken

Token returned by the previous ListSubscriptions request.

**Type:** STRING

</details>

## list_subscriptions_by_topic

Returns a list of the subscriptions to a specific topic. Each call returns a limited list of subscriptions, up to 100. If there are more subscriptions, a NextToken is also returned. Use the NextToken parameter in a new ListSubscriptionsByTopic call to get further results.  https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptionsByTopic.html

<details><summary>Parameters</summary>

#### TopicArn (required)

The ARN of the topic for which you wish to find subscriptions.

**Type:** STRING

</details>

## list_topics



*This operation has no parameters*

## opt_in_phone_number

Use this request to opt in a phone number that is opted out, which enables you to resume sending SMS messages to the number.  https://docs.aws.amazon.com/sns/latest/api/API_OptInPhoneNumber.html

<details><summary>Parameters</summary>

#### phoneNumber (required)

The phone number to opt in.

**Type:** STRING

</details>

## publish

Sends a message to an Amazon SNS topic or sends a text message (SMS message) directly to a phone number.  https://docs.aws.amazon.com/sns/latest/api/API_Publish.html

<details><summary>Parameters</summary>

#### Message (required)

The message you want to send. Important The Message parameter is always a string. If you set MessageStructure to json, you must string-encode the Message parameter. If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the MessageStructure parameter to json and use a JSON object for the Message parameter. See the Examples section for the format of the JSON object. Constraints: With the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in size (262,144 bytes, not 262,144 characters). For SMS, each message can contain up to 140 characters. This character limit depends on the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters. If you publish a message that exceeds this size limit, Amazon SNS sends the  message as multiple messages, each fitting within the size limit. Messages aren't truncated mid-word but are cut off at whole-word boundaries. The total size limit for a single SMS Publish action is 1,600 characters. JSON-specific constraints: Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values. The values will be parsed (unescaped) before they are used in outgoing messages. Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending). Values have a minimum length of 0 (the empty string, "", is allowed). Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes). Non-string values will cause the key to be ignored. Keys that do not correspond to supported transport protocols are ignored. Duplicate keys are not allowed. Failure to parse or validate any key or value in the message will cause the Publish call to return an error (no partial delivery).

**Type:** STRING

#### MessageAttributes.entry.N

Array of names of message attributes for Publish action. String to MessageAttributeValue object map. See https://docs.aws.amazon.com/sns/latest/api/API_MessageAttributeValue.html.

**Type:** ARRAY

#### MessageStructure

Set MessageStructure to json if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set MessageStructure to json, the value of the Message parameter must:  be a syntactically valid JSON object; and contain at least a top-level JSON key of "default" with a value that is a string. You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., "http"). For information about sending different messages for each protocol using the AWS Management Console, go to Create Different Messages for Each Protocol in the Amazon Simple Notification Service Getting Started Guide.  Valid value: json

**Type:** STRING

#### PhoneNumber

The phone number to which you want to deliver an SMS message. Use E.164 format. If you don't specify a value for the PhoneNumber parameter, you must specify a value for the TargetArn or TopicArn parameters.

**Type:** STRING

#### Subject

Optional parameter to be used as the "Subject" line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints. Constraints: Subjects must be ASCII text that begins with a letter, number, or punctuation mark; must not include line breaks or control characters; and must be less than 100 characters long.

**Type:** STRING

#### TargetArn

Either TopicArn or EndpointArn, but not both. If you don't specify a value for the TargetArn parameter, you must specify a value for the PhoneNumber or TopicArn parameters.

**Type:** STRING

#### TopicArn

The topic you want to publish to. If you don't specify a value for the TopicArn parameter, you must specify a value for the PhoneNumber or TargetArn parameters.

**Type:** STRING

</details>

## remove_permission

Removes a statement from a topic's access control policy. https://docs.aws.amazon.com/sns/latest/api/API_RemovePermission.html

<details><summary>Parameters</summary>

#### Label (required)

The unique label of the statement you want to remove.

**Type:** STRING

#### TopicArn (required)

The ARN of the topic whose access control policy you wish to modify.

**Type:** STRING

</details>

## set_endpoint_attributes

Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM and APNS. For more information, see Using Amazon SNS Mobile Push Notifications.  https://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html

<details><summary>Parameters</summary>

#### EndpointArn (required)

EndpointArn used for SetEndpointAttributes action.

**Type:** STRING

#### Attributes.entry.N.key

Array of names of attributes.  Attributes in this map include the following: CustomUserData – arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB. Enabled – flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token. Token – device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.

**Type:** ARRAY

#### Attributes.entry.N.value

Array of values of corresponding attributes. Attributes in this map include the following: CustomUserData – arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB. Enabled – flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token. Token – device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.

**Type:** ARRAY

</details>

## set_platform_application_attributes

Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications. For information on configuring attributes for message delivery status, see Using Amazon SNS Application Attributes for Message Delivery Status.  https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html

<details><summary>Parameters</summary>

#### PlatformApplicationArn (required)

PlatformApplicationArn for SetPlatformApplicationAttributes action.

**Type:** STRING

#### Attributes.entry.N.key

Array of names of attributes.  Attributes in this map include the following: PlatformCredential – The credential received from the notification service. For APNS/APNS_SANDBOX, PlatformCredential is private key. For GCM, PlatformCredential is "API key". For ADM, PlatformCredential is "client secret". PlatformPrincipal – The principal received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is SSL certificate. For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is "client id". EventEndpointCreated – Topic ARN to which EndpointCreated event notifications should be sent. EventEndpointDeleted – Topic ARN to which EndpointDeleted event notifications should be sent. EventEndpointUpdated – Topic ARN to which EndpointUpdate event notifications should be sent. EventDeliveryFailure – Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints. SuccessFeedbackRoleArn – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf. FailureFeedbackRoleArn – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf. SuccessFeedbackSampleRate – Sample rate percentage (0-100) of successfully delivered messages.

**Type:** ARRAY

#### Attributes.entry.N.value

Array of values of corresponding attributes. Attributes in this map include the following: PlatformCredential – The credential received from the notification service. For APNS/APNS_SANDBOX, PlatformCredential is private key. For GCM, PlatformCredential is "API key". For ADM, PlatformCredential is "client secret". PlatformPrincipal – The principal received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is SSL certificate. For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is "client id". EventEndpointCreated – Topic ARN to which EndpointCreated event notifications should be sent. EventEndpointDeleted – Topic ARN to which EndpointDeleted event notifications should be sent. EventEndpointUpdated – Topic ARN to which EndpointUpdate event notifications should be sent. EventDeliveryFailure – Topic ARN to which DeliveryFailure event notifications should be sent upon Direct Publish delivery failure (permanent) to one of the application's endpoints. SuccessFeedbackRoleArn – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf. FailureFeedbackRoleArn – IAM role ARN used to give Amazon SNS write access to use CloudWatch Logs on your behalf. SuccessFeedbackSampleRate – Sample rate percentage (0-100) of successfully delivered messages.

**Type:** ARRAY

</details>

## set_sms_attributes

Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports.  https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html

<details><summary>Parameters</summary>

#### attributes.entry.N.key

Array of names of attributes. The default settings for sending SMS messages from your account. You can set values for the following attribute names: MonthlySpendLimit – The maximum amount in USD that you are willing to spend each month to send SMS messages. When Amazon SNS determines that sending an SMS message would incur a cost that exceeds this limit, it stops sending SMS messages within minutes. Important Amazon SNS stops sending SMS messages within minutes of the limit being crossed. During that interval, if you continue to send SMS messages, you will incur costs that exceed your limit. By default, the spend limit is set to the maximum allowed by Amazon SNS. If you want to raise the limit, submit an SNS Limit Increase case. For New limit value, enter your desired monthly spend limit. In the Use Case Description field, explain that you are requesting an SMS monthly spend limit increase. DeliveryStatusIAMRole – The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs. For each SMS message that you send, Amazon SNS writes a log that includes the message price, the success or failure status, the reason for failure (if the message failed), the message dwell time, and other information. DeliveryStatusSuccessSamplingRate – The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value can be an integer from 0 - 100. For example, to write logs only for failed deliveries, set this value to 0. To write logs for 10% of your successful deliveries, set it to 10. DefaultSenderID – A string, such as your business brand, that is displayed as the sender on the receiving device. Support for sender IDs varies by country. The sender ID can be 1 - 11 alphanumeric characters, and it must contain at least one letter. DefaultSMSType – The type of SMS message that you will send by default. You can assign the following values: Promotional – (Default) Noncritical messages, such as marketing messages. Amazon SNS optimizes the message delivery to incur the lowest cost. Transactional – Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message delivery to achieve the highest reliability. UsageReportS3Bucket – The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS. Each day, Amazon SNS will deliver a usage report as a CSV file to the bucket. The report includes the following information for each SMS message that was successfully delivered by your account: Time that the message was published (in UTC) Message ID Destination phone number Message type Delivery status Message price (in USD) Part number (a message is split into multiple parts if it is too long for a single message) Total number of parts To receive the report, the bucket must have a policy that allows the Amazon SNS service principle to perform the s3:PutObject and s3:GetBucketLocation actions. For an example bucket policy and usage report, see Monitoring SMS Activity in the Amazon SNS Developer Guide.

**Type:** ARRAY

#### attributes.entry.N.value

Array of values of corresponding attributes. The default settings for sending SMS messages from your account. You can set values for the following attribute names: MonthlySpendLimit – The maximum amount in USD that you are willing to spend each month to send SMS messages. When Amazon SNS determines that sending an SMS message would incur a cost that exceeds this limit, it stops sending SMS messages within minutes. Important Amazon SNS stops sending SMS messages within minutes of the limit being crossed. During that interval, if you continue to send SMS messages, you will incur costs that exceed your limit. By default, the spend limit is set to the maximum allowed by Amazon SNS. If you want to raise the limit, submit an SNS Limit Increase case. For New limit value, enter your desired monthly spend limit. In the Use Case Description field, explain that you are requesting an SMS monthly spend limit increase. DeliveryStatusIAMRole – The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs. For each SMS message that you send, Amazon SNS writes a log that includes the message price, the success or failure status, the reason for failure (if the message failed), the message dwell time, and other information. DeliveryStatusSuccessSamplingRate – The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value can be an integer from 0 - 100. For example, to write logs only for failed deliveries, set this value to 0. To write logs for 10% of your successful deliveries, set it to 10. DefaultSenderID – A string, such as your business brand, that is displayed as the sender on the receiving device. Support for sender IDs varies by country. The sender ID can be 1 - 11 alphanumeric characters, and it must contain at least one letter. DefaultSMSType – The type of SMS message that you will send by default. You can assign the following values: Promotional – (Default) Noncritical messages, such as marketing messages. Amazon SNS optimizes the message delivery to incur the lowest cost. Transactional – Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message delivery to achieve the highest reliability. UsageReportS3Bucket – The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS. Each day, Amazon SNS will deliver a usage report as a CSV file to the bucket. The report includes the following information for each SMS message that was successfully delivered by your account: Time that the message was published (in UTC) Message ID Destination phone number Message type Delivery status Message price (in USD) Part number (a message is split into multiple parts if it is too long for a single message) Total number of parts To receive the report, the bucket must have a policy that allows the Amazon SNS service principle to perform the s3:PutObject and s3:GetBucketLocation actions. For an example bucket policy and usage report, see Monitoring SMS Activity in the Amazon SNS Developer Guide.

**Type:** ARRAY

</details>

## set_subscription_attributes

Allows a subscription owner to set an attribute of the subscription to a new value. https://docs.aws.amazon.com/sns/latest/api/API_SetSubscriptionAttributes.html

<details><summary>Parameters</summary>

#### AttributeName (required)

A map of attributes with their corresponding values. The following lists the names, descriptions, and values of the special request parameters that the SetTopicAttributes action uses: DeliveryPolicy – The policy that defines how Amazon SNS retries failed deliveries  to HTTP/S endpoints. FilterPolicy – The simple JSON object that lets your subscriber receive only  a subset of messages, rather than receiving every message published to the topic. RawMessageDelivery – When set to true, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.

**Type:** STRING

#### SubscriptionArn (required)

The ARN of the subscription to modify.

**Type:** STRING

#### AttributeValue

The new value for the attribute in JSON format.

**Type:** STRING

</details>

## set_topic_attributes

Allows a topic owner to set an attribute of the topic to a new value. https://docs.aws.amazon.com/sns/latest/api/API_SetTopicAttributes.html

<details><summary>Parameters</summary>

#### AttributeName (required)

A map of attributes with their corresponding values. The following lists the names, descriptions, and values of the special request parameters that the SetTopicAttributes action uses: DeliveryPolicy – The policy that defines how Amazon SNS retries failed deliveries  to HTTP/S endpoints. DisplayName – The display name to use for a topic with SMS subscriptions. Policy – The policy that defines who can access your topic. By default,  only the topic owner can publish or subscribe to the topic. The following attribute applies only to server-side-encryption: KmsMasterKeyId - The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see  Key Terms. For more examples, see KeyId  in the AWS Key Management Service API Reference.

**Type:** STRING

#### TopicArn (required)

The ARN of the topic to modify.

**Type:** STRING

#### AttributeValue

The new value for the attribute in JSON format.

**Type:** OBJECT

</details>

## subscribe

Prepares to subscribe an endpoint by sending the endpoint a confirmation message. To actually create a subscription, the endpoint owner must call the ConfirmSubscription action with the token from the confirmation message. Confirmation tokens are valid for three days.  https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html

<details><summary>Parameters</summary>

#### Endpoint (required)

The endpoint that you want to receive notifications. Endpoints vary by protocol: For the http protocol, the endpoint is an URL beginning with "https://" For the https protocol, the endpoint is a URL beginning with "https://" For the email protocol, the endpoint is an email address For the email-json protocol, the endpoint is an email address For the sms protocol, the endpoint is a phone number of an SMS-enabled device For the sqs protocol, the endpoint is the ARN of an Amazon SQS queue For the application protocol, the endpoint is the EndpointArn of a mobile app and device. For the lambda protocol, the endpoint is the ARN of an AWS Lambda function.

**Type:** STRING

#### Protocol (required)

The protocol you want to use. Supported protocols include: http – delivery of JSON-encoded message via HTTP POST https – delivery of JSON-encoded message via HTTPS POST email – delivery of message via SMTP email-json – delivery of JSON-encoded message via SMTP sms – delivery of message via SMS sqs – delivery of JSON-encoded message to an Amazon SQS queue application – delivery of JSON-encoded message to an EndpointArn for a mobile app and device. lambda – delivery of JSON-encoded message to an AWS Lambda function.

**Type:** STRING

#### TopicArn (required)

The ARN of the topic you want to subscribe to.

**Type:** STRING

#### Attributes.entry.N.key

Array of names of attributes. The following lists the names, descriptions, and values of the special request parameters that the SetTopicAttributes action uses: DeliveryPolicy – The policy that defines how Amazon SNS retries failed deliveries  to HTTP/S endpoints. FilterPolicy – The simple JSON object that lets your subscriber receive only  a subset of messages, rather than receiving every message published to the topic. RawMessageDelivery – When set to true, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.

**Type:** ARRAY

#### Attributes.entry.N.value

Array of values of corresponding attributes. The following lists the names, descriptions, and values of the special request parameters that the SetTopicAttributes action uses: DeliveryPolicy – The policy that defines how Amazon SNS retries failed deliveries  to HTTP/S endpoints. FilterPolicy – The simple JSON object that lets your subscriber receive only  a subset of messages, rather than receiving every message published to the topic. RawMessageDelivery – When set to true, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.

**Type:** ARRAY

#### ReturnSubscriptionArn

Sets whether the response from the Subscribe request includes the subscription ARN, even if the subscription is not yet confirmed. If you set this parameter to false, the response includes the ARN for confirmed subscriptions, but it includes an ARN value of "pending subscription" for subscriptions that are not yet confirmed. A subscription becomes confirmed when the subscriber calls the ConfirmSubscription action with a confirmation token. If you set this parameter to true, the response includes the ARN in all cases, even if the subscription is not yet confirmed. The default value is false.

**Type:** BOOLEAN

</details>

## unsubscribe

Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic's owner can unsubscribe, and an AWS signature is required. If the Unsubscribe call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint, so that the endpoint owner can easily resubscribe to the topic if the Unsubscribe request was unintended.  https://docs.aws.amazon.com/sns/latest/api/API_Unsubscribe.html

<details><summary>Parameters</summary>

#### SubscriptionArn (required)

The ARN of the subscription to be deleted.

**Type:** STRING

</details>

