---
id: google-mail-documentation
title: Google Mail (version v4.*.*)
sidebar_label: Google Mail
layout: docs.mustache
---

## construct_message



<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### bodyParts

A map of MIME Content-Types to content.

**Type:** OBJECT

#### cc

**Type:** STRING

#### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

#### deleted

**Type:** BOOLEAN

#### draftId

**Type:** STRING

#### from

**Type:** STRING

#### internalDateSource

**Type:** STRING

#### message

**Type:** STRING

#### neverMarkSpam

**Type:** BOOLEAN

#### processForCalendar

**Type:** BOOLEAN

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## create_alias

Creates a custom "from" send-as alias. If an SMTP MSA is specified, Gmail will attempt to connect to the SMTP service to validate the configuration before creating the alias. If ownership verification is required for the alias, a message will be sent to the email address and the resource's verification status will be set to pending; otherwise, the resource will be created with verification status set to accepted. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### $body

Settings associated with a send-as alias, which can be either the primary login address associated with the account or a custom "from" address. Send-as aliases correspond to the "Send Mail As" feature in the web interface.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

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

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### $body

Settings for a delegate. Delegates can read, send, and delete messages, as well as view and add contacts, for the delegator's account. See "Set up mail delegation" for more information about delegates.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_draft

Creates a new draft with the DRAFT label.

<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### cc

**Type:** STRING

#### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

#### from

**Type:** STRING

#### message

**Type:** STRING

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## create_draft_multipart

Creates a new multipart draft with the DRAFT label.

<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### bodyParts

A map of MIME Content-Types to content. Best practices suggest ordering from simplest to fanciest format.

**Type:** OBJECT

#### cc

**Type:** STRING

#### contentType

A multipart Content-Type. Default is multipart/alternative.

**Type:** STRING

#### from

**Type:** STRING

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## create_filter

Creates a filter.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### $body

Resource definition for Gmail filters. Filters apply to specific messages instead of an entire email thread.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_forwarding_address

Creates a forwarding address. If ownership verification is required, a message will be sent to the recipient and the resource's verification status will be set to pending; otherwise, the resource will be created with verification status set to accepted.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### $body

Settings for a forwarding address.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_label

Creates a new label.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

Labels are used to categorize messages and threads within the user's mailbox.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_alias

Deletes the specified send-as alias. Revokes any verification that may have been required for using it.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

#### sendAsEmail (required)

The send-as alias to be deleted.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_delegate

Removes the specified delegate (which can be of any verification status), and revokes any verification that may have been required for using it.

Note that a delegate user must be referred to by their primary email address, and not an email alias.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

#### delegateEmail (required)

The email address of the user to be removed as a delegate.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_draft

Immediately and permanently deletes the specified draft. Does not simply trash it.

<details><summary>Parameters</summary>

#### id (required)

The ID of the draft to delete.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_filter

Deletes a filter.

<details><summary>Parameters</summary>

#### id (required)

The ID of the filter to be deleted.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_forwarding_address

Deletes the specified forwarding address and revokes any verification that may have been required.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

#### forwardingEmail (required)

The forwarding address to be deleted.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_label

Immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to.

<details><summary>Parameters</summary>

#### id (required)

The ID of the label to delete.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_message

Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer messages.trash instead.

<details><summary>Parameters</summary>

#### id (required)

The ID of the message to delete.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_messages

Deletes many messages by message ID. Provides no guarantees that messages were not already deleted or even existed at all.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_smime_for_alias

Deletes the specified S/MIME config for the specified send-as alias.

<details><summary>Parameters</summary>

#### id (required)

The immutable ID for the SmimeInfo.

**Type:** string

#### sendAsEmail (required)

The email address that appears in the "From:" header for mail sent using this alias.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_thread

Immediately and permanently deletes the specified thread. This operation cannot be undone. Prefer threads.trash instead.

<details><summary>Parameters</summary>

#### id (required)

ID of the Thread to delete.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_alias

Gets the specified send-as alias. Fails with an HTTP 404 error if the specified address is not a member of the collection.

<details><summary>Parameters</summary>

#### sendAsEmail (required)

The send-as alias to be retrieved.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_attachment

Gets the specified message attachment.

<details><summary>Parameters</summary>

#### id (required)

The ID of the attachment.

**Type:** string

#### messageId (required)

The ID of the message containing the attachment.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_auto_forwarding

Gets the auto-forwarding setting for the specified account.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_delegate

Gets the specified delegate.

Note that a delegate user must be referred to by their primary email address, and not an email alias.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

#### delegateEmail (required)

The email address of the user whose delegate relationship is to be retrieved.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_draft

Gets the specified draft.

<details><summary>Parameters</summary>

#### id (required)

The ID of the draft to retrieve.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### format

The format to return the draft in.

**Type:** string

**Potential values:** full, metadata, minimal, raw

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_filter

Gets a filter.

<details><summary>Parameters</summary>

#### id (required)

The ID of the filter to be fetched.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_forwarding_address

Gets the specified forwarding address.

<details><summary>Parameters</summary>

#### forwardingEmail (required)

The forwarding address to be retrieved.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_imap_settings

Gets IMAP settings.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_label

Gets the specified label.

<details><summary>Parameters</summary>

#### id (required)

The ID of the label to retrieve.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_message

Gets the specified message.

<details><summary>Parameters</summary>

#### id (required)

The ID of the message to retrieve.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### format

The format to return the message in.

**Type:** string

**Potential values:** full, metadata, minimal, raw

#### metadataHeaders

When given and format is METADATA, only include headers specified.

**Type:** array

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_pop_settings

Gets POP settings.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_profile

Gets the current user's Gmail profile.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_smime_for_alias

Gets the specified S/MIME config for the specified send-as alias.

<details><summary>Parameters</summary>

#### id (required)

The immutable ID for the SmimeInfo.

**Type:** string

#### sendAsEmail (required)

The email address that appears in the "From:" header for mail sent using this alias.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_thread

Gets the specified thread.

<details><summary>Parameters</summary>

#### id (required)

The ID of the thread to retrieve.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### format

The format to return the messages in.

**Type:** string

**Potential values:** full, metadata, minimal

#### metadataHeaders

When given and format is METADATA, only include headers specified.

**Type:** array

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_vacation_settings

Gets vacation responder settings.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## import_message

Imports a message into only this user''s mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. Does not send a message.

<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### cc

**Type:** STRING

#### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

#### deleted

**Type:** BOOLEAN

#### from

**Type:** STRING

#### internalDateSource

**Type:** STRING

#### message

**Type:** STRING

#### neverMarkSpam

**Type:** BOOLEAN

#### processForCalendar

**Type:** BOOLEAN

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## import_message_multipart

Imports a multipart message into only this user''s mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. Does not send a message.

<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### bodyParts

A map of MIME Content-Types to content. Best practices suggest ordering from simplest to fanciest format.

**Type:** OBJECT

#### cc

**Type:** STRING

#### contentType

A multipart Content-Type. Default is multipart/alternative.

**Type:** STRING

#### deleted

**Type:** BOOLEAN

#### from

**Type:** STRING

#### internalDateSource

**Type:** STRING

#### neverMarkSpam

**Type:** BOOLEAN

#### processForCalendar

**Type:** BOOLEAN

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## insert_message

Directly inserts a message into only this user''s mailbox similar to IMAP APPEND, bypassing most scanning and classification. Does not send a message.

<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### cc

**Type:** STRING

#### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

#### deleted

**Type:** BOOLEAN

#### from

**Type:** STRING

#### internalDateSource

**Type:** STRING

#### message

**Type:** STRING

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## insert_message_multipart

Directly inserts a multipart message into only this user''s mailbox similar to IMAP APPEND, bypassing most scanning and classification. Does not send a message.

<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### bodyParts

A map of MIME Content-Types to content. Best practices suggest ordering from simplest to fanciest format.

**Type:** OBJECT

#### cc

**Type:** STRING

#### contentType

A multipart Content-Type. Default is multipart/alternative.

**Type:** STRING

#### deleted

**Type:** BOOLEAN

#### from

**Type:** STRING

#### internalDateSource

**Type:** STRING

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## insert_smime_for_alias

Insert (upload) the given S/MIME config for the specified send-as alias. Note that pkcs12 format is required for the key.

<details><summary>Parameters</summary>

#### sendAsEmail (required)

The email address that appears in the "From:" header for mail sent using this alias.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

An S/MIME email config.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_aliases

Lists the send-as aliases for the specified account. The result includes the primary send-as address associated with the account as well as any custom "from" aliases.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_delegates

Lists the delegates for the specified account.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_drafts

Lists the drafts in the user's mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### includeSpamTrash

Include drafts from SPAM and TRASH in the results.

**Type:** boolean

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### q

Only return draft messages matching the specified query. Supports the same query format as the Gmail search box. For example, "from:someuser@example.com rfc822msgid: is:unread".

**Type:** string

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_filters

Lists the message filters of a Gmail user.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_forwarding_addresses

Lists the forwarding addresses for the specified account.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_history_of_mailbox

Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing historyId).

<details><summary>Parameters</summary>

#### startHistoryId (required)

Required. Returns history records after the specified startHistoryId. The supplied startHistoryId should be obtained from the historyId of a message, thread, or previous list response. History IDs increase chronologically but are not contiguous with random gaps in between valid IDs. Supplying an invalid or out of date startHistoryId typically returns an HTTP 404 error code. A historyId is typically valid for at least a week, but in some rare circumstances may be valid for only a few hours. If you receive an HTTP 404 error response, your application should perform a full sync. If you receive no nextPageToken in the response, there are no updates to retrieve and you can store the returned historyId for a future request.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### historyTypes

History types to be returned by the function

**Type:** array

#### labelId

Only return messages with a label matching the ID.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_labels

Lists all labels in the user's mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_messages

Lists the messages in the user's mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### includeSpamTrash

Include messages from SPAM and TRASH in the results.

**Type:** boolean

#### labelIds

Only return messages with labels that match all of the specified label IDs.

**Type:** array

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### q

Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, "from:someuser@example.com rfc822msgid: is:unread". Parameter cannot be used when accessing the api using the gmail.metadata scope.

**Type:** string

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_smimes_for_alias

Lists S/MIME configs for the specified send-as alias.

<details><summary>Parameters</summary>

#### sendAsEmail (required)

The email address that appears in the "From:" header for mail sent using this alias.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_threads

Lists the threads in the user's mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### includeSpamTrash

Include threads from SPAM and TRASH in the results.

**Type:** boolean

#### labelIds

Only return threads with labels that match all of the specified label IDs.

**Type:** array

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### q

Only return threads matching the specified query. Supports the same query format as the Gmail search box. For example, "from:someuser@example.com rfc822msgid: is:unread". Parameter cannot be used when accessing the api using the gmail.metadata scope.

**Type:** string

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## modify_labels_for_messages

Modifies the labels on the specified messages.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## modify_labels_for_thread

Modifies the labels applied to the thread. This applies to all messages in the thread.

<details><summary>Parameters</summary>

#### id (required)

The ID of the thread to modify.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## modify_message_labels

Modifies the labels on the specified message.

<details><summary>Parameters</summary>

#### id (required)

The ID of the message to modify.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## patch_alias

Updates a send-as alias. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias.

Addresses other than the primary address for the account can only be updated by service account clients that have been delegated domain-wide authority. This method supports patch semantics.

<details><summary>Parameters</summary>

#### sendAsEmail (required)

The send-as alias to be updated.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### $body

Settings associated with a send-as alias, which can be either the primary login address associated with the account or a custom "from" address. Send-as aliases correspond to the "Send Mail As" feature in the web interface.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## patch_label

Updates the specified label. This method supports patch semantics.

<details><summary>Parameters</summary>

#### id (required)

The ID of the label to update.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

Labels are used to categorize messages and threads within the user's mailbox.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## send_draft

Sends the specified, existing draft to the recipients in the To, Cc, and Bcc headers.

<details><summary>Parameters</summary>

#### draftId

**Type:** STRING

#### userId

**Type:** STRING

</details>

## send_message

Sends the specified message to the recipients in the To, Cc, and Bcc headers.

<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### cc

**Type:** STRING

#### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

#### from

**Type:** STRING

#### message

**Type:** STRING

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## send_message_multipart

Sends the specified multipart message to the recipients in the To, Cc, and Bcc headers.

<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### bodyParts

A map of MIME Content-Types to content. Best practices suggest ordering from simplest to fanciest format.

**Type:** OBJECT

#### cc

**Type:** STRING

#### contentType

A multipart Content-Type. Default is multipart/alternative.

**Type:** STRING

#### from

**Type:** STRING

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## set_default_smime_for_alias

Sets the default S/MIME config for the specified send-as alias.

<details><summary>Parameters</summary>

#### id (required)

The immutable ID for the SmimeInfo.

**Type:** string

#### sendAsEmail (required)

The email address that appears in the "From:" header for mail sent using this alias.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## set_push_notification

Set up or update a push notification watch on the given user mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

Set up or update a new push notification watch on this user's mailbox.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## stop_push_notifications

Stop receiving push notifications for the given user mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## trash_message

Moves the specified message to the trash.

<details><summary>Parameters</summary>

#### id (required)

The ID of the message to Trash.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## trash_thread

Moves the specified thread to the trash.

<details><summary>Parameters</summary>

#### id (required)

The ID of the thread to Trash.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## untrash_message

Removes the specified message from the trash.

<details><summary>Parameters</summary>

#### id (required)

The ID of the message to remove from Trash.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## untrash_thread

Removes the specified thread from the trash.

<details><summary>Parameters</summary>

#### id (required)

The ID of the thread to remove from Trash.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_alias

Updates a send-as alias. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias.

Addresses other than the primary address for the account can only be updated by service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

#### sendAsEmail (required)

The send-as alias to be updated.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### $body

Settings associated with a send-as alias, which can be either the primary login address associated with the account or a custom "from" address. Send-as aliases correspond to the "Send Mail As" feature in the web interface.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_auto_forwarding

Updates the auto-forwarding setting for the specified account. A verified forwarding address must be specified when auto-forwarding is enabled.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### $body

Auto-forwarding settings for an account.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_draft

Replaces a draft's content.

<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### cc

**Type:** STRING

#### contentType

Can be either text/plain or text/html. Default is text/plain.

**Type:** STRING

#### from

**Type:** STRING

#### message

**Type:** STRING

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## update_draft_multipart

Replaces a draft's content with a multipart message.

<details><summary>Parameters</summary>

#### additionalHeaders

Additional RFC822 headers, specified as key:value pairs.

**Type:** OBJECT

#### bcc

**Type:** STRING

#### bodyParts

A map of MIME Content-Types to content. Best practices suggest ordering from simplest to fanciest format.

**Type:** OBJECT

#### cc

**Type:** STRING

#### contentType

A multipart Content-Type. Default is multipart/alternative.

**Type:** STRING

#### from

**Type:** STRING

#### subject

**Type:** STRING

#### threadId

**Type:** STRING

#### to

**Type:** STRING

#### userId

**Type:** STRING

</details>

## update_imap_settings

Updates IMAP settings.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### $body

IMAP settings for an account.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_label

Updates the specified label.

<details><summary>Parameters</summary>

#### id (required)

The ID of the label to update.

**Type:** string

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

Labels are used to categorize messages and threads within the user's mailbox.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_pop_settings

Updates POP settings.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### $body

POP settings for an account.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_vacation_settings

Updates vacation responder settings.

<details><summary>Parameters</summary>

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### $body

Vacation auto-reply settings for an account. These settings correspond to the "Vacation responder" feature in the web interface.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## verify_alias

Sends a verification email to the specified send-as alias address. The verification status must be pending.

This method is only available to service account clients that have been delegated domain-wide authority.

<details><summary>Parameters</summary>

#### sendAsEmail (required)

The send-as alias to be verified.

**Type:** string

#### userId (required)

User's email address. The special value "me" can be used to indicate the authenticated user.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

