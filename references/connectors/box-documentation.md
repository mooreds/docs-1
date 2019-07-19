---
id: box-documentation
title: Box (version v1.*.*)
sidebar_label: Box
layout: docs.mustache
---

## add_email_alias

Adds a new email alias to the given user’s account.

<details><summary>Parameters</summary>

#### USER_ID (required)

**Type:** string

#### $body

**Type:** object

</details>

## copy_file

Used to create a copy of a file in another folder. The original version of the file will not be altered.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### $body

**Type:** object

</details>

## copy_folder

Used to create a copy of a folder in another folder. The original version of the folder will not be altered.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## create_collaboration

Used to add a collaboration for a single user or a single group to a folder. Either an email address, a user ID, or a group id can be used to create the collaboration. If the collaboration is being created with a group, access to this endpoint is granted based on the group's invitability_level.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_comment

Used to add a comment by the user to a specific file or comment (i.e. as a reply comment).

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response.

**Type:** string

</details>

## create_file_metadata

Used to create the metadata template instance for a corresponding Box file. When creating metadata, only values that adhere to the metadata template schema will be accepted.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### SCOPE (required)

**Type:** string

#### TEMPLATE (required)

**Type:** string

#### $body

Metadata can be used for many purposes. Enterprises may want to have a better way to organize their digital assets for their marketing teams or developers may want to provide advanced content functionality such as facilitating workflows or approvals. Metadata is also visible in the Box Web Application. To learn more, please visit the help documentation.
Templates
Metadata that belongs to a file/folder is grouped by templates. Templates allow the metadata service to provide a multitude of services, such as pre-defining sets of key:value pairs or schema enforcement on specific fields. For example, a marketingCollateral template may define where and when specific marketing content should be used. You can also see the representation of the template in the Box web application while navigating to a file preview. Currently, metadata associated with folders does not show in the web application.
Each file/folder can have multiple distinct template instances associated with it, such as a marketingCollateral and retentionPolicy template instances. Template instances are also grouped by scopes. Currently, the only scopes support are enterprise and global. Enterprise scopes are defined on a per enterprises basis, whereas global scopes are Box application-wide. Attribute order within template instances is not guaranteed.
Currently, there are four attributes supported by templates: string, enum, float, and  date (RFC 3339).

Global Properties Template
In addition to enterprise scoped templates, every file on Box has access to the global properties template. The Properties template is a bucket of free form key:value string pairs, with no additional schema associated with it. Properties are ideal for scenarios where applications want to write metadata to file objects in a flexible way, without pre-defined template structure.
Properties follow all the conventions of standard templates, except for being located at a different endpoint. All requests made to the properties template must be made to /files/{file_id}/metadata/global/properties.

**Type:** object

</details>

## create_folder

Used to create a new empty folder. The new folder will be created inside of the specified parent folder

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## create_folder_metadata

Used to create the metadata template instance for a corresponding Box folder. When creating metadata, only values that adhere to the metadata template schema will be accepted.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### SCOPE (required)

**Type:** string

#### TEMPLATE (required)

**Type:** string

#### $body

Metadata can be used for many purposes. Enterprises may want to have a better way to organize their digital assets for their marketing teams or developers may want to provide advanced content functionality such as facilitating workflows or approvals. Metadata is also visible in the Box Web Application. To learn more, please visit the help documentation.
Templates
Metadata that belongs to a file/folder is grouped by templates. Templates allow the metadata service to provide a multitude of services, such as pre-defining sets of key:value pairs or schema enforcement on specific fields. For example, a marketingCollateral template may define where and when specific marketing content should be used. You can also see the representation of the template in the Box web application while navigating to a file preview. Currently, metadata associated with folders does not show in the web application.
Each file/folder can have multiple distinct template instances associated with it, such as a marketingCollateral and retentionPolicy template instances. Template instances are also grouped by scopes. Currently, the only scopes support are enterprise and global. Enterprise scopes are defined on a per enterprises basis, whereas global scopes are Box application-wide. Attribute order within template instances is not guaranteed.
Currently, there are four attributes supported by templates: string, enum, float, and  date (RFC 3339).

Global Properties Template
In addition to enterprise scoped templates, every file on Box has access to the global properties template. The Properties template is a bucket of free form key:value string pairs, with no additional schema associated with it. Properties are ideal for scenarios where applications want to write metadata to file objects in a flexible way, without pre-defined template structure.
Properties follow all the conventions of standard templates, except for being located at a different endpoint. All requests made to the properties template must be made to /files/{file_id}/metadata/global/properties.

**Type:** object

</details>

## create_group

Used to create a group.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## create_group_membership

Used to add a member to a Group.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## create_invite

Invites an existing user to join an Enterprise. The existing user can not be part of another Enterprise and must already have a Box account. Once invited, the user will receive an email and prompt to accept the invitation within the Box web application. This method requires the "Manage An Enterprise" scope for the enterprise, which can be enabled within your developer console.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## create_legal_hold_policy

Create a new Legal Hold Policy. Optional date filter may be passed. If Policy has a date filter, any Custodian assignments will apply only to file versions created or uploaded inside of the date range.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_legal_hold_policy_assignment

Create a new Assignment, which will apply the Legal Hold Policy to the target of the Assignment.

<details><summary>Parameters</summary>

#### $body

Request object to create a new Legal Policy Hold Assignment

**Type:** object

</details>

## create_metadata_template

Used to create a new metadata template with the specified schema.

<details><summary>Parameters</summary>

#### $body

Metadata that belongs to a file or folder is grouped by templates. Templates allow the metadata service to provide a multitude of services, such as pre-defining sets of key:value pairs or schema enforcement on specific fields.

**Type:** object

</details>

## create_retention_policy

Used to create a new retention policy.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_retention_policy_assignment

Returns a list of all retention policy assignments associated with a specified retention policy.

<details><summary>Parameters</summary>

#### $body

Request object to create a new Retention Policy Assignment

**Type:** object

</details>

## create_task

Used to create a single task for single user on a single file.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_task_assignment

Used to assign a task to a single user. There can be multiple assignments on a given task.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_user

Used to provision a new user in an enterprise. This method only works for enterprise admins.

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## create_web_link

Creates a web link object within a given folder.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_webhook

Create Webhook

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_collaboration

Used to delete a single collaboration.

<details><summary>Parameters</summary>

#### COLLAB_ID (required)

**Type:** string

</details>

## delete_comment

Permanently deletes a comment.

<details><summary>Parameters</summary>

#### COMMENT_ID (required)

**Type:** string

</details>

## delete_device_pin

Delete individual device pin.

<details><summary>Parameters</summary>

#### ID (required)

**Type:** string

</details>

## delete_file

Discards a file to the trash. The etag of the file can be included as an ‘If-Match’ header to prevent race conditions.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### If-Match

The etag of the file. This is in the ‘etag’ field of the file object.

**Type:** string

</details>

## delete_file_metadata

Used to delete the template instance. To delete custom key:value pairs within a template instance, you should refer to the updating metadata section.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### SCOPE (required)

**Type:** string

#### TEMPLATE (required)

**Type:** string

</details>

## delete_file_version

Discards a specific file version to the trash. (Depending on the enterprise settings for this user, the item will either be actually deleted from Box or moved to the trash.)

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### VERSION_ID (required)

**Type:** string

#### If-Match

The etag of the file. This is in the ‘etag’ field of the file object.

**Type:** string

</details>

## delete_file_watermark

Used to remove the watermark for a corresponding Box file.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

</details>

## delete_folder

Used to delete a folder. A recursive parameter must be included in order to delete folders that have items inside of them. An optional If-Match header can be included to ensure that client only deletes the folder if it knows about the latest version.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### If-Match

This is in the ‘etag’ field of the folder object.

**Type:** string

#### recursive

**Type:** boolean

</details>

## delete_folder_metadata

Used to delete the template instance. To delete custom key:value pairs within a template instance, you should refer to the updating metadata section.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### SCOPE (required)

**Type:** string

#### TEMPLATE (required)

**Type:** string

</details>

## delete_folder_watermark

Used to remove the watermark for a corresponding Box Folder.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

</details>

## delete_group

Permanently deletes a specific group.

<details><summary>Parameters</summary>

#### GROUP_ID (required)

**Type:** string

</details>

## delete_group_membership

Deletes a specific group membership.

<details><summary>Parameters</summary>

#### GROUP_MEMBERSHIP_ID (required)

**Type:** string

</details>

## delete_legal_hold_policy

Sends request to delete an existing Legal Hold Policy. Note that this is an asynchronous process - the Policy will not be fully deleted yet when the response comes back.

<details><summary>Parameters</summary>

#### ID (required)

**Type:** string

</details>

## delete_legal_hold_policy_assignment

Sends request to delete an existing Assignment. Note that this is an asynchronous process - the Assignment will not be fully deleted yet when the response comes back.

<details><summary>Parameters</summary>

#### ASSIGNMENT_ID (required)

**Type:** string

</details>

## delete_task

Permanently deletes a specific task.

<details><summary>Parameters</summary>

#### TASK_ID (required)

**Type:** string

</details>

## delete_task_assignment

Deletes a specific task assignment.

<details><summary>Parameters</summary>

#### TASK_ASSIGNMENT_ID (required)

**Type:** string

</details>

## delete_trashed_file

Permanently deletes an item that is in the trash. The item will no longer exist in Box. This action cannot be undone.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

</details>

## delete_trashed_folder

Permanently deletes an folder that is in the trash. The item will no longer exist in Box. This action cannot be undone.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

</details>

## delete_user

Deletes a user in an enterprise account.

<details><summary>Parameters</summary>

#### USER_ID (required)

**Type:** string

#### force

**Type:** boolean

#### notify

**Type:** boolean

</details>

## delete_user_email_alias

Removes an email alias from a user.

<details><summary>Parameters</summary>

#### EMAIL_ALIAS_ID (required)

**Type:** string

#### USER_ID (required)

**Type:** string

</details>

## delete_web_link

Deletes a web link and moves it to the trash

<details><summary>Parameters</summary>

#### WEB_LINK_ID (required)

**Type:** string

</details>

## delete_webhook

Permanently deletes a webhook

<details><summary>Parameters</summary>

#### WEBHOOK_ID (required)

**Type:** string

</details>

## get_all_file_metadata

Used to retrieve all metadata associated with a given file

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

</details>

## get_all_folder_metadata

Used to retrieve all metadata associated with a given folder

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

</details>

## get_collaboration

Used to get information about a single collaboration. All collaborations for a single folder can be retrieved through GET /folders/{id}/collaborations. A complete list of the user’s pending collaborations can also be retrieved.

<details><summary>Parameters</summary>

#### COLLAB_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

#### status

Can only be pending

**Type:** string

**Potential values:** pending

</details>

## get_collection_items

Retrieves the files and/or folders contained within this collection. Collection item lists behave a lot like getting a folder’s items.
Paginated results can be retrieved using the limit and offset parameters.
Sub-object fields can be requested via the ?fields parameter

<details><summary>Parameters</summary>

#### COLLECTION_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

#### limit

The maximum number of items to return in a page.

**Type:** integer

#### offset

The offset at which to begin the response. An offset of value of 0 will start at the beginning of the folder-listing. Offset of 2 would start at the 2nd record, not the second page. Note: If there are hidden items in your previous response, your next offset should be = offset + limit, not the # of records you received back.

**Type:** string

</details>

## get_collections



*This operation has no parameters*

## get_comment

Used to retrieve the message and metadata about a specific comment. Information about the user who created the comment is also included.

<details><summary>Parameters</summary>

#### COMMENT_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response.

**Type:** string

</details>

## get_current_user

Retrieves information about the user who is currently logged in i.e. the user for whom this auth token was generated.

<details><summary>Parameters</summary>

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_device_pin

Gets information about an individual device pin.

<details><summary>Parameters</summary>

#### ID (required)

**Type:** string

</details>

## get_email_aliases

Retrieves all email aliases for this user. The collection of email aliases does not include the primary login for the user; use GET /users/USER_ID to retrieve the login email address.

<details><summary>Parameters</summary>

#### USER_ID (required)

**Type:** string

</details>

## get_enterprise_device_pins

Gets all the device pins within a given enterprise. Must be an enterprise admin with the manage enterprise scope to make this call.

<details><summary>Parameters</summary>

#### ENTERPRISE_ID (required)

**Type:** string

#### direction

Default is "asc". Valid values are asc, desc. Case in-sensitive, ASC/DESC works just fine.

**Type:** string

#### limit

Default value is 100. Max value is 10000

**Type:** string

#### marker

Needs not be passed or can be empty for first invocation of the API. Use the one returned in response for each subsequent call.

**Type:** string

</details>

## get_enterprise_groups

Retrieves all of the groups for given enterprise. Must have permissions to see an enterprise's groups.

<details><summary>Parameters</summary>

#### fields

Attribute(s) to include in the response

**Type:** string

#### limit

The maximum number of items to return in a page. The default is 100 and the max is 1000.

**Type:** integer

#### offset

The item at which to begin the response.

**Type:** integer

</details>

## get_enterprise_metadata_templates

Used to retrieve all metadata templates within a user's enterprise. Currently only the enterprise scope is supported.

<details><summary>Parameters</summary>

#### SCOPE (required)

**Type:** string

</details>

## get_enterprise_users

Returns a list of all users for the Enterprise along with their user_id, public_name, and login.

<details><summary>Parameters</summary>

#### fields

Attribute(s) to include in the response

**Type:** string

#### filter_term

A string used to filter the results to only users starting with the filter_term in either the name or the login.

**Type:** string

#### limit

The number of records to return. The default is 100 and the max is 1000.

**Type:** integer

#### offset

The record at which to start. The default is 0.

**Type:** integer

#### user_type

The type of user to search for. Valid values are all, external or managed. If nothing is provided, the default behavior will be managed only

**Type:** string

**Potential values:** all, external, managed

</details>

## get_file

Used to retrieve the metadata about a file.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response.

**Type:** string

</details>

## get_file_collaborations

Use this to get a list of all the collaborations on a file

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

#### limit

The maximum number of items to return in a page

**Type:** integer

#### offset

The item at which to begin the response

**Type:** integer

</details>

## get_file_comments

Retrieves the comments on a particular file, if any exist.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_file_content

Retrieves the actual data of the file. An optional version parameter can be set to download a previous version of the file.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### BoxApi

The shared link for this item. Format should be shared_link=SHARED_LINK

**Type:** string

#### Range

The range value in bytes. Format should be bytes={start_range}-{end_range}

**Type:** string

#### version

The ID specific version of this file to download.

**Type:** string

</details>

## get_file_metadata

Used to retrieve the metadata template instance for a corresponding Box file.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### SCOPE (required)

**Type:** string

#### TEMPLATE (required)

**Type:** string

</details>

## get_file_tasks

Retrieves all of the tasks for given file.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_file_thumbnail

Retrieves a thumbnail, or smaller image representation, of this file. Sizes of 32x32,64x64, 128x128, and 256x256 can be returned in the .png format and sizes of 32x32, 94x94, 160x160, and 320x320 can be returned in the .jpg format. Thumbnails can be generated for the image and video file formats listed here.

<details><summary>Parameters</summary>

#### EXTENSION (required)

The preview format, e.g. png or jpg

**Type:** string

#### FILE_ID (required)

**Type:** string

#### max_height

The maximum height of the thumbnail

**Type:** integer

#### max_width

The maximum width of the thumbnail

**Type:** integer

#### min_height

The minimum height of the thumbnail

**Type:** integer

#### min_width

The minimum width of the thumbnail

**Type:** integer

</details>

## get_file_version_legal_hold_policies

Get list of non-deleted Holds for a single Policy.

<details><summary>Parameters</summary>

#### policy_id (required)

**Type:** string

</details>

## get_file_version_legal_hold_policy

Get details of a single File Version Legal Hold.

<details><summary>Parameters</summary>

#### ID (required)

**Type:** string

</details>

## get_file_version_retention

Used to retrieve information about a file version retention

<details><summary>Parameters</summary>

#### FILE_VERSION_RETENTION_ID (required)

**Type:** string

</details>

## get_file_version_retentions

Retrieves all file version retentions for the given enterprise.

<details><summary>Parameters</summary>

#### disposition_action

The disposition action of the retention policy. This action can be permanently_delete, which will cause the content retained by the policy to be permanently deleted, or remove_retention, which will lift the retention policy from the content, allowing it to be deleted by users, once the retention policy time period has passed.

**Type:** string

**Potential values:** permanently_delete, remove_retention

#### disposition_after

See content times for formatting

**Type:** string

#### disposition_before

See content times for formatting

**Type:** string

#### file_id

A file id to filter the file version retentions by.

**Type:** string

#### file_version_id

A file version id to filter the file version retentions by.

**Type:** string

#### limit

The maximum number of items to return in a page

**Type:** integer

#### marker

Base 64 encoded string that represents where the paging should being. It should be left blank to begin paging.

**Type:** string

#### policy_id

A policy id to filter the file version retentions by.

**Type:** string

</details>

## get_file_versions

If there are previous versions of this file, this method can be used to retrieve information about the older versions. (Versions are only tracked for Box users with premium accounts.)

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_file_watermark

Used to retrieve the watermark for a corresponding Box file.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

</details>

## get_folder

Retrieves the full metadata about a folder, including information about when it was last updated as well as the files and folders contained in it. The root folder of a Box account is always represented by the id “0”.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_folder_collaborations

Use this to get a list of all the collaborations on a folder i.e. all of the users that have access to that folder.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

#### limit

The maximum number of items to return in a page. The default is 100 and the max is 1000.

**Type:** integer

#### offset

The item at which to begin the response

**Type:** integer

</details>

## get_folder_items

Retrieves the files and/or folders contained within this folder without any other metadata about the folder. Any attribute in the full files or folders objects can be passed in with the fields parameter to get specific attributes, and only those specific attributes back; otherwise, the mini format is returned for each item by default. Multiple attributes can be passed in separated by commas e.g. fields=name,created_at. Paginated results can be retrieved using the limit and offset parameters.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

#### limit

The maximum number of items to return in a page. The default is 100 and the max is 1000.

**Type:** integer

#### offset

The offset at which to begin the response. An offset of value of 0 will start at the beginning of the folder-listing. Note: If there are hidden items in your previous response, your next offset should be = offset + limit, not the # of records you received back. The default is 0.

**Type:** string

</details>

## get_folder_metadata

Used to retrieve the metadata template instance for a corresponding Box folder.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### SCOPE (required)

**Type:** string

#### TEMPLATE (required)

**Type:** string

</details>

## get_folder_watermark

Used to retrieve the watermark for a corresponding Box folder.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

</details>

## get_group

Used to get information about a group.

<details><summary>Parameters</summary>

#### GROUP_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_group_collaborations

Retrieves all of the group collaborations for a given group. Note this is only available to group admins.

<details><summary>Parameters</summary>

#### GROUP_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

#### limit

The maximum number of items to return in a page. The default is 100 and the max is 1000.

**Type:** integer

#### offset

The item at which to begin the response.

**Type:** integer

</details>

## get_group_membership

Fetches a specific group membership entry.

<details><summary>Parameters</summary>

#### GROUP_MEMBERSHIP_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_group_memberships

Retrieves all of the members for a given group if the requesting user has access (see Group Object member_viewability_level).

<details><summary>Parameters</summary>

#### GROUP_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

#### limit

The maximum number of items to return in a page. The default is 100 and the max is 1000.

**Type:** integer

#### offset

The item at which to begin the response.

**Type:** integer

</details>

## get_invite



<details><summary>Parameters</summary>

#### INVITE_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_legal_hold_policies

Get a list of Legal Hold Policies that belong to your Enterprise.

<details><summary>Parameters</summary>

#### limit

Limit result size to this number. Defaults to 100, maximum is 1,000.

**Type:** integer

#### marker

Take from next_marker column of a prior call to get the next page

**Type:** string

#### policy_name

Case insensitive prefix-match filter on Policy name.

**Type:** string

</details>

## get_legal_hold_policy

Get details of a single Legal Hold Policy

<details><summary>Parameters</summary>

#### ID (required)

**Type:** string

</details>

## get_legal_hold_policy_assignment

Get details of a single assignment.

<details><summary>Parameters</summary>

#### ASSIGNMENT_ID (required)

**Type:** string

</details>

## get_legal_hold_policy_assignments

Get list of assignments for a single Policy.

<details><summary>Parameters</summary>

#### ID (required)

**Type:** string

</details>

## get_metadata_template

Used to retrieve the schema for a given metadata template.

<details><summary>Parameters</summary>

#### SCOPE (required)

**Type:** string

#### TEMPLATE (required)

**Type:** string

</details>

## get_pending_collaborations

Used to retrieve all pending collaboration invites for this user.

<details><summary>Parameters</summary>

#### status (required)

Must be 'pending'

**Type:** string

**Potential values:** pending

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_retention_policies

Retrieves all of the retention policies for the given enterprise.

<details><summary>Parameters</summary>

#### created_by_user_id

A user id to filter the retention policies by.

**Type:** string

#### policy_name

A name to filter the retention policies by. A trailing partial match search is performed.

**Type:** string

#### policy_type

A policy type to filter the retention policies by.

**Type:** string

**Potential values:** finite, indefinite

</details>

## get_retention_policy

Used to retrieve information about a retention policy

<details><summary>Parameters</summary>

#### POLICY_ID (required)

**Type:** string

</details>

## get_retention_policy_assignment

Used to retrieve information about a retention policy assignment.

<details><summary>Parameters</summary>

#### RETENTION_POLICY_ASSIGNMENT_ID (required)

**Type:** string

</details>

## get_retention_policy_assignments

Returns a list of all retention policy assignments associated with a specified retention policy.

<details><summary>Parameters</summary>

#### POLICY_ID (required)

**Type:** string

#### type

The type of the retention policy assignment to retrieve. Can either be folder or enterprise.

**Type:** string

**Potential values:** folder, enterprise

</details>

## get_shared_items

Shared items are any files or folders that are represented by a shared link. Shared items are different from other API resources in that a shared resource doesn’t necessarily have to be in the account of the user accessing it. The actual shared link itself is used along with a normal access token.
Used to retrieve the metadata about a shared item when only given a shared link. Because of varying permission for shared links, a password may be required to retrieve the shared item. Once the item has been retrieved, you can make API requests against the actual resource /files/{id} or /folders/{id} as long as the shared link and optional password are in the header.

<details><summary>Parameters</summary>

#### BoxApi (required)

The usage is 'BoxApi: shared_link=SHARED_LINK&amp;shared_link_password=SHARED_LINK_PASSWORD'

**Type:** string

</details>

## get_task

Fetches a specific task.

<details><summary>Parameters</summary>

#### TASK_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_task_assignment

Fetches a specific task assignment.

<details><summary>Parameters</summary>

#### TASK_ASSIGNMENT_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_task_assignments

Retrieves all of the assignments for a given task.

<details><summary>Parameters</summary>

#### TASK_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_trashed_file

Retrieves an item that has been moved to the trash.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

</details>

## get_trashed_folder

Retrieves an folder that has been moved to the trash.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_trashed_items

Retrieves the files and/or folders that have been moved to the trash. Any attribute in the full files or folders objects can be passed in with the fields parameter to get specific attributes, and only those specific attributes back; otherwise, the mini format is returned for each item by default. Multiple attributes can be passed in separated by commas e.g. fields=name,created_at. Paginated results can be retrieved using the limit and offset parameters.

<details><summary>Parameters</summary>

#### fields

Attribute(s) to include in the response

**Type:** string

#### limit

The maximum number of items to return

**Type:** integer

#### offset

The item at which to begin the response

**Type:** integer

</details>

## get_user

Retrieves information about a user in the enterprise. Requires enterprise administration authorization.

<details><summary>Parameters</summary>

#### USER_ID (required)

Either the unique user ID, or "me" for the currently authenticated user.

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_user_events

Use this to get events for a given user. A chunk of event objects is returned for the user based on the parameters passed in. Parameters indicating how many chunks are left as well as the next stream_position are also returned.

To retrieve Enterprise Events specify 'stream_type=admin_logs'. Retrieves up to a year' events for all users in an enterprise. Upper and lower bounds as well as filters can be applied to the results.

<details><summary>Parameters</summary>

#### created_after

A lower bound on the timestamp of the events returned

**Type:** date-time

#### created_before

An upper bound on the timestamp of the events returned

**Type:** date-time

#### event_type

A comma-separated list of events to filter by

**Type:** string

#### limit

Limits the number of events returned

**Type:** integer

#### stream_position

The location in the event stream at which you want to start receiving events. Can specify special case ‘now’ to get 0 events and the latest stream position for initialization.

**Type:** string

#### stream_type

Limits the type of events returned: all: returns everything, changes: returns tree changes, sync: returns tree changes only for sync folders

**Type:** string

**Potential values:** all, changes, sync, admin_logs

</details>

## get_user_group_membership

Retrieves all of the group memberships for a given user. Note this is only available to group admins. To retrieve group memberships for the user making the API request, use the users/me/memberships endpoint.

<details><summary>Parameters</summary>

#### USER_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

#### limit

Default is 100. Max is 1000

**Type:** integer

#### offset

The item at which to begin the response

**Type:** integer

</details>

## get_web_link

Use to get information about the web link.

<details><summary>Parameters</summary>

#### WEB_LINK_ID (required)

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## get_webhook

Get a Webhook

<details><summary>Parameters</summary>

#### WEBHOOK_ID (required)

**Type:** string

</details>

## get_webhooks

Returns all defined webhooks for the requesting application and user, up to the limit. If no limit is supplied then Box uses the default limit of 100.
If more than limit webhooks are defined then Box returns the webhooks in batches. When the results are batched, Box sends limit webhooks along with a next_marker field in the response object. The value of the next_marker field is a marker string that you can use in later requests to tell Box which batch to send next.
When you send a request that includes a marker string, Box sends the next batch of webhooks, beginning after the last webhook of the previous batch. When the response contains the last of the defined webhooks, Box omits the next_marker field from its response.
You can use limit and marker together with the marker string returned in the next_marker field to paginate lists of webhooks.

<details><summary>Parameters</summary>

#### limit

The maximum number of webhooks to return per page

**Type:** integer

#### marker

A marker string returned by Box if the result contains less than the full number of webhooks that are defined

**Type:** string

</details>

## promote_file_version

If there are previous versions of this file, this method can be used to promote one of the older versions to the top of the stack. This actually mints a copy of the old version and puts it on the top of the versions stack. The file will have the exact same contents, the same SHA1/etag, and the same name as the original. Other properties such as comments do not get updated to their former values.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### $body

**Type:** object

</details>

## restore_trashed_file

Restores an item that has been moved to the trash. Default behavior is to restore the item to the folder it was in before it was moved to the trash. If that parent folder no longer exists or if there is now an item with the same name in that parent folder, the new parent folder and/or new name will need to be included in the request.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### $body

**Type:** object

</details>

## restore_trashed_folder

Restores an item that has been moved to the trash. Default behavior is to restore the item to the folder it was in before it was moved to the trash. If that parent folder no longer exists or if there is now an item with the same name in that parent folder, the new parent folder and/or new name will need to be included in the request.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## search

The search endpoint provides a powerful way of finding items that are accessible by a single user or an entire enterprise. Leverage the parameters listed below to generate targeted advanced searches.

<details><summary>Parameters</summary>

#### query (required)

The string to search for; can be matched against item names, descriptions, text content of a file, and other fields of the different item types.

**Type:** string

#### ancestor_folder_ids

Limit searches to specific parent folders. Requires one or a set of comma delimited folder_ids: folder_id_1,folder_id_2,.... Parent folder results will also include items within subfolders.

**Type:** string

#### content_types

Limit searches to specific Box designated content types. Can be name, description, file_content, comments, or tags. Requires one or a set of comma delimited content_types: content_type_1,content_type_2,....

**Type:** string

#### created_at_range

The date for when the item was created. Specify the date range by using RFC3339 timestamp variables separated by a comma: from_date,to_date (e.g 2014-05-15T13:35:01-07:00,2014-05-17T13:35:01-07:00). Trailing from_date, and leading ,to_date commas are also accepted, where the current date and earliest known date will be designated respectively.

**Type:** date-time

#### file_extensions

Limit searches to specific file extensions like pdf,png,doc. Requires one or a set of comma delimited file extensions: file_extension_1,file_extension_2,....

**Type:** string

#### limit

Number of search results to return. The default is 30 and the max is 200.

**Type:** integer

#### mdfilters

Filters for a specific metadata template for files with metadata object associations. The filters are to be placed in a single JSON object. Please refer the MDFilters object in the definitions section of the swagger.json

**Type:** string

#### offset

The search result at which to start the response. The default is 0.

**Type:** integer

#### owner_user_ids

Search by item owners. Requires one or a set of comma delimited user_ids: user_id_1,user_id_2,...

**Type:** string

#### scope

The scope for which you want to limit your search to. Can be user_content for a search limited to only the current user or enterprise_content for the entire enterprise. To enable the enterprise_content scope for an administrator, please contact us.

**Type:** string

#### size_range

Filter by a file size range. Specify the file size range in bytes separated by a comma:lower_bound_size,upper_bound_size, where 1MB is equivalent to 1000000 bytes. Trailing lower_bound_size, and leading ,upper_bound_size commas are also accepted as parameters.

**Type:** integer

#### trash_content

Allows you to search within the trash. Can be trashed_only or non_trashed_only. Searches without this parameter default to non_trashed_only.

**Type:** string

#### type

The type you want to return in your search. Can be file, folder, or web_link.

**Type:** string

**Potential values:** file, folder, web_link

#### updated_at_range

The date for when the item was last updated. Specify the date range by using RFC3339 variables separated by a comma: from_date,to_date(e.g 2014-05-15T13:35:01-07:00,2014-05-17T13:35:01-07:00). Trailing from_date, and leading ,to_date commas are also accepted, where the current date and earliest known date will be designated respectively.

**Type:** date-time

</details>

## update_collaboation

Used to edit an existing collaboration. Descriptions of the various roles can be found here.

<details><summary>Parameters</summary>

#### COLLAB_ID (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_comment

Used to update the message of the comment.

<details><summary>Parameters</summary>

#### COMMENT_ID (required)

**Type:** string

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response.

**Type:** string

</details>

## update_file_info

Used to update individual or multiple fields in the file object, including renaming the file, changing its description, and creating a shared link for the file. To move a file, change the ID of its parent folder. An optional If-Match header can be included to prevent race conditions.

To lock and unlock files, you execute a PUT operation on the /files/{file id} endpoint and set or clear the lock properties on the file.

Used to create a shared link for this particular file. Please see here for more information on the permissions available for shared links. In order to get default shared link status, set it to an empty access level, i.e. {"shared_link": {}}. In order to disable a shared link, send this same type of PUT request with the value of shared_link set to null, i.e. {"shared_link": null}

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### $body

**Type:** object

#### If-Match

The etag of the file can be included as an ‘If-Match’ header to prevent race conditions.

**Type:** string

</details>

## update_file_metadata

Used to update the template instance. The request body must follow the JSON-Patch specification, which is represented as a JSON array of operation objects (see examples for more details). Updates can be either add, replace, remove , test, move, or copy. The template instance can only be updated if the template instance already exists. When editing metadata, only values that adhere to the metadata template schema will be accepted.
The update is applied atomically. If any errors occur during the application of the update operations, the metadata instance remains unchanged.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### SCOPE (required)

**Type:** string

#### TEMPLATE (required)

**Type:** string

#### $body

**Type:** array

</details>

## update_file_watermark

Used to apply or update the watermark for a corresponding Box file. The endpoint accepts a JSON body describing the watermark to apply.

<details><summary>Parameters</summary>

#### FILE_ID (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_folder

Used to update information about the folder. To move a folder, update the ID of its parent. To enable an email address that can be used to upload files to this folder, update the folder_upload_email attribute. An optional If-Match header can be included to ensure that client only updates the folder if it knows about the latest version.

Used to create a shared link for this particular folder. Please see here for more information on the permissions available for shared links. In order to get default shared link status, set it to an empty access level, i.e. {"shared_link": {}}. In order to disable a shared link, send this same type of PUT request with the value of shared_link set to null, i.e. {"shared_link": null}

To add or remove an item from a collection, you do a PUT on that item and change the list of collections it belongs to. Philosophically, this is similar to the way “move” operations work on files and folders: you do a PUT on the item and change its parent. It’s the same idea with collections, except you’re changing which collection(s) the item belongs to instead of the folder it belongs to. Currently the only collection available is the favorites collection, and you’ll need to know it’s ID for the user that is making the API call, since every user has a different favorites collection_id.
The Add/Remove API handling will check all ids passed in before performing any add/removal operations. If any collection ids are malformed or do not exist in the user’s account, the API call will throw a 400. Only if all of the collection ids are valid will the adds and removals be carried out.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### $body

**Type:** object

#### If-Match

This is in the ‘etag’ field of the folder object.

**Type:** string

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## update_folder_metadata

Used to update the template instance. Updates can be either add, replace, remove , or test. The template instance can only be updated if the template instance already exists. When editing metadata, only values that adhere to the metadata template schema will be accepted.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### SCOPE (required)

**Type:** string

#### TEMPLATE (required)

**Type:** string

#### $body

**Type:** array

</details>

## update_folder_watermark

Used to apply or update the watermark for a corresponding Box folder. The endpoints accepts a JSON body describing the watermark to apply.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_group

Updates a specific group.

<details><summary>Parameters</summary>

#### GROUP_ID (required)

**Type:** string

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## update_group_membership

Used to update a group membership.

<details><summary>Parameters</summary>

#### GROUP_MEMBERSHIP_ID (required)

**Type:** string

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## update_legal_hold_policy

Update existing Legal Hold Policy. Only name and description can be modified.

<details><summary>Parameters</summary>

#### ID (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_metadata_template

Used to update the schema of an existing template.

<details><summary>Parameters</summary>

#### SCOPE (required)

**Type:** string

#### TEMPLATE (required)

**Type:** string

#### $body

**Type:** array

</details>

## update_retention_policy

Used to update a retention policy.

<details><summary>Parameters</summary>

#### POLICY_ID (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_task

Updates a specific task.

<details><summary>Parameters</summary>

#### TASK_ID (required)

**Type:** string

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## update_task_assignment

Used to update a task assignment.

<details><summary>Parameters</summary>

#### TASK_ASSIGNMENT_ID (required)

**Type:** string

#### $body

**Type:** object

</details>

## update_user

Used to edit the settings and information about a user. This method only works for enterprise admins. To roll a user out of the enterprise (and convert them to a standalone free user), update the special enterprise attribute to be null.

Used to convert one of the user’s confirmed email aliases into the user’s primary login.

<details><summary>Parameters</summary>

#### USER_ID (required)

**Type:** string

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## update_user_folder

Moves all of the owned content from within one user’s folder into a new folder in another user’s account. You can move folders across users as long as the you have administrative permissions and the ‘source’ user owns the folders. To move everything from the root folder, use “0” which always represents the root folder of a Box account.

<details><summary>Parameters</summary>

#### FOLDER_ID (required)

**Type:** string

#### USER_ID (required)

**Type:** string

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

#### notify

**Type:** boolean

</details>

## update_web_link

Updates information for a web link.

<details><summary>Parameters</summary>

#### WEB_LINK_ID (required)

**Type:** string

#### $body

**Type:** object

#### fields

Attribute(s) to include in the response

**Type:** string

</details>

## update_webhook

Update a Webhook

<details><summary>Parameters</summary>

#### WEBHOOK_ID (required)

**Type:** string

#### $body

**Type:** object

</details>

