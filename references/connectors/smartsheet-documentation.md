---
id: smartsheet-documentation
title: Smartsheet (version v1.*.*)
sidebar_label: Smartsheet
layout: docs.mustache
---

## add_alternate_emails

Adds one or more alternate email addresses for the specified user.

<details><summary>Parameters</summary>

### userId (required)

**Type:** string

### $body

Array of AlternateEmail objects, each limited to only the email attribute

**Type:** object

```json
{
  "id" : "AlternateEmail Id",
  "confirmed" : "Indicates whether the alternate email address has been confirmed",
  "email" : "User's alternate email address"
}
```

</details>

## add_columns

Inserts one or more columns into the sheet specified in the URL. This operation can be performed using a simple upload or a multipart upload. For more information, see Post an Attachment.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

Column object or an array of Column objects, with the following attributes:
title
type
index (zero-based)
autoNumberFormat (optional)
description (optional)
locked (optional)
options (optional)
symbol (optional)
systemColumnType (optional)
validation (optional)
width (optional)

**Type:** object

```json
{
  "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
  "contactOptions" : [ {
    "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
    "email" : "A parsable email address."
  } ],
  "hidden" : "Indicates whether the column is hidden",
  "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
  "description" : "Column description.",
  "index" : "Column index or position. This number is zero-based.",
  "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
  "title" : "Column title",
  "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
  "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
  "autoNumberFormat" : {
    "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
    "startingNumber" : "The starting number for the auto-id",
    "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
    "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
  },
  "options" : [ "string" ],
  "width" : "Display width of the column in pixels",
  "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
  "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
  "id" : "Column Id",
  "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
  "validation" : "Indicates whether validation has been enabled for the column (value = true)",
  "primary" : "Returned only if the column is the Primary Column (value = true)"
}
```

</details>

## add_comment

Adds a comment to a discussion. 
Creating a Comment without an Attachment 
Creating a Comment with an Attachment

<details><summary>Parameters</summary>

### discussionId (required)

**Type:** string

### sheetId (required)

**Type:** string

### $body

Comment object with the following attribute:
text,Request body should contain parts with the following names:
comment: JSON Comment object with the following attribute:text
file: (optional) file to attach to the new commentSee Multipart Uploads for more information on parts.

**Type:** object

```json
{
  "createdAt" : "Time of creation",
  "attachments" : [ {
    "createdAt" : "A timestamp of when the attachment was originally added",
    "attachmentSubType" : "Attachment sub type",
    "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
    "createdBy" : { },
    "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
    "name" : "Attachment name",
    "id" : "Attachment Id",
    "mimeType" : "Attachment MIME type (PNG, etc.)",
    "sizeInKb" : "The size of the file, if the attachmentType is FILE",
    "parentId" : "The Id of the parent",
    "parentType" : "The type of object the attachment belongs to",
    "url" : "Attachment temporary URL (files only)"
  } ],
  "createdBy" : { },
  "discussionId" : "Discussion Id",
  "modifiedAt" : "Time of last modification",
  "id" : "Comment Id",
  "text" : "Comment body"
}
```

</details>

## add_favorites

Adds one or more items to the user's list of favorite items. This operation supports both single-object and bulk semantics. For more information, see Optional Bulk Operations. If called with a single Favorite object, and that favorite already exists, error code 1129 is returned. If called with an array of Favorite objects, any objects specified in the array that are already marked as favorites are ignored and omitted from the response.

<details><summary>Parameters</summary>

### $body

Favorite object or an array of Favorite objects, with the following attributes:
objectId
type

**Type:** object

```json
{
  "type" : "string. Possible values: folder | report | sheet | sight | template | workspace",
  "objectId" : "Id of the favorited item. If type is template, only private sheet-type template Id is allowed."
}
```

### allowPartialSuccess

If true, allows bulk operations to process even if one or more operations are invalid for some reason.

**Type:** boolean

</details>

## add_group_members

Adds one or more members to a group. If called with a single GroupMember object, and that group member already exists, error code 1129 is returned. If called with an array
of GroupMember objects, any users specified in the array that are already group members are ignored and omitted from the response.

<details><summary>Parameters</summary>

### groupId (required)

**Type:** string

### $body

A single GroupMember object or an array of GroupMember objects, limited to the following attribute:
email

**Type:** object

```json
{
  "firstName" : "Group member's first name",
  "lastName" : "Group member's last name",
  "name" : "Group member's full name",
  "id" : "Group member's user Id",
  "email" : "Group member's email address"
}
```

</details>

## add_image_to_cell

Uploads an image to the specified cell within a sheet.

<details><summary>Parameters</summary>

### columnId (required)

**Type:** string

### rowId (required)

**Type:** string

### sheetId (required)

**Type:** string

### $body

**Type:** object

```json
{ }
```

### altText

url-encoded alternate text for the image

**Type:** string

### overrideValidation

You may use the query string parameter overrideValidation with a value of true to allow a cell value outside of the validation limits. You must specify strict with a value of false to bypass value type checking.

**Type:** boolean

</details>

## add_rows

Inserts one or more rows into the sheet specified in the URL. If you want to insert the rows in any position but the default, use location-specifier attributes.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

Row object or an array of Row objects, with the following attributes:

One or more location-specifier attributes (optional)
expanded (optional)
format (optional)
cells (optional) -- if specified, must be an array of Cell objects, where each object is limited to the following attributes:
columnId (required)
One of the following (required):
formula: for cross-sheet formulas, you must first define a cross-sheet reference
value
When value is specified
hyperlink (optional) with exactly one of the following attributes set:
reportId
sheetId
url
linkInFromCell (optional) with all of the following attributes set:
columnId
rowId
sheetId
strict (optional)
format (optional)
image (optional) -- if specified, use to update alternate text where altText = string.
overrideValidation (optional)
locked (optional) - true to lock the row or false to unlock the row.See Column Types for more information.

NOTE:
Column Ids must be valid for the sheet to which the row belongs, and must only be used once for each row in the operation.
Cells of a project sheet in the "Finish Date" column cannot be updated via API.
Cells of a project sheet in the "Start Date" column cannot be updated via API for rows that contain a value in the "Predecessor" column.
Max length for a cell value is 4000 characters after which truncation occurs without warning. Empty string values are converted to null.
Calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = "#CIRCULAR REFERENCE". 


**Type:** object

```json
{
  "conditionalFormat" : "Describes this row's conditional format. Only returned if the include query string parameter contains format and this row has a conditional format applied.",
  "attachments" : [ {
    "createdAt" : "A timestamp of when the attachment was originally added",
    "attachmentSubType" : "Attachment sub type",
    "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
    "createdBy" : { },
    "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
    "name" : "Attachment name",
    "id" : "Attachment Id",
    "mimeType" : "Attachment MIME type (PNG, etc.)",
    "sizeInKb" : "The size of the file, if the attachmentType is FILE",
    "parentId" : "The Id of the parent",
    "parentType" : "The type of object the attachment belongs to",
    "url" : "Attachment temporary URL (files only)"
  } ],
  "indent" : "Specifies the number of levels to indent an existing row. You can specify this attribute in a request, but it is never present in a response.",
  "columns" : [ {
    "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
    "contactOptions" : [ {
      "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
      "email" : "A parsable email address."
    } ],
    "hidden" : "Indicates whether the column is hidden",
    "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
    "description" : "Column description.",
    "index" : "Column index or position. This number is zero-based.",
    "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
    "title" : "Column title",
    "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
    "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
    "autoNumberFormat" : {
      "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
      "startingNumber" : "The starting number for the auto-id",
      "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
      "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
    },
    "options" : [ "string" ],
    "width" : "Display width of the column in pixels",
    "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
    "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
    "id" : "Column Id",
    "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
    "validation" : "Indicates whether validation has been enabled for the column (value = true)",
    "primary" : "Returned only if the column is the Primary Column (value = true)"
  } ],
  "modifiedAt" : "Time of last modification",
  "discussions" : [ {
    "commentAttachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "comments" : [ {
      "createdAt" : "Time of creation",
      "attachments" : [ {
        "createdAt" : "A timestamp of when the attachment was originally added",
        "attachmentSubType" : "Attachment sub type",
        "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
        "createdBy" : { },
        "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
        "name" : "Attachment name",
        "id" : "Attachment Id",
        "mimeType" : "Attachment MIME type (PNG, etc.)",
        "sizeInKb" : "The size of the file, if the attachmentType is FILE",
        "parentId" : "The Id of the parent",
        "parentType" : "The type of object the attachment belongs to",
        "url" : "Attachment temporary URL (files only)"
      } ],
      "createdBy" : { },
      "discussionId" : "Discussion Id",
      "modifiedAt" : "Time of last modification",
      "id" : "Comment Id",
      "text" : "Comment body"
    } ],
    "accessLevel" : "User's permissions on the discussion",
    "createdBy" : { },
    "readOnly" : "Indicates whether the user can modify the discussion",
    "id" : "Discussion Id",
    "lastCommentedAt" : "Time of most recent comment",
    "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
    "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
    "parentType" : "string. Possible values: SHEET | ROW",
    "commentCount" : "The number of comments in the discussion",
    "lastCommentedUser" : {
      "lastLogin" : "Last login time of the current user",
      "lastName" : "User's last name",
      "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
      "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
      "profileImage" : {
        "altText" : "Alternate text for the image",
        "width" : "Original width (in pixels) of the uploaded image",
        "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
        "id" : "Image Id",
        "height" : "Original height (in pixels) of the uploaded image"
      },
      "firstName" : "User's first name",
      "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
      "name" : "User's full name (read-only)",
      "id" : "User Id",
      "sheetCount" : "The number of sheets owned by the current user within the organization account",
      "email" : "User's primary email address",
      "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
      "status" : "User status"
    }
  } ],
  "toBottom" : "Adds or moves the row to the bottom of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "toTop" : "Adds or moves the row to the top of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "createdAt" : "Time of creation",
  "expanded" : "Indicates whether the row is expanded or collapsed",
  "inCriticalPath" : "Only returned, with a value of true, if the sheet is a project sheet with dependencies enabled and this row is in the critical path",
  "above" : "Specifies the location for a new or moved row. You can specify this attribute in a request, but it is never present in a response.",
  "outdent" : "Specifies the number of levels to outdent an existing row. You can specify this attribute in a request, but it is never present in a response.",
  "modifiedBy" : {
    "lastLogin" : "Last login time of the current user",
    "lastName" : "User's last name",
    "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
    "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
    "profileImage" : {
      "altText" : "Alternate text for the image",
      "width" : "Original width (in pixels) of the uploaded image",
      "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
      "id" : "Image Id",
      "height" : "Original height (in pixels) of the uploaded image"
    },
    "firstName" : "User's first name",
    "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
    "name" : "User's full name (read-only)",
    "id" : "User Id",
    "sheetCount" : "The number of sheets owned by the current user within the organization account",
    "email" : "User's primary email address",
    "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
    "status" : "User status"
  },
  "id" : "Row Id",
  "locked" : "Indicates whether the row is locked. In a response, a value of true indicates that the row has been locked by the sheet owner or the admin.",
  "rowNumber" : "Row number within the sheet (1-based - starts at 1)",
  "accessLevel" : "User's permission level on the sheet that contains the row",
  "format" : "Format descriptor (see Formatting). Only returned if the include query string parameter contains format and this row has a non-default format applied.",
  "version" : "Sheet version number that is incremented every time a sheet is modified",
  "parentId" : "In a response - the Id of the parent row (if any). In a request - the Id of the desired parent row (used to specify the location for a new or moved row).",
  "cells" : [ {
    "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
    "hyperlink" : { },
    "image" : { },
    "columnId" : "The Id of the column that the cell is located in",
    "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
    "objectValue" : {
      "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
    },
    "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
    "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
    "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
    "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
    "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
    "linkInFromCell" : {
      "sheetName" : "Sheet name of the linked cell",
      "columnId" : "Column Id of the linked cell",
      "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
      "rowId" : "Row Id of the linked cell",
      "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
    },
    "value" : { },
    "linksOutToCells" : [ {
      "sheetName" : "Sheet name of the linked cell",
      "columnId" : "Column Id of the linked cell",
      "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
      "rowId" : "Row Id of the linked cell",
      "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
    } ]
  } ],
  "createdBy" : { },
  "filteredOut" : "true if this row is filtered out by a column filter (and thus is not displayed in the Smartsheet app), false if the row is not filtered out. Only returned if the include query string parameter contains filters.",
  "sheetId" : "Parent sheet Id",
  "lockedForUser" : "Indicates whether the row is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
  "permalink" : "URL that represents a direct link to the row in SmartsheetOnly returned if the include query string parameter contains rowPermalink.",
  "siblingId" : "In a response - the Id of the previous sibling row at the same hierarchical level of this row (if any). In a request - the Id of the desired sibling row (used to specify the location for a new or moved row)."
}
```

### allowPartialSuccess

If true, allows bulk operations to process even if one or more operations are invalid for some reason.

**Type:** boolean

</details>

## add_user

Adds a user to the organization account.

<details><summary>Parameters</summary>

### $body

User object with the following attributes:
admin (required)
email (required)
licensedSheetCreator (required)
firstName (optional)
lastName (optional)
groupAdmin (optional)
resourceViewer (optional)

**Type:** object

```json
{
  "lastLogin" : "Last login time of the current user",
  "lastName" : "User's last name",
  "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
  "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
  "profileImage" : {
    "altText" : "Alternate text for the image",
    "width" : "Original width (in pixels) of the uploaded image",
    "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
    "id" : "Image Id",
    "height" : "Original height (in pixels) of the uploaded image"
  },
  "firstName" : "User's first name",
  "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
  "name" : "User's full name (read-only)",
  "id" : "User Id",
  "sheetCount" : "The number of sheets owned by the current user within the organization account",
  "email" : "User's primary email address",
  "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
  "status" : "User status"
}
```

### sendEmail

Indicate whether to send a welcome email.

**Type:** boolean

</details>

## attach_new_version

Uploads a new version of a file to a sheet or row. This operation can be performed using a simple upload or a multipart upload. For more information, see Post an Attachment.

<details><summary>Parameters</summary>

### attachmentId (required)

**Type:** string

### sheetId (required)

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## attach_url_to_comment

Attaches a URL to the comment. The URL can be any of the following:

<details><summary>Parameters</summary>

### commentId (required)

**Type:** string

### sheetId (required)

**Type:** string

### $body

Attachment object limited to the following attributes:
attachmentSubType
attachmentType
description (applicable when attaching to sheet or row only)
name
url

**Type:** object

```json
{
  "createdAt" : "A timestamp of when the attachment was originally added",
  "attachmentSubType" : "Attachment sub type",
  "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
  "createdBy" : { },
  "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
  "name" : "Attachment name",
  "id" : "Attachment Id",
  "mimeType" : "Attachment MIME type (PNG, etc.)",
  "sizeInKb" : "The size of the file, if the attachmentType is FILE",
  "parentId" : "The Id of the parent",
  "parentType" : "The type of object the attachment belongs to",
  "url" : "Attachment temporary URL (files only)"
}
```

</details>

## attach_url_to_row

Attaches a URL to the row. The URL can be any of the following:

<details><summary>Parameters</summary>

### rowId (required)

**Type:** string

### sheetId (required)

**Type:** string

### $body

Attachment object limited to the following attributes:
attachmentSubType
attachmentType
description (applicable when attaching to sheet or row only)
name
url

**Type:** object

```json
{
  "createdAt" : "A timestamp of when the attachment was originally added",
  "attachmentSubType" : "Attachment sub type",
  "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
  "createdBy" : { },
  "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
  "name" : "Attachment name",
  "id" : "Attachment Id",
  "mimeType" : "Attachment MIME type (PNG, etc.)",
  "sizeInKb" : "The size of the file, if the attachmentType is FILE",
  "parentId" : "The Id of the parent",
  "parentType" : "The type of object the attachment belongs to",
  "url" : "Attachment temporary URL (files only)"
}
```

</details>

## attach_url_to_sheet

Attaches a URL to the sheet. The URL can be any of the following:

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

Attachment object limited to the following attributes:
attachmentSubType
attachmentType
description (applicable when attaching to sheet or row only)
name
url

**Type:** object

```json
{
  "createdAt" : "A timestamp of when the attachment was originally added",
  "attachmentSubType" : "Attachment sub type",
  "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
  "createdBy" : { },
  "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
  "name" : "Attachment name",
  "id" : "Attachment Id",
  "mimeType" : "Attachment MIME type (PNG, etc.)",
  "sizeInKb" : "The size of the file, if the attachmentType is FILE",
  "parentId" : "The Id of the parent",
  "parentType" : "The type of object the attachment belongs to",
  "url" : "Attachment temporary URL (files only)"
}
```

</details>

## change_update_request

Changes the specified update request for the sheet.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### updateRequestId (required)

**Type:** string

### $body

UpdateRequest object.

The UpdateRequest object in the request body must specify one or more of the following attributes:
ccMe: Boolean
columnIds: number[]
includeAttachments: Boolean
includeDiscussions: Boolean
message: string
schedule: Schedule object
sendTo: Recipient[]
subject: string

**Type:** object

```json
{
  "createdAt" : "The date and time for when this request was originally created. Read-only.",
  "schedule" : {
    "dayOfMonth" : "The day within the month",
    "dayDescriptors" : [ "string. Possible values: DAY | WEEKDAY | WEEKEND | SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY" ],
    "dayOrdinal" : "This attribute is applicable to the MONTHLY schedule type.",
    "lastSentAt" : "The date and time for when the last request was sent. Read-only.",
    "repeatEvery" : "Frequency on which the request is delivered. The unit is a function of the type attribute.",
    "type" : "Schedule type",
    "endAt" : "The date, time, and time zone at which the delivery schedule ends. It must be a valid ISO-8601 date and time with an offset (YYYY-MM-DDThh:mm:ssTZD).",
    "nextSendAt" : "The date and time for when the next request is scheduled to send. Read-only.",
    "startAt" : "The date, time, and time zone at which the delivery schedule ends. It must be a valid ISO-8601 date and time with an offset (YYYY-MM-DDThh:mm:ssTZD)."
  },
  "modifiedAt" : "The date and time for when the last change was made to this request. Read-only.",
  "id" : "Id of the update request.",
  "sentBy" : {
    "lastLogin" : "Last login time of the current user",
    "lastName" : "User's last name",
    "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
    "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
    "profileImage" : {
      "altText" : "Alternate text for the image",
      "width" : "Original width (in pixels) of the uploaded image",
      "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
      "id" : "Image Id",
      "height" : "Original height (in pixels) of the uploaded image"
    },
    "firstName" : "User's first name",
    "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
    "name" : "User's full name (read-only)",
    "id" : "User Id",
    "sheetCount" : "The number of sheets owned by the current user within the organization account",
    "email" : "User's primary email address",
    "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
    "status" : "User status"
  }
}
```

</details>

## copy_folder

Creates a copy of the specified folder.

<details><summary>Parameters</summary>

### folderId (required)

**Type:** string

### $body

ContainerDestination object

**Type:** object

```json
{
  "newName" : "Name of the newly created object (when creating a copy of a Sheet, Folder, Sight, or Workspace). This attribute is not supported for \"move\" operations (that is, a moved Sheet, Folder, Sight, or Workspace retains its original name).",
  "destinationType" : "Type of the destination container (when copying or moving a Sheet or a Folder).",
  "destinationId" : "Id of the destination container (when copying or moving a Sheet or a Folder). Required if destinationType is \"folder\" or \"workspace\" If destinationType is \"home\", this value must be null."
}
```

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: attachments | cellLinks | data | discussions | forms | ruleRecipients | rules | shares | all" ]
```

### skipRemap

comma-separated list of references to NOT re-map for the newly created folder.

**Type:** array

```json
[ "string. Possible values: cellLinks | reports | sheetHyperlinks | sights" ]
```

</details>

## copy_rows_to_another_sheet

Copies rows from the sheet specified in the URL to (the bottom of) another sheet.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

CopyOrMoveRowDirective object

**Type:** object

```json
{
  "rowIds" : [ "number" ],
  "to" : {
    "sheetId" : "Id of the destination sheet"
  }
}
```

### ignoreRowsNotFound

If set to true, specifying row Ids that do not exist within the source sheet does not cause an error response. If omitted or set to false, specifying row Ids that do not exist within the source sheet causes an error response (and no rows are copied).

**Type:** boolean

### include

comma-separated list of row elements to copy in addition to the cell data

**Type:** array

```json
[ "string. Possible values: all | attachments | children" ]
```

</details>

## copy_sheet

Creates a copy of the specified sheet.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

ContainerDestination object

**Type:** object

```json
{
  "newName" : "Name of the newly created object (when creating a copy of a Sheet, Folder, Sight, or Workspace). This attribute is not supported for \"move\" operations (that is, a moved Sheet, Folder, Sight, or Workspace retains its original name).",
  "destinationType" : "Type of the destination container (when copying or moving a Sheet or a Folder).",
  "destinationId" : "Id of the destination container (when copying or moving a Sheet or a Folder). Required if destinationType is \"folder\" or \"workspace\" If destinationType is \"home\", this value must be null."
}
```

### exclude

a comma-separated list of elements to not include in the response.

**Type:** array

```json
[ "string. Possible values: sheetHyperlinks" ]
```

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: attachments | cellLinks | data | discussions | forms | ruleRecipients | rules | shares | all" ]
```

</details>

## copy_sight

Creates a copy of the specified Sight.

<details><summary>Parameters</summary>

### sightId (required)

**Type:** string

### $body

ContainerDestination object

**Type:** object

```json
{
  "newName" : "Name of the newly created object (when creating a copy of a Sheet, Folder, Sight, or Workspace). This attribute is not supported for \"move\" operations (that is, a moved Sheet, Folder, Sight, or Workspace retains its original name).",
  "destinationType" : "Type of the destination container (when copying or moving a Sheet or a Folder).",
  "destinationId" : "Id of the destination container (when copying or moving a Sheet or a Folder). Required if destinationType is \"folder\" or \"workspace\" If destinationType is \"home\", this value must be null."
}
```

</details>

## copy_workspace

Creates a copy of the specified workspace.

<details><summary>Parameters</summary>

### workspaceId (required)

**Type:** string

### $body

ContainerDestination object, limited to the following attribute:
newName (string) - required

**Type:** object

```json
{
  "newName" : "Name of the newly created object (when creating a copy of a Sheet, Folder, Sight, or Workspace). This attribute is not supported for \"move\" operations (that is, a moved Sheet, Folder, Sight, or Workspace retains its original name).",
  "destinationType" : "Type of the destination container (when copying or moving a Sheet or a Folder).",
  "destinationId" : "Id of the destination container (when copying or moving a Sheet or a Folder). Required if destinationType is \"folder\" or \"workspace\" If destinationType is \"home\", this value must be null."
}
```

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: attachments | cellLinks | data | discussions | forms | ruleRecipients | rules | shares | all" ]
```

### skipRemap

comma-separated list of references to NOT re-map for the newly created workspace.

**Type:** array

```json
[ "string. Possible values: cellLinks | reports | sheetHyperlinks | sights" ]
```

</details>

## create_cross_sheet_references

Adds a cross-sheet reference between two sheets and defines the data range for formulas. Each distinct data range requires a new cross-sheet reference.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

CrossSheetReference object with the following attributes:
sourceSheetId: sheetId for data source
Either two or all of the following:endColumnId: Defines ending edge of range when specifying one or more columns. Must be used with startColumnId.endRowId: Defines ending edge of range when specifying one or more rows. Must be used with startRowId.startColumnId: Defines beginning edge of range when specifying one or more columns. Must be used with endColumnId.startRowId: Defines beginning edge of range when specifying one or more rows. Must be used with endRowId.
name (optional): unique name for reference. If you omit this parameter, Smartsheet will autogenerate a name.

**Type:** object

```json
{
  "startRowId" : "Defines beginning edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
  "startColumnId" : "Defines beginning edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
  "name" : "Friendly name of reference. Auto-generated unless specified in Create Cross-sheet References.",
  "sourceSheetId" : "Sheet Id of source sheet.",
  "endColumnId" : "Defines ending edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
  "endRowId" : "Defines ending edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
  "id" : "Cross-sheet reference Id, guaranteed unique within referencing sheet.",
  "status" : "string. Possible values: OK | BLOCKED | BROKEN | CIRCULAR | DISABLED | INVALID/UNKNOWN | NOT_SHARED"
}
```

</details>

## create_discussion_on_row

Creates a new discussion on a row. 
Creating a Discussion without an Attachment 
Creating a Discussion with an Attachment

<details><summary>Parameters</summary>

### rowId (required)

**Type:** string

### sheetId (required)

**Type:** string

### $body

Discussion object with the following attribute:
comment (Comment object),Request body should contain parts with the following names:
discussion: JSON Discussion object with the following attributes:title (string), must be 100 characters in length or lesscomment (Comment object)
file: (optional) file to attach to the new commentSee Multipart Uploads for more information on parts.

**Type:** object

```json
{
  "commentAttachments" : [ {
    "createdAt" : "A timestamp of when the attachment was originally added",
    "attachmentSubType" : "Attachment sub type",
    "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
    "createdBy" : { },
    "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
    "name" : "Attachment name",
    "id" : "Attachment Id",
    "mimeType" : "Attachment MIME type (PNG, etc.)",
    "sizeInKb" : "The size of the file, if the attachmentType is FILE",
    "parentId" : "The Id of the parent",
    "parentType" : "The type of object the attachment belongs to",
    "url" : "Attachment temporary URL (files only)"
  } ],
  "comments" : [ {
    "createdAt" : "Time of creation",
    "attachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "createdBy" : { },
    "discussionId" : "Discussion Id",
    "modifiedAt" : "Time of last modification",
    "id" : "Comment Id",
    "text" : "Comment body"
  } ],
  "accessLevel" : "User's permissions on the discussion",
  "createdBy" : { },
  "readOnly" : "Indicates whether the user can modify the discussion",
  "id" : "Discussion Id",
  "lastCommentedAt" : "Time of most recent comment",
  "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
  "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
  "parentType" : "string. Possible values: SHEET | ROW",
  "commentCount" : "The number of comments in the discussion",
  "lastCommentedUser" : {
    "lastLogin" : "Last login time of the current user",
    "lastName" : "User's last name",
    "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
    "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
    "profileImage" : {
      "altText" : "Alternate text for the image",
      "width" : "Original width (in pixels) of the uploaded image",
      "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
      "id" : "Image Id",
      "height" : "Original height (in pixels) of the uploaded image"
    },
    "firstName" : "User's first name",
    "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
    "name" : "User's full name (read-only)",
    "id" : "User Id",
    "sheetCount" : "The number of sheets owned by the current user within the organization account",
    "email" : "User's primary email address",
    "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
    "status" : "User status"
  }
}
```

</details>

## create_discussion_on_sheet

Creates a new discussion on a sheet. 
Creating a Discussion without an Attachment 
Creating a Discussion with an Attachment

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

Discussion object with the following attribute:
comment (Comment object),Request body should contain parts with the following names:
discussion: JSON Discussion object with the following attributes:title (string), must be 100 characters in length or lesscomment (Comment object)
file: (optional) file to attach to the new commentSee Multipart Uploads for more information on parts.

**Type:** object

```json
{
  "commentAttachments" : [ {
    "createdAt" : "A timestamp of when the attachment was originally added",
    "attachmentSubType" : "Attachment sub type",
    "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
    "createdBy" : { },
    "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
    "name" : "Attachment name",
    "id" : "Attachment Id",
    "mimeType" : "Attachment MIME type (PNG, etc.)",
    "sizeInKb" : "The size of the file, if the attachmentType is FILE",
    "parentId" : "The Id of the parent",
    "parentType" : "The type of object the attachment belongs to",
    "url" : "Attachment temporary URL (files only)"
  } ],
  "comments" : [ {
    "createdAt" : "Time of creation",
    "attachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "createdBy" : { },
    "discussionId" : "Discussion Id",
    "modifiedAt" : "Time of last modification",
    "id" : "Comment Id",
    "text" : "Comment body"
  } ],
  "accessLevel" : "User's permissions on the discussion",
  "createdBy" : { },
  "readOnly" : "Indicates whether the user can modify the discussion",
  "id" : "Discussion Id",
  "lastCommentedAt" : "Time of most recent comment",
  "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
  "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
  "parentType" : "string. Possible values: SHEET | ROW",
  "commentCount" : "The number of comments in the discussion",
  "lastCommentedUser" : {
    "lastLogin" : "Last login time of the current user",
    "lastName" : "User's last name",
    "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
    "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
    "profileImage" : {
      "altText" : "Alternate text for the image",
      "width" : "Original width (in pixels) of the uploaded image",
      "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
      "id" : "Image Id",
      "height" : "Original height (in pixels) of the uploaded image"
    },
    "firstName" : "User's first name",
    "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
    "name" : "User's full name (read-only)",
    "id" : "User Id",
    "sheetCount" : "The number of sheets owned by the current user within the organization account",
    "email" : "User's primary email address",
    "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
    "status" : "User status"
  }
}
```

</details>

## create_folder_sheets_level

Creates a folder in the user's Sheets folder (Home).

<details><summary>Parameters</summary>

### $body

Folder object, limited to the following attribute:
name (string) - required, does not have to be unique

**Type:** object

```json
{
  "reports" : [ {
    "sourceSheets" : [ { } ]
  } ],
  "sheets" : [ {
    "workspace" : { },
    "attachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "columns" : [ {
      "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
      "contactOptions" : [ {
        "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
        "email" : "A parsable email address."
      } ],
      "hidden" : "Indicates whether the column is hidden",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
      "description" : "Column description.",
      "index" : "Column index or position. This number is zero-based.",
      "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
      "title" : "Column title",
      "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
      "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
      "autoNumberFormat" : {
        "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
        "startingNumber" : "The starting number for the auto-id",
        "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
        "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
      },
      "options" : [ "string" ],
      "width" : "Display width of the column in pixels",
      "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
      "id" : "Column Id",
      "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
      "validation" : "Indicates whether validation has been enabled for the column (value = true)",
      "primary" : "Returned only if the column is the Primary Column (value = true)"
    } ],
    "modifiedAt" : "Time that the sheet was modified",
    "discussions" : [ { } ],
    "source" : { },
    "ownerId" : "User Id of the sheet owner",
    "resourceManagementEnabled" : "Indicates that resource management is enabled",
    "ganttEnabled" : "Indicates whether \"Gantt View\" is enabled",
    "createdAt" : "Time that the sheet was created",
    "id" : "Sheet Id",
    "totalRowCount" : "The total number of rows in the sheet",
    "owner" : "Email address of the sheet owner",
    "accessLevel" : "User's permissions on the sheet",
    "readOnly" : "Returned only if the sheet belongs to an expired trial (value = true)",
    "rows" : [ {
      "conditionalFormat" : "Describes this row's conditional format. Only returned if the include query string parameter contains format and this row has a conditional format applied.",
      "attachments" : [ {
        "createdAt" : "A timestamp of when the attachment was originally added",
        "attachmentSubType" : "Attachment sub type",
        "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
        "createdBy" : { },
        "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
        "name" : "Attachment name",
        "id" : "Attachment Id",
        "mimeType" : "Attachment MIME type (PNG, etc.)",
        "sizeInKb" : "The size of the file, if the attachmentType is FILE",
        "parentId" : "The Id of the parent",
        "parentType" : "The type of object the attachment belongs to",
        "url" : "Attachment temporary URL (files only)"
      } ],
      "indent" : "Specifies the number of levels to indent an existing row. You can specify this attribute in a request, but it is never present in a response.",
      "columns" : [ {
        "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
        "contactOptions" : [ {
          "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
          "email" : "A parsable email address."
        } ],
        "hidden" : "Indicates whether the column is hidden",
        "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
        "description" : "Column description.",
        "index" : "Column index or position. This number is zero-based.",
        "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
        "title" : "Column title",
        "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
        "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
        "autoNumberFormat" : {
          "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
          "startingNumber" : "The starting number for the auto-id",
          "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
          "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
        },
        "options" : [ "string" ],
        "width" : "Display width of the column in pixels",
        "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
        "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
        "id" : "Column Id",
        "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
        "validation" : "Indicates whether validation has been enabled for the column (value = true)",
        "primary" : "Returned only if the column is the Primary Column (value = true)"
      } ],
      "modifiedAt" : "Time of last modification",
      "discussions" : [ {
        "commentAttachments" : [ {
          "createdAt" : "A timestamp of when the attachment was originally added",
          "attachmentSubType" : "Attachment sub type",
          "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
          "createdBy" : { },
          "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
          "name" : "Attachment name",
          "id" : "Attachment Id",
          "mimeType" : "Attachment MIME type (PNG, etc.)",
          "sizeInKb" : "The size of the file, if the attachmentType is FILE",
          "parentId" : "The Id of the parent",
          "parentType" : "The type of object the attachment belongs to",
          "url" : "Attachment temporary URL (files only)"
        } ],
        "comments" : [ {
          "createdAt" : "Time of creation",
          "attachments" : [ {
            "createdAt" : "A timestamp of when the attachment was originally added",
            "attachmentSubType" : "Attachment sub type",
            "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
            "createdBy" : { },
            "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
            "name" : "Attachment name",
            "id" : "Attachment Id",
            "mimeType" : "Attachment MIME type (PNG, etc.)",
            "sizeInKb" : "The size of the file, if the attachmentType is FILE",
            "parentId" : "The Id of the parent",
            "parentType" : "The type of object the attachment belongs to",
            "url" : "Attachment temporary URL (files only)"
          } ],
          "createdBy" : { },
          "discussionId" : "Discussion Id",
          "modifiedAt" : "Time of last modification",
          "id" : "Comment Id",
          "text" : "Comment body"
        } ],
        "accessLevel" : "User's permissions on the discussion",
        "createdBy" : { },
        "readOnly" : "Indicates whether the user can modify the discussion",
        "id" : "Discussion Id",
        "lastCommentedAt" : "Time of most recent comment",
        "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
        "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
        "parentType" : "string. Possible values: SHEET | ROW",
        "commentCount" : "The number of comments in the discussion",
        "lastCommentedUser" : {
          "lastLogin" : "Last login time of the current user",
          "lastName" : "User's last name",
          "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
          "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
          "profileImage" : {
            "altText" : "Alternate text for the image",
            "width" : "Original width (in pixels) of the uploaded image",
            "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
            "id" : "Image Id",
            "height" : "Original height (in pixels) of the uploaded image"
          },
          "firstName" : "User's first name",
          "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
          "name" : "User's full name (read-only)",
          "id" : "User Id",
          "sheetCount" : "The number of sheets owned by the current user within the organization account",
          "email" : "User's primary email address",
          "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
          "status" : "User status"
        }
      } ],
      "toBottom" : "Adds or moves the row to the bottom of the sheet. You can specify this attribute in a request, but it is never present in a response.",
      "toTop" : "Adds or moves the row to the top of the sheet. You can specify this attribute in a request, but it is never present in a response.",
      "createdAt" : "Time of creation",
      "expanded" : "Indicates whether the row is expanded or collapsed",
      "inCriticalPath" : "Only returned, with a value of true, if the sheet is a project sheet with dependencies enabled and this row is in the critical path",
      "above" : "Specifies the location for a new or moved row. You can specify this attribute in a request, but it is never present in a response.",
      "outdent" : "Specifies the number of levels to outdent an existing row. You can specify this attribute in a request, but it is never present in a response.",
      "modifiedBy" : {
        "lastLogin" : "Last login time of the current user",
        "lastName" : "User's last name",
        "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
        "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
        "profileImage" : {
          "altText" : "Alternate text for the image",
          "width" : "Original width (in pixels) of the uploaded image",
          "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
          "id" : "Image Id",
          "height" : "Original height (in pixels) of the uploaded image"
        },
        "firstName" : "User's first name",
        "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
        "name" : "User's full name (read-only)",
        "id" : "User Id",
        "sheetCount" : "The number of sheets owned by the current user within the organization account",
        "email" : "User's primary email address",
        "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
        "status" : "User status"
      },
      "id" : "Row Id",
      "locked" : "Indicates whether the row is locked. In a response, a value of true indicates that the row has been locked by the sheet owner or the admin.",
      "rowNumber" : "Row number within the sheet (1-based - starts at 1)",
      "accessLevel" : "User's permission level on the sheet that contains the row",
      "format" : "Format descriptor (see Formatting). Only returned if the include query string parameter contains format and this row has a non-default format applied.",
      "version" : "Sheet version number that is incremented every time a sheet is modified",
      "parentId" : "In a response - the Id of the parent row (if any). In a request - the Id of the desired parent row (used to specify the location for a new or moved row).",
      "cells" : [ {
        "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
        "hyperlink" : { },
        "image" : { },
        "columnId" : "The Id of the column that the cell is located in",
        "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
        "objectValue" : {
          "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
        },
        "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
        "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
        "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
        "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
        "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
        "linkInFromCell" : {
          "sheetName" : "Sheet name of the linked cell",
          "columnId" : "Column Id of the linked cell",
          "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
          "rowId" : "Row Id of the linked cell",
          "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
        },
        "value" : { },
        "linksOutToCells" : [ {
          "sheetName" : "Sheet name of the linked cell",
          "columnId" : "Column Id of the linked cell",
          "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
          "rowId" : "Row Id of the linked cell",
          "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
        } ]
      } ],
      "createdBy" : { },
      "filteredOut" : "true if this row is filtered out by a column filter (and thus is not displayed in the Smartsheet app), false if the row is not filtered out. Only returned if the include query string parameter contains filters.",
      "sheetId" : "Parent sheet Id",
      "lockedForUser" : "Indicates whether the row is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "permalink" : "URL that represents a direct link to the row in SmartsheetOnly returned if the include query string parameter contains rowPermalink.",
      "siblingId" : "In a response - the Id of the previous sibling row at the same hierarchical level of this row (if any). In a request - the Id of the desired sibling row (used to specify the location for a new or moved row)."
    } ],
    "fromId" : "The Id of the template from which to create the sheet. This attribute can be specified in a request, but is never present in a response.",
    "version" : "A number that is incremented every time a sheet is modified",
    "effectiveAttachmentOptions" : [ "string" ],
    "dependenciesEnabled" : "Indicates whether dependencies are enabled",
    "showParentRowsForFilters" : "Returned only if there are column filters on the sheet. Value = true if \"show parent rows\" is enabled for the filters.",
    "userSettings" : {
      "criticalPathEnabled" : "Does this user have \"Show Critical Path\" turned on for this sheet? NOTE: This setting only has an effect on project sheets with dependencies enabled.",
      "displaySummaryTasks" : "Does this user have \"Display Summary Tasks\" turned on for this sheet? Applies only to sheets where \"Calendar View\" has been configured."
    },
    "crossSheetReferences" : [ {
      "startRowId" : "Defines beginning edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
      "startColumnId" : "Defines beginning edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
      "name" : "Friendly name of reference. Auto-generated unless specified in Create Cross-sheet References.",
      "sourceSheetId" : "Sheet Id of source sheet.",
      "endColumnId" : "Defines ending edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
      "endRowId" : "Defines ending edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
      "id" : "Cross-sheet reference Id, guaranteed unique within referencing sheet.",
      "status" : "string. Possible values: OK | BLOCKED | BROKEN | CIRCULAR | DISABLED | INVALID/UNKNOWN | NOT_SHARED"
    } ],
    "name" : "Sheet name",
    "permalink" : "URL that represents a direct link to the sheet in Smartsheet",
    "favorite" : "Returned only if the user has marked this sheet as a favorite in their Home tab (value = true)",
    "projectSettings" : {
      "nonWorkingDays" : [ "string" ],
      "workingDays" : [ "string. Possible values: MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY" ],
      "lengthOfDay" : "Length of a workday for a project sheet. Valid value must be above or equal to 1 hour, and less than or equal to 24 hours."
    }
  } ],
  "folders" : [ { } ],
  "sights" : [ {
    "createdAt" : "Time of creation",
    "backgroundColor" : "The hex color, for instance #E6F5FE",
    "workspace" : {
      "reports" : [ { } ],
      "sheets" : [ { } ],
      "folders" : [ { } ],
      "sights" : [ { } ],
      "accessLevel" : "User's permissions on the workspace",
      "templates" : [ { } ],
      "name" : "Workspace name",
      "id" : "Workspace Id",
      "permalink" : "URL that represents a direct link to the workspace in Smartsheet",
      "favorite" : "Returned only if the user has marked the workspace as a favorite in their \"Home\" tab (value = true)"
    },
    "accessLevel" : "User's permissions on the Sight.",
    "modifiedAt" : "Time of last modification",
    "name" : "Sight name",
    "id" : "Sight Id",
    "columnCount" : "Number of columns that the Sight contains",
    "permalink" : "URL that represents a direct link to the Sight in Smartsheet",
    "widgets" : [ {
      "showTitleIcon" : "True indicates that the client should display the sheet icon in the widget title",
      "xPosition" : "X-coordinate of widget's position on the Sight",
      "Rich Text" : {
        "html" : "The widget content as HTML. The Rich Text widget supports the following subset of HTML tags and CSS Styles: HTML: a - defines a hyperlink, br - inserts a single line break, li - defines a list item, ol - defines an ordered list, p - defines a paragraph, ul - defines an unordered list, span - defines a section in a document. CSS: color, font-family, font-size, font-style, font-weight, text-align, text-decoration."
      },
      "Report" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "reportId" : "Report Id denoting container source",
        "htmlContent" : "HTML snippet to render report"
      },
      "yPosition" : "Y-coordinate of widget's position on the Sight",
      "Title" : {
        "backgroundColor" : "The hex color, for instance #E6F5FE",
        "htmlContent" : "HTML snippet to render title"
      },
      "type" : "Type of widget. See table below to see how UI widget names map to type.",
      "title" : "Title of the widget",
      "viewMode" : "1 indicates content is centered. 2 indicates content is left aligned. Must use a query parameter of level=2 to see this information.",
      "Image" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "fileName" : "Name of the image file",
        "privateId" : "The image private Id",
        "format" : "formatDescriptor",
        "width" : "Original width of the image in pixels",
        "height" : "Original height of the image in pixels"
      },
      "version" : "Widget version number",
      "titleFormat" : "FormatDescriptor",
      "contents" : { },
      "showTitle" : "True indicates that the client should display the widget title. NOTE: This is independent of the title string which may be null or empty.",
      "Shortcut" : {
        "shortcutData" : [ {
          "hyperlink" : {
            "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
            "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
            "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
            "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
          },
          "attachmentType" : "Attachment type",
          "labelFormat" : "formatDescriptor",
          "label" : "Label for the data point",
          "mimeType" : "MIME type if available for attachment type",
          "order" : "The display order for the ShortcutWidgetItem object"
        } ]
      },
      "Web Content" : {
        "url" : "The URL"
      },
      "width" : "Number of columns that the widget occupies on the Sight",
      "Metric" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "columns" : [ {
          "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
          "contactOptions" : [ {
            "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
            "email" : "A parsable email address."
          } ],
          "hidden" : "Indicates whether the column is hidden",
          "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
          "description" : "Column description.",
          "index" : "Column index or position. This number is zero-based.",
          "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
          "title" : "Column title",
          "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
          "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
          "autoNumberFormat" : {
            "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
            "startingNumber" : "The starting number for the auto-id",
            "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
            "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
          },
          "options" : [ "string" ],
          "width" : "Display width of the column in pixels",
          "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
          "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
          "id" : "Column Id",
          "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
          "validation" : "Indicates whether validation has been enabled for the column (value = true)",
          "primary" : "Returned only if the column is the Primary Column (value = true)"
        } ],
        "sheetId" : "The Id of the sheet from which the cell data originates",
        "cellData" : [ {
          "labelFormat" : "formatDescriptor",
          "columnId" : "Column Id for each item",
          "valueFormat" : "formatDescriptor",
          "sheetId" : "Sheet Id for each item",
          "objectValue" : { },
          "label" : "Label for the data point. This is either the column name or a user-provided string",
          "cell" : {
            "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
            "hyperlink" : { },
            "image" : { },
            "columnId" : "The Id of the column that the cell is located in",
            "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
            "objectValue" : {
              "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
            },
            "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
            "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
            "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
            "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
            "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
            "linkInFromCell" : {
              "sheetName" : "Sheet name of the linked cell",
              "columnId" : "Column Id of the linked cell",
              "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
              "rowId" : "Row Id of the linked cell",
              "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
            },
            "value" : { },
            "linksOutToCells" : [ {
              "sheetName" : "Sheet name of the linked cell",
              "columnId" : "Column Id of the linked cell",
              "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
              "rowId" : "Row Id of the linked cell",
              "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
            } ]
          },
          "dataSource" : "CELL",
          "rowId" : "Row Id for each item",
          "order" : "The display order for the CellDataItem"
        } ]
      },
      "id" : "Widget Id",
      "Chart" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "reportId" : "Report Id denoting container source, if applicable",
        "legend" : "The location in the widget where Smartsheet renders the legend, for example, RIGHT",
        "series" : [ { } ],
        "axes" : [ { } ],
        "sheetId" : "Sheet Id denoting container source, if applicable",
        "includedColumnIds" : [ "number" ],
        "selectionRanges" : [ {
          "sourceRowId2" : "Defines ending edge of range when specifying one or more rows.",
          "sourceColumnId2" : "Defines ending edge of range when specifying one or more columns.",
          "sourceRowId1" : "Defines beginning edge of range when specifying one or more rows.",
          "sourceColumnId1" : "Defines beginning edge of range when specifying one or more columns."
        } ]
      },
      "height" : "Number of rows that the widget occupies on the Sight"
    } ],
    "favorite" : "Indicates whether the user has marked the Sight as a favorite"
  } ],
  "templates" : [ {
    "globalTemplate" : "Type of global template. Only applicable to blank public templates.",
    "image" : "URL to the small preview image for this template. Only applicable to non-blank public templates.",
    "largeImage" : "URL to the large preview image for this template. Only applicable to non-blank public templates.",
    "blank" : "Indicates whether the template is blank. Only applicable to public templates",
    "accessLevel" : "User's permissions on the template",
    "name" : "Template name",
    "description" : "Template description",
    "id" : "Template Id",
    "categories" : [ "string" ],
    "type" : "Type of the template. Only applicable to public templates.",
    "locale" : "Locale of the template.Only applicable to public templates.",
    "tags" : [ "string" ]
  } ],
  "name" : "Folder name",
  "id" : "Folder Id",
  "permalink" : "URL that represents a direct link to the folder in Smartsheet",
  "favorite" : "Returned only if the user has marked the folder as a favorite in their \"Home\" tab (value = true)"
}
```

</details>

## create_folder_subfolder

Creates a folder in the specified folder.

<details><summary>Parameters</summary>

### folderId (required)

**Type:** string

### $body

Folder object, limited to the following attribute:
name (string) - required, does not have to be unique

**Type:** object

```json
{
  "reports" : [ {
    "sourceSheets" : [ { } ]
  } ],
  "sheets" : [ {
    "workspace" : { },
    "attachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "columns" : [ {
      "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
      "contactOptions" : [ {
        "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
        "email" : "A parsable email address."
      } ],
      "hidden" : "Indicates whether the column is hidden",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
      "description" : "Column description.",
      "index" : "Column index or position. This number is zero-based.",
      "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
      "title" : "Column title",
      "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
      "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
      "autoNumberFormat" : {
        "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
        "startingNumber" : "The starting number for the auto-id",
        "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
        "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
      },
      "options" : [ "string" ],
      "width" : "Display width of the column in pixels",
      "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
      "id" : "Column Id",
      "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
      "validation" : "Indicates whether validation has been enabled for the column (value = true)",
      "primary" : "Returned only if the column is the Primary Column (value = true)"
    } ],
    "modifiedAt" : "Time that the sheet was modified",
    "discussions" : [ { } ],
    "source" : { },
    "ownerId" : "User Id of the sheet owner",
    "resourceManagementEnabled" : "Indicates that resource management is enabled",
    "ganttEnabled" : "Indicates whether \"Gantt View\" is enabled",
    "createdAt" : "Time that the sheet was created",
    "id" : "Sheet Id",
    "totalRowCount" : "The total number of rows in the sheet",
    "owner" : "Email address of the sheet owner",
    "accessLevel" : "User's permissions on the sheet",
    "readOnly" : "Returned only if the sheet belongs to an expired trial (value = true)",
    "rows" : [ {
      "conditionalFormat" : "Describes this row's conditional format. Only returned if the include query string parameter contains format and this row has a conditional format applied.",
      "attachments" : [ {
        "createdAt" : "A timestamp of when the attachment was originally added",
        "attachmentSubType" : "Attachment sub type",
        "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
        "createdBy" : { },
        "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
        "name" : "Attachment name",
        "id" : "Attachment Id",
        "mimeType" : "Attachment MIME type (PNG, etc.)",
        "sizeInKb" : "The size of the file, if the attachmentType is FILE",
        "parentId" : "The Id of the parent",
        "parentType" : "The type of object the attachment belongs to",
        "url" : "Attachment temporary URL (files only)"
      } ],
      "indent" : "Specifies the number of levels to indent an existing row. You can specify this attribute in a request, but it is never present in a response.",
      "columns" : [ {
        "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
        "contactOptions" : [ {
          "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
          "email" : "A parsable email address."
        } ],
        "hidden" : "Indicates whether the column is hidden",
        "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
        "description" : "Column description.",
        "index" : "Column index or position. This number is zero-based.",
        "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
        "title" : "Column title",
        "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
        "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
        "autoNumberFormat" : {
          "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
          "startingNumber" : "The starting number for the auto-id",
          "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
          "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
        },
        "options" : [ "string" ],
        "width" : "Display width of the column in pixels",
        "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
        "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
        "id" : "Column Id",
        "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
        "validation" : "Indicates whether validation has been enabled for the column (value = true)",
        "primary" : "Returned only if the column is the Primary Column (value = true)"
      } ],
      "modifiedAt" : "Time of last modification",
      "discussions" : [ {
        "commentAttachments" : [ {
          "createdAt" : "A timestamp of when the attachment was originally added",
          "attachmentSubType" : "Attachment sub type",
          "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
          "createdBy" : { },
          "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
          "name" : "Attachment name",
          "id" : "Attachment Id",
          "mimeType" : "Attachment MIME type (PNG, etc.)",
          "sizeInKb" : "The size of the file, if the attachmentType is FILE",
          "parentId" : "The Id of the parent",
          "parentType" : "The type of object the attachment belongs to",
          "url" : "Attachment temporary URL (files only)"
        } ],
        "comments" : [ {
          "createdAt" : "Time of creation",
          "attachments" : [ {
            "createdAt" : "A timestamp of when the attachment was originally added",
            "attachmentSubType" : "Attachment sub type",
            "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
            "createdBy" : { },
            "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
            "name" : "Attachment name",
            "id" : "Attachment Id",
            "mimeType" : "Attachment MIME type (PNG, etc.)",
            "sizeInKb" : "The size of the file, if the attachmentType is FILE",
            "parentId" : "The Id of the parent",
            "parentType" : "The type of object the attachment belongs to",
            "url" : "Attachment temporary URL (files only)"
          } ],
          "createdBy" : { },
          "discussionId" : "Discussion Id",
          "modifiedAt" : "Time of last modification",
          "id" : "Comment Id",
          "text" : "Comment body"
        } ],
        "accessLevel" : "User's permissions on the discussion",
        "createdBy" : { },
        "readOnly" : "Indicates whether the user can modify the discussion",
        "id" : "Discussion Id",
        "lastCommentedAt" : "Time of most recent comment",
        "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
        "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
        "parentType" : "string. Possible values: SHEET | ROW",
        "commentCount" : "The number of comments in the discussion",
        "lastCommentedUser" : {
          "lastLogin" : "Last login time of the current user",
          "lastName" : "User's last name",
          "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
          "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
          "profileImage" : {
            "altText" : "Alternate text for the image",
            "width" : "Original width (in pixels) of the uploaded image",
            "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
            "id" : "Image Id",
            "height" : "Original height (in pixels) of the uploaded image"
          },
          "firstName" : "User's first name",
          "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
          "name" : "User's full name (read-only)",
          "id" : "User Id",
          "sheetCount" : "The number of sheets owned by the current user within the organization account",
          "email" : "User's primary email address",
          "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
          "status" : "User status"
        }
      } ],
      "toBottom" : "Adds or moves the row to the bottom of the sheet. You can specify this attribute in a request, but it is never present in a response.",
      "toTop" : "Adds or moves the row to the top of the sheet. You can specify this attribute in a request, but it is never present in a response.",
      "createdAt" : "Time of creation",
      "expanded" : "Indicates whether the row is expanded or collapsed",
      "inCriticalPath" : "Only returned, with a value of true, if the sheet is a project sheet with dependencies enabled and this row is in the critical path",
      "above" : "Specifies the location for a new or moved row. You can specify this attribute in a request, but it is never present in a response.",
      "outdent" : "Specifies the number of levels to outdent an existing row. You can specify this attribute in a request, but it is never present in a response.",
      "modifiedBy" : {
        "lastLogin" : "Last login time of the current user",
        "lastName" : "User's last name",
        "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
        "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
        "profileImage" : {
          "altText" : "Alternate text for the image",
          "width" : "Original width (in pixels) of the uploaded image",
          "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
          "id" : "Image Id",
          "height" : "Original height (in pixels) of the uploaded image"
        },
        "firstName" : "User's first name",
        "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
        "name" : "User's full name (read-only)",
        "id" : "User Id",
        "sheetCount" : "The number of sheets owned by the current user within the organization account",
        "email" : "User's primary email address",
        "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
        "status" : "User status"
      },
      "id" : "Row Id",
      "locked" : "Indicates whether the row is locked. In a response, a value of true indicates that the row has been locked by the sheet owner or the admin.",
      "rowNumber" : "Row number within the sheet (1-based - starts at 1)",
      "accessLevel" : "User's permission level on the sheet that contains the row",
      "format" : "Format descriptor (see Formatting). Only returned if the include query string parameter contains format and this row has a non-default format applied.",
      "version" : "Sheet version number that is incremented every time a sheet is modified",
      "parentId" : "In a response - the Id of the parent row (if any). In a request - the Id of the desired parent row (used to specify the location for a new or moved row).",
      "cells" : [ {
        "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
        "hyperlink" : { },
        "image" : { },
        "columnId" : "The Id of the column that the cell is located in",
        "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
        "objectValue" : {
          "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
        },
        "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
        "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
        "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
        "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
        "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
        "linkInFromCell" : {
          "sheetName" : "Sheet name of the linked cell",
          "columnId" : "Column Id of the linked cell",
          "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
          "rowId" : "Row Id of the linked cell",
          "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
        },
        "value" : { },
        "linksOutToCells" : [ {
          "sheetName" : "Sheet name of the linked cell",
          "columnId" : "Column Id of the linked cell",
          "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
          "rowId" : "Row Id of the linked cell",
          "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
        } ]
      } ],
      "createdBy" : { },
      "filteredOut" : "true if this row is filtered out by a column filter (and thus is not displayed in the Smartsheet app), false if the row is not filtered out. Only returned if the include query string parameter contains filters.",
      "sheetId" : "Parent sheet Id",
      "lockedForUser" : "Indicates whether the row is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "permalink" : "URL that represents a direct link to the row in SmartsheetOnly returned if the include query string parameter contains rowPermalink.",
      "siblingId" : "In a response - the Id of the previous sibling row at the same hierarchical level of this row (if any). In a request - the Id of the desired sibling row (used to specify the location for a new or moved row)."
    } ],
    "fromId" : "The Id of the template from which to create the sheet. This attribute can be specified in a request, but is never present in a response.",
    "version" : "A number that is incremented every time a sheet is modified",
    "effectiveAttachmentOptions" : [ "string" ],
    "dependenciesEnabled" : "Indicates whether dependencies are enabled",
    "showParentRowsForFilters" : "Returned only if there are column filters on the sheet. Value = true if \"show parent rows\" is enabled for the filters.",
    "userSettings" : {
      "criticalPathEnabled" : "Does this user have \"Show Critical Path\" turned on for this sheet? NOTE: This setting only has an effect on project sheets with dependencies enabled.",
      "displaySummaryTasks" : "Does this user have \"Display Summary Tasks\" turned on for this sheet? Applies only to sheets where \"Calendar View\" has been configured."
    },
    "crossSheetReferences" : [ {
      "startRowId" : "Defines beginning edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
      "startColumnId" : "Defines beginning edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
      "name" : "Friendly name of reference. Auto-generated unless specified in Create Cross-sheet References.",
      "sourceSheetId" : "Sheet Id of source sheet.",
      "endColumnId" : "Defines ending edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
      "endRowId" : "Defines ending edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
      "id" : "Cross-sheet reference Id, guaranteed unique within referencing sheet.",
      "status" : "string. Possible values: OK | BLOCKED | BROKEN | CIRCULAR | DISABLED | INVALID/UNKNOWN | NOT_SHARED"
    } ],
    "name" : "Sheet name",
    "permalink" : "URL that represents a direct link to the sheet in Smartsheet",
    "favorite" : "Returned only if the user has marked this sheet as a favorite in their Home tab (value = true)",
    "projectSettings" : {
      "nonWorkingDays" : [ "string" ],
      "workingDays" : [ "string. Possible values: MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY" ],
      "lengthOfDay" : "Length of a workday for a project sheet. Valid value must be above or equal to 1 hour, and less than or equal to 24 hours."
    }
  } ],
  "folders" : [ { } ],
  "sights" : [ {
    "createdAt" : "Time of creation",
    "backgroundColor" : "The hex color, for instance #E6F5FE",
    "workspace" : {
      "reports" : [ { } ],
      "sheets" : [ { } ],
      "folders" : [ { } ],
      "sights" : [ { } ],
      "accessLevel" : "User's permissions on the workspace",
      "templates" : [ { } ],
      "name" : "Workspace name",
      "id" : "Workspace Id",
      "permalink" : "URL that represents a direct link to the workspace in Smartsheet",
      "favorite" : "Returned only if the user has marked the workspace as a favorite in their \"Home\" tab (value = true)"
    },
    "accessLevel" : "User's permissions on the Sight.",
    "modifiedAt" : "Time of last modification",
    "name" : "Sight name",
    "id" : "Sight Id",
    "columnCount" : "Number of columns that the Sight contains",
    "permalink" : "URL that represents a direct link to the Sight in Smartsheet",
    "widgets" : [ {
      "showTitleIcon" : "True indicates that the client should display the sheet icon in the widget title",
      "xPosition" : "X-coordinate of widget's position on the Sight",
      "Rich Text" : {
        "html" : "The widget content as HTML. The Rich Text widget supports the following subset of HTML tags and CSS Styles: HTML: a - defines a hyperlink, br - inserts a single line break, li - defines a list item, ol - defines an ordered list, p - defines a paragraph, ul - defines an unordered list, span - defines a section in a document. CSS: color, font-family, font-size, font-style, font-weight, text-align, text-decoration."
      },
      "Report" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "reportId" : "Report Id denoting container source",
        "htmlContent" : "HTML snippet to render report"
      },
      "yPosition" : "Y-coordinate of widget's position on the Sight",
      "Title" : {
        "backgroundColor" : "The hex color, for instance #E6F5FE",
        "htmlContent" : "HTML snippet to render title"
      },
      "type" : "Type of widget. See table below to see how UI widget names map to type.",
      "title" : "Title of the widget",
      "viewMode" : "1 indicates content is centered. 2 indicates content is left aligned. Must use a query parameter of level=2 to see this information.",
      "Image" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "fileName" : "Name of the image file",
        "privateId" : "The image private Id",
        "format" : "formatDescriptor",
        "width" : "Original width of the image in pixels",
        "height" : "Original height of the image in pixels"
      },
      "version" : "Widget version number",
      "titleFormat" : "FormatDescriptor",
      "contents" : { },
      "showTitle" : "True indicates that the client should display the widget title. NOTE: This is independent of the title string which may be null or empty.",
      "Shortcut" : {
        "shortcutData" : [ {
          "hyperlink" : {
            "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
            "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
            "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
            "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
          },
          "attachmentType" : "Attachment type",
          "labelFormat" : "formatDescriptor",
          "label" : "Label for the data point",
          "mimeType" : "MIME type if available for attachment type",
          "order" : "The display order for the ShortcutWidgetItem object"
        } ]
      },
      "Web Content" : {
        "url" : "The URL"
      },
      "width" : "Number of columns that the widget occupies on the Sight",
      "Metric" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "columns" : [ {
          "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
          "contactOptions" : [ {
            "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
            "email" : "A parsable email address."
          } ],
          "hidden" : "Indicates whether the column is hidden",
          "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
          "description" : "Column description.",
          "index" : "Column index or position. This number is zero-based.",
          "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
          "title" : "Column title",
          "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
          "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
          "autoNumberFormat" : {
            "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
            "startingNumber" : "The starting number for the auto-id",
            "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
            "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
          },
          "options" : [ "string" ],
          "width" : "Display width of the column in pixels",
          "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
          "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
          "id" : "Column Id",
          "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
          "validation" : "Indicates whether validation has been enabled for the column (value = true)",
          "primary" : "Returned only if the column is the Primary Column (value = true)"
        } ],
        "sheetId" : "The Id of the sheet from which the cell data originates",
        "cellData" : [ {
          "labelFormat" : "formatDescriptor",
          "columnId" : "Column Id for each item",
          "valueFormat" : "formatDescriptor",
          "sheetId" : "Sheet Id for each item",
          "objectValue" : { },
          "label" : "Label for the data point. This is either the column name or a user-provided string",
          "cell" : {
            "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
            "hyperlink" : { },
            "image" : { },
            "columnId" : "The Id of the column that the cell is located in",
            "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
            "objectValue" : {
              "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
            },
            "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
            "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
            "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
            "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
            "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
            "linkInFromCell" : {
              "sheetName" : "Sheet name of the linked cell",
              "columnId" : "Column Id of the linked cell",
              "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
              "rowId" : "Row Id of the linked cell",
              "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
            },
            "value" : { },
            "linksOutToCells" : [ {
              "sheetName" : "Sheet name of the linked cell",
              "columnId" : "Column Id of the linked cell",
              "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
              "rowId" : "Row Id of the linked cell",
              "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
            } ]
          },
          "dataSource" : "CELL",
          "rowId" : "Row Id for each item",
          "order" : "The display order for the CellDataItem"
        } ]
      },
      "id" : "Widget Id",
      "Chart" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "reportId" : "Report Id denoting container source, if applicable",
        "legend" : "The location in the widget where Smartsheet renders the legend, for example, RIGHT",
        "series" : [ { } ],
        "axes" : [ { } ],
        "sheetId" : "Sheet Id denoting container source, if applicable",
        "includedColumnIds" : [ "number" ],
        "selectionRanges" : [ {
          "sourceRowId2" : "Defines ending edge of range when specifying one or more rows.",
          "sourceColumnId2" : "Defines ending edge of range when specifying one or more columns.",
          "sourceRowId1" : "Defines beginning edge of range when specifying one or more rows.",
          "sourceColumnId1" : "Defines beginning edge of range when specifying one or more columns."
        } ]
      },
      "height" : "Number of rows that the widget occupies on the Sight"
    } ],
    "favorite" : "Indicates whether the user has marked the Sight as a favorite"
  } ],
  "templates" : [ {
    "globalTemplate" : "Type of global template. Only applicable to blank public templates.",
    "image" : "URL to the small preview image for this template. Only applicable to non-blank public templates.",
    "largeImage" : "URL to the large preview image for this template. Only applicable to non-blank public templates.",
    "blank" : "Indicates whether the template is blank. Only applicable to public templates",
    "accessLevel" : "User's permissions on the template",
    "name" : "Template name",
    "description" : "Template description",
    "id" : "Template Id",
    "categories" : [ "string" ],
    "type" : "Type of the template. Only applicable to public templates.",
    "locale" : "Locale of the template.Only applicable to public templates.",
    "tags" : [ "string" ]
  } ],
  "name" : "Folder name",
  "id" : "Folder Id",
  "permalink" : "URL that represents a direct link to the folder in Smartsheet",
  "favorite" : "Returned only if the user has marked the folder as a favorite in their \"Home\" tab (value = true)"
}
```

</details>

## create_folder_workspace

Creates a folder in the specified workspace.

<details><summary>Parameters</summary>

### workspaceId (required)

**Type:** string

### $body

Folder object, limited to the following attribute:
name (string) - required, does not have to be unique

**Type:** object

```json
{
  "reports" : [ {
    "sourceSheets" : [ { } ]
  } ],
  "sheets" : [ {
    "workspace" : { },
    "attachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "columns" : [ {
      "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
      "contactOptions" : [ {
        "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
        "email" : "A parsable email address."
      } ],
      "hidden" : "Indicates whether the column is hidden",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
      "description" : "Column description.",
      "index" : "Column index or position. This number is zero-based.",
      "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
      "title" : "Column title",
      "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
      "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
      "autoNumberFormat" : {
        "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
        "startingNumber" : "The starting number for the auto-id",
        "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
        "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
      },
      "options" : [ "string" ],
      "width" : "Display width of the column in pixels",
      "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
      "id" : "Column Id",
      "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
      "validation" : "Indicates whether validation has been enabled for the column (value = true)",
      "primary" : "Returned only if the column is the Primary Column (value = true)"
    } ],
    "modifiedAt" : "Time that the sheet was modified",
    "discussions" : [ { } ],
    "source" : { },
    "ownerId" : "User Id of the sheet owner",
    "resourceManagementEnabled" : "Indicates that resource management is enabled",
    "ganttEnabled" : "Indicates whether \"Gantt View\" is enabled",
    "createdAt" : "Time that the sheet was created",
    "id" : "Sheet Id",
    "totalRowCount" : "The total number of rows in the sheet",
    "owner" : "Email address of the sheet owner",
    "accessLevel" : "User's permissions on the sheet",
    "readOnly" : "Returned only if the sheet belongs to an expired trial (value = true)",
    "rows" : [ {
      "conditionalFormat" : "Describes this row's conditional format. Only returned if the include query string parameter contains format and this row has a conditional format applied.",
      "attachments" : [ {
        "createdAt" : "A timestamp of when the attachment was originally added",
        "attachmentSubType" : "Attachment sub type",
        "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
        "createdBy" : { },
        "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
        "name" : "Attachment name",
        "id" : "Attachment Id",
        "mimeType" : "Attachment MIME type (PNG, etc.)",
        "sizeInKb" : "The size of the file, if the attachmentType is FILE",
        "parentId" : "The Id of the parent",
        "parentType" : "The type of object the attachment belongs to",
        "url" : "Attachment temporary URL (files only)"
      } ],
      "indent" : "Specifies the number of levels to indent an existing row. You can specify this attribute in a request, but it is never present in a response.",
      "columns" : [ {
        "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
        "contactOptions" : [ {
          "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
          "email" : "A parsable email address."
        } ],
        "hidden" : "Indicates whether the column is hidden",
        "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
        "description" : "Column description.",
        "index" : "Column index or position. This number is zero-based.",
        "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
        "title" : "Column title",
        "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
        "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
        "autoNumberFormat" : {
          "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
          "startingNumber" : "The starting number for the auto-id",
          "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
          "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
        },
        "options" : [ "string" ],
        "width" : "Display width of the column in pixels",
        "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
        "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
        "id" : "Column Id",
        "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
        "validation" : "Indicates whether validation has been enabled for the column (value = true)",
        "primary" : "Returned only if the column is the Primary Column (value = true)"
      } ],
      "modifiedAt" : "Time of last modification",
      "discussions" : [ {
        "commentAttachments" : [ {
          "createdAt" : "A timestamp of when the attachment was originally added",
          "attachmentSubType" : "Attachment sub type",
          "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
          "createdBy" : { },
          "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
          "name" : "Attachment name",
          "id" : "Attachment Id",
          "mimeType" : "Attachment MIME type (PNG, etc.)",
          "sizeInKb" : "The size of the file, if the attachmentType is FILE",
          "parentId" : "The Id of the parent",
          "parentType" : "The type of object the attachment belongs to",
          "url" : "Attachment temporary URL (files only)"
        } ],
        "comments" : [ {
          "createdAt" : "Time of creation",
          "attachments" : [ {
            "createdAt" : "A timestamp of when the attachment was originally added",
            "attachmentSubType" : "Attachment sub type",
            "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
            "createdBy" : { },
            "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
            "name" : "Attachment name",
            "id" : "Attachment Id",
            "mimeType" : "Attachment MIME type (PNG, etc.)",
            "sizeInKb" : "The size of the file, if the attachmentType is FILE",
            "parentId" : "The Id of the parent",
            "parentType" : "The type of object the attachment belongs to",
            "url" : "Attachment temporary URL (files only)"
          } ],
          "createdBy" : { },
          "discussionId" : "Discussion Id",
          "modifiedAt" : "Time of last modification",
          "id" : "Comment Id",
          "text" : "Comment body"
        } ],
        "accessLevel" : "User's permissions on the discussion",
        "createdBy" : { },
        "readOnly" : "Indicates whether the user can modify the discussion",
        "id" : "Discussion Id",
        "lastCommentedAt" : "Time of most recent comment",
        "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
        "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
        "parentType" : "string. Possible values: SHEET | ROW",
        "commentCount" : "The number of comments in the discussion",
        "lastCommentedUser" : {
          "lastLogin" : "Last login time of the current user",
          "lastName" : "User's last name",
          "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
          "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
          "profileImage" : {
            "altText" : "Alternate text for the image",
            "width" : "Original width (in pixels) of the uploaded image",
            "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
            "id" : "Image Id",
            "height" : "Original height (in pixels) of the uploaded image"
          },
          "firstName" : "User's first name",
          "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
          "name" : "User's full name (read-only)",
          "id" : "User Id",
          "sheetCount" : "The number of sheets owned by the current user within the organization account",
          "email" : "User's primary email address",
          "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
          "status" : "User status"
        }
      } ],
      "toBottom" : "Adds or moves the row to the bottom of the sheet. You can specify this attribute in a request, but it is never present in a response.",
      "toTop" : "Adds or moves the row to the top of the sheet. You can specify this attribute in a request, but it is never present in a response.",
      "createdAt" : "Time of creation",
      "expanded" : "Indicates whether the row is expanded or collapsed",
      "inCriticalPath" : "Only returned, with a value of true, if the sheet is a project sheet with dependencies enabled and this row is in the critical path",
      "above" : "Specifies the location for a new or moved row. You can specify this attribute in a request, but it is never present in a response.",
      "outdent" : "Specifies the number of levels to outdent an existing row. You can specify this attribute in a request, but it is never present in a response.",
      "modifiedBy" : {
        "lastLogin" : "Last login time of the current user",
        "lastName" : "User's last name",
        "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
        "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
        "profileImage" : {
          "altText" : "Alternate text for the image",
          "width" : "Original width (in pixels) of the uploaded image",
          "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
          "id" : "Image Id",
          "height" : "Original height (in pixels) of the uploaded image"
        },
        "firstName" : "User's first name",
        "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
        "name" : "User's full name (read-only)",
        "id" : "User Id",
        "sheetCount" : "The number of sheets owned by the current user within the organization account",
        "email" : "User's primary email address",
        "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
        "status" : "User status"
      },
      "id" : "Row Id",
      "locked" : "Indicates whether the row is locked. In a response, a value of true indicates that the row has been locked by the sheet owner or the admin.",
      "rowNumber" : "Row number within the sheet (1-based - starts at 1)",
      "accessLevel" : "User's permission level on the sheet that contains the row",
      "format" : "Format descriptor (see Formatting). Only returned if the include query string parameter contains format and this row has a non-default format applied.",
      "version" : "Sheet version number that is incremented every time a sheet is modified",
      "parentId" : "In a response - the Id of the parent row (if any). In a request - the Id of the desired parent row (used to specify the location for a new or moved row).",
      "cells" : [ {
        "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
        "hyperlink" : { },
        "image" : { },
        "columnId" : "The Id of the column that the cell is located in",
        "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
        "objectValue" : {
          "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
        },
        "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
        "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
        "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
        "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
        "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
        "linkInFromCell" : {
          "sheetName" : "Sheet name of the linked cell",
          "columnId" : "Column Id of the linked cell",
          "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
          "rowId" : "Row Id of the linked cell",
          "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
        },
        "value" : { },
        "linksOutToCells" : [ {
          "sheetName" : "Sheet name of the linked cell",
          "columnId" : "Column Id of the linked cell",
          "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
          "rowId" : "Row Id of the linked cell",
          "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
        } ]
      } ],
      "createdBy" : { },
      "filteredOut" : "true if this row is filtered out by a column filter (and thus is not displayed in the Smartsheet app), false if the row is not filtered out. Only returned if the include query string parameter contains filters.",
      "sheetId" : "Parent sheet Id",
      "lockedForUser" : "Indicates whether the row is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "permalink" : "URL that represents a direct link to the row in SmartsheetOnly returned if the include query string parameter contains rowPermalink.",
      "siblingId" : "In a response - the Id of the previous sibling row at the same hierarchical level of this row (if any). In a request - the Id of the desired sibling row (used to specify the location for a new or moved row)."
    } ],
    "fromId" : "The Id of the template from which to create the sheet. This attribute can be specified in a request, but is never present in a response.",
    "version" : "A number that is incremented every time a sheet is modified",
    "effectiveAttachmentOptions" : [ "string" ],
    "dependenciesEnabled" : "Indicates whether dependencies are enabled",
    "showParentRowsForFilters" : "Returned only if there are column filters on the sheet. Value = true if \"show parent rows\" is enabled for the filters.",
    "userSettings" : {
      "criticalPathEnabled" : "Does this user have \"Show Critical Path\" turned on for this sheet? NOTE: This setting only has an effect on project sheets with dependencies enabled.",
      "displaySummaryTasks" : "Does this user have \"Display Summary Tasks\" turned on for this sheet? Applies only to sheets where \"Calendar View\" has been configured."
    },
    "crossSheetReferences" : [ {
      "startRowId" : "Defines beginning edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
      "startColumnId" : "Defines beginning edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
      "name" : "Friendly name of reference. Auto-generated unless specified in Create Cross-sheet References.",
      "sourceSheetId" : "Sheet Id of source sheet.",
      "endColumnId" : "Defines ending edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
      "endRowId" : "Defines ending edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
      "id" : "Cross-sheet reference Id, guaranteed unique within referencing sheet.",
      "status" : "string. Possible values: OK | BLOCKED | BROKEN | CIRCULAR | DISABLED | INVALID/UNKNOWN | NOT_SHARED"
    } ],
    "name" : "Sheet name",
    "permalink" : "URL that represents a direct link to the sheet in Smartsheet",
    "favorite" : "Returned only if the user has marked this sheet as a favorite in their Home tab (value = true)",
    "projectSettings" : {
      "nonWorkingDays" : [ "string" ],
      "workingDays" : [ "string. Possible values: MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY" ],
      "lengthOfDay" : "Length of a workday for a project sheet. Valid value must be above or equal to 1 hour, and less than or equal to 24 hours."
    }
  } ],
  "folders" : [ { } ],
  "sights" : [ {
    "createdAt" : "Time of creation",
    "backgroundColor" : "The hex color, for instance #E6F5FE",
    "workspace" : {
      "reports" : [ { } ],
      "sheets" : [ { } ],
      "folders" : [ { } ],
      "sights" : [ { } ],
      "accessLevel" : "User's permissions on the workspace",
      "templates" : [ { } ],
      "name" : "Workspace name",
      "id" : "Workspace Id",
      "permalink" : "URL that represents a direct link to the workspace in Smartsheet",
      "favorite" : "Returned only if the user has marked the workspace as a favorite in their \"Home\" tab (value = true)"
    },
    "accessLevel" : "User's permissions on the Sight.",
    "modifiedAt" : "Time of last modification",
    "name" : "Sight name",
    "id" : "Sight Id",
    "columnCount" : "Number of columns that the Sight contains",
    "permalink" : "URL that represents a direct link to the Sight in Smartsheet",
    "widgets" : [ {
      "showTitleIcon" : "True indicates that the client should display the sheet icon in the widget title",
      "xPosition" : "X-coordinate of widget's position on the Sight",
      "Rich Text" : {
        "html" : "The widget content as HTML. The Rich Text widget supports the following subset of HTML tags and CSS Styles: HTML: a - defines a hyperlink, br - inserts a single line break, li - defines a list item, ol - defines an ordered list, p - defines a paragraph, ul - defines an unordered list, span - defines a section in a document. CSS: color, font-family, font-size, font-style, font-weight, text-align, text-decoration."
      },
      "Report" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "reportId" : "Report Id denoting container source",
        "htmlContent" : "HTML snippet to render report"
      },
      "yPosition" : "Y-coordinate of widget's position on the Sight",
      "Title" : {
        "backgroundColor" : "The hex color, for instance #E6F5FE",
        "htmlContent" : "HTML snippet to render title"
      },
      "type" : "Type of widget. See table below to see how UI widget names map to type.",
      "title" : "Title of the widget",
      "viewMode" : "1 indicates content is centered. 2 indicates content is left aligned. Must use a query parameter of level=2 to see this information.",
      "Image" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "fileName" : "Name of the image file",
        "privateId" : "The image private Id",
        "format" : "formatDescriptor",
        "width" : "Original width of the image in pixels",
        "height" : "Original height of the image in pixels"
      },
      "version" : "Widget version number",
      "titleFormat" : "FormatDescriptor",
      "contents" : { },
      "showTitle" : "True indicates that the client should display the widget title. NOTE: This is independent of the title string which may be null or empty.",
      "Shortcut" : {
        "shortcutData" : [ {
          "hyperlink" : {
            "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
            "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
            "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
            "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
          },
          "attachmentType" : "Attachment type",
          "labelFormat" : "formatDescriptor",
          "label" : "Label for the data point",
          "mimeType" : "MIME type if available for attachment type",
          "order" : "The display order for the ShortcutWidgetItem object"
        } ]
      },
      "Web Content" : {
        "url" : "The URL"
      },
      "width" : "Number of columns that the widget occupies on the Sight",
      "Metric" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "columns" : [ {
          "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
          "contactOptions" : [ {
            "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
            "email" : "A parsable email address."
          } ],
          "hidden" : "Indicates whether the column is hidden",
          "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
          "description" : "Column description.",
          "index" : "Column index or position. This number is zero-based.",
          "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
          "title" : "Column title",
          "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
          "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
          "autoNumberFormat" : {
            "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
            "startingNumber" : "The starting number for the auto-id",
            "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
            "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
          },
          "options" : [ "string" ],
          "width" : "Display width of the column in pixels",
          "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
          "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
          "id" : "Column Id",
          "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
          "validation" : "Indicates whether validation has been enabled for the column (value = true)",
          "primary" : "Returned only if the column is the Primary Column (value = true)"
        } ],
        "sheetId" : "The Id of the sheet from which the cell data originates",
        "cellData" : [ {
          "labelFormat" : "formatDescriptor",
          "columnId" : "Column Id for each item",
          "valueFormat" : "formatDescriptor",
          "sheetId" : "Sheet Id for each item",
          "objectValue" : { },
          "label" : "Label for the data point. This is either the column name or a user-provided string",
          "cell" : {
            "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
            "hyperlink" : { },
            "image" : { },
            "columnId" : "The Id of the column that the cell is located in",
            "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
            "objectValue" : {
              "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
            },
            "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
            "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
            "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
            "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
            "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
            "linkInFromCell" : {
              "sheetName" : "Sheet name of the linked cell",
              "columnId" : "Column Id of the linked cell",
              "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
              "rowId" : "Row Id of the linked cell",
              "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
            },
            "value" : { },
            "linksOutToCells" : [ {
              "sheetName" : "Sheet name of the linked cell",
              "columnId" : "Column Id of the linked cell",
              "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
              "rowId" : "Row Id of the linked cell",
              "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
            } ]
          },
          "dataSource" : "CELL",
          "rowId" : "Row Id for each item",
          "order" : "The display order for the CellDataItem"
        } ]
      },
      "id" : "Widget Id",
      "Chart" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "reportId" : "Report Id denoting container source, if applicable",
        "legend" : "The location in the widget where Smartsheet renders the legend, for example, RIGHT",
        "series" : [ { } ],
        "axes" : [ { } ],
        "sheetId" : "Sheet Id denoting container source, if applicable",
        "includedColumnIds" : [ "number" ],
        "selectionRanges" : [ {
          "sourceRowId2" : "Defines ending edge of range when specifying one or more rows.",
          "sourceColumnId2" : "Defines ending edge of range when specifying one or more columns.",
          "sourceRowId1" : "Defines beginning edge of range when specifying one or more rows.",
          "sourceColumnId1" : "Defines beginning edge of range when specifying one or more columns."
        } ]
      },
      "height" : "Number of rows that the widget occupies on the Sight"
    } ],
    "favorite" : "Indicates whether the user has marked the Sight as a favorite"
  } ],
  "templates" : [ {
    "globalTemplate" : "Type of global template. Only applicable to blank public templates.",
    "image" : "URL to the small preview image for this template. Only applicable to non-blank public templates.",
    "largeImage" : "URL to the large preview image for this template. Only applicable to non-blank public templates.",
    "blank" : "Indicates whether the template is blank. Only applicable to public templates",
    "accessLevel" : "User's permissions on the template",
    "name" : "Template name",
    "description" : "Template description",
    "id" : "Template Id",
    "categories" : [ "string" ],
    "type" : "Type of the template. Only applicable to public templates.",
    "locale" : "Locale of the template.Only applicable to public templates.",
    "tags" : [ "string" ]
  } ],
  "name" : "Folder name",
  "id" : "Folder Id",
  "permalink" : "URL that represents a direct link to the folder in Smartsheet",
  "favorite" : "Returned only if the user has marked the folder as a favorite in their \"Home\" tab (value = true)"
}
```

</details>

## create_group

Creates a new group.

<details><summary>Parameters</summary>

### $body

Group object, limited to the following attributes:
name (required) -- must be unique within the organization account
description (optional)
members (optional) -- array of GroupMember objects, each limited to the following attribute:email

**Type:** object

```json
{
  "owner" : "Group owner’s email address",
  "createdAt" : "Time of creation",
  "modifiedAt" : "Time of last modification",
  "members" : [ {
    "firstName" : "Group member's first name",
    "lastName" : "Group member's last name",
    "name" : "Group member's full name",
    "id" : "Group member's user Id",
    "email" : "Group member's email address"
  } ],
  "name" : "Group name",
  "description" : "Group description",
  "id" : "Group Id",
  "ownerId" : "Group owner's user Id"
}
```

</details>

## create_sheet_in_folder_from_template

Creates a sheet in the specified folder, from the specified template.

<details><summary>Parameters</summary>

### folderId (required)

**Type:** string

### $body

Sheet object, limited to the following attributes:
fromId (required) - the Id of the template from which to create the sheet
name (required) - does not have to be unique

**Type:** object

```json
{
  "workspace" : { },
  "attachments" : [ {
    "createdAt" : "A timestamp of when the attachment was originally added",
    "attachmentSubType" : "Attachment sub type",
    "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
    "createdBy" : { },
    "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
    "name" : "Attachment name",
    "id" : "Attachment Id",
    "mimeType" : "Attachment MIME type (PNG, etc.)",
    "sizeInKb" : "The size of the file, if the attachmentType is FILE",
    "parentId" : "The Id of the parent",
    "parentType" : "The type of object the attachment belongs to",
    "url" : "Attachment temporary URL (files only)"
  } ],
  "columns" : [ {
    "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
    "contactOptions" : [ {
      "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
      "email" : "A parsable email address."
    } ],
    "hidden" : "Indicates whether the column is hidden",
    "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
    "description" : "Column description.",
    "index" : "Column index or position. This number is zero-based.",
    "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
    "title" : "Column title",
    "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
    "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
    "autoNumberFormat" : {
      "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
      "startingNumber" : "The starting number for the auto-id",
      "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
      "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
    },
    "options" : [ "string" ],
    "width" : "Display width of the column in pixels",
    "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
    "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
    "id" : "Column Id",
    "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
    "validation" : "Indicates whether validation has been enabled for the column (value = true)",
    "primary" : "Returned only if the column is the Primary Column (value = true)"
  } ],
  "modifiedAt" : "Time that the sheet was modified",
  "discussions" : [ { } ],
  "source" : { },
  "ownerId" : "User Id of the sheet owner",
  "resourceManagementEnabled" : "Indicates that resource management is enabled",
  "ganttEnabled" : "Indicates whether \"Gantt View\" is enabled",
  "createdAt" : "Time that the sheet was created",
  "id" : "Sheet Id",
  "totalRowCount" : "The total number of rows in the sheet",
  "owner" : "Email address of the sheet owner",
  "accessLevel" : "User's permissions on the sheet",
  "readOnly" : "Returned only if the sheet belongs to an expired trial (value = true)",
  "rows" : [ {
    "conditionalFormat" : "Describes this row's conditional format. Only returned if the include query string parameter contains format and this row has a conditional format applied.",
    "attachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "indent" : "Specifies the number of levels to indent an existing row. You can specify this attribute in a request, but it is never present in a response.",
    "columns" : [ {
      "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
      "contactOptions" : [ {
        "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
        "email" : "A parsable email address."
      } ],
      "hidden" : "Indicates whether the column is hidden",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
      "description" : "Column description.",
      "index" : "Column index or position. This number is zero-based.",
      "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
      "title" : "Column title",
      "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
      "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
      "autoNumberFormat" : {
        "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
        "startingNumber" : "The starting number for the auto-id",
        "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
        "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
      },
      "options" : [ "string" ],
      "width" : "Display width of the column in pixels",
      "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
      "id" : "Column Id",
      "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
      "validation" : "Indicates whether validation has been enabled for the column (value = true)",
      "primary" : "Returned only if the column is the Primary Column (value = true)"
    } ],
    "modifiedAt" : "Time of last modification",
    "discussions" : [ {
      "commentAttachments" : [ {
        "createdAt" : "A timestamp of when the attachment was originally added",
        "attachmentSubType" : "Attachment sub type",
        "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
        "createdBy" : { },
        "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
        "name" : "Attachment name",
        "id" : "Attachment Id",
        "mimeType" : "Attachment MIME type (PNG, etc.)",
        "sizeInKb" : "The size of the file, if the attachmentType is FILE",
        "parentId" : "The Id of the parent",
        "parentType" : "The type of object the attachment belongs to",
        "url" : "Attachment temporary URL (files only)"
      } ],
      "comments" : [ {
        "createdAt" : "Time of creation",
        "attachments" : [ {
          "createdAt" : "A timestamp of when the attachment was originally added",
          "attachmentSubType" : "Attachment sub type",
          "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
          "createdBy" : { },
          "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
          "name" : "Attachment name",
          "id" : "Attachment Id",
          "mimeType" : "Attachment MIME type (PNG, etc.)",
          "sizeInKb" : "The size of the file, if the attachmentType is FILE",
          "parentId" : "The Id of the parent",
          "parentType" : "The type of object the attachment belongs to",
          "url" : "Attachment temporary URL (files only)"
        } ],
        "createdBy" : { },
        "discussionId" : "Discussion Id",
        "modifiedAt" : "Time of last modification",
        "id" : "Comment Id",
        "text" : "Comment body"
      } ],
      "accessLevel" : "User's permissions on the discussion",
      "createdBy" : { },
      "readOnly" : "Indicates whether the user can modify the discussion",
      "id" : "Discussion Id",
      "lastCommentedAt" : "Time of most recent comment",
      "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
      "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
      "parentType" : "string. Possible values: SHEET | ROW",
      "commentCount" : "The number of comments in the discussion",
      "lastCommentedUser" : {
        "lastLogin" : "Last login time of the current user",
        "lastName" : "User's last name",
        "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
        "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
        "profileImage" : {
          "altText" : "Alternate text for the image",
          "width" : "Original width (in pixels) of the uploaded image",
          "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
          "id" : "Image Id",
          "height" : "Original height (in pixels) of the uploaded image"
        },
        "firstName" : "User's first name",
        "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
        "name" : "User's full name (read-only)",
        "id" : "User Id",
        "sheetCount" : "The number of sheets owned by the current user within the organization account",
        "email" : "User's primary email address",
        "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
        "status" : "User status"
      }
    } ],
    "toBottom" : "Adds or moves the row to the bottom of the sheet. You can specify this attribute in a request, but it is never present in a response.",
    "toTop" : "Adds or moves the row to the top of the sheet. You can specify this attribute in a request, but it is never present in a response.",
    "createdAt" : "Time of creation",
    "expanded" : "Indicates whether the row is expanded or collapsed",
    "inCriticalPath" : "Only returned, with a value of true, if the sheet is a project sheet with dependencies enabled and this row is in the critical path",
    "above" : "Specifies the location for a new or moved row. You can specify this attribute in a request, but it is never present in a response.",
    "outdent" : "Specifies the number of levels to outdent an existing row. You can specify this attribute in a request, but it is never present in a response.",
    "modifiedBy" : {
      "lastLogin" : "Last login time of the current user",
      "lastName" : "User's last name",
      "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
      "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
      "profileImage" : {
        "altText" : "Alternate text for the image",
        "width" : "Original width (in pixels) of the uploaded image",
        "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
        "id" : "Image Id",
        "height" : "Original height (in pixels) of the uploaded image"
      },
      "firstName" : "User's first name",
      "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
      "name" : "User's full name (read-only)",
      "id" : "User Id",
      "sheetCount" : "The number of sheets owned by the current user within the organization account",
      "email" : "User's primary email address",
      "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
      "status" : "User status"
    },
    "id" : "Row Id",
    "locked" : "Indicates whether the row is locked. In a response, a value of true indicates that the row has been locked by the sheet owner or the admin.",
    "rowNumber" : "Row number within the sheet (1-based - starts at 1)",
    "accessLevel" : "User's permission level on the sheet that contains the row",
    "format" : "Format descriptor (see Formatting). Only returned if the include query string parameter contains format and this row has a non-default format applied.",
    "version" : "Sheet version number that is incremented every time a sheet is modified",
    "parentId" : "In a response - the Id of the parent row (if any). In a request - the Id of the desired parent row (used to specify the location for a new or moved row).",
    "cells" : [ {
      "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
      "hyperlink" : { },
      "image" : { },
      "columnId" : "The Id of the column that the cell is located in",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
      "objectValue" : {
        "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
      },
      "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
      "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
      "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
      "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
      "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
      "linkInFromCell" : {
        "sheetName" : "Sheet name of the linked cell",
        "columnId" : "Column Id of the linked cell",
        "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
        "rowId" : "Row Id of the linked cell",
        "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
      },
      "value" : { },
      "linksOutToCells" : [ {
        "sheetName" : "Sheet name of the linked cell",
        "columnId" : "Column Id of the linked cell",
        "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
        "rowId" : "Row Id of the linked cell",
        "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
      } ]
    } ],
    "createdBy" : { },
    "filteredOut" : "true if this row is filtered out by a column filter (and thus is not displayed in the Smartsheet app), false if the row is not filtered out. Only returned if the include query string parameter contains filters.",
    "sheetId" : "Parent sheet Id",
    "lockedForUser" : "Indicates whether the row is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
    "permalink" : "URL that represents a direct link to the row in SmartsheetOnly returned if the include query string parameter contains rowPermalink.",
    "siblingId" : "In a response - the Id of the previous sibling row at the same hierarchical level of this row (if any). In a request - the Id of the desired sibling row (used to specify the location for a new or moved row)."
  } ],
  "fromId" : "The Id of the template from which to create the sheet. This attribute can be specified in a request, but is never present in a response.",
  "version" : "A number that is incremented every time a sheet is modified",
  "effectiveAttachmentOptions" : [ "string" ],
  "dependenciesEnabled" : "Indicates whether dependencies are enabled",
  "showParentRowsForFilters" : "Returned only if there are column filters on the sheet. Value = true if \"show parent rows\" is enabled for the filters.",
  "userSettings" : {
    "criticalPathEnabled" : "Does this user have \"Show Critical Path\" turned on for this sheet? NOTE: This setting only has an effect on project sheets with dependencies enabled.",
    "displaySummaryTasks" : "Does this user have \"Display Summary Tasks\" turned on for this sheet? Applies only to sheets where \"Calendar View\" has been configured."
  },
  "crossSheetReferences" : [ {
    "startRowId" : "Defines beginning edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
    "startColumnId" : "Defines beginning edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
    "name" : "Friendly name of reference. Auto-generated unless specified in Create Cross-sheet References.",
    "sourceSheetId" : "Sheet Id of source sheet.",
    "endColumnId" : "Defines ending edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
    "endRowId" : "Defines ending edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
    "id" : "Cross-sheet reference Id, guaranteed unique within referencing sheet.",
    "status" : "string. Possible values: OK | BLOCKED | BROKEN | CIRCULAR | DISABLED | INVALID/UNKNOWN | NOT_SHARED"
  } ],
  "name" : "Sheet name",
  "permalink" : "URL that represents a direct link to the sheet in Smartsheet",
  "favorite" : "Returned only if the user has marked this sheet as a favorite in their Home tab (value = true)",
  "projectSettings" : {
    "nonWorkingDays" : [ "string" ],
    "workingDays" : [ "string. Possible values: MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY" ],
    "lengthOfDay" : "Length of a workday for a project sheet. Valid value must be above or equal to 1 hour, and less than or equal to 24 hours."
  }
}
```

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: attachments | cellLinks | data | discussions | forms" ]
```

</details>

## create_sheet_in_quot_sheets_quot_folder_from_template

Creates a sheet in the user's Sheets folder (Home), from the specified template. For subfolders, use Create Sheet in Folder from Template.

<details><summary>Parameters</summary>

### $body

Sheet object, limited to the following attributes:
fromId (required) - the Id of the template from which to create the sheet
name (required) - does not have to be unique

**Type:** object

```json
{
  "workspace" : { },
  "attachments" : [ {
    "createdAt" : "A timestamp of when the attachment was originally added",
    "attachmentSubType" : "Attachment sub type",
    "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
    "createdBy" : { },
    "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
    "name" : "Attachment name",
    "id" : "Attachment Id",
    "mimeType" : "Attachment MIME type (PNG, etc.)",
    "sizeInKb" : "The size of the file, if the attachmentType is FILE",
    "parentId" : "The Id of the parent",
    "parentType" : "The type of object the attachment belongs to",
    "url" : "Attachment temporary URL (files only)"
  } ],
  "columns" : [ {
    "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
    "contactOptions" : [ {
      "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
      "email" : "A parsable email address."
    } ],
    "hidden" : "Indicates whether the column is hidden",
    "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
    "description" : "Column description.",
    "index" : "Column index or position. This number is zero-based.",
    "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
    "title" : "Column title",
    "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
    "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
    "autoNumberFormat" : {
      "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
      "startingNumber" : "The starting number for the auto-id",
      "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
      "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
    },
    "options" : [ "string" ],
    "width" : "Display width of the column in pixels",
    "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
    "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
    "id" : "Column Id",
    "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
    "validation" : "Indicates whether validation has been enabled for the column (value = true)",
    "primary" : "Returned only if the column is the Primary Column (value = true)"
  } ],
  "modifiedAt" : "Time that the sheet was modified",
  "discussions" : [ { } ],
  "source" : { },
  "ownerId" : "User Id of the sheet owner",
  "resourceManagementEnabled" : "Indicates that resource management is enabled",
  "ganttEnabled" : "Indicates whether \"Gantt View\" is enabled",
  "createdAt" : "Time that the sheet was created",
  "id" : "Sheet Id",
  "totalRowCount" : "The total number of rows in the sheet",
  "owner" : "Email address of the sheet owner",
  "accessLevel" : "User's permissions on the sheet",
  "readOnly" : "Returned only if the sheet belongs to an expired trial (value = true)",
  "rows" : [ {
    "conditionalFormat" : "Describes this row's conditional format. Only returned if the include query string parameter contains format and this row has a conditional format applied.",
    "attachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "indent" : "Specifies the number of levels to indent an existing row. You can specify this attribute in a request, but it is never present in a response.",
    "columns" : [ {
      "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
      "contactOptions" : [ {
        "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
        "email" : "A parsable email address."
      } ],
      "hidden" : "Indicates whether the column is hidden",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
      "description" : "Column description.",
      "index" : "Column index or position. This number is zero-based.",
      "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
      "title" : "Column title",
      "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
      "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
      "autoNumberFormat" : {
        "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
        "startingNumber" : "The starting number for the auto-id",
        "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
        "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
      },
      "options" : [ "string" ],
      "width" : "Display width of the column in pixels",
      "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
      "id" : "Column Id",
      "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
      "validation" : "Indicates whether validation has been enabled for the column (value = true)",
      "primary" : "Returned only if the column is the Primary Column (value = true)"
    } ],
    "modifiedAt" : "Time of last modification",
    "discussions" : [ {
      "commentAttachments" : [ {
        "createdAt" : "A timestamp of when the attachment was originally added",
        "attachmentSubType" : "Attachment sub type",
        "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
        "createdBy" : { },
        "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
        "name" : "Attachment name",
        "id" : "Attachment Id",
        "mimeType" : "Attachment MIME type (PNG, etc.)",
        "sizeInKb" : "The size of the file, if the attachmentType is FILE",
        "parentId" : "The Id of the parent",
        "parentType" : "The type of object the attachment belongs to",
        "url" : "Attachment temporary URL (files only)"
      } ],
      "comments" : [ {
        "createdAt" : "Time of creation",
        "attachments" : [ {
          "createdAt" : "A timestamp of when the attachment was originally added",
          "attachmentSubType" : "Attachment sub type",
          "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
          "createdBy" : { },
          "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
          "name" : "Attachment name",
          "id" : "Attachment Id",
          "mimeType" : "Attachment MIME type (PNG, etc.)",
          "sizeInKb" : "The size of the file, if the attachmentType is FILE",
          "parentId" : "The Id of the parent",
          "parentType" : "The type of object the attachment belongs to",
          "url" : "Attachment temporary URL (files only)"
        } ],
        "createdBy" : { },
        "discussionId" : "Discussion Id",
        "modifiedAt" : "Time of last modification",
        "id" : "Comment Id",
        "text" : "Comment body"
      } ],
      "accessLevel" : "User's permissions on the discussion",
      "createdBy" : { },
      "readOnly" : "Indicates whether the user can modify the discussion",
      "id" : "Discussion Id",
      "lastCommentedAt" : "Time of most recent comment",
      "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
      "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
      "parentType" : "string. Possible values: SHEET | ROW",
      "commentCount" : "The number of comments in the discussion",
      "lastCommentedUser" : {
        "lastLogin" : "Last login time of the current user",
        "lastName" : "User's last name",
        "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
        "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
        "profileImage" : {
          "altText" : "Alternate text for the image",
          "width" : "Original width (in pixels) of the uploaded image",
          "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
          "id" : "Image Id",
          "height" : "Original height (in pixels) of the uploaded image"
        },
        "firstName" : "User's first name",
        "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
        "name" : "User's full name (read-only)",
        "id" : "User Id",
        "sheetCount" : "The number of sheets owned by the current user within the organization account",
        "email" : "User's primary email address",
        "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
        "status" : "User status"
      }
    } ],
    "toBottom" : "Adds or moves the row to the bottom of the sheet. You can specify this attribute in a request, but it is never present in a response.",
    "toTop" : "Adds or moves the row to the top of the sheet. You can specify this attribute in a request, but it is never present in a response.",
    "createdAt" : "Time of creation",
    "expanded" : "Indicates whether the row is expanded or collapsed",
    "inCriticalPath" : "Only returned, with a value of true, if the sheet is a project sheet with dependencies enabled and this row is in the critical path",
    "above" : "Specifies the location for a new or moved row. You can specify this attribute in a request, but it is never present in a response.",
    "outdent" : "Specifies the number of levels to outdent an existing row. You can specify this attribute in a request, but it is never present in a response.",
    "modifiedBy" : {
      "lastLogin" : "Last login time of the current user",
      "lastName" : "User's last name",
      "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
      "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
      "profileImage" : {
        "altText" : "Alternate text for the image",
        "width" : "Original width (in pixels) of the uploaded image",
        "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
        "id" : "Image Id",
        "height" : "Original height (in pixels) of the uploaded image"
      },
      "firstName" : "User's first name",
      "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
      "name" : "User's full name (read-only)",
      "id" : "User Id",
      "sheetCount" : "The number of sheets owned by the current user within the organization account",
      "email" : "User's primary email address",
      "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
      "status" : "User status"
    },
    "id" : "Row Id",
    "locked" : "Indicates whether the row is locked. In a response, a value of true indicates that the row has been locked by the sheet owner or the admin.",
    "rowNumber" : "Row number within the sheet (1-based - starts at 1)",
    "accessLevel" : "User's permission level on the sheet that contains the row",
    "format" : "Format descriptor (see Formatting). Only returned if the include query string parameter contains format and this row has a non-default format applied.",
    "version" : "Sheet version number that is incremented every time a sheet is modified",
    "parentId" : "In a response - the Id of the parent row (if any). In a request - the Id of the desired parent row (used to specify the location for a new or moved row).",
    "cells" : [ {
      "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
      "hyperlink" : { },
      "image" : { },
      "columnId" : "The Id of the column that the cell is located in",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
      "objectValue" : {
        "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
      },
      "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
      "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
      "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
      "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
      "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
      "linkInFromCell" : {
        "sheetName" : "Sheet name of the linked cell",
        "columnId" : "Column Id of the linked cell",
        "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
        "rowId" : "Row Id of the linked cell",
        "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
      },
      "value" : { },
      "linksOutToCells" : [ {
        "sheetName" : "Sheet name of the linked cell",
        "columnId" : "Column Id of the linked cell",
        "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
        "rowId" : "Row Id of the linked cell",
        "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
      } ]
    } ],
    "createdBy" : { },
    "filteredOut" : "true if this row is filtered out by a column filter (and thus is not displayed in the Smartsheet app), false if the row is not filtered out. Only returned if the include query string parameter contains filters.",
    "sheetId" : "Parent sheet Id",
    "lockedForUser" : "Indicates whether the row is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
    "permalink" : "URL that represents a direct link to the row in SmartsheetOnly returned if the include query string parameter contains rowPermalink.",
    "siblingId" : "In a response - the Id of the previous sibling row at the same hierarchical level of this row (if any). In a request - the Id of the desired sibling row (used to specify the location for a new or moved row)."
  } ],
  "fromId" : "The Id of the template from which to create the sheet. This attribute can be specified in a request, but is never present in a response.",
  "version" : "A number that is incremented every time a sheet is modified",
  "effectiveAttachmentOptions" : [ "string" ],
  "dependenciesEnabled" : "Indicates whether dependencies are enabled",
  "showParentRowsForFilters" : "Returned only if there are column filters on the sheet. Value = true if \"show parent rows\" is enabled for the filters.",
  "userSettings" : {
    "criticalPathEnabled" : "Does this user have \"Show Critical Path\" turned on for this sheet? NOTE: This setting only has an effect on project sheets with dependencies enabled.",
    "displaySummaryTasks" : "Does this user have \"Display Summary Tasks\" turned on for this sheet? Applies only to sheets where \"Calendar View\" has been configured."
  },
  "crossSheetReferences" : [ {
    "startRowId" : "Defines beginning edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
    "startColumnId" : "Defines beginning edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
    "name" : "Friendly name of reference. Auto-generated unless specified in Create Cross-sheet References.",
    "sourceSheetId" : "Sheet Id of source sheet.",
    "endColumnId" : "Defines ending edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
    "endRowId" : "Defines ending edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
    "id" : "Cross-sheet reference Id, guaranteed unique within referencing sheet.",
    "status" : "string. Possible values: OK | BLOCKED | BROKEN | CIRCULAR | DISABLED | INVALID/UNKNOWN | NOT_SHARED"
  } ],
  "name" : "Sheet name",
  "permalink" : "URL that represents a direct link to the sheet in Smartsheet",
  "favorite" : "Returned only if the user has marked this sheet as a favorite in their Home tab (value = true)",
  "projectSettings" : {
    "nonWorkingDays" : [ "string" ],
    "workingDays" : [ "string. Possible values: MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY" ],
    "lengthOfDay" : "Length of a workday for a project sheet. Valid value must be above or equal to 1 hour, and less than or equal to 24 hours."
  }
}
```

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: attachments | cellLinks | data | discussions | forms" ]
```

</details>

## create_sheet_in_workspace_from_template

Creates a sheet at the top-level of the specified workspace, from the specified template. For subfolders, use Create Sheet in Folder from Template.

<details><summary>Parameters</summary>

### workspaceId (required)

**Type:** string

### $body

Sheet object, limited to the following attributes:
fromId (required) - the Id of the template from which to create the sheet
name (required) - does not have to be unique

**Type:** object

```json
{
  "workspace" : { },
  "attachments" : [ {
    "createdAt" : "A timestamp of when the attachment was originally added",
    "attachmentSubType" : "Attachment sub type",
    "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
    "createdBy" : { },
    "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
    "name" : "Attachment name",
    "id" : "Attachment Id",
    "mimeType" : "Attachment MIME type (PNG, etc.)",
    "sizeInKb" : "The size of the file, if the attachmentType is FILE",
    "parentId" : "The Id of the parent",
    "parentType" : "The type of object the attachment belongs to",
    "url" : "Attachment temporary URL (files only)"
  } ],
  "columns" : [ {
    "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
    "contactOptions" : [ {
      "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
      "email" : "A parsable email address."
    } ],
    "hidden" : "Indicates whether the column is hidden",
    "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
    "description" : "Column description.",
    "index" : "Column index or position. This number is zero-based.",
    "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
    "title" : "Column title",
    "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
    "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
    "autoNumberFormat" : {
      "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
      "startingNumber" : "The starting number for the auto-id",
      "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
      "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
    },
    "options" : [ "string" ],
    "width" : "Display width of the column in pixels",
    "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
    "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
    "id" : "Column Id",
    "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
    "validation" : "Indicates whether validation has been enabled for the column (value = true)",
    "primary" : "Returned only if the column is the Primary Column (value = true)"
  } ],
  "modifiedAt" : "Time that the sheet was modified",
  "discussions" : [ { } ],
  "source" : { },
  "ownerId" : "User Id of the sheet owner",
  "resourceManagementEnabled" : "Indicates that resource management is enabled",
  "ganttEnabled" : "Indicates whether \"Gantt View\" is enabled",
  "createdAt" : "Time that the sheet was created",
  "id" : "Sheet Id",
  "totalRowCount" : "The total number of rows in the sheet",
  "owner" : "Email address of the sheet owner",
  "accessLevel" : "User's permissions on the sheet",
  "readOnly" : "Returned only if the sheet belongs to an expired trial (value = true)",
  "rows" : [ {
    "conditionalFormat" : "Describes this row's conditional format. Only returned if the include query string parameter contains format and this row has a conditional format applied.",
    "attachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "indent" : "Specifies the number of levels to indent an existing row. You can specify this attribute in a request, but it is never present in a response.",
    "columns" : [ {
      "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
      "contactOptions" : [ {
        "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
        "email" : "A parsable email address."
      } ],
      "hidden" : "Indicates whether the column is hidden",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
      "description" : "Column description.",
      "index" : "Column index or position. This number is zero-based.",
      "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
      "title" : "Column title",
      "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
      "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
      "autoNumberFormat" : {
        "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
        "startingNumber" : "The starting number for the auto-id",
        "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
        "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
      },
      "options" : [ "string" ],
      "width" : "Display width of the column in pixels",
      "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
      "id" : "Column Id",
      "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
      "validation" : "Indicates whether validation has been enabled for the column (value = true)",
      "primary" : "Returned only if the column is the Primary Column (value = true)"
    } ],
    "modifiedAt" : "Time of last modification",
    "discussions" : [ {
      "commentAttachments" : [ {
        "createdAt" : "A timestamp of when the attachment was originally added",
        "attachmentSubType" : "Attachment sub type",
        "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
        "createdBy" : { },
        "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
        "name" : "Attachment name",
        "id" : "Attachment Id",
        "mimeType" : "Attachment MIME type (PNG, etc.)",
        "sizeInKb" : "The size of the file, if the attachmentType is FILE",
        "parentId" : "The Id of the parent",
        "parentType" : "The type of object the attachment belongs to",
        "url" : "Attachment temporary URL (files only)"
      } ],
      "comments" : [ {
        "createdAt" : "Time of creation",
        "attachments" : [ {
          "createdAt" : "A timestamp of when the attachment was originally added",
          "attachmentSubType" : "Attachment sub type",
          "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
          "createdBy" : { },
          "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
          "name" : "Attachment name",
          "id" : "Attachment Id",
          "mimeType" : "Attachment MIME type (PNG, etc.)",
          "sizeInKb" : "The size of the file, if the attachmentType is FILE",
          "parentId" : "The Id of the parent",
          "parentType" : "The type of object the attachment belongs to",
          "url" : "Attachment temporary URL (files only)"
        } ],
        "createdBy" : { },
        "discussionId" : "Discussion Id",
        "modifiedAt" : "Time of last modification",
        "id" : "Comment Id",
        "text" : "Comment body"
      } ],
      "accessLevel" : "User's permissions on the discussion",
      "createdBy" : { },
      "readOnly" : "Indicates whether the user can modify the discussion",
      "id" : "Discussion Id",
      "lastCommentedAt" : "Time of most recent comment",
      "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
      "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
      "parentType" : "string. Possible values: SHEET | ROW",
      "commentCount" : "The number of comments in the discussion",
      "lastCommentedUser" : {
        "lastLogin" : "Last login time of the current user",
        "lastName" : "User's last name",
        "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
        "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
        "profileImage" : {
          "altText" : "Alternate text for the image",
          "width" : "Original width (in pixels) of the uploaded image",
          "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
          "id" : "Image Id",
          "height" : "Original height (in pixels) of the uploaded image"
        },
        "firstName" : "User's first name",
        "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
        "name" : "User's full name (read-only)",
        "id" : "User Id",
        "sheetCount" : "The number of sheets owned by the current user within the organization account",
        "email" : "User's primary email address",
        "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
        "status" : "User status"
      }
    } ],
    "toBottom" : "Adds or moves the row to the bottom of the sheet. You can specify this attribute in a request, but it is never present in a response.",
    "toTop" : "Adds or moves the row to the top of the sheet. You can specify this attribute in a request, but it is never present in a response.",
    "createdAt" : "Time of creation",
    "expanded" : "Indicates whether the row is expanded or collapsed",
    "inCriticalPath" : "Only returned, with a value of true, if the sheet is a project sheet with dependencies enabled and this row is in the critical path",
    "above" : "Specifies the location for a new or moved row. You can specify this attribute in a request, but it is never present in a response.",
    "outdent" : "Specifies the number of levels to outdent an existing row. You can specify this attribute in a request, but it is never present in a response.",
    "modifiedBy" : {
      "lastLogin" : "Last login time of the current user",
      "lastName" : "User's last name",
      "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
      "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
      "profileImage" : {
        "altText" : "Alternate text for the image",
        "width" : "Original width (in pixels) of the uploaded image",
        "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
        "id" : "Image Id",
        "height" : "Original height (in pixels) of the uploaded image"
      },
      "firstName" : "User's first name",
      "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
      "name" : "User's full name (read-only)",
      "id" : "User Id",
      "sheetCount" : "The number of sheets owned by the current user within the organization account",
      "email" : "User's primary email address",
      "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
      "status" : "User status"
    },
    "id" : "Row Id",
    "locked" : "Indicates whether the row is locked. In a response, a value of true indicates that the row has been locked by the sheet owner or the admin.",
    "rowNumber" : "Row number within the sheet (1-based - starts at 1)",
    "accessLevel" : "User's permission level on the sheet that contains the row",
    "format" : "Format descriptor (see Formatting). Only returned if the include query string parameter contains format and this row has a non-default format applied.",
    "version" : "Sheet version number that is incremented every time a sheet is modified",
    "parentId" : "In a response - the Id of the parent row (if any). In a request - the Id of the desired parent row (used to specify the location for a new or moved row).",
    "cells" : [ {
      "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
      "hyperlink" : { },
      "image" : { },
      "columnId" : "The Id of the column that the cell is located in",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
      "objectValue" : {
        "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
      },
      "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
      "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
      "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
      "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
      "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
      "linkInFromCell" : {
        "sheetName" : "Sheet name of the linked cell",
        "columnId" : "Column Id of the linked cell",
        "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
        "rowId" : "Row Id of the linked cell",
        "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
      },
      "value" : { },
      "linksOutToCells" : [ {
        "sheetName" : "Sheet name of the linked cell",
        "columnId" : "Column Id of the linked cell",
        "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
        "rowId" : "Row Id of the linked cell",
        "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
      } ]
    } ],
    "createdBy" : { },
    "filteredOut" : "true if this row is filtered out by a column filter (and thus is not displayed in the Smartsheet app), false if the row is not filtered out. Only returned if the include query string parameter contains filters.",
    "sheetId" : "Parent sheet Id",
    "lockedForUser" : "Indicates whether the row is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
    "permalink" : "URL that represents a direct link to the row in SmartsheetOnly returned if the include query string parameter contains rowPermalink.",
    "siblingId" : "In a response - the Id of the previous sibling row at the same hierarchical level of this row (if any). In a request - the Id of the desired sibling row (used to specify the location for a new or moved row)."
  } ],
  "fromId" : "The Id of the template from which to create the sheet. This attribute can be specified in a request, but is never present in a response.",
  "version" : "A number that is incremented every time a sheet is modified",
  "effectiveAttachmentOptions" : [ "string" ],
  "dependenciesEnabled" : "Indicates whether dependencies are enabled",
  "showParentRowsForFilters" : "Returned only if there are column filters on the sheet. Value = true if \"show parent rows\" is enabled for the filters.",
  "userSettings" : {
    "criticalPathEnabled" : "Does this user have \"Show Critical Path\" turned on for this sheet? NOTE: This setting only has an effect on project sheets with dependencies enabled.",
    "displaySummaryTasks" : "Does this user have \"Display Summary Tasks\" turned on for this sheet? Applies only to sheets where \"Calendar View\" has been configured."
  },
  "crossSheetReferences" : [ {
    "startRowId" : "Defines beginning edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
    "startColumnId" : "Defines beginning edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
    "name" : "Friendly name of reference. Auto-generated unless specified in Create Cross-sheet References.",
    "sourceSheetId" : "Sheet Id of source sheet.",
    "endColumnId" : "Defines ending edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
    "endRowId" : "Defines ending edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
    "id" : "Cross-sheet reference Id, guaranteed unique within referencing sheet.",
    "status" : "string. Possible values: OK | BLOCKED | BROKEN | CIRCULAR | DISABLED | INVALID/UNKNOWN | NOT_SHARED"
  } ],
  "name" : "Sheet name",
  "permalink" : "URL that represents a direct link to the sheet in Smartsheet",
  "favorite" : "Returned only if the user has marked this sheet as a favorite in their Home tab (value = true)",
  "projectSettings" : {
    "nonWorkingDays" : [ "string" ],
    "workingDays" : [ "string. Possible values: MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY" ],
    "lengthOfDay" : "Length of a workday for a project sheet. Valid value must be above or equal to 1 hour, and less than or equal to 24 hours."
  }
}
```

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: attachments | cellLinks | data | discussions | forms" ]
```

</details>

## create_update_request

Creates an update request for the specified rows within the sheet. An email notification (containing a link to the update request) is sent to the specified recipients according to the specified schedule.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

UpdateRequest object.

The UpdateRequest object in the request body must specify one or more of the following attributes:
rowIds: number[]
sendTo: Recipient[]
One or more of the followings:columnIds: number[]includeAttachments: trueincludeDiscussions: trueThe following attributes have the following values when not specified:
ccMe: false
message: Please update the following rows in my online sheet.
subject: Update Request: {Sheet Name}When the Schedule object is not specified, the request is sent to the recipients immediately.

**Type:** object

```json
{
  "createdAt" : "The date and time for when this request was originally created. Read-only.",
  "schedule" : {
    "dayOfMonth" : "The day within the month",
    "dayDescriptors" : [ "string. Possible values: DAY | WEEKDAY | WEEKEND | SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY" ],
    "dayOrdinal" : "This attribute is applicable to the MONTHLY schedule type.",
    "lastSentAt" : "The date and time for when the last request was sent. Read-only.",
    "repeatEvery" : "Frequency on which the request is delivered. The unit is a function of the type attribute.",
    "type" : "Schedule type",
    "endAt" : "The date, time, and time zone at which the delivery schedule ends. It must be a valid ISO-8601 date and time with an offset (YYYY-MM-DDThh:mm:ssTZD).",
    "nextSendAt" : "The date and time for when the next request is scheduled to send. Read-only.",
    "startAt" : "The date, time, and time zone at which the delivery schedule ends. It must be a valid ISO-8601 date and time with an offset (YYYY-MM-DDThh:mm:ssTZD)."
  },
  "modifiedAt" : "The date and time for when the last change was made to this request. Read-only.",
  "id" : "Id of the update request.",
  "sentBy" : {
    "lastLogin" : "Last login time of the current user",
    "lastName" : "User's last name",
    "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
    "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
    "profileImage" : {
      "altText" : "Alternate text for the image",
      "width" : "Original width (in pixels) of the uploaded image",
      "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
      "id" : "Image Id",
      "height" : "Original height (in pixels) of the uploaded image"
    },
    "firstName" : "User's first name",
    "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
    "name" : "User's full name (read-only)",
    "id" : "User Id",
    "sheetCount" : "The number of sheets owned by the current user within the organization account",
    "email" : "User's primary email address",
    "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
    "status" : "User status"
  }
}
```

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## create_webhook

Creates a new webhook.

<details><summary>Parameters</summary>

### $body

Webhook object, limited to the following attributes:
callbackUrl (required)
events (required)
name (required)
scope (required)
scopeObjectId (required)
version (required)

**Type:** object

```json
{
  "apiClientName" : "API client name corresponding to third-party app that created the webhook. Read-only. Only present if webhook was created by third-party app.",
  "disabledDetails" : "Details about the reason the webhook was disabled. Read-only. Only present when enabled=false.",
  "modifiedAt" : "Time of last modification. Read-only.",
  "version" : "Webhook version. Currently, the only supported value is 1. This attribute is intended to ensure backward compatibility as new webhook functionality is released. For example, a webhook with a version of 1 is guaranteed to always be sent callback objects that are compatible with the version 1 release of webhooks.",
  "enabled" : "Indicates whether the webhook is on (true) or off (false)",
  "createdAt" : "Time of creation. Read-only.",
  "stats" : {
    "lastCallbackAttemptRetryCount" : "The number of retries the webhook had performed as of the last callback attempt.",
    "lastSuccessfulCallback" : "When this webhook last made a successful callback.",
    "lastCallbackAttempt" : "When this webhook last made a callback attempt."
  },
  "scopeObjectId" : "Id of the object that is subscribed to. Specified when a webhook is created and cannot be changed.",
  "scope" : "Scope of the subscription. Currently, the only supported value is sheet. Specified when a webhook is created and cannot be changed.",
  "name" : "Webhook name",
  "apiClientId" : "API client Id corresponding to third-party app that created the webhook. Read-only. Only present if webhook was created by third-party app.",
  "callbackUrl" : "HTTPS URL where callbacks are sent. NOTES: Smartsheet webhooks do not support callbacks to servers using self-signed certificates. The callback server must be using a signed certificate from a certificate authority. The callbackURL must use one of the following ports: 443 (default for HTTPS), 8000, 8008, 8080, or 8443.",
  "id" : "Webhook Id",
  "sharedSecret" : "Shared secret for this webhook, randomly generated by Smartsheet. Read-only. See Authenticating Callbacks for details about how this value can be used.",
  "events" : [ "string" ],
  "status" : "Webhook status. Read-only. See Webhook Status for list of possible values."
}
```

</details>

## create_workspace

Creates a workspace.

<details><summary>Parameters</summary>

### $body

Workspace object, limited to the following attribute:
name (string) - required

**Type:** object

```json
{
  "reports" : [ { } ],
  "sheets" : [ { } ],
  "folders" : [ { } ],
  "sights" : [ { } ],
  "accessLevel" : "User's permissions on the workspace",
  "templates" : [ { } ],
  "name" : "Workspace name",
  "id" : "Workspace Id",
  "permalink" : "URL that represents a direct link to the workspace in Smartsheet",
  "favorite" : "Returned only if the user has marked the workspace as a favorite in their \"Home\" tab (value = true)"
}
```

</details>

## delete_all_versions

Deletes all versions of the attachment corresponding to the specified attachmentId. For attachments with multiple versions, this effectively deletes the attachment from the object that it’s attached to.

<details><summary>Parameters</summary>

### attachmentId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## delete_alternate_email

Deletes the specified alternate email address for the specified user.

<details><summary>Parameters</summary>

### alternateEmailId (required)

**Type:** string

### userId (required)

**Type:** string

</details>

## delete_an_automation_rule

Deletes an automation rule.

<details><summary>Parameters</summary>

### automationRuleId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## delete_attachment

Deletes the attachment specified in the URL.

<details><summary>Parameters</summary>

### attachmentId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## delete_column

Deletes the column specified in the URL.

<details><summary>Parameters</summary>

### columnId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## delete_comment

Deletes the comment specified in the URL.

<details><summary>Parameters</summary>

### commentId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## delete_discussion

Deletes the discussion specified in the URL.

<details><summary>Parameters</summary>

### discussionId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## delete_folder

Deletes the folder (and its contents) specified in the URL.

<details><summary>Parameters</summary>

### folderId (required)

**Type:** string

</details>

## delete_group

Deletes the group specified in the URL.

<details><summary>Parameters</summary>

### groupId (required)

**Type:** string

</details>

## delete_report_share

Deletes the share specified in the URL.

<details><summary>Parameters</summary>

### reportId (required)

**Type:** string

### shareId (required)

**Type:** string

</details>

## delete_rows

Deletes one or more rows from the sheet specified in the URL.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### ids

**Type:** array

```json
[ "string" ]
```

</details>

## delete_sent_update_request

Deletes the specified sent update request.

<details><summary>Parameters</summary>

### sentUpdateRequestId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## delete_sheet

Deletes the sheet specified in the URL.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

</details>

## delete_sheet_share

Deletes the share specified in the URL.

<details><summary>Parameters</summary>

### shareId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## delete_sight

Deletes the Sight specified in the URL.

<details><summary>Parameters</summary>

### sightId (required)

**Type:** string

</details>

## delete_sight_share

Deletes the share specified in the URL.

<details><summary>Parameters</summary>

### shareId (required)

**Type:** string

### sightId (required)

**Type:** string

</details>

## delete_update_request

Terminates the future scheduled delivery of the update request specified in the URL.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### updateRequestId (required)

**Type:** string

</details>

## delete_webhook

Deletes the webhook specified in the URL.

<details><summary>Parameters</summary>

### webhookId (required)

**Type:** string

</details>

## delete_workspace

Deletes the specified workspace (and its contents).

<details><summary>Parameters</summary>

### workspaceid (required)

**Type:** string

</details>

## delete_workspace_share

Deletes the share specified in the URL.

<details><summary>Parameters</summary>

### shareId (required)

**Type:** string

### workspaceId (required)

**Type:** string

</details>

## edit_comment

Updates the text of a comment. NOTE: Only the user that created the comment is permitted to update it. Updating a Comment

<details><summary>Parameters</summary>

### commentId (required)

**Type:** string

### sheetId (required)

**Type:** string

### $body

Comment object with the following attribute:
text

**Type:** object

```json
{
  "createdAt" : "Time of creation",
  "attachments" : [ {
    "createdAt" : "A timestamp of when the attachment was originally added",
    "attachmentSubType" : "Attachment sub type",
    "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
    "createdBy" : { },
    "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
    "name" : "Attachment name",
    "id" : "Attachment Id",
    "mimeType" : "Attachment MIME type (PNG, etc.)",
    "sizeInKb" : "The size of the file, if the attachmentType is FILE",
    "parentId" : "The Id of the parent",
    "parentType" : "The type of object the attachment belongs to",
    "url" : "Attachment temporary URL (files only)"
  } ],
  "createdBy" : { },
  "discussionId" : "Discussion Id",
  "modifiedAt" : "Time of last modification",
  "id" : "Comment Id",
  "text" : "Comment body"
}
```

</details>

## get_all_sent_update_requests

Gets a summarized list of all sent update requests on the sheet.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## get_all_update_requests

Gets a summarized list of all update requests that have future schedules associated with the specified sheet.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## get_alternate_email

Gets the specified alternate email.

<details><summary>Parameters</summary>

### alternateEmailId (required)

**Type:** string

### userId (required)

**Type:** string

</details>

## get_an_automation_rule

Returns the specified automation rule, including any action values.

<details><summary>Parameters</summary>

### automationRuleId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## get_attachment

Fetches a temporary URL that allows you to download an attachment. The urlExpiresInMillis attribute tells you how long the URL is valid.

<details><summary>Parameters</summary>

### attachmentId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## get_cell_history

Gets the cell modification history.

<details><summary>Parameters</summary>

### columnId (required)

**Type:** string

### rowId (required)

**Type:** string

### sheetId (required)

**Type:** string

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: columnType | objectValue" ]
```

### includeAll

If true, includes all results.

**Type:** boolean

### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

</details>

## get_column

Gets the column specified in the URL.

<details><summary>Parameters</summary>

### columnId (required)

**Type:** string

### sheetId (required)

**Type:** string

### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

</details>

## get_comment

Gets the comment specified in the URL.

<details><summary>Parameters</summary>

### commentId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## get_contact

Gets the specified contact.

<details><summary>Parameters</summary>

### contactId (required)

**Type:** string

</details>

## get_cross_sheet_reference

Gets the cross-sheet reference specified in the URL.

<details><summary>Parameters</summary>

### crossSheetReferenceId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## get_current_user

Gets the current user.

<details><summary>Parameters</summary>

### include

comma-separated list of row elements to move in addition to the cell data

**Type:** array

```json
[ "string. Possible values: groups" ]
```

</details>

## get_discussion

Gets the discussion specified in the URL.

<details><summary>Parameters</summary>

### discussionId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## get_events

Gets events that are occurring in your Smartsheet organization account. Examples of events are creation, update, load, and delete of sheets, reports, dashboards, attachments, users, etc. Each event type has a distinct combination of objectType and action. Many event types have additional information returned under an additionalDetails object. See the Event Reporting reference documentation for a complete list of all currently supported events, including their respective objectType, action, and additionalDetails properties.

<details><summary>Parameters</summary>

### Accept-Encoding

Strongly recommended to make sure payload is compressed.

**Type:** string

**Potential values:** deflate, gzip

### maxCount

Maximum number of events to return as response to this call.

**Type:** number

### numericDates

If true, dates are accepted and returned in Unix epoch time (milliseconds since midnight on January 1, 1970 in UTC time). Default is false, which means ISO-8601 format.

**Type:** boolean

### since

Starting time for events to return. Intended for use only at client startup or recovery. This is intended for backfilling data and not for fine-grained date-based queries. Therefore, resolution is limited to the nearest hour. Interpreted as ISO-8601 format, unless numericDates is specified. You must pass in a value for either since or streamPosition and never both.

**Type:** string

### streamPosition

Indicates next set of events to return. Use value of nextStreamPosition returned from the previous call. You must pass in a value for either since or streamPosition and never both.

**Type:** string

</details>

## get_folder

Gets the specified folder (and lists its contents).

<details><summary>Parameters</summary>

### folderId (required)

**Type:** string

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: ownerInfo | sheetVersion | source" ]
```

</details>

## get_group

Gets information about and an array of members for the group specified in the URL.

<details><summary>Parameters</summary>

### groupId (required)

**Type:** string

</details>

## get_report

Gets the report, based on the report Id.

<details><summary>Parameters</summary>

### reportId (required)

**Type:** string

### Accept

If specified, gets the sheet in the format specified, based on the sheet Id.

**Type:** string

**Potential values:** application/vnd.ms-excel, text/csv

### exclude

a comma-separated list of elements to not include in the response.

**Type:** array

```json
[ "string. Possible values: linkInFromCellDetails | linksOutToCellsDetails" ]
```

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: attachments | discussions | format | objectValue | source | sourceSheets" ]
```

### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

### page

Specifies which page to return, for example, page=4.

**Type:** number

### pageSize

Specifies the maximum number of items to return per page, for example, pageSize=25.

**Type:** number

</details>

## get_report_publish_status

Gets the Report's 'Publish' settings.

<details><summary>Parameters</summary>

### reportId (required)

**Type:** string

</details>

## get_report_share

Gets the share specified in the URL.

<details><summary>Parameters</summary>

### reportId (required)

**Type:** string

### shareId (required)

**Type:** string

</details>

## get_row

Gets the row specified in the URL.

<details><summary>Parameters</summary>

### rowId (required)

**Type:** string

### sheetId (required)

**Type:** string

### exclude

a comma-separated list of elements to not include in the response.

**Type:** array

```json
[ "string. Possible values: linkInFromCellDetails | linksOutToCellsDetails | nonexistentCells" ]
```

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: attachments | columnType | discussions | filters | format | objectValue | rowPermalink | rowWriterInfo | columns" ]
```

</details>

## get_sent_update_request

Gets the specified sent update request on the sheet.

<details><summary>Parameters</summary>

### sentUpdateRequestId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## get_server_info



*This operation has no parameters*

## get_sheet

Gets the sheet specified in the URL. Returns the sheet, including rows, and optionally populated with discussion and attachment objects.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### Accept

If specified, gets the sheet in the format specified, based on the sheet Id.

**Type:** string

**Potential values:** application/pdf, application/vnd.ms-excel, text/csv

### columnIds

a comma-separated list of column Ids. The response contains only the specified columns in the "columns" array, and individual rows' "cells" array only contains cells in the specified columns.

**Type:** array

```json
[ "string" ]
```

### exclude

a comma-separated list of elements to not include in the response.

**Type:** array

```json
[ "string. Possible values: filteredOutRows | linkInFromCellDetails | linksOutToCellsDetails | nonexistentCells" ]
```

### filterId

overrides the existing include={filters} parameter if both are supplied. Applies the given filter (if accessible by the calling user) and marks the affected rows as "filteredOut"= true.

**Type:** string

### ifVersionAfter

If version specified is still the current sheet version, then returns an abbreviated Sheet object with only the sheet version property. Otherwise, if the sheet has been modified, returns the complete Sheet object. Intended to allow clients with a cached copy to make sure they have the latest version.

**Type:** boolean

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: columnType | rowPermalink | rowWriterInfo | attachments | crossSheetReferences | discussions | filters | filterDefinitions | format | ganttConfig | objectValue | ownerInfo | source" ]
```

### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

### page

Specifies which page to return, for example, page=4.

**Type:** number

### pageSize

Specifies the maximum number of items to return per page, for example, pageSize=25.

**Type:** number

### paperSize

applies to PDF only

**Type:** string

**Potential values:** LETTER, LEGAL, WIDE, ARCHD, A4, A3, A2, A1, A0

### rowIds

a comma-separated list of row Ids on which to filter the rows included in the result

**Type:** array

```json
[ "string" ]
```

### rowNumbers

a comma-separated list of row numbers on which to filter the rows included in the result. Non-existent row numbers are ignored.

**Type:** array

```json
[ "number" ]
```

</details>

## get_sheet_publish_status

Gets the sheet's 'Publish' settings.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

</details>

## get_sheet_share

Gets the share specified in the URL.

<details><summary>Parameters</summary>

### shareId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## get_sheet_version

Gets the sheet version without loading the entire sheet. The following actions increment sheet version:

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

</details>

## get_sight

Gets the specified Sight.

<details><summary>Parameters</summary>

### sightId (required)

**Type:** string

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: source" ]
```

### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

### objectValue

when used in combination with a level query parameter, includes the email addresses for multi-contact data.

**Type:** boolean

</details>

## get_sight_publish_status

Gets the Sight 'publish' settings.

<details><summary>Parameters</summary>

### sightId (required)

**Type:** string

</details>

## get_sight_share

Gets the share specified in the URL.

<details><summary>Parameters</summary>

### shareId (required)

**Type:** string

### sightId (required)

**Type:** string

</details>

## get_update_request

Gets the specified update request for the sheet that has a future schedule.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### updateRequestId (required)

**Type:** string

</details>

## get_user

Gets the user specified in the URL.

<details><summary>Parameters</summary>

### userId (required)

**Type:** string

</details>

## get_webhook

Gets the webhook specified in the URL.

<details><summary>Parameters</summary>

### webhookId (required)

**Type:** string

</details>

## get_workspace

Gets the specified workspace (and lists its contents).

<details><summary>Parameters</summary>

### workspaceid (required)

**Type:** string

### include

when specified with a value of workspaceShares, response contains both item-level shares (scope=ITEM) and workspace-level shares (scope=WORKSPACE).

**Type:** array

```json
[ "string. Possible values: ownerInfo | source" ]
```

### loadAll

true or false, defaults to false

**Type:** boolean

</details>

## get_workspace_share

Gets the share specified in the URL.

<details><summary>Parameters</summary>

### shareId (required)

**Type:** string

### workspaceId (required)

**Type:** string

</details>

## import_sheet_from_csv_xlsx

Imports CSV or XLSX data into a new sheet in the top-level "sheets" folder.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

### headerRowIndex

a zero-based integer indicating the row number to use for column names. Rows before this are omitted. If not specified, the default values are Column1, Column2, etc.

**Type:** integer

### primaryColumnIndex

a zero-based integer indicating the column to designate as primary. If not specified, the default value is 0.

**Type:** integer

### sheetName

desired name of the sheet.

**Type:** string

</details>

## import_sheet_into_folder

Imports CSV or XLSX data into a new sheet in the specified folder.

<details><summary>Parameters</summary>

### folderId (required)

**Type:** string

### $body

**Type:** object

```json
{ }
```

### headerRowIndex

a zero-based integer indicating the row number to use for column names. Rows before this are omitted. If not specified, the default values are Column1, Column2, etc.

**Type:** integer

### primaryColumnIndex

a zero-based integer indicating the column to designate as primary. If not specified, the default value is 0.

**Type:** integer

### sheetName

desired name of the sheet.

**Type:** string

</details>

## import_sheet_into_workspace

Imports CSV or XLSX data into a new sheet in the specified workspace.

<details><summary>Parameters</summary>

### workspaceId (required)

**Type:** string

### $body

**Type:** object

```json
{ }
```

### headerRowIndex

a zero-based integer indicating the row number to use for column names. Rows before this are omitted. If not specified, the default values are Column1, Column2, etc.

**Type:** integer

### primaryColumnIndex

a zero-based integer indicating the column to designate as primary. If not specified, the default value is 0.

**Type:** integer

### sheetName

desired name of the sheet.

**Type:** string

</details>

## list_all_automation_rules

Returns all automation rules associated with the specified sheet.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_alternate_emails

Gets a list of the alternate emails for the specified user.

<details><summary>Parameters</summary>

### userId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_attachments

Gets a list of all attachments that are on the sheet, including sheet, row, and discussion-level attachments.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_columns

Gets a list of all columns belonging to the sheet specified in the URL.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_contacts

Gets a list of the user's Smartsheet contacts.

<details><summary>Parameters</summary>

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_contents

Gets a nested list of all Home objects, including folders, reports, sheets, Sights, templates, and workspaces, as shown on the "Home" tab.

<details><summary>Parameters</summary>

### exclude

a comma-separated list of optional elements to not include in the response

**Type:** array

```json
[ "string. Possible values: permalinks" ]
```

### include

a comma-separated list of optional elements to include in the response

**Type:** array

```json
[ "string. Possible values: source" ]
```

</details>

## list_cross_sheet_references

Lists all cross-sheet references for the sheet.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_discussion_attachments

Gets a list of all attachments that are in the discussion.

<details><summary>Parameters</summary>

### discussionId (required)

**Type:** string

### sheetId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_discussions

Gets a list of all discussions associated with the specified sheet. Remember that discussions are containers for the conversation thread. To see the entire thread, use the include=comments parameter.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: attachments | comments" ]
```

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_favorites

Gets a list of all of the user's favorite items.

<details><summary>Parameters</summary>

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_folders_sheet_level

Gets a list of the top-level child folders within the user's Sheets folder (Home).

<details><summary>Parameters</summary>

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_folders_subfolder

Gets a list of the top-level child folders within the specified folder.

<details><summary>Parameters</summary>

### folderId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_folders_workspace

Gets a list of the top-level child folders within the specified workspace.

<details><summary>Parameters</summary>

### workspaceId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_image_urls

Gets a list of URLs that can be used to retrieve the specified cell images. To retrieve images, see the workflow in Download Cell Image.

<details><summary>Parameters</summary>

### $body

Array of ImageUrl objects, with the following attributes:
imageId (required)
height (optional)
width (optional)Each image in the response is sized according to which dimensions were specified by the request:
If neither height nor width is specified, the image is returned in its original size.
If both height and width are specified, image is sized using those measurements.
If either height or width is specified (that is, one or the other -- not both), the image is automatically scaled using that measurement.Additionally, the following rules apply:
If the requested image size is less than or equal to the actual image size, the returned image size matches the requested size.
If the requested image size is larger than the actual image size, the returned image size matches the actual image size.

**Type:** object

```json
{
  "imageId" : "Image Id",
  "width" : "Image width (in pixels). In the Get All Image URLs request, this (optional) attribute represents requested width; in the response, it represents actual width of the image returned. (See List Image URLs.)",
  "error" : {
    "errorCode" : "Custom error code from Smartsheet. See the Complete Error Code List.",
    "refId" : "Id of the specific error occurrence. Please include this information when contacting Smartsheet support.",
    "message" : "Descriptive message."
  },
  "url" : "Temporary URL that can be used to retrieve the image. This attribute can be present in a response but is never specified in a request.",
  "height" : "Image height (in pixels). In the Get All Image URLs request, this (optional) attribute represents requested height; in the response, it represents actual height of the image returned. (See List Image URLs.)"
}
```

</details>

## list_org_groups

Gets a list of all groups in an organization account. To fetch the members of an individual group, use the Get Group operation.

<details><summary>Parameters</summary>

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_org_sheets

Gets a summarized list of all sheets owned by the members of the organization account.

<details><summary>Parameters</summary>

### includeAll

If true, includes all results.

**Type:** boolean

### modifiedSince

when specified with a date and time value, response only includes the objects that are modified on or after the date and time specified.

**Type:** string

</details>

## list_public_templates

Gets a list of public templates that the user has access to.

<details><summary>Parameters</summary>

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_report_shares

Gets a list of all users and groups to whom the specified report is shared, and their access level.

<details><summary>Parameters</summary>

### reportId (required)

**Type:** string

### include

when specified with a value of workspaceShares, response contains both item-level shares (scope=ITEM) and workspace-level shares (scope=WORKSPACE).

**Type:** array

```json
[ "string. Possible values: workspaceShares" ]
```

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_reports

Gets a list of all reports that the user has access to in alphabetical order by name. The list contains an abbreviated Report object for each report.

<details><summary>Parameters</summary>

### includeAll

If true, includes all results.

**Type:** boolean

### modifiedSince

when specified with a date and time value, response only includes the objects that are modified on or after the date and time specified.

**Type:** string

</details>

## list_row_attachments

Gets a list of all attachments that are on the row, including row and discussion-level attachments.

<details><summary>Parameters</summary>

### rowId (required)

**Type:** string

### sheetId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_row_discussions

Gets a list of all discussions associated with the specified row. Remember that discussions are containers for the conversation thread. To see the entire thread, use the include=comments parameter.

<details><summary>Parameters</summary>

### rowId (required)

**Type:** string

### sheetId (required)

**Type:** string

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: attachments | comments" ]
```

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_sheet_shares

Gets a list of all users and groups to whom the specified sheet is shared, and their access level.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### include

when specified with a value of workspaceShares, response contains both item-level shares (scope=ITEM) and workspace-level shares (scope=WORKSPACE).

**Type:** array

```json
[ "string. Possible values: workspaceShares" ]
```

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_sheets

Gets a list of all sheets that the user has access to in alphabetical order by name. The list contains an abbreviated Sheet object for each sheet.

<details><summary>Parameters</summary>

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: sheetVersion | source" ]
```

### includeAll

If true, includes all results.

**Type:** boolean

### modifiedSince

when specified with a date and time value, response only includes the objects that are modified on or after the date and time specified.

**Type:** string

</details>

## list_sight_shares

Gets a list of all users and groups to whom the specified Sight is shared, and their access level.

<details><summary>Parameters</summary>

### sightId (required)

**Type:** string

### include

when specified with a value of workspaceShares, response contains both item-level shares (scope=ITEM) and workspace-level shares (scope=WORKSPACE).

**Type:** array

```json
[ "string. Possible values: workspaceShares" ]
```

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_sights

Gets a list of all Sights that the user has access to.

<details><summary>Parameters</summary>

### includeAll

If true, includes all results.

**Type:** boolean

### modifiedSince

when specified with a date and time value, response only includes the objects that are modified on or after the date and time specified.

**Type:** string

</details>

## list_user_created_templates

Gets a list of user-created templates that the user has access to.

<details><summary>Parameters</summary>

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_users

Gets a list of users in the organization account. To filter by email, use the optional email query string parameter to specify a list of users' email addresses.

<details><summary>Parameters</summary>

### email

Comma-separated list of email addresses on which to filter the results.

**Type:** array

```json
[ "string" ]
```

### include

when specified with a value of favoriteFlag, response indicates which returned items are favorites

**Type:** array

```json
[ "string. Possible values: lastLogin" ]
```

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_versions

Gets a list of all versions of the given attachmentId in order from newest to oldest.

<details><summary>Parameters</summary>

### attachmentId (required)

**Type:** string

### sheetId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_webhooks

Gets the list of all webhooks that the user owns (if a user-generated token was used to make the request) 
or the list of all webhooks associated with the third-party app (if a third-party app made the request). 
Items in the response are ordered by API cient name &gt; webhook name &gt; creation date.

<details><summary>Parameters</summary>

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_workspace_shares

Gets a list of all users and groups to whom the specified workspace is shared, and their access level.

<details><summary>Parameters</summary>

### workspaceId (required)

**Type:** string

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_workspaces

Gets a list of workspaces that the user has access to. The list contains an abbreviated Workspace object for each workspace.

<details><summary>Parameters</summary>

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: sheetVersion" ]
```

### includeAll

If true, includes all results.

**Type:** boolean

</details>

## make_alternate_email_primary

Makes the specified alternate email address to become the primary email address for the specified user.

<details><summary>Parameters</summary>

### alternateEmailId (required)

**Type:** string

### userId (required)

**Type:** string

</details>

## move_folder

Moves the specified folder to another location.

<details><summary>Parameters</summary>

### folderId (required)

**Type:** string

### $body

ContainerDestination object, limited to the following required attributes:
destinationId
destinationType

**Type:** object

```json
{
  "newName" : "Name of the newly created object (when creating a copy of a Sheet, Folder, Sight, or Workspace). This attribute is not supported for \"move\" operations (that is, a moved Sheet, Folder, Sight, or Workspace retains its original name).",
  "destinationType" : "Type of the destination container (when copying or moving a Sheet or a Folder).",
  "destinationId" : "Id of the destination container (when copying or moving a Sheet or a Folder). Required if destinationType is \"folder\" or \"workspace\" If destinationType is \"home\", this value must be null."
}
```

</details>

## move_rows_to_another_sheet

Moves rows from the sheet specified in the URL to (the bottom of) another sheet.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

CopyOrMoveRowDirective object

**Type:** object

```json
{
  "rowIds" : [ "number" ],
  "to" : {
    "sheetId" : "Id of the destination sheet"
  }
}
```

### ignoreRowsNotFound

If set to true, specifying row Ids that do not exist within the source sheet does not cause an error response. If omitted or set to false, specifying row Ids that do not exist within the source sheet causes an error response (and no rows are moved).

**Type:** boolean

### include

comma-separated list of row elements to move in addition to the cell data

**Type:** array

```json
[ "string. Possible values: attachments | discussions" ]
```

</details>

## move_sheet

Moves the specified sheet to a new location.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

ContainerDestination object, limited to the following required attributes:
destinationId
destinationType

**Type:** object

```json
{
  "newName" : "Name of the newly created object (when creating a copy of a Sheet, Folder, Sight, or Workspace). This attribute is not supported for \"move\" operations (that is, a moved Sheet, Folder, Sight, or Workspace retains its original name).",
  "destinationType" : "Type of the destination container (when copying or moving a Sheet or a Folder).",
  "destinationId" : "Id of the destination container (when copying or moving a Sheet or a Folder). Required if destinationType is \"folder\" or \"workspace\" If destinationType is \"home\", this value must be null."
}
```

</details>

## move_sight

Moves the specified Sight to a new location.

<details><summary>Parameters</summary>

### sightId (required)

**Type:** string

### $body

ContainerDestination object, limited to the following required attributes:
destinationId
destinationType

**Type:** object

```json
{
  "newName" : "Name of the newly created object (when creating a copy of a Sheet, Folder, Sight, or Workspace). This attribute is not supported for \"move\" operations (that is, a moved Sheet, Folder, Sight, or Workspace retains its original name).",
  "destinationType" : "Type of the destination container (when copying or moving a Sheet or a Folder).",
  "destinationId" : "Id of the destination container (when copying or moving a Sheet or a Folder). Required if destinationType is \"folder\" or \"workspace\" If destinationType is \"home\", this value must be null."
}
```

</details>

## refresh_access_token

Refreshes an access token, as part of the OAuth process. For more information, see OAuth Flow.

<details><summary>Parameters</summary>

### client_id

client id for your app

**Type:** string

### grant_type

must be set to "refresh_token"

**Type:** string

### hash

SHA-256 hash of your app secret concatenated with a pipe and the refresh token value

**Type:** string

### refresh_token

refresh_token value that came with the access token

**Type:** string

</details>

## remove_favorite_folder

Removes a single folder from the user's list of favorite items.

<details><summary>Parameters</summary>

### folderId (required)

**Type:** string

### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

```json
[ "string" ]
```

</details>

## remove_favorite_report

Removes a single report from the user's list of favorite items.

<details><summary>Parameters</summary>

### reportId (required)

**Type:** string

</details>

## remove_favorite_sheet

Removes a single sheet from the user's list of favorite items.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

</details>

## remove_favorite_sight

Removes a single Sight from the user's list of favorite items.

<details><summary>Parameters</summary>

### sightId (required)

**Type:** string

</details>

## remove_favorite_template

Removes a single template from the user's list of favorite items.

<details><summary>Parameters</summary>

### templateId (required)

**Type:** string

</details>

## remove_favorite_workspace

Removes a single workspace from the user's list of favorite items.

<details><summary>Parameters</summary>

### workspaceId (required)

**Type:** string

</details>

## remove_group_member

Removes a member from a group.

<details><summary>Parameters</summary>

### groupId (required)

**Type:** string

### userId (required)

**Type:** string

</details>

## remove_multiple_favorite_folders



*This operation has no parameters*

## remove_multiple_favorite_reports

Removes multiple reports from the user's list of favorite items.

<details><summary>Parameters</summary>

### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

```json
[ "string" ]
```

</details>

## remove_multiple_favorite_sheets

Removes multiple sheets from the user's list of favorite items.

<details><summary>Parameters</summary>

### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

```json
[ "string" ]
```

</details>

## remove_multiple_favorite_sights

Removes multiple Sights from the user's list of favorite items.

<details><summary>Parameters</summary>

### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

```json
[ "string" ]
```

</details>

## remove_multiple_favorite_templates

Removes multiple templates from the user's list of favorite items.

<details><summary>Parameters</summary>

### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

```json
[ "string" ]
```

</details>

## remove_multiple_favorite_workspaces

Removes multiple workspaces from the user's list of favorite items.

<details><summary>Parameters</summary>

### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

```json
[ "string" ]
```

</details>

## remove_user

Removes a user from an organization account. User is transitioned to a free collaborator with read-only access to owned reports, sheets, Sights, workspaces, and any shared templates (unless those are optionally transferred to another user).

<details><summary>Parameters</summary>

### userId (required)

**Type:** string

### removeFromSharing

Set to true to remove the user from sharing for all sheets/workspaces in the organization account. If not specified, user is not removed from sharing.

**Type:** boolean

### transferSheets

If true, and transferTo is specified, the removed user's sheets are transferred. Else, sheets are not transferred. Defaults to false.

**Type:** boolean

### transferTo

The Id of the user to transfer ownership to. If the user being removed owns groups, they are transferred to this user. If the user owns sheets, and transferSheets is true, the removed user's sheets are transferred to this user.

**Type:** string

</details>

## reset_shared_secret

Resets the shared secret for the specified webhook. For more information about how a shared secret is used, see Authenticating Callbacks. This operation can be used to rotate an API client's webhooks' shared secrets at periodic intervals to provide additional security.

<details><summary>Parameters</summary>

### webhookId (required)

**Type:** string

</details>

## revoke_access_token

Revokes the access token used to make this request. The access token is no longer valid, and subsequent API calls made using the token fail.

<details><summary>Parameters</summary>

### deleteAllForApiClient

The client Id and user Id is fetched based on the token that is used to make this API call. A value of true deletes all tokens associated to the given client Id and user Id. Defaults to false.

**Type:** boolean

</details>

## search_everything

Searches all sheets that the user can access, for the specified text.

<details><summary>Parameters</summary>

### include

when specified with a value of favoriteFlag, response indicates which returned items are favorites

**Type:** array

```json
[ "string. Possible values: attachments | discussions | format | objectValue | source | sourceSheets" ]
```

### location

when specified with a value of personalWorkspace, limits the response to only those items in the user's workspaces.

**Type:** string

### modifiedSince

when specified with a date and time value, response only includes the objects that are modified on or after the date and time specified.

**Type:** string

### query

text with which to perform the search. Enclose in double-quotes for an exact search.

**Type:** string

### scopes

If search fails, try using an array for each type of this comma-separated list of search filters

**Type:** array

```json
[ "string. Possible values: attachments | cellData | comments | folderNames | profileFields | reportNames | sheetNames | sightNames | templateNames | workspaceNames" ]
```

</details>

## search_sheet

Searches a sheet for the specified text.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### query

text with which to perform the search. Enclose in double-quotes for an exact search.

**Type:** string

</details>

## send_report

Sends the report as a PDF attachment via email to the designated recipients.

<details><summary>Parameters</summary>

### reportId (required)

**Type:** string

### $body

SheetEmail object

**Type:** object

```json
{
  "formatDetails" : {
    "paperSize" : "string. Possible values: LETTER | LEGAL | WIDE | ARCHD | A4 | A3 | A2 | A1 | A0"
  },
  "format" : "string. Possible values: EXCEL | PDF | PDF_GANTT"
}
```

</details>

## send_rows

Sends one or more rows via email.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

MultiRowEmail object. 

The columns included for each row in the email are populated according to the following rules:
If the columnIds attribute of the MultiRowEmail object is specified as an array of column Ids, those specific columns are included.
If the columnIds attribute of the MultiRowEmail object is omitted, all columns except hidden columns shall be included.
If the columnIds attribute of the MultiRowEmail object is specified as empty, no columns shall be included. (NOTE: In this case, either includeAttachments=true or includeDiscussions=true must be specified.)

**Type:** object

```json
{
  "rowIds" : [ "number" ]
}
```

</details>

## send_sheet_via_email

Sends the sheet as a PDF attachment via email to the designated recipients.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

SheetEmail object

**Type:** object

```json
{
  "formatDetails" : {
    "paperSize" : "string. Possible values: LETTER | LEGAL | WIDE | ARCHD | A4 | A3 | A2 | A1 | A0"
  },
  "format" : "string. Possible values: EXCEL | PDF | PDF_GANTT"
}
```

</details>

## set_report_publish_status

Sets the publish status of the report and returns the new status, including the URL of any enabled publishing.

<details><summary>Parameters</summary>

### reportId (required)

**Type:** string

### $body

ReportPublish object

**Type:** object

```json
{
  "readOnlyFullUrl" : "URL for 'Read-Only Full' view of the published report. Only returned in a response if readOnlyFullEnabled = true.",
  "readOnlyFullEnabled" : "(Required) If true, a rich version of the report is published with the ability to download row attachments and discussions.",
  "readOnlyFullAccessibleBy" : "Indicates who can access the 'Read-Only Full' view of the published sheet: ALL -- available to anyone who has the link. ORG -- available only to members of the sheet owner's Smartsheet organization account. Only returned in a response if readOnlyFullEnabled = true.",
  "readOnlyFullShowToolbar" : "DEPRECATED Indicates whether the left nav toolbar is displayed. The default, or true, is to display the toolbar. If false, hides the toolbar.",
  "readOnlyFullDefaultView" : "Indicates which view the user has set for a read-only, default view of the published report."
}
```

</details>

## set_sheet_publish_status

Sets the publish status of the sheet and returns the new status, including the URLs of any enabled publishings.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

SheetPublish object

**Type:** object

```json
{
  "readWriteDefaultView" : "Indicates which view the user has set for a read-only, default view of the published sheet.",
  "readOnlyFullAccessibleBy" : "Indicates who can access the 'Read-Only Full' view of the published sheet: ALL -- available to anyone who has the link. ORG -- available only to members of the sheet owner's Smartsheet organization account. Only returned in a response if readOnlyFullEnabled = true.",
  "readWriteEnabled" : "If true, a rich version of the sheet is published with the ability to edit cells and manage attachments and discussions.",
  "icalUrl" : "URL for iCal view of the published sheetOnly returned in a response if icalEnabled = true.",
  "readOnlyFullDefaultView" : "Indicates which view the user has set for a read-only, default view of the published sheet.",
  "readWriteShowToolbar" : "DEPRECATED Indicates whether the left nav toolbar is displayed. The default, or true, is to display the toolbar. If false, hides the toolbar.",
  "readOnlyFullUrl" : "URL for 'Read-Only Full' view of the published sheet. Only returned in a response if readOnlyFullEnabled = true.",
  "icalEnabled" : "If true, a webcal is available for the calendar in the sheet.",
  "readOnlyFullEnabled" : "If true, a rich version of the sheet is published with the ability to download row attachments and discussions.",
  "readWriteUrl" : "URL for 'Edit by Anyone' view of the published sheetOnly returned in a response if readWriteEnabled = true.",
  "readOnlyLiteSslUrl" : "URL for 'Read-Only' view of the published sheet when SSL is enabled.",
  "readOnlyLiteUrl" : "URL for 'Read-Only HTML' view of the published sheet. Only returned in a response if readOnlyLiteEnabled = true.",
  "readOnlyLiteEnabled" : "If true, a lightweight version of the sheet is published without row attachments and discussions.",
  "readOnlyFullShowToolbar" : "DEPRECATED Indicates whether the left nav toolbar is displayed. The default, or true, is to display the toolbar. If false, hides the toolbar.",
  "readWriteAccessibleBy" : "Indicates who can access the 'Edit by Anyone' view of the published sheet: ALL -- available to anyone who has the link. ORG -- available only to members of the sheet owner's Smartsheet organization account.Only returned in a response if readWriteEnabled = true."
}
```

</details>

## set_sight_publish_status

Publishes or unpublishes a Sight.

<details><summary>Parameters</summary>

### sightId (required)

**Type:** string

### $body

SightPublish object limited to the following attributes:
readOnlyFullEnabled (required)
readOnlyFullAccessibleBy (optional) - set to either ALL or ORG, when readOnlyFullEnabled=true.To publish the Sight, set readOnlyFullEnabled to true. To unpublish the Sight, set readOnlyFullEnabled to false.

**Type:** object

```json
{
  "readOnlyFullUrl" : "URL for 'Read-Only Full' view of the published Sight.Only returned in a response if readOnlyFullEnabled = true.",
  "readOnlyFullEnabled" : "If true, a rich version of the Sight is published with the ability to use shortcuts and widget interactions.",
  "readOnlyFullAccessibleBy" : "Indicates who can access the 'Read-Only Full' view of the published sheet: ALL -- available to anyone who has the link. ORG -- available only to members of the sheet owner's Smartsheet organization account. Only returned in a response if readOnlyFullEnabled = true."
}
```

</details>

## share_report_2

Shares a report with the specified users and groups. If called with a single Share object, and that user or group share already exists, error code 1025 is returned. If called with an array of Share objects, and one or more user or group shares in the array already exist, they are ignored and omitted from the response.

<details><summary>Parameters</summary>

### reportId (required)

**Type:** string

### $body

Share object or an array of Share objects, with the following attributes:
accessLevel (required)
ccMe (optional): Boolean flag to indicate whether or not to CC the user sharing the sheet.
email (optional): the individual share recipient's email address
groupId (optional): the group share recipient's group Id
message (optional): The message in the body of the email that is optionally sent to the recipient.
subject (optional): The subject of the email that is optionally sent to notify the recipient.NOTE: One of email or groupId must be specified, but not both.

**Type:** object

```json
{
  "accessLevel" : "User or group's access level on shared object.",
  "modifiedAt" : "Time that the share was modified.",
  "subject" : "The subject of the email that is optionally sent to notify the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "groupId" : "Group Id if the share is a group share, else null.",
  "type" : "The type of this share.",
  "message" : "The message included in the body of the email that is optionally sent to the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "userId" : "User Id if the share is a user share, else null.",
  "createdAt" : "Time that the share was created.",
  "ccMe" : "Indicates whether to send a copy of the email to the sharer of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "scope" : "The scope of this share. One of the following values: ITEM: an item-level share (that is, the specific object to which the share applies is shared with the user or group) WORKSPACE: a workspace-level share (that is, the workspace that contains the object to which the share applies is shared with the user or group)",
  "name" : "If a user share and user is also a contact, the user's full name. If a group share, the group's name.",
  "id" : "Share Id. NOTE: unlike other Smartsheet object Ids, this Id is an alphanumeric string.",
  "email" : "User's primary email address for user shares; null for group shares."
}
```

### sendEmail

Indicate whether to notify the user by email.

**Type:** boolean

</details>

## share_sheet

Shares a sheet with the specified users and groups. If called with a single Share object, and that user or group share already exists, error code 1025 is returned. If called with an array of Share objects, and one or more user or group shares in the array already exist, they are ignored and omitted from the response.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

Share object or an array of Share objects, with the following attributes:
accessLevel (required)
ccMe (optional): Boolean flag to indicate whether or not to CC the user sharing the sheet.
email (optional): the individual share recipient's email address
groupId (optional): the group share recipient's group Id
message (optional): The message in the body of the email that is optionally sent to the recipient.
subject (optional): The subject of the email that is optionally sent to notify the recipient.NOTE: One of email or groupId must be specified, but not both.

**Type:** object

```json
{
  "accessLevel" : "User or group's access level on shared object.",
  "modifiedAt" : "Time that the share was modified.",
  "subject" : "The subject of the email that is optionally sent to notify the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "groupId" : "Group Id if the share is a group share, else null.",
  "type" : "The type of this share.",
  "message" : "The message included in the body of the email that is optionally sent to the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "userId" : "User Id if the share is a user share, else null.",
  "createdAt" : "Time that the share was created.",
  "ccMe" : "Indicates whether to send a copy of the email to the sharer of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "scope" : "The scope of this share. One of the following values: ITEM: an item-level share (that is, the specific object to which the share applies is shared with the user or group) WORKSPACE: a workspace-level share (that is, the workspace that contains the object to which the share applies is shared with the user or group)",
  "name" : "If a user share and user is also a contact, the user's full name. If a group share, the group's name.",
  "id" : "Share Id. NOTE: unlike other Smartsheet object Ids, this Id is an alphanumeric string.",
  "email" : "User's primary email address for user shares; null for group shares."
}
```

### sendEmail

Indicate whether to notify the user by email.

**Type:** boolean

</details>

## share_sight

Shares a Sight with the specified users and groups. If called with a single Share object, and that user or group share already exists, error code 1025 is returned. If called with an array of Share objects, and one or more user or group shares in the array already exist, they are ignored and omitted from the response.

<details><summary>Parameters</summary>

### sightId (required)

**Type:** string

### $body

Share object or an array of Share objects, with the following attributes:
accessLevel (required)
ccMe (optional): Boolean flag to indicate whether to CC the user sharing the sheet.
email (optional): the individual share recipient's email address
groupId (optional): the group share recipient's group Id
message (optional): The message in the body of the email that is optionally sent to the recipient.
subject (optional): The subject of the email that is optionally sent to notify the recipient.NOTE: One of email or groupId must be specified, but not both.

**Type:** object

```json
{
  "accessLevel" : "User or group's access level on shared object.",
  "modifiedAt" : "Time that the share was modified.",
  "subject" : "The subject of the email that is optionally sent to notify the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "groupId" : "Group Id if the share is a group share, else null.",
  "type" : "The type of this share.",
  "message" : "The message included in the body of the email that is optionally sent to the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "userId" : "User Id if the share is a user share, else null.",
  "createdAt" : "Time that the share was created.",
  "ccMe" : "Indicates whether to send a copy of the email to the sharer of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "scope" : "The scope of this share. One of the following values: ITEM: an item-level share (that is, the specific object to which the share applies is shared with the user or group) WORKSPACE: a workspace-level share (that is, the workspace that contains the object to which the share applies is shared with the user or group)",
  "name" : "If a user share and user is also a contact, the user's full name. If a group share, the group's name.",
  "id" : "Share Id. NOTE: unlike other Smartsheet object Ids, this Id is an alphanumeric string.",
  "email" : "User's primary email address for user shares; null for group shares."
}
```

### sendEmail

Indicate whether to notify the user by email.

**Type:** boolean

</details>

## share_workspace

Shares a workspace with the specified users and groups. If called with a single Share object, and that user or group share already exists, error code 1025 is returned. If called with an array of Share objects, and one or more user or group shares in the array already exist, they are ignored and omitted from the response.

<details><summary>Parameters</summary>

### workspaceId (required)

**Type:** string

### $body

Share object or an array of Share objects, with the following attributes:
accessLevel (required)
ccMe (optional): Boolean that indicates whether to CC the user sharing the sheet.
email (optional): the individual share recipient's email address
groupId (optional): the group share recipient's group Id
message (optional): The message in the body of the email that is optionally sent to the recipient.
subject (optional): The subject of the email that is optionally sent to notify the recipient.NOTE: One of email or groupId must be specified, but not both.

**Type:** object

```json
{
  "accessLevel" : "User or group's access level on shared object.",
  "modifiedAt" : "Time that the share was modified.",
  "subject" : "The subject of the email that is optionally sent to notify the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "groupId" : "Group Id if the share is a group share, else null.",
  "type" : "The type of this share.",
  "message" : "The message included in the body of the email that is optionally sent to the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "userId" : "User Id if the share is a user share, else null.",
  "createdAt" : "Time that the share was created.",
  "ccMe" : "Indicates whether to send a copy of the email to the sharer of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "scope" : "The scope of this share. One of the following values: ITEM: an item-level share (that is, the specific object to which the share applies is shared with the user or group) WORKSPACE: a workspace-level share (that is, the workspace that contains the object to which the share applies is shared with the user or group)",
  "name" : "If a user share and user is also a contact, the user's full name. If a group share, the group's name.",
  "id" : "Share Id. NOTE: unlike other Smartsheet object Ids, this Id is an alphanumeric string.",
  "email" : "User's primary email address for user shares; null for group shares."
}
```

### sendEmail

Indicate whether to notify the user by email.

**Type:** boolean

</details>

## sort_rows_in_sheet

Sorts the rows of a sheet, either in ascending or descending order.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

SortSpecifier with the following attribute:
sortCriteria -- SortCriterion array in priority order. Specifies sort order.

**Type:** object

```json
{
  "sortCriteria" : [ {
    "columnId" : "Column Id",
    "direction" : "The direction for the sort."
  } ]
}
```

### columnIds

a comma-separated list of column Ids. The response contains only the specified columns in the "columns" array, and individual rows' "cells" array only contains cells in the specified columns.

**Type:** array

```json
[ "string" ]
```

### exclude

a comma-separated list of elements to not include in the response.

**Type:** array

```json
[ "string. Possible values: filteredOutRows | linkInFromCellDetails | linksOutToCellsDetails | nonexistentCells" ]
```

### filterId

overrides the existing include={filters} parameter if both are supplied. Applies the given filter (if accessible by the calling user) and marks the affected rows as "filteredOut"= true.

**Type:** string

### ifVersionAfter

If version specified is still the current sheet version, then returns an abbreviated Sheet object with only the sheet version property. Otherwise, if the sheet has been modified, returns the complete Sheet object. Intended to allow clients with a cached copy to make sure they have the latest version.

**Type:** boolean

### include

a comma-separated list of elements to include in the response.

**Type:** array

```json
[ "string. Possible values: columnType | rowPermalink | rowWriterInfo | attachments | crossSheetReferences | discussions | filters | filterDefinitions | format | ganttConfig | objectValue | ownerInfo | source" ]
```

### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

### rowIds

a comma-separated list of row Ids on which to filter the rows included in the result

**Type:** array

```json
[ "string" ]
```

### rowNumbers

a comma-separated list of row numbers on which to filter the rows included in the result. Non-existent row numbers are ignored.

**Type:** array

```json
[ "number" ]
```

</details>

## update_an_automation_rule

Updates an existing automation rule.

<details><summary>Parameters</summary>

### automationRuleId (required)

**Type:** string

### sheetId (required)

**Type:** string

### $body

An AutomationRule object. When sending an AutomationRule, you must always specify action.type and it must match the existing rule type.

**Type:** object

```json
{
  "createdAt" : "A timestamp of when the rule was originally added.",
  "disabledReason" : "Machine-readable reason a rule is disabled. See table of Disabled Reasons.",
  "createdBy" : { },
  "modifiedAt" : "The datetime for when the change was made to the rule.",
  "name" : "Rule name as shown in the UI.",
  "userCanModify" : "If true, indicates that the current user can modify the rule.",
  "action" : {
    "notifyAllSharedUsers" : "If true, notifications are sent to all users shared to the sheet.",
    "includeAttachments" : "If true, includes attachments.",
    "recipients" : {
      "groupId" : "The Id of a group recipient.",
      "email" : "The email address of an individual recipient."
    },
    "subject" : "Email subject line.",
    "recipientColumnIds" : [ "number" ],
    "includeAllColumns" : "If true (default), all columns are included in email contents.",
    "includedColumnIds" : [ "number" ],
    "type" : "string. Possible values: APPROVAL_REQUEST_ACTION | NOTIFICATION_ACTION | UPDATE_REQUEST_ACTION",
    "message" : "Email body.",
    "frequency" : "string. Possible values: DAILY | HOURLY | IMMEDIATELY | WEEKLY",
    "includeDiscussions" : "If true, includes discussions."
  },
  "modifiedBy" : {
    "lastLogin" : "Last login time of the current user",
    "lastName" : "User's last name",
    "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
    "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
    "profileImage" : {
      "altText" : "Alternate text for the image",
      "width" : "Original width (in pixels) of the uploaded image",
      "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
      "id" : "Image Id",
      "height" : "Original height (in pixels) of the uploaded image"
    },
    "firstName" : "User's first name",
    "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
    "name" : "User's full name (read-only)",
    "id" : "User Id",
    "sheetCount" : "The number of sheets owned by the current user within the organization account",
    "email" : "User's primary email address",
    "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
    "status" : "User status"
  },
  "id" : "AutomationRule Id",
  "disabledReasonText" : "Descriptive reason a rule is disabled.",
  "enabled" : "If true, indicates that the rule is active."
}
```

</details>

## update_column

Updates properties of the column, moves the column, and/or renames the column. NOTES:

<details><summary>Parameters</summary>

### columnId (required)

**Type:** string

### sheetId (required)

**Type:** string

</details>

## update_folder

Updates the folder specified in the URL.

<details><summary>Parameters</summary>

### folderId (required)

**Type:** string

### $body

Folder object, limited to the following required attribute:
name (string)Name does not have to be unique.

**Type:** object

```json
{
  "reports" : [ {
    "sourceSheets" : [ { } ]
  } ],
  "sheets" : [ {
    "workspace" : { },
    "attachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "columns" : [ {
      "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
      "contactOptions" : [ {
        "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
        "email" : "A parsable email address."
      } ],
      "hidden" : "Indicates whether the column is hidden",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
      "description" : "Column description.",
      "index" : "Column index or position. This number is zero-based.",
      "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
      "title" : "Column title",
      "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
      "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
      "autoNumberFormat" : {
        "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
        "startingNumber" : "The starting number for the auto-id",
        "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
        "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
      },
      "options" : [ "string" ],
      "width" : "Display width of the column in pixels",
      "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
      "id" : "Column Id",
      "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
      "validation" : "Indicates whether validation has been enabled for the column (value = true)",
      "primary" : "Returned only if the column is the Primary Column (value = true)"
    } ],
    "modifiedAt" : "Time that the sheet was modified",
    "discussions" : [ { } ],
    "source" : { },
    "ownerId" : "User Id of the sheet owner",
    "resourceManagementEnabled" : "Indicates that resource management is enabled",
    "ganttEnabled" : "Indicates whether \"Gantt View\" is enabled",
    "createdAt" : "Time that the sheet was created",
    "id" : "Sheet Id",
    "totalRowCount" : "The total number of rows in the sheet",
    "owner" : "Email address of the sheet owner",
    "accessLevel" : "User's permissions on the sheet",
    "readOnly" : "Returned only if the sheet belongs to an expired trial (value = true)",
    "rows" : [ {
      "conditionalFormat" : "Describes this row's conditional format. Only returned if the include query string parameter contains format and this row has a conditional format applied.",
      "attachments" : [ {
        "createdAt" : "A timestamp of when the attachment was originally added",
        "attachmentSubType" : "Attachment sub type",
        "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
        "createdBy" : { },
        "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
        "name" : "Attachment name",
        "id" : "Attachment Id",
        "mimeType" : "Attachment MIME type (PNG, etc.)",
        "sizeInKb" : "The size of the file, if the attachmentType is FILE",
        "parentId" : "The Id of the parent",
        "parentType" : "The type of object the attachment belongs to",
        "url" : "Attachment temporary URL (files only)"
      } ],
      "indent" : "Specifies the number of levels to indent an existing row. You can specify this attribute in a request, but it is never present in a response.",
      "columns" : [ {
        "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
        "contactOptions" : [ {
          "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
          "email" : "A parsable email address."
        } ],
        "hidden" : "Indicates whether the column is hidden",
        "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
        "description" : "Column description.",
        "index" : "Column index or position. This number is zero-based.",
        "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
        "title" : "Column title",
        "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
        "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
        "autoNumberFormat" : {
          "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
          "startingNumber" : "The starting number for the auto-id",
          "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
          "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
        },
        "options" : [ "string" ],
        "width" : "Display width of the column in pixels",
        "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
        "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
        "id" : "Column Id",
        "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
        "validation" : "Indicates whether validation has been enabled for the column (value = true)",
        "primary" : "Returned only if the column is the Primary Column (value = true)"
      } ],
      "modifiedAt" : "Time of last modification",
      "discussions" : [ {
        "commentAttachments" : [ {
          "createdAt" : "A timestamp of when the attachment was originally added",
          "attachmentSubType" : "Attachment sub type",
          "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
          "createdBy" : { },
          "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
          "name" : "Attachment name",
          "id" : "Attachment Id",
          "mimeType" : "Attachment MIME type (PNG, etc.)",
          "sizeInKb" : "The size of the file, if the attachmentType is FILE",
          "parentId" : "The Id of the parent",
          "parentType" : "The type of object the attachment belongs to",
          "url" : "Attachment temporary URL (files only)"
        } ],
        "comments" : [ {
          "createdAt" : "Time of creation",
          "attachments" : [ {
            "createdAt" : "A timestamp of when the attachment was originally added",
            "attachmentSubType" : "Attachment sub type",
            "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
            "createdBy" : { },
            "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
            "name" : "Attachment name",
            "id" : "Attachment Id",
            "mimeType" : "Attachment MIME type (PNG, etc.)",
            "sizeInKb" : "The size of the file, if the attachmentType is FILE",
            "parentId" : "The Id of the parent",
            "parentType" : "The type of object the attachment belongs to",
            "url" : "Attachment temporary URL (files only)"
          } ],
          "createdBy" : { },
          "discussionId" : "Discussion Id",
          "modifiedAt" : "Time of last modification",
          "id" : "Comment Id",
          "text" : "Comment body"
        } ],
        "accessLevel" : "User's permissions on the discussion",
        "createdBy" : { },
        "readOnly" : "Indicates whether the user can modify the discussion",
        "id" : "Discussion Id",
        "lastCommentedAt" : "Time of most recent comment",
        "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
        "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
        "parentType" : "string. Possible values: SHEET | ROW",
        "commentCount" : "The number of comments in the discussion",
        "lastCommentedUser" : {
          "lastLogin" : "Last login time of the current user",
          "lastName" : "User's last name",
          "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
          "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
          "profileImage" : {
            "altText" : "Alternate text for the image",
            "width" : "Original width (in pixels) of the uploaded image",
            "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
            "id" : "Image Id",
            "height" : "Original height (in pixels) of the uploaded image"
          },
          "firstName" : "User's first name",
          "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
          "name" : "User's full name (read-only)",
          "id" : "User Id",
          "sheetCount" : "The number of sheets owned by the current user within the organization account",
          "email" : "User's primary email address",
          "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
          "status" : "User status"
        }
      } ],
      "toBottom" : "Adds or moves the row to the bottom of the sheet. You can specify this attribute in a request, but it is never present in a response.",
      "toTop" : "Adds or moves the row to the top of the sheet. You can specify this attribute in a request, but it is never present in a response.",
      "createdAt" : "Time of creation",
      "expanded" : "Indicates whether the row is expanded or collapsed",
      "inCriticalPath" : "Only returned, with a value of true, if the sheet is a project sheet with dependencies enabled and this row is in the critical path",
      "above" : "Specifies the location for a new or moved row. You can specify this attribute in a request, but it is never present in a response.",
      "outdent" : "Specifies the number of levels to outdent an existing row. You can specify this attribute in a request, but it is never present in a response.",
      "modifiedBy" : {
        "lastLogin" : "Last login time of the current user",
        "lastName" : "User's last name",
        "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
        "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
        "profileImage" : {
          "altText" : "Alternate text for the image",
          "width" : "Original width (in pixels) of the uploaded image",
          "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
          "id" : "Image Id",
          "height" : "Original height (in pixels) of the uploaded image"
        },
        "firstName" : "User's first name",
        "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
        "name" : "User's full name (read-only)",
        "id" : "User Id",
        "sheetCount" : "The number of sheets owned by the current user within the organization account",
        "email" : "User's primary email address",
        "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
        "status" : "User status"
      },
      "id" : "Row Id",
      "locked" : "Indicates whether the row is locked. In a response, a value of true indicates that the row has been locked by the sheet owner or the admin.",
      "rowNumber" : "Row number within the sheet (1-based - starts at 1)",
      "accessLevel" : "User's permission level on the sheet that contains the row",
      "format" : "Format descriptor (see Formatting). Only returned if the include query string parameter contains format and this row has a non-default format applied.",
      "version" : "Sheet version number that is incremented every time a sheet is modified",
      "parentId" : "In a response - the Id of the parent row (if any). In a request - the Id of the desired parent row (used to specify the location for a new or moved row).",
      "cells" : [ {
        "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
        "hyperlink" : { },
        "image" : { },
        "columnId" : "The Id of the column that the cell is located in",
        "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
        "objectValue" : {
          "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
        },
        "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
        "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
        "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
        "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
        "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
        "linkInFromCell" : {
          "sheetName" : "Sheet name of the linked cell",
          "columnId" : "Column Id of the linked cell",
          "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
          "rowId" : "Row Id of the linked cell",
          "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
        },
        "value" : { },
        "linksOutToCells" : [ {
          "sheetName" : "Sheet name of the linked cell",
          "columnId" : "Column Id of the linked cell",
          "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
          "rowId" : "Row Id of the linked cell",
          "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
        } ]
      } ],
      "createdBy" : { },
      "filteredOut" : "true if this row is filtered out by a column filter (and thus is not displayed in the Smartsheet app), false if the row is not filtered out. Only returned if the include query string parameter contains filters.",
      "sheetId" : "Parent sheet Id",
      "lockedForUser" : "Indicates whether the row is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "permalink" : "URL that represents a direct link to the row in SmartsheetOnly returned if the include query string parameter contains rowPermalink.",
      "siblingId" : "In a response - the Id of the previous sibling row at the same hierarchical level of this row (if any). In a request - the Id of the desired sibling row (used to specify the location for a new or moved row)."
    } ],
    "fromId" : "The Id of the template from which to create the sheet. This attribute can be specified in a request, but is never present in a response.",
    "version" : "A number that is incremented every time a sheet is modified",
    "effectiveAttachmentOptions" : [ "string" ],
    "dependenciesEnabled" : "Indicates whether dependencies are enabled",
    "showParentRowsForFilters" : "Returned only if there are column filters on the sheet. Value = true if \"show parent rows\" is enabled for the filters.",
    "userSettings" : {
      "criticalPathEnabled" : "Does this user have \"Show Critical Path\" turned on for this sheet? NOTE: This setting only has an effect on project sheets with dependencies enabled.",
      "displaySummaryTasks" : "Does this user have \"Display Summary Tasks\" turned on for this sheet? Applies only to sheets where \"Calendar View\" has been configured."
    },
    "crossSheetReferences" : [ {
      "startRowId" : "Defines beginning edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
      "startColumnId" : "Defines beginning edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
      "name" : "Friendly name of reference. Auto-generated unless specified in Create Cross-sheet References.",
      "sourceSheetId" : "Sheet Id of source sheet.",
      "endColumnId" : "Defines ending edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
      "endRowId" : "Defines ending edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
      "id" : "Cross-sheet reference Id, guaranteed unique within referencing sheet.",
      "status" : "string. Possible values: OK | BLOCKED | BROKEN | CIRCULAR | DISABLED | INVALID/UNKNOWN | NOT_SHARED"
    } ],
    "name" : "Sheet name",
    "permalink" : "URL that represents a direct link to the sheet in Smartsheet",
    "favorite" : "Returned only if the user has marked this sheet as a favorite in their Home tab (value = true)",
    "projectSettings" : {
      "nonWorkingDays" : [ "string" ],
      "workingDays" : [ "string. Possible values: MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY" ],
      "lengthOfDay" : "Length of a workday for a project sheet. Valid value must be above or equal to 1 hour, and less than or equal to 24 hours."
    }
  } ],
  "folders" : [ { } ],
  "sights" : [ {
    "createdAt" : "Time of creation",
    "backgroundColor" : "The hex color, for instance #E6F5FE",
    "workspace" : {
      "reports" : [ { } ],
      "sheets" : [ { } ],
      "folders" : [ { } ],
      "sights" : [ { } ],
      "accessLevel" : "User's permissions on the workspace",
      "templates" : [ { } ],
      "name" : "Workspace name",
      "id" : "Workspace Id",
      "permalink" : "URL that represents a direct link to the workspace in Smartsheet",
      "favorite" : "Returned only if the user has marked the workspace as a favorite in their \"Home\" tab (value = true)"
    },
    "accessLevel" : "User's permissions on the Sight.",
    "modifiedAt" : "Time of last modification",
    "name" : "Sight name",
    "id" : "Sight Id",
    "columnCount" : "Number of columns that the Sight contains",
    "permalink" : "URL that represents a direct link to the Sight in Smartsheet",
    "widgets" : [ {
      "showTitleIcon" : "True indicates that the client should display the sheet icon in the widget title",
      "xPosition" : "X-coordinate of widget's position on the Sight",
      "Rich Text" : {
        "html" : "The widget content as HTML. The Rich Text widget supports the following subset of HTML tags and CSS Styles: HTML: a - defines a hyperlink, br - inserts a single line break, li - defines a list item, ol - defines an ordered list, p - defines a paragraph, ul - defines an unordered list, span - defines a section in a document. CSS: color, font-family, font-size, font-style, font-weight, text-align, text-decoration."
      },
      "Report" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "reportId" : "Report Id denoting container source",
        "htmlContent" : "HTML snippet to render report"
      },
      "yPosition" : "Y-coordinate of widget's position on the Sight",
      "Title" : {
        "backgroundColor" : "The hex color, for instance #E6F5FE",
        "htmlContent" : "HTML snippet to render title"
      },
      "type" : "Type of widget. See table below to see how UI widget names map to type.",
      "title" : "Title of the widget",
      "viewMode" : "1 indicates content is centered. 2 indicates content is left aligned. Must use a query parameter of level=2 to see this information.",
      "Image" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "fileName" : "Name of the image file",
        "privateId" : "The image private Id",
        "format" : "formatDescriptor",
        "width" : "Original width of the image in pixels",
        "height" : "Original height of the image in pixels"
      },
      "version" : "Widget version number",
      "titleFormat" : "FormatDescriptor",
      "contents" : { },
      "showTitle" : "True indicates that the client should display the widget title. NOTE: This is independent of the title string which may be null or empty.",
      "Shortcut" : {
        "shortcutData" : [ {
          "hyperlink" : {
            "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
            "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
            "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
            "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
          },
          "attachmentType" : "Attachment type",
          "labelFormat" : "formatDescriptor",
          "label" : "Label for the data point",
          "mimeType" : "MIME type if available for attachment type",
          "order" : "The display order for the ShortcutWidgetItem object"
        } ]
      },
      "Web Content" : {
        "url" : "The URL"
      },
      "width" : "Number of columns that the widget occupies on the Sight",
      "Metric" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "columns" : [ {
          "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
          "contactOptions" : [ {
            "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
            "email" : "A parsable email address."
          } ],
          "hidden" : "Indicates whether the column is hidden",
          "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
          "description" : "Column description.",
          "index" : "Column index or position. This number is zero-based.",
          "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
          "title" : "Column title",
          "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
          "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
          "autoNumberFormat" : {
            "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
            "startingNumber" : "The starting number for the auto-id",
            "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
            "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
          },
          "options" : [ "string" ],
          "width" : "Display width of the column in pixels",
          "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
          "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
          "id" : "Column Id",
          "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
          "validation" : "Indicates whether validation has been enabled for the column (value = true)",
          "primary" : "Returned only if the column is the Primary Column (value = true)"
        } ],
        "sheetId" : "The Id of the sheet from which the cell data originates",
        "cellData" : [ {
          "labelFormat" : "formatDescriptor",
          "columnId" : "Column Id for each item",
          "valueFormat" : "formatDescriptor",
          "sheetId" : "Sheet Id for each item",
          "objectValue" : { },
          "label" : "Label for the data point. This is either the column name or a user-provided string",
          "cell" : {
            "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
            "hyperlink" : { },
            "image" : { },
            "columnId" : "The Id of the column that the cell is located in",
            "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
            "objectValue" : {
              "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
            },
            "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
            "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
            "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
            "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
            "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
            "linkInFromCell" : {
              "sheetName" : "Sheet name of the linked cell",
              "columnId" : "Column Id of the linked cell",
              "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
              "rowId" : "Row Id of the linked cell",
              "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
            },
            "value" : { },
            "linksOutToCells" : [ {
              "sheetName" : "Sheet name of the linked cell",
              "columnId" : "Column Id of the linked cell",
              "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
              "rowId" : "Row Id of the linked cell",
              "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
            } ]
          },
          "dataSource" : "CELL",
          "rowId" : "Row Id for each item",
          "order" : "The display order for the CellDataItem"
        } ]
      },
      "id" : "Widget Id",
      "Chart" : {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "reportId" : "Report Id denoting container source, if applicable",
        "legend" : "The location in the widget where Smartsheet renders the legend, for example, RIGHT",
        "series" : [ { } ],
        "axes" : [ { } ],
        "sheetId" : "Sheet Id denoting container source, if applicable",
        "includedColumnIds" : [ "number" ],
        "selectionRanges" : [ {
          "sourceRowId2" : "Defines ending edge of range when specifying one or more rows.",
          "sourceColumnId2" : "Defines ending edge of range when specifying one or more columns.",
          "sourceRowId1" : "Defines beginning edge of range when specifying one or more rows.",
          "sourceColumnId1" : "Defines beginning edge of range when specifying one or more columns."
        } ]
      },
      "height" : "Number of rows that the widget occupies on the Sight"
    } ],
    "favorite" : "Indicates whether the user has marked the Sight as a favorite"
  } ],
  "templates" : [ {
    "globalTemplate" : "Type of global template. Only applicable to blank public templates.",
    "image" : "URL to the small preview image for this template. Only applicable to non-blank public templates.",
    "largeImage" : "URL to the large preview image for this template. Only applicable to non-blank public templates.",
    "blank" : "Indicates whether the template is blank. Only applicable to public templates",
    "accessLevel" : "User's permissions on the template",
    "name" : "Template name",
    "description" : "Template description",
    "id" : "Template Id",
    "categories" : [ "string" ],
    "type" : "Type of the template. Only applicable to public templates.",
    "locale" : "Locale of the template.Only applicable to public templates.",
    "tags" : [ "string" ]
  } ],
  "name" : "Folder name",
  "id" : "Folder Id",
  "permalink" : "URL that represents a direct link to the folder in Smartsheet",
  "favorite" : "Returned only if the user has marked the folder as a favorite in their \"Home\" tab (value = true)"
}
```

</details>

## update_group

Updates the Group specified in the URL.

<details><summary>Parameters</summary>

### groupId (required)

**Type:** string

### $body

Group object, limited to the following attributes:
description (optional)
name (optional) -- must be unique within the organization account
ownerId (optional): Id of an admin user to whom the group ownership is transferred

**Type:** object

```json
{
  "owner" : "Group owner’s email address",
  "createdAt" : "Time of creation",
  "modifiedAt" : "Time of last modification",
  "members" : [ {
    "firstName" : "Group member's first name",
    "lastName" : "Group member's last name",
    "name" : "Group member's full name",
    "id" : "Group member's user Id",
    "email" : "Group member's email address"
  } ],
  "name" : "Group name",
  "description" : "Group description",
  "id" : "Group Id",
  "ownerId" : "Group owner's user Id"
}
```

</details>

## update_report_share

Updates the access level of a user or group for the specified report.

<details><summary>Parameters</summary>

### reportId (required)

**Type:** string

### shareId (required)

**Type:** string

### $body

Share object limited to the following attribute:
accessLevel (string)

**Type:** object

```json
{
  "accessLevel" : "User or group's access level on shared object.",
  "modifiedAt" : "Time that the share was modified.",
  "subject" : "The subject of the email that is optionally sent to notify the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "groupId" : "Group Id if the share is a group share, else null.",
  "type" : "The type of this share.",
  "message" : "The message included in the body of the email that is optionally sent to the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "userId" : "User Id if the share is a user share, else null.",
  "createdAt" : "Time that the share was created.",
  "ccMe" : "Indicates whether to send a copy of the email to the sharer of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "scope" : "The scope of this share. One of the following values: ITEM: an item-level share (that is, the specific object to which the share applies is shared with the user or group) WORKSPACE: a workspace-level share (that is, the workspace that contains the object to which the share applies is shared with the user or group)",
  "name" : "If a user share and user is also a contact, the user's full name. If a group share, the group's name.",
  "id" : "Share Id. NOTE: unlike other Smartsheet object Ids, this Id is an alphanumeric string.",
  "email" : "User's primary email address for user shares; null for group shares."
}
```

</details>

## update_rows

Updates cell values in the specified rows, expands/collapses the specified rows, and/or modifies the position of specified rows (including indenting/outdenting). For detailed information about changing row positions, see location-specifier attributes.

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

Row object or an array of Row objects, with the following attributes:
id (required)

One or more location-specifier attributes (optional)
expanded (optional)
format (optional)
cells (optional) -- if specified, must be an array of Cell objects, where each object is limited to the following attributes:
columnId (required)
One of the following (required):
formula: for cross-sheet formulas, you must first define a cross-sheet reference
value
When value is specified
hyperlink (optional) with exactly one of the following attributes set:
reportId
sheetId
url
linkInFromCell (optional) with all of the following attributes set:
columnId
rowId
sheetId
strict (optional)
format (optional)
image (optional) -- if specified, use to update alternate text where altText = string.
overrideValidation (optional)
locked (optional) - true to lock the row or false to unlock the row.See Column Types for more information.

NOTE:
Column Ids must be valid for the sheet to which the row belongs, and must only be used once for each row in the operation.
Cells of a project sheet in the "Finish Date" column cannot be updated via API.
Cells of a project sheet in the "Start Date" column cannot be updated via API for rows that contain a value in the "Predecessor" column.
Max length for a cell value is 4000 characters after which truncation occurs without warning. Empty string values are converted to null.
Calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = "#CIRCULAR REFERENCE". 


**Type:** object

```json
{
  "conditionalFormat" : "Describes this row's conditional format. Only returned if the include query string parameter contains format and this row has a conditional format applied.",
  "attachments" : [ {
    "createdAt" : "A timestamp of when the attachment was originally added",
    "attachmentSubType" : "Attachment sub type",
    "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
    "createdBy" : { },
    "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
    "name" : "Attachment name",
    "id" : "Attachment Id",
    "mimeType" : "Attachment MIME type (PNG, etc.)",
    "sizeInKb" : "The size of the file, if the attachmentType is FILE",
    "parentId" : "The Id of the parent",
    "parentType" : "The type of object the attachment belongs to",
    "url" : "Attachment temporary URL (files only)"
  } ],
  "indent" : "Specifies the number of levels to indent an existing row. You can specify this attribute in a request, but it is never present in a response.",
  "columns" : [ {
    "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
    "contactOptions" : [ {
      "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
      "email" : "A parsable email address."
    } ],
    "hidden" : "Indicates whether the column is hidden",
    "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
    "description" : "Column description.",
    "index" : "Column index or position. This number is zero-based.",
    "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
    "title" : "Column title",
    "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
    "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
    "autoNumberFormat" : {
      "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
      "startingNumber" : "The starting number for the auto-id",
      "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
      "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
    },
    "options" : [ "string" ],
    "width" : "Display width of the column in pixels",
    "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
    "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
    "id" : "Column Id",
    "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
    "validation" : "Indicates whether validation has been enabled for the column (value = true)",
    "primary" : "Returned only if the column is the Primary Column (value = true)"
  } ],
  "modifiedAt" : "Time of last modification",
  "discussions" : [ {
    "commentAttachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "comments" : [ {
      "createdAt" : "Time of creation",
      "attachments" : [ {
        "createdAt" : "A timestamp of when the attachment was originally added",
        "attachmentSubType" : "Attachment sub type",
        "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
        "createdBy" : { },
        "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
        "name" : "Attachment name",
        "id" : "Attachment Id",
        "mimeType" : "Attachment MIME type (PNG, etc.)",
        "sizeInKb" : "The size of the file, if the attachmentType is FILE",
        "parentId" : "The Id of the parent",
        "parentType" : "The type of object the attachment belongs to",
        "url" : "Attachment temporary URL (files only)"
      } ],
      "createdBy" : { },
      "discussionId" : "Discussion Id",
      "modifiedAt" : "Time of last modification",
      "id" : "Comment Id",
      "text" : "Comment body"
    } ],
    "accessLevel" : "User's permissions on the discussion",
    "createdBy" : { },
    "readOnly" : "Indicates whether the user can modify the discussion",
    "id" : "Discussion Id",
    "lastCommentedAt" : "Time of most recent comment",
    "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
    "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
    "parentType" : "string. Possible values: SHEET | ROW",
    "commentCount" : "The number of comments in the discussion",
    "lastCommentedUser" : {
      "lastLogin" : "Last login time of the current user",
      "lastName" : "User's last name",
      "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
      "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
      "profileImage" : {
        "altText" : "Alternate text for the image",
        "width" : "Original width (in pixels) of the uploaded image",
        "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
        "id" : "Image Id",
        "height" : "Original height (in pixels) of the uploaded image"
      },
      "firstName" : "User's first name",
      "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
      "name" : "User's full name (read-only)",
      "id" : "User Id",
      "sheetCount" : "The number of sheets owned by the current user within the organization account",
      "email" : "User's primary email address",
      "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
      "status" : "User status"
    }
  } ],
  "toBottom" : "Adds or moves the row to the bottom of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "toTop" : "Adds or moves the row to the top of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "createdAt" : "Time of creation",
  "expanded" : "Indicates whether the row is expanded or collapsed",
  "inCriticalPath" : "Only returned, with a value of true, if the sheet is a project sheet with dependencies enabled and this row is in the critical path",
  "above" : "Specifies the location for a new or moved row. You can specify this attribute in a request, but it is never present in a response.",
  "outdent" : "Specifies the number of levels to outdent an existing row. You can specify this attribute in a request, but it is never present in a response.",
  "modifiedBy" : {
    "lastLogin" : "Last login time of the current user",
    "lastName" : "User's last name",
    "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
    "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
    "profileImage" : {
      "altText" : "Alternate text for the image",
      "width" : "Original width (in pixels) of the uploaded image",
      "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
      "id" : "Image Id",
      "height" : "Original height (in pixels) of the uploaded image"
    },
    "firstName" : "User's first name",
    "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
    "name" : "User's full name (read-only)",
    "id" : "User Id",
    "sheetCount" : "The number of sheets owned by the current user within the organization account",
    "email" : "User's primary email address",
    "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
    "status" : "User status"
  },
  "id" : "Row Id",
  "locked" : "Indicates whether the row is locked. In a response, a value of true indicates that the row has been locked by the sheet owner or the admin.",
  "rowNumber" : "Row number within the sheet (1-based - starts at 1)",
  "accessLevel" : "User's permission level on the sheet that contains the row",
  "format" : "Format descriptor (see Formatting). Only returned if the include query string parameter contains format and this row has a non-default format applied.",
  "version" : "Sheet version number that is incremented every time a sheet is modified",
  "parentId" : "In a response - the Id of the parent row (if any). In a request - the Id of the desired parent row (used to specify the location for a new or moved row).",
  "cells" : [ {
    "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
    "hyperlink" : { },
    "image" : { },
    "columnId" : "The Id of the column that the cell is located in",
    "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
    "objectValue" : {
      "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
    },
    "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
    "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
    "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
    "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
    "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
    "linkInFromCell" : {
      "sheetName" : "Sheet name of the linked cell",
      "columnId" : "Column Id of the linked cell",
      "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
      "rowId" : "Row Id of the linked cell",
      "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
    },
    "value" : { },
    "linksOutToCells" : [ {
      "sheetName" : "Sheet name of the linked cell",
      "columnId" : "Column Id of the linked cell",
      "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
      "rowId" : "Row Id of the linked cell",
      "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
    } ]
  } ],
  "createdBy" : { },
  "filteredOut" : "true if this row is filtered out by a column filter (and thus is not displayed in the Smartsheet app), false if the row is not filtered out. Only returned if the include query string parameter contains filters.",
  "sheetId" : "Parent sheet Id",
  "lockedForUser" : "Indicates whether the row is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
  "permalink" : "URL that represents a direct link to the row in SmartsheetOnly returned if the include query string parameter contains rowPermalink.",
  "siblingId" : "In a response - the Id of the previous sibling row at the same hierarchical level of this row (if any). In a request - the Id of the desired sibling row (used to specify the location for a new or moved row)."
}
```

### allowPartialSuccess

If true, allows bulk operations to process even if one or more operations are invalid for some reason.

**Type:** boolean

### overrideValidation

You may use the query string parameter overrideValidation with a value of true to allow a cell value outside of the validation limits. You must specify strict with a value of false to bypass value type checking.

**Type:** boolean

</details>

## update_sheet

Updates the sheet specified in the URL. To modify sheet contents, see Add Rows, Update Rows, Add Columns, and Update Column. This operation can be used to update an individual user's sheet settings.  If the request body contains only the userSettings attribute, this operation may be performed even if the user
only has read-only access to the sheet (for example, the user has viewer permissions or the sheet is read-only).

<details><summary>Parameters</summary>

### sheetId (required)

**Type:** string

### $body

Sheet object limited to the following attributes:
name (optional)
projectSettings (optional): ProjectSettings object, containing at least one of the projectSettings attributes, for updating this sheet's project settings and dependencies.
userSettings (optional): SheetUserSettings object for updating these user's settings for the sheetNOTE:
Attributes not specified in projectSettings are not updated.
If projectSettings.nonWorkingDays is specified as an empty array, all non-working days are removed from the project sheet.

**Type:** object

```json
{
  "workspace" : { },
  "attachments" : [ {
    "createdAt" : "A timestamp of when the attachment was originally added",
    "attachmentSubType" : "Attachment sub type",
    "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
    "createdBy" : { },
    "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
    "name" : "Attachment name",
    "id" : "Attachment Id",
    "mimeType" : "Attachment MIME type (PNG, etc.)",
    "sizeInKb" : "The size of the file, if the attachmentType is FILE",
    "parentId" : "The Id of the parent",
    "parentType" : "The type of object the attachment belongs to",
    "url" : "Attachment temporary URL (files only)"
  } ],
  "columns" : [ {
    "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
    "contactOptions" : [ {
      "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
      "email" : "A parsable email address."
    } ],
    "hidden" : "Indicates whether the column is hidden",
    "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
    "description" : "Column description.",
    "index" : "Column index or position. This number is zero-based.",
    "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
    "title" : "Column title",
    "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
    "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
    "autoNumberFormat" : {
      "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
      "startingNumber" : "The starting number for the auto-id",
      "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
      "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
    },
    "options" : [ "string" ],
    "width" : "Display width of the column in pixels",
    "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
    "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
    "id" : "Column Id",
    "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
    "validation" : "Indicates whether validation has been enabled for the column (value = true)",
    "primary" : "Returned only if the column is the Primary Column (value = true)"
  } ],
  "modifiedAt" : "Time that the sheet was modified",
  "discussions" : [ { } ],
  "source" : { },
  "ownerId" : "User Id of the sheet owner",
  "resourceManagementEnabled" : "Indicates that resource management is enabled",
  "ganttEnabled" : "Indicates whether \"Gantt View\" is enabled",
  "createdAt" : "Time that the sheet was created",
  "id" : "Sheet Id",
  "totalRowCount" : "The total number of rows in the sheet",
  "owner" : "Email address of the sheet owner",
  "accessLevel" : "User's permissions on the sheet",
  "readOnly" : "Returned only if the sheet belongs to an expired trial (value = true)",
  "rows" : [ {
    "conditionalFormat" : "Describes this row's conditional format. Only returned if the include query string parameter contains format and this row has a conditional format applied.",
    "attachments" : [ {
      "createdAt" : "A timestamp of when the attachment was originally added",
      "attachmentSubType" : "Attachment sub type",
      "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
      "createdBy" : { },
      "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
      "name" : "Attachment name",
      "id" : "Attachment Id",
      "mimeType" : "Attachment MIME type (PNG, etc.)",
      "sizeInKb" : "The size of the file, if the attachmentType is FILE",
      "parentId" : "The Id of the parent",
      "parentType" : "The type of object the attachment belongs to",
      "url" : "Attachment temporary URL (files only)"
    } ],
    "indent" : "Specifies the number of levels to indent an existing row. You can specify this attribute in a request, but it is never present in a response.",
    "columns" : [ {
      "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
      "contactOptions" : [ {
        "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
        "email" : "A parsable email address."
      } ],
      "hidden" : "Indicates whether the column is hidden",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
      "description" : "Column description.",
      "index" : "Column index or position. This number is zero-based.",
      "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
      "title" : "Column title",
      "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
      "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
      "autoNumberFormat" : {
        "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
        "startingNumber" : "The starting number for the auto-id",
        "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
        "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
      },
      "options" : [ "string" ],
      "width" : "Display width of the column in pixels",
      "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
      "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
      "id" : "Column Id",
      "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
      "validation" : "Indicates whether validation has been enabled for the column (value = true)",
      "primary" : "Returned only if the column is the Primary Column (value = true)"
    } ],
    "modifiedAt" : "Time of last modification",
    "discussions" : [ {
      "commentAttachments" : [ {
        "createdAt" : "A timestamp of when the attachment was originally added",
        "attachmentSubType" : "Attachment sub type",
        "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
        "createdBy" : { },
        "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
        "name" : "Attachment name",
        "id" : "Attachment Id",
        "mimeType" : "Attachment MIME type (PNG, etc.)",
        "sizeInKb" : "The size of the file, if the attachmentType is FILE",
        "parentId" : "The Id of the parent",
        "parentType" : "The type of object the attachment belongs to",
        "url" : "Attachment temporary URL (files only)"
      } ],
      "comments" : [ {
        "createdAt" : "Time of creation",
        "attachments" : [ {
          "createdAt" : "A timestamp of when the attachment was originally added",
          "attachmentSubType" : "Attachment sub type",
          "attachmentType" : "string. Possible values: BOX_COM | DROPBOX | EGNYTE | EVERNOTE | FILE | GOOGLE_DRIVE | LINK | ONEDRIVE",
          "createdBy" : { },
          "urlExpiresInMillis" : "Attachment temporary URL time to live (files only)",
          "name" : "Attachment name",
          "id" : "Attachment Id",
          "mimeType" : "Attachment MIME type (PNG, etc.)",
          "sizeInKb" : "The size of the file, if the attachmentType is FILE",
          "parentId" : "The Id of the parent",
          "parentType" : "The type of object the attachment belongs to",
          "url" : "Attachment temporary URL (files only)"
        } ],
        "createdBy" : { },
        "discussionId" : "Discussion Id",
        "modifiedAt" : "Time of last modification",
        "id" : "Comment Id",
        "text" : "Comment body"
      } ],
      "accessLevel" : "User's permissions on the discussion",
      "createdBy" : { },
      "readOnly" : "Indicates whether the user can modify the discussion",
      "id" : "Discussion Id",
      "lastCommentedAt" : "Time of most recent comment",
      "title" : "Read Only. Discussion title automatically created by duplicating the first 100 characters of the top-level comment",
      "parentId" : "Id of the directly associated row or sheet: present only when the direct association is not clear (see List Discussions)",
      "parentType" : "string. Possible values: SHEET | ROW",
      "commentCount" : "The number of comments in the discussion",
      "lastCommentedUser" : {
        "lastLogin" : "Last login time of the current user",
        "lastName" : "User's last name",
        "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
        "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
        "profileImage" : {
          "altText" : "Alternate text for the image",
          "width" : "Original width (in pixels) of the uploaded image",
          "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
          "id" : "Image Id",
          "height" : "Original height (in pixels) of the uploaded image"
        },
        "firstName" : "User's first name",
        "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
        "name" : "User's full name (read-only)",
        "id" : "User Id",
        "sheetCount" : "The number of sheets owned by the current user within the organization account",
        "email" : "User's primary email address",
        "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
        "status" : "User status"
      }
    } ],
    "toBottom" : "Adds or moves the row to the bottom of the sheet. You can specify this attribute in a request, but it is never present in a response.",
    "toTop" : "Adds or moves the row to the top of the sheet. You can specify this attribute in a request, but it is never present in a response.",
    "createdAt" : "Time of creation",
    "expanded" : "Indicates whether the row is expanded or collapsed",
    "inCriticalPath" : "Only returned, with a value of true, if the sheet is a project sheet with dependencies enabled and this row is in the critical path",
    "above" : "Specifies the location for a new or moved row. You can specify this attribute in a request, but it is never present in a response.",
    "outdent" : "Specifies the number of levels to outdent an existing row. You can specify this attribute in a request, but it is never present in a response.",
    "modifiedBy" : {
      "lastLogin" : "Last login time of the current user",
      "lastName" : "User's last name",
      "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
      "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
      "profileImage" : {
        "altText" : "Alternate text for the image",
        "width" : "Original width (in pixels) of the uploaded image",
        "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
        "id" : "Image Id",
        "height" : "Original height (in pixels) of the uploaded image"
      },
      "firstName" : "User's first name",
      "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
      "name" : "User's full name (read-only)",
      "id" : "User Id",
      "sheetCount" : "The number of sheets owned by the current user within the organization account",
      "email" : "User's primary email address",
      "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
      "status" : "User status"
    },
    "id" : "Row Id",
    "locked" : "Indicates whether the row is locked. In a response, a value of true indicates that the row has been locked by the sheet owner or the admin.",
    "rowNumber" : "Row number within the sheet (1-based - starts at 1)",
    "accessLevel" : "User's permission level on the sheet that contains the row",
    "format" : "Format descriptor (see Formatting). Only returned if the include query string parameter contains format and this row has a non-default format applied.",
    "version" : "Sheet version number that is incremented every time a sheet is modified",
    "parentId" : "In a response - the Id of the parent row (if any). In a request - the Id of the desired parent row (used to specify the location for a new or moved row).",
    "cells" : [ {
      "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
      "hyperlink" : { },
      "image" : { },
      "columnId" : "The Id of the column that the cell is located in",
      "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
      "objectValue" : {
        "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
      },
      "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
      "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
      "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
      "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
      "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
      "linkInFromCell" : {
        "sheetName" : "Sheet name of the linked cell",
        "columnId" : "Column Id of the linked cell",
        "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
        "rowId" : "Row Id of the linked cell",
        "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
      },
      "value" : { },
      "linksOutToCells" : [ {
        "sheetName" : "Sheet name of the linked cell",
        "columnId" : "Column Id of the linked cell",
        "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
        "rowId" : "Row Id of the linked cell",
        "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
      } ]
    } ],
    "createdBy" : { },
    "filteredOut" : "true if this row is filtered out by a column filter (and thus is not displayed in the Smartsheet app), false if the row is not filtered out. Only returned if the include query string parameter contains filters.",
    "sheetId" : "Parent sheet Id",
    "lockedForUser" : "Indicates whether the row is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
    "permalink" : "URL that represents a direct link to the row in SmartsheetOnly returned if the include query string parameter contains rowPermalink.",
    "siblingId" : "In a response - the Id of the previous sibling row at the same hierarchical level of this row (if any). In a request - the Id of the desired sibling row (used to specify the location for a new or moved row)."
  } ],
  "fromId" : "The Id of the template from which to create the sheet. This attribute can be specified in a request, but is never present in a response.",
  "version" : "A number that is incremented every time a sheet is modified",
  "effectiveAttachmentOptions" : [ "string" ],
  "dependenciesEnabled" : "Indicates whether dependencies are enabled",
  "showParentRowsForFilters" : "Returned only if there are column filters on the sheet. Value = true if \"show parent rows\" is enabled for the filters.",
  "userSettings" : {
    "criticalPathEnabled" : "Does this user have \"Show Critical Path\" turned on for this sheet? NOTE: This setting only has an effect on project sheets with dependencies enabled.",
    "displaySummaryTasks" : "Does this user have \"Display Summary Tasks\" turned on for this sheet? Applies only to sheets where \"Calendar View\" has been configured."
  },
  "crossSheetReferences" : [ {
    "startRowId" : "Defines beginning edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
    "startColumnId" : "Defines beginning edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
    "name" : "Friendly name of reference. Auto-generated unless specified in Create Cross-sheet References.",
    "sourceSheetId" : "Sheet Id of source sheet.",
    "endColumnId" : "Defines ending edge of range when specifying one or more columns. To specify an entire column, omit the startRowId and endRowId parameters.",
    "endRowId" : "Defines ending edge of range when specifying one or more rows. To specify an entire row, omit the startColumnId and endColumnId parameters.",
    "id" : "Cross-sheet reference Id, guaranteed unique within referencing sheet.",
    "status" : "string. Possible values: OK | BLOCKED | BROKEN | CIRCULAR | DISABLED | INVALID/UNKNOWN | NOT_SHARED"
  } ],
  "name" : "Sheet name",
  "permalink" : "URL that represents a direct link to the sheet in Smartsheet",
  "favorite" : "Returned only if the user has marked this sheet as a favorite in their Home tab (value = true)",
  "projectSettings" : {
    "nonWorkingDays" : [ "string" ],
    "workingDays" : [ "string. Possible values: MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY" ],
    "lengthOfDay" : "Length of a workday for a project sheet. Valid value must be above or equal to 1 hour, and less than or equal to 24 hours."
  }
}
```

</details>

## update_sheet_share

Updates the access level of a user or group for the specified sheet.

<details><summary>Parameters</summary>

### shareId (required)

**Type:** string

### sheetId (required)

**Type:** string

### $body

Share object limited to the following attribute:
accessLevel (string)

**Type:** object

```json
{
  "accessLevel" : "User or group's access level on shared object.",
  "modifiedAt" : "Time that the share was modified.",
  "subject" : "The subject of the email that is optionally sent to notify the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "groupId" : "Group Id if the share is a group share, else null.",
  "type" : "The type of this share.",
  "message" : "The message included in the body of the email that is optionally sent to the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "userId" : "User Id if the share is a user share, else null.",
  "createdAt" : "Time that the share was created.",
  "ccMe" : "Indicates whether to send a copy of the email to the sharer of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "scope" : "The scope of this share. One of the following values: ITEM: an item-level share (that is, the specific object to which the share applies is shared with the user or group) WORKSPACE: a workspace-level share (that is, the workspace that contains the object to which the share applies is shared with the user or group)",
  "name" : "If a user share and user is also a contact, the user's full name. If a group share, the group's name.",
  "id" : "Share Id. NOTE: unlike other Smartsheet object Ids, this Id is an alphanumeric string.",
  "email" : "User's primary email address for user shares; null for group shares."
}
```

</details>

## update_sight

Updates (renames) the specified Sight.

<details><summary>Parameters</summary>

### sightId (required)

**Type:** string

### $body

Sight object limited to the following attribute:
name (string)

**Type:** object

```json
{
  "createdAt" : "Time of creation",
  "backgroundColor" : "The hex color, for instance #E6F5FE",
  "workspace" : {
    "reports" : [ { } ],
    "sheets" : [ { } ],
    "folders" : [ { } ],
    "sights" : [ { } ],
    "accessLevel" : "User's permissions on the workspace",
    "templates" : [ { } ],
    "name" : "Workspace name",
    "id" : "Workspace Id",
    "permalink" : "URL that represents a direct link to the workspace in Smartsheet",
    "favorite" : "Returned only if the user has marked the workspace as a favorite in their \"Home\" tab (value = true)"
  },
  "accessLevel" : "User's permissions on the Sight.",
  "modifiedAt" : "Time of last modification",
  "name" : "Sight name",
  "id" : "Sight Id",
  "columnCount" : "Number of columns that the Sight contains",
  "permalink" : "URL that represents a direct link to the Sight in Smartsheet",
  "widgets" : [ {
    "showTitleIcon" : "True indicates that the client should display the sheet icon in the widget title",
    "xPosition" : "X-coordinate of widget's position on the Sight",
    "Rich Text" : {
      "html" : "The widget content as HTML. The Rich Text widget supports the following subset of HTML tags and CSS Styles: HTML: a - defines a hyperlink, br - inserts a single line break, li - defines a list item, ol - defines an ordered list, p - defines a paragraph, ul - defines an unordered list, span - defines a section in a document. CSS: color, font-family, font-size, font-style, font-weight, text-align, text-decoration."
    },
    "Report" : {
      "hyperlink" : {
        "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
        "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
        "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
        "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
      },
      "reportId" : "Report Id denoting container source",
      "htmlContent" : "HTML snippet to render report"
    },
    "yPosition" : "Y-coordinate of widget's position on the Sight",
    "Title" : {
      "backgroundColor" : "The hex color, for instance #E6F5FE",
      "htmlContent" : "HTML snippet to render title"
    },
    "type" : "Type of widget. See table below to see how UI widget names map to type.",
    "title" : "Title of the widget",
    "viewMode" : "1 indicates content is centered. 2 indicates content is left aligned. Must use a query parameter of level=2 to see this information.",
    "Image" : {
      "hyperlink" : {
        "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
        "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
        "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
        "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
      },
      "fileName" : "Name of the image file",
      "privateId" : "The image private Id",
      "format" : "formatDescriptor",
      "width" : "Original width of the image in pixels",
      "height" : "Original height of the image in pixels"
    },
    "version" : "Widget version number",
    "titleFormat" : "FormatDescriptor",
    "contents" : { },
    "showTitle" : "True indicates that the client should display the widget title. NOTE: This is independent of the title string which may be null or empty.",
    "Shortcut" : {
      "shortcutData" : [ {
        "hyperlink" : {
          "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
          "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
          "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
          "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
        },
        "attachmentType" : "Attachment type",
        "labelFormat" : "formatDescriptor",
        "label" : "Label for the data point",
        "mimeType" : "MIME type if available for attachment type",
        "order" : "The display order for the ShortcutWidgetItem object"
      } ]
    },
    "Web Content" : {
      "url" : "The URL"
    },
    "width" : "Number of columns that the widget occupies on the Sight",
    "Metric" : {
      "hyperlink" : {
        "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
        "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
        "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
        "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
      },
      "columns" : [ {
        "symbol" : "When applicable for CHECKBOX or PICKLIST column types.",
        "contactOptions" : [ {
          "name" : "Can be a user's name, display name, or free text, such as a job class or TBD.",
          "email" : "A parsable email address."
        } ],
        "hidden" : "Indicates whether the column is hidden",
        "format" : "The format descriptor. Only returned if the include query string parameter contains format and this column has a non-default format applied to it.",
        "description" : "Column description.",
        "index" : "Column index or position. This number is zero-based.",
        "type" : "string. Possible values: ABSTRACT_DATETIME | CHECKBOX | CONTACT_LIST | DATE | DATETIME | DURATION | MULTI_CONTACT_LIST | PICKLIST | PREDECESSOR | TEXT_NUMBER",
        "title" : "Column title",
        "version" : "A zero-based integer indicating whether the column allows multi-contact data. A value of 0 indicates the data will be stored as text and the column type will be TEXT_NUMBER, a value of 1 for sheets and reports or a value of 2 for Sights (aka dashboards) indicates the data will be stored as contacts and the column type will be MULTI_CONTACT_LIST. If not specified, the default value is 0 for sheets and reports or 1 for Sights (aka dashboards).",
        "tags" : [ "string. Possible values: CALENDAR_END_DATE | CALENDAR_START_DATE | GANTT_ALLOCATION | GANTT_ASSIGNED_RESOURCE | GANTT_DISPLAY_LABEL | GANTT_DURATION | GANTT_END_DATE | GANTT_PERCENT_COMPLETE | GANTT_PREDECESSOR | GANTT_START_DATE" ],
        "autoNumberFormat" : {
          "prefix" : "The prefix. Can include the date tokens:{YY}{YYYY}{MM}{DD}",
          "startingNumber" : "The starting number for the auto-id",
          "fill" : "Indicates zero-padding. Must be between 0 and 10 \"0\" (zero) characters.",
          "suffix" : "The suffix. Can include the date tokens:{YY}{YYYY}{MM}{DD}"
        },
        "options" : [ "string" ],
        "width" : "Display width of the column in pixels",
        "lockedForUser" : "Indicates whether the column is locked for the requesting user. This attribute may be present in a response, but cannot be specified in a request.",
        "systemColumnType" : "string. Possible values: AUTO_NUMBER | CREATED_BY | CREATED_DATE | MODIFIED_BY | MODIFIED_DATE",
        "id" : "Column Id",
        "locked" : "Indicates whether the column is locked. In a response, a value of true indicates that the column has been locked by the sheet owner or the admin.",
        "validation" : "Indicates whether validation has been enabled for the column (value = true)",
        "primary" : "Returned only if the column is the Primary Column (value = true)"
      } ],
      "sheetId" : "The Id of the sheet from which the cell data originates",
      "cellData" : [ {
        "labelFormat" : "formatDescriptor",
        "columnId" : "Column Id for each item",
        "valueFormat" : "formatDescriptor",
        "sheetId" : "Sheet Id for each item",
        "objectValue" : { },
        "label" : "Label for the data point. This is either the column name or a user-provided string",
        "cell" : {
          "conditionalFormat" : "The format descriptor describing this cell's conditional format (see Formatting). Only returned if the include query string parameter contains format and this cell has a conditional format applied.",
          "hyperlink" : { },
          "image" : { },
          "columnId" : "The Id of the column that the cell is located in",
          "format" : "The format descriptor. Only returned if the include query string parameter contains format and this cell has a non-default format applied.",
          "objectValue" : {
            "objectType" : "string. Possible values: ABSTRACT_DATETIME | CONTACT | DATE | DATETIME | DURATION | MULTI_CONTACT | PREDECESSOR_LIST"
          },
          "overrideValidation" : "(Admin only) Indicates whether the cell value can contain a value outside of the validation limits (value = true). When using this parameter, you must also set strict to false to bypass value type checking. This property is honored for POST or PUT actions that update rows.",
          "displayValue" : "Visual representation of cell contents, as presented to the user in the UI.",
          "columnType" : "See type definition on the Column object. Only returned if the include query string parameter contains columnType.",
          "formula" : "The formula for a cell, if set. NOTE: calculation errors or problems with a formula do not cause the API call to return an error code. Instead, the response contains the same value as in the UI, such as cell.value = \"#CIRCULAR REFERENCE\".",
          "strict" : "Set to false to enable lenient parsing. Defaults to true. You can specify this attribute in a request, but it is never present in a response. See Cell Value Parsing for more information about using this attribute.",
          "linkInFromCell" : {
            "sheetName" : "Sheet name of the linked cell",
            "columnId" : "Column Id of the linked cell",
            "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
            "rowId" : "Row Id of the linked cell",
            "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
          },
          "value" : { },
          "linksOutToCells" : [ {
            "sheetName" : "Sheet name of the linked cell",
            "columnId" : "Column Id of the linked cell",
            "sheetId" : "Sheet Id of the sheet that the linked cell belongs to",
            "rowId" : "Row Id of the linked cell",
            "status" : "string. Possible values: OK | BROKEN | INACCESSIBLE | BLOCKED | CIRCULAR | DISABLED | INVALID | NOT_SHARED"
          } ]
        },
        "dataSource" : "CELL",
        "rowId" : "Row Id for each item",
        "order" : "The display order for the CellDataItem"
      } ]
    },
    "id" : "Widget Id",
    "Chart" : {
      "hyperlink" : {
        "reportId" : "If non-null, this hyperlink is a link to the report with this Id.",
        "sheetId" : "If non-null, this hyperlink is a link to the sheet with this Id.",
        "sightId" : "If non-null, this hyperlink is a link to the Sight with this Id.",
        "url" : "When the hyperlink is a URL link, this property contains the URL value. When the hyperlink is a sheet/report/Sight link (that is, sheetId, reportId, or sightId is non-null), this property contains the permalink to the sheet, report, or Sight."
      },
      "reportId" : "Report Id denoting container source, if applicable",
      "legend" : "The location in the widget where Smartsheet renders the legend, for example, RIGHT",
      "series" : [ { } ],
      "axes" : [ { } ],
      "sheetId" : "Sheet Id denoting container source, if applicable",
      "includedColumnIds" : [ "number" ],
      "selectionRanges" : [ {
        "sourceRowId2" : "Defines ending edge of range when specifying one or more rows.",
        "sourceColumnId2" : "Defines ending edge of range when specifying one or more columns.",
        "sourceRowId1" : "Defines beginning edge of range when specifying one or more rows.",
        "sourceColumnId1" : "Defines beginning edge of range when specifying one or more columns."
      } ]
    },
    "height" : "Number of rows that the widget occupies on the Sight"
  } ],
  "favorite" : "Indicates whether the user has marked the Sight as a favorite"
}
```

</details>

## update_sight_share

Updates the access level of a user or group for the specified Sight.

<details><summary>Parameters</summary>

### shareId (required)

**Type:** string

### sightId (required)

**Type:** string

### $body

Share object limited to the following attribute:
accessLevel (string)

**Type:** object

```json
{
  "accessLevel" : "User or group's access level on shared object.",
  "modifiedAt" : "Time that the share was modified.",
  "subject" : "The subject of the email that is optionally sent to notify the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "groupId" : "Group Id if the share is a group share, else null.",
  "type" : "The type of this share.",
  "message" : "The message included in the body of the email that is optionally sent to the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "userId" : "User Id if the share is a user share, else null.",
  "createdAt" : "Time that the share was created.",
  "ccMe" : "Indicates whether to send a copy of the email to the sharer of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "scope" : "The scope of this share. One of the following values: ITEM: an item-level share (that is, the specific object to which the share applies is shared with the user or group) WORKSPACE: a workspace-level share (that is, the workspace that contains the object to which the share applies is shared with the user or group)",
  "name" : "If a user share and user is also a contact, the user's full name. If a group share, the group's name.",
  "id" : "Share Id. NOTE: unlike other Smartsheet object Ids, this Id is an alphanumeric string.",
  "email" : "User's primary email address for user shares; null for group shares."
}
```

</details>

## update_user

Updates the user specified in the URL.

<details><summary>Parameters</summary>

### userId (required)

**Type:** string

### $body

User object containing at least one of the following attributes:
admin (required)
licensedSheetCreator (required)
firstName (optional)
groupAdmin (optional)
lastName (optional)
resourceViewer (optional)

**Type:** object

```json
{
  "lastLogin" : "Last login time of the current user",
  "lastName" : "User's last name",
  "customWelcomeScreenViewed" : "Timestamp of viewing an Enterprise Custom Welcome Screen by the current user",
  "admin" : "Indicates whether the user is a system admin (can manage user accounts and organization account)",
  "profileImage" : {
    "altText" : "Alternate text for the image",
    "width" : "Original width (in pixels) of the uploaded image",
    "resourceViewer" : "Indicates whether the user is a resource viewer (can access resource views)",
    "id" : "Image Id",
    "height" : "Original height (in pixels) of the uploaded image"
  },
  "firstName" : "User's first name",
  "groupAdmin" : "Indicates whether the user is a group admin (can create and edit groups)",
  "name" : "User's full name (read-only)",
  "id" : "User Id",
  "sheetCount" : "The number of sheets owned by the current user within the organization account",
  "email" : "User's primary email address",
  "licensedSheetCreator" : "Indicates whether the user is a licensed user (can create and own sheets)",
  "status" : "User status"
}
```

</details>

## update_user_profile_image

Uploads an image to the user profile.

<details><summary>Parameters</summary>

### userId (required)

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## update_webhook

Updates the webhook specified in the URL.

<details><summary>Parameters</summary>

### webhookId (required)

**Type:** string

### $body

Webhook object, limited to the following attributes:
callbackUrl (optional)
enabled (optional)
events (optional)
name (optional)
version (optional)

**Type:** object

```json
{
  "apiClientName" : "API client name corresponding to third-party app that created the webhook. Read-only. Only present if webhook was created by third-party app.",
  "disabledDetails" : "Details about the reason the webhook was disabled. Read-only. Only present when enabled=false.",
  "modifiedAt" : "Time of last modification. Read-only.",
  "version" : "Webhook version. Currently, the only supported value is 1. This attribute is intended to ensure backward compatibility as new webhook functionality is released. For example, a webhook with a version of 1 is guaranteed to always be sent callback objects that are compatible with the version 1 release of webhooks.",
  "enabled" : "Indicates whether the webhook is on (true) or off (false)",
  "createdAt" : "Time of creation. Read-only.",
  "stats" : {
    "lastCallbackAttemptRetryCount" : "The number of retries the webhook had performed as of the last callback attempt.",
    "lastSuccessfulCallback" : "When this webhook last made a successful callback.",
    "lastCallbackAttempt" : "When this webhook last made a callback attempt."
  },
  "scopeObjectId" : "Id of the object that is subscribed to. Specified when a webhook is created and cannot be changed.",
  "scope" : "Scope of the subscription. Currently, the only supported value is sheet. Specified when a webhook is created and cannot be changed.",
  "name" : "Webhook name",
  "apiClientId" : "API client Id corresponding to third-party app that created the webhook. Read-only. Only present if webhook was created by third-party app.",
  "callbackUrl" : "HTTPS URL where callbacks are sent. NOTES: Smartsheet webhooks do not support callbacks to servers using self-signed certificates. The callback server must be using a signed certificate from a certificate authority. The callbackURL must use one of the following ports: 443 (default for HTTPS), 8000, 8008, 8080, or 8443.",
  "id" : "Webhook Id",
  "sharedSecret" : "Shared secret for this webhook, randomly generated by Smartsheet. Read-only. See Authenticating Callbacks for details about how this value can be used.",
  "events" : [ "string" ],
  "status" : "Webhook status. Read-only. See Webhook Status for list of possible values."
}
```

</details>

## update_workspace

Updates the workspace specified in the URL.

<details><summary>Parameters</summary>

### workspaceid (required)

**Type:** string

### $body

Workspace object limited to the following attribute:
name (string)

**Type:** object

```json
{
  "reports" : [ { } ],
  "sheets" : [ { } ],
  "folders" : [ { } ],
  "sights" : [ { } ],
  "accessLevel" : "User's permissions on the workspace",
  "templates" : [ { } ],
  "name" : "Workspace name",
  "id" : "Workspace Id",
  "permalink" : "URL that represents a direct link to the workspace in Smartsheet",
  "favorite" : "Returned only if the user has marked the workspace as a favorite in their \"Home\" tab (value = true)"
}
```

</details>

## update_workspace_share

Updates the access level of a user or group for the specified workspace.

<details><summary>Parameters</summary>

### shareId (required)

**Type:** string

### workspaceId (required)

**Type:** string

### $body

Share object limited to the following attribute:
accessLevel (string)

**Type:** object

```json
{
  "accessLevel" : "User or group's access level on shared object.",
  "modifiedAt" : "Time that the share was modified.",
  "subject" : "The subject of the email that is optionally sent to notify the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "groupId" : "Group Id if the share is a group share, else null.",
  "type" : "The type of this share.",
  "message" : "The message included in the body of the email that is optionally sent to the recipient. You can specify this attribute in a request, but it is never present in a response.",
  "userId" : "User Id if the share is a user share, else null.",
  "createdAt" : "Time that the share was created.",
  "ccMe" : "Indicates whether to send a copy of the email to the sharer of the sheet. You can specify this attribute in a request, but it is never present in a response.",
  "scope" : "The scope of this share. One of the following values: ITEM: an item-level share (that is, the specific object to which the share applies is shared with the user or group) WORKSPACE: a workspace-level share (that is, the workspace that contains the object to which the share applies is shared with the user or group)",
  "name" : "If a user share and user is also a contact, the user's full name. If a group share, the group's name.",
  "id" : "Share Id. NOTE: unlike other Smartsheet object Ids, this Id is an alphanumeric string.",
  "email" : "User's primary email address for user shares; null for group shares."
}
```

</details>

