---
id: twilio-documentation
title: Twilio (version v1.*.*)
sidebar_label: Twilio
layout: docs.mustache
---

## add_credential_to_list

Add a Credential to the CredentialList. When creating a Credential, you will POST both a username and password, but only receive the username back in the response. The password is intentionally not returned so as to protect it.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CLSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## add_incoming_phone_number_local

Adds a new phone number to your account. If a phone number is found for your request, Twilio will add it to your account and bill you for the first month's cost of the phone number.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

</details>

## add_incoming_phone_number_mobile

Adds a new phone number to your account. If a phone number is found for your request, Twilio will add it to your account and bill you for the first month's cost of the phone number.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

</details>

## add_incoming_phone_number_tollfree

Adds a new phone number to your account. If a phone number is found for your request, Twilio will add it to your account and bill you for the first month's cost of the phone number.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

</details>

## add_ip_address_to_list

Add an IP Address to the list with a description.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IpAccessControlListSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## add_outgoing_caller_id

Adds a new CallerID to your account.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## change_password_for_credential

Change the password of a Credential record. If the change is successful, Twilio will respond with the Credential record but will not include the password in the response.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CLSid (required)

**Type:** string

#### CredentialSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## create_account

Create a new Account instance resource as a subaccount of the one used to make the request. See Creating Subaccounts for more information.

<details><summary>Parameters</summary>

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## create_app

Creates a new application within your account.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## create_credential_list

Create a new Credential List.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## create_credential_list_mapping

Map a CredentialList to the domain.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### SipDomainSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## create_domain

Creates a new Domain and returns its instance resource. You must pick a unique domain name that ends in ".sip.twilio.com". After creating a Domain, you must map it to an authentication method before the domain is ready to receive traffic.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## create_incoming_phone_number

Purchases a new phone number for your account. If a phone number is found for your request, Twilio will add it to your account and bill you for the first month's cost of the phone number. To find an available phone number to POST, use the subresources of the AvailablePhoneNumbers list resource.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## create_ip_access_control_list

Create a new IpAccessControlList resource. When created, the list will contain no IP addresses. You will need to add IP addresses to the list for it to be active. To add IP addresses, you will need to POST to the IpAddresses List subresource.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

</details>

## create_ip_access_control_list_mapping

Map an IpAccessControlList to this domain.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### SipDomainSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

</details>

## create_queue

Create a new Queue resource.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## create_usage_trigger

Creates a new UsageTrigger. Each account can create up to 1,000 UsageTriggers. Currently, UsageTriggers that are no longer active are not deleted automatically. Use DELETE to delete triggers you no longer need.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_application

Delete this application.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### ApplicationSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_credential_from_list

Remove a Credential from a CredentialList.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CLSid (required)

**Type:** string

#### CredentialSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_credential_list

Delete a CredentialList from your account. It can only be deleted if no domains are mapped to it. If you attempt to delete one that is mapped to a domain, you will receive an error.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CLSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_credential_list_mapping

Remove a CredentialListMapping from a domain

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CLSid (required)

**Type:** string

#### SipDomainSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_domain

Delete a domain. If you have created subdomains of a domain, you will not be able to delete the domain until you first delete all subdomains of it.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### SipDomainSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_ip_access_control_list

Delete an IpAccessControlList from your account. It can only be deleted if no domains are mapped to it. If you attempt to delete one that is mapped to a domain, you will receive an error.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IpAccessControlListSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_ip_access_control_list_mapping

Remove a mapping from this domain.

<details><summary>Parameters</summary>

#### ALSid (required)

**Type:** string

#### AccountSid (required)

**Type:** string

#### SipDomainSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_ip_address_from_list

Deletes an IP address entry from the list.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IpAccessControlListSid (required)

**Type:** string

#### IpAddressSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_notification

Deletes the notification identified by {NotificationSid} from an account's log.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### NotificationSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_outgoing_caller_id

Deletes the caller ID from the account. Returns an HTTP 204 response if successful, with no body.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### OutgoingCallerIdSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_queue

The DELETE method allows you to remove a Queue. Only empty queues are deletable.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### QueueSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## delete_recording

Deletes a recording from your account.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### RecordingSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

**Potential values:** .xml, .wav, .mp3

</details>

## delete_transcription

Deletes a transcription from your account.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### TranscriptionSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html, .txt, .xml

</details>

## delete_usage_trigger

Delete this UsageTrigger.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### UsageTriggerSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## dequeue_front_member_of_queue

Posting a URL and Method to a Queue instance will dequeue a member from a queue and have the member's call begin executing the TwiML document at that URL When dequeuing the 'Front' of the queue, the next call in the queue will be redirected.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### QueueSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## dequeue_member_of_queue

Posting a URL and Method to a Queue instance will dequeue a member from a queue and have the member's call begin executing the TwiML document at that URL When redirecting a member of a queue addressed by CallSid, only the first request will succeed and return a 200 response code. A second request will fail and return an appropriate 400 response code.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CallSid (required)

**Type:** string

#### QueueSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_account

Returns a representation of an account.

<details><summary>Parameters</summary>

#### AccountSid (required)

A 34 character string that uniquely identifies this account.

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_app_properties

Get the properties of the authorized application.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### ConnectAppSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_application

Get application instance resource.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### ApplicationSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_call

Returns the single Call resource identified by {CallSid}.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CallSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_conference

Returns a representation of the conference identified by {ConferenceSid}.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### ConferenceSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_connect_app_properties

Get the properties of a Connect App.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### ConnectAppSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_credential_in_list

Get a specific Credential in a list. Though a password is stored for each username in your list, the password is not returned to protect your password. If you cannot remember your password, you will need to POST to this resource to update it.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CLSid (required)

**Type:** string

#### CredentialSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_credential_list

Get a credential list instance resource

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CLSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_domain

Return a specific instance by Sid.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### SipDomainSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_front_member_of_queue

Get a front member.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### QueueSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_incoming_phone_number

Get info about incoming call's phone number.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IncomingPhoneNumberSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_ip_access_control_list

Return a specific IpAccessControlList resource.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IpAccessControlListSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_ip_access_control_list_mapping

Return a specific IpAccessControlListMapping instance by Sid.

<details><summary>Parameters</summary>

#### ALSid (required)

**Type:** string

#### AccountSid (required)

**Type:** string

#### SipDomainSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_ip_address_from_list

Return a single IP Address resource.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IpAccessControlListSid (required)

**Type:** string

#### IpAddressSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_media_for_message

Without an extension, the media is returned using the mime-type provided when the media was generated.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### MediaSid (required)

**Type:** string

#### MessageSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_member_of_queue

Get a specific member.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CallSid (required)

**Type:** string

#### QueueSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_message

Returns a single message specified by the provided {MessageSid}.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### MessageSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_notification

Get a notification entry.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### NotificationSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_outgoing_caller_id

Get Outgoing Caller ID Details

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### OutgoingCallerIdSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_participant

Returns a representation of this participant.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CallSid (required)

**Type:** string

#### ConferenceSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_queue

Get resource's individual Queue instance.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### QueueSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_recording

Returns one of several representations: Without an extension, or with a ".wav", a binary WAV audio file is returned with mime-type "audio/x-wav". Appending ".mp3" to the URI returns a binary MP3 audio file with mime-type type "audio/mpeg". Appending ".xml" to the URI returns a XML representation.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### RecordingSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

**Potential values:** .xml, .wav, .mp3

</details>

## get_shortcode

Get a single shortcode.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### ShortCodeSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## get_transcription

Returns a single Transcription resource representation identified by the given {TranscriptionSid}. By default Twilio will respond with the XML metadata for the Transcription. If you append ".txt" to the end of the Transcription resource's URI Twilio will just return you the transcription tex.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### TranscriptionSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html, .txt, .xml

</details>

## get_usage_trigger

Returns a repesentation of the UsageTrigger.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### UsageTriggerSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_accounts

Retrieve a list of the Account resources belonging to the account used to make the API request. This list will include that Account as well.

<details><summary>Parameters</summary>

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_all_usage_records

Returns UsageRecords for all usage categories. The list includes paging information. By default, the UsageRecords resource will return one UsageRecord for each Category, representing all usage accrued all-time for the account. You can filter the usage Category or change the date-range over which usage is counted using optional GET query parameters.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_app_resources

Returns a list of Application resource representations, each representing an application within your account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_available_phone_numbers

Returns a list of all AvailablePhoneNumber subresources for your account by ISO Country. For full information about our phone number support, see our Phone Number CSV (http://www.twilio.com/resources/rates/international-phone-number-rates.csv).

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_available_phone_numbers_local

Returns a list of local AvailablePhoneNumber resource representations that match the specified filters, each representing a phone number tha is currently available for provisioning within your account.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IsoCountryCode (required)

ISO 3166-1 alpha-2.

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_available_phone_numbers_mobile

Returns a list of mobile AvailablePhoneNumber resource representations that match the specified filters, each representing a phone number that is currently available for provisioning within your account.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IsoCountryCode (required)

ISO 3166-1 alpha-2.

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_available_phone_numbers_tollfree

Returns a list of toll-free AvailablePhoneNumber elements that match the specified filters, each representing a phone number that is currently available for provisioning within your account. To provision an available phone number, POST the number to the IncomingPhoneNumbers resource.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IsoCountryCode (required)

ISO 3166-1 alpha-2.

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_call_notifications

Returns a list of notifications generated for an account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CallSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_call_recordings

Returns a list of Recording resource representations, each representing a recording generated during the course of a phone call.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CallSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_calls

Returns a list of phone calls made to and from the account identified by {AccountSid}.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_conferences

Returns a list of conferences within an account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_connect_app_resources

Returns a list of Connect App resource representations, each representing a Connect App you've authorized to access your account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_connect_apps

Returns a list of Connect App resource representations, each representing a Connect App in your account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_credential_list_mappings

Get the user lists mapped to this domain.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### SipDomainSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_credential_lists

Gets a list of Credential Lists for an account

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_credentials_in_list

Get the list of Credentials in a CredentialList. The passwords for the Credentials are intentionally not returned so as to protect them.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CLSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_domains

Returns a paged list of the domains for an account.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_incoming_phone_numbers

Returns a list of IncomingPhoneNumber resource representations, each representing a phone number given to your account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_incoming_phone_numbers_local

Returns a list of local  elements, each representing a local (not toll-free) phone number given to your account, under an  list element that includes paging information. Works exactly the same as the IncomingPhoneNumber resource, but filters out toll-free numbers.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

</details>

## list_incoming_phone_numbers_mobile

Returns a list of local  elements, each representing a mobile phone number given to your account, under an  list element that includes paging information. Works exactly the same as the IncomingPhoneNumber resource, but filters out local and toll free numbers.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

</details>

## list_incoming_phone_numbers_tollfree

Returns a list of local  elements, each representing a toll-free phone number given to your account, under an  list element that includes paging information. Works exactly the same as the IncomingPhoneNumber resource, but filters out all numbers that aren't toll-free.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

</details>

## list_ip_access_control_list_mappings

Return the IpAccessControlListMappings that are associated to this domain.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### SipDomainSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

</details>

## list_ip_access_control_lists

Return a paged list of all IpAccessControlLists under this account.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

**Type:** string

</details>

## list_ip_addresses_in_list

List the IP Addresses contained in this list.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IpAccessControlListSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_media_for_message

Returns a list of media associated with your message.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### MessageSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_members_of_queue

Returns the list of members in the queue identified by {QueueSid}.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### QueueSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_messages

Returns a list of messages associated with your account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_notifications

Returns a list of notifications generated for an account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_outgoing_caller_ids

Returns a list of OutgoingCallerId resource representations, each representing a Caller ID number valid for an account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_participants

Returns the list of participants in the conference identified by {ConferenceSid}.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### ConferenceSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_queues

Returns a list of queues within an account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_recording_transcriptions

Returns a set of Transcription resource representations that includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### RecordingSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_recordings

Returns a list of Recording resource representations, each representing a recording generated during the course of a phone call.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_shortcodes

Returns a list of ShortCode resource representations, each representing a short code within your account. The list includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_transcriptions

Returns a set of Transcription resource representations that includes paging information.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_usage_records_for_subresource

Returns UsageRecords for all usage categories for a specified subresource.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### Subresource (required)

|Subresource|Description| |---|---| |Daily|Return multiple UsageRecords for each usage category, each representing usage over a daily time-interval.| |Monthly|Return multiple UsageRecords for each usage category, each representing usage over a monthly time-interval.| |Yearly|Return multple UsageRecords for each usage category, each representing usage over a yearly time-interval.| |AllTime| Return a single UsageRecord for each usage category, each representing usage over the date-range specified. This is the same as the root /Usage/Records.| |Today|Return a single UsageRecord per usage category, for today's usage only.| ||Yesterday|Return a single UsageRecord per usage category, for yesterday's usage only.| |ThisMonth|Return a single UsageRecord per usage category, for this month's usage only.| |LastMonth|Return a single UsageRecord per usage category, for last month's usage only.|

**Type:** string

**Potential values:** Daily, Monthly, Yearly, AllTime, Today, Yesterday, ThisMonth, LastMonth

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## list_usage_triggers

Returns a list of UsageTrigger resource representations. The list includes paging information. By default, all UsageTriggers are returned. You can filter the list by specifying one or more query parameters. Note that the query parameters are case-sensitive

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## modify_call

Modify a phone call.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CallSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## place_call

To make a call, make an HTTP POST request. Initiate a new phone call.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

#### $body

**Type:** object

</details>

## release_incoming_phone_number

Release this phone number from your account. Twilio will no longer answer calls to this number, and you will stop being billed the monthly phone number fee. The phone number will eventually be recycled and potentially given to another customer, so use with care. If you make a mistake, contac us. We may be able to give you the number back.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IncomingPhoneNumberSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## remove_participant_from_conference

Kick this participant from the conference.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CallSid (required)

**Type:** string

#### ConferenceSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## rename_ip_access_control_list

Rename an IpAccessControlList.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IpAccessControlListSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## send_message

To send a new outgoing message, make an HTTP POST to your Messages list resource URI

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

#### $body

**Type:** object

</details>

## update_account

Allows you to modify the properties of an account.

<details><summary>Parameters</summary>

#### AccountSid (required)

A 34 character string that uniquely identifies this account.

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_app_properties

Tries to update the application's properties, and returns the updated resource representation if successful. The returned response is identical to that returned above when making a GET request.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### ApplicationSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_connect_app_properties

Tries to update the Connect App's properties, and returns the updated resource representation if successful. The returned response is identical to that returned above when making a GET request.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### ConnectAppSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_credential_list

Change the FriendlyName of the list

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CLSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_domain

Update the attributes of a domain.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### SipDomainSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_incoming_phone_number

Tries to update the incoming phone number's properties, and returns the updated resource representation if successful. The returned response is identical to that returned above when making a GET request.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IncomingPhoneNumberSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_ip_address_in_list

Change the description or IP address of a given IpAddress instance resource

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### IpAccessControlListSid (required)

**Type:** string

#### IpAddressSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_outgoing_caller_id

Updates the caller id, and returns the updated resource if successful.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### OutgoingCallerIdSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_participant

Updates the status of a participant.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### CallSid (required)

**Type:** string

#### ConferenceSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_queue

This POST request allows you to change the FriendlyName or MaxSize.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### QueueSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_shortcode

Tries to update the shortcode's properties, and returns the updated resource representation if successful.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### ShortCodeSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

## update_usage_trigger

Tries to update the UsageTrigger's properties, and returns the updated resource representation if successful.

<details><summary>Parameters</summary>

#### AccountSid (required)

**Type:** string

#### UsageTriggerSid (required)

**Type:** string

#### mediaTypeExtension (required)

By default, Twilio's REST API returns XML. You may obtain CSV, JSON or HTML by appending ".csv", ".json", or ".html".

**Type:** string

**Potential values:** .json, .csv, .html

</details>

