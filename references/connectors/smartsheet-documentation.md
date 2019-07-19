---
id: smartsheet-documentation
title: Smartsheet (version v1.*.*)
sidebar_label: Smartsheet
layout: docs.mustache
---

## add_alternate_emails

Adds one or more alternate email addresses for the specified user.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### $body

Array of AlternateEmail objects, each limited to only the email attribute

**Type:** object

</details>

## add_columns

Inserts one or more columns into the sheet specified in the URL. This operation can be performed using a simple upload or a multipart upload. For more information, see Post an Attachment.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

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

</details>

## add_comment

Adds a comment to a discussion. 
Creating a Comment without an Attachment 
Creating a Comment with an Attachment

<details><summary>Parameters</summary>

#### discussionId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### $body

Comment object with the following attribute:
text,Request body should contain parts with the following names:
comment: JSON Comment object with the following attribute:text
file: (optional) file to attach to the new commentSee Multipart Uploads for more information on parts.

**Type:** object

</details>

## add_favorites

Adds one or more items to the user's list of favorite items. This operation supports both single-object and bulk semantics. For more information, see Optional Bulk Operations. If called with a single Favorite object, and that favorite already exists, error code 1129 is returned. If called with an array of Favorite objects, any objects specified in the array that are already marked as favorites are ignored and omitted from the response.

<details><summary>Parameters</summary>

#### $body

Favorite object or an array of Favorite objects, with the following attributes:
objectId
type

**Type:** object

#### allowPartialSuccess

If true, allows bulk operations to process even if one or more operations are invalid for some reason.

**Type:** boolean

</details>

## add_group_members

Adds one or more members to a group. If called with a single GroupMember object, and that group member already exists, error code 1129 is returned. If called with an array
of GroupMember objects, any users specified in the array that are already group members are ignored and omitted from the response.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

#### $body

A single GroupMember object or an array of GroupMember objects, limited to the following attribute:
email

**Type:** object

</details>

## add_image_to_cell

Uploads an image to the specified cell within a sheet.

<details><summary>Parameters</summary>

#### columnId (required)

**Type:** string

#### rowId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### $body

**Type:** object

#### altText

url-encoded alternate text for the image

**Type:** string

#### overrideValidation

You may use the query string parameter overrideValidation with a value of true to allow a cell value outside of the validation limits. You must specify strict with a value of false to bypass value type checking.

**Type:** boolean

</details>

## add_rows

Inserts one or more rows into the sheet specified in the URL. If you want to insert the rows in any position but the default, use location-specifier attributes.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

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

#### allowPartialSuccess

If true, allows bulk operations to process even if one or more operations are invalid for some reason.

**Type:** boolean

</details>

## add_user

Adds a user to the organization account.

<details><summary>Parameters</summary>

#### $body

User object with the following attributes:
admin (required)
email (required)
licensedSheetCreator (required)
firstName (optional)
lastName (optional)
groupAdmin (optional)
resourceViewer (optional)

**Type:** object

#### sendEmail

Indicate whether to send a welcome email.

**Type:** boolean

</details>

## attach_new_version

Uploads a new version of a file to a sheet or row. This operation can be performed using a simple upload or a multipart upload. For more information, see Post an Attachment.

<details><summary>Parameters</summary>

#### attachmentId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### $body

**Type:** object

</details>

## attach_url_to_comment

Attaches a URL to the comment. The URL can be any of the following:

<details><summary>Parameters</summary>

#### commentId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### $body

Attachment object limited to the following attributes:
attachmentSubType
attachmentType
description (applicable when attaching to sheet or row only)
name
url

**Type:** object

</details>

## attach_url_to_row

Attaches a URL to the row. The URL can be any of the following:

<details><summary>Parameters</summary>

#### rowId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### $body

Attachment object limited to the following attributes:
attachmentSubType
attachmentType
description (applicable when attaching to sheet or row only)
name
url

**Type:** object

</details>

## attach_url_to_sheet

Attaches a URL to the sheet. The URL can be any of the following:

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

Attachment object limited to the following attributes:
attachmentSubType
attachmentType
description (applicable when attaching to sheet or row only)
name
url

**Type:** object

</details>

## change_update_request

Changes the specified update request for the sheet.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### updateRequestId (required)

**Type:** string

#### $body

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

</details>

## copy_folder

Creates a copy of the specified folder.

<details><summary>Parameters</summary>

#### folderId (required)

**Type:** string

#### $body

ContainerDestination object

**Type:** object

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### skipRemap

comma-separated list of references to NOT re-map for the newly created folder.

**Type:** array

</details>

## copy_rows_to_another_sheet

Copies rows from the sheet specified in the URL to (the bottom of) another sheet.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

CopyOrMoveRowDirective object

**Type:** object

#### ignoreRowsNotFound

If set to true, specifying row Ids that do not exist within the source sheet does not cause an error response. If omitted or set to false, specifying row Ids that do not exist within the source sheet causes an error response (and no rows are copied).

**Type:** boolean

#### include

comma-separated list of row elements to copy in addition to the cell data

**Type:** array

</details>

## copy_sheet

Creates a copy of the specified sheet.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

ContainerDestination object

**Type:** object

#### exclude

a comma-separated list of elements to not include in the response.

**Type:** array

#### include

a comma-separated list of elements to include in the response.

**Type:** array

</details>

## copy_sight

Creates a copy of the specified Sight.

<details><summary>Parameters</summary>

#### sightId (required)

**Type:** string

#### $body

ContainerDestination object

**Type:** object

</details>

## copy_workspace

Creates a copy of the specified workspace.

<details><summary>Parameters</summary>

#### workspaceId (required)

**Type:** string

#### $body

ContainerDestination object, limited to the following attribute:
newName (string) - required

**Type:** object

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### skipRemap

comma-separated list of references to NOT re-map for the newly created workspace.

**Type:** array

</details>

## create_cross_sheet_references

Adds a cross-sheet reference between two sheets and defines the data range for formulas. Each distinct data range requires a new cross-sheet reference.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

CrossSheetReference object with the following attributes:
sourceSheetId: sheetId for data source
Either two or all of the following:endColumnId: Defines ending edge of range when specifying one or more columns. Must be used with startColumnId.endRowId: Defines ending edge of range when specifying one or more rows. Must be used with startRowId.startColumnId: Defines beginning edge of range when specifying one or more columns. Must be used with endColumnId.startRowId: Defines beginning edge of range when specifying one or more rows. Must be used with endRowId.
name (optional): unique name for reference. If you omit this parameter, Smartsheet will autogenerate a name.

**Type:** object

</details>

## create_discussion_on_row

Creates a new discussion on a row. 
Creating a Discussion without an Attachment 
Creating a Discussion with an Attachment

<details><summary>Parameters</summary>

#### rowId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### $body

Discussion object with the following attribute:
comment (Comment object),Request body should contain parts with the following names:
discussion: JSON Discussion object with the following attributes:title (string), must be 100 characters in length or lesscomment (Comment object)
file: (optional) file to attach to the new commentSee Multipart Uploads for more information on parts.

**Type:** object

</details>

## create_discussion_on_sheet

Creates a new discussion on a sheet. 
Creating a Discussion without an Attachment 
Creating a Discussion with an Attachment

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

Discussion object with the following attribute:
comment (Comment object),Request body should contain parts with the following names:
discussion: JSON Discussion object with the following attributes:title (string), must be 100 characters in length or lesscomment (Comment object)
file: (optional) file to attach to the new commentSee Multipart Uploads for more information on parts.

**Type:** object

</details>

## create_folder_sheets_level

Creates a folder in the user's Sheets folder (Home).

<details><summary>Parameters</summary>

#### $body

Folder object, limited to the following attribute:
name (string) - required, does not have to be unique

**Type:** object

</details>

## create_folder_subfolder

Creates a folder in the specified folder.

<details><summary>Parameters</summary>

#### folderId (required)

**Type:** string

#### $body

Folder object, limited to the following attribute:
name (string) - required, does not have to be unique

**Type:** object

</details>

## create_folder_workspace

Creates a folder in the specified workspace.

<details><summary>Parameters</summary>

#### workspaceId (required)

**Type:** string

#### $body

Folder object, limited to the following attribute:
name (string) - required, does not have to be unique

**Type:** object

</details>

## create_group

Creates a new group.

<details><summary>Parameters</summary>

#### $body

Group object, limited to the following attributes:
name (required) -- must be unique within the organization account
description (optional)
members (optional) -- array of GroupMember objects, each limited to the following attribute:email

**Type:** object

</details>

## create_sheet_in_folder_from_template

Creates a sheet in the specified folder, from the specified template.

<details><summary>Parameters</summary>

#### folderId (required)

**Type:** string

#### $body

Sheet object, limited to the following attributes:
fromId (required) - the Id of the template from which to create the sheet
name (required) - does not have to be unique

**Type:** object

#### include

a comma-separated list of elements to include in the response.

**Type:** array

</details>

## create_sheet_in_quot_sheets_quot_folder_from_template

Creates a sheet in the user's Sheets folder (Home), from the specified template. For subfolders, use Create Sheet in Folder from Template.

<details><summary>Parameters</summary>

#### $body

Sheet object, limited to the following attributes:
fromId (required) - the Id of the template from which to create the sheet
name (required) - does not have to be unique

**Type:** object

#### include

a comma-separated list of elements to include in the response.

**Type:** array

</details>

## create_sheet_in_workspace_from_template

Creates a sheet at the top-level of the specified workspace, from the specified template. For subfolders, use Create Sheet in Folder from Template.

<details><summary>Parameters</summary>

#### workspaceId (required)

**Type:** string

#### $body

Sheet object, limited to the following attributes:
fromId (required) - the Id of the template from which to create the sheet
name (required) - does not have to be unique

**Type:** object

#### include

a comma-separated list of elements to include in the response.

**Type:** array

</details>

## create_update_request

Creates an update request for the specified rows within the sheet. An email notification (containing a link to the update request) is sent to the specified recipients according to the specified schedule.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

UpdateRequest object.

The UpdateRequest object in the request body must specify one or more of the following attributes:
rowIds: number[]
sendTo: Recipient[]
One or more of the followings:columnIds: number[]includeAttachments: trueincludeDiscussions: trueThe following attributes have the following values when not specified:
ccMe: false
message: Please update the following rows in my online sheet.
subject: Update Request: {Sheet Name}When the Schedule object is not specified, the request is sent to the recipients immediately.

**Type:** object

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## create_webhook

Creates a new webhook.

<details><summary>Parameters</summary>

#### $body

Webhook object, limited to the following attributes:
callbackUrl (required)
events (required)
name (required)
scope (required)
scopeObjectId (required)
version (required)

**Type:** object

</details>

## create_workspace

Creates a workspace.

<details><summary>Parameters</summary>

#### $body

Workspace object, limited to the following attribute:
name (string) - required

**Type:** object

</details>

## delete_all_versions

Deletes all versions of the attachment corresponding to the specified attachmentId. For attachments with multiple versions, this effectively deletes the attachment from the object that it’s attached to.

<details><summary>Parameters</summary>

#### attachmentId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## delete_alternate_email

Deletes the specified alternate email address for the specified user.

<details><summary>Parameters</summary>

#### alternateEmailId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## delete_an_automation_rule

Deletes an automation rule.

<details><summary>Parameters</summary>

#### automationRuleId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## delete_attachment

Deletes the attachment specified in the URL.

<details><summary>Parameters</summary>

#### attachmentId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## delete_column

Deletes the column specified in the URL.

<details><summary>Parameters</summary>

#### columnId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## delete_comment

Deletes the comment specified in the URL.

<details><summary>Parameters</summary>

#### commentId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## delete_discussion

Deletes the discussion specified in the URL.

<details><summary>Parameters</summary>

#### discussionId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## delete_folder

Deletes the folder (and its contents) specified in the URL.

<details><summary>Parameters</summary>

#### folderId (required)

**Type:** string

</details>

## delete_group

Deletes the group specified in the URL.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

</details>

## delete_report_share

Deletes the share specified in the URL.

<details><summary>Parameters</summary>

#### reportId (required)

**Type:** string

#### shareId (required)

**Type:** string

</details>

## delete_rows

Deletes one or more rows from the sheet specified in the URL.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### ids

**Type:** array

</details>

## delete_sent_update_request

Deletes the specified sent update request.

<details><summary>Parameters</summary>

#### sentUpdateRequestId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## delete_sheet

Deletes the sheet specified in the URL.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

</details>

## delete_sheet_share

Deletes the share specified in the URL.

<details><summary>Parameters</summary>

#### shareId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## delete_sight

Deletes the Sight specified in the URL.

<details><summary>Parameters</summary>

#### sightId (required)

**Type:** string

</details>

## delete_sight_share

Deletes the share specified in the URL.

<details><summary>Parameters</summary>

#### shareId (required)

**Type:** string

#### sightId (required)

**Type:** string

</details>

## delete_update_request

Terminates the future scheduled delivery of the update request specified in the URL.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### updateRequestId (required)

**Type:** string

</details>

## delete_webhook

Deletes the webhook specified in the URL.

<details><summary>Parameters</summary>

#### webhookId (required)

**Type:** string

</details>

## delete_workspace

Deletes the specified workspace (and its contents).

<details><summary>Parameters</summary>

#### workspaceid (required)

**Type:** string

</details>

## delete_workspace_share

Deletes the share specified in the URL.

<details><summary>Parameters</summary>

#### shareId (required)

**Type:** string

#### workspaceId (required)

**Type:** string

</details>

## edit_comment

Updates the text of a comment. NOTE: Only the user that created the comment is permitted to update it. Updating a Comment

<details><summary>Parameters</summary>

#### commentId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### $body

Comment object with the following attribute:
text

**Type:** object

</details>

## get_all_sent_update_requests

Gets a summarized list of all sent update requests on the sheet.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## get_all_update_requests

Gets a summarized list of all update requests that have future schedules associated with the specified sheet.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## get_alternate_email

Gets the specified alternate email.

<details><summary>Parameters</summary>

#### alternateEmailId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## get_an_automation_rule

Returns the specified automation rule, including any action values.

<details><summary>Parameters</summary>

#### automationRuleId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## get_attachment

Fetches a temporary URL that allows you to download an attachment. The urlExpiresInMillis attribute tells you how long the URL is valid.

<details><summary>Parameters</summary>

#### attachmentId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## get_cell_history

Gets the cell modification history.

<details><summary>Parameters</summary>

#### columnId (required)

**Type:** string

#### rowId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### includeAll

If true, includes all results.

**Type:** boolean

#### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

</details>

## get_column

Gets the column specified in the URL.

<details><summary>Parameters</summary>

#### columnId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

</details>

## get_comment

Gets the comment specified in the URL.

<details><summary>Parameters</summary>

#### commentId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## get_contact

Gets the specified contact.

<details><summary>Parameters</summary>

#### contactId (required)

**Type:** string

</details>

## get_cross_sheet_reference

Gets the cross-sheet reference specified in the URL.

<details><summary>Parameters</summary>

#### crossSheetReferenceId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## get_current_user

Gets the current user.

<details><summary>Parameters</summary>

#### include

comma-separated list of row elements to move in addition to the cell data

**Type:** array

</details>

## get_discussion

Gets the discussion specified in the URL.

<details><summary>Parameters</summary>

#### discussionId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## get_events

Gets events that are occurring in your Smartsheet organization account. Examples of events are creation, update, load, and delete of sheets, reports, dashboards, attachments, users, etc. Each event type has a distinct combination of objectType and action. Many event types have additional information returned under an additionalDetails object. See the Event Reporting reference documentation for a complete list of all currently supported events, including their respective objectType, action, and additionalDetails properties.

<details><summary>Parameters</summary>

#### Accept-Encoding

Strongly recommended to make sure payload is compressed.

**Type:** string

**Potential values:** deflate, gzip

#### maxCount

Maximum number of events to return as response to this call.

**Type:** number

#### numericDates

If true, dates are accepted and returned in Unix epoch time (milliseconds since midnight on January 1, 1970 in UTC time). Default is false, which means ISO-8601 format.

**Type:** boolean

#### since

Starting time for events to return. Intended for use only at client startup or recovery. This is intended for backfilling data and not for fine-grained date-based queries. Therefore, resolution is limited to the nearest hour. Interpreted as ISO-8601 format, unless numericDates is specified. You must pass in a value for either since or streamPosition and never both.

**Type:** string

#### streamPosition

Indicates next set of events to return. Use value of nextStreamPosition returned from the previous call. You must pass in a value for either since or streamPosition and never both.

**Type:** string

</details>

## get_folder

Gets the specified folder (and lists its contents).

<details><summary>Parameters</summary>

#### folderId (required)

**Type:** string

#### include

a comma-separated list of elements to include in the response.

**Type:** array

</details>

## get_group

Gets information about and an array of members for the group specified in the URL.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

</details>

## get_report

Gets the report, based on the report Id.

<details><summary>Parameters</summary>

#### reportId (required)

**Type:** string

#### Accept

If specified, gets the sheet in the format specified, based on the sheet Id.

**Type:** string

**Potential values:** application/vnd.ms-excel, text/csv

#### exclude

a comma-separated list of elements to not include in the response.

**Type:** array

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

</details>

## get_report_publish_status

Gets the Report's 'Publish' settings.

<details><summary>Parameters</summary>

#### reportId (required)

**Type:** string

</details>

## get_report_share

Gets the share specified in the URL.

<details><summary>Parameters</summary>

#### reportId (required)

**Type:** string

#### shareId (required)

**Type:** string

</details>

## get_row

Gets the row specified in the URL.

<details><summary>Parameters</summary>

#### rowId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### exclude

a comma-separated list of elements to not include in the response.

**Type:** array

#### include

a comma-separated list of elements to include in the response.

**Type:** array

</details>

## get_sent_update_request

Gets the specified sent update request on the sheet.

<details><summary>Parameters</summary>

#### sentUpdateRequestId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## get_server_info



*This operation has no parameters*

## get_sheet

Gets the sheet specified in the URL. Returns the sheet, including rows, and optionally populated with discussion and attachment objects.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### Accept

If specified, gets the sheet in the format specified, based on the sheet Id.

**Type:** string

**Potential values:** application/pdf, application/vnd.ms-excel, text/csv

#### columnIds

a comma-separated list of column Ids. The response contains only the specified columns in the "columns" array, and individual rows' "cells" array only contains cells in the specified columns.

**Type:** array

#### exclude

a comma-separated list of elements to not include in the response.

**Type:** array

#### filterId

overrides the existing include={filters} parameter if both are supplied. Applies the given filter (if accessible by the calling user) and marks the affected rows as "filteredOut"= true.

**Type:** string

#### ifVersionAfter

If version specified is still the current sheet version, then returns an abbreviated Sheet object with only the sheet version property. Otherwise, if the sheet has been modified, returns the complete Sheet object. Intended to allow clients with a cached copy to make sure they have the latest version.

**Type:** boolean

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

#### paperSize

applies to PDF only

**Type:** string

**Potential values:** LETTER, LEGAL, WIDE, ARCHD, A4, A3, A2, A1, A0

#### rowIds

a comma-separated list of row Ids on which to filter the rows included in the result

**Type:** array

#### rowNumbers

a comma-separated list of row numbers on which to filter the rows included in the result. Non-existent row numbers are ignored.

**Type:** array

</details>

## get_sheet_publish_status

Gets the sheet's 'Publish' settings.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

</details>

## get_sheet_share

Gets the share specified in the URL.

<details><summary>Parameters</summary>

#### shareId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## get_sheet_version

Gets the sheet version without loading the entire sheet. The following actions increment sheet version:

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

</details>

## get_sight

Gets the specified Sight.

<details><summary>Parameters</summary>

#### sightId (required)

**Type:** string

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

#### objectValue

when used in combination with a level query parameter, includes the email addresses for multi-contact data.

**Type:** boolean

</details>

## get_sight_publish_status

Gets the Sight 'publish' settings.

<details><summary>Parameters</summary>

#### sightId (required)

**Type:** string

</details>

## get_sight_share

Gets the share specified in the URL.

<details><summary>Parameters</summary>

#### shareId (required)

**Type:** string

#### sightId (required)

**Type:** string

</details>

## get_update_request

Gets the specified update request for the sheet that has a future schedule.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### updateRequestId (required)

**Type:** string

</details>

## get_user

Gets the user specified in the URL.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

</details>

## get_webhook

Gets the webhook specified in the URL.

<details><summary>Parameters</summary>

#### webhookId (required)

**Type:** string

</details>

## get_workspace

Gets the specified workspace (and lists its contents).

<details><summary>Parameters</summary>

#### workspaceid (required)

**Type:** string

#### include

when specified with a value of workspaceShares, response contains both item-level shares (scope=ITEM) and workspace-level shares (scope=WORKSPACE).

**Type:** array

#### loadAll

true or false, defaults to false

**Type:** boolean

</details>

## get_workspace_share

Gets the share specified in the URL.

<details><summary>Parameters</summary>

#### shareId (required)

**Type:** string

#### workspaceId (required)

**Type:** string

</details>

## import_sheet_from_csv_xlsx

Imports CSV or XLSX data into a new sheet in the top-level "sheets" folder.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### headerRowIndex

a zero-based integer indicating the row number to use for column names. Rows before this are omitted. If not specified, the default values are Column1, Column2, etc.

**Type:** integer

#### primaryColumnIndex

a zero-based integer indicating the column to designate as primary. If not specified, the default value is 0.

**Type:** integer

#### sheetName

desired name of the sheet.

**Type:** string

</details>

## import_sheet_into_folder

Imports CSV or XLSX data into a new sheet in the specified folder.

<details><summary>Parameters</summary>

#### folderId (required)

**Type:** string

#### $body

**Type:** object

#### headerRowIndex

a zero-based integer indicating the row number to use for column names. Rows before this are omitted. If not specified, the default values are Column1, Column2, etc.

**Type:** integer

#### primaryColumnIndex

a zero-based integer indicating the column to designate as primary. If not specified, the default value is 0.

**Type:** integer

#### sheetName

desired name of the sheet.

**Type:** string

</details>

## import_sheet_into_workspace

Imports CSV or XLSX data into a new sheet in the specified workspace.

<details><summary>Parameters</summary>

#### workspaceId (required)

**Type:** string

#### $body

**Type:** object

#### headerRowIndex

a zero-based integer indicating the row number to use for column names. Rows before this are omitted. If not specified, the default values are Column1, Column2, etc.

**Type:** integer

#### primaryColumnIndex

a zero-based integer indicating the column to designate as primary. If not specified, the default value is 0.

**Type:** integer

#### sheetName

desired name of the sheet.

**Type:** string

</details>

## list_all_automation_rules

Returns all automation rules associated with the specified sheet.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_alternate_emails

Gets a list of the alternate emails for the specified user.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_attachments

Gets a list of all attachments that are on the sheet, including sheet, row, and discussion-level attachments.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_columns

Gets a list of all columns belonging to the sheet specified in the URL.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_contacts

Gets a list of the user's Smartsheet contacts.

<details><summary>Parameters</summary>

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_contents

Gets a nested list of all Home objects, including folders, reports, sheets, Sights, templates, and workspaces, as shown on the "Home" tab.

<details><summary>Parameters</summary>

#### exclude

a comma-separated list of optional elements to not include in the response

**Type:** array

#### include

a comma-separated list of optional elements to include in the response

**Type:** array

</details>

## list_cross_sheet_references

Lists all cross-sheet references for the sheet.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_discussion_attachments

Gets a list of all attachments that are in the discussion.

<details><summary>Parameters</summary>

#### discussionId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_discussions

Gets a list of all discussions associated with the specified sheet. Remember that discussions are containers for the conversation thread. To see the entire thread, use the include=comments parameter.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_favorites

Gets a list of all of the user's favorite items.

<details><summary>Parameters</summary>

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_folders_sheet_level

Gets a list of the top-level child folders within the user's Sheets folder (Home).

<details><summary>Parameters</summary>

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_folders_subfolder

Gets a list of the top-level child folders within the specified folder.

<details><summary>Parameters</summary>

#### folderId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_folders_workspace

Gets a list of the top-level child folders within the specified workspace.

<details><summary>Parameters</summary>

#### workspaceId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_image_urls

Gets a list of URLs that can be used to retrieve the specified cell images. To retrieve images, see the workflow in Download Cell Image.

<details><summary>Parameters</summary>

#### $body

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

</details>

## list_org_groups

Gets a list of all groups in an organization account. To fetch the members of an individual group, use the Get Group operation.

<details><summary>Parameters</summary>

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_org_sheets

Gets a summarized list of all sheets owned by the members of the organization account.

<details><summary>Parameters</summary>

#### includeAll

If true, includes all results.

**Type:** boolean

#### modifiedSince

when specified with a date and time value, response only includes the objects that are modified on or after the date and time specified.

**Type:** string

</details>

## list_public_templates

Gets a list of public templates that the user has access to.

<details><summary>Parameters</summary>

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_report_shares

Gets a list of all users and groups to whom the specified report is shared, and their access level.

<details><summary>Parameters</summary>

#### reportId (required)

**Type:** string

#### include

when specified with a value of workspaceShares, response contains both item-level shares (scope=ITEM) and workspace-level shares (scope=WORKSPACE).

**Type:** array

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_reports

Gets a list of all reports that the user has access to in alphabetical order by name. The list contains an abbreviated Report object for each report.

<details><summary>Parameters</summary>

#### includeAll

If true, includes all results.

**Type:** boolean

#### modifiedSince

when specified with a date and time value, response only includes the objects that are modified on or after the date and time specified.

**Type:** string

</details>

## list_row_attachments

Gets a list of all attachments that are on the row, including row and discussion-level attachments.

<details><summary>Parameters</summary>

#### rowId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_row_discussions

Gets a list of all discussions associated with the specified row. Remember that discussions are containers for the conversation thread. To see the entire thread, use the include=comments parameter.

<details><summary>Parameters</summary>

#### rowId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_sheet_shares

Gets a list of all users and groups to whom the specified sheet is shared, and their access level.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### include

when specified with a value of workspaceShares, response contains both item-level shares (scope=ITEM) and workspace-level shares (scope=WORKSPACE).

**Type:** array

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_sheets

Gets a list of all sheets that the user has access to in alphabetical order by name. The list contains an abbreviated Sheet object for each sheet.

<details><summary>Parameters</summary>

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### includeAll

If true, includes all results.

**Type:** boolean

#### modifiedSince

when specified with a date and time value, response only includes the objects that are modified on or after the date and time specified.

**Type:** string

</details>

## list_sight_shares

Gets a list of all users and groups to whom the specified Sight is shared, and their access level.

<details><summary>Parameters</summary>

#### sightId (required)

**Type:** string

#### include

when specified with a value of workspaceShares, response contains both item-level shares (scope=ITEM) and workspace-level shares (scope=WORKSPACE).

**Type:** array

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_sights

Gets a list of all Sights that the user has access to.

<details><summary>Parameters</summary>

#### includeAll

If true, includes all results.

**Type:** boolean

#### modifiedSince

when specified with a date and time value, response only includes the objects that are modified on or after the date and time specified.

**Type:** string

</details>

## list_user_created_templates

Gets a list of user-created templates that the user has access to.

<details><summary>Parameters</summary>

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_users

Gets a list of users in the organization account. To filter by email, use the optional email query string parameter to specify a list of users' email addresses.

<details><summary>Parameters</summary>

#### email

Comma-separated list of email addresses on which to filter the results.

**Type:** array

#### include

when specified with a value of favoriteFlag, response indicates which returned items are favorites

**Type:** array

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_versions

Gets a list of all versions of the given attachmentId in order from newest to oldest.

<details><summary>Parameters</summary>

#### attachmentId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_webhooks

Gets the list of all webhooks that the user owns (if a user-generated token was used to make the request) 
or the list of all webhooks associated with the third-party app (if a third-party app made the request). 
Items in the response are ordered by API cient name &gt; webhook name &gt; creation date.

<details><summary>Parameters</summary>

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_workspace_shares

Gets a list of all users and groups to whom the specified workspace is shared, and their access level.

<details><summary>Parameters</summary>

#### workspaceId (required)

**Type:** string

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## list_workspaces

Gets a list of workspaces that the user has access to. The list contains an abbreviated Workspace object for each workspace.

<details><summary>Parameters</summary>

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### includeAll

If true, includes all results.

**Type:** boolean

</details>

## make_alternate_email_primary

Makes the specified alternate email address to become the primary email address for the specified user.

<details><summary>Parameters</summary>

#### alternateEmailId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## move_folder

Moves the specified folder to another location.

<details><summary>Parameters</summary>

#### folderId (required)

**Type:** string

#### $body

ContainerDestination object, limited to the following required attributes:
destinationId
destinationType

**Type:** object

</details>

## move_rows_to_another_sheet

Moves rows from the sheet specified in the URL to (the bottom of) another sheet.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

CopyOrMoveRowDirective object

**Type:** object

#### ignoreRowsNotFound

If set to true, specifying row Ids that do not exist within the source sheet does not cause an error response. If omitted or set to false, specifying row Ids that do not exist within the source sheet causes an error response (and no rows are moved).

**Type:** boolean

#### include

comma-separated list of row elements to move in addition to the cell data

**Type:** array

</details>

## move_sheet

Moves the specified sheet to a new location.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

ContainerDestination object, limited to the following required attributes:
destinationId
destinationType

**Type:** object

</details>

## move_sight

Moves the specified Sight to a new location.

<details><summary>Parameters</summary>

#### sightId (required)

**Type:** string

#### $body

ContainerDestination object, limited to the following required attributes:
destinationId
destinationType

**Type:** object

</details>

## refresh_access_token

Refreshes an access token, as part of the OAuth process. For more information, see OAuth Flow.

<details><summary>Parameters</summary>

#### client_id

client id for your app

**Type:** string

#### grant_type

must be set to "refresh_token"

**Type:** string

#### hash

SHA-256 hash of your app secret concatenated with a pipe and the refresh token value

**Type:** string

#### refresh_token

refresh_token value that came with the access token

**Type:** string

</details>

## remove_favorite_folder

Removes a single folder from the user's list of favorite items.

<details><summary>Parameters</summary>

#### folderId (required)

**Type:** string

#### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

</details>

## remove_favorite_report

Removes a single report from the user's list of favorite items.

<details><summary>Parameters</summary>

#### reportId (required)

**Type:** string

</details>

## remove_favorite_sheet

Removes a single sheet from the user's list of favorite items.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

</details>

## remove_favorite_sight

Removes a single Sight from the user's list of favorite items.

<details><summary>Parameters</summary>

#### sightId (required)

**Type:** string

</details>

## remove_favorite_template

Removes a single template from the user's list of favorite items.

<details><summary>Parameters</summary>

#### templateId (required)

**Type:** string

</details>

## remove_favorite_workspace

Removes a single workspace from the user's list of favorite items.

<details><summary>Parameters</summary>

#### workspaceId (required)

**Type:** string

</details>

## remove_group_member

Removes a member from a group.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

#### userId (required)

**Type:** string

</details>

## remove_multiple_favorite_folders



*This operation has no parameters*

## remove_multiple_favorite_reports

Removes multiple reports from the user's list of favorite items.

<details><summary>Parameters</summary>

#### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

</details>

## remove_multiple_favorite_sheets

Removes multiple sheets from the user's list of favorite items.

<details><summary>Parameters</summary>

#### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

</details>

## remove_multiple_favorite_sights

Removes multiple Sights from the user's list of favorite items.

<details><summary>Parameters</summary>

#### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

</details>

## remove_multiple_favorite_templates

Removes multiple templates from the user's list of favorite items.

<details><summary>Parameters</summary>

#### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

</details>

## remove_multiple_favorite_workspaces

Removes multiple workspaces from the user's list of favorite items.

<details><summary>Parameters</summary>

#### objectIds (required)

a comma-separated list of object Ids representing the items to remove from favorites

**Type:** array

</details>

## remove_user

Removes a user from an organization account. User is transitioned to a free collaborator with read-only access to owned reports, sheets, Sights, workspaces, and any shared templates (unless those are optionally transferred to another user).

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### removeFromSharing

Set to true to remove the user from sharing for all sheets/workspaces in the organization account. If not specified, user is not removed from sharing.

**Type:** boolean

#### transferSheets

If true, and transferTo is specified, the removed user's sheets are transferred. Else, sheets are not transferred. Defaults to false.

**Type:** boolean

#### transferTo

The Id of the user to transfer ownership to. If the user being removed owns groups, they are transferred to this user. If the user owns sheets, and transferSheets is true, the removed user's sheets are transferred to this user.

**Type:** string

</details>

## reset_shared_secret

Resets the shared secret for the specified webhook. For more information about how a shared secret is used, see Authenticating Callbacks. This operation can be used to rotate an API client's webhooks' shared secrets at periodic intervals to provide additional security.

<details><summary>Parameters</summary>

#### webhookId (required)

**Type:** string

</details>

## revoke_access_token

Revokes the access token used to make this request. The access token is no longer valid, and subsequent API calls made using the token fail.

<details><summary>Parameters</summary>

#### deleteAllForApiClient

The client Id and user Id is fetched based on the token that is used to make this API call. A value of true deletes all tokens associated to the given client Id and user Id. Defaults to false.

**Type:** boolean

</details>

## search_everything

Searches all sheets that the user can access, for the specified text.

<details><summary>Parameters</summary>

#### include

when specified with a value of favoriteFlag, response indicates which returned items are favorites

**Type:** array

#### location

when specified with a value of personalWorkspace, limits the response to only those items in the user's workspaces.

**Type:** string

#### modifiedSince

when specified with a date and time value, response only includes the objects that are modified on or after the date and time specified.

**Type:** string

#### query

text with which to perform the search. Enclose in double-quotes for an exact search.

**Type:** string

#### scopes

If search fails, try using an array for each type of this comma-separated list of search filters

**Type:** array

</details>

## search_sheet

Searches a sheet for the specified text.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### query

text with which to perform the search. Enclose in double-quotes for an exact search.

**Type:** string

</details>

## send_report

Sends the report as a PDF attachment via email to the designated recipients.

<details><summary>Parameters</summary>

#### reportId (required)

**Type:** string

#### $body

SheetEmail object

**Type:** object

</details>

## send_rows

Sends one or more rows via email.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

MultiRowEmail object. 

The columns included for each row in the email are populated according to the following rules:
If the columnIds attribute of the MultiRowEmail object is specified as an array of column Ids, those specific columns are included.
If the columnIds attribute of the MultiRowEmail object is omitted, all columns except hidden columns shall be included.
If the columnIds attribute of the MultiRowEmail object is specified as empty, no columns shall be included. (NOTE: In this case, either includeAttachments=true or includeDiscussions=true must be specified.)

**Type:** object

</details>

## send_sheet_via_email

Sends the sheet as a PDF attachment via email to the designated recipients.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

SheetEmail object

**Type:** object

</details>

## set_report_publish_status

Sets the publish status of the report and returns the new status, including the URL of any enabled publishing.

<details><summary>Parameters</summary>

#### reportId (required)

**Type:** string

#### $body

ReportPublish object

**Type:** object

</details>

## set_sheet_publish_status

Sets the publish status of the sheet and returns the new status, including the URLs of any enabled publishings.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

SheetPublish object

**Type:** object

</details>

## set_sight_publish_status

Publishes or unpublishes a Sight.

<details><summary>Parameters</summary>

#### sightId (required)

**Type:** string

#### $body

SightPublish object limited to the following attributes:
readOnlyFullEnabled (required)
readOnlyFullAccessibleBy (optional) - set to either ALL or ORG, when readOnlyFullEnabled=true.To publish the Sight, set readOnlyFullEnabled to true. To unpublish the Sight, set readOnlyFullEnabled to false.

**Type:** object

</details>

## share_report_2

Shares a report with the specified users and groups. If called with a single Share object, and that user or group share already exists, error code 1025 is returned. If called with an array of Share objects, and one or more user or group shares in the array already exist, they are ignored and omitted from the response.

<details><summary>Parameters</summary>

#### reportId (required)

**Type:** string

#### $body

Share object or an array of Share objects, with the following attributes:
accessLevel (required)
ccMe (optional): Boolean flag to indicate whether or not to CC the user sharing the sheet.
email (optional): the individual share recipient's email address
groupId (optional): the group share recipient's group Id
message (optional): The message in the body of the email that is optionally sent to the recipient.
subject (optional): The subject of the email that is optionally sent to notify the recipient.NOTE: One of email or groupId must be specified, but not both.

**Type:** object

#### sendEmail

Indicate whether to notify the user by email.

**Type:** boolean

</details>

## share_sheet

Shares a sheet with the specified users and groups. If called with a single Share object, and that user or group share already exists, error code 1025 is returned. If called with an array of Share objects, and one or more user or group shares in the array already exist, they are ignored and omitted from the response.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

Share object or an array of Share objects, with the following attributes:
accessLevel (required)
ccMe (optional): Boolean flag to indicate whether or not to CC the user sharing the sheet.
email (optional): the individual share recipient's email address
groupId (optional): the group share recipient's group Id
message (optional): The message in the body of the email that is optionally sent to the recipient.
subject (optional): The subject of the email that is optionally sent to notify the recipient.NOTE: One of email or groupId must be specified, but not both.

**Type:** object

#### sendEmail

Indicate whether to notify the user by email.

**Type:** boolean

</details>

## share_sight

Shares a Sight with the specified users and groups. If called with a single Share object, and that user or group share already exists, error code 1025 is returned. If called with an array of Share objects, and one or more user or group shares in the array already exist, they are ignored and omitted from the response.

<details><summary>Parameters</summary>

#### sightId (required)

**Type:** string

#### $body

Share object or an array of Share objects, with the following attributes:
accessLevel (required)
ccMe (optional): Boolean flag to indicate whether to CC the user sharing the sheet.
email (optional): the individual share recipient's email address
groupId (optional): the group share recipient's group Id
message (optional): The message in the body of the email that is optionally sent to the recipient.
subject (optional): The subject of the email that is optionally sent to notify the recipient.NOTE: One of email or groupId must be specified, but not both.

**Type:** object

#### sendEmail

Indicate whether to notify the user by email.

**Type:** boolean

</details>

## share_workspace

Shares a workspace with the specified users and groups. If called with a single Share object, and that user or group share already exists, error code 1025 is returned. If called with an array of Share objects, and one or more user or group shares in the array already exist, they are ignored and omitted from the response.

<details><summary>Parameters</summary>

#### workspaceId (required)

**Type:** string

#### $body

Share object or an array of Share objects, with the following attributes:
accessLevel (required)
ccMe (optional): Boolean that indicates whether to CC the user sharing the sheet.
email (optional): the individual share recipient's email address
groupId (optional): the group share recipient's group Id
message (optional): The message in the body of the email that is optionally sent to the recipient.
subject (optional): The subject of the email that is optionally sent to notify the recipient.NOTE: One of email or groupId must be specified, but not both.

**Type:** object

#### sendEmail

Indicate whether to notify the user by email.

**Type:** boolean

</details>

## sort_rows_in_sheet

Sorts the rows of a sheet, either in ascending or descending order.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

SortSpecifier with the following attribute:
sortCriteria -- SortCriterion array in priority order. Specifies sort order.

**Type:** object

#### columnIds

a comma-separated list of column Ids. The response contains only the specified columns in the "columns" array, and individual rows' "cells" array only contains cells in the specified columns.

**Type:** array

#### exclude

a comma-separated list of elements to not include in the response.

**Type:** array

#### filterId

overrides the existing include={filters} parameter if both are supplied. Applies the given filter (if accessible by the calling user) and marks the affected rows as "filteredOut"= true.

**Type:** string

#### ifVersionAfter

If version specified is still the current sheet version, then returns an abbreviated Sheet object with only the sheet version property. Otherwise, if the sheet has been modified, returns the complete Sheet object. Intended to allow clients with a cached copy to make sure they have the latest version.

**Type:** boolean

#### include

a comma-separated list of elements to include in the response.

**Type:** array

#### level

specifies whether multi-contact data is returned in a backwards-compatible, text format (level=0, default) or as multi-contact data (level=1).

**Type:** number

#### rowIds

a comma-separated list of row Ids on which to filter the rows included in the result

**Type:** array

#### rowNumbers

a comma-separated list of row numbers on which to filter the rows included in the result. Non-existent row numbers are ignored.

**Type:** array

</details>

## update_an_automation_rule

Updates an existing automation rule.

<details><summary>Parameters</summary>

#### automationRuleId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### $body

An AutomationRule object. When sending an AutomationRule, you must always specify action.type and it must match the existing rule type.

**Type:** object

</details>

## update_column

Updates properties of the column, moves the column, and/or renames the column. NOTES:

<details><summary>Parameters</summary>

#### columnId (required)

**Type:** string

#### sheetId (required)

**Type:** string

</details>

## update_folder

Updates the folder specified in the URL.

<details><summary>Parameters</summary>

#### folderId (required)

**Type:** string

#### $body

Folder object, limited to the following required attribute:
name (string)Name does not have to be unique.

**Type:** object

</details>

## update_group

Updates the Group specified in the URL.

<details><summary>Parameters</summary>

#### groupId (required)

**Type:** string

#### $body

Group object, limited to the following attributes:
description (optional)
name (optional) -- must be unique within the organization account
ownerId (optional): Id of an admin user to whom the group ownership is transferred

**Type:** object

</details>

## update_report_share

Updates the access level of a user or group for the specified report.

<details><summary>Parameters</summary>

#### reportId (required)

**Type:** string

#### shareId (required)

**Type:** string

#### $body

Share object limited to the following attribute:
accessLevel (string)

**Type:** object

</details>

## update_rows

Updates cell values in the specified rows, expands/collapses the specified rows, and/or modifies the position of specified rows (including indenting/outdenting). For detailed information about changing row positions, see location-specifier attributes.

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

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

#### allowPartialSuccess

If true, allows bulk operations to process even if one or more operations are invalid for some reason.

**Type:** boolean

#### overrideValidation

You may use the query string parameter overrideValidation with a value of true to allow a cell value outside of the validation limits. You must specify strict with a value of false to bypass value type checking.

**Type:** boolean

</details>

## update_sheet

Updates the sheet specified in the URL. To modify sheet contents, see Add Rows, Update Rows, Add Columns, and Update Column. This operation can be used to update an individual user's sheet settings.  If the request body contains only the userSettings attribute, this operation may be performed even if the user
only has read-only access to the sheet (for example, the user has viewer permissions or the sheet is read-only).

<details><summary>Parameters</summary>

#### sheetId (required)

**Type:** string

#### $body

Sheet object limited to the following attributes:
name (optional)
projectSettings (optional): ProjectSettings object, containing at least one of the projectSettings attributes, for updating this sheet's project settings and dependencies.
userSettings (optional): SheetUserSettings object for updating these user's settings for the sheetNOTE:
Attributes not specified in projectSettings are not updated.
If projectSettings.nonWorkingDays is specified as an empty array, all non-working days are removed from the project sheet.

**Type:** object

</details>

## update_sheet_share

Updates the access level of a user or group for the specified sheet.

<details><summary>Parameters</summary>

#### shareId (required)

**Type:** string

#### sheetId (required)

**Type:** string

#### $body

Share object limited to the following attribute:
accessLevel (string)

**Type:** object

</details>

## update_sight

Updates (renames) the specified Sight.

<details><summary>Parameters</summary>

#### sightId (required)

**Type:** string

#### $body

Sight object limited to the following attribute:
name (string)

**Type:** object

</details>

## update_sight_share

Updates the access level of a user or group for the specified Sight.

<details><summary>Parameters</summary>

#### shareId (required)

**Type:** string

#### sightId (required)

**Type:** string

#### $body

Share object limited to the following attribute:
accessLevel (string)

**Type:** object

</details>

## update_user

Updates the user specified in the URL.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### $body

User object containing at least one of the following attributes:
admin (required)
licensedSheetCreator (required)
firstName (optional)
groupAdmin (optional)
lastName (optional)
resourceViewer (optional)

**Type:** object

</details>

## update_user_profile_image

Uploads an image to the user profile.

<details><summary>Parameters</summary>

#### userId (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_webhook

Updates the webhook specified in the URL.

<details><summary>Parameters</summary>

#### webhookId (required)

**Type:** string

#### $body

Webhook object, limited to the following attributes:
callbackUrl (optional)
enabled (optional)
events (optional)
name (optional)
version (optional)

**Type:** object

</details>

## update_workspace

Updates the workspace specified in the URL.

<details><summary>Parameters</summary>

#### workspaceid (required)

**Type:** string

#### $body

Workspace object limited to the following attribute:
name (string)

**Type:** object

</details>

## update_workspace_share

Updates the access level of a user or group for the specified workspace.

<details><summary>Parameters</summary>

#### shareId (required)

**Type:** string

#### workspaceId (required)

**Type:** string

#### $body

Share object limited to the following attribute:
accessLevel (string)

**Type:** object

</details>

