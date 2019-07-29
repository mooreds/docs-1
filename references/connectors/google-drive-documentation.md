---
id: google-drive-documentation
title: Google Drive (version v2.*.*)
sidebar_label: Google Drive
layout: docs.mustache
---

Google Drive Integration

## copy_file

Creates a copy of a file and applies any requested updates with patch semantics.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

**Type:** string

### $body

The metadata for a file.

**Type:** object

```json
{
  "modifiedTime" : "The last time the file was modified by anyone (RFC 3339 date-time).\nNote that setting modifiedTime will also update modifiedByMeTime for the user.",
  "owners" : [ {
    "permissionId" : "The user's ID as visible in Permission resources.",
    "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
    "displayName" : "A plain text displayable name for this user.",
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
    "me" : "Whether this user is the requesting user.",
    "photoLink" : "A link to the user's profile photo, if available."
  } ],
  "mimeType" : "The MIME type of the file.\nDrive will attempt to automatically detect an appropriate value from uploaded content if no value is provided. The value cannot be changed unless a new revision is uploaded.\nIf a file is created with a Google Doc MIME type, the uploaded content will be imported if possible. The supported import formats are published in the About resource.",
  "iconLink" : "A static, unauthenticated link to the file's icon.",
  "starred" : "Whether the user has starred the file.",
  "permissions" : [ {
    "emailAddress" : "The email address of the user or group to which this permission refers.",
    "teamDrivePermissionDetails" : [ {
      "role" : "The primary role for this user. While new values may be added in the future, the following are currently possible:  \n- organizer \n- writer \n- commenter \n- reader",
      "inherited" : "Whether this permission is inherited. This field is always populated. This is an output-only field.",
      "inheritedFrom" : "The ID of the item from which this permission is inherited. This is an output-only field and is only populated for members of the Team Drive.",
      "teamDrivePermissionType" : "The Team Drive permission type for this user. While new values may be added in future, the following are currently possible:  \n- file \n- member"
    } ],
    "deleted" : "Whether the account associated with this permission has been deleted. This field only pertains to user and group permissions.",
    "role" : "The role granted by this permission. While new values may be supported in the future, the following are currently allowed:  \n- organizer \n- owner \n- writer \n- commenter \n- reader",
    "displayName" : "A displayable name for users, groups or domains.",
    "expirationTime" : "The time at which this permission will expire (RFC 3339 date-time). Expiration times have the following restrictions:  \n- They can only be set on user and group permissions \n- The time must be in the future \n- The time cannot be more than a year in the future",
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#permission\".",
    "domain" : "The domain to which this permission refers.",
    "id" : "The ID of this permission. This is a unique identifier for the grantee, and is published in User resources as permissionId.",
    "photoLink" : "A link to the user's profile photo, if available.",
    "type" : "The type of the grantee. Valid values are:  \n- user \n- group \n- domain \n- anyone",
    "allowFileDiscovery" : "Whether the permission allows the file to be discovered through search. This is only applicable for permissions of type domain or anyone."
  } ],
  "modifiedByMe" : "Whether the file has been modified by this user.",
  "contentHints" : {
    "thumbnail" : {
      "image" : "The thumbnail data encoded with URL-safe Base64 (RFC 4648 section 5).",
      "mimeType" : "The MIME type of the thumbnail."
    },
    "indexableText" : "Text to be indexed for the file to improve fullText queries. This is limited to 128KB in length and may contain HTML elements."
  },
  "isAppAuthorized" : "Whether the file was created or opened by the requesting app.",
  "createdTime" : "The time at which the file was created (RFC 3339 date-time).",
  "id" : "The ID of the file.",
  "sharedWithMeTime" : "The time at which the file was shared with the user, if applicable (RFC 3339 date-time).",
  "writersCanShare" : "Whether users with only writer permission can modify the file's permissions. Not populated for Team Drive files.",
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#file\".",
  "viewersCanCopyContent" : "Whether users with only reader or commenter permission can copy the file's content. This affects copy, download, and print operations.",
  "webViewLink" : "A link for opening the file in a relevant Google editor or viewer in a browser.",
  "ownedByMe" : "Whether the user owns the file. Not populated for Team Drive files.",
  "version" : "A monotonically increasing version number for the file. This reflects every change made to the file on the server, even those not visible to the user.",
  "explicitlyTrashed" : "Whether the file has been explicitly trashed, as opposed to recursively trashed from a parent folder.",
  "trashedTime" : "The time that the item was trashed (RFC 3339 date-time). Only populated for Team Drive files.",
  "viewedByMe" : "Whether the file has been viewed by this user.",
  "size" : "The size of the file's content in bytes. This is only applicable to files with binary content in Drive.",
  "imageMediaMetadata" : {
    "meteringMode" : "The metering mode used to create the photo.",
    "exposureTime" : "The length of the exposure, in seconds.",
    "whiteBalance" : "The white balance mode used to create the photo.",
    "rotation" : "The rotation in clockwise degrees from the image's original orientation.",
    "maxApertureValue" : "The smallest f-number of the lens at the focal length used to create the photo (APEX value).",
    "lens" : "The lens used to create the photo.",
    "exposureBias" : "The exposure bias of the photo (APEX value).",
    "colorSpace" : "The color space of the photo.",
    "aperture" : "The aperture used to create the photo (f-number).",
    "flashUsed" : "Whether a flash was used to create the photo.",
    "subjectDistance" : "The distance to the subject of the photo, in meters.",
    "cameraModel" : "The model of the camera used to create the photo.",
    "width" : "The width of the image in pixels.",
    "isoSpeed" : "The ISO speed used to create the photo.",
    "location" : {
      "altitude" : "The altitude stored in the image.",
      "latitude" : "The latitude stored in the image.",
      "longitude" : "The longitude stored in the image."
    },
    "sensor" : "The type of sensor used to create the photo.",
    "time" : "The date and time the photo was taken (EXIF DateTime).",
    "cameraMake" : "The make of the camera used to create the photo.",
    "exposureMode" : "The exposure mode used to create the photo.",
    "focalLength" : "The focal length used to create the photo, in millimeters.",
    "height" : "The height of the image in pixels."
  },
  "name" : "The name of the file. This is not necessarily unique within a folder. Note that for immutable items such as the top level folders of Team Drives, My Drive root folder, and Application Data folder the name is constant.",
  "spaces" : [ "string" ],
  "appProperties" : "A collection of arbitrary key-value pairs which are private to the requesting app.\nEntries with null values are cleared in update and copy requests.",
  "folderColorRgb" : "The color for a folder as an RGB hex string. The supported colors are published in the folderColorPalette field of the About resource.\nIf an unsupported color is specified, the closest color in the palette will be used instead.",
  "headRevisionId" : "The ID of the file's head revision. This is currently only available for files with binary content in Drive.",
  "parents" : [ "string" ],
  "teamDriveId" : "ID of the Team Drive the file resides in.",
  "trashed" : "Whether the file has been trashed, either explicitly or from a trashed parent folder. Only the owner may trash a file, and other users cannot see files in the owner's trash.",
  "modifiedByMeTime" : "The last time the file was modified by the user (RFC 3339 date-time).",
  "shared" : "Whether the file has been shared. Not populated for Team Drive files.",
  "hasAugmentedPermissions" : "Whether any users are granted file access directly on this file. This field is only populated for Team Drive files.",
  "description" : "A short description of the file.",
  "trashingUser" : {
    "permissionId" : "The user's ID as visible in Permission resources.",
    "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
    "displayName" : "A plain text displayable name for this user.",
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
    "me" : "Whether this user is the requesting user.",
    "photoLink" : "A link to the user's profile photo, if available."
  },
  "permissionIds" : [ "string" ],
  "thumbnailLink" : "A short-lived link to the file's thumbnail, if available. Typically lasts on the order of hours. Only populated when the requesting app can access the file's content.",
  "quotaBytesUsed" : "The number of storage quota bytes used by the file. This includes the head revision as well as previous revisions with keepForever enabled.",
  "lastModifyingUser" : {
    "permissionId" : "The user's ID as visible in Permission resources.",
    "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
    "displayName" : "A plain text displayable name for this user.",
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
    "me" : "Whether this user is the requesting user.",
    "photoLink" : "A link to the user's profile photo, if available."
  },
  "md5Checksum" : "The MD5 checksum for the content of the file. This is only applicable to files with binary content in Drive.",
  "fileExtension" : "The final component of fullFileExtension. This is only available for files with binary content in Drive.",
  "fullFileExtension" : "The full file extension extracted from the name field. May contain multiple concatenated extensions, such as \"tar.gz\". This is only available for files with binary content in Drive.\nThis is automatically updated when the name field changes, however it is not cleared if the new name does not contain a valid extension.",
  "webContentLink" : "A link for downloading the content of the file in a browser. This is only available for files with binary content in Drive.",
  "capabilities" : {
    "canMoveTeamDriveItem" : "Whether the current user can move this Team Drive item by changing its parent. Note that a request to change the parent for this item may still fail depending on the new parent that is being added. Only populated for Team Drive files.",
    "canReadRevisions" : "Whether the current user can read the revisions resource of this file. For a Team Drive item, whether revisions of non-folder descendants of this item, or this item itself if it is not a folder, can be read.",
    "canEdit" : "Whether the current user can edit this file.",
    "canShare" : "Whether the current user can modify the sharing settings for this file.",
    "canRename" : "Whether the current user can rename this file.",
    "canAddChildren" : "Whether the current user can add children to this folder. This is always false when the item is not a folder.",
    "canListChildren" : "Whether the current user can list the children of this folder. This is always false when the item is not a folder.",
    "canTrash" : "Whether the current user can move this file to trash.",
    "canMoveItemIntoTeamDrive" : "Whether the current user can move this item into a Team Drive. If the item is in a Team Drive, this field is equivalent to canMoveTeamDriveItem.",
    "canRemoveChildren" : "Whether the current user can remove children from this folder. This is always false when the item is not a folder.",
    "canCopy" : "Whether the current user can copy this file. For a Team Drive item, whether the current user can copy non-folder descendants of this item, or this item itself if it is not a folder.",
    "canChangeViewersCanCopyContent" : "Whether the current user can change whether viewers can copy the contents of this file.",
    "canDownload" : "Whether the current user can download this file.",
    "canDelete" : "Whether the current user can delete this file.",
    "canComment" : "Whether the current user can comment on this file.",
    "canUntrash" : "Whether the current user can restore this file from trash.",
    "canReadTeamDrive" : "Whether the current user can read the Team Drive to which this file belongs. Only populated for Team Drive files."
  },
  "hasThumbnail" : "Whether this file has a thumbnail. This does not indicate whether the requesting app has access to the thumbnail. To check access, look for the presence of the thumbnailLink field.",
  "viewedByMeTime" : "The last time the file was viewed by the user (RFC 3339 date-time).",
  "videoMediaMetadata" : {
    "width" : "The width of the video in pixels.",
    "durationMillis" : "The duration of the video in milliseconds.",
    "height" : "The height of the video in pixels."
  },
  "thumbnailVersion" : "The thumbnail version for use in thumbnail cache invalidation.",
  "sharingUser" : {
    "permissionId" : "The user's ID as visible in Permission resources.",
    "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
    "displayName" : "A plain text displayable name for this user.",
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
    "me" : "Whether this user is the requesting user.",
    "photoLink" : "A link to the user's profile photo, if available."
  },
  "originalFilename" : "The original filename of the uploaded content if available, or else the original value of the name field. This is only available for files with binary content in Drive.",
  "properties" : "A collection of arbitrary key-value pairs which are visible to all apps.\nEntries with null values are cleared in update and copy requests."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### ignoreDefaultVisibility

Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.

**Type:** boolean

### keepRevisionForever

Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Drive.

**Type:** boolean

### ocrLanguage

A language hint for OCR processing during image import (ISO 639-1 code).

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## create_comment

Creates a new comment on a file.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

**Type:** string

### $body

A comment on a file.

**Type:** object

```json
{
  "modifiedTime" : "The last time the comment or any of its replies was modified (RFC 3339 date-time).",
  "deleted" : "Whether the comment has been deleted. A deleted comment has no content.",
  "replies" : [ {
    "modifiedTime" : "The last time the reply was modified (RFC 3339 date-time).",
    "deleted" : "Whether the reply has been deleted. A deleted reply has no content.",
    "author" : {
      "permissionId" : "The user's ID as visible in Permission resources.",
      "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
      "displayName" : "A plain text displayable name for this user.",
      "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
      "me" : "Whether this user is the requesting user.",
      "photoLink" : "A link to the user's profile photo, if available."
    },
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#reply\".",
    "action" : "The action the reply performed to the parent comment. Valid values are:  \n- resolve \n- reopen",
    "createdTime" : "The time at which the reply was created (RFC 3339 date-time).",
    "id" : "The ID of the reply.",
    "content" : "The plain text content of the reply. This field is used for setting the content, while htmlContent should be displayed. This is required on creates if no action is specified.",
    "htmlContent" : "The content of the reply with HTML formatting."
  } ],
  "author" : {
    "permissionId" : "The user's ID as visible in Permission resources.",
    "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
    "displayName" : "A plain text displayable name for this user.",
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
    "me" : "Whether this user is the requesting user.",
    "photoLink" : "A link to the user's profile photo, if available."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#comment\".",
  "anchor" : "A region of the document represented as a JSON string. See anchor documentation for details on how to define and interpret anchor properties.",
  "createdTime" : "The time at which the comment was created (RFC 3339 date-time).",
  "id" : "The ID of the comment.",
  "content" : "The plain text content of the comment. This field is used for setting the content, while htmlContent should be displayed.",
  "quotedFileContent" : {
    "mimeType" : "The MIME type of the quoted content.",
    "value" : "The quoted content itself. This is interpreted as plain text if set through the API."
  },
  "htmlContent" : "The content of the comment with HTML formatting.",
  "resolved" : "Whether the comment has been resolved by one of its replies."
}
```

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

</details>

## create_comment_reply

Creates a new reply to a comment.

<details><summary>Parameters</summary>

### commentId (required)

The ID of the comment.

**Type:** string

### fileId (required)

The ID of the file.

**Type:** string

### $body

A reply to a comment on a file.

**Type:** object

```json
{
  "modifiedTime" : "The last time the reply was modified (RFC 3339 date-time).",
  "deleted" : "Whether the reply has been deleted. A deleted reply has no content.",
  "author" : {
    "permissionId" : "The user's ID as visible in Permission resources.",
    "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
    "displayName" : "A plain text displayable name for this user.",
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
    "me" : "Whether this user is the requesting user.",
    "photoLink" : "A link to the user's profile photo, if available."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#reply\".",
  "action" : "The action the reply performed to the parent comment. Valid values are:  \n- resolve \n- reopen",
  "createdTime" : "The time at which the reply was created (RFC 3339 date-time).",
  "id" : "The ID of the reply.",
  "content" : "The plain text content of the reply. This field is used for setting the content, while htmlContent should be displayed. This is required on creates if no action is specified.",
  "htmlContent" : "The content of the reply with HTML formatting."
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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## create_permission

Creates a permission for a file or Team Drive.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file or Team Drive.

**Type:** string

### $body

A permission for a file. A permission grants a user, group, domain or the world access to a file or a folder hierarchy.

**Type:** object

```json
{
  "emailAddress" : "The email address of the user or group to which this permission refers.",
  "teamDrivePermissionDetails" : [ {
    "role" : "The primary role for this user. While new values may be added in the future, the following are currently possible:  \n- organizer \n- writer \n- commenter \n- reader",
    "inherited" : "Whether this permission is inherited. This field is always populated. This is an output-only field.",
    "inheritedFrom" : "The ID of the item from which this permission is inherited. This is an output-only field and is only populated for members of the Team Drive.",
    "teamDrivePermissionType" : "The Team Drive permission type for this user. While new values may be added in future, the following are currently possible:  \n- file \n- member"
  } ],
  "deleted" : "Whether the account associated with this permission has been deleted. This field only pertains to user and group permissions.",
  "role" : "The role granted by this permission. While new values may be supported in the future, the following are currently allowed:  \n- organizer \n- owner \n- writer \n- commenter \n- reader",
  "displayName" : "A displayable name for users, groups or domains.",
  "expirationTime" : "The time at which this permission will expire (RFC 3339 date-time). Expiration times have the following restrictions:  \n- They can only be set on user and group permissions \n- The time must be in the future \n- The time cannot be more than a year in the future",
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#permission\".",
  "domain" : "The domain to which this permission refers.",
  "id" : "The ID of this permission. This is a unique identifier for the grantee, and is published in User resources as permissionId.",
  "photoLink" : "A link to the user's profile photo, if available.",
  "type" : "The type of the grantee. Valid values are:  \n- user \n- group \n- domain \n- anyone",
  "allowFileDiscovery" : "Whether the permission allows the file to be discovered through search. This is only applicable for permissions of type domain or anyone."
}
```

### emailMessage

A plain text custom message to include in the notification email.

**Type:** string

### sendNotificationEmail

Whether to send a notification email when sharing to users or groups. This defaults to true for users and groups, and is not allowed for other requests. It must not be disabled for ownership transfers.

**Type:** boolean

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### transferOwnership

Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect.

**Type:** boolean

### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the item belongs.

**Type:** boolean

</details>

## create_team_drive

Creates a new Team Drive.

<details><summary>Parameters</summary>

### requestId (required)

An ID, such as a random UUID, which uniquely identifies this user's request for idempotent creation of a Team Drive. A repeated request by the same user and with the same request ID will avoid creating duplicates by attempting to create the same Team Drive. If the Team Drive already exists a 409 error will be returned.

**Type:** string

### $body

Representation of a Team Drive.

**Type:** object

```json
{
  "capabilities" : {
    "canChangeTeamDriveBackground" : "Whether the current user can change the background of this Team Drive.",
    "canReadRevisions" : "Whether the current user can read the revisions resource of files in this Team Drive.",
    "canDeleteTeamDrive" : "Whether the current user can delete this Team Drive. Attempting to delete the Team Drive may still fail if there are untrashed items inside the Team Drive.",
    "canEdit" : "Whether the current user can edit files in this Team Drive",
    "canShare" : "Whether the current user can share files or folders in this Team Drive.",
    "canRename" : "Whether the current user can rename files or folders in this Team Drive.",
    "canRenameTeamDrive" : "Whether the current user can rename this Team Drive.",
    "canAddChildren" : "Whether the current user can add children to folders in this Team Drive.",
    "canListChildren" : "Whether the current user can list the children of folders in this Team Drive.",
    "canManageMembers" : "Whether the current user can add members to this Team Drive or remove them or change their role.",
    "canRemoveChildren" : "Whether the current user can remove children from folders in this Team Drive.",
    "canCopy" : "Whether the current user can copy files in this Team Drive.",
    "canDownload" : "Whether the current user can download files in this Team Drive.",
    "canComment" : "Whether the current user can comment on files in this Team Drive."
  },
  "backgroundImageFile" : {
    "xCoordinate" : "The X coordinate of the upper left corner of the cropping area in the background image. This is a value in the closed range of 0 to 1. This value represents the horizontal distance from the left side of the entire image to the left side of the cropping area divided by the width of the entire image.",
    "yCoordinate" : "The Y coordinate of the upper left corner of the cropping area in the background image. This is a value in the closed range of 0 to 1. This value represents the vertical distance from the top side of the entire image to the top side of the cropping area divided by the height of the entire image.",
    "width" : "The width of the cropped image in the closed range of 0 to 1. This value represents the width of the cropped image divided by the width of the entire image. The height is computed by applying a width to height aspect ratio of 80 to 9. The resulting image must be at least 1280 pixels wide and 144 pixels high.",
    "id" : "The ID of an image file in Drive to use for the background image."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#teamDrive\".",
  "backgroundImageLink" : "A short-lived link to this Team Drive's background image.",
  "name" : "The name of this Team Drive.",
  "createdTime" : "The time at which the Team Drive was created (RFC 3339 date-time).",
  "themeId" : "The ID of the theme from which the background image and color will be set. The set of possible teamDriveThemes can be retrieved from a drive.about.get response. When not specified on a drive.teamdrives.create request, a random theme is chosen from which the background image and color are set. This is a write-only field; it can only be set on requests that don't set colorRgb or backgroundImageFile.",
  "id" : "The ID of this Team Drive which is also the ID of the top level folder for this Team Drive.",
  "colorRgb" : "The color of this Team Drive as an RGB hex string. It can only be set on a drive.teamdrives.update request that does not set themeId."
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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## delete_comment

Deletes a comment.

<details><summary>Parameters</summary>

### commentId (required)

The ID of the comment.

**Type:** string

### fileId (required)

The ID of the file.

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## delete_comment_reply

Deletes a reply.

<details><summary>Parameters</summary>

### commentId (required)

The ID of the comment.

**Type:** string

### fileId (required)

The ID of the file.

**Type:** string

### replyId (required)

The ID of the reply.

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## delete_file

Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a Team Drive the user must be an organizer on the parent. If the target is a folder, all descendants owned by the user are also deleted.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## delete_permission

Deletes a permission.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file or Team Drive.

**Type:** string

### permissionId (required)

The ID of the permission.

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the item belongs.

**Type:** boolean

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## delete_revision

Permanently deletes a revision. This method is only applicable to files with binary content in Drive.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

**Type:** string

### revisionId (required)

The ID of the revision.

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## delete_team_drive

Permanently deletes a Team Drive for which the user is an organizer. The Team Drive cannot contain any untrashed items.

<details><summary>Parameters</summary>

### teamDriveId (required)

The ID of the Team Drive

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## empty_trash

Permanently deletes all of the user's trashed files.

<details><summary>Parameters</summary>

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## export_file

Exports a Google Doc to the requested MIME type and returns the exported content. Please note that the exported content is limited to 10MB.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

**Type:** string

### mimeType (required)

The MIME type of the format requested for this export.

**Type:** string

</details>

## generate_ids

Generates a set of file IDs which can be provided in create requests.

<details><summary>Parameters</summary>

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### count

The number of IDs to return.

**Type:** integer

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### space

The space in which the IDs can be used to create new files. Supported values are 'drive' and 'appDataFolder'.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## get_about_drive

Gets information about the user, the user's Drive, and system capabilities.

<details><summary>Parameters</summary>

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## get_comment

Gets a comment by ID.

<details><summary>Parameters</summary>

### commentId (required)

The ID of the comment.

**Type:** string

### fileId (required)

The ID of the file.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeDeleted

Whether to return deleted comments. Deleted comments will not include their original content.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## get_comment_reply

Gets a reply by ID.

<details><summary>Parameters</summary>

### commentId (required)

The ID of the comment.

**Type:** string

### fileId (required)

The ID of the file.

**Type:** string

### replyId (required)

The ID of the reply.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeDeleted

Whether to return deleted replies. Deleted replies will not include their original content.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## get_file

Gets a file's metadata or content by ID.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

**Type:** string

### acknowledgeAbuse

Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.

**Type:** boolean

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## get_permission

Gets a permission by ID.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

**Type:** string

### permissionId (required)

The ID of the permission.

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the item belongs.

**Type:** boolean

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## get_revision

Gets a revision's metadata or content by ID.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

**Type:** string

### revisionId (required)

The ID of the revision.

**Type:** string

### acknowledgeAbuse

Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.

**Type:** boolean

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## get_start_page_token

Gets the starting pageToken for listing future changes.

<details><summary>Parameters</summary>

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### teamDriveId

The ID of the Team Drive for which the starting pageToken for listing future changes from that Team Drive will be returned.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## get_team_drive

Gets a Team Drive's metadata by ID.

<details><summary>Parameters</summary>

### teamDriveId (required)

The ID of the Team Drive

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the Team Drive belongs.

**Type:** boolean

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## list_changes

Lists the changes for a user or Team Drive.

<details><summary>Parameters</summary>

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeCorpusRemovals

Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.

**Type:** boolean

### includeRemoved

Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access.

**Type:** boolean

### includeTeamDriveItems

Whether Team Drive files or changes should be included in results.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### restrictToMyDrive

Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive.

**Type:** boolean

### spaces

A comma-separated list of spaces to query within the user corpus. Supported values are 'drive', 'appDataFolder' and 'photos'.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### teamDriveId

The Team Drive from which changes will be returned. If specified the change IDs will be reflective of the Team Drive; use the combined Team Drive ID and change ID as an identifier.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## list_comment_replies

Lists a comment's replies.

<details><summary>Parameters</summary>

### commentId (required)

The ID of the comment.

**Type:** string

### fileId (required)

The ID of the file.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeDeleted

Whether to include deleted replies. Deleted replies will not include their original content.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## list_comments

Lists a file's comments.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeDeleted

Whether to include deleted comments. Deleted comments will not include their original content.

**Type:** boolean

### startModifiedTime

The minimum value of 'modifiedTime' for the result comments (RFC 3339 date-time).

**Type:** string

</details>

## list_files

Lists or searches files.

<details><summary>Parameters</summary>

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### corpora

Comma-separated list of bodies of items (files/documents) to which the query applies. Supported bodies are 'user', 'domain', 'teamDrive' and 'allTeamDrives'. 'allTeamDrives' must be combined with 'user'; all other values must be used in isolation. Prefer 'user' or 'teamDrive' to 'allTeamDrives' for efficiency.

**Type:** string

### corpus

The source of files to list. Deprecated: use 'corpora' instead.

**Type:** string

**Potential values:** domain, user

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeTeamDriveItems

Whether Team Drive items should be included in results.

**Type:** boolean

### orderBy

A comma-separated list of sort keys. Valid keys are 'createdTime', 'folder', 'modifiedByMeTime', 'modifiedTime', 'name', 'name_natural', 'quotaBytesUsed', 'recency', 'sharedWithMeTime', 'starred', and 'viewedByMeTime'. Each key sorts ascending by default, but may be reversed with the 'desc' modifier. Example usage: ?orderBy=folder,modifiedTime desc,name. Please note that there is a current limitation for users with approximately one million files in which the requested sort order is ignored.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### q

A query for filtering the file results. See the "Search for Files" guide for supported syntax.

**Type:** string

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### spaces

A comma-separated list of spaces to query within the corpus. Supported values are 'drive', 'appDataFolder' and 'photos'.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### teamDriveId

ID of Team Drive to search.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## list_permissions

Lists a file's or Team Drive's permissions.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file or Team Drive.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the item belongs.

**Type:** boolean

</details>

## list_revisions

Lists a file's revisions.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## list_team_drives

Lists the user's Team Drives.

<details><summary>Parameters</summary>

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

### q

Query string for searching Team Drives.

**Type:** string

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then all Team Drives of the domain in which the requester is an administrator are returned.

**Type:** boolean

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## stop_channels

Stop watching resources through this channel

<details><summary>Parameters</summary>

### $body

An notification channel used to watch for resource changes.

**Type:** object

```json
{
  "resourceId" : "An opaque ID that identifies the resource being watched on this channel. Stable across different API versions.",
  "address" : "The address where notifications are delivered for this channel.",
  "payload" : "A Boolean value to indicate whether payload is wanted. Optional.",
  "kind" : "Identifies this as a notification channel used to watch for changes to a resource. Value: the fixed string \"api#channel\".",
  "expiration" : "Date and time of notification channel expiration, expressed as a Unix timestamp, in milliseconds. Optional.",
  "id" : "A UUID or similar unique string that identifies this channel.",
  "resourceUri" : "A version-specific identifier for the watched resource.",
  "params" : "Additional parameters controlling delivery channel behavior. Optional.",
  "type" : "The type of delivery mechanism used for this channel.",
  "token" : "An arbitrary string delivered to the target address with each notification delivered over this channel. Optional."
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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## update_comment

Updates a comment with patch semantics.

<details><summary>Parameters</summary>

### commentId (required)

The ID of the comment.

**Type:** string

### fileId (required)

The ID of the file.

**Type:** string

### $body

A comment on a file.

**Type:** object

```json
{
  "modifiedTime" : "The last time the comment or any of its replies was modified (RFC 3339 date-time).",
  "deleted" : "Whether the comment has been deleted. A deleted comment has no content.",
  "replies" : [ {
    "modifiedTime" : "The last time the reply was modified (RFC 3339 date-time).",
    "deleted" : "Whether the reply has been deleted. A deleted reply has no content.",
    "author" : {
      "permissionId" : "The user's ID as visible in Permission resources.",
      "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
      "displayName" : "A plain text displayable name for this user.",
      "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
      "me" : "Whether this user is the requesting user.",
      "photoLink" : "A link to the user's profile photo, if available."
    },
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#reply\".",
    "action" : "The action the reply performed to the parent comment. Valid values are:  \n- resolve \n- reopen",
    "createdTime" : "The time at which the reply was created (RFC 3339 date-time).",
    "id" : "The ID of the reply.",
    "content" : "The plain text content of the reply. This field is used for setting the content, while htmlContent should be displayed. This is required on creates if no action is specified.",
    "htmlContent" : "The content of the reply with HTML formatting."
  } ],
  "author" : {
    "permissionId" : "The user's ID as visible in Permission resources.",
    "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
    "displayName" : "A plain text displayable name for this user.",
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
    "me" : "Whether this user is the requesting user.",
    "photoLink" : "A link to the user's profile photo, if available."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#comment\".",
  "anchor" : "A region of the document represented as a JSON string. See anchor documentation for details on how to define and interpret anchor properties.",
  "createdTime" : "The time at which the comment was created (RFC 3339 date-time).",
  "id" : "The ID of the comment.",
  "content" : "The plain text content of the comment. This field is used for setting the content, while htmlContent should be displayed.",
  "quotedFileContent" : {
    "mimeType" : "The MIME type of the quoted content.",
    "value" : "The quoted content itself. This is interpreted as plain text if set through the API."
  },
  "htmlContent" : "The content of the comment with HTML formatting.",
  "resolved" : "Whether the comment has been resolved by one of its replies."
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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## update_comment_reply

Updates a reply with patch semantics.

<details><summary>Parameters</summary>

### commentId (required)

The ID of the comment.

**Type:** string

### fileId (required)

The ID of the file.

**Type:** string

### replyId (required)

The ID of the reply.

**Type:** string

### $body

A reply to a comment on a file.

**Type:** object

```json
{
  "modifiedTime" : "The last time the reply was modified (RFC 3339 date-time).",
  "deleted" : "Whether the reply has been deleted. A deleted reply has no content.",
  "author" : {
    "permissionId" : "The user's ID as visible in Permission resources.",
    "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
    "displayName" : "A plain text displayable name for this user.",
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
    "me" : "Whether this user is the requesting user.",
    "photoLink" : "A link to the user's profile photo, if available."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#reply\".",
  "action" : "The action the reply performed to the parent comment. Valid values are:  \n- resolve \n- reopen",
  "createdTime" : "The time at which the reply was created (RFC 3339 date-time).",
  "id" : "The ID of the reply.",
  "content" : "The plain text content of the reply. This field is used for setting the content, while htmlContent should be displayed. This is required on creates if no action is specified.",
  "htmlContent" : "The content of the reply with HTML formatting."
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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## update_permission

Updates a permission with patch semantics.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file or Team Drive.

**Type:** string

### permissionId (required)

The ID of the permission.

**Type:** string

### $body

A permission for a file. A permission grants a user, group, domain or the world access to a file or a folder hierarchy.

**Type:** object

```json
{
  "emailAddress" : "The email address of the user or group to which this permission refers.",
  "teamDrivePermissionDetails" : [ {
    "role" : "The primary role for this user. While new values may be added in the future, the following are currently possible:  \n- organizer \n- writer \n- commenter \n- reader",
    "inherited" : "Whether this permission is inherited. This field is always populated. This is an output-only field.",
    "inheritedFrom" : "The ID of the item from which this permission is inherited. This is an output-only field and is only populated for members of the Team Drive.",
    "teamDrivePermissionType" : "The Team Drive permission type for this user. While new values may be added in future, the following are currently possible:  \n- file \n- member"
  } ],
  "deleted" : "Whether the account associated with this permission has been deleted. This field only pertains to user and group permissions.",
  "role" : "The role granted by this permission. While new values may be supported in the future, the following are currently allowed:  \n- organizer \n- owner \n- writer \n- commenter \n- reader",
  "displayName" : "A displayable name for users, groups or domains.",
  "expirationTime" : "The time at which this permission will expire (RFC 3339 date-time). Expiration times have the following restrictions:  \n- They can only be set on user and group permissions \n- The time must be in the future \n- The time cannot be more than a year in the future",
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#permission\".",
  "domain" : "The domain to which this permission refers.",
  "id" : "The ID of this permission. This is a unique identifier for the grantee, and is published in User resources as permissionId.",
  "photoLink" : "A link to the user's profile photo, if available.",
  "type" : "The type of the grantee. Valid values are:  \n- user \n- group \n- domain \n- anyone",
  "allowFileDiscovery" : "Whether the permission allows the file to be discovered through search. This is only applicable for permissions of type domain or anyone."
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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### removeExpiration

Whether to remove the expiration date.

**Type:** boolean

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### transferOwnership

Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect.

**Type:** boolean

### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the item belongs.

**Type:** boolean

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## update_revision

Updates a revision with patch semantics.

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

**Type:** string

### revisionId (required)

The ID of the revision.

**Type:** string

### $body

The metadata for a revision to a file.

**Type:** object

```json
{
  "lastModifyingUser" : {
    "permissionId" : "The user's ID as visible in Permission resources.",
    "emailAddress" : "The email address of the user. This may not be present in certain contexts if the user has not made their email address visible to the requester.",
    "displayName" : "A plain text displayable name for this user.",
    "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#user\".",
    "me" : "Whether this user is the requesting user.",
    "photoLink" : "A link to the user's profile photo, if available."
  },
  "md5Checksum" : "The MD5 checksum of the revision's content. This is only applicable to files with binary content in Drive.",
  "modifiedTime" : "The last time the revision was modified (RFC 3339 date-time).",
  "size" : "The size of the revision's content in bytes. This is only applicable to files with binary content in Drive.",
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#revision\".",
  "publishedOutsideDomain" : "Whether this revision is published outside the domain. This is only applicable to Google Docs.",
  "keepForever" : "Whether to keep this revision forever, even if it is no longer the head revision. If not set, the revision will be automatically purged 30 days after newer content is uploaded. This can be set on a maximum of 200 revisions for a file.\nThis field is only applicable to files with binary content in Drive.",
  "publishAuto" : "Whether subsequent revisions will be automatically republished. This is only applicable to Google Docs.",
  "id" : "The ID of the revision.",
  "mimeType" : "The MIME type of the revision.",
  "published" : "Whether this revision is published. This is only applicable to Google Docs.",
  "originalFilename" : "The original filename used to create this revision. This is only applicable to files with binary content in Drive."
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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## update_team_drive

Updates a Team Drive's metadata

<details><summary>Parameters</summary>

### teamDriveId (required)

The ID of the Team Drive

**Type:** string

### $body

Representation of a Team Drive.

**Type:** object

```json
{
  "capabilities" : {
    "canChangeTeamDriveBackground" : "Whether the current user can change the background of this Team Drive.",
    "canReadRevisions" : "Whether the current user can read the revisions resource of files in this Team Drive.",
    "canDeleteTeamDrive" : "Whether the current user can delete this Team Drive. Attempting to delete the Team Drive may still fail if there are untrashed items inside the Team Drive.",
    "canEdit" : "Whether the current user can edit files in this Team Drive",
    "canShare" : "Whether the current user can share files or folders in this Team Drive.",
    "canRename" : "Whether the current user can rename files or folders in this Team Drive.",
    "canRenameTeamDrive" : "Whether the current user can rename this Team Drive.",
    "canAddChildren" : "Whether the current user can add children to folders in this Team Drive.",
    "canListChildren" : "Whether the current user can list the children of folders in this Team Drive.",
    "canManageMembers" : "Whether the current user can add members to this Team Drive or remove them or change their role.",
    "canRemoveChildren" : "Whether the current user can remove children from folders in this Team Drive.",
    "canCopy" : "Whether the current user can copy files in this Team Drive.",
    "canDownload" : "Whether the current user can download files in this Team Drive.",
    "canComment" : "Whether the current user can comment on files in this Team Drive."
  },
  "backgroundImageFile" : {
    "xCoordinate" : "The X coordinate of the upper left corner of the cropping area in the background image. This is a value in the closed range of 0 to 1. This value represents the horizontal distance from the left side of the entire image to the left side of the cropping area divided by the width of the entire image.",
    "yCoordinate" : "The Y coordinate of the upper left corner of the cropping area in the background image. This is a value in the closed range of 0 to 1. This value represents the vertical distance from the top side of the entire image to the top side of the cropping area divided by the height of the entire image.",
    "width" : "The width of the cropped image in the closed range of 0 to 1. This value represents the width of the cropped image divided by the width of the entire image. The height is computed by applying a width to height aspect ratio of 80 to 9. The resulting image must be at least 1280 pixels wide and 144 pixels high.",
    "id" : "The ID of an image file in Drive to use for the background image."
  },
  "kind" : "Identifies what kind of resource this is. Value: the fixed string \"drive#teamDrive\".",
  "backgroundImageLink" : "A short-lived link to this Team Drive's background image.",
  "name" : "The name of this Team Drive.",
  "createdTime" : "The time at which the Team Drive was created (RFC 3339 date-time).",
  "themeId" : "The ID of the theme from which the background image and color will be set. The set of possible teamDriveThemes can be retrieved from a drive.about.get response. When not specified on a drive.teamdrives.create request, a random theme is chosen from which the background image and color are set. This is a write-only field; it can only be set on requests that don't set colorRgb or backgroundImageFile.",
  "id" : "The ID of this Team Drive which is also the ID of the top level folder for this Team Drive.",
  "colorRgb" : "The color of this Team Drive as an RGB hex string. It can only be set on a drive.teamdrives.update request that does not set themeId."
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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## watch_changes

Subscribes to changes for a user.

<details><summary>Parameters</summary>

### pageToken (required)

The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response or to the response from the getStartPageToken method.

**Type:** string

### $body

An notification channel used to watch for resource changes.

**Type:** object

```json
{
  "resourceId" : "An opaque ID that identifies the resource being watched on this channel. Stable across different API versions.",
  "address" : "The address where notifications are delivered for this channel.",
  "payload" : "A Boolean value to indicate whether payload is wanted. Optional.",
  "kind" : "Identifies this as a notification channel used to watch for changes to a resource. Value: the fixed string \"api#channel\".",
  "expiration" : "Date and time of notification channel expiration, expressed as a Unix timestamp, in milliseconds. Optional.",
  "id" : "A UUID or similar unique string that identifies this channel.",
  "resourceUri" : "A version-specific identifier for the watched resource.",
  "params" : "Additional parameters controlling delivery channel behavior. Optional.",
  "type" : "The type of delivery mechanism used for this channel.",
  "token" : "An arbitrary string delivered to the target address with each notification delivered over this channel. Optional."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeCorpusRemovals

Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.

**Type:** boolean

### includeRemoved

Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access.

**Type:** boolean

### includeTeamDriveItems

Whether Team Drive files or changes should be included in results.

**Type:** boolean

### pageSize

The maximum number of changes to return per page.

**Type:** integer

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### restrictToMyDrive

Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive.

**Type:** boolean

### spaces

A comma-separated list of spaces to query within the user corpus. Supported values are 'drive', 'appDataFolder' and 'photos'.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### teamDriveId

The Team Drive from which changes will be returned. If specified the change IDs will be reflective of the Team Drive; use the combined Team Drive ID and change ID as an identifier.

**Type:** string

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

## watch_drive_files

Subscribes to changes to a file

<details><summary>Parameters</summary>

### fileId (required)

The ID of the file.

**Type:** string

### $body

An notification channel used to watch for resource changes.

**Type:** object

```json
{
  "resourceId" : "An opaque ID that identifies the resource being watched on this channel. Stable across different API versions.",
  "address" : "The address where notifications are delivered for this channel.",
  "payload" : "A Boolean value to indicate whether payload is wanted. Optional.",
  "kind" : "Identifies this as a notification channel used to watch for changes to a resource. Value: the fixed string \"api#channel\".",
  "expiration" : "Date and time of notification channel expiration, expressed as a Unix timestamp, in milliseconds. Optional.",
  "id" : "A UUID or similar unique string that identifies this channel.",
  "resourceUri" : "A version-specific identifier for the watched resource.",
  "params" : "Additional parameters controlling delivery channel behavior. Optional.",
  "type" : "The type of delivery mechanism used for this channel.",
  "token" : "An arbitrary string delivered to the target address with each notification delivered over this channel. Optional."
}
```

### acknowledgeAbuse

Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.

**Type:** boolean

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

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

### userIp

IP address of the site where the request originates. Use this if you want to enforce per-user limits.

**Type:** string

</details>

