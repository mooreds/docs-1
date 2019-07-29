---
id: slack-documentation
title: Slack (version v3.*.*)
sidebar_label: Slack
layout: docs.mustache
---

## add_files_comments

Add a comment to an existing file.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File to add a comment to.",
  "comment" : "Text of the comment to add."
}
```

</details>

## add_pins

Pins an item to a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File to pin.",
  "channel" : "Channel to pin the item in.",
  "file_comment" : "File comment to pin.",
  "timestamp" : "Timestamp of the message to pin."
}
```

</details>

## add_reactions

Adds a reaction to an item.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File to add reaction to.",
  "name" : "Reaction (emoji) name.",
  "channel" : "Channel where the message to add reaction to was posted.",
  "file_comment" : "File comment to add reaction to.",
  "timestamp" : "Timestamp of the message to add reaction to."
}
```

</details>

## add_reminders

Creates a reminder.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "text" : "The content of the reminder",
  "time" : "When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. \"in 15 minutes,\" or \"every Thursday\")",
  "user" : "The user who will receive the reminder. If no user is specified, the reminder will go to user who created it."
}
```

</details>

## add_stars

Adds a star to an item.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File to add star to.",
  "channel" : "Channel to add star to, or channel where the message to add star to was posted (used with `timestamp`).",
  "file_comment" : "File comment to add star to.",
  "timestamp" : "Timestamp of the message to add star to."
}
```

</details>

## archive_channels

Archives a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Channel to archive"
}
```

</details>

## archive_conversations

Archives a conversation.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "ID of conversation to archive"
}
```

</details>

## archive_groups

Archives a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Private channel to archive"
}
```

</details>

## check_api

Checks API calling code.

*This operation has no parameters*

## close_conversations

Closes a direct message or multi-person direct message.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Conversation to close."
}
```

</details>

## close_im

Close a direct message channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Direct message channel to close."
}
```

</details>

## close_mpim

Closes a multiparty direct message channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "MPIM to close."
}
```

</details>

## connect_rtm

Starts a Real Time Messaging session.

<details><summary>Parameters</summary>

### batch_presence_aware

Batch presence deliveries via subscription. Enabling changes the shape of `presence_change` events. See [batch presence](/docs/presence-and-status#batching).

**Type:** boolean

### presence_sub

Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions).

**Type:** boolean

</details>

## create_channels

Creates a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "Name of channel to create",
  "validate" : "Whether to return errors on invalid channel name instead of modifying it to meet the specified criteria."
}
```

</details>

## create_conversations

Initiates a public or private channel-based conversation

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "is_private" : "Create a private channel instead of a public one",
  "name" : "Name of the public or private channel to create"
}
```

</details>

## create_groups

Creates a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "Name of private channel to create",
  "validate" : "Whether to return errors on invalid channel name instead of modifying it to meet the specified criteria."
}
```

</details>

## create_usergroups

Create a User Group

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channels" : "A comma separated string of encoded channel IDs for which the User Group uses as a default.",
  "name" : "A name for the User Group. Must be unique among User Groups.",
  "description" : "A short description of the User Group.",
  "handle" : "A mention handle. Must be unique among channels, users and User Groups.",
  "include_count" : "Include the number of users in each User Group."
}
```

</details>

## delete_chat

Deletes a message.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "as_user" : "Pass true to delete the message as the authed user with `chat:write:user` scope. [Bot users](/bot-users) in this context are considered authed users. If unused or false, the message will be deleted with `chat:write:bot` scope.",
  "channel" : "Channel containing the message to be deleted.",
  "ts" : "Timestamp of the message to be deleted."
}
```

</details>

## delete_files

Deletes a file.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "ID of file to delete."
}
```

</details>

## delete_files_comments

Deletes an existing comment on a file.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File to delete a comment from.",
  "id" : "The comment to delete."
}
```

</details>

## delete_reminders

Deletes a reminder.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "reminder" : "The ID of the reminder"
}
```

</details>

## disable_usergroups

Disable an existing User Group

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "usergroup" : "The encoded ID of the User Group to disable.",
  "include_count" : "Include the number of users in the User Group."
}
```

</details>

## dnd_set_snooze

Turns on Do Not Disturb mode for the current user, or changes its duration.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "num_minutes" : "Number of minutes, from now, to snooze until."
}
```

</details>

## edit_files_comments

Edit an existing file comment.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File containing the comment to edit.",
  "comment" : "Text of the comment to edit.",
  "id" : "The comment to edit."
}
```

</details>

## enable_files_public_url

Enables a file for public/external sharing.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File to share"
}
```

</details>

## enable_usergroups

Enable a User Group

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "usergroup" : "The encoded ID of the User Group to enable.",
  "include_count" : "Include the number of users in the User Group."
}
```

</details>

## end_dnd_snooze

Ends the current user's snooze mode immediately.

*This operation has no parameters*

## end_user_dnd

Ends the current user's Do Not Disturb session immediately.

*This operation has no parameters*

## exchange_migration

For Enterprise Grid workspaces, map local user IDs to global user IDs

<details><summary>Parameters</summary>

### to_old

Specify `true` to convert `W` global user IDs to workspace-specific `U` IDs. Defaults to `false`.

**Type:** boolean

### users

A comma-separated list of user ids, up to 400 per request

**Type:** string

</details>

## files_upload

Uploads or creates a file.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "filetype" : "A [file type](/types/file#file_types) identifier.",
  "filename" : "Filename of file.",
  "file" : "File contents via `multipart/form-data`. If omitting this parameter, you must submit `content`. Currently Transposit does not support multipart/form-data.",
  "channels" : "Comma-separated list of channel names or IDs where the file will be shared.",
  "initial_comment" : "Initial comment to add to file.",
  "title" : "Title of file.",
  "content" : "File contents via a POST variable. If omitting this parameter, you must provide a `file`."
}
```

</details>

## get_apps_permissions_info

Returns list of permissions this app has on a team.

*This operation has no parameters*

## get_bots_info

Gets information about a bot user.

<details><summary>Parameters</summary>

### bot

Bot user to get info on

**Type:** string

</details>

## get_channels_history

Fetches history of messages and events from a channel.

<details><summary>Parameters</summary>

### channel (required)

Channel to fetch history for.

**Type:** string

### count

Number of messages to return, between 1 and 1000.

**Type:** integer

### inclusive

Include messages with latest or oldest timestamp in results.

**Type:** boolean

### latest

End of time range of messages to include in results.

**Type:** number

### oldest

Start of time range of messages to include in results.

**Type:** number

### unreads

Include `unread_count_display` in the output?

**Type:** boolean

</details>

## get_channels_info

Gets information about a channel.

<details><summary>Parameters</summary>

### channel

Channel to get info on

**Type:** string

### include_locale

Set this to `true` to receive the locale for this channel. Defaults to `false`

**Type:** boolean

</details>

## get_channels_list

Lists all channels in a Slack team.

<details><summary>Parameters</summary>

### exclude_archived

Exclude archived channels from the list

**Type:** boolean

### exclude_members

Exclude the `members` collection from each `channel`

**Type:** boolean

</details>

## get_channels_replies

Retrieve a thread of messages posted to a channel

<details><summary>Parameters</summary>

### channel

Channel to fetch thread from

**Type:** string

### thread_ts

Unique identifier of a thread's parent message

**Type:** string

</details>

## get_chat_permalink

Retrieve a permalink URL for a specific extant message

<details><summary>Parameters</summary>

### channel

The ID of the conversation or channel containing the message

**Type:** string

### message_ts

A message's `ts` value, uniquely identifying it within a channel

**Type:** number

</details>

## get_conversations_history

Fetches a conversation's history of messages and events.

<details><summary>Parameters</summary>

### channel

Conversation ID to fetch history for.

**Type:** string

### inclusive

Include messages with latest or oldest timestamp in results only when either timestamp is specified.

**Type:** boolean

### latest

End of time range of messages to include in results.

**Type:** number

### oldest

Start of time range of messages to include in results.

**Type:** number

</details>

## get_conversations_info

Retrieve information about a conversation.

<details><summary>Parameters</summary>

### channel

Conversation ID to learn more about

**Type:** string

### include_locale

Set this to `true` to receive the locale for this conversation. Defaults to `false`

**Type:** boolean

</details>

## get_conversations_members

Retrieve members of a conversation.

<details><summary>Parameters</summary>

### channel

ID of the conversation to retrieve members for

**Type:** string

</details>

## get_conversations_replies

Retrieve a thread of messages posted to a conversation

<details><summary>Parameters</summary>

### channel

Conversation ID to fetch thread from.

**Type:** string

### inclusive

Include messages with latest or oldest timestamp in results only when either timestamp is specified.

**Type:** boolean

### latest

End of time range of messages to include in results.

**Type:** number

### oldest

Start of time range of messages to include in results.

**Type:** number

### ts

Unique identifier of a thread's parent message.

**Type:** string

</details>

## get_dnd_info

Retrieves a user's current Do Not Disturb status.

<details><summary>Parameters</summary>

### user

User to fetch status for (defaults to current user)

**Type:** string

</details>

## get_dnd_team_info

Retrieves the Do Not Disturb status for users on a team.

<details><summary>Parameters</summary>

### users

Comma-separated list of users to fetch Do Not Disturb status for

**Type:** string

</details>

## get_files_info

Gets information about a team file.

<details><summary>Parameters</summary>

### count

**Type:** string

### file

Specify a file by providing its ID.

**Type:** string

</details>

## get_groups_history

Fetches history of messages and events from a private channel.

<details><summary>Parameters</summary>

### channel

Private channel to fetch history for.

**Type:** string

### count

Number of messages to return, between 1 and 1000.

**Type:** integer

### inclusive

Include messages with latest or oldest timestamp in results.

**Type:** boolean

### latest

End of time range of messages to include in results.

**Type:** number

### oldest

Start of time range of messages to include in results.

**Type:** number

### unreads

Include `unread_count_display` in the output?

**Type:** boolean

</details>

## get_groups_info

Gets information about a private channel.

<details><summary>Parameters</summary>

### channel

Private channel to get info on

**Type:** string

### include_locale

Set this to `true` to receive the locale for this group. Defaults to `false`

**Type:** boolean

</details>

## get_groups_replies

Retrieve a thread of messages posted to a private channel

<details><summary>Parameters</summary>

### channel

Private channel to fetch thread from

**Type:** string

### thread_ts

Unique identifier of a thread's parent message

**Type:** string

</details>

## get_im_history

Fetches history of messages and events from direct message channel.

<details><summary>Parameters</summary>

### channel

Direct message channel to fetch history for.

**Type:** string

### count

Number of messages to return, between 1 and 1000.

**Type:** integer

### inclusive

Include messages with latest or oldest timestamp in results.

**Type:** boolean

### latest

End of time range of messages to include in results.

**Type:** number

### oldest

Start of time range of messages to include in results.

**Type:** number

### unreads

Include `unread_count_display` in the output?

**Type:** boolean

</details>

## get_im_replies

Retrieve a thread of messages posted to a direct message conversation

<details><summary>Parameters</summary>

### channel

Direct message channel to fetch thread from

**Type:** string

### thread_ts

Unique identifier of a thread's parent message

**Type:** string

</details>

## get_mpim_replies

Retrieve a thread of messages posted to a direct message conversation from a multiparty direct message.

<details><summary>Parameters</summary>

### channel

Multiparty direct message channel to fetch thread from.

**Type:** string

### thread_ts

Unique identifier of a thread's parent message.

**Type:** string

</details>

## get_oauth_access

Exchanges a temporary OAuth verifier code for an access token.

<details><summary>Parameters</summary>

### client_id

Issued when you created your application.

**Type:** string

### client_secret

Issued when you created your application.

**Type:** string

### code

The `code` param returned via the OAuth callback.

**Type:** string

### redirect_uri

This must match the originally submitted URI (if one was sent).

**Type:** string

### single_channel

Request the user to add your app only to a single channel.

**Type:** boolean

</details>

## get_oauth_token

Exchanges a temporary OAuth verifier code for a workspace token.

<details><summary>Parameters</summary>

### client_id

Issued when you created your application.

**Type:** string

### client_secret

Issued when you created your application.

**Type:** string

### code

The `code` param returned via the OAuth callback.

**Type:** string

### redirect_uri

This must match the originally submitted URI (if one was sent).

**Type:** string

### single_channel

Request the user to add your app only to a single channel.

**Type:** boolean

</details>

## get_reactions

Gets reactions for an item.

<details><summary>Parameters</summary>

### channel

Channel where the message to get reactions for was posted.

**Type:** string

### file

File to get reactions for.

**Type:** string

### file_comment

File comment to get reactions for.

**Type:** string

### full

If true always return the complete reaction list.

**Type:** boolean

### timestamp

Timestamp of the message to get reactions for.

**Type:** number

</details>

## get_reminders_info

Gets information about a reminder.

<details><summary>Parameters</summary>

### reminder

The ID of the reminder

**Type:** string

</details>

## get_team_access_logs

Gets the access logs for the current team.

<details><summary>Parameters</summary>

### before

End of time range of logs to include in results (inclusive).

**Type:** integer

### count

**Type:** string

</details>

## get_team_billable_info

Gets billable users information for the current team.

<details><summary>Parameters</summary>

### user

A user to retrieve the billable information for. Defaults to all users.

**Type:** string

</details>

## get_team_info

Gets information about the current team.

*This operation has no parameters*

## get_team_integration_logs

Gets the integration logs for the current team.

<details><summary>Parameters</summary>

### app_id

Filter logs to this Slack app. Defaults to all logs.

**Type:** integer

### change_type

Filter logs with this change type. Defaults to all logs.

**Type:** string

### count

**Type:** string

### service_id

Filter logs to this service. Defaults to all logs.

**Type:** integer

### user

Filter logs generated by this user’s actions. Defaults to all logs.

**Type:** string

</details>

## get_team_profile

Retrieve a team's profile.

<details><summary>Parameters</summary>

### visibility

Filter by visibility.

**Type:** string

</details>

## get_users_identity

Get a user's identity.

*This operation has no parameters*

## get_users_info

Gets information about a user.

<details><summary>Parameters</summary>

### include_locale

Set this to `true` to receive the locale for this user. Defaults to `false`

**Type:** boolean

### user

User to get info on

**Type:** string

</details>

## get_users_presence

Gets user presence information.

<details><summary>Parameters</summary>

### user

User to get presence info on. Defaults to the authed user.

**Type:** string

</details>

## get_users_profile

Retrieves a user's profile information.

<details><summary>Parameters</summary>

### include_labels

Include labels for each ID in custom profile fields

**Type:** boolean

### user

User to retrieve profile info for

**Type:** string

</details>

## groups_create_child

Clones and archives a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Private channel to clone and archive."
}
```

</details>

## invite_channels

Invites a user to a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Channel to invite user to.",
  "user" : "User to invite to channel."
}
```

</details>

## invite_conversations

Invites users to a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "The ID of the public or private channel to invite user(s) to.",
  "users" : "A comma separated list of user IDs. Up to 30 users may be listed."
}
```

</details>

## invite_groups

Invites a user to a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Private channel to invite user to.",
  "user" : "User to invite."
}
```

</details>

## join_channels

Joins a channel, creating it if needed.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "Name of channel to join",
  "validate" : "Whether to return errors on invalid channel name instead of modifying it to meet the specified criteria."
}
```

</details>

## join_conversations

Joins an existing conversation.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "ID of conversation to join"
}
```

</details>

## kick_groups

Removes a user from a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Private channel to remove user from.",
  "user" : "User to remove from private channel."
}
```

</details>

## leave_channels

Leaves a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Channel to leave"
}
```

</details>

## leave_conversations

Leaves a conversation.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Conversation to leave"
}
```

</details>

## leave_groups

Leaves a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Private channel to leave"
}
```

</details>

## list_apps_permissions_resources

Returns list of resource grants this app has on a team.

*This operation has no parameters*

## list_apps_permissions_scopes

Returns list of scopes this app has on a team.

*This operation has no parameters*

## list_conversations

Lists all channels in a Slack team.

<details><summary>Parameters</summary>

### exclude_archived

Set to `true` to exclude archived channels from the list

**Type:** boolean

### types

Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`

**Type:** string

</details>

## list_emoji

Lists custom emoji for a team.

*This operation has no parameters*

## list_files

Lists &amp; filters team files.

<details><summary>Parameters</summary>

### channel

Filter files appearing in a specific channel, indicated by its ID.

**Type:** string

### count

**Type:** string

### ts_from

Filter files created after this timestamp (inclusive).

**Type:** number

### ts_to

Filter files created before this timestamp (inclusive).

**Type:** number

### types

Filter files by type:

* `all` - All files
* `spaces` - Posts
* `snippets` - Snippets
* `images` - Image files
* `gdocs` - Google docs
* `zips` - Zip files
* `pdfs` - PDF files

You can pass multiple values in the types argument, like `types=spaces,snippets`.The default value is `all`, which does not filter the list.

**Type:** string

### user

Filter files created by a single user.

**Type:** string

</details>

## list_groups

Lists private channels that the calling user has access to.

<details><summary>Parameters</summary>

### exclude_archived

Don't return archived private channels.

**Type:** boolean

### exclude_members

Exclude the `members` from each `group`

**Type:** boolean

</details>

## list_ims

Lists direct message channels for the calling user.

*This operation has no parameters*

## list_mpim

Lists multiparty direct message channels for the calling user.

*This operation has no parameters*

## list_reactions

Lists reactions made by a user.

<details><summary>Parameters</summary>

### count

**Type:** string

### full

If true always return the complete reaction list.

**Type:** boolean

### user

Show reactions made by this user. Defaults to the authed user.

**Type:** string

</details>

## list_reminders

Lists all reminders created by or for a given user.

*This operation has no parameters*

## list_stars

Lists stars for a user.

<details><summary>Parameters</summary>

### count

**Type:** string

</details>

## list_usergroups

List all User Groups for a team

<details><summary>Parameters</summary>

### include_count

Include the number of users in each User Group.

**Type:** boolean

### include_disabled

Include disabled User Groups.

**Type:** boolean

### include_users

Include the list of users for each User Group.

**Type:** boolean

</details>

## list_users

Lists all users in a Slack team.

<details><summary>Parameters</summary>

### include_locale

Set this to `true` to receive the locale for users. Defaults to `false`

**Type:** boolean

### presence

Deprecated. Whether to include presence data in the output. Defaults to `false`. Setting this to `true` reduces performance, especially with large teams.

**Type:** boolean

</details>

## list_users_conversations

List conversations the calling user may access.

<details><summary>Parameters</summary>

### exclude_archived

Set to `true` to exclude archived channels from the list

**Type:** boolean

### types

Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`

**Type:** string

### user

Browse conversations by a specific user ID's membership. Non-public channels are restricted to those where the calling user shares membership.

**Type:** string

</details>

## list_users_from_usergroups

List all users in a User Group

<details><summary>Parameters</summary>

### include_disabled

Allow results that involve disabled User Groups.

**Type:** boolean

### usergroup

The encoded ID of the User Group to update.

**Type:** string

</details>

## lookup_users_by_email

Find a user with an email address.

<details><summary>Parameters</summary>

### email

An email address belonging to a user in the workspace

**Type:** string

</details>

## mark_channels

Sets the read cursor in a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Channel to set reading cursor in.",
  "ts" : "Timestamp of the most recently seen message."
}
```

</details>

## mark_groups

Sets the read cursor in a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Private channel to set reading cursor in.",
  "ts" : "Timestamp of the most recently seen message."
}
```

</details>

## mark_im

Sets the read cursor in a direct message channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Direct message channel to set reading cursor in.",
  "ts" : "Timestamp of the most recently seen message."
}
```

</details>

## mark_mpim

Sets the read cursor in a multiparty direct message channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "multiparty direct message channel to set reading cursor in.",
  "ts" : "Timestamp of the most recently seen message."
}
```

</details>

## mark_reminders_complete

Marks a reminder as complete.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "reminder" : "The ID of the reminder to be marked as complete"
}
```

</details>

## mpim_history

Fetches history of messages and events from a multiparty direct message.

<details><summary>Parameters</summary>

### channel

Multiparty direct message to fetch history for.

**Type:** string

### count

Number of messages to return, between 1 and 1000.

**Type:** integer

### inclusive

Include messages with latest or oldest timestamp in results.

**Type:** boolean

### latest

End of time range of messages to include in results.

**Type:** number

### oldest

Start of time range of messages to include in results.

**Type:** number

### unreads

Include `unread_count_display` in the output?

**Type:** boolean

</details>

## open_conversations

Opens or resumes a direct message or multi-person direct message.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "return_im" : "Boolean, indicates you want the full IM channel definition in the response.",
  "channel" : "Resume a conversation by supplying an `im` or `mpim`'s ID. Or provide the `users` field instead.",
  "users" : "Comma separated lists of users. If only one user is included, this creates a 1:1 DM. The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a `channel` when not supplying `users`."
}
```

</details>

## open_dialog

Open a dialog with a user

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "dialog" : "The dialog definition. This must be a JSON-encoded string.",
  "trigger_id" : "Exchange a trigger to post to the user."
}
```

</details>

## open_groups

Opens a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Private channel to open."
}
```

</details>

## open_im

Opens a direct message channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "return_im" : "Boolean, indicates you want the full IM channel definition in the response.",
  "include_locale" : "Set this to `true` to receive the locale for this im. Defaults to `false`",
  "user" : "User to open a direct message channel with."
}
```

</details>

## open_mpim

This method opens a multiparty direct message.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "users" : "Comma separated lists of users. The ordering of the users is preserved whenever a MPIM group is returned."
}
```

</details>

## pins_list

Lists items pinned to a channel.

<details><summary>Parameters</summary>

### channel

Channel to get pinned items for.

**Type:** string

</details>

## post_chat_ephemeral

Sends an ephemeral message to a user in a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "link_names" : "Find and link channel names and usernames.",
  "attachments" : "A JSON-based array of structured attachments, presented as a URL-encoded string.",
  "as_user" : "Pass true to post the message as the authed bot. Defaults to false.",
  "channel" : "Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.",
  "text" : "Text of the message to send. See below for an explanation of [formatting](#formatting). This field is usually required, unless you're providing only `attachments` instead.",
  "parse" : "Change how messages are treated. Defaults to `none`. See [below](#formatting).",
  "user" : "`id` of the user who will receive the ephemeral message. The user should be in the channel specified by the `channel` argument."
}
```

</details>

## post_chat_me_message

Share a me message into a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Channel to send message to. Can be a public channel, private group or IM channel. Can be an encoded ID, or a name.",
  "text" : "Text of the message to send."
}
```

</details>

## post_chat_message

Sends a message to a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "icon_url" : "URL to an image to use as the icon for this message. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below.",
  "link_names" : "Find and link channel names and usernames.",
  "attachments" : "A JSON-based array of structured attachments, presented as a URL-encoded string.",
  "icon_emoji" : "Emoji to use as the icon for this message. Overrides `icon_url`. Must be used in conjunction with `as_user` set to `false`, otherwise ignored. See [authorship](#authorship) below.",
  "channel" : "Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details.",
  "parse" : "Change how messages are treated. Defaults to `none`. See [below](#formatting).",
  "mrkdwn" : "Disable Slack markup parsing by setting to `false`. Enabled by default.",
  "as_user" : "Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [authorship](#authorship) below.",
  "thread_ts" : "Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.",
  "unfurl_media" : "Pass false to disable unfurling of media content.",
  "unfurl_links" : "Pass true to enable unfurling of primarily text-based content.",
  "reply_broadcast" : "Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.",
  "text" : "Text of the message to send. See below for an explanation of [formatting](#formatting). This field is usually required, unless you're providing only `attachments` instead. Provide no more than 40,000 characters or [risk truncation](/changelog/2018-04-truncating-really-long-messages).",
  "username" : "Set your bot's user name. Must be used in conjunction with `as_user` set to false, otherwise ignored. See [authorship](#authorship) below."
}
```

</details>

## remove_pins

Un-pins an item from a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File to un-pin.",
  "channel" : "Channel where the item is pinned to.",
  "file_comment" : "File comment to un-pin.",
  "timestamp" : "Timestamp of the message to un-pin."
}
```

</details>

## remove_reactions

Removes a reaction from an item.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File to remove reaction from.",
  "name" : "Reaction (emoji) name.",
  "channel" : "Channel where the message to remove reaction from was posted.",
  "file_comment" : "File comment to remove reaction from.",
  "timestamp" : "Timestamp of the message to remove reaction from."
}
```

</details>

## remove_stars

Removes a star from an item.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File to remove star from.",
  "channel" : "Channel to remove star from, or channel where the message to remove star from was posted (used with `timestamp`).",
  "file_comment" : "File comment to remove star from.",
  "timestamp" : "Timestamp of the message to remove star from."
}
```

</details>

## remove_user_from_channel

Removes a user from a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Channel to remove user from.",
  "user" : "User to remove from channel."
}
```

</details>

## remove_user_from_conversation

Removes a user from a conversation.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "ID of conversation to remove user from.",
  "user" : "User ID to be removed."
}
```

</details>

## rename_channels

Renames a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "New name for channel.",
  "channel" : "Channel to rename",
  "validate" : "Whether to return errors on invalid channel name instead of modifying it to meet the specified criteria."
}
```

</details>

## rename_conversations

Renames a conversation.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "New name for conversation.",
  "channel" : "ID of conversation to rename"
}
```

</details>

## rename_groups

Renames a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "New name for private channel.",
  "channel" : "Private channel to rename",
  "validate" : "Whether to return errors on invalid channel name instead of modifying it to meet the specified criteria."
}
```

</details>

## request_apps_permissions

Allows an app to request additional scopes

<details><summary>Parameters</summary>

### scopes

A comma separated list of scopes to request for

**Type:** string

### trigger_id

Token used to trigger the permissions API

**Type:** string

</details>

## revoke_auth

Revokes a token.

<details><summary>Parameters</summary>

### test

Setting this parameter to `1` triggers a _testing mode_ where the specified token will not actually be revoked.

**Type:** boolean

</details>

## revoke_files_public_url

Revokes public/external sharing access for a file

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "file" : "File to revoke"
}
```

</details>

## schedule_chat_message

Sends a message to a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "link_names" : "Find and link channel names and usernames.",
  "attachments" : "A JSON-based array of structured attachments, presented as a URL-encoded string.",
  "as_user" : "Pass true to post the message as the authed user, instead of as a bot. Defaults to false. See [authorship](#authorship) below.",
  "thread_ts" : "Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.",
  "unfurl_media" : "Pass false to disable unfurling of media content.",
  "channel" : "Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details.",
  "unfurl_links" : "Pass true to enable unfurling of primarily text-based content.",
  "reply_broadcast" : "Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.",
  "text" : "Text of the message to send. See below for an explanation of [formatting](#formatting). This field is usually required, unless you're providing only `attachments` instead. Provide no more than 40,000 characters or [risk truncation](/changelog/2018-04-truncating-really-long-messages).",
  "parse" : "Change how messages are treated. Defaults to `none`. See [below](#formatting).",
  "post_at" : "Unix EPOCH timestamp of time in future to send the message."
}
```

</details>

## search_all

Searches for messages and files matching a query.

<details><summary>Parameters</summary>

### count

**Type:** string

### highlight

Pass a value of `true` to enable query highlight markers (see below).

**Type:** boolean

### query

Search query. May contains booleans, etc.

**Type:** string

### sort

Return matches sorted by either `score` or `timestamp`.

**Type:** string

### sort_dir

Change sort direction to ascending (`asc`) or descending (`desc`).

**Type:** string

</details>

## search_files

Searches for files matching a query.

<details><summary>Parameters</summary>

### count

**Type:** string

### highlight

Pass a value of `true` to enable query highlight markers (see below).

**Type:** boolean

### query

Search query.

**Type:** string

### sort

Return matches sorted by either `score` or `timestamp`.

**Type:** string

### sort_dir

Change sort direction to ascending (`asc`) or descending (`desc`).

**Type:** string

</details>

## search_messages

Searches for messages matching a query.

<details><summary>Parameters</summary>

### count

Pass the number of results you want per "page". Maximum of `100`.

**Type:** string

### highlight

Pass a value of `true` to enable query highlight markers (see below).

**Type:** boolean

### query

Search query.

**Type:** string

### sort

Return matches sorted by either `score` or `timestamp`.

**Type:** string

### sort_dir

Change sort direction to ascending (`asc`) or descending (`desc`).

**Type:** string

</details>

## set_active_users

Marked a user as active. Deprecated and non-functional.

*This operation has no parameters*

## set_channels_purpose

Sets the purpose for a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "purpose" : "The new purpose",
  "channel" : "Channel to set the purpose of"
}
```

</details>

## set_channels_topic

Sets the topic for a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Channel to set the topic of",
  "topic" : "The new topic"
}
```

</details>

## set_conversations_purpose

Sets the purpose for a conversation.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "purpose" : "A new, specialer purpose",
  "channel" : "Conversation to set the purpose of"
}
```

</details>

## set_conversations_topic

Sets the topic for a conversation.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Conversation to set the topic of",
  "topic" : "The new topic string. Does not support formatting or linkification."
}
```

</details>

## set_groups_purpose

Sets the purpose for a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "purpose" : "The new purpose",
  "channel" : "Private channel to set the purpose of"
}
```

</details>

## set_groups_topic

Sets the topic for a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Private channel to set the topic of",
  "topic" : "The new topic"
}
```

</details>

## set_users_presence

Manually sets user presence.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "presence" : "Either `auto` or `away`"
}
```

</details>

## set_users_profile

Set the profile information for a user.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "profile" : "Collection of key:value pairs presented as a URL-encoded JSON hash.",
  "name" : "Name of a single key to set. Usable only if `profile` is not passed.",
  "user" : "ID of user to change. This argument may only be specified by team admins on paid teams.",
  "value" : "Value to set a single key to. Usable only if `profile` is not passed."
}
```

</details>

## start_rtm

Starts a Real Time Messaging session.

<details><summary>Parameters</summary>

### batch_presence_aware

Batch presence deliveries via subscription. Enabling changes the shape of `presence_change` events. See [batch presence](/docs/presence-and-status#batching).

**Type:** boolean

### include_locale

Set this to `true` to receive the locale for users and channels. Defaults to `false`

**Type:** boolean

### mpim_aware

Returns MPIMs to the client in the API response.

**Type:** boolean

### no_latest

Exclude latest timestamps for channels, groups, mpims, and ims. Automatically sets `no_unreads` to `1`

**Type:** boolean

### no_unreads

Skip unread counts for each channel (improves performance).

**Type:** boolean

### presence_sub

Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions).

**Type:** boolean

### simple_latest

Return timestamp only for latest message object of each channel (improves performance).

**Type:** boolean

</details>

## test_auth

Checks authentication &amp; identity.

*This operation has no parameters*

## unarchive_channels

Unarchives a channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Channel to unarchive"
}
```

</details>

## unarchive_conversations

Reverses conversation archival.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "ID of conversation to unarchive"
}
```

</details>

## unarchive_groups

Unarchives a private channel.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channel" : "Private channel to unarchive"
}
```

</details>

## unfurl_chat

Provide custom unfurl behavior for user-posted URLs

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "unfurls" : "URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl message attachments.",
  "user_auth_message" : "Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior",
  "channel" : "Channel ID of the message",
  "user_auth_url" : "Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded.",
  "user_auth_required" : "Set to `true` or `1` to indicate the user must install your Slack app to trigger unfurls for this domain",
  "ts" : "Timestamp of the message to add unfurl behavior to."
}
```

</details>

## update_chat

Updates a message.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "link_names" : "Find and link channel names and usernames. Defaults to `none`. See [below](#formatting).",
  "attachments" : "A JSON-based array of structured attachments, presented as a URL-encoded string. This field is required when not presenting `text`.",
  "as_user" : "Pass true to update the message as the authed user. [Bot users](/bot-users) in this context are considered authed users.",
  "channel" : "Channel containing the message to be updated.",
  "text" : "New text for the message, using the [default formatting rules](/docs/formatting). It's not required when presenting `attachments`.",
  "parse" : "Change how messages are treated. Defaults to `client`, unlike `chat.postMessage`. See [below](#formatting).",
  "ts" : "Timestamp of the message to be updated."
}
```

</details>

## update_usergroups

Update an existing User Group

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "channels" : "A comma separated string of encoded channel IDs for which the User Group uses as a default.",
  "usergroup" : "The encoded ID of the User Group to update.",
  "name" : "A name for the User Group. Must be unique among User Groups.",
  "description" : "A short description of the User Group.",
  "handle" : "A mention handle. Must be unique among channels, users and User Groups.",
  "include_count" : "Include the number of users in the User Group."
}
```

</details>

## update_users_for_usergroups

Update the list of users for a User Group

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "usergroup" : "The encoded ID of the User Group to update.",
  "include_count" : "Include the number of users in the User Group.",
  "users" : "A comma separated string of encoded user IDs that represent the entire list of users for the User Group."
}
```

</details>

## users_delete_photo

Delete the user profile photo

*This operation has no parameters*

