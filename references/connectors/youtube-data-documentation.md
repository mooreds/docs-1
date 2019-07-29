---
id: youtube-data-documentation
title: Youtube Data (version v1.*.*)
sidebar_label: Youtube Data
layout: docs.mustache
---

## add_channel_section

Adds a channelSection for the authenticated user's channel.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part names that you can include in the parameter value are snippet and contentDetails.

**Type:** string

### $body

**Type:** object

```json
{
  "snippet" : {
    "defaultLanguage" : "The language of the channel section's default title and description.",
    "localized" : {
      "title" : "The localized strings for channel section's title."
    },
    "style" : "The style of the channel section.",
    "position" : "The position of the channel section in the channel.",
    "title" : "The channel section's title for multiple_playlists and multiple_channels.",
    "type" : "The type of the channel section.",
    "channelId" : "The ID that YouTube uses to uniquely identify the channel that published the channel section."
  },
  "targeting" : {
    "regions" : [ "string" ],
    "languages" : [ "string" ],
    "countries" : [ "string" ]
  },
  "localizations" : "Localizations for different languages",
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#channelSection\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the channel section.",
  "contentDetails" : {
    "channels" : [ "string" ],
    "playlists" : [ "string" ]
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## add_item_to_playlist

Adds a resource to a playlist.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

**Type:** string

### $body

A playlistItem resource identifies another resource, such as a video, that is included in a playlist. In addition, the playlistItem  resource contains details about the included resource that pertain specifically to how that resource is used in that playlist.

YouTube uses playlists to identify special collections of videos for a channel, such as:  
- uploaded videos 
- favorite videos 
- positively rated (liked) videos 
- watch history 
- watch later  To be more specific, these lists are associated with a channel, which is a collection of a person, group, or company's videos, playlists, and other YouTube information.

You can retrieve the playlist IDs for each of these lists from the  channel resource  for a given channel. You can then use the   playlistItems.list method to retrieve any of those lists. You can also add or remove items from those lists by calling the   playlistItems.insert and   playlistItems.delete methods. For example, if a user gives a positive rating to a video, you would insert that video into the liked videos playlist for that user's channel.

**Type:** object

```json
{
  "snippet" : {
    "playlistId" : "The ID that YouTube uses to uniquely identify the playlist that the playlist item is in.",
    "resourceId" : {
      "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
      "kind" : "The type of the API resource.",
      "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
      "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
    },
    "publishedAt" : "The date and time that the item was added to the playlist. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "description" : "The item's description.",
    "position" : "The order in which the item appears in the playlist. The value uses a zero-based index, so the first item has a position of 0, the second item has a position of 1, and so forth.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The item's title.",
    "channelId" : "The ID that YouTube uses to uniquely identify the user that added the item to the playlist.",
    "channelTitle" : "Channel title for the channel that the playlist item belongs to."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#playlistItem\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the playlist item.",
  "contentDetails" : {
    "note" : "A user-generated note for this item.",
    "videoPublishedAt" : "The date and time that the video was published to YouTube. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "videoId" : "The ID that YouTube uses to uniquely identify a video. To retrieve the video resource, set the id query parameter to this value in your API request.",
    "endAt" : "The time, measured in seconds from the start of the video, when the video should stop playing. (The playlist owner can specify the times when the video should start and stop playing when the video is played in the context of the playlist.) By default, assume that the video.endTime is the end of the video.",
    "startAt" : "The time, measured in seconds from the start of the video, when the video should start playing. (The playlist owner can specify the times when the video should start and stop playing when the video is played in the context of the playlist.) The default value is 0."
  },
  "status" : {
    "privacyStatus" : "This resource's privacy status."
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## add_moderator_to_live_chat

Adds a new moderator for the chat.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response returns. Set the parameter value to snippet.

**Type:** string

### $body

A liveChatModerator resource represents a moderator for a YouTube live chat. A chat moderator has the ability to ban/unban users from a chat, remove message, etc.

**Type:** object

```json
{
  "snippet" : {
    "liveChatId" : "The ID of the live chat this moderator can act on.",
    "moderatorDetails" : {
      "channelUrl" : "The channel's URL.",
      "displayName" : "The channel's display name.",
      "profileImageUrl" : "The channels's avatar URL.",
      "channelId" : "The YouTube channel ID."
    }
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#liveChatModerator\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube assigns to uniquely identify the moderator."
}
```

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

## add_subscription

Adds a subscription for the authenticated user's channel.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

**Type:** string

### $body

A subscription resource contains information about a YouTube user subscription. A subscription notifies a user when new videos are added to a channel or when another user takes one of several actions on YouTube, such as uploading a video, rating a video, or commenting on a video.

**Type:** object

```json
{
  "snippet" : {
    "resourceId" : {
      "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
      "kind" : "The type of the API resource.",
      "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
      "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
    },
    "publishedAt" : "The date and time that the subscription was created. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "description" : "The subscription's details.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The subscription's title.",
    "channelId" : "The ID that YouTube uses to uniquely identify the subscriber's channel.",
    "channelTitle" : "Channel title for the channel that the subscription belongs to."
  },
  "subscriberSnippet" : {
    "description" : "The description of the subscriber.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The title of the subscriber.",
    "channelId" : "The channel ID of the subscriber."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#subscription\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the subscription.",
  "contentDetails" : {
    "newItemCount" : "The number of new items in the subscription since its content was last read.",
    "activityType" : "The type of activity this subscription is for (only uploads, everything).",
    "totalItemCount" : "The approximate number of items that the subscription points to."
  }
}
```

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

## ban_from_live_chat

Adds a new ban to the chat.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response returns. Set the parameter value to snippet.

**Type:** string

### $body

A liveChatBan resource represents a ban for a YouTube live chat.

**Type:** object

```json
{
  "snippet" : {
    "bannedUserDetails" : {
      "channelUrl" : "The channel's URL.",
      "displayName" : "The channel's display name.",
      "profileImageUrl" : "The channels's avatar URL.",
      "channelId" : "The YouTube channel ID."
    },
    "liveChatId" : "The chat this ban is pertinent to.",
    "banDurationSeconds" : "The duration of a ban, only filled if the ban has type TEMPORARY.",
    "type" : "The type of ban."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#liveChatBan\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube assigns to uniquely identify the ban."
}
```

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

## control_slate_settings_for_live_broadcast

Controls the settings for a slate that can be displayed in the broadcast stream.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the YouTube live broadcast ID that uniquely identifies the broadcast in which the slate is being updated.

**Type:** string

### part (required)

The part parameter specifies a comma-separated list of one or more liveBroadcast resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, contentDetails, and status.

**Type:** string

### displaySlate

The displaySlate parameter specifies whether the slate is being enabled or disabled.

**Type:** boolean

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### offsetTimeMs

The offsetTimeMs parameter specifies a positive time offset when the specified slate change will occur. The value is measured in milliseconds from the beginning of the broadcast's monitor stream, which is the time that the testing phase for the broadcast began. Even though it is specified in milliseconds, the value is actually an approximation, and YouTube completes the requested action as closely as possible to that time.

If you do not specify a value for this parameter, then YouTube performs the action as soon as possible. See the Getting started guide for more details.

Important: You should only specify a value for this parameter if your broadcast stream is delayed.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

### walltime

The walltime parameter specifies the wall clock time at which the specified slate change will occur. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sssZ) format.

**Type:** string

</details>

## create_comment_thread

Creates a new top-level comment. To add a reply to an existing comment, use the comments.insert method instead.

<details><summary>Parameters</summary>

### part (required)

The part parameter identifies the properties that the API response will include. Set the parameter value to snippet. The snippet part has a quota cost of 2 units.

**Type:** string

### $body

A comment thread represents information that applies to a top level comment and all its replies. It can also include the top level comment itself and some of the replies.

**Type:** object

```json
{
  "snippet" : {
    "canReply" : "Whether the current viewer of the thread can reply to it. This is viewer specific - other viewers may see a different value for this field.",
    "totalReplyCount" : "The total number of replies (not including the top level comment).",
    "topLevelComment" : {
      "snippet" : {
        "authorProfileImageUrl" : "The URL for the avatar of the user who posted the comment.",
        "textDisplay" : "The comment's text. The format is either plain text or HTML dependent on what has been requested. Even the plain text representation may differ from the text originally posted in that it may replace video links with video titles etc.",
        "publishedAt" : "The date and time when the comment was orignally published. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
        "authorChannelId" : { },
        "moderationStatus" : "The comment's moderation status. Will not be set if the comments were requested through the id filter.",
        "likeCount" : "The total number of likes this comment has received.",
        "videoId" : "The ID of the video the comment refers to, if any.",
        "textOriginal" : "The comment's original raw text as initially posted or last updated. The original text will only be returned if it is accessible to the viewer, which is only guaranteed if the viewer is the comment's author.",
        "authorDisplayName" : "The name of the user who posted the comment.",
        "parentId" : "The unique id of the parent comment, only set for replies.",
        "canRate" : "Whether the current viewer can rate this comment.",
        "authorChannelUrl" : "Link to the author's YouTube channel, if any.",
        "channelId" : "The id of the corresponding YouTube channel. In case of a channel comment this is the channel the comment refers to. In case of a video comment it's the video's channel.",
        "updatedAt" : "The date and time when was last updated . The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
        "viewerRating" : "The rating the viewer has given to this comment. For the time being this will never return RATE_TYPE_DISLIKE and instead return RATE_TYPE_NONE. This may change in the future."
      },
      "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#comment\".",
      "etag" : "Etag of this resource.",
      "id" : "The ID that YouTube uses to uniquely identify the comment."
    },
    "isPublic" : "Whether the thread (and therefore all its comments) is visible to all YouTube users.",
    "videoId" : "The ID of the video the comments refer to, if any. No video_id implies a channel discussion comment.",
    "channelId" : "The YouTube channel the comments in the thread refer to or the channel with the video the comments refer to. If video_id isn't set the comments refer to the channel itself."
  },
  "replies" : {
    "comments" : [ {
      "snippet" : {
        "authorProfileImageUrl" : "The URL for the avatar of the user who posted the comment.",
        "textDisplay" : "The comment's text. The format is either plain text or HTML dependent on what has been requested. Even the plain text representation may differ from the text originally posted in that it may replace video links with video titles etc.",
        "publishedAt" : "The date and time when the comment was orignally published. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
        "authorChannelId" : { },
        "moderationStatus" : "The comment's moderation status. Will not be set if the comments were requested through the id filter.",
        "likeCount" : "The total number of likes this comment has received.",
        "videoId" : "The ID of the video the comment refers to, if any.",
        "textOriginal" : "The comment's original raw text as initially posted or last updated. The original text will only be returned if it is accessible to the viewer, which is only guaranteed if the viewer is the comment's author.",
        "authorDisplayName" : "The name of the user who posted the comment.",
        "parentId" : "The unique id of the parent comment, only set for replies.",
        "canRate" : "Whether the current viewer can rate this comment.",
        "authorChannelUrl" : "Link to the author's YouTube channel, if any.",
        "channelId" : "The id of the corresponding YouTube channel. In case of a channel comment this is the channel the comment refers to. In case of a video comment it's the video's channel.",
        "updatedAt" : "The date and time when was last updated . The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
        "viewerRating" : "The rating the viewer has given to this comment. For the time being this will never return RATE_TYPE_DISLIKE and instead return RATE_TYPE_NONE. This may change in the future."
      },
      "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#comment\".",
      "etag" : "Etag of this resource.",
      "id" : "The ID that YouTube uses to uniquely identify the comment."
    } ]
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#commentThread\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the comment thread."
}
```

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

## create_live_broadcast

Creates a broadcast.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part properties that you can include in the parameter value are id, snippet, contentDetails, and status.

**Type:** string

### $body

A liveBroadcast resource represents an event that will be streamed, via live video, on YouTube.

**Type:** object

```json
{
  "snippet" : {
    "actualStartTime" : "The date and time that the broadcast actually started. This information is only available once the broadcast's state is live. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "isDefaultBroadcast" : "boolean",
    "publishedAt" : "The date and time that the broadcast was added to YouTube's live broadcast schedule. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "liveChatId" : "The id of the live chat for this broadcast.",
    "scheduledStartTime" : "The date and time that the broadcast is scheduled to start. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "scheduledEndTime" : "The date and time that the broadcast is scheduled to end. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "actualEndTime" : "The date and time that the broadcast actually ended. This information is only available once the broadcast's state is complete. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "description" : "The broadcast's description. As with the title, you can set this field by modifying the broadcast resource or by setting the description field of the corresponding video resource.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The broadcast's title. Note that the broadcast represents exactly one YouTube video. You can set this field by modifying the broadcast resource or by setting the title field of the corresponding video resource.",
    "channelId" : "The ID that YouTube uses to uniquely identify the channel that is publishing the broadcast."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#liveBroadcast\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube assigns to uniquely identify the broadcast.",
  "contentDetails" : {
    "monitorStream" : {
      "enableMonitorStream" : "This value determines whether the monitor stream is enabled for the broadcast. If the monitor stream is enabled, then YouTube will broadcast the event content on a special stream intended only for the broadcaster's consumption. The broadcaster can use the stream to review the event content and also to identify the optimal times to insert cuepoints.\n\nYou need to set this value to true if you intend to have a broadcast delay for your event.\n\nNote: This property cannot be updated once the broadcast is in the testing or live state.",
      "embedHtml" : "HTML code that embeds a player that plays the monitor stream.",
      "broadcastStreamDelayMs" : "If you have set the enableMonitorStream property to true, then this property determines the length of the live broadcast delay."
    },
    "recordFromStart" : "Automatically start recording after the event goes live. The default value for this property is true.\n\n\n\nImportant: You must also set the enableDvr property's value to true if you want the playback to be available immediately after the broadcast ends. If you set this property's value to true but do not also set the enableDvr property to true, there may be a delay of around one day before the archived video will be available for playback.",
    "boundStreamId" : "This value uniquely identifies the live stream bound to the broadcast.",
    "enableDvr" : "This setting determines whether viewers can access DVR controls while watching the video. DVR controls enable the viewer to control the video playback experience by pausing, rewinding, or fast forwarding content. The default value for this property is true.\n\n\n\nImportant: You must set the value to true and also set the enableArchive property's value to true if you want to make playback available immediately after the broadcast ends.",
    "enableLowLatency" : "Indicates whether this broadcast has low latency enabled.",
    "stereoLayout" : "string. Possible values: left_right | mono | top_bottom",
    "boundStreamLastUpdateTimeMs" : "The date and time that the live stream referenced by boundStreamId was last updated.",
    "startWithSlate" : "This setting indicates whether the broadcast should automatically begin with an in-stream slate when you update the broadcast's status to live. After updating the status, you then need to send a liveCuepoints.insert request that sets the cuepoint's eventState to end to remove the in-stream slate and make your broadcast stream visible to viewers.",
    "closedCaptionsType" : "string. Possible values: closedCaptionsDisabled | closedCaptionsEmbedded | closedCaptionsHttpPost",
    "enableEmbed" : "This setting indicates whether the broadcast video can be played in an embedded player. If you choose to archive the video (using the enableArchive property), this setting will also apply to the archived video.",
    "enableContentEncryption" : "This setting indicates whether YouTube should enable content encryption for the broadcast.",
    "enableAutoStart" : "This setting indicates whether auto start is enabled for this broadcast.",
    "latencyPreference" : "If both this and enable_low_latency are set, they must match. LATENCY_NORMAL should match enable_low_latency=false LATENCY_LOW should match enable_low_latency=true LATENCY_ULTRA_LOW should have enable_low_latency omitted.",
    "projection" : "The projection format of this broadcast. This defaults to rectangular.",
    "enableClosedCaptions" : "This setting indicates whether HTTP POST closed captioning is enabled for this broadcast. The ingestion URL of the closed captions is returned through the liveStreams API. This is mutually exclusive with using the closed_captions_type property, and is equivalent to setting closed_captions_type to CLOSED_CAPTIONS_HTTP_POST.",
    "mesh" : "byte"
  },
  "statistics" : {
    "totalChatCount" : "The total number of live chat messages currently on the broadcast. The property and its value will be present if the broadcast is public, has the live chat feature enabled, and has at least one message. Note that this field will not be filled after the broadcast ends. So this property would not identify the number of chat messages for an archived video of a completed live broadcast.",
    "concurrentViewers" : "The number of viewers currently watching the broadcast. The property and its value will be present if the broadcast has current viewers and the broadcast owner has not hidden the viewcount for the video. Note that YouTube stops tracking the number of concurrent viewers for a broadcast when the broadcast ends. So, this property would not identify the number of viewers watching an archived video of a live broadcast that already ended."
  },
  "status" : {
    "liveBroadcastPriority" : "Priority of the live broadcast event (internal state).",
    "recordingStatus" : "The broadcast's recording status.",
    "privacyStatus" : "The broadcast's privacy status. Note that the broadcast represents exactly one YouTube video, so the privacy settings are identical to those supported for videos. In addition, you can set this field by modifying the broadcast resource or by setting the privacyStatus field of the corresponding video resource.",
    "lifeCycleStatus" : "The broadcast's status. The status can be updated using the API's liveBroadcasts.transition method."
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## create_live_stream

Creates a video stream. The stream enables you to send your video to YouTube, which can then broadcast the video to your audience.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part properties that you can include in the parameter value are id, snippet, cdn, and status.

**Type:** string

### $body

A live stream describes a live ingestion point.

**Type:** object

```json
{
  "snippet" : {
    "publishedAt" : "The date and time that the stream was created. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "description" : "The stream's description. The value cannot be longer than 10000 characters.",
    "title" : "The stream's title. The value must be between 1 and 128 characters long.",
    "channelId" : "The ID that YouTube uses to uniquely identify the channel that is transmitting the stream.",
    "isDefaultStream" : "boolean"
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#liveStream\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube assigns to uniquely identify the stream.",
  "cdn" : {
    "frameRate" : "The frame rate of the inbound video data.",
    "format" : "The format of the video stream that you are sending to Youtube.",
    "ingestionType" : "The method or protocol used to transmit the video stream.",
    "ingestionInfo" : {
      "ingestionAddress" : "The primary ingestion URL that you should use to stream video to YouTube. You must stream video to this URL.\n\nDepending on which application or tool you use to encode your video stream, you may need to enter the stream URL and stream name separately or you may need to concatenate them in the following format:\n\nSTREAM_URL/STREAM_NAME",
      "backupIngestionAddress" : "The backup ingestion URL that you should use to stream video to YouTube. You have the option of simultaneously streaming the content that you are sending to the ingestionAddress to this URL.",
      "streamName" : "The HTTP or RTMP stream name that YouTube assigns to the video stream."
    },
    "resolution" : "The resolution of the inbound video data."
  },
  "contentDetails" : {
    "closedCaptionsIngestionUrl" : "The ingestion URL where the closed captions of this stream are sent.",
    "isReusable" : "Indicates whether the stream is reusable, which means that it can be bound to multiple broadcasts. It is common for broadcasters to reuse the same stream for many different broadcasts if those broadcasts occur at different times.\n\nIf you set this value to false, then the stream will not be reusable, which means that it can only be bound to one broadcast. Non-reusable streams differ from reusable streams in the following ways:  \n- A non-reusable stream can only be bound to one broadcast. \n- A non-reusable stream might be deleted by an automated process after the broadcast ends. \n- The  liveStreams.list method does not list non-reusable streams if you call the method and set the mine parameter to true. The only way to use that method to retrieve the resource for a non-reusable stream is to use the id parameter to identify the stream."
  },
  "status" : {
    "healthStatus" : {
      "lastUpdateTimeSeconds" : "The last time this status was updated (in seconds)",
      "configurationIssues" : [ {
        "severity" : "How severe this issue is to the stream.",
        "reason" : "The short-form reason for this issue.",
        "description" : "The long-form description of the issue and how to resolve it.",
        "type" : "The kind of error happening."
      } ],
      "status" : "The status code of this stream"
    },
    "streamStatus" : "string. Possible values: active | created | error | inactive | ready"
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## create_message_in_live_chat

Adds a message to a live chat.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes. It identifies the properties that the write operation will set as well as the properties that the API response will include. Set the parameter value to snippet.

**Type:** string

### $body

A liveChatMessage resource represents a chat message in a YouTube Live Chat.

**Type:** object

```json
{
  "snippet" : {
    "publishedAt" : "The date and time when the message was orignally published. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "messageRetractedDetails" : {
      "retractedMessageId" : "string"
    },
    "superStickerDetails" : {
      "amountDisplayString" : "A rendered string that displays the fund amount and currency to the user.",
      "superStickerMetadata" : {
        "altText" : "Internationalized alt text that describes the sticker image and any animation associated with it.",
        "altTextLanguage" : "Specifies the localization language in which the alt text is returned.",
        "stickerId" : "Unique identifier of the Super Sticker. This is a shorter form of the alt_text that includes pack name and a recognizable characteristic of the sticker."
      },
      "tier" : "The tier in which the amount belongs. Lower amounts belong to lower tiers. The lowest tier is 1.",
      "amountMicros" : "The amount purchased by the user, in micros (1,750,000 micros = 1.75).",
      "currency" : "The currency in which the purchase was made."
    },
    "textMessageDetails" : {
      "messageText" : "The user's message."
    },
    "authorChannelId" : "The ID of the user that authored this message, this field is not always filled. textMessageEvent - the user that wrote the message fanFundingEvent - the user that funded the broadcast newSponsorEvent - the user that just became a sponsor messageDeletedEvent - the moderator that took the action messageRetractedEvent - the author that retracted their message userBannedEvent - the moderator that took the action superChatEvent - the user that made the purchase",
    "pollClosedDetails" : {
      "pollId" : "The id of the poll that was closed."
    },
    "type" : "The type of message, this will always be present, it determines the contents of the message as well as which fields will be present.",
    "messageDeletedDetails" : {
      "deletedMessageId" : "string"
    },
    "displayMessage" : "Contains a string that can be displayed to the user. If this field is not present the message is silent, at the moment only messages of type TOMBSTONE and CHAT_ENDED_EVENT are silent.",
    "hasDisplayContent" : "Whether the message has display content that should be displayed to users.",
    "pollOpenedDetails" : {
      "id" : "string",
      "items" : [ {
        "itemId" : "string",
        "description" : "Plain text description of the item."
      } ],
      "prompt" : "string"
    },
    "superChatDetails" : {
      "amountDisplayString" : "A rendered string that displays the fund amount and currency to the user.",
      "userComment" : "The comment added by the user to this Super Chat event.",
      "tier" : "The tier in which the amount belongs. Lower amounts belong to lower tiers. The lowest tier is 1.",
      "amountMicros" : "The amount purchased by the user, in micros (1,750,000 micros = 1.75).",
      "currency" : "The currency in which the purchase was made."
    },
    "liveChatId" : "string",
    "pollVotedDetails" : {
      "itemId" : "The poll item the user chose.",
      "pollId" : "The poll the user voted on."
    },
    "userBannedDetails" : {
      "bannedUserDetails" : {
        "channelUrl" : "The channel's URL.",
        "displayName" : "The channel's display name.",
        "profileImageUrl" : "The channels's avatar URL.",
        "channelId" : "The YouTube channel ID."
      },
      "banType" : "The type of ban.",
      "banDurationSeconds" : "The duration of the ban. This property is only present if the banType is temporary."
    },
    "pollEditedDetails" : {
      "id" : "string",
      "items" : [ {
        "itemId" : "string",
        "description" : "Plain text description of the item."
      } ],
      "prompt" : "string"
    },
    "fanFundingEventDetails" : {
      "amountDisplayString" : "A rendered string that displays the fund amount and currency to the user.",
      "userComment" : "The comment added by the user to this fan funding event.",
      "amountMicros" : "The amount of the fund.",
      "currency" : "The currency in which the fund was made."
    }
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#liveChatMessage\".",
  "authorDetails" : {
    "isVerified" : "Whether the author's identity has been verified by YouTube.",
    "channelUrl" : "The channel's URL.",
    "displayName" : "The channel's display name.",
    "isChatModerator" : "Whether the author is a moderator of the live chat.",
    "profileImageUrl" : "The channels's avatar URL.",
    "channelId" : "The YouTube channel ID.",
    "isChatSponsor" : "Whether the author is a sponsor of the live chat.",
    "isChatOwner" : "Whether the author is the owner of the live chat."
  },
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube assigns to uniquely identify the message."
}
```

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

## create_playlist

Creates a playlist.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

**Type:** string

### $body

A playlist resource represents a YouTube playlist. A playlist is a collection of videos that can be viewed sequentially and shared with other users. A playlist can contain up to 200 videos, and YouTube does not limit the number of playlists that each user creates. By default, playlists are publicly visible to other users, but playlists can be public or private.

YouTube also uses playlists to identify special collections of videos for a channel, such as:  
- uploaded videos 
- favorite videos 
- positively rated (liked) videos 
- watch history 
- watch later  To be more specific, these lists are associated with a channel, which is a collection of a person, group, or company's videos, playlists, and other YouTube information. You can retrieve the playlist IDs for each of these lists from the  channel resource for a given channel.

You can then use the   playlistItems.list method to retrieve any of those lists. You can also add or remove items from those lists by calling the   playlistItems.insert and   playlistItems.delete methods.

**Type:** object

```json
{
  "snippet" : {
    "defaultLanguage" : "The language of the playlist's default title and description.",
    "publishedAt" : "The date and time that the playlist was created. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "localized" : {
      "description" : "The localized strings for playlist's description.",
      "title" : "The localized strings for playlist's title."
    },
    "description" : "The playlist's description.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The playlist's title.",
    "channelId" : "The ID that YouTube uses to uniquely identify the channel that published the playlist.",
    "channelTitle" : "The channel title of the channel that the video belongs to.",
    "tags" : [ "string" ]
  },
  "localizations" : "Localizations for different languages",
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#playlist\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the playlist.",
  "contentDetails" : {
    "itemCount" : "The number of videos in the playlist."
  },
  "player" : {
    "embedHtml" : "An  tag that embeds a player that will play the playlist."
  },
  "status" : {
    "privacyStatus" : "The playlist's privacy status."
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## delete_caption

Deletes a specified caption track.

<details><summary>Parameters</summary>

### id (required)

The id parameter identifies the caption track that is being deleted. The value is a caption track ID as identified by the id property in a caption resource.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOf

ID of the Google+ Page for the channel that the request is be on behalf of

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## delete_channel_section

Deletes a channelSection.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the YouTube channelSection ID for the resource that is being deleted. In a channelSection resource, the id property specifies the YouTube channelSection ID.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## delete_comment

Deletes a comment.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the comment ID for the resource that is being deleted.

**Type:** string

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

## delete_item_from_playlist

Deletes a playlist item.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the YouTube playlist item ID for the playlist item that is being deleted. In a playlistItem resource, the id property specifies the playlist item's ID.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## delete_live_broadcast

Deletes a broadcast.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the YouTube live broadcast ID for the resource that is being deleted.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## delete_live_stream

Deletes a video stream.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the YouTube live stream ID for the resource that is being deleted.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## delete_message_from_live_chat

Deletes a chat message.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the YouTube chat message ID of the resource that is being deleted.

**Type:** string

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

## delete_playlist

Deletes a playlist.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the YouTube playlist ID for the playlist that is being deleted. In a playlist resource, the id property specifies the playlist's ID.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## delete_subscription

Deletes a subscription.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the YouTube subscription ID for the resource that is being deleted. In a subscription resource, the id property specifies the YouTube subscription ID.

**Type:** string

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

## delete_video

Deletes a YouTube video.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the YouTube video ID for the resource that is being deleted. In a video resource, the id property specifies the video's ID.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## download_caption

Downloads a caption track. The caption track is returned in its original format unless the request specifies a value for the tfmt parameter and in its original language unless the request specifies a value for the tlang parameter.

<details><summary>Parameters</summary>

### id (required)

The id parameter identifies the caption track that is being retrieved. The value is a caption track ID as identified by the id property in a caption resource.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOf

ID of the Google+ Page for the channel that the request is be on behalf of

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### tfmt

The tfmt parameter specifies that the caption track should be returned in a specific format. If the parameter is not included in the request, the track is returned in its original format.

**Type:** string

**Potential values:** sbv, scc, srt, ttml, vtt

### tlang

The tlang parameter specifies that the API response should return a translation of the specified caption track. The parameter value is an ISO 639-1 two-letter language code that identifies the desired caption language. The translation is generated by using machine translation, such as Google Translate.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_rating_for_video

Retrieves the ratings that the authorized user gave to a list of specified videos.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies a comma-separated list of the YouTube video ID(s) for the resource(s) for which you are retrieving rating data. In a video resource, the id property specifies the video's ID.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## list_activities_for_channel

Returns a list of channel activity events that match the request criteria. For example, you can retrieve events associated with a particular channel, events associated with the user's subscriptions and Google+ friends, or the YouTube home page feed, which is customized for each user.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more activity resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in an activity resource, the snippet property contains other properties that identify the type of activity, a display title for the activity, and so forth. If you set part=snippet, the API response will also contain all of those nested properties.

**Type:** string

### channelId

The channelId parameter specifies a unique YouTube channel ID. The API will then return a list of that channel's activities.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### home

Set this parameter's value to true to retrieve the activity feed that displays on the YouTube home page for the currently authenticated user.

**Type:** boolean

### mine

Set this parameter's value to true to retrieve a feed of the authenticated user's activities.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### publishedAfter

The publishedAfter parameter specifies the earliest date and time that an activity could have occurred for that activity to be included in the API response. If the parameter value specifies a day, but not a time, then any activities that occurred that day will be included in the result set. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.

**Type:** string

### publishedBefore

The publishedBefore parameter specifies the date and time before which an activity must have occurred for that activity to be included in the API response. If the parameter value specifies a day, but not a time, then any activities that occurred that day will be excluded from the result set. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.

**Type:** string

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### regionCode

The regionCode parameter instructs the API to return results for the specified country. The parameter value is an ISO 3166-1 alpha-2 country code. YouTube uses this value when the authorized user's previous activity on YouTube does not provide enough information to generate the activity feed.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_captions

Returns a list of caption tracks that are associated with a specified video. Note that the API response does not contain the actual captions and that the captions.download method provides the ability to retrieve a caption track.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more caption resource parts that the API response will include. The part names that you can include in the parameter value are id and snippet.

**Type:** string

### videoId (required)

The videoId parameter specifies the YouTube video ID of the video for which the API should return caption tracks.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### id

The id parameter specifies a comma-separated list of IDs that identify the caption resources that should be retrieved. Each ID must identify a caption track associated with the specified video.

**Type:** string

### onBehalfOf

ID of the Google+ Page for the channel that the request is on behalf of.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## list_categories

Returns a list of categories that can be associated with YouTube videos.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies the videoCategory resource properties that the API response will include. Set the parameter value to snippet.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### hl

The hl parameter specifies the language that should be used for text values in the API response.

**Type:** string

### id

The id parameter specifies a comma-separated list of video category IDs for the resources that you are retrieving.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### regionCode

The regionCode parameter instructs the API to return the list of video categories available in the specified country. The parameter value is an ISO 3166-1 alpha-2 country code.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_channel_sections

Returns channelSection resources that match the API request criteria.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more channelSection resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, and contentDetails.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a channelSection resource, the snippet property contains other properties, such as a display title for the channelSection. If you set part=snippet, the API response will also contain all of those nested properties.

**Type:** string

### channelId

The channelId parameter specifies a YouTube channel ID. The API will only return that channel's channelSections.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### hl

The hl parameter indicates that the snippet.localized property values in the returned channelSection resources should be in the specified language if localized values for that language are available. For example, if the API request specifies hl=de, the snippet.localized properties in the API response will contain German titles if German titles are available. Channel owners can provide localized channel section titles using either the channelSections.insert or channelSections.update method.

**Type:** string

### id

The id parameter specifies a comma-separated list of the YouTube channelSection ID(s) for the resource(s) that are being retrieved. In a channelSection resource, the id property specifies the YouTube channelSection ID.

**Type:** string

### mine

Set this parameter's value to true to retrieve a feed of the authenticated user's channelSections.

**Type:** boolean

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## list_channels

Returns a collection of zero or more channel resources that match the request criteria.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more channel resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a channel resource, the contentDetails property contains other properties, such as the uploads properties. As such, if you set part=contentDetails, the API response will also contain all of those nested properties.

**Type:** string

### categoryId

The categoryId parameter specifies a YouTube guide category, thereby requesting YouTube channels associated with that category.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### forUsername

The forUsername parameter specifies a YouTube username, thereby requesting the channel associated with that username.

**Type:** string

### hl

The hl parameter should be used for filter out the properties that are not in the given language. Used for the brandingSettings part.

**Type:** string

### id

The id parameter specifies a comma-separated list of the YouTube channel ID(s) for the resource(s) that are being retrieved. In a channel resource, the id property specifies the channel's YouTube channel ID.

**Type:** string

### managedByMe

Note: This parameter is intended exclusively for YouTube content partners.

Set this parameter's value to true to instruct the API to only return channels managed by the content owner that the onBehalfOfContentOwner parameter specifies. The user must be authenticated as a CMS account linked to the specified content owner and onBehalfOfContentOwner must be provided.

**Type:** boolean

### mine

Set this parameter's value to true to instruct the API to only return channels owned by the authenticated user.

**Type:** boolean

### mySubscribers

Use the subscriptions.list method and its mySubscribers parameter to retrieve a list of subscribers to the authenticated user's channel.

**Type:** boolean

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## list_comment_threads

Returns a list of comment threads that match the API request parameters.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more commentThread resource properties that the API response will include.

**Type:** string

### allThreadsRelatedToChannelId

The allThreadsRelatedToChannelId parameter instructs the API to return all comment threads associated with the specified channel. The response can include comments about the channel or about the channel's videos.

**Type:** string

### channelId

The channelId parameter instructs the API to return comment threads containing comments about the specified channel. (The response will not include comments left on videos that the channel uploaded.)

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### id

The id parameter specifies a comma-separated list of comment thread IDs for the resources that should be retrieved.

**Type:** string

### moderationStatus

Set this parameter to limit the returned comment threads to a particular moderation state.

Note: This parameter is not supported for use in conjunction with the id parameter.

**Type:** string

**Potential values:** heldForReview, likelySpam, published

### order

The order parameter specifies the order in which the API response should list comment threads. Valid values are: 
- time - Comment threads are ordered by time. This is the default behavior.
- relevance - Comment threads are ordered by relevance.Note: This parameter is not supported for use in conjunction with the id parameter.

**Type:** string

**Potential values:** relevance, time

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### searchTerms

The searchTerms parameter instructs the API to limit the API response to only contain comments that contain the specified search terms.

Note: This parameter is not supported for use in conjunction with the id parameter.

**Type:** string

### textFormat

Set this parameter's value to html or plainText to instruct the API to return the comments left by users in html formatted or in plain text.

**Type:** string

**Potential values:** html, plainText

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

### videoId

The videoId parameter instructs the API to return comment threads associated with the specified video ID.

**Type:** string

</details>

## list_comments

Returns a list of comments that match the API request parameters.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more comment resource properties that the API response will include.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### id

The id parameter specifies a comma-separated list of comment IDs for the resources that are being retrieved. In a comment resource, the id property specifies the comment's ID.

**Type:** string

### parentId

The parentId parameter specifies the ID of the comment for which replies should be retrieved.

Note: YouTube currently supports replies only for top-level comments. However, replies to replies may be supported in the future.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### textFormat

This parameter indicates whether the API should return comments formatted as HTML or as plain text.

**Type:** string

**Potential values:** html, plainText

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_content_regions

Returns a list of content regions that the YouTube website supports.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies the i18nRegion resource properties that the API response will include. Set the parameter value to snippet.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### hl

The hl parameter specifies the language that should be used for text values in the API response.

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

## list_guide_categories

Returns a list of categories that can be associated with YouTube channels.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies the guideCategory resource properties that the API response will include. Set the parameter value to snippet.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### hl

The hl parameter specifies the language that will be used for text values in the API response.

**Type:** string

### id

The id parameter specifies a comma-separated list of the YouTube channel category ID(s) for the resource(s) that are being retrieved. In a guideCategory resource, the id property specifies the YouTube channel category ID.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### regionCode

The regionCode parameter instructs the API to return the list of guide categories available in the specified country. The parameter value is an ISO 3166-1 alpha-2 country code.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_items_in_playlist

Returns a collection of playlist items that match the API request parameters. You can retrieve all of the playlist items in a specified playlist or retrieve one or more playlist items by their unique IDs.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more playlistItem resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a playlistItem resource, the snippet property contains numerous fields, including the title, description, position, and resourceId properties. As such, if you set part=snippet, the API response will contain all of those properties.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### id

The id parameter specifies a comma-separated list of one or more unique playlist item IDs.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### playlistId

The playlistId parameter specifies the unique ID of the playlist for which you want to retrieve playlist items. Note that even though this is an optional parameter, every request to retrieve playlist items must specify a value for either the id parameter or the playlistId parameter.

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

### videoId

The videoId parameter specifies that the request should return only the playlist items that contain the specified video.

**Type:** string

</details>

## list_languages

Returns a list of application languages that the YouTube website supports.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies the i18nLanguage resource properties that the API response will include. Set the parameter value to snippet.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### hl

The hl parameter specifies the language that should be used for text values in the API response.

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

## list_live_broadcasts

Returns a list of YouTube broadcasts that match the API request parameters.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more liveBroadcast resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, contentDetails, and status.

**Type:** string

### broadcastStatus

The broadcastStatus parameter filters the API response to only include broadcasts with the specified status.

**Type:** string

**Potential values:** active, all, completed, upcoming

### broadcastType

The broadcastType parameter filters the API response to only include broadcasts with the specified type. This is only compatible with the mine filter for now.

**Type:** string

**Potential values:** all, event, persistent

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### id

The id parameter specifies a comma-separated list of YouTube broadcast IDs that identify the broadcasts being retrieved. In a liveBroadcast resource, the id property specifies the broadcast's ID.

**Type:** string

### mine

The mine parameter can be used to instruct the API to only return broadcasts owned by the authenticated user. Set the parameter value to true to only retrieve your own broadcasts.

**Type:** boolean

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## list_live_streams

Returns a list of video streams that match the API request parameters.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more liveStream resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, cdn, and status.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### id

The id parameter specifies a comma-separated list of YouTube stream IDs that identify the streams being retrieved. In a liveStream resource, the id property specifies the stream's ID.

**Type:** string

### mine

The mine parameter can be used to instruct the API to only return streams owned by the authenticated user. Set the parameter value to true to only retrieve your own streams.

**Type:** boolean

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## list_members_in_channel

Lists sponsors for a channel.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies the sponsor resource parts that the API response will include. Supported values are id and snippet.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### filter

The filter parameter specifies which channel sponsors to return.

**Type:** string

**Potential values:** all, newest

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

## list_messages_in_live_chat

Lists live chat messages for a specific chat.

<details><summary>Parameters</summary>

### liveChatId (required)

The liveChatId parameter specifies the ID of the chat whose messages will be returned.

**Type:** string

### part (required)

The part parameter specifies the liveChatComment resource parts that the API response will include. Supported values are id and snippet.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### hl

The hl parameter instructs the API to retrieve localized resource metadata for a specific application language that the YouTube website supports. The parameter value must be a language code included in the list returned by the i18nLanguages.list method.

If localized resource details are available in that language, the resource's snippet.localized object will contain the localized values. However, if localized details are not available, the snippet.localized object will contain resource details in the resource's default language.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### profileImageSize

The profileImageSize parameter specifies the size of the user profile pictures that should be returned in the result set. Default: 88.

**Type:** integer

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_moderators_for_live_chat

Lists moderators for a live chat.

<details><summary>Parameters</summary>

### liveChatId (required)

The liveChatId parameter specifies the YouTube live chat for which the API should return moderators.

**Type:** string

### part (required)

The part parameter specifies the liveChatModerator resource parts that the API response will include. Supported values are id and snippet.

**Type:** string

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

## list_playlists

Returns a collection of playlists that match the API request parameters. For example, you can retrieve all playlists that the authenticated user owns, or you can retrieve one or more playlists by their unique IDs.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a playlist resource, the snippet property contains properties like author, title, description, tags, and timeCreated. As such, if you set part=snippet, the API response will contain all of those properties.

**Type:** string

### channelId

This value indicates that the API should only return the specified channel's playlists.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### hl

The hl parameter should be used for filter out the properties that are not in the given language. Used for the snippet part.

**Type:** string

### id

The id parameter specifies a comma-separated list of the YouTube playlist ID(s) for the resource(s) that are being retrieved. In a playlist resource, the id property specifies the playlist's YouTube playlist ID.

**Type:** string

### mine

Set this parameter's value to true to instruct the API to only return playlists owned by the authenticated user.

**Type:** boolean

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## list_reasons_for_reporting_abuse

Returns a list of abuse reasons that can be used for reporting abusive videos.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies the videoCategory resource parts that the API response will include. Supported values are id and snippet.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### hl

The hl parameter specifies the language that should be used for text values in the API response.

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

## list_subscriptions

Returns subscription resources that match the API request criteria.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more subscription resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a subscription resource, the snippet property contains other properties, such as a display title for the subscription. If you set part=snippet, the API response will also contain all of those nested properties.

**Type:** string

### channelId

The channelId parameter specifies a YouTube channel ID. The API will only return that channel's subscriptions.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### forChannelId

The forChannelId parameter specifies a comma-separated list of channel IDs. The API response will then only contain subscriptions matching those channels.

**Type:** string

### id

The id parameter specifies a comma-separated list of the YouTube subscription ID(s) for the resource(s) that are being retrieved. In a subscription resource, the id property specifies the YouTube subscription ID.

**Type:** string

### mine

Set this parameter's value to true to retrieve a feed of the authenticated user's subscriptions.

**Type:** boolean

### myRecentSubscribers

Set this parameter's value to true to retrieve a feed of the subscribers of the authenticated user in reverse chronological order (newest first).

**Type:** boolean

### mySubscribers

Set this parameter's value to true to retrieve a feed of the subscribers of the authenticated user in no particular order.

**Type:** boolean

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

**Type:** string

### order

The order parameter specifies the method that will be used to sort resources in the API response.

**Type:** string

**Potential values:** alphabetical, relevance, unread

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

## list_super_chat_events

Lists Super Chat events for a channel.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies the superChatEvent resource parts that the API response will include. Supported values are id and snippet.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### hl

The hl parameter instructs the API to retrieve localized resource metadata for a specific application language that the YouTube website supports. The parameter value must be a language code included in the list returned by the i18nLanguages.list method.

If localized resource details are available in that language, the resource's snippet.localized object will contain the localized values. However, if localized details are not available, the snippet.localized object will contain resource details in the resource's default language.

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

## list_videos

Returns a list of videos that match the API request parameters.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more video resource properties that the API response will include.

If the parameter identifies a property that contains child properties, the child properties will be included in the response. For example, in a video resource, the snippet property contains the channelId, title, description, tags, and categoryId properties. As such, if you set part=snippet, the API response will contain all of those properties.

**Type:** string

### chart

The chart parameter identifies the chart that you want to retrieve.

**Type:** string

**Potential values:** mostPopular

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### hl

The hl parameter instructs the API to retrieve localized resource metadata for a specific application language that the YouTube website supports. The parameter value must be a language code included in the list returned by the i18nLanguages.list method.

If localized resource details are available in that language, the resource's snippet.localized object will contain the localized values. However, if localized details are not available, the snippet.localized object will contain resource details in the resource's default language.

**Type:** string

### id

The id parameter specifies a comma-separated list of the YouTube video ID(s) for the resource(s) that are being retrieved. In a video resource, the id property specifies the video's ID.

**Type:** string

### locale

DEPRECATED

**Type:** string

### maxHeight

The maxHeight parameter specifies a maximum height of the embedded player. If maxWidth is provided, maxHeight may not be reached in order to not violate the width request.

**Type:** integer

### maxWidth

The maxWidth parameter specifies a maximum width of the embedded player. If maxHeight is provided, maxWidth may not be reached in order to not violate the height request.

**Type:** integer

### myRating

Set this parameter's value to like or dislike to instruct the API to only return videos liked or disliked by the authenticated user.

**Type:** string

**Potential values:** dislike, like

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### regionCode

The regionCode parameter instructs the API to select a video chart available in the specified region. This parameter can only be used in conjunction with the chart parameter. The parameter value is an ISO 3166-1 alpha-2 country code.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

### videoCategoryId

The videoCategoryId parameter identifies the video category for which the chart should be retrieved. This parameter can only be used in conjunction with the chart parameter. By default, charts are not restricted to a particular category.

**Type:** string

</details>

## mark_comment_as_spam

Expresses the caller's opinion that one or more comments should be flagged as spam.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies a comma-separated list of IDs of comments that the caller believes should be classified as spam.

**Type:** string

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

## modify_item_in_playlist

Modifies a playlist item. For example, you could update the item's position in the playlist.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. For example, a playlist item can specify a start time and end time, which identify the times portion of the video that should play when users watch the video in the playlist. If your request is updating a playlist item that sets these values, and the request's part parameter value includes the contentDetails part, the playlist item's start and end times will be updated to whatever value the request body specifies. If the request body does not specify values, the existing start and end times will be removed and replaced with the default settings.

**Type:** string

### $body

A playlistItem resource identifies another resource, such as a video, that is included in a playlist. In addition, the playlistItem  resource contains details about the included resource that pertain specifically to how that resource is used in that playlist.

YouTube uses playlists to identify special collections of videos for a channel, such as:  
- uploaded videos 
- favorite videos 
- positively rated (liked) videos 
- watch history 
- watch later  To be more specific, these lists are associated with a channel, which is a collection of a person, group, or company's videos, playlists, and other YouTube information.

You can retrieve the playlist IDs for each of these lists from the  channel resource  for a given channel. You can then use the   playlistItems.list method to retrieve any of those lists. You can also add or remove items from those lists by calling the   playlistItems.insert and   playlistItems.delete methods. For example, if a user gives a positive rating to a video, you would insert that video into the liked videos playlist for that user's channel.

**Type:** object

```json
{
  "snippet" : {
    "playlistId" : "The ID that YouTube uses to uniquely identify the playlist that the playlist item is in.",
    "resourceId" : {
      "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
      "kind" : "The type of the API resource.",
      "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
      "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
    },
    "publishedAt" : "The date and time that the item was added to the playlist. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "description" : "The item's description.",
    "position" : "The order in which the item appears in the playlist. The value uses a zero-based index, so the first item has a position of 0, the second item has a position of 1, and so forth.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The item's title.",
    "channelId" : "The ID that YouTube uses to uniquely identify the user that added the item to the playlist.",
    "channelTitle" : "Channel title for the channel that the playlist item belongs to."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#playlistItem\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the playlist item.",
  "contentDetails" : {
    "note" : "A user-generated note for this item.",
    "videoPublishedAt" : "The date and time that the video was published to YouTube. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "videoId" : "The ID that YouTube uses to uniquely identify a video. To retrieve the video resource, set the id query parameter to this value in your API request.",
    "endAt" : "The time, measured in seconds from the start of the video, when the video should stop playing. (The playlist owner can specify the times when the video should start and stop playing when the video is played in the context of the playlist.) By default, assume that the video.endTime is the end of the video.",
    "startAt" : "The time, measured in seconds from the start of the video, when the video should start playing. (The playlist owner can specify the times when the video should start and stop playing when the video is played in the context of the playlist.) The default value is 0."
  },
  "status" : {
    "privacyStatus" : "This resource's privacy status."
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## modify_playlist

Modifies a playlist. For example, you could change a playlist's title, description, or privacy status.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

Note that this method will override the existing values for mutable properties that are contained in any parts that the request body specifies. For example, a playlist's description is contained in the snippet part, which must be included in the request body. If the request does not specify a value for the snippet.description property, the playlist's existing description will be deleted.

**Type:** string

### $body

A playlist resource represents a YouTube playlist. A playlist is a collection of videos that can be viewed sequentially and shared with other users. A playlist can contain up to 200 videos, and YouTube does not limit the number of playlists that each user creates. By default, playlists are publicly visible to other users, but playlists can be public or private.

YouTube also uses playlists to identify special collections of videos for a channel, such as:  
- uploaded videos 
- favorite videos 
- positively rated (liked) videos 
- watch history 
- watch later  To be more specific, these lists are associated with a channel, which is a collection of a person, group, or company's videos, playlists, and other YouTube information. You can retrieve the playlist IDs for each of these lists from the  channel resource for a given channel.

You can then use the   playlistItems.list method to retrieve any of those lists. You can also add or remove items from those lists by calling the   playlistItems.insert and   playlistItems.delete methods.

**Type:** object

```json
{
  "snippet" : {
    "defaultLanguage" : "The language of the playlist's default title and description.",
    "publishedAt" : "The date and time that the playlist was created. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "localized" : {
      "description" : "The localized strings for playlist's description.",
      "title" : "The localized strings for playlist's title."
    },
    "description" : "The playlist's description.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The playlist's title.",
    "channelId" : "The ID that YouTube uses to uniquely identify the channel that published the playlist.",
    "channelTitle" : "The channel title of the channel that the video belongs to.",
    "tags" : [ "string" ]
  },
  "localizations" : "Localizations for different languages",
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#playlist\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the playlist.",
  "contentDetails" : {
    "itemCount" : "The number of videos in the playlist."
  },
  "player" : {
    "embedHtml" : "An  tag that embeds a player that will play the playlist."
  },
  "status" : {
    "privacyStatus" : "The playlist's privacy status."
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## post_bulletin_to_channel

Posts a bulletin for a specific channel. (The user submitting the request must be authorized to act on the channel's behalf.)

Note: Even though an activity resource can contain information about actions like a user rating a video or marking a video as a favorite, you need to use other API methods to generate those activity resources. For example, you would use the API's videos.rate() method to rate a video and the playlistItems.insert() method to mark a video as a favorite.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

**Type:** string

### $body

An activity resource contains information about an action that a particular channel, or user, has taken on YouTube.The actions reported in activity feeds include rating a video, sharing a video, marking a video as a favorite, commenting on a video, uploading a video, and so forth. Each activity resource identifies the type of action, the channel associated with the action, and the resource(s) associated with the action, such as the video that was rated or uploaded.

**Type:** object

```json
{
  "snippet" : {
    "publishedAt" : "The date and time that the video was uploaded. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "groupId" : "The group ID associated with the activity. A group ID identifies user events that are associated with the same user and resource. For example, if a user rates a video and marks the same video as a favorite, the entries for those events would have the same group ID in the user's activity feed. In your user interface, you can avoid repetition by grouping events with the same groupId value.",
    "description" : "The description of the resource primarily associated with the activity.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The title of the resource primarily associated with the activity.",
    "type" : "The type of activity that the resource describes.",
    "channelId" : "The ID that YouTube uses to uniquely identify the channel associated with the activity.",
    "channelTitle" : "Channel title for the channel responsible for this activity"
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#activity\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the activity.",
  "contentDetails" : {
    "channelItem" : {
      "resourceId" : {
        "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
        "kind" : "The type of the API resource.",
        "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
        "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
      }
    },
    "like" : {
      "resourceId" : {
        "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
        "kind" : "The type of the API resource.",
        "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
        "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
      }
    },
    "playlistItem" : {
      "playlistId" : "The value that YouTube uses to uniquely identify the playlist.",
      "playlistItemId" : "ID of the item within the playlist.",
      "resourceId" : {
        "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
        "kind" : "The type of the API resource.",
        "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
        "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
      }
    },
    "social" : {
      "resourceId" : {
        "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
        "kind" : "The type of the API resource.",
        "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
        "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
      },
      "author" : "The author of the social network post.",
      "imageUrl" : "An image of the post's author.",
      "type" : "The name of the social network.",
      "referenceUrl" : "The URL of the social network post."
    },
    "upload" : {
      "videoId" : "The ID that YouTube uses to uniquely identify the uploaded video."
    },
    "promotedItem" : {
      "adTag" : "The URL the client should fetch to request a promoted item.",
      "ctaType" : "The type of call-to-action, a message to the user indicating action that can be taken.",
      "clickTrackingUrl" : "The URL the client should ping to indicate that the user clicked through on this promoted item.",
      "customCtaButtonText" : "The custom call-to-action button text. If specified, it will override the default button text for the cta_type.",
      "impressionUrl" : [ "string" ],
      "forecastingUrl" : [ "string" ],
      "creativeViewUrl" : "The URL the client should ping to indicate that the user was shown this promoted item.",
      "videoId" : "The ID that YouTube uses to uniquely identify the promoted video.",
      "descriptionText" : "The text description to accompany the promoted item.",
      "destinationUrl" : "The URL the client should direct the user to, if the user chooses to visit the advertiser's website."
    },
    "recommendation" : {
      "reason" : "The reason that the resource is recommended to the user.",
      "resourceId" : {
        "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
        "kind" : "The type of the API resource.",
        "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
        "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
      },
      "seedResourceId" : {
        "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
        "kind" : "The type of the API resource.",
        "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
        "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
      }
    },
    "comment" : {
      "resourceId" : {
        "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
        "kind" : "The type of the API resource.",
        "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
        "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
      }
    },
    "subscription" : {
      "resourceId" : {
        "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
        "kind" : "The type of the API resource.",
        "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
        "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
      }
    },
    "favorite" : {
      "resourceId" : {
        "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
        "kind" : "The type of the API resource.",
        "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
        "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
      }
    },
    "bulletin" : {
      "resourceId" : {
        "playlistId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a playlist. This property is only present if the resourceId.kind value is youtube#playlist.",
        "kind" : "The type of the API resource.",
        "videoId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a video. This property is only present if the resourceId.kind value is youtube#video.",
        "channelId" : "The ID that YouTube uses to uniquely identify the referred resource, if that resource is a channel. This property is only present if the resourceId.kind value is youtube#channel."
      }
    }
  }
}
```

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

## rate_video

Add a like or dislike rating to a video or remove a rating from a video.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the YouTube video ID of the video that is being rated or having its rating removed.

**Type:** string

### rating (required)

Specifies the rating to record.

**Type:** string

**Potential values:** dislike, like, none

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

## remove_moderator_from_live_chat

Removes a chat moderator.

<details><summary>Parameters</summary>

### id (required)

The id parameter identifies the chat moderator to remove. The value uniquely identifies both the moderator and the chat.

**Type:** string

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

## reply_to_comment

Creates a reply to an existing comment. Note: To create a top-level comment, use the commentThreads.insert method.

<details><summary>Parameters</summary>

### part (required)

The part parameter identifies the properties that the API response will include. Set the parameter value to snippet. The snippet part has a quota cost of 2 units.

**Type:** string

### $body

A comment represents a single YouTube comment.

**Type:** object

```json
{
  "snippet" : {
    "authorProfileImageUrl" : "The URL for the avatar of the user who posted the comment.",
    "textDisplay" : "The comment's text. The format is either plain text or HTML dependent on what has been requested. Even the plain text representation may differ from the text originally posted in that it may replace video links with video titles etc.",
    "publishedAt" : "The date and time when the comment was orignally published. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "authorChannelId" : { },
    "moderationStatus" : "The comment's moderation status. Will not be set if the comments were requested through the id filter.",
    "likeCount" : "The total number of likes this comment has received.",
    "videoId" : "The ID of the video the comment refers to, if any.",
    "textOriginal" : "The comment's original raw text as initially posted or last updated. The original text will only be returned if it is accessible to the viewer, which is only guaranteed if the viewer is the comment's author.",
    "authorDisplayName" : "The name of the user who posted the comment.",
    "parentId" : "The unique id of the parent comment, only set for replies.",
    "canRate" : "Whether the current viewer can rate this comment.",
    "authorChannelUrl" : "Link to the author's YouTube channel, if any.",
    "channelId" : "The id of the corresponding YouTube channel. In case of a channel comment this is the channel the comment refers to. In case of a video comment it's the video's channel.",
    "updatedAt" : "The date and time when was last updated . The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "viewerRating" : "The rating the viewer has given to this comment. For the time being this will never return RATE_TYPE_DISLIKE and instead return RATE_TYPE_NONE. This may change in the future."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#comment\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the comment."
}
```

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

## report_abuse_for_video

Report abuse for a video.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "comments" : "Additional comments regarding the abuse report.",
  "reasonId" : "The high-level, or primary, reason that the content is abusive. The value is an abuse report reason ID.",
  "secondaryReasonId" : "The specific, or secondary, reason that this content is abusive (if available). The value is an abuse report reason ID that is a valid secondary reason for the primary reason.",
  "language" : "The language that the content was viewed in.",
  "videoId" : "The ID that YouTube uses to uniquely identify the video."
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## search

Returns a collection of search results that match the query parameters specified in the API request. By default, a search result set identifies matching video, channel, and playlist resources, but you can also configure queries to only retrieve a specific type of resource.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of one or more search resource properties that the API response will include. Set the parameter value to snippet.

**Type:** string

### channelId

The channelId parameter indicates that the API response should only contain resources created by the channel

**Type:** string

### channelType

The channelType parameter lets you restrict a search to a particular type of channel.

**Type:** string

**Potential values:** any, show

### eventType

The eventType parameter restricts a search to broadcast events. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** completed, live, upcoming

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### forContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The forContentOwner parameter restricts the search to only retrieve resources owned by the content owner specified by the onBehalfOfContentOwner parameter. The user must be authenticated using a CMS account linked to the specified content owner and onBehalfOfContentOwner must be provided.

**Type:** boolean

### forDeveloper

The forDeveloper parameter restricts the search to only retrieve videos uploaded via the developer's application or website. The API server uses the request's authorization credentials to identify the developer. Therefore, a developer can restrict results to videos uploaded through the developer's own app or website but not to videos uploaded through other apps or sites.

**Type:** boolean

### forMine

The forMine parameter restricts the search to only retrieve videos owned by the authenticated user. If you set this parameter to true, then the type parameter's value must also be set to video.

**Type:** boolean

### location

The location parameter, in conjunction with the locationRadius parameter, defines a circular geographic area and also restricts a search to videos that specify, in their metadata, a geographic location that falls within that area. The parameter value is a string that specifies latitude/longitude coordinates e.g. (37.42307,-122.08427).


- The location parameter value identifies the point at the center of the area.
- The locationRadius parameter specifies the maximum distance that the location associated with a video can be from that point for the video to still be included in the search results.The API returns an error if your request specifies a value for the location parameter but does not also specify a value for the locationRadius parameter.

**Type:** string

### locationRadius

The locationRadius parameter, in conjunction with the location parameter, defines a circular geographic area.

The parameter value must be a floating point number followed by a measurement unit. Valid measurement units are m, km, ft, and mi. For example, valid parameter values include 1500m, 5km, 10000ft, and 0.75mi. The API does not support locationRadius parameter values larger than 1000 kilometers.

Note: See the definition of the location parameter for more information.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### order

The order parameter specifies the method that will be used to order resources in the API response.

**Type:** string

**Potential values:** date, rating, relevance, title, videoCount, viewCount

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### publishedAfter

The publishedAfter parameter indicates that the API response should only contain resources created after the specified time. The value is an RFC 3339 formatted date-time value (1970-01-01T00:00:00Z).

**Type:** string

### publishedBefore

The publishedBefore parameter indicates that the API response should only contain resources created before the specified time. The value is an RFC 3339 formatted date-time value (1970-01-01T00:00:00Z).

**Type:** string

### q

The q parameter specifies the query term to search for.

Your request can also use the Boolean NOT (-) and OR (|) operators to exclude videos or to find videos that are associated with one of several search terms. For example, to search for videos matching either "boating" or "sailing", set the q parameter value to boating|sailing. Similarly, to search for videos matching either "boating" or "sailing" but not "fishing", set the q parameter value to boating|sailing -fishing. Note that the pipe character must be URL-escaped when it is sent in your API request. The URL-escaped value for the pipe character is %7C.

**Type:** string

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### regionCode

The regionCode parameter instructs the API to return search results for the specified country. The parameter value is an ISO 3166-1 alpha-2 country code.

**Type:** string

### relatedToVideoId

The relatedToVideoId parameter retrieves a list of videos that are related to the video that the parameter value identifies. The parameter value must be set to a YouTube video ID and, if you are using this parameter, the type parameter must be set to video.

**Type:** string

### relevanceLanguage

The relevanceLanguage parameter instructs the API to return search results that are most relevant to the specified language. The parameter value is typically an ISO 639-1 two-letter language code. However, you should use the values zh-Hans for simplified Chinese and zh-Hant for traditional Chinese. Please note that results in other languages will still be returned if they are highly relevant to the search query term.

**Type:** string

### safeSearch

The safeSearch parameter indicates whether the search results should include restricted content as well as standard content.

**Type:** string

**Potential values:** moderate, none, strict

### topicId

The topicId parameter indicates that the API response should only contain resources associated with the specified topic. The value identifies a Freebase topic ID.

**Type:** string

### type

The type parameter restricts a search query to only retrieve a particular type of resource. The value is a comma-separated list of resource types.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

### videoCaption

The videoCaption parameter indicates whether the API should filter video search results based on whether they have captions. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, closedCaption, none

### videoCategoryId

The videoCategoryId parameter filters video search results based on their category. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

### videoDefinition

The videoDefinition parameter lets you restrict a search to only include either high definition (HD) or standard definition (SD) videos. HD videos are available for playback in at least 720p, though higher resolutions, like 1080p, might also be available. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, high, standard

### videoDimension

The videoDimension parameter lets you restrict a search to only retrieve 2D or 3D videos. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** 2d, 3d, any

### videoDuration

The videoDuration parameter filters video search results based on their duration. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, long, medium, short

### videoEmbeddable

The videoEmbeddable parameter lets you to restrict a search to only videos that can be embedded into a webpage. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, true

### videoLicense

The videoLicense parameter filters search results to only include videos with a particular license. YouTube lets video uploaders choose to attach either the Creative Commons license or the standard YouTube license to each of their videos. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, creativeCommon, youtube

### videoSyndicated

The videoSyndicated parameter lets you to restrict a search to only videos that can be played outside youtube.com. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, true

### videoType

The videoType parameter lets you restrict a search to a particular type of videos. If you specify a value for this parameter, you must also set the type parameter's value to video.

**Type:** string

**Potential values:** any, episode, movie

</details>

## set_live_broadcast_binding

Binds a YouTube broadcast to a stream or removes an existing binding between a broadcast and a stream. A broadcast can only be bound to one video stream, though a video stream may be bound to more than one broadcast.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies the unique ID of the broadcast that is being bound to a video stream.

**Type:** string

### part (required)

The part parameter specifies a comma-separated list of one or more liveBroadcast resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, contentDetails, and status.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### streamId

The streamId parameter specifies the unique ID of the video stream that is being bound to a broadcast. If this parameter is omitted, the API will remove any existing binding between the broadcast and a video stream.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## set_moderation_status_of_comment

Sets the moderation status of one or more comments. The API request must be authorized by the owner of the channel or video associated with the comments.

<details><summary>Parameters</summary>

### id (required)

The id parameter specifies a comma-separated list of IDs that identify the comments for which you are updating the moderation status.

**Type:** string

### moderationStatus (required)

Identifies the new moderation status of the specified comments.

**Type:** string

**Potential values:** heldForReview, published, rejected

### banAuthor

The banAuthor parameter lets you indicate that you want to automatically reject any additional comments written by the comment's author. Set the parameter value to true to ban the author.

Note: This parameter is only valid if the moderationStatus parameter is also set to rejected.

**Type:** boolean

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

## set_thumbnail

Uploads a custom video thumbnail to YouTube and sets it for a video.

<details><summary>Parameters</summary>

### videoId (required)

The videoId parameter specifies a YouTube video ID for which the custom video thumbnail is being provided.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## set_watermark



*This operation has no parameters*

## transition_status_of_live_broadcast

Changes the status of a YouTube live broadcast and initiates any processes associated with the new status. For example, when you transition a broadcast's status to testing, YouTube starts to transmit video to that broadcast's monitor stream. Before calling this method, you should confirm that the value of the status.streamStatus property for the stream bound to your broadcast is active.

<details><summary>Parameters</summary>

### broadcastStatus (required)

The broadcastStatus parameter identifies the state to which the broadcast is changing. Note that to transition a broadcast to either the testing or live state, the status.streamStatus must be active for the stream that the broadcast is bound to.

**Type:** string

**Potential values:** complete, live, testing

### id (required)

The id parameter specifies the unique ID of the broadcast that is transitioning to another status.

**Type:** string

### part (required)

The part parameter specifies a comma-separated list of one or more liveBroadcast resource properties that the API response will include. The part names that you can include in the parameter value are id, snippet, contentDetails, and status.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## unban_from_live_chat

Removes a chat ban.

<details><summary>Parameters</summary>

### id (required)

The id parameter identifies the chat ban to remove. The value uniquely identifies both the ban and the chat.

**Type:** string

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

## unset_watermark

Deletes a channel's watermark image.

<details><summary>Parameters</summary>

### channelId (required)

The channelId parameter specifies the YouTube channel ID for which the watermark is being unset.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## update_caption

Updates a caption track. When updating a caption track, you can change the track's draft status, upload a new caption file for the track, or both.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include. Set the property value to snippet if you are updating the track's draft status. Otherwise, set the property value to id.

**Type:** string

### $body

A caption resource represents a YouTube caption track. A caption track is associated with exactly one YouTube video.

**Type:** object

```json
{
  "snippet" : {
    "trackKind" : "The caption track's type.",
    "audioTrackType" : "The type of audio track associated with the caption track.",
    "isDraft" : "Indicates whether the caption track is a draft. If the value is true, then the track is not publicly visible. The default value is false.",
    "language" : "The language of the caption track. The property value is a BCP-47 language tag.",
    "videoId" : "The ID that YouTube uses to uniquely identify the video associated with the caption track.",
    "lastUpdated" : "The date and time when the caption track was last updated. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "isAutoSynced" : "Indicates whether YouTube synchronized the caption track to the audio track in the video. The value will be true if a sync was explicitly requested when the caption track was uploaded. For example, when calling the captions.insert or captions.update methods, you can set the sync parameter to true to instruct YouTube to sync the uploaded track to the video. If the value is false, YouTube uses the time codes in the uploaded caption track to determine when to display captions.",
    "failureReason" : "The reason that YouTube failed to process the caption track. This property is only present if the state property's value is failed.",
    "name" : "The name of the caption track. The name is intended to be visible to the user as an option during playback.",
    "isEasyReader" : "Indicates whether caption track is formatted for \"easy reader,\" meaning it is at a third-grade level for language learners. The default value is false.",
    "isLarge" : "Indicates whether the caption track uses large text for the vision-impaired. The default value is false.",
    "isCC" : "Indicates whether the track contains closed captions for the deaf and hard of hearing. The default value is false.",
    "status" : "The caption track's status."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#caption\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the caption track."
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOf

ID of the Google+ Page for the channel that the request is be on behalf of

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sync

Note: The API server only processes the parameter value if the request contains an updated caption file.

The sync parameter indicates whether YouTube should automatically synchronize the caption file with the audio track of the video. If you set the value to true, YouTube will automatically synchronize the caption track with the audio track.

**Type:** boolean

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_channel

Updates a channel's metadata. Note that this method currently only supports updates to the channel resource's brandingSettings and invideoPromotion objects and their child properties.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The API currently only allows the parameter value to be set to either brandingSettings or invideoPromotion. (You cannot update both of those parts with a single request.)

Note that this method overrides the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies.

**Type:** string

### $body

A channel resource contains information about a YouTube channel.

**Type:** object

```json
{
  "snippet" : {
    "customUrl" : "The custom url of the channel.",
    "country" : "The country of the channel.",
    "defaultLanguage" : "The language of the channel's default title and description.",
    "publishedAt" : "The date and time that the channel was created. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "localized" : {
      "description" : "The localized strings for channel's description.",
      "title" : "The localized strings for channel's title."
    },
    "description" : "The description of the channel.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The channel's title."
  },
  "localizations" : "Localizations for different languages",
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#channel\".",
  "contentDetails" : {
    "relatedPlaylists" : {
      "favorites" : "The ID of the playlist that contains the channel\"s favorite videos. Use the playlistItems.insert and playlistItems.delete to add or remove items from that list.",
      "watchHistory" : "The ID of the playlist that contains the channel\"s watch history. Use the playlistItems.insert and playlistItems.delete to add or remove items from that list.",
      "watchLater" : "The ID of the playlist that contains the channel\"s watch later playlist. Use the playlistItems.insert and playlistItems.delete to add or remove items from that list.",
      "likes" : "The ID of the playlist that contains the channel\"s liked videos. Use the playlistItems.insert and playlistItems.delete to add or remove items from that list.",
      "uploads" : "The ID of the playlist that contains the channel\"s uploaded videos. Use the videos.insert method to upload new videos and the videos.delete method to delete previously uploaded videos."
    }
  },
  "topicDetails" : {
    "topicIds" : [ "string" ],
    "topicCategories" : [ "string" ]
  },
  "brandingSettings" : {
    "image" : {
      "bannerTabletExtraHdImageUrl" : "Banner image. Tablet size extra high resolution (2560x424).",
      "bannerTvImageUrl" : "Banner image. TV size extra high resolution (2120x1192).",
      "watchIconImageUrl" : "The URL for the image that appears above the top-left corner of the video player. This is a 25-pixel-high image with a flexible width that cannot exceed 170 pixels.",
      "bannerExternalUrl" : "This is used only in update requests; if it's set, we use this URL to generate all of the above banner URLs.",
      "smallBrandedBannerImageUrl" : {
        "default" : "string",
        "defaultLanguage" : {
          "value" : "string"
        },
        "localized" : [ {
          "language" : "string",
          "value" : "string"
        } ]
      },
      "bannerMobileLowImageUrl" : "Banner image. Mobile size low resolution (320x88).",
      "bannerMobileExtraHdImageUrl" : "Banner image. Mobile size high resolution (1440x395).",
      "trackingImageUrl" : "The URL for a 1px by 1px tracking pixel that can be used to collect statistics for views of the channel or video pages.",
      "bannerMobileHdImageUrl" : "Banner image. Mobile size high resolution (1280x360).",
      "bannerTvLowImageUrl" : "Banner image. TV size low resolution (854x480).",
      "bannerTabletLowImageUrl" : "Banner image. Tablet size low resolution (1138x188).",
      "bannerTvHighImageUrl" : "Banner image. TV size high resolution (1920x1080).",
      "bannerTvMediumImageUrl" : "Banner image. TV size medium resolution (1280x720).",
      "bannerMobileMediumHdImageUrl" : "Banner image. Mobile size medium/high resolution (960x263).",
      "largeBrandedBannerImageUrl" : {
        "default" : "string",
        "defaultLanguage" : {
          "value" : "string"
        },
        "localized" : [ {
          "language" : "string",
          "value" : "string"
        } ]
      },
      "bannerTabletImageUrl" : "Banner image. Tablet size (1707x283).",
      "smallBrandedBannerImageImapScript" : {
        "default" : "string",
        "defaultLanguage" : {
          "value" : "string"
        },
        "localized" : [ {
          "language" : "string",
          "value" : "string"
        } ]
      },
      "bannerImageUrl" : "Banner image. Desktop size (1060x175).",
      "largeBrandedBannerImageImapScript" : {
        "default" : "string",
        "defaultLanguage" : {
          "value" : "string"
        },
        "localized" : [ {
          "language" : "string",
          "value" : "string"
        } ]
      },
      "bannerMobileImageUrl" : "Banner image. Mobile size (640x175).",
      "bannerTabletHdImageUrl" : "Banner image. Tablet size high resolution (2276x377).",
      "backgroundImageUrl" : {
        "default" : "string",
        "defaultLanguage" : {
          "value" : "string"
        },
        "localized" : [ {
          "language" : "string",
          "value" : "string"
        } ]
      }
    },
    "watch" : {
      "backgroundColor" : "The text color for the video watch page's branded area.",
      "featuredPlaylistId" : "An ID that uniquely identifies a playlist that displays next to the video player.",
      "textColor" : "The background color for the video watch page's branded area."
    },
    "hints" : [ {
      "property" : "A property.",
      "value" : "The property's value."
    } ],
    "channel" : {
      "country" : "The country of the channel.",
      "featuredChannelsUrls" : [ "string" ],
      "featuredChannelsTitle" : "Title for the featured channels tab.",
      "keywords" : "Lists keywords associated with the channel, comma-separated.",
      "defaultTab" : "Which content tab users should see when viewing the channel.",
      "showRelatedChannels" : "Whether related channels should be proposed.",
      "description" : "Specifies the channel description.",
      "unsubscribedTrailer" : "The trailer of the channel, for users that are not subscribers.",
      "title" : "Specifies the channel title.",
      "defaultLanguage" : "string",
      "moderateComments" : "Whether user-submitted comments left on the channel page need to be approved by the channel owner to be publicly visible.",
      "trackingAnalyticsAccountId" : "The ID for a Google Analytics account to track and measure traffic to the channels.",
      "showBrowseView" : "Whether the tab to browse the videos should be displayed.",
      "profileColor" : "A prominent color that can be rendered on this channel page."
    }
  },
  "contentOwnerDetails" : {
    "contentOwner" : "The ID of the content owner linked to the channel.",
    "timeLinked" : "The date and time of when the channel was linked to the content owner. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format."
  },
  "conversionPings" : {
    "pings" : [ {
      "conversionUrl" : "The url (without the schema) that the player shall send the ping to. It's at caller's descretion to decide which schema to use (http vs https) Example of a returned url: //googleads.g.doubleclick.net/pagead/ viewthroughconversion/962985656/?data=path%3DtHe_path%3Btype%3D cview%3Butuid%3DGISQtTNGYqaYl4sKxoVvKA&amp;labe=default The caller must append biscotti authentication (ms param in case of mobile, for example) to this ping.",
      "context" : "Defines the context of the ping."
    } ]
  },
  "auditDetails" : {
    "contentIdClaimsGoodStanding" : "Whether or not the channel has any unresolved claims.",
    "copyrightStrikesGoodStanding" : "Whether or not the channel has any copyright strikes.",
    "communityGuidelinesGoodStanding" : "Whether or not the channel respects the community guidelines."
  },
  "invideoPromotion" : {
    "defaultTiming" : {
      "offsetMs" : "Defines the time at which the promotion will appear. Depending on the value of type the value of the offsetMs field will represent a time offset from the start or from the end of the video, expressed in milliseconds.",
      "type" : "Describes a timing type. If the value is offsetFromStart, then the offsetMs field represents an offset from the start of the video. If the value is offsetFromEnd, then the offsetMs field represents an offset from the end of the video.",
      "durationMs" : "Defines the duration in milliseconds for which the promotion should be displayed. If missing, the client should use the default."
    },
    "position" : {
      "cornerPosition" : "Describes in which corner of the video the visual widget will appear.",
      "type" : "Defines the position type."
    },
    "items" : [ {
      "timing" : {
        "offsetMs" : "Defines the time at which the promotion will appear. Depending on the value of type the value of the offsetMs field will represent a time offset from the start or from the end of the video, expressed in milliseconds.",
        "type" : "Describes a timing type. If the value is offsetFromStart, then the offsetMs field represents an offset from the start of the video. If the value is offsetFromEnd, then the offsetMs field represents an offset from the end of the video.",
        "durationMs" : "Defines the duration in milliseconds for which the promotion should be displayed. If missing, the client should use the default."
      },
      "customMessage" : "A custom message to display for this promotion. This field is currently ignored unless the promoted item is a website.",
      "id" : {
        "websiteUrl" : "If the promoted item represents a website, this field represents the url pointing to the website. This field will be present only if type has the value website.",
        "recentlyUploadedBy" : "If type is recentUpload, this field identifies the channel from which to take the recent upload. If missing, the channel is assumed to be the same channel for which the invideoPromotion is set.",
        "videoId" : "If the promoted item represents a video, this field represents the unique YouTube ID identifying it. This field will be present only if type has the value video.",
        "type" : "Describes the type of the promoted item."
      },
      "promotedByContentOwner" : "If true, the content owner's name will be used when displaying the promotion. This field can only be set when the update is made on behalf of the content owner."
    } ],
    "useSmartTiming" : "Indicates whether the channel's promotional campaign uses \"smart timing.\" This feature attempts to show promotions at a point in the video when they are more likely to be clicked and less likely to disrupt the viewing experience. This feature also picks up a single promotion to show on each video."
  },
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the channel.",
  "statistics" : {
    "videoCount" : "The number of videos uploaded to the channel.",
    "subscriberCount" : "The number of subscribers that the channel has.",
    "viewCount" : "The number of times the channel has been viewed.",
    "hiddenSubscriberCount" : "Whether or not the number of subscribers is shown for this user.",
    "commentCount" : "The number of comments for the channel."
  },
  "status" : {
    "isLinked" : "If true, then the user is linked to either a YouTube username or G+ account. Otherwise, the user doesn't have a public YouTube identity.",
    "longUploadsStatus" : "The long uploads status of this channel. See",
    "privacyStatus" : "Privacy status of the channel."
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

The onBehalfOfContentOwner parameter indicates that the authenticated user is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with needs to be linked to the specified YouTube content owner.

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

## update_channel_section

Update a channelSection.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part names that you can include in the parameter value are snippet and contentDetails.

**Type:** string

### $body

**Type:** object

```json
{
  "snippet" : {
    "defaultLanguage" : "The language of the channel section's default title and description.",
    "localized" : {
      "title" : "The localized strings for channel section's title."
    },
    "style" : "The style of the channel section.",
    "position" : "The position of the channel section in the channel.",
    "title" : "The channel section's title for multiple_playlists and multiple_channels.",
    "type" : "The type of the channel section.",
    "channelId" : "The ID that YouTube uses to uniquely identify the channel that published the channel section."
  },
  "targeting" : {
    "regions" : [ "string" ],
    "languages" : [ "string" ],
    "countries" : [ "string" ]
  },
  "localizations" : "Localizations for different languages",
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#channelSection\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the channel section.",
  "contentDetails" : {
    "channels" : [ "string" ],
    "playlists" : [ "string" ]
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## update_comment

Modifies a comment.

<details><summary>Parameters</summary>

### part (required)

The part parameter identifies the properties that the API response will include. You must at least include the snippet part in the parameter value since that part contains all of the properties that the API request can update.

**Type:** string

### $body

A comment represents a single YouTube comment.

**Type:** object

```json
{
  "snippet" : {
    "authorProfileImageUrl" : "The URL for the avatar of the user who posted the comment.",
    "textDisplay" : "The comment's text. The format is either plain text or HTML dependent on what has been requested. Even the plain text representation may differ from the text originally posted in that it may replace video links with video titles etc.",
    "publishedAt" : "The date and time when the comment was orignally published. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "authorChannelId" : { },
    "moderationStatus" : "The comment's moderation status. Will not be set if the comments were requested through the id filter.",
    "likeCount" : "The total number of likes this comment has received.",
    "videoId" : "The ID of the video the comment refers to, if any.",
    "textOriginal" : "The comment's original raw text as initially posted or last updated. The original text will only be returned if it is accessible to the viewer, which is only guaranteed if the viewer is the comment's author.",
    "authorDisplayName" : "The name of the user who posted the comment.",
    "parentId" : "The unique id of the parent comment, only set for replies.",
    "canRate" : "Whether the current viewer can rate this comment.",
    "authorChannelUrl" : "Link to the author's YouTube channel, if any.",
    "channelId" : "The id of the corresponding YouTube channel. In case of a channel comment this is the channel the comment refers to. In case of a video comment it's the video's channel.",
    "updatedAt" : "The date and time when was last updated . The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "viewerRating" : "The rating the viewer has given to this comment. For the time being this will never return RATE_TYPE_DISLIKE and instead return RATE_TYPE_NONE. This may change in the future."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#comment\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the comment."
}
```

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

## update_comment_thread

Modifies the top-level comment in a comment thread.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies a comma-separated list of commentThread resource properties that the API response will include. You must at least include the snippet part in the parameter value since that part contains all of the properties that the API request can update.

**Type:** string

### $body

A comment thread represents information that applies to a top level comment and all its replies. It can also include the top level comment itself and some of the replies.

**Type:** object

```json
{
  "snippet" : {
    "canReply" : "Whether the current viewer of the thread can reply to it. This is viewer specific - other viewers may see a different value for this field.",
    "totalReplyCount" : "The total number of replies (not including the top level comment).",
    "topLevelComment" : {
      "snippet" : {
        "authorProfileImageUrl" : "The URL for the avatar of the user who posted the comment.",
        "textDisplay" : "The comment's text. The format is either plain text or HTML dependent on what has been requested. Even the plain text representation may differ from the text originally posted in that it may replace video links with video titles etc.",
        "publishedAt" : "The date and time when the comment was orignally published. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
        "authorChannelId" : { },
        "moderationStatus" : "The comment's moderation status. Will not be set if the comments were requested through the id filter.",
        "likeCount" : "The total number of likes this comment has received.",
        "videoId" : "The ID of the video the comment refers to, if any.",
        "textOriginal" : "The comment's original raw text as initially posted or last updated. The original text will only be returned if it is accessible to the viewer, which is only guaranteed if the viewer is the comment's author.",
        "authorDisplayName" : "The name of the user who posted the comment.",
        "parentId" : "The unique id of the parent comment, only set for replies.",
        "canRate" : "Whether the current viewer can rate this comment.",
        "authorChannelUrl" : "Link to the author's YouTube channel, if any.",
        "channelId" : "The id of the corresponding YouTube channel. In case of a channel comment this is the channel the comment refers to. In case of a video comment it's the video's channel.",
        "updatedAt" : "The date and time when was last updated . The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
        "viewerRating" : "The rating the viewer has given to this comment. For the time being this will never return RATE_TYPE_DISLIKE and instead return RATE_TYPE_NONE. This may change in the future."
      },
      "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#comment\".",
      "etag" : "Etag of this resource.",
      "id" : "The ID that YouTube uses to uniquely identify the comment."
    },
    "isPublic" : "Whether the thread (and therefore all its comments) is visible to all YouTube users.",
    "videoId" : "The ID of the video the comments refer to, if any. No video_id implies a channel discussion comment.",
    "channelId" : "The YouTube channel the comments in the thread refer to or the channel with the video the comments refer to. If video_id isn't set the comments refer to the channel itself."
  },
  "replies" : {
    "comments" : [ {
      "snippet" : {
        "authorProfileImageUrl" : "The URL for the avatar of the user who posted the comment.",
        "textDisplay" : "The comment's text. The format is either plain text or HTML dependent on what has been requested. Even the plain text representation may differ from the text originally posted in that it may replace video links with video titles etc.",
        "publishedAt" : "The date and time when the comment was orignally published. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
        "authorChannelId" : { },
        "moderationStatus" : "The comment's moderation status. Will not be set if the comments were requested through the id filter.",
        "likeCount" : "The total number of likes this comment has received.",
        "videoId" : "The ID of the video the comment refers to, if any.",
        "textOriginal" : "The comment's original raw text as initially posted or last updated. The original text will only be returned if it is accessible to the viewer, which is only guaranteed if the viewer is the comment's author.",
        "authorDisplayName" : "The name of the user who posted the comment.",
        "parentId" : "The unique id of the parent comment, only set for replies.",
        "canRate" : "Whether the current viewer can rate this comment.",
        "authorChannelUrl" : "Link to the author's YouTube channel, if any.",
        "channelId" : "The id of the corresponding YouTube channel. In case of a channel comment this is the channel the comment refers to. In case of a video comment it's the video's channel.",
        "updatedAt" : "The date and time when was last updated . The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
        "viewerRating" : "The rating the viewer has given to this comment. For the time being this will never return RATE_TYPE_DISLIKE and instead return RATE_TYPE_NONE. This may change in the future."
      },
      "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#comment\".",
      "etag" : "Etag of this resource.",
      "id" : "The ID that YouTube uses to uniquely identify the comment."
    } ]
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#commentThread\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the comment thread."
}
```

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

## update_live_broadcast

Updates a broadcast. For example, you could modify the broadcast settings defined in the liveBroadcast resource's contentDetails object.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part properties that you can include in the parameter value are id, snippet, contentDetails, and status.

Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. For example, a broadcast's privacy status is defined in the status part. As such, if your request is updating a private or unlisted broadcast, and the request's part parameter value includes the status part, the broadcast's privacy setting will be updated to whatever value the request body specifies. If the request body does not specify a value, the existing privacy setting will be removed and the broadcast will revert to the default privacy setting.

**Type:** string

### $body

A liveBroadcast resource represents an event that will be streamed, via live video, on YouTube.

**Type:** object

```json
{
  "snippet" : {
    "actualStartTime" : "The date and time that the broadcast actually started. This information is only available once the broadcast's state is live. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "isDefaultBroadcast" : "boolean",
    "publishedAt" : "The date and time that the broadcast was added to YouTube's live broadcast schedule. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "liveChatId" : "The id of the live chat for this broadcast.",
    "scheduledStartTime" : "The date and time that the broadcast is scheduled to start. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "scheduledEndTime" : "The date and time that the broadcast is scheduled to end. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "actualEndTime" : "The date and time that the broadcast actually ended. This information is only available once the broadcast's state is complete. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "description" : "The broadcast's description. As with the title, you can set this field by modifying the broadcast resource or by setting the description field of the corresponding video resource.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The broadcast's title. Note that the broadcast represents exactly one YouTube video. You can set this field by modifying the broadcast resource or by setting the title field of the corresponding video resource.",
    "channelId" : "The ID that YouTube uses to uniquely identify the channel that is publishing the broadcast."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#liveBroadcast\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube assigns to uniquely identify the broadcast.",
  "contentDetails" : {
    "monitorStream" : {
      "enableMonitorStream" : "This value determines whether the monitor stream is enabled for the broadcast. If the monitor stream is enabled, then YouTube will broadcast the event content on a special stream intended only for the broadcaster's consumption. The broadcaster can use the stream to review the event content and also to identify the optimal times to insert cuepoints.\n\nYou need to set this value to true if you intend to have a broadcast delay for your event.\n\nNote: This property cannot be updated once the broadcast is in the testing or live state.",
      "embedHtml" : "HTML code that embeds a player that plays the monitor stream.",
      "broadcastStreamDelayMs" : "If you have set the enableMonitorStream property to true, then this property determines the length of the live broadcast delay."
    },
    "recordFromStart" : "Automatically start recording after the event goes live. The default value for this property is true.\n\n\n\nImportant: You must also set the enableDvr property's value to true if you want the playback to be available immediately after the broadcast ends. If you set this property's value to true but do not also set the enableDvr property to true, there may be a delay of around one day before the archived video will be available for playback.",
    "boundStreamId" : "This value uniquely identifies the live stream bound to the broadcast.",
    "enableDvr" : "This setting determines whether viewers can access DVR controls while watching the video. DVR controls enable the viewer to control the video playback experience by pausing, rewinding, or fast forwarding content. The default value for this property is true.\n\n\n\nImportant: You must set the value to true and also set the enableArchive property's value to true if you want to make playback available immediately after the broadcast ends.",
    "enableLowLatency" : "Indicates whether this broadcast has low latency enabled.",
    "stereoLayout" : "string. Possible values: left_right | mono | top_bottom",
    "boundStreamLastUpdateTimeMs" : "The date and time that the live stream referenced by boundStreamId was last updated.",
    "startWithSlate" : "This setting indicates whether the broadcast should automatically begin with an in-stream slate when you update the broadcast's status to live. After updating the status, you then need to send a liveCuepoints.insert request that sets the cuepoint's eventState to end to remove the in-stream slate and make your broadcast stream visible to viewers.",
    "closedCaptionsType" : "string. Possible values: closedCaptionsDisabled | closedCaptionsEmbedded | closedCaptionsHttpPost",
    "enableEmbed" : "This setting indicates whether the broadcast video can be played in an embedded player. If you choose to archive the video (using the enableArchive property), this setting will also apply to the archived video.",
    "enableContentEncryption" : "This setting indicates whether YouTube should enable content encryption for the broadcast.",
    "enableAutoStart" : "This setting indicates whether auto start is enabled for this broadcast.",
    "latencyPreference" : "If both this and enable_low_latency are set, they must match. LATENCY_NORMAL should match enable_low_latency=false LATENCY_LOW should match enable_low_latency=true LATENCY_ULTRA_LOW should have enable_low_latency omitted.",
    "projection" : "The projection format of this broadcast. This defaults to rectangular.",
    "enableClosedCaptions" : "This setting indicates whether HTTP POST closed captioning is enabled for this broadcast. The ingestion URL of the closed captions is returned through the liveStreams API. This is mutually exclusive with using the closed_captions_type property, and is equivalent to setting closed_captions_type to CLOSED_CAPTIONS_HTTP_POST.",
    "mesh" : "byte"
  },
  "statistics" : {
    "totalChatCount" : "The total number of live chat messages currently on the broadcast. The property and its value will be present if the broadcast is public, has the live chat feature enabled, and has at least one message. Note that this field will not be filled after the broadcast ends. So this property would not identify the number of chat messages for an archived video of a completed live broadcast.",
    "concurrentViewers" : "The number of viewers currently watching the broadcast. The property and its value will be present if the broadcast has current viewers and the broadcast owner has not hidden the viewcount for the video. Note that YouTube stops tracking the number of concurrent viewers for a broadcast when the broadcast ends. So, this property would not identify the number of viewers watching an archived video of a live broadcast that already ended."
  },
  "status" : {
    "liveBroadcastPriority" : "Priority of the live broadcast event (internal state).",
    "recordingStatus" : "The broadcast's recording status.",
    "privacyStatus" : "The broadcast's privacy status. Note that the broadcast represents exactly one YouTube video, so the privacy settings are identical to those supported for videos. In addition, you can set this field by modifying the broadcast resource or by setting the privacyStatus field of the corresponding video resource.",
    "lifeCycleStatus" : "The broadcast's status. The status can be updated using the API's liveBroadcasts.transition method."
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## update_live_stream

Updates a video stream. If the properties that you want to change cannot be updated, then you need to create a new stream with the proper settings.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

The part properties that you can include in the parameter value are id, snippet, cdn, and status.

Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. If the request body does not specify a value for a mutable property, the existing value for that property will be removed.

**Type:** string

### $body

A live stream describes a live ingestion point.

**Type:** object

```json
{
  "snippet" : {
    "publishedAt" : "The date and time that the stream was created. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "description" : "The stream's description. The value cannot be longer than 10000 characters.",
    "title" : "The stream's title. The value must be between 1 and 128 characters long.",
    "channelId" : "The ID that YouTube uses to uniquely identify the channel that is transmitting the stream.",
    "isDefaultStream" : "boolean"
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#liveStream\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube assigns to uniquely identify the stream.",
  "cdn" : {
    "frameRate" : "The frame rate of the inbound video data.",
    "format" : "The format of the video stream that you are sending to Youtube.",
    "ingestionType" : "The method or protocol used to transmit the video stream.",
    "ingestionInfo" : {
      "ingestionAddress" : "The primary ingestion URL that you should use to stream video to YouTube. You must stream video to this URL.\n\nDepending on which application or tool you use to encode your video stream, you may need to enter the stream URL and stream name separately or you may need to concatenate them in the following format:\n\nSTREAM_URL/STREAM_NAME",
      "backupIngestionAddress" : "The backup ingestion URL that you should use to stream video to YouTube. You have the option of simultaneously streaming the content that you are sending to the ingestionAddress to this URL.",
      "streamName" : "The HTTP or RTMP stream name that YouTube assigns to the video stream."
    },
    "resolution" : "The resolution of the inbound video data."
  },
  "contentDetails" : {
    "closedCaptionsIngestionUrl" : "The ingestion URL where the closed captions of this stream are sent.",
    "isReusable" : "Indicates whether the stream is reusable, which means that it can be bound to multiple broadcasts. It is common for broadcasters to reuse the same stream for many different broadcasts if those broadcasts occur at different times.\n\nIf you set this value to false, then the stream will not be reusable, which means that it can only be bound to one broadcast. Non-reusable streams differ from reusable streams in the following ways:  \n- A non-reusable stream can only be bound to one broadcast. \n- A non-reusable stream might be deleted by an automated process after the broadcast ends. \n- The  liveStreams.list method does not list non-reusable streams if you call the method and set the mine parameter to true. The only way to use that method to retrieve the resource for a non-reusable stream is to use the id parameter to identify the stream."
  },
  "status" : {
    "healthStatus" : {
      "lastUpdateTimeSeconds" : "The last time this status was updated (in seconds)",
      "configurationIssues" : [ {
        "severity" : "How severe this issue is to the stream.",
        "reason" : "The short-form reason for this issue.",
        "description" : "The long-form description of the issue and how to resolve it.",
        "type" : "The kind of error happening."
      } ],
      "status" : "The status code of this stream"
    },
    "streamStatus" : "string. Possible values: active | created | error | inactive | ready"
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### onBehalfOfContentOwnerChannel

This parameter can only be used in a properly authorized request. Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwnerChannel parameter specifies the YouTube channel ID of the channel to which a video is being added. This parameter is required when a request specifies a value for the onBehalfOfContentOwner parameter, and it can only be used in conjunction with that parameter. In addition, the request must be authorized using a CMS account that is linked to the content owner that the onBehalfOfContentOwner parameter specifies. Finally, the channel that the onBehalfOfContentOwnerChannel parameter value specifies must be linked to the content owner that the onBehalfOfContentOwner parameter specifies.

This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and perform actions on behalf of the channel specified in the parameter value, without having to provide authentication credentials for each separate channel.

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

## update_metadata_for_video

Updates a video's metadata.

<details><summary>Parameters</summary>

### part (required)

The part parameter serves two purposes in this operation. It identifies the properties that the write operation will set as well as the properties that the API response will include.

Note that this method will override the existing values for all of the mutable properties that are contained in any parts that the parameter value specifies. For example, a video's privacy setting is contained in the status part. As such, if your request is updating a private video, and the request's part parameter value includes the status part, the video's privacy setting will be updated to whatever value the request body specifies. If the request body does not specify a value, the existing privacy setting will be removed and the video will revert to the default privacy setting.

In addition, not all parts contain properties that can be set when inserting or updating a video. For example, the statistics object encapsulates statistics that YouTube calculates for a video and does not contain values that you can set or modify. If the parameter value specifies a part that does not contain mutable values, that part will still be included in the API response.

**Type:** string

### $body

A video resource represents a YouTube video.

**Type:** object

```json
{
  "snippet" : {
    "defaultLanguage" : "The language of the videos's default snippet.",
    "publishedAt" : "The date and time that the video was uploaded. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "defaultAudioLanguage" : "The default_audio_language property specifies the language spoken in the video's default audio track.",
    "localized" : {
      "description" : "Localized version of the video's description.",
      "title" : "Localized version of the video's title."
    },
    "description" : "The video's description.",
    "thumbnails" : {
      "standard" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "default" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "high" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "maxres" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      },
      "medium" : {
        "width" : "(Optional) Width of the thumbnail image.",
        "url" : "The thumbnail image's URL.",
        "height" : "(Optional) Height of the thumbnail image."
      }
    },
    "title" : "The video's title.",
    "categoryId" : "The YouTube video category associated with the video.",
    "channelId" : "The ID that YouTube uses to uniquely identify the channel that the video was uploaded to.",
    "channelTitle" : "Channel title for the channel that the video belongs to.",
    "liveBroadcastContent" : "Indicates if the video is an upcoming/active live broadcast. Or it's \"none\" if the video is not an upcoming/active live broadcast.",
    "tags" : [ "string" ]
  },
  "fileDetails" : {
    "container" : "The uploaded video file's container format.",
    "fileName" : "The uploaded file's name. This field is present whether a video file or another type of file was uploaded.",
    "creationTime" : "The date and time when the uploaded video file was created. The value is specified in ISO 8601 format. Currently, the following ISO 8601 formats are supported:  \n- Date only: YYYY-MM-DD \n- Naive time: YYYY-MM-DDTHH:MM:SS \n- Time with timezone: YYYY-MM-DDTHH:MM:SS+HH:MM",
    "fileSize" : "The uploaded file's size in bytes. This field is present whether a video file or another type of file was uploaded.",
    "videoStreams" : [ {
      "codec" : "The video codec that the stream uses.",
      "vendor" : "A value that uniquely identifies a video vendor. Typically, the value is a four-letter vendor code.",
      "rotation" : "The amount that YouTube needs to rotate the original source content to properly display the video.",
      "frameRateFps" : "The video stream's frame rate, in frames per second.",
      "aspectRatio" : "The video content's display aspect ratio, which specifies the aspect ratio in which the video should be displayed.",
      "heightPixels" : "The encoded video content's height in pixels.",
      "bitrateBps" : "The video stream's bitrate, in bits per second.",
      "widthPixels" : "The encoded video content's width in pixels. You can calculate the video's encoding aspect ratio as width_pixels&nbsp;/&nbsp;height_pixels."
    } ],
    "audioStreams" : [ {
      "channelCount" : "The number of audio channels that the stream contains.",
      "codec" : "The audio codec that the stream uses.",
      "vendor" : "A value that uniquely identifies a video vendor. Typically, the value is a four-letter vendor code.",
      "bitrateBps" : "The audio stream's bitrate, in bits per second."
    } ],
    "bitrateBps" : "The uploaded video file's combined (video and audio) bitrate in bits per second.",
    "durationMs" : "The length of the uploaded video in milliseconds.",
    "fileType" : "The uploaded file's type as detected by YouTube's video processing engine. Currently, YouTube only processes video files, but this field is present whether a video file or another type of file was uploaded."
  },
  "monetizationDetails" : {
    "access" : {
      "exception" : [ "string" ],
      "allowed" : "The value of allowed indicates whether the access to the policy is allowed or denied by default."
    }
  },
  "localizations" : "List with all localizations.",
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#video\".",
  "recordingDetails" : {
    "locationDescription" : "The text description of the location where the video was recorded.",
    "recordingDate" : "The date and time when the video was recorded. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sssZ) format.",
    "location" : {
      "altitude" : "Altitude above the reference ellipsoid, in meters.",
      "latitude" : "Latitude in degrees.",
      "longitude" : "Longitude in degrees."
    }
  },
  "projectDetails" : {
    "tags" : [ "string" ]
  },
  "contentDetails" : {
    "duration" : "The length of the video. The tag value is an ISO 8601 duration in the format PT#M#S, in which the letters PT indicate that the value specifies a period of time, and the letters M and S refer to length in minutes and seconds, respectively. The # characters preceding the M and S letters are both integers that specify the number of minutes (or seconds) of the video. For example, a value of PT15M51S indicates that the video is 15 minutes and 51 seconds long.",
    "licensedContent" : "The value of is_license_content indicates whether the video is licensed content.",
    "countryRestriction" : {
      "exception" : [ "string" ],
      "allowed" : "The value of allowed indicates whether the access to the policy is allowed or denied by default."
    },
    "caption" : "The value of captions indicates whether the video has captions or not.",
    "contentRating" : {
      "ifcoRating" : "The video's Irish Film Classification Office (IFCO - Ireland) rating. See the IFCO website for more information.",
      "lsfRating" : "The video's rating from Indonesia's Lembaga Sensor Film.",
      "cicfRating" : "The video's rating from the Commission de Contrôle des Films (Belgium).",
      "tvpgRating" : "The video's TV Parental Guidelines (TVPG) rating.",
      "menaMpaaRating" : "The rating system for MENA countries, a clone of MPAA. It is needed to",
      "ilfilmRating" : "The video's rating in Israel.",
      "nkclvRating" : "The video's rating from the Nacionãlais Kino centrs (National Film Centre of Latvia).",
      "catvfrRating" : "The video's rating from the Canadian Radio-Television and Telecommunications Commission (CRTC) for Canadian French-language broadcasts. For more information, see the Canadian Broadcast Standards Council website.",
      "egfilmRating" : "The video's rating in Egypt.",
      "cccRating" : "The video's Consejo de Calificación Cinematográfica (Chile) rating.",
      "resorteviolenciaRating" : "The video's rating in Venezuela.",
      "chvrsRating" : "The video's Canadian Home Video Rating System (CHVRS) rating.",
      "nbcplRating" : "The video's rating in Poland.",
      "chfilmRating" : "The video's rating in Switzerland.",
      "anatelRating" : "The video's Anatel (Asociación Nacional de Televisión) rating for Chilean television.",
      "smsaRating" : "The video's rating from Statens medieråd (Sweden's National Media Council).",
      "smaisRating" : "The video's rating in Iceland.",
      "kfcbRating" : "The video's rating from the Kenya Film Classification Board.",
      "skfilmRating" : "The video's rating in Slovakia.",
      "acbRating" : "The video's Australian Classification Board (ACB) or Australian Communications and Media Authority (ACMA) rating. ACMA ratings are used to classify children's television programming.",
      "mibacRating" : "The video's rating from the Ministero dei Beni e delle Attività Culturali e del Turismo (Italy).",
      "djctqRatingReasons" : [ "string. Possible values: djctqCriminalActs | djctqDrugs | djctqExplicitSex | djctqExtremeViolence | djctqIllegalDrugs | djctqImpactingContent | djctqInappropriateLanguage | djctqLegalDrugs | djctqNudity | djctqSex | djctqSexualContent | djctqViolence" ],
      "ytRating" : "A rating that YouTube uses to identify age-restricted content.",
      "kijkwijzerRating" : "voor de Classificatie van Audiovisuele Media (Netherlands).",
      "mdaRating" : "The video's rating from Singapore's Media Development Authority (MDA) and, specifically, it's Board of Film Censors (BFC).",
      "fcoRating" : "The video's rating from Hong Kong's Office for Film, Newspaper and Article Administration.",
      "mekuRating" : "The video's rating from Finland's Kansallinen Audiovisuaalinen Instituutti (National Audiovisual Institute).",
      "mccaaRating" : "The video's rating from Malta's Film Age-Classification Board.",
      "cncRating" : "Rating system in France - Commission de classification cinematographique",
      "rteRating" : "The video's rating from Ireland's Raidió Teilifís Éireann.",
      "nbcRating" : "The video's rating from the Maldives National Bureau of Classification.",
      "moctwRating" : "The video's rating from Taiwan's Ministry of Culture (文化部).",
      "mocRating" : "The video's Ministerio de Cultura (Colombia) rating.",
      "csaRating" : "The video's rating from France's Conseil supérieur de l?audiovisuel, which rates broadcast content.",
      "mpaaRating" : "The video's Motion Picture Association of America (MPAA) rating.",
      "pefilmRating" : "The video's rating in Peru.",
      "cscfRating" : "The video's rating from Luxembourg's Commission de surveillance de la classification des films (CSCF).",
      "bfvcRating" : "The video's rating from Thailand's Board of Film and Video Censors.",
      "mccypRating" : "The video's rating from the Danish Film Institute's (Det Danske Filminstitut) Media Council for Children and Young People.",
      "mpaatRating" : "The rating system for trailer, DVD, and Ad in the US. See http://movielabs.com/md/ratings/v2.3/html/US_MPAAT_Ratings.html.",
      "mcstRating" : "The video's rating system for Vietnam - MCST",
      "eefilmRating" : "The video's rating in Estonia.",
      "grfilmRating" : "The video's rating in Greece.",
      "bmukkRating" : "The video's rating from the Austrian Board of Media Classification (Bundesministerium für Unterricht, Kunst und Kultur).",
      "cbfcRating" : "The video's Central Board of Film Certification (CBFC - India) rating.",
      "djctqRating" : "The video's Departamento de Justiça, Classificação, Qualificação e Títulos (DJCQT - Brazil) rating.",
      "rcnofRating" : "The video's rating from the Hungarian Nemzeti Filmiroda, the Rating Committee of the National Office of Film.",
      "fmocRating" : "This property has been deprecated. Use the contentDetails.contentRating.cncRating instead.",
      "mtrcbRating" : "The video's rating from the Movie and Television Review and Classification Board (Philippines).",
      "oflcRating" : "The video's Office of Film and Literature Classification (OFLC - New Zealand) rating.",
      "agcomRating" : "The video's rating from Italy's Autorità per le Garanzie nelle Comunicazioni (AGCOM).",
      "russiaRating" : "The video's National Film Registry of the Russian Federation (MKRF - Russia) rating.",
      "cceRating" : "The video's rating from Portugal's Comissão de Classificação de Espect´culos.",
      "fskRating" : "The video's Freiwillige Selbstkontrolle der Filmwirtschaft (FSK - Germany) rating.",
      "rtcRating" : "The video's General Directorate of Radio, Television and Cinematography (Mexico) rating.",
      "nfvcbRating" : "The video's rating from Nigeria's National Film and Video Censors Board.",
      "incaaRating" : "The video's INCAA (Instituto Nacional de Cine y Artes Audiovisuales - Argentina) rating.",
      "medietilsynetRating" : "The video's rating from Medietilsynet, the Norwegian Media Authority.",
      "eirinRating" : "The video's Eirin (映倫) rating. Eirin is the Japanese rating system.",
      "fpbRatingReasons" : [ "string. Possible values: fpbBlasphemy | fpbCriminalTechniques | fpbDrugs | fpbHorror | fpbImitativeActsTechniques | fpbLanguage | fpbNudity | fpbPrejudice | fpbSex | fpbSexualViolence | fpbViolence" ],
      "icaaRating" : "The video's Instituto de la Cinematografía y de las Artes Audiovisuales (ICAA - Spain) rating.",
      "catvRating" : "Rating system for Canadian TV - Canadian TV Classification System The video's rating from the Canadian Radio-Television and Telecommunications Commission (CRTC) for Canadian English-language broadcasts. For more information, see the Canadian Broadcast Standards Council website.",
      "fcbmRating" : "The video's rating from Malaysia's Film Censorship Board.",
      "fpbRating" : "The video's rating from South Africa's Film and Publication Board.",
      "bbfcRating" : "The video's British Board of Film Classification (BBFC) rating.",
      "kmrbRating" : "The video's Korea Media Rating Board (영상물등급위원회) rating. The KMRB rates videos in South Korea.",
      "nfrcRating" : "The video's rating from the Bulgarian National Film Center.",
      "cnaRating" : "The video's rating from Romania's CONSILIUL NATIONAL AL AUDIOVIZUALULUI (CNA).",
      "czfilmRating" : "The video's rating in the Czech Republic.",
      "ecbmctRating" : "Rating system in Turkey - Evaluation and Classification Board of the Ministry of Culture and Tourism"
    },
    "definition" : "The value of definition indicates whether the video is available in high definition or only in standard definition.",
    "hasCustomThumbnail" : "Indicates whether the video uploader has provided a custom thumbnail image for the video. This property is only visible to the video uploader.",
    "projection" : "Specifies the projection format of the video.",
    "regionRestriction" : {
      "blocked" : [ "string" ],
      "allowed" : [ "string" ]
    },
    "dimension" : "The value of dimension indicates whether the video is available in 3D or in 2D."
  },
  "topicDetails" : {
    "relevantTopicIds" : [ "string" ],
    "topicIds" : [ "string" ],
    "topicCategories" : [ "string" ]
  },
  "liveStreamingDetails" : {
    "activeLiveChatId" : "The ID of the currently active live chat attached to this video. This field is filled only if the video is a currently live broadcast that has live chat. Once the broadcast transitions to complete this field will be removed and the live chat closed down. For persistent broadcasts that live chat id will no longer be tied to this video but rather to the new video being displayed at the persistent page.",
    "actualStartTime" : "The time that the broadcast actually started. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format. This value will not be available until the broadcast begins.",
    "scheduledStartTime" : "The time that the broadcast is scheduled to begin. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "scheduledEndTime" : "The time that the broadcast is scheduled to end. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format. If the value is empty or the property is not present, then the broadcast is scheduled to continue indefinitely.",
    "actualEndTime" : "The time that the broadcast actually ended. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format. This value will not be available until the broadcast is over.",
    "concurrentViewers" : "The number of viewers currently watching the broadcast. The property and its value will be present if the broadcast has current viewers and the broadcast owner has not hidden the viewcount for the video. Note that YouTube stops tracking the number of concurrent viewers for a broadcast when the broadcast ends. So, this property would not identify the number of viewers watching an archived video of a live broadcast that already ended."
  },
  "processingDetails" : {
    "processingStatus" : "The video's processing status. This value indicates whether YouTube was able to process the video or if the video is still being processed.",
    "processingFailureReason" : "The reason that YouTube failed to process the video. This property will only have a value if the processingStatus property's value is failed.",
    "thumbnailsAvailability" : "This value indicates whether thumbnail images have been generated for the video.",
    "fileDetailsAvailability" : "This value indicates whether file details are available for the uploaded video. You can retrieve a video's file details by requesting the fileDetails part in your videos.list() request.",
    "editorSuggestionsAvailability" : "This value indicates whether video editing suggestions, which might improve video quality or the playback experience, are available for the video. You can retrieve these suggestions by requesting the suggestions part in your videos.list() request.",
    "tagSuggestionsAvailability" : "This value indicates whether keyword (tag) suggestions are available for the video. Tags can be added to a video's metadata to make it easier for other users to find the video. You can retrieve these suggestions by requesting the suggestions part in your videos.list() request.",
    "processingIssuesAvailability" : "This value indicates whether the video processing engine has generated suggestions that might improve YouTube's ability to process the the video, warnings that explain video processing problems, or errors that cause video processing problems. You can retrieve these suggestions by requesting the suggestions part in your videos.list() request.",
    "processingProgress" : {
      "partsProcessed" : "The number of parts of the video that YouTube has already processed. You can estimate the percentage of the video that YouTube has already processed by calculating:\n100 * parts_processed / parts_total\n\nNote that since the estimated number of parts could increase without a corresponding increase in the number of parts that have already been processed, it is possible that the calculated progress could periodically decrease while YouTube processes a video.",
      "timeLeftMs" : "An estimate of the amount of time, in millseconds, that YouTube needs to finish processing the video.",
      "partsTotal" : "An estimate of the total number of parts that need to be processed for the video. The number may be updated with more precise estimates while YouTube processes the video."
    }
  },
  "ageGating" : {
    "alcoholContent" : "Indicates whether or not the video has alcoholic beverage content. Only users of legal purchasing age in a particular country, as identified by ICAP, can view the content.",
    "restricted" : "Age-restricted trailers. For redband trailers and adult-rated video-games. Only users aged 18+ can view the content. The the field is true the content is restricted to viewers aged 18+. Otherwise The field won't be present.",
    "videoGameRating" : "Video game rating, if any."
  },
  "etag" : "Etag of this resource.",
  "suggestions" : {
    "processingWarnings" : [ "string. Possible values: hasEditlist | inconsistentResolution | problematicAudioCodec | problematicHdrLookupTable | problematicVideoCodec | unknownAudioCodec | unknownContainer | unknownVideoCodec | unsupportedHdrColorMetadata | unsupportedHdrPixelFormat | unsupportedSphericalProjectionType | unsupportedVrStereoMode" ],
    "editorSuggestions" : [ "string. Possible values: audioQuietAudioSwap | videoAutoLevels | videoCrop | videoStabilize" ],
    "processingErrors" : [ "string. Possible values: archiveFile | audioFile | docFile | imageFile | notAVideoFile | projectFile | unsupportedSpatialAudioLayout" ],
    "processingHints" : [ "string. Possible values: hdrVideo | nonStreamableMov | sendBestQualityVideo | spatialAudio | sphericalVideo | vrVideo" ],
    "tagSuggestions" : [ {
      "tag" : "The keyword tag suggested for the video.",
      "categoryRestricts" : [ "string" ]
    } ]
  },
  "id" : "The ID that YouTube uses to uniquely identify the video.",
  "player" : {
    "embedHeight" : "int64",
    "embedWidth" : "The embed width",
    "embedHtml" : "An  tag that embeds a player that will play the video."
  },
  "statistics" : {
    "dislikeCount" : "The number of users who have indicated that they disliked the video by giving it a negative rating.",
    "likeCount" : "The number of users who have indicated that they liked the video by giving it a positive rating.",
    "viewCount" : "The number of times the video has been viewed.",
    "commentCount" : "The number of comments for the video.",
    "favoriteCount" : "The number of users who currently have the video marked as a favorite video."
  },
  "status" : {
    "license" : "The video's license.",
    "failureReason" : "This value explains why a video failed to upload. This property is only present if the uploadStatus property indicates that the upload failed.",
    "privacyStatus" : "The video's privacy status.",
    "publishAt" : "The date and time when the video is scheduled to publish. It can be set only if the privacy status of the video is private. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "uploadStatus" : "The status of the uploaded video.",
    "publicStatsViewable" : "This value indicates if the extended video statistics on the watch page can be viewed by everyone. Note that the view count, likes, etc will still be visible if this is disabled.",
    "rejectionReason" : "This value explains why YouTube rejected an uploaded video. This property is only present if the uploadStatus property indicates that the upload was rejected.",
    "embeddable" : "This value indicates if the video can be embedded on another website."
  }
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

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

## upload_caption

Uploads a caption track.

<details><summary>Parameters</summary>

### part (required)

The part parameter specifies the caption resource parts that the API response will include. Set the parameter value to snippet.

**Type:** string

### $body

A caption resource represents a YouTube caption track. A caption track is associated with exactly one YouTube video.

**Type:** object

```json
{
  "snippet" : {
    "trackKind" : "The caption track's type.",
    "audioTrackType" : "The type of audio track associated with the caption track.",
    "isDraft" : "Indicates whether the caption track is a draft. If the value is true, then the track is not publicly visible. The default value is false.",
    "language" : "The language of the caption track. The property value is a BCP-47 language tag.",
    "videoId" : "The ID that YouTube uses to uniquely identify the video associated with the caption track.",
    "lastUpdated" : "The date and time when the caption track was last updated. The value is specified in ISO 8601 (YYYY-MM-DDThh:mm:ss.sZ) format.",
    "isAutoSynced" : "Indicates whether YouTube synchronized the caption track to the audio track in the video. The value will be true if a sync was explicitly requested when the caption track was uploaded. For example, when calling the captions.insert or captions.update methods, you can set the sync parameter to true to instruct YouTube to sync the uploaded track to the video. If the value is false, YouTube uses the time codes in the uploaded caption track to determine when to display captions.",
    "failureReason" : "The reason that YouTube failed to process the caption track. This property is only present if the state property's value is failed.",
    "name" : "The name of the caption track. The name is intended to be visible to the user as an option during playback.",
    "isEasyReader" : "Indicates whether caption track is formatted for \"easy reader,\" meaning it is at a third-grade level for language learners. The default value is false.",
    "isLarge" : "Indicates whether the caption track uses large text for the vision-impaired. The default value is false.",
    "isCC" : "Indicates whether the track contains closed captions for the deaf and hard of hearing. The default value is false.",
    "status" : "The caption track's status."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"youtube#caption\".",
  "etag" : "Etag of this resource.",
  "id" : "The ID that YouTube uses to uniquely identify the caption track."
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### onBehalfOf

ID of the Google+ Page for the channel that the request is be on behalf of

**Type:** string

### onBehalfOfContentOwner

Note: This parameter is intended exclusively for YouTube content partners.

The onBehalfOfContentOwner parameter indicates that the request's authorization credentials identify a YouTube CMS user who is acting on behalf of the content owner specified in the parameter value. This parameter is intended for YouTube content partners that own and manage many different YouTube channels. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The actual CMS account that the user authenticates with must be linked to the specified YouTube content owner.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sync

The sync parameter indicates whether YouTube should automatically synchronize the caption file with the audio track of the video. If you set the value to true, YouTube will disregard any time codes that are in the uploaded caption file and generate new time codes for the captions.

You should set the sync parameter to true if you are uploading a transcript, which has no time codes, or if you suspect the time codes in your file are incorrect and want YouTube to try to fix them.

**Type:** boolean

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

