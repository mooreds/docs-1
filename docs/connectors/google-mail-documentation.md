---
id: google-mail-documentation
title: Google Mail (version v1.*.*)
sidebar_label: Google Mail
---

## create_draft

Creates a new draft with the DRAFT label.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## create_label

Creates a new label.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## delete_draft

Immediately and permanently deletes the specified draft. Does not simply trash it.

<details><summary>Parameters</summary>

#### id (required)

The ID of the draft to delete.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## delete_label

Immediately and permanently deletes the specified label and removes it from any messages and threads that it is applied to.

<details><summary>Parameters</summary>

#### id (required)

The ID of the label to delete.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## delete_message

Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer messages.trash instead.

<details><summary>Parameters</summary>

#### id (required)

The ID of the message to delete.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## delete_thread

Immediately and permanently deletes the specified thread. This operation cannot be undone. Prefer threads.trash instead.

<details><summary>Parameters</summary>

#### id (required)

ID of the Thread to delete.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

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

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## get_draft

Gets the specified draft.

<details><summary>Parameters</summary>

#### id (required)

The ID of the draft to retrieve.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### format

The format to return the draft in.

**Type:** string

</details>

## get_label

Gets the specified label.

<details><summary>Parameters</summary>

#### id (required)

The ID of the label to retrieve.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## get_labels

Lists all labels in the users mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## get_message

Gets the specified message.

<details><summary>Parameters</summary>

#### id (required)

The ID of the message to retrieve.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### format

The format to return the message in.

**Type:** string

#### metadataHeaders

When given and format is METADATA, only include headers specified.

**Type:** string

</details>

## get_messages

Lists the messages in the users mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### includeSpamTrash

Include messages from SPAM and TRASH in the results.

**Type:** string

#### labelIds

Only return messages with labels that match all of the specified label IDs.

**Type:** array

#### q

Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, from:someuser@example.com rfc822msgid: is:unread.

**Type:** string

</details>

## get_profile

Gets the current users Gmail profile.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## get_thread

Gets the specified thread.

<details><summary>Parameters</summary>

#### id (required)

The ID of the thread to retrieve.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### format

The format to return the messages in.

**Type:** string

**Potential values:** full, metadata, minimal

#### metadataHeaders

When given and format is METADATA, only include headers specified.

**Type:** array

</details>

## import_message

Imports a message into only this users mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. Does not send a message.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### deleted

Mark the email as permanently deleted (not TRASH) and only visible in Google Apps Vault to a Vault administrator. Only used for Google Apps for Work accounts.

**Type:** string

#### internalDateSource

Source for Gmails internal date of the message.

**Type:** string

#### neverMarkSpam

Ignore the Gmail spam classifier decision and never mark this email as SPAM in the mailbox.

**Type:** string

#### processForCalendar

Process calendar invites in the email and add any extracted meetings to the Google Calendar for this user.

**Type:** string

</details>

## insert_message

Directly inserts a message into only this users mailbox similar to IMAP APPEND, bypassing most scanning and classification. Does not send a message.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### deleted

Mark the email as permanently deleted (not TRASH) and only visible in Google Apps Vault to a Vault administrator. Only used for Google Apps for Work accounts.

**Type:** string

#### internalDateSource

Source for Gmails internal date of the message.

**Type:** string

</details>

## list_drafts

Lists the drafts in the users mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## list_histories

Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing historyId).

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### labelId

Only return messages with a label matching the ID.

**Type:** string

#### startHistoryId

Required. Returns history records after the specified startHistoryId. The supplied startHistoryId should be obtained from the historyId of a message, thread, or previous list response. History IDs increase chronologically but are not contiguous with random gaps in between valid IDs. Supplying an invalid or out of date startHistoryId typically returns an HTTP 404 error code. A historyId is typically valid for at least a week, but in some circumstances may be valid for only a few hours. If you rec

**Type:** string

</details>

## list_threads

Lists the threads in the users mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### includeSpamTrash

Include threads from SPAM and TRASH in the results.

**Type:** boolean

#### labelIds

Only return threads with labels that match all of the specified label IDs.

**Type:** array

#### q

Only return threads matching the specified query. Supports the same query format as the Gmail search box. For example, from:someuser@example.com rfc822msgid: is:unread.

**Type:** string

</details>

## modify_message

Modifies the labels on the specified message.

<details><summary>Parameters</summary>

#### id (required)

The ID of the message to modify.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## modify_thread

Modifies the labels applied to the thread. This applies to all messages in the thread.

<details><summary>Parameters</summary>

#### id (required)

The ID of the thread to modify.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

Modifies the labels applied to the thread.

**Type:** object

</details>

## patch_label

Updates the specified label. This method supports patch semantics.

<details><summary>Parameters</summary>

#### id (required)

The ID of the label to update.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## send_draft

Sends the specified, existing draft to the recipients in the To, Cc, and Bcc headers.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## send_message

Sends the specified message to the recipients in the To, Cc, and Bcc headers.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

The entire email message in an RFC 2822 formatted and base64url encoded string. Returned in messages.get and drafts.get responses when the format=RAW parameter is supplied.

**Type:** object

</details>

## stop

Stop receiving push notifications for the given user mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The user's email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## trash_message

Moves the specified message to the trash.

<details><summary>Parameters</summary>

#### id (required)

The ID of the message to Trash.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## trash_thread

Moves the specified thread to the trash.

<details><summary>Parameters</summary>

#### id (required)

The ID of the thread to Trash.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## untrash_message

Removes the specified message from the trash.

<details><summary>Parameters</summary>

#### id (required)

The ID of the message to remove from Trash.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## untrash_thread

Removes the specified thread from the trash.

<details><summary>Parameters</summary>

#### id (required)

The ID of the thread to remove from Trash.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## update_draft

Replaces a drafts content.

<details><summary>Parameters</summary>

#### id (required)

The ID of the draft to update.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## update_label

Updates the specified label.

<details><summary>Parameters</summary>

#### id (required)

The ID of the label to update.

**Type:** string

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

</details>

## watch

Set up or update a push notification watch on the given user mailbox.

<details><summary>Parameters</summary>

#### userId (required)

The users email address. The special value me can be used to indicate the authenticated user.

**Type:** string

#### $body

Set up or update a new push notification watch on this user's mailbox.

**Type:** object

</details>

