---
id: google-mail-documentation
title: Google Mail (version v4.*.*)
sidebar_label: Google Mail
layout: docs.mustache
---

## construct_message



<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### bodyParts

A map of MIME Content-Types to content.

**Type:** OBJECT

### cc

**Type:** STRING

### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

### deleted

**Type:** BOOLEAN

### draftId

**Type:** STRING

### from

**Type:** STRING

### internalDateSource

**Type:** STRING

### message

**Type:** STRING

### neverMarkSpam

**Type:** BOOLEAN

### processForCalendar

**Type:** BOOLEAN

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## create_alias

Creates a custom "from" send-as alias. If an SMTP MSA is specified, Gmail will attempt to connect to the SMTP service to validate the configuration before creating the alias. If ownership verification is required for the alias, a message will be sent to the email address and the resource's verification status will be set to pending; otherwise, the resource will be created with verification status set to accepted. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### $body

Settings associated with a send-as alias, which can be either the primary login address associated with the account or a custom "from" address. Send-as aliases correspond to the "Send Mail As" feature in the web interface.

**Type:** object

```json
{
  "isDefault" : "Whether this address is selected as the default \"From:\" address in situations such as composing a new message or sending a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients may write to this field is true. Changing this from false to true for an address will result in this field becoming false for the other previous default address.",
  "signature" : "An optional HTML signature that is included in messages composed with this alias in the Gmail web UI.",
  "verificationStatus" : "Indicates whether this address has been verified for use as a send-as alias. Read-only. This setting only applies to custom \"from\" aliases.",
  "displayName" : "A name that appears in the \"From:\" header for mail sent using this alias. For custom \"from\" addresses, when this is empty, Gmail will populate the \"From:\" header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.",
  "isPrimary" : "Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases. This field is read-only.",
  "sendAsEmail" : "The email address that appears in the \"From:\" header for mail sent using this alias. This is read-only for all operations except create.",
  "smtpMsa" : {
    "password" : "The password that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses.",
    "port" : "The port of the SMTP service. Required.",
    "host" : "The hostname of the SMTP service. Required.",
    "securityMode" : "The protocol that will be used to secure communication with the SMTP service. Required.",
    "username" : "The username that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses."
  },
  "replyToAddress" : "An optional email address that is included in a \"Reply-To:\" header for mail sent using this alias. If this is empty, Gmail will not generate a \"Reply-To:\" header.",
  "treatAsAlias" : "Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom \"from\" aliases."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_delegate

Adds a delegate with its verification status set directly to accepted, without sending any verification email. The delegate user must be a member of the same G Suite organization as the delegator user.

Gmail imposes limtations on the number of delegates and delegators each user in a G Suite organization can have. These limits depend on your organization, but in general each user can have up to 25 delegates and up to 10 delegators.

Note that a delegate user must be referred to by their primary email address, and not an email alias.

Also note that when a new delegate is created, there may be up to a one minute delay before the new delegate is available for use.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### $body

Settings for a delegate. Delegates can read, send, and delete messages, as well as view and add contacts, for the delegator's account. See "Set up mail delegation" for more information about delegates.

**Type:** object

```json
{
  "verificationStatus" : "Indicates whether this address has been verified and can act as a delegate for the account. Read-only.",
  "delegateEmail" : "The email address of the delegate."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_draft

Creates a new draft with the DRAFT label.

<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### cc

**Type:** STRING

### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

### from

**Type:** STRING

### message

**Type:** STRING

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## create_draft_multipart

Creates a new multipart draft with the DRAFT label.

<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### bodyParts

A map of MIME Content-Types to content. Best practices suggest ordering from simplest to fanciest format.

**Type:** OBJECT

### cc

**Type:** STRING

### contentType

A multipart Content-Type. Default is multipart/alternative.

**Type:** STRING

### from

**Type:** STRING

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## create_filter

Creates a filter.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### $body

Resource definition for Gmail filters. Filters apply to specific messages instead of an entire email thread.

**Type:** object

```json
{
  "criteria" : {
    "hasAttachment" : "Whether the message has any attachment.",
    "excludeChats" : "Whether the response should exclude chats.",
    "size" : "The size of the entire RFC822 message in bytes, including all headers and attachments.",
    "sizeComparison" : "How the message size in bytes should be in relation to the size field.",
    "subject" : "Case-insensitive phrase found in the message's subject. Trailing and leading whitespace are be trimmed and adjacent spaces are collapsed.",
    "query" : "Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, \"from:someuser@example.com rfc822msgid: is:unread\".",
    "from" : "The sender's display name or email address.",
    "to" : "The recipient's display name or email address. Includes recipients in the \"to\", \"cc\", and \"bcc\" header fields. You can use simply the local part of the email address. For example, \"example\" and \"example@\" both match \"example@gmail.com\". This field is case-insensitive.",
    "negatedQuery" : "Only return messages not matching the specified query. Supports the same query format as the Gmail search box. For example, \"from:someuser@example.com rfc822msgid: is:unread\"."
  },
  "action" : {
    "addLabelIds" : [ "string" ],
    "forward" : "Email address that the message should be forwarded to.",
    "removeLabelIds" : [ "string" ]
  },
  "id" : "The server assigned ID of the filter."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_forwarding_address

Creates a forwarding address. If ownership verification is required, a message will be sent to the recipient and the resource's verification status will be set to pending; otherwise, the resource will be created with verification status set to accepted.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### $body

Settings for a forwarding address.

**Type:** object

```json
{
  "verificationStatus" : "Indicates whether this address has been verified and is usable for forwarding. Read-only.",
  "forwardingEmail" : "An email address to which messages can be forwarded."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_label

Creates a new label.

<details><summary>Parameters</summary>

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### $body

Labels are used to categorize messages and threads within the user's mailbox.

**Type:** object

```json
{
  "messageListVisibility" : "The visibility of the label in the message list in the Gmail web interface.",
  "messagesUnread" : "The number of unread messages with the label.",
  "threadsUnread" : "The number of unread threads with the label.",
  "color" : {
    "backgroundColor" : "The background color represented as hex string #RRGGBB (ex #000000). This field is required in order to set the color of a label. Only the following predefined set of color values are allowed:\n#000000, #434343, #666666, #999999, #cccccc, #efefef, #f3f3f3, #ffffff, #fb4c2f, #ffad47, #fad165, #16a766, #43d692, #4a86e8, #a479e2, #f691b3, #f6c5be, #ffe6c7, #fef1d1, #b9e4d0, #c6f3de, #c9daf8, #e4d7f5, #fcdee8, #efa093, #ffd6a2, #fce8b3, #89d3b2, #a0eac9, #a4c2f4, #d0bcf1, #fbc8d9, #e66550, #ffbc6b, #fcda83, #44b984, #68dfa9, #6d9eeb, #b694e8, #f7a7c0, #cc3a21, #eaa041, #f2c960, #149e60, #3dc789, #3c78d8, #8e63ce, #e07798, #ac2b16, #cf8933, #d5ae49, #0b804b, #2a9c68, #285bac, #653e9b, #b65775, #822111, #a46a21, #aa8831, #076239, #1a764d, #1c4587, #41236d, #83334c",
    "textColor" : "The text color of the label, represented as hex string. This field is required in order to set the color of a label. Only the following predefined set of color values are allowed:\n#000000, #434343, #666666, #999999, #cccccc, #efefef, #f3f3f3, #ffffff, #fb4c2f, #ffad47, #fad165, #16a766, #43d692, #4a86e8, #a479e2, #f691b3, #f6c5be, #ffe6c7, #fef1d1, #b9e4d0, #c6f3de, #c9daf8, #e4d7f5, #fcdee8, #efa093, #ffd6a2, #fce8b3, #89d3b2, #a0eac9, #a4c2f4, #d0bcf1, #fbc8d9, #e66550, #ffbc6b, #fcda83, #44b984, #68dfa9, #6d9eeb, #b694e8, #f7a7c0, #cc3a21, #eaa041, #f2c960, #149e60, #3dc789, #3c78d8, #8e63ce, #e07798, #ac2b16, #cf8933, #d5ae49, #0b804b, #2a9c68, #285bac, #653e9b, #b65775, #822111, #a46a21, #aa8831, #076239, #1a764d, #1c4587, #41236d, #83334c"
  },
  "threadsTotal" : "The total number of threads with the label.",
  "name" : "The display name of the label.",
  "id" : "The immutable ID of the label.",
  "labelListVisibility" : "The visibility of the label in the label list in the Gmail web interface.",
  "type" : "The owner type for the label. User labels are created by the user and can be modified and deleted by the user and can be applied to any message or thread. System labels are internally created and cannot be added, modified, or deleted. System labels may be able to be applied to or removed from messages and threads under some circumstances but this is not guaranteed. For example, users can apply and remove the INBOX and UNREAD labels from messages and threads, but cannot apply or remove the DRAFTS or SENT labels from messages or threads.",
  "messagesTotal" : "The total number of messages with the label."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_alias

Deletes the specified send-as alias. Revokes any verification that may have been required for using it.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### sendAsEmail (required)

The send-as alias to be deleted.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_delegate

Removes the specified delegate (which can be of any verification status), and revokes any verification that may have been required for using it.

Note that a delegate user must be referred to by their primary email address, and not an email alias.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### delegateEmail (required)

The email address of the user to be removed as a delegate.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_draft

Immediately and permanently deletes the specified draft. Does not simply trash it.

<details><summary>Parameters</summary>

### id (required)

The ID of the draft to delete.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_filter

Deletes a filter.

<details><summary>Parameters</summary>

### id (required)

The ID of the filter to be deleted.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_forwarding_address

Deletes the specified forwarding address and revokes any verification that may have been required.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### forwardingEmail (required)

The forwarding address to be deleted.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_label

Immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to.

<details><summary>Parameters</summary>

### id (required)

The ID of the label to delete.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_message

Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer messages.trash instead.

<details><summary>Parameters</summary>

### id (required)

The ID of the message to delete.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_messages

Deletes many messages by message ID. Provides no guarantees that messages were not already deleted or even existed at all.

<details><summary>Parameters</summary>

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### $body

**Type:** object

```json
{
  "ids" : [ "string" ]
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_smime_for_alias

Deletes the specified S/MIME config for the specified send-as alias.

<details><summary>Parameters</summary>

### id (required)

The immutable ID for the SmimeInfo.

**Type:** string

### sendAsEmail (required)

The email address that appears in the "From:" header for mail sent using this alias.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_thread

Immediately and permanently deletes the specified thread. This operation cannot be undone. Prefer threads.trash instead.

<details><summary>Parameters</summary>

### id (required)

ID of the Thread to delete.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_alias

Gets the specified send-as alias. Fails with an HTTP 404 error if the specified address is not a member of the collection.

<details><summary>Parameters</summary>

### sendAsEmail (required)

The send-as alias to be retrieved.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_attachment

Gets the specified message attachment.

<details><summary>Parameters</summary>

### id (required)

The ID of the attachment.

**Type:** string

### messageId (required)

The ID of the message containing the attachment.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_auto_forwarding

Gets the auto-forwarding setting for the specified account.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_delegate

Gets the specified delegate.

Note that a delegate user must be referred to by their primary email address, and not an email alias.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### delegateEmail (required)

The email address of the user whose delegate relationship is to be retrieved.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_draft

Gets the specified draft.

<details><summary>Parameters</summary>

### id (required)

The ID of the draft to retrieve.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### format

The format to return the draft in.

**Type:** string

**Potential values:** full, metadata, minimal, raw

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_filter

Gets a filter.

<details><summary>Parameters</summary>

### id (required)

The ID of the filter to be fetched.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_forwarding_address

Gets the specified forwarding address.

<details><summary>Parameters</summary>

### forwardingEmail (required)

The forwarding address to be retrieved.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_imap_settings

Gets IMAP settings.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_label

Gets the specified label.

<details><summary>Parameters</summary>

### id (required)

The ID of the label to retrieve.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_message

Gets the specified message.

<details><summary>Parameters</summary>

### id (required)

The ID of the message to retrieve.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### format

The format to return the message in.

**Type:** string

**Potential values:** full, metadata, minimal, raw

### metadataHeaders

When given and format is METADATA, only include headers specified.

**Type:** array

```json
[ "string" ]
```

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_pop_settings

Gets POP settings.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_profile

Gets the current user's Gmail profile.

<details><summary>Parameters</summary>

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_smime_for_alias

Gets the specified S/MIME config for the specified send-as alias.

<details><summary>Parameters</summary>

### id (required)

The immutable ID for the SmimeInfo.

**Type:** string

### sendAsEmail (required)

The email address that appears in the "From:" header for mail sent using this alias.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_thread

Gets the specified thread.

<details><summary>Parameters</summary>

### id (required)

The ID of the thread to retrieve.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### format

The format to return the messages in.

**Type:** string

**Potential values:** full, metadata, minimal

### metadataHeaders

When given and format is METADATA, only include headers specified.

**Type:** array

```json
[ "string" ]
```

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_vacation_settings

Gets vacation responder settings.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## import_message

Imports a message into only this user''s mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. Does not send a message.

<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### cc

**Type:** STRING

### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

### deleted

**Type:** BOOLEAN

### from

**Type:** STRING

### internalDateSource

**Type:** STRING

### message

**Type:** STRING

### neverMarkSpam

**Type:** BOOLEAN

### processForCalendar

**Type:** BOOLEAN

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## import_message_multipart

Imports a multipart message into only this user''s mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. Does not send a message.

<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### bodyParts

A map of MIME Content-Types to content. Best practices suggest ordering from simplest to fanciest format.

**Type:** OBJECT

### cc

**Type:** STRING

### contentType

A multipart Content-Type. Default is multipart/alternative.

**Type:** STRING

### deleted

**Type:** BOOLEAN

### from

**Type:** STRING

### internalDateSource

**Type:** STRING

### neverMarkSpam

**Type:** BOOLEAN

### processForCalendar

**Type:** BOOLEAN

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## insert_message

Directly inserts a message into only this user''s mailbox similar to IMAP APPEND, bypassing most scanning and classification. Does not send a message.

<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### cc

**Type:** STRING

### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

### deleted

**Type:** BOOLEAN

### from

**Type:** STRING

### internalDateSource

**Type:** STRING

### message

**Type:** STRING

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## insert_message_multipart

Directly inserts a multipart message into only this user''s mailbox similar to IMAP APPEND, bypassing most scanning and classification. Does not send a message.

<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### bodyParts

A map of MIME Content-Types to content. Best practices suggest ordering from simplest to fanciest format.

**Type:** OBJECT

### cc

**Type:** STRING

### contentType

A multipart Content-Type. Default is multipart/alternative.

**Type:** STRING

### deleted

**Type:** BOOLEAN

### from

**Type:** STRING

### internalDateSource

**Type:** STRING

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## insert_smime_for_alias

Insert (upload) the given S/MIME config for the specified send-as alias. Note that pkcs12 format is required for the key.

<details><summary>Parameters</summary>

### sendAsEmail (required)

The email address that appears in the "From:" header for mail sent using this alias.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### $body

An S/MIME email config.

**Type:** object

```json
{
  "issuerCn" : "The S/MIME certificate issuer's common name.",
  "isDefault" : "Whether this SmimeInfo is the default one for this user's send-as address.",
  "pem" : "PEM formatted X509 concatenated certificate string (standard base64 encoding). Format used for returning key, which includes public key as well as certificate chain (not private key).",
  "expiration" : "When the certificate expires (in milliseconds since epoch).",
  "id" : "The immutable ID for the SmimeInfo.",
  "encryptedKeyPassword" : "Encrypted key password, when key is encrypted.",
  "pkcs12" : "PKCS#12 format containing a single private/public key pair and certificate chain. This format is only accepted from client for creating a new SmimeInfo and is never returned, because the private key is not intended to be exported. PKCS#12 may be encrypted, in which case encryptedKeyPassword should be set appropriately."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_aliases

Lists the send-as aliases for the specified account. The result includes the primary send-as address associated with the account as well as any custom "from" aliases.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_delegates

Lists the delegates for the specified account.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_drafts

Lists the drafts in the user's mailbox.

<details><summary>Parameters</summary>

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeSpamTrash

Include drafts from SPAM and TRASH in the results.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### q

Only return draft messages matching the specified query. Supports the same query format as the Gmail search box. For example, "from:someuser@example.com rfc822msgid: is:unread".

**Type:** string

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_filters

Lists the message filters of a Gmail user.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_forwarding_addresses

Lists the forwarding addresses for the specified account.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_history_of_mailbox

Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing historyId).

<details><summary>Parameters</summary>

### startHistoryId (required)

Required. Returns history records after the specified startHistoryId. The supplied startHistoryId should be obtained from the historyId of a message, thread, or previous list response. History IDs increase chronologically but are not contiguous with random gaps in between valid IDs. Supplying an invalid or out of date startHistoryId typically returns an HTTP 404 error code. A historyId is typically valid for at least a week, but in some rare circumstances may be valid for only a few hours. If you receive an HTTP 404 error response, your application should perform a full sync. If you receive no nextPageToken in the response, there are no updates to retrieve and you can store the returned historyId for a future request.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### historyTypes

History types to be returned by the function

**Type:** array

```json
[ "string. Possible values: labelAdded | labelRemoved | messageAdded | messageDeleted" ]
```

### labelId

Only return messages with a label matching the ID.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_labels

Lists all labels in the user's mailbox.

<details><summary>Parameters</summary>

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_messages

Lists the messages in the user's mailbox.

<details><summary>Parameters</summary>

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeSpamTrash

Include messages from SPAM and TRASH in the results.

**Type:** boolean

### labelIds

Only return messages with labels that match all of the specified label IDs.

**Type:** array

```json
[ "string" ]
```

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### q

Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, "from:someuser@example.com rfc822msgid: is:unread". Parameter cannot be used when accessing the api using the gmail.metadata scope.

**Type:** string

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_smimes_for_alias

Lists S/MIME configs for the specified send-as alias.

<details><summary>Parameters</summary>

### sendAsEmail (required)

The email address that appears in the "From:" header for mail sent using this alias.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_threads

Lists the threads in the user's mailbox.

<details><summary>Parameters</summary>

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeSpamTrash

Include threads from SPAM and TRASH in the results.

**Type:** boolean

### labelIds

Only return threads with labels that match all of the specified label IDs.

**Type:** array

```json
[ "string" ]
```

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### q

Only return threads matching the specified query. Supports the same query format as the Gmail search box. For example, "from:someuser@example.com rfc822msgid: is:unread". Parameter cannot be used when accessing the api using the gmail.metadata scope.

**Type:** string

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## modify_labels_for_messages

Modifies the labels on the specified messages.

<details><summary>Parameters</summary>

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### $body

**Type:** object

```json
{
  "addLabelIds" : [ "string" ],
  "removeLabelIds" : [ "string" ],
  "ids" : [ "string" ]
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## modify_labels_for_thread

Modifies the labels applied to the thread. This applies to all messages in the thread.

<details><summary>Parameters</summary>

### id (required)

The ID of the thread to modify.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### $body

**Type:** object

```json
{
  "addLabelIds" : [ "string" ],
  "removeLabelIds" : [ "string" ]
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## modify_message_labels

Modifies the labels on the specified message.

<details><summary>Parameters</summary>

### id (required)

The ID of the message to modify.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### $body

**Type:** object

```json
{
  "addLabelIds" : [ "string" ],
  "removeLabelIds" : [ "string" ]
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## patch_alias

Updates a send-as alias. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias.

Addresses other than the primary address for the account can only be updated by service account clients that have been delegated domain-wide authority. This method supports patch semantics.

<details><summary>Parameters</summary>

### sendAsEmail (required)

The send-as alias to be updated.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### $body

Settings associated with a send-as alias, which can be either the primary login address associated with the account or a custom "from" address. Send-as aliases correspond to the "Send Mail As" feature in the web interface.

**Type:** object

```json
{
  "isDefault" : "Whether this address is selected as the default \"From:\" address in situations such as composing a new message or sending a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients may write to this field is true. Changing this from false to true for an address will result in this field becoming false for the other previous default address.",
  "signature" : "An optional HTML signature that is included in messages composed with this alias in the Gmail web UI.",
  "verificationStatus" : "Indicates whether this address has been verified for use as a send-as alias. Read-only. This setting only applies to custom \"from\" aliases.",
  "displayName" : "A name that appears in the \"From:\" header for mail sent using this alias. For custom \"from\" addresses, when this is empty, Gmail will populate the \"From:\" header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.",
  "isPrimary" : "Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases. This field is read-only.",
  "sendAsEmail" : "The email address that appears in the \"From:\" header for mail sent using this alias. This is read-only for all operations except create.",
  "smtpMsa" : {
    "password" : "The password that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses.",
    "port" : "The port of the SMTP service. Required.",
    "host" : "The hostname of the SMTP service. Required.",
    "securityMode" : "The protocol that will be used to secure communication with the SMTP service. Required.",
    "username" : "The username that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses."
  },
  "replyToAddress" : "An optional email address that is included in a \"Reply-To:\" header for mail sent using this alias. If this is empty, Gmail will not generate a \"Reply-To:\" header.",
  "treatAsAlias" : "Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom \"from\" aliases."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## patch_label

Updates the specified label. This method supports patch semantics.

<details><summary>Parameters</summary>

### id (required)

The ID of the label to update.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### $body

Labels are used to categorize messages and threads within the user's mailbox.

**Type:** object

```json
{
  "messageListVisibility" : "The visibility of the label in the message list in the Gmail web interface.",
  "messagesUnread" : "The number of unread messages with the label.",
  "threadsUnread" : "The number of unread threads with the label.",
  "color" : {
    "backgroundColor" : "The background color represented as hex string #RRGGBB (ex #000000). This field is required in order to set the color of a label. Only the following predefined set of color values are allowed:\n#000000, #434343, #666666, #999999, #cccccc, #efefef, #f3f3f3, #ffffff, #fb4c2f, #ffad47, #fad165, #16a766, #43d692, #4a86e8, #a479e2, #f691b3, #f6c5be, #ffe6c7, #fef1d1, #b9e4d0, #c6f3de, #c9daf8, #e4d7f5, #fcdee8, #efa093, #ffd6a2, #fce8b3, #89d3b2, #a0eac9, #a4c2f4, #d0bcf1, #fbc8d9, #e66550, #ffbc6b, #fcda83, #44b984, #68dfa9, #6d9eeb, #b694e8, #f7a7c0, #cc3a21, #eaa041, #f2c960, #149e60, #3dc789, #3c78d8, #8e63ce, #e07798, #ac2b16, #cf8933, #d5ae49, #0b804b, #2a9c68, #285bac, #653e9b, #b65775, #822111, #a46a21, #aa8831, #076239, #1a764d, #1c4587, #41236d, #83334c",
    "textColor" : "The text color of the label, represented as hex string. This field is required in order to set the color of a label. Only the following predefined set of color values are allowed:\n#000000, #434343, #666666, #999999, #cccccc, #efefef, #f3f3f3, #ffffff, #fb4c2f, #ffad47, #fad165, #16a766, #43d692, #4a86e8, #a479e2, #f691b3, #f6c5be, #ffe6c7, #fef1d1, #b9e4d0, #c6f3de, #c9daf8, #e4d7f5, #fcdee8, #efa093, #ffd6a2, #fce8b3, #89d3b2, #a0eac9, #a4c2f4, #d0bcf1, #fbc8d9, #e66550, #ffbc6b, #fcda83, #44b984, #68dfa9, #6d9eeb, #b694e8, #f7a7c0, #cc3a21, #eaa041, #f2c960, #149e60, #3dc789, #3c78d8, #8e63ce, #e07798, #ac2b16, #cf8933, #d5ae49, #0b804b, #2a9c68, #285bac, #653e9b, #b65775, #822111, #a46a21, #aa8831, #076239, #1a764d, #1c4587, #41236d, #83334c"
  },
  "threadsTotal" : "The total number of threads with the label.",
  "name" : "The display name of the label.",
  "id" : "The immutable ID of the label.",
  "labelListVisibility" : "The visibility of the label in the label list in the Gmail web interface.",
  "type" : "The owner type for the label. User labels are created by the user and can be modified and deleted by the user and can be applied to any message or thread. System labels are internally created and cannot be added, modified, or deleted. System labels may be able to be applied to or removed from messages and threads under some circumstances but this is not guaranteed. For example, users can apply and remove the INBOX and UNREAD labels from messages and threads, but cannot apply or remove the DRAFTS or SENT labels from messages or threads.",
  "messagesTotal" : "The total number of messages with the label."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## send_draft

Sends the specified, existing draft to the recipients in the To, Cc, and Bcc headers.

<details><summary>Parameters</summary>

### draftId

**Type:** STRING

### userId

**Type:** STRING

</details>

## send_message

Sends the specified message to the recipients in the To, Cc, and Bcc headers.

<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### cc

**Type:** STRING

### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

### from

**Type:** STRING

### message

**Type:** STRING

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## send_message_multipart

Sends the specified multipart message to the recipients in the To, Cc, and Bcc headers.

<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### bodyParts

A map of MIME Content-Types to content. Best practices suggest ordering from simplest to fanciest format.

**Type:** OBJECT

### cc

**Type:** STRING

### contentType

A multipart Content-Type. Default is multipart/alternative.

**Type:** STRING

### from

**Type:** STRING

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## set_default_smime_for_alias

Sets the default S/MIME config for the specified send-as alias.

<details><summary>Parameters</summary>

### id (required)

The immutable ID for the SmimeInfo.

**Type:** string

### sendAsEmail (required)

The email address that appears in the "From:" header for mail sent using this alias.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## set_push_notification

Set up or update a push notification watch on the given user mailbox.

<details><summary>Parameters</summary>

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### $body

Set up or update a new push notification watch on this user's mailbox.

**Type:** object

```json
{
  "labelIds" : [ "string" ],
  "labelFilterAction" : "Filtering behavior of labelIds list specified.",
  "topicName" : "A fully qualified Google Cloud Pub/Sub API topic name to publish the events to. This topic name **must** already exist in Cloud Pub/Sub and you **must** have already granted gmail \"publish\" permission on it. For example, \"projects/my-project-identifier/topics/my-topic-name\" (using the Cloud Pub/Sub \"v1\" topic naming format).\n\nNote that the \"my-project-identifier\" portion must exactly match your Google developer project id (the one executing this watch request)."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## stop_push_notifications

Stop receiving push notifications for the given user mailbox.

<details><summary>Parameters</summary>

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## trash_message

Moves the specified message to the trash.

<details><summary>Parameters</summary>

### id (required)

The ID of the message to Trash.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## trash_thread

Moves the specified thread to the trash.

<details><summary>Parameters</summary>

### id (required)

The ID of the thread to Trash.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## untrash_message

Removes the specified message from the trash.

<details><summary>Parameters</summary>

### id (required)

The ID of the message to remove from Trash.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## untrash_thread

Removes the specified thread from the trash.

<details><summary>Parameters</summary>

### id (required)

The ID of the thread to remove from Trash.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_alias

Updates a send-as alias. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias.

Addresses other than the primary address for the account can only be updated by service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### sendAsEmail (required)

The send-as alias to be updated.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### $body

Settings associated with a send-as alias, which can be either the primary login address associated with the account or a custom "from" address. Send-as aliases correspond to the "Send Mail As" feature in the web interface.

**Type:** object

```json
{
  "isDefault" : "Whether this address is selected as the default \"From:\" address in situations such as composing a new message or sending a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients may write to this field is true. Changing this from false to true for an address will result in this field becoming false for the other previous default address.",
  "signature" : "An optional HTML signature that is included in messages composed with this alias in the Gmail web UI.",
  "verificationStatus" : "Indicates whether this address has been verified for use as a send-as alias. Read-only. This setting only applies to custom \"from\" aliases.",
  "displayName" : "A name that appears in the \"From:\" header for mail sent using this alias. For custom \"from\" addresses, when this is empty, Gmail will populate the \"From:\" header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail.",
  "isPrimary" : "Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases. This field is read-only.",
  "sendAsEmail" : "The email address that appears in the \"From:\" header for mail sent using this alias. This is read-only for all operations except create.",
  "smtpMsa" : {
    "password" : "The password that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses.",
    "port" : "The port of the SMTP service. Required.",
    "host" : "The hostname of the SMTP service. Required.",
    "securityMode" : "The protocol that will be used to secure communication with the SMTP service. Required.",
    "username" : "The username that will be used for authentication with the SMTP service. This is a write-only field that can be specified in requests to create or update SendAs settings; it is never populated in responses."
  },
  "replyToAddress" : "An optional email address that is included in a \"Reply-To:\" header for mail sent using this alias. If this is empty, Gmail will not generate a \"Reply-To:\" header.",
  "treatAsAlias" : "Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom \"from\" aliases."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_auto_forwarding

Updates the auto-forwarding setting for the specified account. A verified forwarding address must be specified when auto-forwarding is enabled.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### $body

Auto-forwarding settings for an account.

**Type:** object

```json
{
  "disposition" : "The state that a message should be left in after it has been forwarded.",
  "emailAddress" : "Email address to which all incoming messages are forwarded. This email address must be a verified member of the forwarding addresses.",
  "enabled" : "Whether all incoming mail is automatically forwarded to another address."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_draft

Replaces a draft's content.

<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### cc

**Type:** STRING

### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

### from

**Type:** STRING

### message

**Type:** STRING

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## update_draft_multipart

Replaces a draft's content with a multipart message.

<details><summary>Parameters</summary>

### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

### bcc

**Type:** STRING

### bodyParts

A map of MIME Content-Types to content. Best practices suggest ordering from simplest to fanciest format.

**Type:** OBJECT

### cc

**Type:** STRING

### contentType

A multipart Content-Type. Default is multipart/alternative.

**Type:** STRING

### from

**Type:** STRING

### subject

**Type:** STRING

### threadId

**Type:** STRING

### to

**Type:** STRING

### userId

**Type:** STRING

</details>

## update_imap_settings

Updates IMAP settings.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### $body

IMAP settings for an account.

**Type:** object

```json
{
  "maxFolderSize" : "An optional limit on the number of messages that an IMAP folder may contain. Legal values are 0, 1000, 2000, 5000 or 10000. A value of zero is interpreted to mean that there is no limit.",
  "expungeBehavior" : "The action that will be executed on a message when it is marked as deleted and expunged from the last visible IMAP folder.",
  "autoExpunge" : "If this value is true, Gmail will immediately expunge a message when it is marked as deleted in IMAP. Otherwise, Gmail will wait for an update from the client before expunging messages marked as deleted.",
  "enabled" : "Whether IMAP is enabled for the account."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_label

Updates the specified label.

<details><summary>Parameters</summary>

### id (required)

The ID of the label to update.

**Type:** string

### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

### $body

Labels are used to categorize messages and threads within the user's mailbox.

**Type:** object

```json
{
  "messageListVisibility" : "The visibility of the label in the message list in the Gmail web interface.",
  "messagesUnread" : "The number of unread messages with the label.",
  "threadsUnread" : "The number of unread threads with the label.",
  "color" : {
    "backgroundColor" : "The background color represented as hex string #RRGGBB (ex #000000). This field is required in order to set the color of a label. Only the following predefined set of color values are allowed:\n#000000, #434343, #666666, #999999, #cccccc, #efefef, #f3f3f3, #ffffff, #fb4c2f, #ffad47, #fad165, #16a766, #43d692, #4a86e8, #a479e2, #f691b3, #f6c5be, #ffe6c7, #fef1d1, #b9e4d0, #c6f3de, #c9daf8, #e4d7f5, #fcdee8, #efa093, #ffd6a2, #fce8b3, #89d3b2, #a0eac9, #a4c2f4, #d0bcf1, #fbc8d9, #e66550, #ffbc6b, #fcda83, #44b984, #68dfa9, #6d9eeb, #b694e8, #f7a7c0, #cc3a21, #eaa041, #f2c960, #149e60, #3dc789, #3c78d8, #8e63ce, #e07798, #ac2b16, #cf8933, #d5ae49, #0b804b, #2a9c68, #285bac, #653e9b, #b65775, #822111, #a46a21, #aa8831, #076239, #1a764d, #1c4587, #41236d, #83334c",
    "textColor" : "The text color of the label, represented as hex string. This field is required in order to set the color of a label. Only the following predefined set of color values are allowed:\n#000000, #434343, #666666, #999999, #cccccc, #efefef, #f3f3f3, #ffffff, #fb4c2f, #ffad47, #fad165, #16a766, #43d692, #4a86e8, #a479e2, #f691b3, #f6c5be, #ffe6c7, #fef1d1, #b9e4d0, #c6f3de, #c9daf8, #e4d7f5, #fcdee8, #efa093, #ffd6a2, #fce8b3, #89d3b2, #a0eac9, #a4c2f4, #d0bcf1, #fbc8d9, #e66550, #ffbc6b, #fcda83, #44b984, #68dfa9, #6d9eeb, #b694e8, #f7a7c0, #cc3a21, #eaa041, #f2c960, #149e60, #3dc789, #3c78d8, #8e63ce, #e07798, #ac2b16, #cf8933, #d5ae49, #0b804b, #2a9c68, #285bac, #653e9b, #b65775, #822111, #a46a21, #aa8831, #076239, #1a764d, #1c4587, #41236d, #83334c"
  },
  "threadsTotal" : "The total number of threads with the label.",
  "name" : "The display name of the label.",
  "id" : "The immutable ID of the label.",
  "labelListVisibility" : "The visibility of the label in the label list in the Gmail web interface.",
  "type" : "The owner type for the label. User labels are created by the user and can be modified and deleted by the user and can be applied to any message or thread. System labels are internally created and cannot be added, modified, or deleted. System labels may be able to be applied to or removed from messages and threads under some circumstances but this is not guaranteed. For example, users can apply and remove the INBOX and UNREAD labels from messages and threads, but cannot apply or remove the DRAFTS or SENT labels from messages or threads.",
  "messagesTotal" : "The total number of messages with the label."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_pop_settings

Updates POP settings.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### $body

POP settings for an account.

**Type:** object

```json
{
  "disposition" : "The action that will be executed on a message after it has been fetched via POP.",
  "accessWindow" : "The range of messages which are accessible via POP."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_vacation_settings

Updates vacation responder settings.

<details><summary>Parameters</summary>

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### $body

Vacation auto-reply settings for an account. These settings correspond to the "Vacation responder" feature in the web interface.

**Type:** object

```json
{
  "responseBodyPlainText" : "Response body in plain text format.",
  "responseSubject" : "Optional text to prepend to the subject line in vacation responses. In order to enable auto-replies, either the response subject or the response body must be nonempty.",
  "enableAutoReply" : "Flag that controls whether Gmail automatically replies to messages.",
  "responseBodyHtml" : "Response body in HTML format. Gmail will sanitize the HTML before storing it.",
  "restrictToContacts" : "Flag that determines whether responses are sent to recipients who are not in the user's list of contacts.",
  "startTime" : "An optional start time for sending auto-replies (epoch ms). When this is specified, Gmail will automatically reply only to messages that it receives after the start time. If both startTime and endTime are specified, startTime must precede endTime.",
  "endTime" : "An optional end time for sending auto-replies (epoch ms). When this is specified, Gmail will automatically reply only to messages that it receives before the end time. If both startTime and endTime are specified, startTime must precede endTime.",
  "restrictToDomain" : "Flag that determines whether responses are sent to recipients who are outside of the user's domain. This feature is only available for G Suite users."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## verify_alias

Sends a verification email to the specified send-as alias address. The verification status must be pending.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

### sendAsEmail (required)

The send-as alias to be verified.

**Type:** string

### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

