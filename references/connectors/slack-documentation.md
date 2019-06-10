---
id: slack-documentation
title: Slack (version v1.*.*)
sidebar_label: Slack
layout: docs.mustache
---

## add_files_comments

Add a comment to an existing file.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## add_pins

Pins an item to a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## add_reactions

Adds a reaction to an item.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## add_reminders

Creates a reminder.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## add_stars

Adds a star to an item.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## archive_channels

Archives a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## archive_conversations

Archives a conversation.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## archive_groups

Archives a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## check_api

Checks API calling code.

<details><summary>Parameters</summary>

#### error

Error response to return

**Type:** string

#### foo

example property to return

**Type:** string

</details>

## close_conversations

Closes a direct message or multi-person direct message.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## close_im

Close a direct message channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## close_mpim

Closes a multiparty direct message channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## connect_rtm

Starts a Real Time Messaging session.

<details><summary>Parameters</summary>

#### batch_presence_aware

Batch presence deliveries via subscription. Enabling changes the shape of `presence_change` events. See [batch presence](/docs/presence-and-status#batching).

**Type:** boolean

#### presence_sub

Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions).

**Type:** boolean

</details>

## create_channels

Creates a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_conversations

Initiates a public or private channel-based conversation

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_groups

Creates a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_usergroups

Create a User Group

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_chat

Deletes a message.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_files

Deletes a file.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_files_comments

Deletes an existing comment on a file.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_reminders

Deletes a reminder.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## disable_usergroups

Disable an existing User Group

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## dnd_set_snooze

Turns on Do Not Disturb mode for the current user, or changes its duration.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## edit_files_comments

Edit an existing file comment.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## enable_files_public_url

Enables a file for public/external sharing.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## enable_usergroups

Enable a User Group

<details><summary>Parameters</summary>

#### $body

**Type:** object

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

#### to_old

Specify `true` to convert `W` global user IDs to workspace-specific `U` IDs. Defaults to `false`.

**Type:** boolean

#### users

A comma-separated list of user ids, up to 400 per request

**Type:** string

</details>

## files_upload

Uploads or creates a file.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_apps_permissions_info

Returns list of permissions this app has on a team.

*This operation has no parameters*

## get_bots_info

Gets information about a bot user.

<details><summary>Parameters</summary>

#### bot

Bot user to get info on

**Type:** string

</details>

## get_channels_history

Fetches history of messages and events from a channel.

<details><summary>Parameters</summary>

#### channel (required)

Channel to fetch history for.

**Type:** string

#### count

Number of messages to return, between 1 and 1000.

**Type:** integer

#### inclusive

Include messages with latest or oldest timestamp in results.

**Type:** boolean

#### latest

End of time range of messages to include in results.

**Type:** number

#### oldest

Start of time range of messages to include in results.

**Type:** number

#### unreads

Include `unread_count_display` in the output?

**Type:** boolean

</details>

## get_channels_info

Gets information about a channel.

<details><summary>Parameters</summary>

#### channel

Channel to get info on

**Type:** string

#### include_locale

Set this to `true` to receive the locale for this channel. Defaults to `false`

**Type:** boolean

</details>

## get_channels_list

Lists all channels in a Slack team.

<details><summary>Parameters</summary>

#### exclude_archived

Exclude archived channels from the list

**Type:** boolean

#### exclude_members

Exclude the `members` collection from each `channel`

**Type:** boolean

</details>

## get_channels_replies

Retrieve a thread of messages posted to a channel

<details><summary>Parameters</summary>

#### channel

Channel to fetch thread from

**Type:** string

#### thread_ts

Unique identifier of a thread's parent message

**Type:** string

</details>

## get_chat_permalink

Retrieve a permalink URL for a specific extant message

<details><summary>Parameters</summary>

#### channel

The ID of the conversation or channel containing the message

**Type:** string

#### message_ts

A message's `ts` value, uniquely identifying it within a channel

**Type:** number

</details>

## get_conversations_history

Fetches a conversation's history of messages and events.

<details><summary>Parameters</summary>

#### channel

Conversation ID to fetch history for.

**Type:** string

#### inclusive

Include messages with latest or oldest timestamp in results only when either timestamp is specified.

**Type:** boolean

#### latest

End of time range of messages to include in results.

**Type:** number

#### oldest

Start of time range of messages to include in results.

**Type:** number

</details>

## get_conversations_info

Retrieve information about a conversation.

<details><summary>Parameters</summary>

#### channel

Conversation ID to learn more about

**Type:** string

#### include_locale

Set this to `true` to receive the locale for this conversation. Defaults to `false`

**Type:** boolean

</details>

## get_conversations_members

Retrieve members of a conversation.

<details><summary>Parameters</summary>

#### channel

ID of the conversation to retrieve members for

**Type:** string

</details>

## get_conversations_replies

Retrieve a thread of messages posted to a conversation

<details><summary>Parameters</summary>

#### channel

Conversation ID to fetch thread from.

**Type:** string

#### inclusive

Include messages with latest or oldest timestamp in results only when either timestamp is specified.

**Type:** boolean

#### latest

End of time range of messages to include in results.

**Type:** number

#### oldest

Start of time range of messages to include in results.

**Type:** number

#### ts

Unique identifier of a thread's parent message.

**Type:** string

</details>

## get_dnd_info

Retrieves a user's current Do Not Disturb status.

<details><summary>Parameters</summary>

#### user

User to fetch status for (defaults to current user)

**Type:** string

</details>

## get_dnd_team_info

Retrieves the Do Not Disturb status for users on a team.

<details><summary>Parameters</summary>

#### users

Comma-separated list of users to fetch Do Not Disturb status for

**Type:** string

</details>

## get_files_info

Gets information about a team file.

<details><summary>Parameters</summary>

#### count

**Type:** string

#### file

Specify a file by providing its ID.

**Type:** string

</details>

## get_groups_history

Fetches history of messages and events from a private channel.

<details><summary>Parameters</summary>

#### channel

Private channel to fetch history for.

**Type:** string

#### count

Number of messages to return, between 1 and 1000.

**Type:** integer

#### inclusive

Include messages with latest or oldest timestamp in results.

**Type:** boolean

#### latest

End of time range of messages to include in results.

**Type:** number

#### oldest

Start of time range of messages to include in results.

**Type:** number

#### unreads

Include `unread_count_display` in the output?

**Type:** boolean

</details>

## get_groups_info

Gets information about a private channel.

<details><summary>Parameters</summary>

#### channel

Private channel to get info on

**Type:** string

#### include_locale

Set this to `true` to receive the locale for this group. Defaults to `false`

**Type:** boolean

</details>

## get_groups_replies

Retrieve a thread of messages posted to a private channel

<details><summary>Parameters</summary>

#### channel

Private channel to fetch thread from

**Type:** string

#### thread_ts

Unique identifier of a thread's parent message

**Type:** string

</details>

## get_im_history

Fetches history of messages and events from direct message channel.

<details><summary>Parameters</summary>

#### channel

Direct message channel to fetch history for.

**Type:** string

#### count

Number of messages to return, between 1 and 1000.

**Type:** integer

#### inclusive

Include messages with latest or oldest timestamp in results.

**Type:** boolean

#### latest

End of time range of messages to include in results.

**Type:** number

#### oldest

Start of time range of messages to include in results.

**Type:** number

#### unreads

Include `unread_count_display` in the output?

**Type:** boolean

</details>

## get_im_replies

Retrieve a thread of messages posted to a direct message conversation

<details><summary>Parameters</summary>

#### channel

Direct message channel to fetch thread from

**Type:** string

#### thread_ts

Unique identifier of a thread's parent message

**Type:** string

</details>

## get_mpim_replies

Retrieve a thread of messages posted to a direct message conversation from a multiparty direct message.

<details><summary>Parameters</summary>

#### channel

Multiparty direct message channel to fetch thread from.

**Type:** string

#### thread_ts

Unique identifier of a thread's parent message.

**Type:** string

</details>

## get_oauth_access

Exchanges a temporary OAuth verifier code for an access token.

<details><summary>Parameters</summary>

#### client_id

Issued when you created your application.

**Type:** string

#### client_secret

Issued when you created your application.

**Type:** string

#### code

The `code` param returned via the OAuth callback.

**Type:** string

#### redirect_uri

This must match the originally submitted URI (if one was sent).

**Type:** string

#### single_channel

Request the user to add your app only to a single channel.

**Type:** boolean

</details>

## get_oauth_token

Exchanges a temporary OAuth verifier code for a workspace token.

<details><summary>Parameters</summary>

#### client_id

Issued when you created your application.

**Type:** string

#### client_secret

Issued when you created your application.

**Type:** string

#### code

The `code` param returned via the OAuth callback.

**Type:** string

#### redirect_uri

This must match the originally submitted URI (if one was sent).

**Type:** string

#### single_channel

Request the user to add your app only to a single channel.

**Type:** boolean

</details>

## get_reactions

Gets reactions for an item.

<details><summary>Parameters</summary>

#### channel

Channel where the message to get reactions for was posted.

**Type:** string

#### file

File to get reactions for.

**Type:** string

#### file_comment

File comment to get reactions for.

**Type:** string

#### full

If true always return the complete reaction list.

**Type:** boolean

#### timestamp

Timestamp of the message to get reactions for.

**Type:** number

</details>

## get_reminders_info

Gets information about a reminder.

<details><summary>Parameters</summary>

#### reminder

The ID of the reminder

**Type:** string

</details>

## get_team_access_logs

Gets the access logs for the current team.

<details><summary>Parameters</summary>

#### before

End of time range of logs to include in results (inclusive).

**Type:** integer

#### count

**Type:** string

</details>

## get_team_billable_info

Gets billable users information for the current team.

<details><summary>Parameters</summary>

#### user

A user to retrieve the billable information for. Defaults to all users.

**Type:** string

</details>

## get_team_info

Gets information about the current team.

*This operation has no parameters*

## get_team_integration_logs

Gets the integration logs for the current team.

<details><summary>Parameters</summary>

#### app_id

Filter logs to this Slack app. Defaults to all logs.

**Type:** integer

#### change_type

Filter logs with this change type. Defaults to all logs.

**Type:** string

#### count

**Type:** string

#### service_id

Filter logs to this service. Defaults to all logs.

**Type:** integer

#### user

Filter logs generated by this user’s actions. Defaults to all logs.

**Type:** string

</details>

## get_team_profile

Retrieve a team's profile.

<details><summary>Parameters</summary>

#### visibility

Filter by visibility.

**Type:** string

</details>

## get_users_identity

Get a user's identity.

*This operation has no parameters*

## get_users_info

Gets information about a user.

<details><summary>Parameters</summary>

#### include_locale

Set this to `true` to receive the locale for this user. Defaults to `false`

**Type:** boolean

#### user

User to get info on

**Type:** string

</details>

## get_users_presence

Gets user presence information.

<details><summary>Parameters</summary>

#### user

User to get presence info on. Defaults to the authed user.

**Type:** string

</details>

## get_users_profile

Retrieves a user's profile information.

<details><summary>Parameters</summary>

#### include_labels

Include labels for each ID in custom profile fields

**Type:** boolean

#### user

User to retrieve profile info for

**Type:** string

</details>

## groups_create_child

Clones and archives a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## invite_channels

Invites a user to a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## invite_conversations

Invites users to a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## invite_groups

Invites a user to a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## join_channels

Joins a channel, creating it if needed.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## join_conversations

Joins an existing conversation.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## kick_groups

Removes a user from a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## leave_channels

Leaves a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## leave_conversations

Leaves a conversation.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## leave_groups

Leaves a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

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

#### exclude_archived

Set to `true` to exclude archived channels from the list

**Type:** boolean

#### types

Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`

**Type:** string

</details>

## list_emoji

Lists custom emoji for a team.

*This operation has no parameters*

## list_files

Lists & filters team files.

<details><summary>Parameters</summary>

#### channel

Filter files appearing in a specific channel, indicated by its ID.

**Type:** string

#### count

**Type:** string

#### ts_from

Filter files created after this timestamp (inclusive).

**Type:** number

#### ts_to

Filter files created before this timestamp (inclusive).

**Type:** number

#### types

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

#### user

Filter files created by a single user.

**Type:** string

</details>

## list_groups

Lists private channels that the calling user has access to.

<details><summary>Parameters</summary>

#### exclude_archived

Don't return archived private channels.

**Type:** boolean

#### exclude_members

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

#### count

**Type:** string

#### full

If true always return the complete reaction list.

**Type:** boolean

#### user

Show reactions made by this user. Defaults to the authed user.

**Type:** string

</details>

## list_reminders

Lists all reminders created by or for a given user.

*This operation has no parameters*

## list_stars

Lists stars for a user.

<details><summary>Parameters</summary>

#### count

**Type:** string

</details>

## list_usergroups

List all User Groups for a team

<details><summary>Parameters</summary>

#### include_count

Include the number of users in each User Group.

**Type:** boolean

#### include_disabled

Include disabled User Groups.

**Type:** boolean

#### include_users

Include the list of users for each User Group.

**Type:** boolean

</details>

## list_users

Lists all users in a Slack team.

<details><summary>Parameters</summary>

#### include_locale

Set this to `true` to receive the locale for users. Defaults to `false`

**Type:** boolean

#### presence

Deprecated. Whether to include presence data in the output. Defaults to `false`. Setting this to `true` reduces performance, especially with large teams.

**Type:** boolean

</details>

## list_users_conversations

List conversations the calling user may access.

<details><summary>Parameters</summary>

#### exclude_archived

Set to `true` to exclude archived channels from the list

**Type:** boolean

#### types

Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`

**Type:** string

#### user

Browse conversations by a specific user ID's membership. Non-public channels are restricted to those where the calling user shares membership.

**Type:** string

</details>

## list_users_from_usergroups

List all users in a User Group

<details><summary>Parameters</summary>

#### include_disabled

Allow results that involve disabled User Groups.

**Type:** boolean

#### usergroup

The encoded ID of the User Group to update.

**Type:** string

</details>

## lookup_users_by_email

Find a user with an email address.

<details><summary>Parameters</summary>

#### email

An email address belonging to a user in the workspace

**Type:** string

</details>

## mark_channels

Sets the read cursor in a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## mark_groups

Sets the read cursor in a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## mark_im

Sets the read cursor in a direct message channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## mark_mpim

Sets the read cursor in a multiparty direct message channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## mark_reminders_complete

Marks a reminder as complete.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## mpim_history

Fetches history of messages and events from a multiparty direct message.

<details><summary>Parameters</summary>

#### channel

Multiparty direct message to fetch history for.

**Type:** string

#### count

Number of messages to return, between 1 and 1000.

**Type:** integer

#### inclusive

Include messages with latest or oldest timestamp in results.

**Type:** boolean

#### latest

End of time range of messages to include in results.

**Type:** number

#### oldest

Start of time range of messages to include in results.

**Type:** number

#### unreads

Include `unread_count_display` in the output?

**Type:** boolean

</details>

## open_conversations

Opens or resumes a direct message or multi-person direct message.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## open_dialog

Open a dialog with a user

*This operation has no parameters*

## open_groups

Opens a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## open_im

Opens a direct message channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## open_mpim

This method opens a multiparty direct message.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## pins_list

Lists items pinned to a channel.

<details><summary>Parameters</summary>

#### channel

Channel to get pinned items for.

**Type:** string

</details>

## post_chat_ephemeral

Sends an ephemeral message to a user in a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## post_chat_me_message

Share a me message into a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## post_chat_message

Sends a message to a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## remove_pins

Un-pins an item from a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## remove_reactions

Removes a reaction from an item.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## remove_stars

Removes a star from an item.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## remove_user_from_channel

Removes a user from a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## remove_user_from_conversation

Removes a user from a conversation.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## rename_channels

Renames a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## rename_conversations

Renames a conversation.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## rename_groups

Renames a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## request_apps_permissions

Allows an app to request additional scopes

<details><summary>Parameters</summary>

#### scopes

A comma separated list of scopes to request for

**Type:** string

#### trigger_id

Token used to trigger the permissions API

**Type:** string

</details>

## revoke_auth

Revokes a token.

<details><summary>Parameters</summary>

#### test

Setting this parameter to `1` triggers a _testing mode_ where the specified token will not actually be revoked.

**Type:** boolean

</details>

## revoke_files_public_url

Revokes public/external sharing access for a file

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## schedule_chat_message

Sends a message to a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## search_all

Searches for messages and files matching a query.

<details><summary>Parameters</summary>

#### count

**Type:** string

#### highlight

Pass a value of `true` to enable query highlight markers (see below).

**Type:** boolean

#### query

Search query. May contains booleans, etc.

**Type:** string

#### sort

Return matches sorted by either `score` or `timestamp`.

**Type:** string

#### sort_dir

Change sort direction to ascending (`asc`) or descending (`desc`).

**Type:** string

</details>

## search_files

Searches for files matching a query.

<details><summary>Parameters</summary>

#### count

**Type:** string

#### highlight

Pass a value of `true` to enable query highlight markers (see below).

**Type:** boolean

#### query

Search query.

**Type:** string

#### sort

Return matches sorted by either `score` or `timestamp`.

**Type:** string

#### sort_dir

Change sort direction to ascending (`asc`) or descending (`desc`).

**Type:** string

</details>

## search_messages

Searches for messages matching a query.

<details><summary>Parameters</summary>

#### count

Pass the number of results you want per "page". Maximum of `100`.

**Type:** string

#### highlight

Pass a value of `true` to enable query highlight markers (see below).

**Type:** boolean

#### query

Search query.

**Type:** string

#### sort

Return matches sorted by either `score` or `timestamp`.

**Type:** string

#### sort_dir

Change sort direction to ascending (`asc`) or descending (`desc`).

**Type:** string

</details>

## set_active_users

Marked a user as active. Deprecated and non-functional.

*This operation has no parameters*

## set_channels_purpose

Sets the purpose for a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## set_channels_topic

Sets the topic for a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## set_conversations_purpose

Sets the purpose for a conversation.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## set_conversations_topic

Sets the topic for a conversation.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## set_groups_purpose

Sets the purpose for a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## set_groups_topic

Sets the topic for a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## set_users_presence

Manually sets user presence.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## set_users_profile

Set the profile information for a user.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## start_rtm

Starts a Real Time Messaging session.

<details><summary>Parameters</summary>

#### batch_presence_aware

Batch presence deliveries via subscription. Enabling changes the shape of `presence_change` events. See [batch presence](/docs/presence-and-status#batching).

**Type:** boolean

#### include_locale

Set this to `true` to receive the locale for users and channels. Defaults to `false`

**Type:** boolean

#### mpim_aware

Returns MPIMs to the client in the API response.

**Type:** boolean

#### no_latest

Exclude latest timestamps for channels, groups, mpims, and ims. Automatically sets `no_unreads` to `1`

**Type:** boolean

#### no_unreads

Skip unread counts for each channel (improves performance).

**Type:** boolean

#### presence_sub

Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions).

**Type:** boolean

#### simple_latest

Return timestamp only for latest message object of each channel (improves performance).

**Type:** boolean

</details>

## test_auth

Checks authentication & identity.

*This operation has no parameters*

## unarchive_channels

Unarchives a channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## unarchive_conversations

Reverses conversation archival.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## unarchive_groups

Unarchives a private channel.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## unfurl_chat

Provide custom unfurl behavior for user-posted URLs

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## update_chat

Updates a message.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## update_usergroups

Update an existing User Group

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## update_users_for_usergroups

Update the list of users for a User Group

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## users_delete_photo

Delete the user profile photo

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

