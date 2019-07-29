---
id: google-photos-documentation
title: Google Photos (version v1.*.*)
sidebar_label: Google Photos
layout: docs.mustache
---

## add_enrichment

Adds an enrichment at a specified position in a defined album.

<details><summary>Parameters</summary>

### albumId (required)

Identifier of the album to be requested.

**Type:** string

### $body

The album to be created.

**Type:** object

```json
{
  "albumPosition" : {
    "relativeMediaItemId" : "The media item to which the position is relative to. Only used when position type is AFTER_MEDIA_ITEM.",
    "relativeEnrichmentItemId" : "The enrichment item to which the position is relative to. Only used when position type is AFTER_ENRICHMENT_ITEM.",
    "position" : "Type of position, for a media or enrichment item. \n * `POSITION_TYPE_UNSPECIFIED` - Default value if this enum isn't set.\n * `FIRST_IN_ALBUM` - At the beginning of the album.\n * `LAST_IN_ALBUM` - At the end of the album.\n * `AFTER_MEDIA_ITEM` - After a media item.\n * `AFTER_ENRICHMENT_ITEM` - After an enrichment item.\n"
  },
  "newEnrichmentItem" : {
    "textEnrichment" : {
      "text" : "Text for this enrichment item."
    }
  }
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## create_album

Creates an album in a user's Google Photos library.

<details><summary>Parameters</summary>

### $body

The album to be created.

**Type:** object

```json
{
  "album" : {
    "title" : "Name of the album displayed to the user in their Google Photos account. This string shouldn't be more than 500 characters."
  }
}
```

</details>

## get_album

Returns the album based on the specified albumId. The albumId should be the ID of an album owned by the user or a shared album that the user has joined.

<details><summary>Parameters</summary>

### albumId (required)

Identifier of the album to be requested.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## get_media_item

Returns the media item for the specified media item id.

<details><summary>Parameters</summary>

### mediaItemId (required)

Identifier of media item to be requested.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## get_shared_album

Returns the album based on the specified shareToken.

<details><summary>Parameters</summary>

### shareToken (required)

Share token of the album to be request.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## join_shared_album

Joins a shared album on behalf of the Google Photos user.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "shareToken" : "Token to join the shared album on behalf of the user."
}
```

</details>

## list_albums

Lists all albums shown to a user in the Albums tab of the Google Photos app.

<details><summary>Parameters</summary>

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### excludeNonAppCreatedData

If set, the results exclude media items that were not created by this app. Defaults to false (all albums are returned). This field is ignored if the photoslibrary.readonly.appcreateddata scope is used.

**Type:** boolean

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## list_media_items

List all media items from a user's Google Photos library.

<details><summary>Parameters</summary>

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### excludeNonAppCreatedData

If set, the results exclude media items that were not created by this app. Defaults to false (all albums are returned). This field is ignored if the photoslibrary.readonly.appcreateddata scope is used.

**Type:** boolean

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## list_shared_albums

Lists all shared albums available in the Sharing tab of the user's Google Photos app..

<details><summary>Parameters</summary>

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### excludeNonAppCreatedData

If set, the results exclude media items that were not created by this app. Defaults to false (all albums are returned). This field is ignored if the photoslibrary.readonly.appcreateddata scope is used.

**Type:** boolean

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## search_media_items

Searches for media items in a user's Google Photos library. If no filters are set, then all media items in the user's library are returned. If an album is set, all media items in the specified album are returned. If filters are specified, media items that match the filters from the user's library are listed. If you set both the album and the filters, the request results in an error.

<details><summary>Parameters</summary>

### $body

The album to be created.

**Type:** object

```json
{
  "albumId" : "Identifier of an album. If populated, lists all media items in specified album. Can't set in conjunction with any filters.",
  "pageSize" : "Maximum number of media items to return in the response",
  "pageToken" : "A continuation token to get the next page of the results. Adding this to the request returns the rows after the pageToken. The pageToken should be the value returned in the nextPageToken parameter in the response to the searchMediaItems request.",
  "filters" : {
    "excludeNonAppCreatedData" : "If set, the results exclude media items that were not created by this app. Defaults to false (all media items are returned). This field is ignored if the photoslibrary.readonly.appcreateddata scope is used.",
    "contentFilter" : {
      "excludedContentCategories" : [ "schema_type_none" ],
      "includedContentCategories" : [ "schema_type_none" ]
    },
    "mediaTypeFilter" : {
      "mediaTypes" : [ "schema_type_none" ]
    },
    "dateFilter" : {
      "ranges" : [ {
        "endDate" : {
          "month" : "Month of year. Must be from 1 to 12, or 0 if specifying a date without a month.",
          "year" : "Year of date. Must be from 1 to 9999, or 0 if specifying a date without a year.",
          "day" : "Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a year/month where the day isn't significant."
        },
        "startDate" : {
          "month" : "Month of year. Must be from 1 to 12, or 0 if specifying a date without a month.",
          "year" : "Year of date. Must be from 1 to 9999, or 0 if specifying a date without a year.",
          "day" : "Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a year/month where the day isn't significant."
        }
      } ],
      "dates" : [ {
        "month" : "Month of year. Must be from 1 to 12, or 0 if specifying a date without a month.",
        "year" : "Year of date. Must be from 1 to 9999, or 0 if specifying a date without a year.",
        "day" : "Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a year/month where the day isn't significant."
      } ]
    },
    "includeArchivedMedia" : "If set, the results include media items that the user has archived. Defaults to false (archived media items aren't included)."
  }
}
```

### body

**Type:** STRING

</details>

## share_album

Marks an album as shared and accessible to other users. This action can only be performed on albums which were created by the developer via the API.

<details><summary>Parameters</summary>

### albumId (required)

Identifier of the album to be requested.

**Type:** string

### $body

Options to be set when converting the album to a shared album.

**Type:** object

```json
{
  "sharedAlbumOptions" : {
    "isCommentable" : "True if the shared album allows the owner and the collaborators (users who have joined the album) to add comments to the album. Defaults to false.",
    "isCollaborative" : "True if the shared album allows collaborators (users who have joined the album) to add media items to it. Defaults to false."
  }
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

