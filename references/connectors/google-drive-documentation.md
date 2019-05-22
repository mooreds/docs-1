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

#### fileId (required)

The ID of the file.

**Type:** string

#### $body

The metadata for a file.

**Type:** object

#### ignoreDefaultVisibility

Whether to ignore the domain's default visibility settings for the created file. Domain administrators can choose to make all uploaded files visible to the domain by default; this parameter bypasses that behavior for the request. Permissions are still inherited from parent folders.

**Type:** boolean

#### keepRevisionForever

Whether to set the 'keepForever' field in the new head revision. This is only applicable to files with binary content in Drive.

**Type:** boolean

#### ocrLanguage

A language hint for OCR processing during image import (ISO 639-1 code).

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

</details>

## create_comment

Creates a new comment on a file.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### $body

A comment on a file.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

</details>

## create_comment_reply

Creates a new reply to a comment.

<details><summary>Parameters</summary>

#### commentId (required)

The ID of the comment.

**Type:** string

#### fileId (required)

The ID of the file.

**Type:** string

#### $body

A reply to a comment on a file.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## create_permission

Creates a permission for a file or Team Drive.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file or Team Drive.

**Type:** string

#### $body

A permission for a file. A permission grants a user, group, domain or the world access to a file or a folder hierarchy.

**Type:** object

#### emailMessage

A plain text custom message to include in the notification email.

**Type:** string

#### sendNotificationEmail

Whether to send a notification email when sharing to users or groups. This defaults to true for users and groups, and is not allowed for other requests. It must not be disabled for ownership transfers.

**Type:** boolean

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

#### transferOwnership

Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect.

**Type:** boolean

#### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the item belongs.

**Type:** boolean

</details>

## create_team_drive

Creates a new Team Drive.

<details><summary>Parameters</summary>

#### requestId (required)

An ID, such as a random UUID, which uniquely identifies this user's request for idempotent creation of a Team Drive. A repeated request by the same user and with the same request ID will avoid creating duplicates by attempting to create the same Team Drive. If the Team Drive already exists a 409 error will be returned.

**Type:** string

#### $body

Representation of a Team Drive.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## delete_comment

Deletes a comment.

<details><summary>Parameters</summary>

#### commentId (required)

The ID of the comment.

**Type:** string

#### fileId (required)

The ID of the file.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## delete_comment_reply

Deletes a reply.

<details><summary>Parameters</summary>

#### commentId (required)

The ID of the comment.

**Type:** string

#### fileId (required)

The ID of the file.

**Type:** string

#### replyId (required)

The ID of the reply.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## delete_file

Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a Team Drive the user must be an organizer on the parent. If the target is a folder, all descendants owned by the user are also deleted.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

</details>

## delete_permission

Deletes a permission.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file or Team Drive.

**Type:** string

#### permissionId (required)

The ID of the permission.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

#### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the item belongs.

**Type:** boolean

</details>

## delete_revision

Permanently deletes a revision. This method is only applicable to files with binary content in Drive.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### revisionId (required)

The ID of the revision.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## delete_team_drive

Permanently deletes a Team Drive for which the user is an organizer. The Team Drive cannot contain any untrashed items.

<details><summary>Parameters</summary>

#### teamDriveId (required)

The ID of the Team Drive

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## empty_trash

Permanently deletes all of the user's trashed files.

<details><summary>Parameters</summary>

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## export_file

Exports a Google Doc to the requested MIME type and returns the exported content. Please note that the exported content is limited to 10MB.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### mimeType (required)

The MIME type of the format requested for this export.

**Type:** string

</details>

## generate_ids

Generates a set of file IDs which can be provided in create requests.

<details><summary>Parameters</summary>

#### count

The number of IDs to return.

**Type:** integer

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### space

The space in which the IDs can be used to create new files. Supported values are 'drive' and 'appDataFolder'.

**Type:** string

</details>

## get_about_drive

Gets information about the user, the user's Drive, and system capabilities.

<details><summary>Parameters</summary>

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## get_comment

Gets a comment by ID.

<details><summary>Parameters</summary>

#### commentId (required)

The ID of the comment.

**Type:** string

#### fileId (required)

The ID of the file.

**Type:** string

#### includeDeleted

Whether to return deleted comments. Deleted comments will not include their original content.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## get_comment_reply

Gets a reply by ID.

<details><summary>Parameters</summary>

#### commentId (required)

The ID of the comment.

**Type:** string

#### fileId (required)

The ID of the file.

**Type:** string

#### replyId (required)

The ID of the reply.

**Type:** string

#### includeDeleted

Whether to return deleted replies. Deleted replies will not include their original content.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## get_file

Gets a file's metadata or content by ID.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### acknowledgeAbuse

Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

</details>

## get_permission

Gets a permission by ID.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### permissionId (required)

The ID of the permission.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

#### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the item belongs.

**Type:** boolean

</details>

## get_revision

Gets a revision's metadata or content by ID.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### revisionId (required)

The ID of the revision.

**Type:** string

#### acknowledgeAbuse

Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## get_start_page_token

Gets the starting pageToken for listing future changes.

<details><summary>Parameters</summary>

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

#### teamDriveId

The ID of the Team Drive for which the starting pageToken for listing future changes from that Team Drive will be returned.

**Type:** string

</details>

## get_team_drive

Gets a Team Drive's metadata by ID.

<details><summary>Parameters</summary>

#### teamDriveId (required)

The ID of the Team Drive

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the Team Drive belongs.

**Type:** boolean

</details>

## list_changes

Lists the changes for a user or Team Drive.

<details><summary>Parameters</summary>

#### includeCorpusRemovals

Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.

**Type:** boolean

#### includeRemoved

Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access.

**Type:** boolean

#### includeTeamDriveItems

Whether Team Drive files or changes should be included in results.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### restrictToMyDrive

Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive.

**Type:** boolean

#### spaces

A comma-separated list of spaces to query within the user corpus. Supported values are 'drive', 'appDataFolder' and 'photos'.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

#### teamDriveId

The Team Drive from which changes will be returned. If specified the change IDs will be reflective of the Team Drive; use the combined Team Drive ID and change ID as an identifier.

**Type:** string

</details>

## list_comment_replies

Lists a comment's replies.

<details><summary>Parameters</summary>

#### commentId (required)

The ID of the comment.

**Type:** string

#### fileId (required)

The ID of the file.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### includeDeleted

Whether to include deleted replies. Deleted replies will not include their original content.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## list_comments

Lists a file's comments.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### includeDeleted

Whether to include deleted comments. Deleted comments will not include their original content.

**Type:** boolean

#### startModifiedTime

The minimum value of 'modifiedTime' for the result comments (RFC 3339 date-time).

**Type:** string

</details>

## list_files

Lists or searches files.

<details><summary>Parameters</summary>

#### corpora

Comma-separated list of bodies of items (files/documents) to which the query applies. Supported bodies are 'user', 'domain', 'teamDrive' and 'allTeamDrives'. 'allTeamDrives' must be combined with 'user'; all other values must be used in isolation. Prefer 'user' or 'teamDrive' to 'allTeamDrives' for efficiency.

**Type:** string

#### corpus

The source of files to list. Deprecated: use 'corpora' instead.

**Type:** string

**Potential values:** domain, user

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### includeTeamDriveItems

Whether Team Drive items should be included in results.

**Type:** boolean

#### orderBy

A comma-separated list of sort keys. Valid keys are 'createdTime', 'folder', 'modifiedByMeTime', 'modifiedTime', 'name', 'name_natural', 'quotaBytesUsed', 'recency', 'sharedWithMeTime', 'starred', and 'viewedByMeTime'. Each key sorts ascending by default, but may be reversed with the 'desc' modifier. Example usage: ?orderBy=folder,modifiedTime desc,name. Please note that there is a current limitation for users with approximately one million files in which the requested sort order is ignored.

**Type:** string

#### q

A query for filtering the file results. See the "Search for Files" guide for supported syntax.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### spaces

A comma-separated list of spaces to query within the corpus. Supported values are 'drive', 'appDataFolder' and 'photos'.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

#### teamDriveId

ID of Team Drive to search.

**Type:** string

</details>

## list_permissions

Lists a file's or Team Drive's permissions.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file or Team Drive.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

#### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the item belongs.

**Type:** boolean

</details>

## list_revisions

Lists a file's revisions.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## list_team_drives

Lists the user's Team Drives.

<details><summary>Parameters</summary>

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### q

Query string for searching Team Drives.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then all Team Drives of the domain in which the requester is an administrator are returned.

**Type:** boolean

</details>

## stop_channels

Stop watching resources through this channel

<details><summary>Parameters</summary>

#### $body

An notification channel used to watch for resource changes.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## update_comment

Updates a comment with patch semantics.

<details><summary>Parameters</summary>

#### commentId (required)

The ID of the comment.

**Type:** string

#### fileId (required)

The ID of the file.

**Type:** string

#### $body

A comment on a file.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## update_comment_reply

Updates a reply with patch semantics.

<details><summary>Parameters</summary>

#### commentId (required)

The ID of the comment.

**Type:** string

#### fileId (required)

The ID of the file.

**Type:** string

#### replyId (required)

The ID of the reply.

**Type:** string

#### $body

A reply to a comment on a file.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## update_permission

Updates a permission with patch semantics.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file or Team Drive.

**Type:** string

#### permissionId (required)

The ID of the permission.

**Type:** string

#### $body

A permission for a file. A permission grants a user, group, domain or the world access to a file or a folder hierarchy.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### removeExpiration

Whether to remove the expiration date.

**Type:** boolean

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

#### transferOwnership

Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect.

**Type:** boolean

#### useDomainAdminAccess

Whether the request should be treated as if it was issued by a domain administrator; if set to true, then the requester will be granted access if they are an administrator of the domain to which the item belongs.

**Type:** boolean

</details>

## update_revision

Updates a revision with patch semantics.

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### revisionId (required)

The ID of the revision.

**Type:** string

#### $body

The metadata for a revision to a file.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## update_team_drive

Updates a Team Drive's metadata

<details><summary>Parameters</summary>

#### teamDriveId (required)

The ID of the Team Drive

**Type:** string

#### $body

Representation of a Team Drive.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

</details>

## watch_changes

Subscribes to changes for a user.

<details><summary>Parameters</summary>

#### pageToken (required)

The token for continuing a previous list request on the next page. This should be set to the value of 'nextPageToken' from the previous response or to the response from the getStartPageToken method.

**Type:** string

#### $body

An notification channel used to watch for resource changes.

**Type:** object

#### includeCorpusRemovals

Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.

**Type:** boolean

#### includeRemoved

Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access.

**Type:** boolean

#### includeTeamDriveItems

Whether Team Drive files or changes should be included in results.

**Type:** boolean

#### pageSize

The maximum number of changes to return per page.

**Type:** integer

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### restrictToMyDrive

Whether to restrict the results to changes inside the My Drive hierarchy. This omits changes to files such as those in the Application Data folder or shared files which have not been added to My Drive.

**Type:** boolean

#### spaces

A comma-separated list of spaces to query within the user corpus. Supported values are 'drive', 'appDataFolder' and 'photos'.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

#### teamDriveId

The Team Drive from which changes will be returned. If specified the change IDs will be reflective of the Team Drive; use the combined Team Drive ID and change ID as an identifier.

**Type:** string

</details>

## watch_drive_files

Subscribes to changes to a file

<details><summary>Parameters</summary>

#### fileId (required)

The ID of the file.

**Type:** string

#### $body

An notification channel used to watch for resource changes.

**Type:** object

#### acknowledgeAbuse

Whether the user is acknowledging the risk of downloading known malware or other abusive files. This is only applicable when alt=media.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.

**Type:** string

#### supportsTeamDrives

Whether the requesting application supports Team Drives.

**Type:** boolean

</details>

