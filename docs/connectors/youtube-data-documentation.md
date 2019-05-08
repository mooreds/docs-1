---
id: youtube-data-documentation
title: Youtube Data (version v1.*.*)
sidebar_label: Youtube Data
---

## add_channel_section

Adds a channelSection for the authenticated user's channel.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part names that you can include in the parameter value are snippet and contentDetails.

**Type:** string

#### $body

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## add_item_to_playlist

Adds a resource to a playlist.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

**Type:** string

#### $body

A playlistItem resource identifies another resource, such as a video, that is included in a playlist. In addition, the playlistItem  resource contains details about the included resource that pertain specifically to how that resource is used in that playlist.

YouTube uses playlists to identify special collections of videos for a channel, such as:  
- uploaded videos 
- favorite videos 
- positively rated (liked) videos 
- watch history 
- watch later  To be more specific, these lists are associated with a channel, which is a collection of a person, group, or company's videos, playlists, and other YouTube information.

You can retrieve the playlist IDs for each of these lists from the  channel resource  for a given channel. You can then use the   playlistItems.list method to retrieve any of those lists. You can also add or remove items from those lists by calling the   playlistItems.insert and   playlistItems.delete methods. For example, if a user gives a positive rating to a video, you would insert that video into the liked videos playlist for that user's channel.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## add_moderator_to_live_chat

Adds a new moderator for the chat.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response returns. Set the parameter value to snippet.

**Type:** string

#### $body

A liveChatModerator resource represents a moderator for a YouTube live chat. A chat moderator has the ability to ban/unban users from a chat, remove message, etc.

**Type:** object

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

## add_subscription

Adds a subscription for the authenticated user's channel.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

**Type:** string

#### $body

A subscription resource contains information about a YouTube user subscription. A subscription notifies a user when new videos are added to a channel or when another user takes one of several actions on YouTube, such as uploading a video, rating a video, or commenting on a video.

**Type:** object

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

## ban_from_live_chat

Adds a new ban to the chat.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response returns. Set the parameter value to snippet.

**Type:** string

#### $body

A liveChatBan resource represents a ban for a YouTube live chat.

**Type:** object

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

## control_slate_settings_for_live_broadcast

Controls the settings for a slate that can be displayed in the broadcast stream.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the YouTube live broadcast ID that uniquely identifies the broadcast in which the slate is being updated.

**Type:** string

#### part (required)

The part parameter specifies a comma-separated list of one or more liveBroadcast resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, contentDetails, and status.

**Type:** string

#### displaySlate

The displaySlate parameter specifies whether the slate is being enabled or disabled.

**Type:** boolean

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### offsetTimeMs

The offsetTimeMs parameter specifies a positive time offset when the specified slate change will occur. The value is measured in milliseconds from the beginning of the broadcast's monitor stream, which is the time that the testing phase for the broadcast began. Even though it is specified in milliseconds, the value is actually an approximation, and YouTube completes the requested action as closely as possible to that time.

If you do not specify a value for this parameter, then YouTube performs the action as soon as possible. See the Getting started guide for more details.

Important: You should only specify a value for this parameter if your broadcast stream is delayed.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

#### walltime

The walltime parameter specifies the wall clock time at which the specified slate change will occur. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sssZ) format.

**Type:** string

</details>

## create_comment_thread

Creates a new top-level comment. To add a reply to an existing comment, use the comments.insert method instead.

<details><summary>Parameters</summary>

#### part (required)

The part parameter identifies the properties that the API response will include. Set the parameter value to snippet. The snippet part has a quota cost of 2 units.

**Type:** string

#### $body

A comment thread represents information that applies to a top level comment and all its replies. It can also include the top level comment itself and some of the replies.

**Type:** object

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

## create_live_broadcast

Creates a broadcast.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part properties that you can include in the parameter value are id, snippet, contentDetails, and status.

**Type:** string

#### $body

A liveBroadcast resource represents an event that will be streamed, via live video, on YouTube.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## create_live_stream

Creates a video stream. The stream enables you to send your video to YouTube, which can then broadcast the video to your audience.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part properties that you can include in the parameter value are id, snippet, cdn, and status.

**Type:** string

#### $body

A live stream describes a live ingestion point.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## create_message_in_live_chat

Adds a message to a live chat.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes. It identifies the properties that the write operation will set as well as the properties that the API response will include. Set the parameter value to snippet.

**Type:** string

#### $body

A liveChatMessage resource represents a chat message in a YouTube Live Chat.

**Type:** object

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

## create_playlist

Creates a playlist.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

**Type:** string

#### $body

A playlist resource represents a YouTube playlist. A playlist is a collection of videos that can be viewed sequentially and shared with other users. A playlist can contain up to 200 videos, and YouTube does not limit the number of playlists that each user creates. By default, playlists are publicly visible to other users, but playlists can be public or private.

YouTube also uses playlists to identify special collections of videos for a channel, such as:  
- uploaded videos 
- favorite videos 
- positively rated (liked) videos 
- watch history 
- watch later  To be more specific, these lists are associated with a channel, which is a collection of a person, group, or company's videos, playlists, and other YouTube information. You can retrieve the playlist IDs for each of these lists from the  channel resource for a given channel.

You can then use the   playlistItems.list method to retrieve any of those lists. You can also add or remove items from those lists by calling the   playlistItems.insert and   playlistItems.delete methods.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## delete_caption

Deletes a specified caption track.

<details><summary>Parameters</summary>

#### id (required)

The id parameter identifies the caption track that is being deleted. The value is a caption track ID as identified by the id property in a caption resource.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOf

ID of the Google+ Page for the channel that the request is be on behalf of

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## delete_channel_section

Deletes a channelSection.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the YouTube channelSection ID for the resource that is being deleted. In a channelSection resource, the id property specifies the YouTube channelSection ID.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## delete_comment

Deletes a comment.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the comment ID for the resource that is being deleted.

**Type:** string

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

## delete_item_from_playlist

Deletes a playlist item.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the YouTube playlist item ID for the playlist item that is being deleted. In a playlistItem resource, the id property specifies the playlist item's ID.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## delete_live_broadcast

Deletes a broadcast.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the YouTube live broadcast ID for the resource that is being deleted.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## delete_live_stream

Deletes a video stream.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the YouTube live stream ID for the resource that is being deleted.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## delete_message_from_live_chat

Deletes a chat message.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the YouTube chat message ID of the resource that is being deleted.

**Type:** string

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

## delete_playlist

Deletes a playlist.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the YouTube playlist ID for the playlist that is being deleted. In a playlist resource, the id property specifies the playlist's ID.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## delete_subscription

Deletes a subscription.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the YouTube subscription ID for the resource that is being deleted. In a subscription resource, the id property specifies the YouTube subscription ID.

**Type:** string

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

## delete_video

Deletes a YouTube video.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the YouTube video ID for the resource that is being deleted. In a video resource, the id property specifies the video's ID.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## download_caption

Downloads a caption track. The caption track is returned in its original format unless the request specifies a value for the tfmt parameter and in its original language unless the request specifies a value for the tlang parameter.

<details><summary>Parameters</summary>

#### id (required)

The id parameter identifies the caption track that is being retrieved. The value is a caption track ID as identified by the id property in a caption resource.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOf

ID of the Google+ Page for the channel that the request is be on behalf of

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### tfmt

The tfmt parameter specifies that the caption track should be returned in a specific format. If the parameter is not included in the request, the track is returned in its original format.

**Type:** string

**Potential values:** sbv, scc, srt, ttml, vtt

#### tlang

The tlang parameter specifies that the API response should return a translation of the specified caption track. The parameter value is an ISO 639-1 two-letter language code that identifies the desired caption language. The translation is generated by using machine translation, such as Google Translate.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_rating_for_video

Retrieves the ratings that the authorized user gave to a list of specified videos.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies a comma-separated list of the YouTube video ID(s) for the resource(s) for which you are retrieving rating data. In a video resource, the id property specifies the video's ID.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## list_activities_for_channel

Returns a list of channel activity events that match the request criteria. For example, you can retrieve events associated with a particular channel, events associated with the user's subscriptions and Google+ friends, or the YouTube home page feed, which is customized for each user.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more activity resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in an activity resource, the snippet property contains other properties that identify the type of activity, a display title for the activity, and so forth. If you set part=snippet, the API response will also contain all of those nested properties.

**Type:** string

#### channelId

The channelId parameter specifies a unique YouTube channel ID. The API will then return a list of that channel's activities.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### home

Set this parameter's value to true to retrieve the activity feed that displays on the YouTube home page for the currently authenticated user.

**Type:** boolean

#### mine

Set this parameter's value to true to retrieve a feed of the authenticated user's activities.

**Type:** boolean

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### publishedAfter

The publishedAfter parameter specifies the earliest date and time that an activity could have occurred for that activity to be included in the API response. If the parameter value specifies a day, but not a time, then any activities that occurred that day will be included in the result set. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.

**Type:** string

#### publishedBefore

The publishedBefore parameter specifies the date and time before which an activity must have occurred for that activity to be included in the API response. If the parameter value specifies a day, but not a time, then any activities that occurred that day will be excluded from the result set. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.

**Type:** string

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### regionCode

The regionCode parameter instructs the API to return results for the specified country. The parameter value is an ISO 3166-1 alpha-2 country code. YouTube uses this value when the authorized user's previous activity on YouTube does not provide enough information to generate the activity feed.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_captions

Returns a list of caption tracks that are associated with a specified video. Note that the API response does not contain the actual captions and that the captions.download method provides the ability to retrieve a caption track.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more caption resource parts that the API response will include. The part names that you can include in the parameter value are id and snippet.

**Type:** string

#### videoId (required)

The videoId parameter specifies the YouTube video ID of the video for which the API should return caption tracks.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### id

The id parameter specifies a comma-separated list of IDs that identify the caption resources that should be retrieved. Each ID must identify a caption track associated with the specified video.

**Type:** string

#### onBehalfOf

ID of the Google+ Page for the channel that the request is on behalf of.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## list_categories

Returns a list of categories that can be associated with YouTube videos.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies the videoCategory resource properties that the API response will include. Set the parameter value to snippet.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### hl

The hl parameter specifies the language that should be used for text values in the API response.

**Type:** string

#### id

The id parameter specifies a comma-separated list of video category IDs for the resources that you are retrieving.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### regionCode

The regionCode parameter instructs the API to return the list of video categories available in the specified country. The parameter value is an ISO 3166-1 alpha-2 country code.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_channel_sections

Returns channelSection resources that match the API request criteria.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more channelSection resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, and contentDetails.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a channelSection resource, the snippet property contains other properties, such as a display title for the channelSection. If you set part=snippet, the API response will also contain all of those nested properties.

**Type:** string

#### channelId

The channelId parameter specifies a YouTube channel ID. The API will only return that channel's channelSections.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### hl

The hl parameter indicates that the snippet.localized property values in the returned channelSection resources should be in the specified language if localized values for that language are available. For example, if the API request specifies hl=de, the snippet.localized properties in the API response will contain German titles if German titles are available. Channel owners can provide localized channel section titles using either the channelSections.insert or channelSections.update method.

**Type:** string

#### id

The id parameter specifies a comma-separated list of the YouTube channelSection ID(s) for the resource(s) that are being retrieved. In a channelSection resource, the id property specifies the YouTube channelSection ID.

**Type:** string

#### mine

Set this parameter's value to true to retrieve a feed of the authenticated user's channelSections.

**Type:** boolean

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## list_channels

Returns a collection of zero or more channel resources that match the request criteria.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more channel resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a channel resource, the contentDetails property contains other properties, such as the uploads properties. As such, if you set part=contentDetails, the API response will also contain all of those nested properties.

**Type:** string

#### categoryId

The categoryId parameter specifies a YouTube guide category, thereby requesting YouTube channels associated with that category.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### forUsername

The forUsername parameter specifies a YouTube username, thereby requesting the channel associated with that username.

**Type:** string

#### hl

The hl parameter should be used for filter out the properties that are not in the given language. Used for the brandingSettings part.

**Type:** string

#### id

The id parameter specifies a comma-separated list of the YouTube channel ID(s) for the resource(s) that are being retrieved. In a channel resource, the id property specifies the channel's YouTube channel ID.

**Type:** string

#### managedByMe

Note: This parameter is intended exclusively for YouTube content partners.

Set this parameter's value to true to instruct the API to only return channels managed by the content owner that the onBehalfOfContentOwner parameter specifies. The user must be authenticated as a CMS account linked to the specified content owner and onBehalfOfContentOwner must be provided.

**Type:** boolean

#### mine

Set this parameter's value to true to instruct the API to only return channels owned by the authenticated user.

**Type:** boolean

#### mySubscribers

Use the subscriptions.list method and its mySubscribers parameter to retrieve a list of subscribers to the authenticated user's channel.

**Type:** boolean

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## list_comment_threads

Returns a list of comment threads that match the API request parameters.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more commentThread resource properties that the API response will include.

**Type:** string

#### allThreadsRelatedToChannelId

The allThreadsRelatedToChannelId parameter instructs the API to return all comment threads associated with the specified channel. The response can include comments about the channel or about the channel's videos.

**Type:** string

#### channelId

The channelId parameter instructs the API to return comment threads containing comments about the specified channel. (The response will not include comments left on videos that the channel uploaded.)

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### id

The id parameter specifies a comma-separated list of comment thread IDs for the resources that should be retrieved.

**Type:** string

#### moderationStatus

Set this parameter to limit the returned comment threads to a particular moderation state.

Note: This parameter is not supported for use in conjunction with the id parameter.

**Type:** string

**Potential values:** heldForReview, likelySpam, published

#### order

The order parameter specifies the order in which the API response should list comment threads. Valid values are: 
- time - Comment threads are ordered by time. This is the default behavior.
- relevance - Comment threads are ordered by relevance.Note: This parameter is not supported for use in conjunction with the id parameter.

**Type:** string

**Potential values:** relevance, time

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### searchTerms

The searchTerms parameter instructs the API to limit the API response to only contain comments that contain the specified search terms.

Note: This parameter is not supported for use in conjunction with the id parameter.

**Type:** string

#### textFormat

Set this parameter's value to html or plainText to instruct the API to return the comments left by users in html formatted or in plain text.

**Type:** string

**Potential values:** html, plainText

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### videoId

The videoId parameter instructs the API to return comment threads associated with the specified video ID.

**Type:** string

</details>

## list_comments

Returns a list of comments that match the API request parameters.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more comment resource properties that the API response will include.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### id

The id parameter specifies a comma-separated list of comment IDs for the resources that are being retrieved. In a comment resource, the id property specifies the comment's ID.

**Type:** string

#### parentId

The parentId parameter specifies the ID of the comment for which replies should be retrieved.

Note: YouTube currently supports replies only for top-level comments. However, replies to replies may be supported in the future.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### textFormat

This parameter indicates whether the API should return comments formatted as HTML or as plain text.

**Type:** string

**Potential values:** html, plainText

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_content_regions

Returns a list of content regions that the YouTube website supports.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies the i18nRegion resource properties that the API response will include. Set the parameter value to snippet.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### hl

The hl parameter specifies the language that should be used for text values in the API response.

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

## list_guide_categories

Returns a list of categories that can be associated with YouTube channels.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies the guideCategory resource properties that the API response will include. Set the parameter value to snippet.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### hl

The hl parameter specifies the language that will be used for text values in the API response.

**Type:** string

#### id

The id parameter specifies a comma-separated list of the YouTube channel category ID(s) for the resource(s) that are being retrieved. In a guideCategory resource, the id property specifies the YouTube channel category ID.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### regionCode

The regionCode parameter instructs the API to return the list of guide categories available in the specified country. The parameter value is an ISO 3166-1 alpha-2 country code.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_items_in_playlist

Returns a collection of playlist items that match the API request parameters. You can retrieve all of the playlist items in a specified playlist or retrieve one or more playlist items by their unique IDs.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more playlistItem resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a playlistItem resource, the snippet property contains numerous fields, including the title, description, position, and resourceId properties. As such, if you set part=snippet, the API response will contain all of those properties.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### id

The id parameter specifies a comma-separated list of one or more unique playlist item IDs.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### playlistId

The playlistId parameter specifies the unique ID of the playlist for which you want to retrieve playlist items. Note that even though this is an optional parameter, every request to retrieve playlist items must specify a value for either the id parameter or the playlistId parameter.

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

#### videoId

The videoId parameter specifies that the request should return only the playlist items that contain the specified video.

**Type:** string

</details>

## list_languages

Returns a list of application languages that the YouTube website supports.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies the i18nLanguage resource properties that the API response will include. Set the parameter value to snippet.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### hl

The hl parameter specifies the language that should be used for text values in the API response.

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

## list_live_broadcasts

Returns a list of YouTube broadcasts that match the API request parameters.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more liveBroadcast resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, contentDetails, and status.

**Type:** string

#### broadcastStatus

The broadcastStatus parameter filters the API response to only include broadcasts with the specified status.

**Type:** string

**Potential values:** active, all, completed, upcoming

#### broadcastType

The broadcastType parameter filters the API response to only include broadcasts with the specified type. This is only compatible with the mine filter for now.

**Type:** string

**Potential values:** all, event, persistent

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### id

The id parameter specifies a comma-separated list of YouTube broadcast IDs that identify the broadcasts being retrieved. In a liveBroadcast resource, the id property specifies the broadcast's ID.

**Type:** string

#### mine

The mine parameter can be used to instruct the API to only return broadcasts owned by the authenticated user. Set the parameter value to true to only retrieve your own broadcasts.

**Type:** boolean

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## list_live_streams

Returns a list of video streams that match the API request parameters.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more liveStream resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, cdn, and status.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### id

The id parameter specifies a comma-separated list of YouTube stream IDs that identify the streams being retrieved. In a liveStream resource, the id property specifies the stream's ID.

**Type:** string

#### mine

The mine parameter can be used to instruct the API to only return streams owned by the authenticated user. Set the parameter value to true to only retrieve your own streams.

**Type:** boolean

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## list_members_in_channel

Lists sponsors for a channel.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies the sponsor resource parts that the API response will include. Supported values are id and snippet.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### filter

The filter parameter specifies which channel sponsors to return.

**Type:** string

**Potential values:** all, newest

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

## list_messages_in_live_chat

Lists live chat messages for a specific chat.

<details><summary>Parameters</summary>

#### liveChatId (required)

The liveChatId parameter specifies the ID of the chat whose messages will be returned.

**Type:** string

#### part (required)

The part parameter specifies the liveChatComment resource parts that the API response will include. Supported values are id and snippet.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### hl

The hl parameter instructs the API to retrieve localized resource metadata for a specific application language that the YouTube website supports. The parameter value must be a language code included in the list returned by the i18nLanguages.list method.

If localized resource details are available in that language, the resource's snippet.localized object will contain the localized values. However, if localized details are not available, the snippet.localized object will contain resource details in the resource's default language.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### profileImageSize

The profileImageSize parameter specifies the size of the user profile pictures that should be returned in the result set. Default: 88.

**Type:** integer

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_moderators_for_live_chat

Lists moderators for a live chat.

<details><summary>Parameters</summary>

#### liveChatId (required)

The liveChatId parameter specifies the YouTube live chat for which the API should return moderators.

**Type:** string

#### part (required)

The part parameter specifies the liveChatModerator resource parts that the API response will include. Supported values are id and snippet.

**Type:** string

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

## list_playlists

Returns a collection of playlists that match the API request parameters. For example, you can retrieve all playlists that the authenticated user owns, or you can retrieve one or more playlists by their unique IDs.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a playlist resource, the snippet property contains properties like author, title, description, tags, and timeCreated. As such, if you set part=snippet, the API response will contain all of those properties.

**Type:** string

#### channelId

This value indicates that the API should only return the specified channel's playlists.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### hl

The hl parameter should be used for filter out the properties that are not in the given language. Used for the snippet part.

**Type:** string

#### id

The id parameter specifies a comma-separated list of the YouTube playlist ID(s) for the resource(s) that are being retrieved. In a playlist resource, the id property specifies the playlist's YouTube playlist ID.

**Type:** string

#### mine

Set this parameter's value to true to instruct the API to only return playlists owned by the authenticated user.

**Type:** boolean

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## list_reasons_for_reporting_abuse

Returns a list of abuse reasons that can be used for reporting abusive videos.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies the videoCategory resource parts that the API response will include. Supported values are id and snippet.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### hl

The hl parameter specifies the language that should be used for text values in the API response.

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

## list_subscriptions

Returns subscription resources that match the API request criteria.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more subscription resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a subscription resource, the snippet property contains other properties, such as a display title for the subscription. If you set part=snippet, the API response will also contain all of those nested properties.

**Type:** string

#### channelId

The channelId parameter specifies a YouTube channel ID. The API will only return that channel's subscriptions.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### forChannelId

The forChannelId parameter specifies a comma-separated list of channel IDs. The API response will then only contain subscriptions matching those channels.

**Type:** string

#### id

The id parameter specifies a comma-separated list of the YouTube subscription ID(s) for the resource(s) that are being retrieved. In a subscription resource, the id property specifies the YouTube subscription ID.

**Type:** string

#### mine

Set this parameter's value to true to retrieve a feed of the authenticated user's subscriptions.

**Type:** boolean

#### myRecentSubscribers

Set this parameter's value to true to retrieve a feed of the subscribers of the authenticated user in reverse chronological order (newest first).

**Type:** boolean

#### mySubscribers

Set this parameter's value to true to retrieve a feed of the subscribers of the authenticated user in no particular order.

**Type:** boolean

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

**Type:** string

#### order

The order parameter specifies the method that will be used to sort resources in the API response.

**Type:** string

**Potential values:** alphabetical, relevance, unread

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

## list_super_chat_events

Lists Super Chat events for a channel.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies the superChatEvent resource parts that the API response will include. Supported values are id and snippet.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### hl

The hl parameter instructs the API to retrieve localized resource metadata for a specific application language that the YouTube website supports. The parameter value must be a language code included in the list returned by the i18nLanguages.list method.

If localized resource details are available in that language, the resource's snippet.localized object will contain the localized values. However, if localized details are not available, the snippet.localized object will contain resource details in the resource's default language.

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

## list_videos

Returns a list of videos that match the API request parameters.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more video resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a video resource, the snippet property contains the channelId, title, description, tags, and categoryId properties. As such, if you set part=snippet, the API response will contain all of those properties.

**Type:** string

#### chart

The chart parameter identifies the chart that you want to retrieve.

**Type:** string

**Potential values:** mostPopular

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### hl

The hl parameter instructs the API to retrieve localized resource metadata for a specific application language that the YouTube website supports. The parameter value must be a language code included in the list returned by the i18nLanguages.list method.

If localized resource details are available in that language, the resource's snippet.localized object will contain the localized values. However, if localized details are not available, the snippet.localized object will contain resource details in the resource's default language.

**Type:** string

#### id

The id parameter specifies a comma-separated list of the YouTube video ID(s) for the resource(s) that are being retrieved. In a video resource, the id property specifies the video's ID.

**Type:** string

#### locale

DEPRECATED

**Type:** string

#### maxHeight

The maxHeight parameter specifies a maximum height of the embedded player. If maxWidth is provided, maxHeight may not be reached in order to not violate the width request.

**Type:** integer

#### maxWidth

The maxWidth parameter specifies a maximum width of the embedded player. If maxHeight is provided, maxWidth may not be reached in order to not violate the height request.

**Type:** integer

#### myRating

Set this parameter's value to like or dislike to instruct the API to only return videos liked or disliked by the authenticated user.

**Type:** string

**Potential values:** dislike, like

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### regionCode

The regionCode parameter instructs the API to select a video chart available in the specified region. This parameter can only be used in conjunction with the chart parameter. The parameter value is an ISO 3166-1 alpha-2 country code.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### videoCategoryId

The videoCategoryId parameter identifies the video category for which the chart should be retrieved. This parameter can only be used in conjunction with the chart parameter. By default, charts are not restricted to a particular category.

**Type:** string

</details>

## mark_comment_as_spam

Expresses the caller's opinion that one or more comments should be flagged as spam.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies a comma-separated list of IDs of comments that the caller believes should be classified as spam.

**Type:** string

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

## modify_item_in_playlist

Modifies a playlist item. For example, you could update the item's position in the playlist.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. For example, a playlist item can specify a start time and end time, which identify the times portion of the video that should play when users watch the video in the playlist. If your request is updating a playlist item that sets these values, and the request's part parameter value includes the contentDetails part, the playlist item's start and end times will be updated to whatever value the request body specifies. If the request body does not specify values, the existing start and end times will be removed and replaced with the default settings.

**Type:** string

#### $body

A playlistItem resource identifies another resource, such as a video, that is included in a playlist. In addition, the playlistItem  resource contains details about the included resource that pertain specifically to how that resource is used in that playlist.

YouTube uses playlists to identify special collections of videos for a channel, such as:  
- uploaded videos 
- favorite videos 
- positively rated (liked) videos 
- watch history 
- watch later  To be more specific, these lists are associated with a channel, which is a collection of a person, group, or company's videos, playlists, and other YouTube information.

You can retrieve the playlist IDs for each of these lists from the  channel resource  for a given channel. You can then use the   playlistItems.list method to retrieve any of those lists. You can also add or remove items from those lists by calling the   playlistItems.insert and   playlistItems.delete methods. For example, if a user gives a positive rating to a video, you would insert that video into the liked videos playlist for that user's channel.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## modify_playlist

Modifies a playlist. For example, you could change a playlist's title, description, or privacy status.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

Note that this method will override the existing values for mutable properties that are contained in any parts that the request body specifies. For example, a playlist's description is contained in the snippet part, which must be included in the request body. If the request does not specify a value for the snippet.description property, the playlist's existing description will be deleted.

**Type:** string

#### $body

A playlist resource represents a YouTube playlist. A playlist is a collection of videos that can be viewed sequentially and shared with other users. A playlist can contain up to 200 videos, and YouTube does not limit the number of playlists that each user creates. By default, playlists are publicly visible to other users, but playlists can be public or private.

YouTube also uses playlists to identify special collections of videos for a channel, such as:  
- uploaded videos 
- favorite videos 
- positively rated (liked) videos 
- watch history 
- watch later  To be more specific, these lists are associated with a channel, which is a collection of a person, group, or company's videos, playlists, and other YouTube information. You can retrieve the playlist IDs for each of these lists from the  channel resource for a given channel.

You can then use the   playlistItems.list method to retrieve any of those lists. You can also add or remove items from those lists by calling the   playlistItems.insert and   playlistItems.delete methods.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## post_bulletin_to_channel

Posts a bulletin for a specific channel. (The user submitting the request must be authorized to act on the channel's behalf.)

Note: Even though an activity resource can contain information about actions like a user rating a video or marking a video as a favorite, you need to use other API methods to generate those activity resources. For example, you would use the API's videos.rate() method to rate a video and the playlistItems.insert() method to mark a video as a favorite.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

**Type:** string

#### $body

An activity resource contains information about an action that a particular channel, or user, has taken on YouTube.The actions reported in activity feeds include rating a video, sharing a video, marking a video as a favorite, commenting on a video, uploading a video, and so forth. Each activity resource identifies the type of action, the channel associated with the action, and the resource(s) associated with the action, such as the video that was rated or uploaded.

**Type:** object

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

## rate_video

Add a like or dislike rating to a video or remove a rating from a video.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the YouTube video ID of the video that is being rated or having its rating removed.

**Type:** string

#### rating (required)

Specifies the rating to record.

**Type:** string

**Potential values:** dislike, like, none

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

## remove_moderator_from_live_chat

Removes a chat moderator.

<details><summary>Parameters</summary>

#### id (required)

The id parameter identifies the chat moderator to remove. The value uniquely identifies both the moderator and the chat.

**Type:** string

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

## reply_to_comment

Creates a reply to an existing comment. Note: To create a top-level comment, use the commentThreads.insert method.

<details><summary>Parameters</summary>

#### part (required)

The part parameter identifies the properties that the API response will include. Set the parameter value to snippet. The snippet part has a quota cost of 2 units.

**Type:** string

#### $body

A comment represents a single YouTube comment.

**Type:** object

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

## report_abuse_for_video

Report abuse for a video.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## search

Returns a collection of search results that match the query parameters specified in the API request. By default, a search result set identifies matching video, channel, and playlist resources, but you can also configure queries to only retrieve a specific type of resource.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of one or more search resource properties that the API response will include. Set the parameter value to snippet.

**Type:** string

#### channelId

The channelId parameter indicates that the API response should only contain resources created by the channel

**Type:** string

#### channelType

The channelType parameter lets you restrict a search to a particular type of channel.

**Type:** string

**Potential values:** any, show

#### eventType

The eventType parameter restricts a search to broadcast events. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** completed, live, upcoming

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### forContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The forContentOwner parameter restricts the search to only retrieve resources owned by the content owner specified by the onBehalfOfContentOwner parameter. The user must be authenticated using a CMS account linked to the specified content owner and onBehalfOfContentOwner must be provided.

**Type:** boolean

#### forDeveloper

The forDeveloper parameter restricts the search to only retrieve videos uploaded via the developer's application or website. The API server uses the request's authorization credentials to identify the developer. Therefore, a developer can restrict results to videos uploaded through the developer's own app or website but not to videos uploaded through other apps or sites.

**Type:** boolean

#### forMine

The forMine parameter restricts the search to only retrieve videos owned by the authenticated user. If you set this parameter to true, then the type parameter's value must also be set to video.

**Type:** boolean

#### location

The location parameter, in conjunction with the locationRadius parameter, defines a circular geographic area and also restricts a search to videos that specify, in their metadata, a geographic location that falls within that area. The parameter value is a string that specifies latitude/longitude coordinates e.g. (37.42307,-122.08427).


- The location parameter value identifies the point at the center of the area.
- The locationRadius parameter specifies the maximum distance that the location associated with a video can be from that point for the video to still be included in the search results.The API returns an error if your request specifies a value for the location parameter but does not also specify a value for the locationRadius parameter.

**Type:** string

#### locationRadius

The locationRadius parameter, in conjunction with the location parameter, defines a circular geographic area.

The parameter value must be a floating point number followed by a measurement unit. Valid measurement units are m, km, ft, and mi. For example, valid parameter values include 1500m, 5km, 10000ft, and 0.75mi. The API does not support locationRadius parameter values larger than 1000 kilometers.

Note: See the definition of the location parameter for more information.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### order

The order parameter specifies the method that will be used to order resources in the API response.

**Type:** string

**Potential values:** date, rating, relevance, title, videoCount, viewCount

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### publishedAfter

The publishedAfter parameter indicates that the API response should only contain resources created after the specified time. The value is an RFC 3339 formatted date-time value (1970-01-01T00:00:00Z).

**Type:** string

#### publishedBefore

The publishedBefore parameter indicates that the API response should only contain resources created before the specified time. The value is an RFC 3339 formatted date-time value (1970-01-01T00:00:00Z).

**Type:** string

#### q

The q parameter specifies the query term to search for.

Your request can also use the Boolean NOT (-) and OR (|) operators to exclude videos or to find videos that are associated with one of several search terms. For example, to search for videos matching either "boating" or "sailing", set the q parameter value to boating|sailing. Similarly, to search for videos matching either "boating" or "sailing" but not "fishing", set the q parameter value to boating|sailing -fishing. Note that the pipe character must be URL-escaped when it is sent in your API request. The URL-escaped value for the pipe character is %7C.

**Type:** string

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### regionCode

The regionCode parameter instructs the API to return search results for the specified country. The parameter value is an ISO 3166-1 alpha-2 country code.

**Type:** string

#### relatedToVideoId

The relatedToVideoId parameter retrieves a list of videos that are related to the video that the parameter value identifies. The parameter value must be set to a YouTube video ID and, if you are using this parameter, the type parameter must be set to video.

**Type:** string

#### relevanceLanguage

The relevanceLanguage parameter instructs the API to return search results that are most relevant to the specified language. The parameter value is typically an ISO 639-1 two-letter language code. However, you should use the values zh-Hans for simplified Chinese and zh-Hant for traditional Chinese. Please note that results in other languages will still be returned if they are highly relevant to the search query term.

**Type:** string

#### safeSearch

The safeSearch parameter indicates whether the search results should include restricted content as well as standard content.

**Type:** string

**Potential values:** moderate, none, strict

#### topicId

The topicId parameter indicates that the API response should only contain resources associated with the specified topic. The value identifies a Freebase topic ID.

**Type:** string

#### type

The type parameter restricts a search query to only retrieve a particular type of resource. The value is a comma-separated list of resource types.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### videoCaption

The videoCaption parameter indicates whether the API should filter video search results based on whether they have captions. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, closedCaption, none

#### videoCategoryId

The videoCategoryId parameter filters video search results based on their category. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

#### videoDefinition

The videoDefinition parameter lets you restrict a search to only include either high definition (HD) or standard definition (SD) videos. HD videos are available for playback in at least 720p, though higher resolutions, like 1080p, might also be available. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, high, standard

#### videoDimension

The videoDimension parameter lets you restrict a search to only retrieve 2D or 3D videos. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** 2d, 3d, any

#### videoDuration

The videoDuration parameter filters video search results based on their duration. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, long, medium, short

#### videoEmbeddable

The videoEmbeddable parameter lets you to restrict a search to only videos that can be embedded into a webpage. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, true

#### videoLicense

The videoLicense parameter filters search results to only include videos with a particular license. YouTube lets video uploaders choose to attach either the Creative Commons license or the standard YouTube license to each of their videos. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, creativeCommon, youtube

#### videoSyndicated

The videoSyndicated parameter lets you to restrict a search to only videos that can be played outside youtube.com. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, true

#### videoType

The videoType parameter lets you restrict a search to a particular type of videos. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, episode, movie

</details>

## set_live_broadcast_binding

Binds a YouTube broadcast to a stream or removes an existing binding between a broadcast and a stream. A broadcast can only be bound to one video stream, though a video stream may be bound to more than one broadcast.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies the unique ID of the broadcast that is being bound to a video stream.

**Type:** string

#### part (required)

The part parameter specifies a comma-separated list of one or more liveBroadcast resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, contentDetails, and status.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### streamId

The streamId parameter specifies the unique ID of the video stream that is being bound to a broadcast. If this parameter is omitted, the API will remove any existing binding between the broadcast and a video stream.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## set_moderation_status_of_comment

Sets the moderation status of one or more comments. The API request must be authorized by the owner of the channel or video associated with the comments.

<details><summary>Parameters</summary>

#### id (required)

The id parameter specifies a comma-separated list of IDs that identify the comments for which you are updating the moderation status.

**Type:** string

#### moderationStatus (required)

Identifies the new moderation status of the specified comments.

**Type:** string

**Potential values:** heldForReview, published, rejected

#### banAuthor

The banAuthor parameter lets you indicate that you want to automatically reject any additional comments written by the comment's author. Set the parameter value to true to ban the author.

Note: This parameter is only valid if the moderationStatus parameter is also set to rejected.

**Type:** boolean

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

## set_thumbnail

Uploads a custom video thumbnail to YouTube and sets it for a video.

<details><summary>Parameters</summary>

#### videoId (required)

The videoId parameter specifies a YouTube video ID for which the custom video thumbnail is being provided.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## set_watermark



*This operation has no parameters*

## transition_status_of_live_broadcast

Changes the status of a YouTube live broadcast and initiates any processes associated with the new status. For example, when you transition a broadcast's status to testing, YouTube starts to transmit video to that broadcast's monitor stream. Before calling this method, you should confirm that the value of the status.streamStatus property for the stream bound to your broadcast is active.

<details><summary>Parameters</summary>

#### broadcastStatus (required)

The broadcastStatus parameter identifies the state to which the broadcast is changing. Note that to transition a broadcast to either the testing or live state, the status.streamStatus must be active for the stream that the broadcast is bound to.

**Type:** string

**Potential values:** complete, live, testing

#### id (required)

The id parameter specifies the unique ID of the broadcast that is transitioning to another status.

**Type:** string

#### part (required)

The part parameter specifies a comma-separated list of one or more liveBroadcast resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, contentDetails, and status.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## unban_from_live_chat

Removes a chat ban.

<details><summary>Parameters</summary>

#### id (required)

The id parameter identifies the chat ban to remove. The value uniquely identifies both the ban and the chat.

**Type:** string

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

## unset_watermark

Deletes a channel's watermark image.

<details><summary>Parameters</summary>

#### channelId (required)

The channelId parameter specifies the YouTube channel ID for which the watermark is being unset.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## update_caption

Updates a caption track. When updating a caption track, you can change the track's draft status, upload a new caption file for the track, or both.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. Set the property value to snippet if you are updating the track's draft status. Otherwise, set the property value to id.

**Type:** string

#### $body

A caption resource represents a YouTube caption track. A caption track is associated with exactly one YouTube video.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOf

ID of the Google+ Page for the channel that the request is be on behalf of

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### sync

Note: The API server only processes the parameter value if the request contains an updated caption file.

The sync parameter indicates whether YouTube should automatically synchronize the caption file with the audio track of the video. If you set the value to true, YouTube will automatically synchronize the caption track with the audio track.

**Type:** boolean

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_channel

Updates a channel's metadata. Note that this method currently only supports updates to the channel resource's brandingSettings and invideoPromotion objects and their child properties.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The API currently only allows the parameter value to be set to either brandingSettings or invideoPromotion. (You cannot update both of those parts with a single request.)

Note that this method overrides the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies.

**Type:** string

#### $body

A channel resource contains information about a YouTube channel.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

The onBehalfOfContentOwner parameter indicates that the authenticated user is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with needs to be linked to the specified YouTube content owner.

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

## update_channel_section

Update a channelSection.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part names that you can include in the parameter value are snippet and contentDetails.

**Type:** string

#### $body

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## update_comment

Modifies a comment.

<details><summary>Parameters</summary>

#### part (required)

The part parameter identifies the properties that the API response will include. You must at least include the snippet part in the parameter value since that part contains all of the properties that the API request can update.

**Type:** string

#### $body

A comment represents a single YouTube comment.

**Type:** object

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

## update_comment_thread

Modifies the top-level comment in a comment thread.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies a comma-separated list of commentThread resource properties that the API response will include. You must at least include the snippet part in the parameter value since that part contains all of the properties that the API request can update.

**Type:** string

#### $body

A comment thread represents information that applies to a top level comment and all its replies. It can also include the top level comment itself and some of the replies.

**Type:** object

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

## update_live_broadcast

Updates a broadcast. For example, you could modify the broadcast settings defined in the liveBroadcast resource's contentDetails object.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part properties that you can include in the parameter value are id, snippet, contentDetails, and status.

Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. For example, a broadcast's privacy status is defined in the status part. As such, if your request is updating a private or unlisted broadcast, and the request's part parameter value includes the status part, the broadcast's privacy setting will be updated to whatever value the request body specifies. If the request body does not specify a value, the existing privacy setting will be removed and the broadcast will revert to the default privacy setting.

**Type:** string

#### $body

A liveBroadcast resource represents an event that will be streamed, via live video, on YouTube.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## update_live_stream

Updates a video stream. If the properties that you want to change cannot be updated, then you need to create a new stream with the proper settings.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part properties that you can include in the parameter value are id, snippet, cdn, and status.

Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. If the request body does not specify a value for a mutable property, the existing value for that property will be removed.

**Type:** string

#### $body

A live stream describes a live ingestion point.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## update_metadata_for_video

Updates a video's metadata.

<details><summary>Parameters</summary>

#### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. For example, a video's privacy setting is contained in the status part. As such, if your request is updating a private video, and the request's part parameter value includes the status part, the video's privacy setting will be updated to whatever value the request body specifies. If the request body does not specify a value, the existing privacy setting will be removed and the video will revert to the default privacy setting.

In addition, not all parts contain properties that can be set when inserting or updating a video. For example, the statistics object encapsulates statistics that YouTube calculates for a video and does not contain values that you can set or modify. If the parameter value specifies a part that does not contain mutable values, that part will still be included in the API response.

**Type:** string

#### $body

A video resource represents a YouTube video.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## upload_caption

Uploads a caption track.

<details><summary>Parameters</summary>

#### part (required)

The part parameter specifies the caption resource parts that the API response will include. Set the parameter value to snippet.

**Type:** string

#### $body

A caption resource represents a YouTube caption track. A caption track is associated with exactly one YouTube video.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### onBehalfOf

ID of the Google+ Page for the channel that the request is be on behalf of

**Type:** string

#### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### sync

The sync parameter indicates whether YouTube should automatically synchronize the caption file with the audio track of the video. If you set the value to true, YouTube will disregard any time codes that are in the uploaded caption file and generate new time codes for the captions.

You should set the sync parameter to true if you are uploading a transcript, which has no time codes, or if you suspect the time codes in your file are incorrect and want YouTube to try to fix them.

**Type:** boolean

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

