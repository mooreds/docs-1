---
id: aws-sns-documentation
title: AWS SNS (version v2.*.*)
sidebar_label: AWS SNS
layout: docs.mustache
---

## add_permission

Adds a statement to a topic's access control policy, granting access for the specified AWS accounts to the specified actions.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## check_if_phone_number_is_opted_out

Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your account. You cannot send SMS messages to a number that is opted out. 
To resume sending messages, you can opt in the number by using the OptInPhoneNumber action.

<details><summary>Parameters</summary>

#### $body

The input for the CheckIfPhoneNumberIsOptedOut action.

**Type:** object

</details>

## confirm_subscription

Verifies an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the AuthenticateOnUnsubscribe flag is set to "true".

<details><summary>Parameters</summary>

#### $body

Input for ConfirmSubscription action.

**Type:** object

</details>

## create_platform_application

Creates a platform application object for one of the supported push notification services, such as APNS and GCM, to which devices and mobile apps may register. You must specify PlatformPrincipal and PlatformCredential attributes when using the CreatePlatformApplication action. The PlatformPrincipal is received from the notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is "SSL certificate". For GCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is "client id". The PlatformCredential is also received from the notification service. For WNS, PlatformPrincipal is "Package Security Identifier". For MPNS, PlatformPrincipal is "TLS certificate". For Baidu, PlatformPrincipal is "API key". 
For APNS/APNS_SANDBOX, PlatformCredential is "private key". For GCM, PlatformCredential is "API key". For ADM, PlatformCredential is "client secret". For WNS, PlatformCredential is "secret key". For MPNS, PlatformCredential is "private key". For Baidu, PlatformCredential is "secret key". The PlatformApplicationArn that is returned when using CreatePlatformApplication is then used as an attribute for the CreatePlatformEndpoint action. For more information, see Using Amazon SNS Mobile Push Notifications. For more information about obtaining the PlatformPrincipal and PlatformCredential for each of the supported push notification services, see Getting Started with Apple Push Notification Service, Getting Started with Amazon Device Messaging, Getting Started with Baidu Cloud Push, Getting Started with Google Cloud Messaging for Android, Getting Started with MPNS, or Getting Started with WNS. 

<details><summary>Parameters</summary>

#### $body

Input for CreatePlatformApplication action.

**Type:** object

</details>

## create_platform_endpoint

Creates an endpoint for a device and mobile app on one of the supported push notification services, such as GCM and APNS. CreatePlatformEndpoint requires the PlatformApplicationArn that is returned from CreatePlatformApplication. The EndpointArn that is returned when using CreatePlatformEndpoint can then be used by the Publish action to send a message to a mobile app or by the Subscribe action for subscription to a topic. The CreatePlatformEndpoint action is idempotent, so if the requester already owns an endpoint with the same device token and attributes, that endpoint's ARN is returned without creating a new endpoint. For more information, see Using Amazon SNS Mobile Push Notifications.  
When using CreatePlatformEndpoint with Baidu, two attributes must be provided: ChannelId and UserId. The token field must also contain the ChannelId. For more information, see Creating an Amazon SNS Endpoint for Baidu. 

<details><summary>Parameters</summary>

#### $body

Input for CreatePlatformEndpoint action.

**Type:** object

</details>

## create_topic

Creates a topic to which notifications can be published. Users can create at most 100,000 topics. For more information, see http://aws.amazon.com/sns. This action is idempotent, so if the requester already owns a topic with the specified name, that topic's ARN is returned without creating a new topic.

<details><summary>Parameters</summary>

#### $body

Input for CreateTopic action.

**Type:** object

</details>

## delete_endpoint

Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent. For more information, see Using Amazon SNS Mobile Push Notifications.  
When you delete an endpoint that is also subscribed to a topic, then you must also unsubscribe the endpoint from the topic.

<details><summary>Parameters</summary>

#### $body

Input for DeleteEndpoint action.

**Type:** object

</details>

## delete_platform_application

Deletes a platform application object for one of the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications. 

<details><summary>Parameters</summary>

#### $body

Input for DeletePlatformApplication action.

**Type:** object

</details>

## delete_topic

Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages previously sent to the topic from being delivered to subscribers. This action is idempotent, so deleting a topic that does not exist does not result in an error.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_endpoint_attributes

Retrieves the endpoint attributes for a device on one of the supported push notification services, such as GCM and APNS. For more information, see Using Amazon SNS Mobile Push Notifications. 

<details><summary>Parameters</summary>

#### $body

Input for GetEndpointAttributes action.

**Type:** object

</details>

## get_platform_application_attributes

Retrieves the attributes of the platform application object for the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications. 

<details><summary>Parameters</summary>

#### $body

Input for GetPlatformApplicationAttributes action.

**Type:** object

</details>

## get_sms_attributes

Returns the settings for sending SMS messages from your account. 
These settings are set with the SetSMSAttributes action.

<details><summary>Parameters</summary>

#### $body

The input for the GetSMSAttributes request.

**Type:** object

</details>

## get_subscription_attributes

Returns all of the properties of a subscription.

<details><summary>Parameters</summary>

#### $body

Input for GetSubscriptionAttributes.

**Type:** object

</details>

## get_topic_attributes

Returns all of the properties of a topic. Topic properties returned might differ based on the authorization of the user.

<details><summary>Parameters</summary>

#### $body

Input for GetTopicAttributes action.

**Type:** object

</details>

## list_endpoints_by_platform_application

Lists the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM and APNS. The results for ListEndpointsByPlatformApplication are paginated and return a limited list of endpoints, up to 100. If additional records are available after the first page results, then a NextToken string will be returned. To receive the next page, you call ListEndpointsByPlatformApplication again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null. For more information, see Using Amazon SNS Mobile Push Notifications.  
This action is throttled at 30 transactions per second (TPS).

<details><summary>Parameters</summary>

#### $body

Input for ListEndpointsByPlatformApplication action.

**Type:** object

</details>

## list_phone_numbers_opted_out

Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to them. 
The results for ListPhoneNumbersOptedOut are paginated, and each page returns up to 100 phone numbers. If additional phone numbers are available after the first page of results, then a NextToken string will be returned. To receive the next page, you call ListPhoneNumbersOptedOut again using the NextToken string received from the previous call. When there are no more records to return, NextToken will be null.

<details><summary>Parameters</summary>

#### $body

The input for the ListPhoneNumbersOptedOut action.

**Type:** object

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

#### $body

Input for ListSubscriptionsByTopic action.

**Type:** object

</details>

## list_topics

Returns a list of the requester's topics. Each call returns a limited list of topics, up to 100. If there are more topics, a NextToken is also returned. Use the NextToken parameter in a new ListTopics call to get further results. 
This action is throttled at 30 transactions per second (TPS).

*This operation has no parameters*

## opt_in_phone_number

Use this request to opt in a phone number that is opted out, which enables you to resume sending SMS messages to the number. 
You can opt in a phone number only once every 30 days.

<details><summary>Parameters</summary>

#### $body

Input for the OptInPhoneNumber action.

**Type:** object

</details>

## publish

Sends a message to an Amazon SNS topic or sends a text message (SMS message) directly to a phone number.  
If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint. 
When a messageId is returned, the message has been saved and Amazon SNS will attempt to deliver it shortly. 
To use the Publish action for sending a message to a mobile endpoint, such as an app on a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn parameter. The EndpointArn is returned when making a call with the CreatePlatformEndpoint action.  
For more information about formatting messages, see Send Custom Platform-Specific Payloads in Messages to Mobile Devices. 

<details><summary>Parameters</summary>

#### $body

Input for Publish action.

**Type:** object

</details>

## remove_permission

Removes a statement from a topic's access control policy.

<details><summary>Parameters</summary>

#### $body

Input for RemovePermission action.

**Type:** object

</details>

## set_endpoint_attributes

Sets the attributes for an endpoint for a device on one of the supported push notification services, such as GCM and APNS. For more information, see Using Amazon SNS Mobile Push Notifications. 

<details><summary>Parameters</summary>

#### $body

Input for SetEndpointAttributes action.

**Type:** object

</details>

## set_platform_application_attributes

Sets the attributes of the platform application object for the supported push notification services, such as APNS and GCM. For more information, see Using Amazon SNS Mobile Push Notifications. For information on configuring attributes for message delivery status, see Using Amazon SNS Application Attributes for Message Delivery Status. 

<details><summary>Parameters</summary>

#### $body

Input for SetPlatformApplicationAttributes action.

**Type:** object

</details>

## set_sms_attributes

Use this request to set the default settings for sending SMS messages and receiving daily SMS usage reports. 
You can override some of these settings for a single message when you use the Publish action with the MessageAttributes.entry.N parameter. For more information, see Sending an SMS Message in the Amazon SNS Developer Guide.

<details><summary>Parameters</summary>

#### $body

The input for the SetSMSAttributes action.

**Type:** object

</details>

## set_subscription_attributes

Allows a subscription owner to set an attribute of the subscription to a new value.

<details><summary>Parameters</summary>

#### $body

Input for SetSubscriptionAttributes action.

**Type:** object

</details>

## set_topic_attributes

Allows a topic owner to set an attribute of the topic to a new value.

<details><summary>Parameters</summary>

#### $body

Input for SetTopicAttributes action.

**Type:** object

</details>

## subscribe

Prepares to subscribe an endpoint by sending the endpoint a confirmation message. To actually create a subscription, the endpoint owner must call the ConfirmSubscription action with the token from the confirmation message. Confirmation tokens are valid for three days. 
This action is throttled at 100 transactions per second (TPS).

<details><summary>Parameters</summary>

#### $body

Input for Subscribe action.

**Type:** object

</details>

## unsubscribe

Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic's owner can unsubscribe, and an AWS signature is required. If the Unsubscribe call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint, so that the endpoint owner can easily resubscribe to the topic if the Unsubscribe request was unintended. 
This action is throttled at 100 transactions per second (TPS).

<details><summary>Parameters</summary>

#### $body

Input for Unsubscribe action.

**Type:** object

</details>

