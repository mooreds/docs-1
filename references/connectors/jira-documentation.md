---
id: jira-documentation
title: Jira (version v1.*.*)
sidebar_label: Jira
layout: docs.mustache
---

## acknowledge_errors



*This operation has no parameters*

## add_actor_users

Adds an actor (user or group) to a project role.

<details><summary>Parameters</summary>

### id (required)

the project role id

**Type:** integer

### projectIdOrKey (required)

the project id or project key

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## add_attachment

Add one or more attachments to an issue.
 
 This resource expects a multipart post. The media-type multipart/form-data is defined in RFC 1867. Most client
 libraries have classes that make dealing with multipart posts simple. For instance, in Java the Apache HTTP Components
 library provides a
 MultiPartEntity
 that makes it simple to submit a multipart POST.
 
 In order to protect against XSRF attacks, because this method accepts multipart/form-data, it has XSRF protection
 on it.  This means you must submit a header of X-Atlassian-Token: no-check with the request, otherwise it will be
 blocked.
 
 The name of the multipart/form-data parameter that contains attachments must be "file"
 
 A simple example to upload a file called "myfile.txt" to issue REST-123:
 curl -D- -u admin:admin -X POST -H "X-Atlassian-Token: no-check" -F "file=@myfile.txt" http://myhost/rest/api/2/issue/TEST-123/attachments

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue that you want to add the attachments to

**Type:** string

</details>

## add_comment

Adds a new comment to an issue.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

a string containing the issue id or key the comment will be added to

**Type:** string

### $body

**Type:** object

```json
{ }
```

### expand

optional flags: renderedBody (provides body rendered in HTML)

**Type:** string

</details>

## add_field

Adds field to the given tab.

<details><summary>Parameters</summary>

### screenId (required)

id of screen

**Type:** integer

### tabId (required)

id of tab

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## add_field_to_default_screen

Adds field or custom field to the default tab

<details><summary>Parameters</summary>

### fieldId (required)

id of field / custom field

**Type:** string

</details>

## add_project_role_actors_to_role

Adds default actors to the given role. The request data should contain a list of usernames or a list of groups to add.

<details><summary>Parameters</summary>

### id (required)

the role id to remove the actors from

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## add_record

Store a record in Audit Log

<details><summary>Parameters</summary>

### $body

**Type:** string

</details>

## add_share_permission

Adds a share permissions to the given filter. Adding a global permission removes all previous permissions from the filter.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## add_tab

Creates tab for given screen

<details><summary>Parameters</summary>

### screenId (required)

id of screen

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## add_user_to_application

Add user to given application. Admin permission will be required to perform this operation.

<details><summary>Parameters</summary>

### applicationKey

application key

**Type:** string

### username

username

**Type:** string

</details>

## add_user_to_group

Adds given user to a group.
 
 Returns the current state of the group.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

### groupname

A name of requested group.

**Type:** string

</details>

## add_vote

Cast your vote in favour of an issue.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue to view voting information for

**Type:** string

</details>

## add_watcher

Adds a user to an issue's watcher list.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

a String containing an issue key.

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## add_worklog

Adds a new worklog entry to an issue.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

a string containing the issue id or key the worklog will be added to

**Type:** string

### $body

**Type:** string

### adjustEstimate

(optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are
                       
                       "new" - sets the estimate to a specific value
                       "leave"- leaves the estimate as is
                       "manual" - specify a specific amount to increase remaining estimate by
                       "auto"- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog 

**Type:** string

### newEstimate

(required when "new" is selected for adjustEstimate) the new value for the remaining estimate field. e.g. "2d"

**Type:** string

### reduceBy

(required when "manual" is selected for adjustEstimate) the amount to reduce the remaining estimate by e.g. "2d"

**Type:** string

</details>

## approve_upgrade



*This operation has no parameters*

## are_metrics_exposed



*This operation has no parameters*

## assign

Assigns an issue to a user.
 You can use this resource to assign issues when the user submitting the request has the assign permission but not the
 edit issue permission.
 If the name is "-1" automatic assignee is used.  A null name will remove the assignee.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

a String containing an issue key

**Type:** string

### $body

**Type:** string

</details>

## assign_permission_scheme

Assigns a permission scheme with a project.

<details><summary>Parameters</summary>

### projectKeyOrId (required)

key or id of the project

**Type:** string

### $body

**Type:** object

```json
{ }
```

### expand

**Type:** string

</details>

## can_move_sub_task



<details><summary>Parameters</summary>

### issueIdOrKey (required)

The parent issue's key or id

**Type:** string

</details>

## cancel_upgrade



*This operation has no parameters*

## change_my_password

Modify caller password.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## change_user_password

Modify user password.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

### key

user key

**Type:** string

### username

the username

**Type:** string

</details>

## convert_avatar_with_project_id

Converts temporary avatar into a real avatar

<details><summary>Parameters</summary>

### projectIdOrKey (required)

**Type:** string

### $body

**Type:** string

</details>

## create_avatar_for_user

Converts temporary avatar into a real avatar

<details><summary>Parameters</summary>

### $body

**Type:** string

### username

username

**Type:** string

</details>

## create_avatar_from_temporary

Converts temporary avatar into a real avatar

<details><summary>Parameters</summary>

### id (required)

the id of the issue type, which avatar is updated.

**Type:** string

### $body

**Type:** string

</details>

## create_avatar_with_type



<details><summary>Parameters</summary>

### owningObjectId (required)

**Type:** string

### type (required)

**Type:** string

### $body

**Type:** string

</details>

## create_component

Create a component via POST.

<details><summary>Parameters</summary>

### $body

**Type:** string

</details>

## create_custom_field

Creates a custom field using a definition (object encapsulating custom field data)

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_draft_for_parent

Create a draft for the passed scheme. The draft will be a copy of the state of the parent.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

</details>

## create_filter

Creates a new filter, and returns newly created filter.
 Currently sets permissions just using the users default sharing permissions

<details><summary>Parameters</summary>

### $body

**Type:** string

### expand

the parameters to expand

**Type:** string

</details>

## create_group

Creates a group by given group parameter
 
 Returns REST representation for the requested group.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_issue

Creates an issue or a sub-task from a JSON representation.
 
 The fields that can be set on create, in either the fields parameter or the update parameter can be determined
 using the /rest/api/2/issue/createmeta resource.
 If a field is not configured to appear on the create screen, then it will not be in the createmeta, and a field
 validation error will occur if it is submitted.
 
 Creating a sub-task is similar to creating a regular issue, with two important differences:
 
 the issueType field must correspond to a sub-task issue type (you can use
 /issue/createmeta to discover sub-task issue types), and
 you must provide a parent field in the issue create request containing the id or key of the
 parent issue.
 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_issue_link_type

Create a new issue link type.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_issue_type

Creates an issue type from a JSON representation and adds the issue newly created issue type to the default issue
 type scheme.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_issues

Creates issues or sub-tasks from a JSON representation.
 
 Creates many issues in one bulk operation.
 
 Creating a sub-task is similar to creating a regular issue. More details can be found in createIssue section:
 {@link IssueResource#createIssue(IssueUpdateBean)}}

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_or_update_remote_issue_link

Creates or updates a remote issue link from a JSON representation. If a globalId is provided and a remote issue link
 exists with that globalId, the remote issue link is updated. Otherwise, the remote issue link is created.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue to create the remote issue link for

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## create_or_update_remote_version_link

Create a remote version link via POST.  The link's global ID will be taken from the
 JSON payload if provided; otherwise, it will be generated.

<details><summary>Parameters</summary>

### versionId (required)

The version for which to delete ALL existing remote version links

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## create_permission_grant

Creates a permission grant in a permission scheme.

<details><summary>Parameters</summary>

### schemeId (required)

**Type:** integer

### $body

**Type:** object

```json
{ }
```

### expand

**Type:** string

</details>

## create_permission_scheme

Create a new permission scheme.
 This method can create schemes with a defined permission set, or without.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

### expand

**Type:** string

</details>

## create_project

Creates a new project.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_project_category

Create a project category via POST.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_project_role

Creates a new ProjectRole to be available in JIRA.
 The created role does not have any default actors assigned.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_property

Add a new property to a transition. Trying to add a property that already
 exists will fail.

<details><summary>Parameters</summary>

### id (required)

the ID of the transition within the workflow.

**Type:** integer

### $body

**Type:** object

```json
{ }
```

### key

the name of the property to add.

**Type:** string

### workflowMode

the type of workflow to use. Can either be "live" or "draft".

**Type:** string

### workflowName

the name of the workflow to use.

**Type:** string

</details>

## create_remote_version_link

Create a remote version link via POST.  The link's global ID will be taken from the
 JSON payload if provided; otherwise, it will be generated.

<details><summary>Parameters</summary>

### globalId (required)

The global ID of the remote link

**Type:** string

### versionId (required)

The version ID of the remote link

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## create_scheme

Create a new workflow scheme.
 
 The body contains a representation of the new scheme. Values not passed are assumed to be set to their defaults.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_user

Create user. By default created user will not be notified with email.
 If password field is not set then password will be randomly generated.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## create_version

Create a version via POST.

<details><summary>Parameters</summary>

### $body

**Type:** string

</details>

## current_user



*This operation has no parameters*

## default_columns

Returns the default columns for the given user. Admin permission will be required to get columns for a user
 other than the currently logged in user.

<details><summary>Parameters</summary>

### username

username

**Type:** string

</details>

## default_columns_for_filter

Returns the default columns for the given filter. Currently logged in user will be used as
 the user making such request.

<details><summary>Parameters</summary>

### id (required)

id of the filter

**Type:** integer

</details>

## delete_actor

Deletes actors (users or groups) from a project role.
 
 
 Delete a user from the role: /rest/api/2/project/{projectIdOrKey}/role/{roleId}?user={username}
 Delete a group from the role: /rest/api/2/project/{projectIdOrKey}/role/{roleId}?group={groupname}
 

<details><summary>Parameters</summary>

### id (required)

the project role id

**Type:** integer

### projectIdOrKey (required)

the project id or project key

**Type:** string

### group

the groupname to remove from the project role

**Type:** string

### user

the username to remove from the project role

**Type:** string

</details>

## delete_avatar_by_id

Deletes avatar

<details><summary>Parameters</summary>

### id (required)

database id for avatar

**Type:** integer

### username

username

**Type:** string

</details>

## delete_avatar_by_owner

Deletes avatar

<details><summary>Parameters</summary>

### id (required)

database id for avatar

**Type:** integer

### owningObjectId (required)

**Type:** string

### type (required)

Project id or project key

**Type:** string

</details>

## delete_avatar_for_project

Deletes avatar

<details><summary>Parameters</summary>

### id (required)

database id for avatar

**Type:** integer

### projectIdOrKey (required)

Project id or project key

**Type:** string

</details>

## delete_comment

Deletes an existing comment .

<details><summary>Parameters</summary>

### id (required)

the ID of the comment to request

**Type:** string

### issueIdOrKey (required)

of the issue the comment belongs to

**Type:** string

</details>

## delete_default

Remove the default workflow from the passed workflow scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### updateDraftIfNeeded

when true will create and return a draft when the workflow scheme cannot be edited
                            (e.g. when it is being used by a project).

**Type:** boolean

</details>

## delete_draft_by_id

Delete the passed draft workflow scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

</details>

## delete_draft_default

Remove the default workflow from the passed draft workflow scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

</details>

## delete_draft_issue_type

Remove the specified issue type mapping from the draft scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

### issueType (required)

the issue type being set.

**Type:** string

</details>

## delete_draft_workflow_mapping

Delete the passed workflow from the draft workflow scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

### workflowName

the name of the workflow to delete.

**Type:** string

</details>

## delete_filter

Delete a filter.

<details><summary>Parameters</summary>

### id (required)

the id of the filter being looked up

**Type:** integer

</details>

## delete_issue

Delete an issue.
 
 If the issue has subtasks you must set the parameter deleteSubtasks=true to delete the issue.
 You cannot delete an issue without its subtasks also being deleted.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue id or key to update (i.e. JRA-1330)

**Type:** string

### deleteSubtasks

a String of true or false indicating that any subtasks should also be deleted.  If the
                       issue has no subtasks this parameter is ignored.  If the issue has subtasks and this parameter is missing or false,
                       then the issue will not be deleted and an error will be returned.

**Type:** string

</details>

## delete_issue_link

Deletes an issue link with the specified id.
 To be able to delete an issue link you must be able to view both issues and must have the link issue permission
 for at least one of the issues.

<details><summary>Parameters</summary>

### linkId (required)

the issue link id.

**Type:** string

</details>

## delete_issue_link_type

Delete the specified issue link type.

<details><summary>Parameters</summary>

### issueLinkTypeId (required)

**Type:** string

</details>

## delete_issue_type

Remove the specified issue type mapping from the scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### issueType (required)

the issue type being set.

**Type:** string

### updateDraftIfNeeded

when true will create and return a draft when the workflow scheme cannot be edited
                            (e.g. when it is being used by a project).

**Type:** boolean

</details>

## delete_permission_scheme

Deletes a permission scheme identified by the given id.

<details><summary>Parameters</summary>

### schemeId (required)

**Type:** integer

</details>

## delete_permission_scheme_entity

Deletes a permission grant from a permission scheme.

<details><summary>Parameters</summary>

### permissionId (required)

**Type:** integer

### schemeId (required)

**Type:** integer

</details>

## delete_project

Deletes a project.

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project id or project key

**Type:** string

</details>

## delete_project_component

Delete a project component.

<details><summary>Parameters</summary>

### id (required)

The component to delete.

**Type:** string

### moveIssuesTo

The new component applied to issues whose 'id' component will be deleted.
                     If this value is null, then the 'id' component is simply removed from the related isues.

**Type:** string

</details>

## delete_project_role

Deletes a role. May return 403 in the future

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

### swap

if given, removes a role even if it is used in scheme by replacing the role with the given one

**Type:** integer

</details>

## delete_project_role_actors_from_role

Removes default actor from the given role.

<details><summary>Parameters</summary>

### id (required)

the role id to remove the actors from

**Type:** integer

### group

if given, removes an actor from given role

**Type:** string

### user

if given, removes an actor from given role

**Type:** string

</details>

## delete_project_version

Delete a project version.

<details><summary>Parameters</summary>

### id (required)

The version to delete

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## delete_project_version_by_id

Delete a project version.

<details><summary>Parameters</summary>

### id (required)

The version to delete

**Type:** string

### moveAffectedIssuesTo

The version to set affectedVersion to on issues where the deleted version is the affected version,
                             If null then the affectedVersion is removed.

**Type:** string

### moveFixIssuesTo

The version to set fixVersion to on issues where the deleted version is the fix version,
                             If null then the fixVersion is removed.

**Type:** string

</details>

## delete_property_by_id

Removes the property from the dashboard item identified by the key or by the id. Ths user removing the property is required
 to have permissions to administer the dashboard item.

<details><summary>Parameters</summary>

### dashboardId (required)

**Type:** string

### itemId (required)

the dashboard item from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## delete_property_from_comment

Removes the property from the comment identified by the key or by the id. Ths user removing the property is required
 to have permissions to administer the comment.

<details><summary>Parameters</summary>

### commentId (required)

the comment from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## delete_property_from_issue

Removes the property from the issue identified by the key or by the id. Ths user removing the property is required
 to have permissions to edit the issue.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## delete_property_from_issue_type

Removes the property from the issue type identified by the id. Ths user removing the property is required
 to have permissions to edit the issue type.

<details><summary>Parameters</summary>

### issueTypeId (required)

the issue type from which the property will be returned

**Type:** string

### propertyKey (required)

the key of the property to return

**Type:** string

</details>

## delete_property_from_project

Removes the property from the project identified by the key or by the id. Ths user removing the property is required
 to have permissions to administer the project.

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## delete_property_from_transition

Delete a property from the passed transition on the passed workflow. It is not an error to delete a property that
 does not exist.

<details><summary>Parameters</summary>

### id (required)

the ID of the transition within the workflow.

**Type:** integer

### key

the name of the property to add.

**Type:** string

### workflowMode

the type of workflow to use. Can either be "live" or "draft".

**Type:** string

### workflowName

the name of the workflow to use.

**Type:** string

</details>

## delete_property_from_user

Removes the property from the user identified by the key or by the id. Ths user removing the property is required
 to have permissions to administer the user.

<details><summary>Parameters</summary>

### propertyKey (required)

**Type:** string

### userKey

key of the user whose property is to be removed

**Type:** string

### username

username of the user whose property is to be removed

**Type:** string

</details>

## delete_remote_issue_link_by_global_id

Delete the remote issue link with the given global id on the issue.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue to create the remote issue link for

**Type:** string

### globalId

the global id of the remote issue link

**Type:** string

</details>

## delete_remote_issue_link_by_id

Delete the remote issue link with the given id on the issue.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue to create the remote issue link for

**Type:** string

### linkId (required)

the id of the remote issue link

**Type:** string

</details>

## delete_remote_version_link

Delete a specific remote version link with the given version ID and global ID.

<details><summary>Parameters</summary>

### globalId (required)

The global ID of the remote link

**Type:** string

### versionId (required)

The version ID of the remote link

**Type:** string

</details>

## delete_remote_version_links_by_version_id

Delete all remote version links for a given version ID.

<details><summary>Parameters</summary>

### versionId (required)

The version for which to delete ALL existing remote version links

**Type:** string

</details>

## delete_scheme

Delete the passed workflow scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

</details>

## delete_share_permission

Removes a share permissions from the given filter.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

### permission-id (required)

**Type:** integer

</details>

## delete_specific_issue_type

Deletes the specified issue type. If the issue type has any associated issues, these issues will be migrated to
 the alternative issue type specified in the parameter. You can determine the alternative issue types by calling
 the /rest/api/2/issuetype/{id}/alternatives resource.

<details><summary>Parameters</summary>

### id (required)

the id of the issue type to update.

**Type:** string

### alternativeIssueTypeId

the id of an issue type to which issues associated with the removed issue type will be migrated.

**Type:** string

</details>

## delete_tab

Deletes tab to give screen

<details><summary>Parameters</summary>

### screenId (required)

id of screen

**Type:** integer

### tabId (required)

id of tab

**Type:** integer

</details>

## delete_workflow_mapping

Delete the passed workflow from the workflow scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### updateDraftIfNeeded

flag to indicate if a draft should be created if necessary to delete the workflow
                            from the scheme.

**Type:** boolean

### workflowName

the name of the workflow to delete.

**Type:** string

</details>

## delete_worklog

Deletes an existing worklog entry.

<details><summary>Parameters</summary>

### id (required)

id of the worklog to be deleted

**Type:** string

### issueIdOrKey (required)

a string containing the issue id or key the worklog belongs to

**Type:** string

### adjustEstimate

(optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are
                       
                       "new" - sets the estimate to a specific value
                       "leave"- leaves the estimate as is
                       "manual" - specify a specific amount to increase remaining estimate by
                       "auto"- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog 

**Type:** string

### increaseBy

(required when "manual" is selected for adjustEstimate) the amount to increase the remaining estimate by e.g. "2d"

**Type:** string

### newEstimate

(required when "new" is selected for adjustEstimate) the new value for the remaining estimate field. e.g. "2d"

**Type:** string

</details>

## do_transition

Perform a transition on an issue.
 When performing the transition you can update or set other issue fields.
 
 The fields that can be set on transtion, in either the fields parameter or the update parameter can be determined
 using the /rest/api/2/issue/{issueIdOrKey}/transitions?expand=transitions.fields resource.
 If a field is not configured to appear on the transition screen, then it will not be in the transition metadata, and a field
 validation error will occur if it is submitted.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue whose transitions you want to view

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## edit_filter

Updates an existing filter, and returns its new value.

<details><summary>Parameters</summary>

### id (required)

the id of the filter being looked up

**Type:** integer

### $body

**Type:** string

### expand

the parameters to expand

**Type:** string

</details>

## edit_issue

Edits an issue from a JSON representation.
 
 The issue can either be updated by setting explicit the field value(s)
 or by using an operation to change the field value.
 
 The fields that can be updated, in either the fields parameter or the update parameter, can be determined
 using the /rest/api/2/issue/{issueIdOrKey}/editmeta resource.
 If a field is not configured to appear on the edit screen, then it will not be in the editmeta, and a field
 validation error will occur if it is submitted.
 
 Specifying a "field_id": field_value in the "fields" is a shorthand for a "set" operation in the "update" section.
 Field should appear either in "fields" or "update", not in both.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue id or key to update (i.e. JRA-1330)

**Type:** string

### $body

**Type:** object

```json
{ }
```

### notifyUsers

send the email with notification that the issue was updated to users that watch it.
                    Admin or project admin permissions are required to disable the notification.

**Type:** boolean

</details>

## expand_for_humans

Tries to expand an attachment. Output is human-readable and subject to change.

<details><summary>Parameters</summary>

### id (required)

the id of the attachment to expand.

**Type:** string

</details>

## expand_for_machines

Tries to expand an attachment. Output is raw and should be backwards-compatible through the course of time.

<details><summary>Parameters</summary>

### id (required)

the id of the attachment to expand.

**Type:** string

</details>

## find_assignable_users

Returns a list of users that match the search string. This resource cannot be accessed anonymously.
 Please note that this resource should be called with an issue key when a list of assignable users is retrieved
 for editing.  For create only a project key should be supplied.  The list of assignable users may be incorrect
 if it's called with the project key for editing.

<details><summary>Parameters</summary>

### actionDescriptorId

**Type:** integer

### issueKey

the issue key for the issue being edited we need to find assignable users for.

**Type:** string

### project

the key of the project we are finding assignable users for

**Type:** string

### username

the username

**Type:** string

</details>

## find_bulk_assignable_users

Returns a list of users that match the search string and can be assigned issues for all the given projects.
 This resource cannot be accessed anonymously.

<details><summary>Parameters</summary>

### projectKeys

the keys of the projects we are finding assignable users for, comma-separated

**Type:** string

### username

the username

**Type:** string

</details>

## find_groups

Returns groups with substrings matching a given query. This is mainly for use with
 the group picker, so the returned groups contain html to be used as picker suggestions.
 The groups are also wrapped in a single response object that also contains a header for
 use in the picker, specifically Showing X of Y matching groups.
 
 The number of groups returned is limited by the system property "jira.ajax.autocomplete.limit"
 
 The groups will be unique and sorted.

<details><summary>Parameters</summary>

### exclude

**Type:** string

### maxResults

**Type:** integer

### query

a String to match groups agains

**Type:** string

### userName

**Type:** string

</details>

## find_users

Returns a list of users that match the search string. This resource cannot be accessed anonymously.

<details><summary>Parameters</summary>

### includeActive

If true, then active users are included in the results (default true)

**Type:** boolean

### includeInactive

If true, then inactive users are included in the results (default false)

**Type:** boolean

### username

A query string used to search username, name or e-mail address

**Type:** string

</details>

## find_users_and_groups

Returns a list of users and groups matching query with highlighting. This resource cannot be accessed
 anonymously.

<details><summary>Parameters</summary>

### fieldId

The custom field id, if this request comes from a custom field, such as a user picker. Optional.

**Type:** string

### issueTypeId

The list of issue type ids to further restrict the search.
                    This parameter can occur multiple times to pass in multiple issue type ids.
                    Comma separated value is not supported.
                    Special values such as -1 (all standard issue types), -2 (all subtask issue types) are supported.
                    This parameter is only used when fieldId is present.

**Type:** string

### maxResults

the maximum number of users to return (defaults to 50). The maximum allowed value is 1000. If
                    you specify a value that is higher than this number, your search results will be truncated.

**Type:** integer

### projectId

The list of project ids to further restrict the search
                    This parameter can occur multiple times to pass in multiple project ids.
                    Comma separated value is not supported.
                    This parameter is only used when fieldId is present.

**Type:** string

### query

A string used to search username, Name or e-mail address

**Type:** string

### showAvatar

**Type:** boolean

</details>

## find_users_for_picker

Returns a list of users matching query with highlighting. This resource cannot be accessed anonymously.

<details><summary>Parameters</summary>

### exclude

**Type:** string

### maxResults

the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.
                   If you specify a value that is higher than this number, your search results will be truncated.

**Type:** integer

### query

A string used to search username, Name or e-mail address

**Type:** string

### showAvatar

**Type:** boolean

</details>

## find_users_with_all_permissions

Returns a list of active users that match the search string and have all specified permissions for the project or issue.
 This resource can be accessed by users with ADMINISTER_PROJECT permission for the project or global ADMIN or SYSADMIN rights.

<details><summary>Parameters</summary>

### issueKey

the issue key for the issue for which returned users have specified permissions.

**Type:** string

### permissions

comma separated list of permissions for project or issue returned users must have, see
                    Permissions
                    JavaDoc for the list of all possible permissions.

**Type:** string

### projectKey

the optional project key to search for users with if no issueKey is supplied.

**Type:** string

### username

the username filter, list includes all users if unspecified

**Type:** string

</details>

## find_users_with_browse_permission

Returns a list of active users that match the search string. This resource cannot be accessed anonymously 
 and requires the Browse Users global permission.
 Given an issue key this resource will provide a list of users that match the search string and have
 the browse issue permission for the issue provided.

<details><summary>Parameters</summary>

### issueKey

the issue key for the issue being edited we need to find viewable users for.

**Type:** string

### maxResults

the maximum number of users to return (defaults to 50). The maximum allowed value is 1000.
                   If you specify a value that is higher than this number, your search results will be truncated.

**Type:** integer

### projectKey

the optional project key to search for users with if no issueKey is supplied.

**Type:** string

### startAt

the index of the first user to return (0-based)

**Type:** integer

### username

the username filter, no users returned if left blank

**Type:** string

</details>

## fully_update_project_role

Fully updates a roles. Both name and description must be given.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## get

Returns the ApplicationRole with passed key if it exists.

<details><summary>Parameters</summary>

### key (required)

the key of the role to update.

**Type:** string

</details>

## get_accessible_project_type_by_key

Returns the project type with the given key, if it is accessible to the logged in user.
 This takes into account whether the user is licensed on the Application that defines the project type.

<details><summary>Parameters</summary>

### projectTypeKey (required)

**Type:** string

</details>

## get_advanced_settings



*This operation has no parameters*

## get_all



*This operation has no parameters*

## get_all_avatars

Returns all avatars which are visible for the currently logged in user.

<details><summary>Parameters</summary>

### username

username

**Type:** string

</details>

## get_all_avatars_grouped

Returns all avatars which are visible for the currently logged in user.  The avatars are grouped into
 system and custom.

<details><summary>Parameters</summary>

### projectIdOrKey (required)

project id or project key

**Type:** string

</details>

## get_all_fields

Gets all fields for a given tab

<details><summary>Parameters</summary>

### screenId (required)

id of screen

**Type:** integer

### tabId (required)

id of tab

**Type:** integer

### projectKey

the key of the project; this parameter is optional

**Type:** string

</details>

## get_all_permissions



*This operation has no parameters*

## get_all_project_categories



*This operation has no parameters*

## get_all_project_roles



*This operation has no parameters*

## get_all_project_types



*This operation has no parameters*

## get_all_projects

Returns all projects which are visible for the currently logged in user. If no user is logged in, it returns the
 list of projects that are visible when using anonymous access.

<details><summary>Parameters</summary>

### expand

the parameters to expand

**Type:** string

### recent

if this parameter is set then only projects recently accessed by the current user (if not logged in then based on HTTP session) will be returned (maximum count limited to the specified number but no more than 20).

**Type:** integer

</details>

## get_all_statuses

Get all issue types with valid status values for a project

<details><summary>Parameters</summary>

### projectIdOrKey (required)

Project id or project key

**Type:** string

</details>

## get_all_system_avatars

Returns all system avatars of the given type.

<details><summary>Parameters</summary>

### type (required)

the avatar type

**Type:** string

</details>

## get_all_tabs

Returns a list of all tabs for the given screen

<details><summary>Parameters</summary>

### screenId (required)

id of screen

**Type:** integer

### projectKey

the key of the project; this parameter is optional

**Type:** string

</details>

## get_all_workflows

Returns all workflows.

<details><summary>Parameters</summary>

### workflowName

**Type:** string

</details>

## get_alternative_issue_types

Returns a list of all alternative issue types for the given issue type id. The list will contain these issues types, to which
 issues assigned to the given issue type can be migrated. The suitable alternatives are issue types which are assigned
 to the same workflow, the same field configuration and the same screen scheme.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## get_application_property

Returns an application property.

<details><summary>Parameters</summary>

### key

a String containing the property key

**Type:** string

### keyFilter

when fetching a list allows the list to be filtered by the property's start of key
                        e.g. "jira.lf.*" whould fetch only those permissions that are editable and whose keys start with
                        "jira.lf.". This is a regex.

**Type:** string

### permissionLevel

when fetching a list specifies the permission level of all items in the list
                        see {@link com.atlassian.jira.bc.admin.ApplicationPropertiesService.EditPermissionLevel}

**Type:** string

</details>

## get_assigned_permission_scheme

Gets a permission scheme assigned with a project.

<details><summary>Parameters</summary>

### projectKeyOrId (required)

key or id of the project

**Type:** string

### expand

**Type:** string

</details>

## get_attachment

Returns the meta-data for an attachment, including the URI of the actual attached file.

<details><summary>Parameters</summary>

### id (required)

id of the attachment to remove

**Type:** string

</details>

## get_attachment_meta



*This operation has no parameters*

## get_auto_complete



*This operation has no parameters*

## get_available_metrics



*This operation has no parameters*

## get_avatars



<details><summary>Parameters</summary>

### owningObjectId (required)

**Type:** string

### type (required)

**Type:** string

</details>

## get_by_id

Returns the requested workflow scheme to the caller.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### returnDraftIfExists

when true indicates that a scheme's draft, if it exists, should be queried instead of
                            the scheme itself.

**Type:** boolean

</details>

## get_comment

Returns a single comment.

<details><summary>Parameters</summary>

### id (required)

the ID of the comment to request

**Type:** string

### issueIdOrKey (required)

of the issue the comment belongs to

**Type:** string

### expand

optional flags: renderedBody (provides body rendered in HTML)

**Type:** string

</details>

## get_comment_property

Returns the value of the property with a given key from the comment identified by the key or by the id. The user who retrieves
 the property is required to have permissions to read the comment.

<details><summary>Parameters</summary>

### commentId (required)

the comment from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## get_comments

Returns all comments for an issue.
 
 Results can be ordered by the "created" field which means the date a comment was added.
 

<details><summary>Parameters</summary>

### issueIdOrKey (required)

a string containing the issue id or key the comment will be added to

**Type:** string

### expand

optional flags: renderedBody (provides body rendered in HTML)

**Type:** string

### orderBy

ordering of the results.

**Type:** string

</details>

## get_component

Returns a project component.

<details><summary>Parameters</summary>

### id (required)

The component to delete.

**Type:** string

</details>

## get_component_related_issues

Returns counts of issues related to this component.

<details><summary>Parameters</summary>

### id (required)

a String containing the component id

**Type:** string

</details>

## get_configuration



*This operation has no parameters*

## get_create_issue_meta

Returns the meta data for creating issues. This includes the available projects, issue types and fields,
 including field types and whether or not those fields are required.
 Projects will not be returned if the user does not have permission to create issues in that project.
 
 The fields in the createmeta correspond to the fields in the create screen for the project/issuetype.
 Fields not in the screen will not be in the createmeta.
 
 Fields will only be returned if expand=projects.issuetypes.fields.
 
 The results can be filtered by project and/or issue type, given by the query params.

<details><summary>Parameters</summary>

### issuetypeIds

combinded with issuetypeNames, lists the issue types with which to filter the results. If null, all issue types are returned.
                       This parameter can be specified multiple times, and/or be a comma-separated list.
                       Specifiying an issue type that does not exist is not an error.

**Type:** string

### issuetypeNames

combinded with issuetypeIds, lists the issue types with which to filter the results. If null, all issue types are returned.
                       This parameter can be specified multiple times, but is NOT interpreted as a comma-separated list.
                       Specifiying an issue type that does not exist is not an error.

**Type:** string

### projectIds

combined with the projectKeys param, lists the projects with which to filter the results. If absent, all projects are returned.
                       This parameter can be specified multiple times, and/or be a comma-separated list.
                       Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results.

**Type:** string

### projectKeys

combined with the projectIds param, lists the projects with which to filter the results. If null, all projects are returned.
                       This parameter can be specified multiple times, and/or be a comma-separated list.
                       Specifiying a project that does not exist (or that you cannot create issues in) is not an error, but it will not be in the results.

**Type:** string

</details>

## get_custom_field_option

Returns a full representation of the Custom Field Option that has the given id.

<details><summary>Parameters</summary>

### id (required)

a String containing an Custom Field Option id

**Type:** string

</details>

## get_dashboard

Returns a single dashboard.

<details><summary>Parameters</summary>

### id (required)

the dashboard id

**Type:** string

</details>

## get_dashboard_item_property

Returns the value of the property with a given key from the dashboard item identified by the id.
 The user who retrieves the property is required to have permissions to read the dashboard item.

<details><summary>Parameters</summary>

### dashboardId (required)

**Type:** string

### itemId (required)

the dashboard item from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## get_default

Return the default workflow from the passed workflow scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### returnDraftIfExists

when true indicates that a scheme's draft, if it exists, should be queried instead of
                            the scheme itself.

**Type:** boolean

</details>

## get_default_share_scope



*This operation has no parameters*

## get_draft_by_id

Returns the requested draft workflow scheme to the caller.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

</details>

## get_draft_default

Return the default workflow from the passed draft workflow scheme to the caller.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

</details>

## get_draft_issue_type

Returns the issue type mapping for the passed draft workflow scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

### issueType (required)

the issue type being set.

**Type:** string

</details>

## get_draft_workflow

Returns the draft workflow mappings or requested mapping to the caller.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

### workflowName

the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name.

**Type:** string

</details>

## get_edit_issue_meta

Returns the meta data for editing an issue.
 
 The fields in the editmeta correspond to the fields in the edit screen for the issue.
 Fields not in the screen will not be in the editmeta.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue whose edit meta data you want to view

**Type:** string

</details>

## get_favourite_filters

Returns the favourite filters of the logged-in user.

<details><summary>Parameters</summary>

### enableSharedUsers

enable calculating shared users collection

**Type:** boolean

### expand

the parameters to expand

**Type:** string

</details>

## get_field_auto_complete_for_query_string

Returns auto complete suggestions for JQL search.

<details><summary>Parameters</summary>

### fieldName

the field name for which the suggestions are generated.

**Type:** string

### fieldValue

the portion of the field value that has already been provided by the user.

**Type:** string

### predicateName

the predicate for which the suggestions are generated. Suggestions are generated only for: "by", "from" and "to".

**Type:** string

### predicateValue

the portion of the predicate value that has already been provided by the user.

**Type:** string

</details>

## get_fields



*This operation has no parameters*

## get_fields_to_add

Gets available fields for screen. i.e ones that haven't already been added.

<details><summary>Parameters</summary>

### screenId (required)

id of screen

**Type:** integer

</details>

## get_filter

Returns a filter given an id

<details><summary>Parameters</summary>

### id (required)

the id of the filter being looked up

**Type:** integer

### enableSharedUsers

enable calculating shared users collection

**Type:** boolean

### expand

the parameters to expand

**Type:** string

</details>

## get_group

Returns REST representation for the requested group. Allows to get list of active users belonging to the
 specified group and its subgroups if "users" expand option is provided. You can page through users list by using
 indexes in expand param. For example to get users from index 10 to index 15 use "users[10:15]" expand value. This
 will return 6 users (if there are at least 16 users in this group). Indexes are 0-based and inclusive.
 
 This resource is deprecated, please use group/member API instead.

<details><summary>Parameters</summary>

### expand

List of fields to expand. Currently only available expand is "users".

**Type:** string

### groupname

A name of requested group.

**Type:** string

</details>

## get_ids_of_worklogs_deleted_since

Returns worklogs id and delete time of worklogs that was deleted since given time.
 The returns set of worklogs is limited to 1000 elements.
 This API will not return worklogs deleted during last minute.

<details><summary>Parameters</summary>

### since

a date time in unix timestamp format since when deleted worklogs will be returned.

**Type:** integer

</details>

## get_ids_of_worklogs_modified_since

Returns worklogs id and update time of worklogs that was updated since given time.
 The returns set of worklogs is limited to 1000 elements.
 This API will not return worklogs updated during last minute.

<details><summary>Parameters</summary>

### since

a date time in unix timestamp format since when updated worklogs will be returned.

**Type:** integer

</details>

## get_index_summary



*This operation has no parameters*

## get_issue

Returns a full representation of the issue for the given issue key.
 
 An issue JSON consists of the issue key, a collection of fields,
 a link to the workflow transition sub-resource, and (optionally) the HTML rendered values of any fields that support it
 (e.g. if wiki syntax is enabled for the description or comments).
 
 The fields param (which can be specified multiple times) gives a comma-separated list of fields
 to include in the response. This can be used to retrieve a subset of fields.
 A particular field can be excluded by prefixing it with a minus.
 
 By default, all (*all) fields are returned in this get-issue resource. Note: the default is different
 when doing a jql search -- the default there is just navigable fields (*navigable).
 
 *all - include all fields
 *navigable - include just navigable fields
 summary,comment - include just the summary and comments
 -comment - include everything except comments (the default is *all for get-issue)
 *all,-comment - include everything except comments
 
 
 The {@code properties} param is similar to {@code fields} and specifies a comma-separated list of issue
 properties to include. Unlike {@code fields}, properties are not included by default. To include them all
 send {@code ?properties=*all}. You can also include only specified properties or exclude some properties
 with a minus (-) sign.
 
 
 {@code *all} - include all properties
 {@code *all, -prop1} - include all properties except {@code prop1} 
 {@code prop1, prop1} - include {@code prop1} and {@code prop2} properties 
 
 
 
 JIRA will attempt to identify the issue by the issueIdOrKey path parameter. This can be an issue id,
 or an issue key. If the issue cannot be found via an exact match, JIRA will also look for the issue in a case-insensitive way, or
 by looking to see if the issue was moved. In either of these cases, the request will proceed as normal (a 302 or other redirect
 will not be returned). The issue key contained in the response will indicate the current value of issue's key.
 
 The expand param is used to include, hidden by default, parts of response. This can be used to include:
 
 renderedFields - field values in HTML format
 names - display name of each field
 schema - schema for each field which describes a type of the field
 transitions - all possible transitions for the given issue
 operations - all possibles operations which may be applied on issue
 editmeta - information about how each field may be edited. It contains field's schema as well.
 changelog - history of all changes of the given issue
 versionedRepresentations -
 REST representations of all fields. Some field may contain more recent versions. RESET representations are numbered.
 The greatest number always represents the most recent version. It is recommended that the most recent version is used.
 version for these fields which provide a more recent REST representation.
 After including versionedRepresentations "fields" field become hidden.
 

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue id or key to update (i.e. JRA-1330)

**Type:** string

### expand

**Type:** string

### fields

the list of fields to return for the issue. By default, all fields are returned.

**Type:** string

### properties

the list of properties to return for the issue. By default no properties are returned.

**Type:** string

</details>

## get_issue_all_types



*This operation has no parameters*

## get_issue_link

Returns an issue link with the specified id.

<details><summary>Parameters</summary>

### linkId (required)

the issue link id.

**Type:** string

</details>

## get_issue_link_type

Returns for a given issue link type id all information about this issue link type.

<details><summary>Parameters</summary>

### issueLinkTypeId (required)

**Type:** string

</details>

## get_issue_link_types



*This operation has no parameters*

## get_issue_navigator_default_columns



*This operation has no parameters*

## get_issue_picker_resource

Returns suggested issues which match the auto-completion query for the user which executes this request. This REST
 method will check the user's history and the user's browsing context and select this issues, which match the query.

<details><summary>Parameters</summary>

### currentIssueKey

the key of the issue in context of which the request is executed. The issue which is in context will not be included in the auto-completion result, even if it matches the query.

**Type:** string

### currentJQL

the JQL in context of which the request is executed. Only issues which match this JQL query will be included in results.

**Type:** string

### currentProjectId

the id of the project in context of which the request is executed. Suggested issues will be only from this project.

**Type:** string

### query

the query.

**Type:** string

### showSubTaskParent

if set to false and request is executed in context of a subtask, the parent issue will not be included in the auto-completion result, even if it matches the query.

**Type:** boolean

### showSubTasks

if set to false, subtasks will not be included in the list.

**Type:** boolean

</details>

## get_issue_property

Returns the value of the property with a given key from the issue identified by the key or by the id. The user who retrieves
 the property is required to have permissions to read the issue.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## get_issue_security_scheme_by_id

Returns the issue security scheme along with that are defined.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

</details>

## get_issue_security_scheme_by_project

Returns the issue security scheme for project.

<details><summary>Parameters</summary>

### projectKeyOrId (required)

**Type:** string

</details>

## get_issue_security_schemes



*This operation has no parameters*

## get_issue_type_by_id

Returns a full representation of the issue type that has the given id.

<details><summary>Parameters</summary>

### id (required)

the id of the issue type to update.

**Type:** string

</details>

## get_issue_type_for_workflow

Returns the issue type mapping for the passed workflow scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### issueType (required)

the issue type being set.

**Type:** string

### returnDraftIfExists

when true indicates that a scheme's draft, if it exists, should be queried instead of
                            the scheme itself.

**Type:** boolean

</details>

## get_issue_type_property

Returns the value of the property with a given key from the issue type identified by the id. The user who retrieves
 the property is required to have permissions to view the issue type.

<details><summary>Parameters</summary>

### issueTypeId (required)

the issue type from which the property will be returned

**Type:** string

### propertyKey (required)

the key of the property to return

**Type:** string

</details>

## get_issue_watchers

Returns the list of watchers for the issue with the given key.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

a String containing an issue key.

**Type:** string

</details>

## get_issue_worklog

Returns all work logs for an issue. 
 Note: Work logs won't be returned if the Log work field is hidden for the project.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

a string containing the issue id or key the worklog will be added to

**Type:** string

</details>

## get_issuesecuritylevel

Returns a full representation of the security level that has the given id.

<details><summary>Parameters</summary>

### id (required)

a String containing an issue security level id

**Type:** string

</details>

## get_logged_in_user



*This operation has no parameters*

## get_notification_scheme

Gets a notification scheme associated with the project.
 Follow the documentation of /notificationscheme/{id} resource for all details about returned value.

<details><summary>Parameters</summary>

### projectKeyOrId (required)

key or id of the project

**Type:** string

### expand

**Type:** string

</details>

## get_notification_scheme_by_id

Returns a full representation of the notification scheme for the given id. This resource will return a
 notification scheme containing a list of events and recipient configured to receive notifications for these events. Consumer
 should allow events without recipients to appear in response. User accessing
 the data is required to have permissions to administer at least one project associated with the requested notification scheme.
 
 Notification recipients can be:
 
 current assignee - the value of the notificationType is CurrentAssignee
 issue reporter - the value of the notificationType is Reporter
 current user - the value of the notificationType is CurrentUser
 project lead - the value of the notificationType is ProjectLead
 component lead - the value of the notificationType is ComponentLead
 all watchers - the value of the notification type is AllWatchers
 configured user - the value of the notification type is User. Parameter will contain key of the user. Information about the user will be provided
 if user expand parameter is used. 
 configured group - the value of the notification type is Group. Parameter will contain name of the group. Information about the group will be provided
 if group expand parameter is used. 
 configured email address - the value of the notification type is EmailAddress, additionally information about the email will be provided.
 users or users in groups in the configured custom fields - the value of the notification type is UserCustomField or GroupCustomField. Parameter
 will contain id of the custom field. Information about the field will be provided if field expand parameter is used. 
 configured project role - the value of the notification type is ProjectRole. Parameter will contain project role id. Information about the project role
 will be provided if projectRole expand parameter is used. 
 
 Please see the example for reference.
 
 The events can be JIRA system events or events configured by administrator. In case of the system events, data about theirs
 ids, names and descriptions is provided. In case of custom events, the template event is included as well.

<details><summary>Parameters</summary>

### id (required)

an id of the notification scheme to retrieve

**Type:** integer

### expand

**Type:** string

</details>

## get_notification_schemes

Returns a paginated list of notification schemes. In order to access notification scheme, the calling user is
 required to have permissions to administer at least one project associated with the requested notification scheme. Each scheme contains
 a list of events and recipient configured to receive notifications for these events. Consumer should allow events without recipients to appear in response.
 The list is ordered by the scheme's name.
 Follow the documentation of /notificationscheme/{id} resource for all details about returned value.

<details><summary>Parameters</summary>

### expand

**Type:** string

### maxResults

the maximum number of notification schemes to return (max 50).

**Type:** integer

### startAt

the index of the first notification scheme to return (0 based).

**Type:** integer

</details>

## get_password_policy

Returns the list of requirements for the current password policy. For example, "The password must have at least 10 characters.",
 "The password must not be similar to the user's name or email address.", etc.

<details><summary>Parameters</summary>

### hasOldPassword

whether or not the user will be required to enter their current password.  Use
                       {@code false} (the default) if this is a new user or if an administrator is forcibly changing
                       another user's password.

**Type:** boolean

</details>

## get_permission_scheme

Returns a permission scheme identified by the given id.

<details><summary>Parameters</summary>

### schemeId (required)

**Type:** integer

### expand

**Type:** string

</details>

## get_permission_scheme_grant

Returns a permission grant identified by the given id.

<details><summary>Parameters</summary>

### permissionId (required)

**Type:** integer

### schemeId (required)

**Type:** integer

### expand

**Type:** string

</details>

## get_permission_scheme_grants

Returns all permission grants of the given permission scheme.

<details><summary>Parameters</summary>

### schemeId (required)

**Type:** integer

### expand

**Type:** string

</details>

## get_permission_schemes

Returns a list of all permission schemes.
 
 By default only shortened beans are returned. If you want to include permissions of all the schemes,
 then specify the permissions expand parameter. Permissions will be included also if you specify
 any other expand parameter.
 

<details><summary>Parameters</summary>

### expand

**Type:** string

</details>

## get_permissions

Returns all permissions in the system and whether the currently logged in user has them. You can optionally provide a specific context to get permissions for
 (projectKey OR projectId OR issueKey OR issueId)
 
  When no context supplied the project related permissions will return true if the user has that permission in ANY project 
  If a project context is provided, project related permissions will return true if the user has the permissions in the specified project.
 For permissions that are determined using issue data (e.g Current Assignee), true will be returned if the user meets the permission criteria in ANY issue in that project 
  If an issue context is provided, it will return whether or not the user has each permission in that specific issue
 
 
 NB: The above means that for issue-level permissions (EDIT_ISSUE for example), hasPermission may be true when no context is provided, or when a project context is provided,
 but may be false for any given (or all) issues. This would occur (for example) if Reporters were given the EDIT_ISSUE permission. This is because
 any user could be a reporter, except in the context of a concrete issue, where the reporter is known.
 
 
 Global permissions will still be returned for all scopes.
 
 
 Prior to version 6.4 this service returned project permissions with keys corresponding to com.atlassian.jira.security.Permissions.Permission constants.
 Since 6.4 those keys are considered deprecated and this service returns system project permission keys corresponding to constants defined in com.atlassian.jira.permission.ProjectPermissions.
 Permissions with legacy keys are still also returned for backwards compatibility, they are marked with an attribute deprecatedKey=true.
 The attribute is missing for project permissions with the current keys.
 

<details><summary>Parameters</summary>

### issueId

- id of the issue to scope returned permissions for.

**Type:** string

### issueKey

- key of the issue to scope returned permissions for.

**Type:** string

### projectId

- id of project to scope returned permissions for.

**Type:** string

### projectKey

- key of project to scope returned permissions for.

**Type:** string

</details>

## get_preference

Returns preference of the currently logged in user. Preference key must be provided as input parameter (key). The
 value is returned exactly as it is. If key parameter is not provided or wrong - status code 404. If value is
 found  - status code 200.

<details><summary>Parameters</summary>

### key

- key of the preference to be returned.

**Type:** string

</details>

## get_priorities



*This operation has no parameters*

## get_priority

Returns an issue priority.

<details><summary>Parameters</summary>

### id (required)

a String containing the priority id

**Type:** string

</details>

## get_progress

Retrieves the progress of a single reindex request.

<details><summary>Parameters</summary>

### requestId (required)

the reindex request ID.

**Type:** integer

</details>

## get_progress_bulk

Retrieves the progress of a multiple reindex requests.  Only reindex requests that actually exist will be returned
 in the results.

<details><summary>Parameters</summary>

### requestId

the reindex request IDs.

**Type:** string

</details>

## get_project

Validates a project key.

<details><summary>Parameters</summary>

### key

the project key

**Type:** string

</details>

## get_project_by_id

Contains a full representation of a project in JSON format.
 
 All project keys associated with the project will only be returned if expand=projectKeys.
 

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project id or project key

**Type:** string

### expand

the parameters to expand

**Type:** string

</details>

## get_project_category_by_id

Contains a representation of a project category in JSON format.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

</details>

## get_project_components

Contains a full representation of a the specified project's components.

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project id or project key

**Type:** string

</details>

## get_project_property

Returns the value of the property with a given key from the project identified by the key or by the id. The user who retrieves
 the property is required to have permissions to read the project.

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## get_project_role

Returns the details for a given project role in a project.

<details><summary>Parameters</summary>

### id (required)

the project role id

**Type:** integer

### projectIdOrKey (required)

the project id or project key

**Type:** string

</details>

## get_project_role_actors_for_role

Gets default actors for the given role.

<details><summary>Parameters</summary>

### id (required)

the role id to remove the actors from

**Type:** integer

</details>

## get_project_roles

Returns all roles in the given project Id or key, with links to full details on each role.

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project id or project key

**Type:** string

</details>

## get_project_roles_by_id

Get a specific ProjectRole available in JIRA.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

</details>

## get_project_type_by_key

Returns the project type with the given key.

<details><summary>Parameters</summary>

### projectTypeKey (required)

**Type:** string

</details>

## get_project_versions

Contains a full representation of a the specified project's versions.

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project id or project key

**Type:** string

### expand

the parameters to expand

**Type:** string

</details>

## get_project_versions_paginated

Returns all versions for the specified project. Results are paginated.
 
 Results can be ordered by the following fields:
 
 sequence
 name
 startDate
 releaseDate
 
 

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project id or project key

**Type:** string

### expand

the parameters to expand

**Type:** string

### orderBy

ordering of the results.

**Type:** string

</details>

## get_properties

Return the property or properties associated with a transition.

<details><summary>Parameters</summary>

### id (required)

the ID of the transition within the workflow.

**Type:** integer

### includeReservedKeys

some keys under the "jira." prefix are editable, some are not. Set this to true
                            in order to include the non-editable keys in the response.

**Type:** boolean

### key

the name of the property key to query. Can be left off the query to return all properties.

**Type:** string

### workflowMode

the type of workflow to use. Can either be "live" or "draft".

**Type:** string

### workflowName

the name of the workflow to use.

**Type:** string

</details>

## get_properties_keys_for_comment

Returns the keys of all properties for the comment identified by the key or by the id.

<details><summary>Parameters</summary>

### commentId (required)

the comment from which keys will be returned.

**Type:** string

</details>

## get_properties_keys_for_dashboard_items

Returns the keys of all properties for the dashboard item identified by the id.

<details><summary>Parameters</summary>

### dashboardId (required)

**Type:** string

### itemId (required)

the dashboard item from which keys will be returned.

**Type:** string

</details>

## get_properties_keys_for_issues

Returns the keys of all properties for the issue identified by the key or by the id.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue from which keys will be returned.

**Type:** string

</details>

## get_properties_keys_for_project

Returns the keys of all properties for the project identified by the key or by the id.

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project from which keys will be returned.

**Type:** string

</details>

## get_properties_keys_for_user

Returns the keys of all properties for the user identified by the key or by the id.

<details><summary>Parameters</summary>

### userKey

key of the user whose properties are to be returned

**Type:** string

### username

username of the user whose properties are to be returned

**Type:** string

</details>

## get_property_keys_for_issue_type

Returns the keys of all properties for the issue type identified by the id.

<details><summary>Parameters</summary>

### issueTypeId (required)

the issue type from which the keys will be returned

**Type:** string

</details>

## get_records

Returns auditing records filtered using provided parameters

<details><summary>Parameters</summary>

### filter

- text query; each record that will be returned must contain the provided text in one of its fields

**Type:** string

### from

- timestamp in past; 'from' must be less or equal 'to', otherwise the result set will be empty
               only records that where created in the same moment or after the 'from' timestamp will be provided in response

**Type:** string

### limit

- maximum number of returned results (if is limit is &lt;= 0 or &gt; 1000, it will be set do default value: 1000)

**Type:** integer

### offset

- the number of record from which search starts

**Type:** integer

### projectIds

- list of project ids to look for

**Type:** string

### to

- timestamp in past; 'from' must be less or equal 'to', otherwise the result set will be empty
               only records that where created in the same moment or earlier than the 'to' timestamp will be provided in response

**Type:** string

### userIds

- list of user ids to look for

**Type:** string

</details>

## get_reindex_info

Returns information on the system reindexes.  If a reindex is currently taking place then information about this reindex is returned.
 If there is no active index task, then returns information about the latest reindex task run, otherwise returns a 404
 indicating that no reindex has taken place.

<details><summary>Parameters</summary>

### taskId

the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and
               returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no
               reindexing task with that id then a 404 is returned.

**Type:** integer

</details>

## get_reindex_progress

Returns information on the system reindexes.  If a reindex is currently taking place then information about this reindex is returned.
 If there is no active index task, then returns information about the latest reindex task run, otherwise returns a 404
 indicating that no reindex has taken place.

<details><summary>Parameters</summary>

### taskId

the id of an indexing task you wish to obtain details on.  If omitted, then defaults to the standard behaviour and
               returns information on the active reindex task, or the last task to run if no reindex is taking place. .  If there is no
               reindexing task with that id then a 404 is returned.

**Type:** integer

</details>

## get_remote_issue_link_by_id

Get the remote issue link with the given id on the issue.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue to create the remote issue link for

**Type:** string

### linkId (required)

the id of the remote issue link

**Type:** string

</details>

## get_remote_issue_links

A REST sub-resource representing the remote issue links on the issue.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue to create the remote issue link for

**Type:** string

### globalId

The id of the remote issue link to be returned.  If null (not provided) all remote links for the
                     issue are returned.
                     For a fullexplanation of Issue Link fields please refer to
                     https://developer.atlassian.com/display/JIRADEV/Fields+in+Remote+Issue+Links

**Type:** string

</details>

## get_remote_version_link

A REST sub-resource representing a remote version link

<details><summary>Parameters</summary>

### globalId (required)

The global ID of the remote link

**Type:** string

### versionId (required)

The version ID of the remote link

**Type:** string

</details>

## get_remote_version_links

Returns the remote version links for a given global ID.

<details><summary>Parameters</summary>

### globalId

the global ID of the remote resource that is linked to the versions

**Type:** string

</details>

## get_remote_version_links_by_version_id

Returns the remote version links associated with the given version ID.

<details><summary>Parameters</summary>

### versionId (required)

The version for which to delete ALL existing remote version links

**Type:** string

</details>

## get_resolution

Returns a resolution.

<details><summary>Parameters</summary>

### id (required)

a String containing the resolution id

**Type:** string

</details>

## get_resolutions



*This operation has no parameters*

## get_scheme_attribute



<details><summary>Parameters</summary>

### attributeKey (required)

permission scheme attribute key

**Type:** string

### permissionSchemeId (required)

permission scheme id

**Type:** integer

</details>

## get_security_levels_for_project

Returns all security levels for the project that the current logged in user has access to.
 If the user does not have the Set Issue Security permission, the list will be empty.

<details><summary>Parameters</summary>

### projectKeyOrId (required)

- key or id of project to list the security levels for

**Type:** string

</details>

## get_server_info

Returns general information about the current JIRA server.

<details><summary>Parameters</summary>

### doHealthCheck

**Type:** boolean

</details>

## get_share_permission

Returns a single share permission of the given filter.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

### permissionId (required)

**Type:** integer

</details>

## get_share_permissions

Returns all share permissions of the given filter.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

</details>

## get_sprints

Returns a list of all the sprints for a board

<details><summary>Parameters</summary>

### boardId (required)

- id of board.

**Type:** string

</details>

## get_state



*This operation has no parameters*

## get_status

Returns a full representation of the Status having the given id or name.

<details><summary>Parameters</summary>

### idOrName (required)

a numeric Status id or a status name

**Type:** string

</details>

## get_status_categories



*This operation has no parameters*

## get_status_category

Returns a full representation of the StatusCategory having the given id or key

<details><summary>Parameters</summary>

### idOrKey (required)

a numeric StatusCategory id or a status category key

**Type:** string

</details>

## get_statuses



*This operation has no parameters*

## get_sub_tasks

Returns an issue's subtask list

<details><summary>Parameters</summary>

### issueIdOrKey (required)

The parent issue's key or id

**Type:** string

</details>

## get_transitions

Get a list of the transitions possible for this issue by the current user, along with fields that are required and their types.
 
 Fields will only be returned if expand=transitions.fields.
 
 The fields in the metadata correspond to the fields in the transition screen for that transition.
 Fields not in the screen will not be in the metadata.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue whose transitions you want to view

**Type:** string

### transitionId

**Type:** string

</details>

## get_upgrade_result



*This operation has no parameters*

## get_user

Returns a user. This resource cannot be accessed anonymously.

<details><summary>Parameters</summary>

### key

user key

**Type:** string

### username

the username

**Type:** string

</details>

## get_user_property

Returns the value of the property with a given key from the user identified by the key or by the id. The user who retrieves
 the property is required to have permissions to read the user.

<details><summary>Parameters</summary>

### propertyKey (required)

**Type:** string

### userKey

key of the user whose property is to be returned

**Type:** string

### username

username of the user whose property is to be returned

**Type:** string

</details>

## get_users_from_group

This resource returns a paginated list of users who are members of the specified group and its subgroups.
 Users in the page are ordered by user names. User of this resource is required to have sysadmin or admin permissions.

<details><summary>Parameters</summary>

### groupname

a name of the group for which members will be returned.

**Type:** string

### includeInactiveUsers

inactive users will be included in the response if set to true.

**Type:** boolean

</details>

## get_version

Returns a project version.

<details><summary>Parameters</summary>

### id (required)

The version to delete

**Type:** string

### expand

**Type:** string

</details>

## get_version_related_issues

Returns a bean containing the number of fixed in and affected issues for the given version.

<details><summary>Parameters</summary>

### id (required)

a String containing the version id

**Type:** string

</details>

## get_version_unresolved_issues

Returns the number of unresolved issues for the given version

<details><summary>Parameters</summary>

### id (required)

a String containing the version id

**Type:** string

</details>

## get_votes

A REST sub-resource representing the voters on the issue.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue to view voting information for

**Type:** string

</details>

## get_workflow

Returns the workflow mappings or requested mapping to the caller for the passed scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### returnDraftIfExists

when true indicates that a scheme's draft, if it exists, should be queried instead of
                            the scheme itself.

**Type:** boolean

### workflowName

the workflow mapping to return. Null can be passed to return all mappings. Must be a valid workflow name.

**Type:** string

</details>

## get_worklog

Returns a specific worklog. 
 Note: The work log won't be returned if the Log work field is hidden for the project.

<details><summary>Parameters</summary>

### id (required)

id of the worklog to be deleted

**Type:** string

### issueIdOrKey (required)

a string containing the issue id or key the worklog belongs to

**Type:** string

</details>

## get_worklogs_for_ids

Returns worklogs for given worklog ids. Only worklogs to which the calling user has permissions, will be included in the result.
 The returns set of worklogs is limited to 1000 elements.

<details><summary>Parameters</summary>

### $body

**Type:** string

</details>

## link_issues

Creates an issue link between two issues.
 The user requires the link issue permission for the issue which will be linked to another issue.
 The specified link type in the request is used to create the link and will create a link from the first issue
 to the second issue using the outward description. It also create a link from the second issue to the first issue using the
 inward description of the issue link type.
 It will add the supplied comment to the first issue. The comment can have a restriction who can view it.
 If group is specified, only users of this group can view this comment, if roleLevel is specified only users who have the specified role can view this comment.
 The user who creates the issue link needs to belong to the specified group or have the specified role.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## list

Returns a list of all dashboards, optionally filtering them.

<details><summary>Parameters</summary>

### filter

an optional filter that is applied to the list of dashboards. Valid values include
                        "favourite" for returning only favourite dashboards, and "my" for returning
                        dashboards that are owned by the calling user.

**Type:** string

</details>

## login

Creates a new session for a user in JIRA. Once a session has been successfully created it can be used to access
 any of JIRA's remote APIs and also the web UI by passing the appropriate HTTP Cookie header.
 
 Note that it is generally preferrable to use HTTP BASIC authentication with the REST API. However, this resource
 may be used to mimic the behaviour of JIRA's log-in page (e.g. to display log-in errors to a user).

<details><summary>Parameters</summary>

### $body

**Type:** string

</details>

## logout



*This operation has no parameters*

## merge

Merge versions

<details><summary>Parameters</summary>

### id (required)

The version that will be merged to version {@code moveIssuesTo} and removed

**Type:** string

### moveIssuesTo (required)

The version to set fixVersion to on issues where the deleted version is the fix version,
                     If null then the fixVersion is removed.

**Type:** string

</details>

## move_field

Moves field on the given tab

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### screenId (required)

id of screen

**Type:** integer

### tabId (required)

id of tab

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## move_sub_tasks

Reorders an issue's subtasks by moving the subtask at index "from"
 to index "to".

<details><summary>Parameters</summary>

### issueIdOrKey (required)

The parent issue's key or id

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## move_tab

Moves tab position

<details><summary>Parameters</summary>

### pos (required)

position of tab

**Type:** integer

### screenId (required)

id of screen

**Type:** integer

### tabId (required)

id of tab

**Type:** integer

</details>

## move_version

Modify a version's sequence within a project.
 
 The move version bean has 2 alternative field value pairs:
 
 positionAn absolute position, which may have a value of 'First', 'Last', 'Earlier' or 'Later'
 afterA version to place this version after.  The value should be the self link of another version
 

<details><summary>Parameters</summary>

### id (required)

a String containing the version id

**Type:** string

### $body

**Type:** string

</details>

## notify

Sends a notification (email) to the list or recipients defined in the request.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

a string containing the issue id or key the comment will be added to

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## partial_update_project_role

Partially updates a roles name or description.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## policy_check_create_user

Returns a list of statements explaining why the password policy would disallow a proposed password for a new user.
 
 You can use this method to test the password policy validation. This could be done prior to an action 
 where a new user and related password are created, using methods like the ones in 
 UserService.      
 For example, you could use this to validate a password in a create user form in the user interface, as the user enters it.
 The username and new password must be not empty to perform the validation.
 Note, this method will help you validate against the policy only. It won't check any other validations that might be performed 
 when creating a new user, e.g. checking whether a user with the same name already exists.
 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## policy_check_update_user

Returns a list of statements explaining why the password policy would disallow a proposed new password for a user with an existing password.
 
 You can use this method to test the password policy validation. This could be done prior to an action where the password 
 is actually updated, using methods like ChangePassword      
 or ResetPassword. 
 For example, you could use this to validate a password in a change password form in the user interface, as the user enters it.
 The user must exist and the username and new password must be not empty, to perform the validation.
 Note, this method will help you validate against the policy only. It won't check any other validations that might be performed 
 when submitting a password change/reset request, e.g. verifying whether the old password is valid.
 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## process_requests



*This operation has no parameters*

## put

Updates the ApplicationRole with the passed data. Only the groups and default groups setting of the
 role may be updated. Requests to change the key or the name of the role will be silently ignored.
 
 Optional: If versionHash is passed through the If-Match header the request will be rejected if not the
 same as server

<details><summary>Parameters</summary>

### key (required)

the key of the role to update.

**Type:** string

### $body

**Type:** object

```json
{ }
```

### If-Match

the hash of the version to update. Optional Param

**Type:** string

</details>

## put_bulk

Updates the ApplicationRoles with the passed data if the version hash is the same as the server.
 Only the groups and default groups setting of the role may be updated. Requests to change the key
 or the name of the role will be silently ignored. It is acceptable to pass only the roles that are updated
 as roles that are present in the server but not in data to update with, will not be deleted.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

### If-Match

**Type:** string

</details>

## reindex

Kicks off a reindex. Need Admin permissions to perform this reindex.

<details><summary>Parameters</summary>

### indexChangeHistory

Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed.

**Type:** boolean

### indexComments

Indicates that comments should also be reindexed. Not relevant for foreground reindex, where comments are always reindexed.

**Type:** boolean

### indexWorklogs

Indicates that changeHistory should also be reindexed. Not relevant for foreground reindex, where changeHistory is always reindexed.

**Type:** boolean

### type

Case insensitive String indicating type of reindex. If omitted, then defaults to BACKGROUND_PREFERRED.

**Type:** string

</details>

## reindex_issues

Reindexes one or more individual issues.  Indexing is performed synchronously - the call returns when indexing of
 the issues has completed or a failure occurs.
 
 Use either explicitly specified issue IDs or a JQL query to select issues to reindex.

<details><summary>Parameters</summary>

### indexChangeHistory

Indicates that changeHistory should also be reindexed.

**Type:** boolean

### indexComments

Indicates that comments should also be reindexed.

**Type:** boolean

### indexWorklogs

Indicates that changeHistory should also be reindexed.

**Type:** boolean

### issueId

the IDs or keys of one or more issues to reindex.

**Type:** string

</details>

## release



*This operation has no parameters*

## remove_attachment

Remove an attachment from an issue.

<details><summary>Parameters</summary>

### id (required)

id of the attachment to remove

**Type:** string

</details>

## remove_field

Removes field from given tab

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### screenId (required)

id of screen

**Type:** integer

### tabId (required)

id of tab

**Type:** integer

</details>

## remove_group

Deletes a group by given group parameter.
 
 Returns no content

<details><summary>Parameters</summary>

### groupname

(mandatory) The name of the group to delete.

**Type:** string

### swapGroup

If you delete a group and content is restricted to that group, the content will be hidden from all users. 
 To prevent this, use this parameter to specify a different group to transfer the restrictions (comments and worklogs only) to.

**Type:** string

</details>

## remove_preference

Removes preference of the currently logged in user. Preference key must be provided as input parameters (key). If
 key parameter is not provided or wrong - status code 404. If preference is unset - status code 204.

<details><summary>Parameters</summary>

### key

- key of the preference to be removed.

**Type:** string

</details>

## remove_project_category

Delete a project category.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

</details>

## remove_user

Removes user.

<details><summary>Parameters</summary>

### key

user key

**Type:** string

### username

the username

**Type:** string

</details>

## remove_user_from_application

Remove user from given application. Admin permission will be required to perform this operation.

<details><summary>Parameters</summary>

### applicationKey

application key

**Type:** string

### username

username

**Type:** string

</details>

## remove_user_from_group

Removes given user from a group.
 
 Returns no content

<details><summary>Parameters</summary>

### groupname

A name of requested group.

**Type:** string

### username

User to remove from a group

**Type:** string

</details>

## remove_vote

Remove your vote from an issue. (i.e. "unvote")

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue to view voting information for

**Type:** string

</details>

## remove_watcher

Removes a user from an issue's watcher list.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

a String containing an issue key.

**Type:** string

### username

a String containing the name of the user to remove from the watcher list. Must not be null.

**Type:** string

</details>

## rename_tab

Renames tab on given screen

<details><summary>Parameters</summary>

### screenId (required)

id of screen

**Type:** integer

### tabId (required)

id of tab

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## reset_columns_with_filter

Resets the columns for the given filter such that the filter no longer has its own column config.

<details><summary>Parameters</summary>

### id (required)

id of the filter

**Type:** integer

</details>

## reset_default_columns

Reset the default columns for the given user to the system default. Admin permission will be required to get
 columns for a user other than the currently logged in user.

<details><summary>Parameters</summary>

### username

username

**Type:** string

</details>

## run_upgrades_now



*This operation has no parameters*

## search

Searches for issues using JQL.
 
 Sorting
 the jql parameter is a full JQL
 expression, and includes an ORDER BY clause.
 
 
 The fields param (which can be specified multiple times) gives a comma-separated list of fields
 to include in the response. This can be used to retrieve a subset of fields.
 A particular field can be excluded by prefixing it with a minus.
 
 By default, only navigable (*navigable) fields are returned in this search resource. Note: the default is different
 in the get-issue resource -- the default there all fields (*all).
 
 *all - include all fields
 *navigable - include just navigable fields
 summary,comment - include just the summary and comments
 -description - include navigable fields except the description (the default is *navigable for search)
 *all,-comment - include everything except comments
 
 
 
 GET vs POST:
 If the JQL query is too large to be encoded as a query param you should instead
 POST to this resource.
 
 
 Expanding Issues in the Search Result:
 It is possible to expand the issues returned by directly specifying the expansion on the expand parameter passed
 in to this resources.
 
 
 For instance, to expand the "changelog" for all the issues on the search result, it is neccesary to
 specify "changelog" as one of the values to expand.
 

<details><summary>Parameters</summary>

### expand

A comma-separated list of the parameters to expand.

**Type:** string

### fields

the list of fields to return for each issue. By default, all navigable fields are returned.

**Type:** string

### jql

a JQL query string

**Type:** string

### validateQuery

whether to validate the JQL query

**Type:** boolean

</details>

## search_using_search_request

Performs a search using JQL.

<details><summary>Parameters</summary>

### $body

**Type:** string

</details>

## set_actors

Updates a project role to include the specified actors (users or groups).

<details><summary>Parameters</summary>

### id (required)

the project role id

**Type:** integer

### projectIdOrKey (required)

the project id or project key

**Type:** string

### $body

**Type:** string

</details>

## set_base_url

Sets the base URL that is configured for this JIRA instance.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## set_comment_property

Sets the value of the specified comment's property.
 
 You can use this resource to store a custom data against the comment identified by the key or by the id. The user
 who stores the data is required to have permissions to administer the comment.
 

<details><summary>Parameters</summary>

### commentId (required)

the comment from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## set_default_share_scope

Sets the default share scope of the logged-in user. Available values are GLOBAL and PRIVATE.

<details><summary>Parameters</summary>

### $body

**Type:** string

</details>

## set_draft_issue_type

Set the issue type mapping for the passed draft scheme.
 
 The passed representation can have its updateDraftIfNeeded flag set to true to indicate that
 the draft should be created/updated when the actual scheme cannot be edited.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

### issueType (required)

the issue type being set.

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## set_issue_property

Sets the value of the specified issue's property.
 
 You can use this resource to store a custom data against the issue identified by the key or by the id. The user
 who stores the data is required to have permissions to edit the issue.
 

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## set_issue_type

Set the issue type mapping for the passed scheme.
 
 The passed representation can have its updateDraftIfNeeded flag set to true to indicate that
 the draft should be created/updated when the actual scheme cannot be edited.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### issueType (required)

the issue type being set.

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## set_issue_type_property

Sets the value of the specified issue type's property.
 
 You can use this resource to store a custom data against an issue type identified by the id. The user
 who stores the data is required to have permissions to edit an issue type.
 

<details><summary>Parameters</summary>

### issueTypeId (required)

the issue type from which the property will be returned

**Type:** string

### propertyKey (required)

the key of the property to return

**Type:** string

</details>

## set_preference

Sets preference of the currently logged in user. Preference key must be provided as input parameters (key). Value
 must be provided as post body. If key or value parameter is not provided - status code 404. If preference is set
 - status code 204.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

### key

- key of the preference to be set.

**Type:** string

</details>

## set_project_property

Sets the value of the specified project's property.
 
 You can use this resource to store a custom data against the project identified by the key or by the id. The user
 who stores the data is required to have permissions to administer the project.
 

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## set_property_for_dashboard_item

Sets the value of the specified dashboard item's property.
 
 You can use this resource to store a custom data against the dashboard item identified by the id.
 The user who stores the data is required to have permissions to administer the dashboard item.
 

<details><summary>Parameters</summary>

### dashboardId (required)

**Type:** string

### itemId (required)

the dashboard item from which the property will be returned.

**Type:** string

### propertyKey (required)

the key of the property to return.

**Type:** string

</details>

## set_property_via_restful_table

Modify an application property via PUT. The "value" field present in the PUT will override the existing value.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

**Type:** string

</details>

## set_ready_to_upgrade



*This operation has no parameters*

## set_scheme_attribute

Updates or inserts the attribute for a permission scheme specified by permission scheme id.
 The attribute consists of the key and the value. The value will be converted to Boolean using Boolean#valueOf.

<details><summary>Parameters</summary>

### key (required)

permission scheme attribute key

**Type:** string

### permissionSchemeId (required)

permission scheme id

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## set_user_property

Sets the value of the specified user's property.
 
 You can use this resource to store a custom data against the user identified by the key or by the id. The user
 who stores the data is required to have permissions to administer the user.
 

<details><summary>Parameters</summary>

### propertyKey (required)

**Type:** string

### userKey

key of the user whose property is to be set

**Type:** string

### username

username of the user whose property is to be set

**Type:** string

</details>

## start



*This operation has no parameters*

## stop



*This operation has no parameters*

## store_temporary_avatar

Creates temporary avatar

<details><summary>Parameters</summary>

### type (required)

the avatar type

**Type:** string

### filename

name of file being uploaded

**Type:** string

### size

size of file

**Type:** integer

</details>

## store_temporary_avatar_using_multi_part_by_type



<details><summary>Parameters</summary>

### owningObjectId (required)

**Type:** string

### type (required)

**Type:** string

</details>

## store_temporary_avatar_using_multi_part_for_issue

Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because
 the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from
 which the client parses the JSON from.
 
 Creating a temporary avatar is part of a 3-step process in uploading a new
 avatar for an issue type: upload, crop, confirm. This endpoint allows you to use a multipart upload
 instead of sending the image directly as the request body.
 
 
 You *must* use "avatar" as the name of the upload parameter:
 
  curl -c cookiejar.txt -X POST -u admin:admin -H "X-Atlassian-Token: no-check" \
   -F "avatar=@mynewavatar.png;type=image/png" \
   'http://localhost:8090/jira/rest/api/2/issuetype/1/avatar/temporary'
 

<details><summary>Parameters</summary>

### id (required)

the id of the issue type, which avatar is updated.

**Type:** string

</details>

## store_temporary_avatar_using_multi_part_for_project

Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because
 the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from
 which the client parses the JSON.

<details><summary>Parameters</summary>

### projectIdOrKey (required)

Project id or project key

**Type:** string

</details>

## store_temporary_avatar_using_multi_part_for_user

Creates temporary avatar using multipart. The response is sent back as JSON stored in a textarea. This is because
 the client uses remote iframing to submit avatars using multipart. So we must send them a valid HTML page back from
 which the client parses the JSON from.
 
 Creating a temporary avatar is part of a 3-step process in uploading a new
 avatar for a user: upload, crop, confirm. This endpoint allows you to use a multipart upload
 instead of sending the image directly as the request body.
 
 
 You *must* use "avatar" as the name of the upload parameter:
 
  curl -c cookiejar.txt -X POST -u admin:admin -H "X-Atlassian-Token: no-check" \
   -F "avatar=@mynewavatar.png;type=image/png" \
   'http://localhost:8090/jira/rest/api/2/user/avatar/temporary?username=admin'
 

<details><summary>Parameters</summary>

### username

Username

**Type:** string

</details>

## update

Update the passed workflow scheme.
 
 The body of the request is a representation of the workflow scheme. Values not passed are assumed to indicate
 no change for that field.
 
 The passed representation can have its updateDraftIfNeeded flag set to true to indicate that the draft
 should be created and/or updated when the actual scheme cannot be edited (e.g. when the scheme is being used by
 a project). Values not appearing the body will not be touched.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## update_avatar_from_temporary

Updates the cropping instructions of the temporary avatar.

<details><summary>Parameters</summary>

### type (required)

the avatar type

**Type:** string

### $body

**Type:** string

</details>

## update_comment

Updates an existing comment using its JSON representation.

<details><summary>Parameters</summary>

### id (required)

the ID of the comment to request

**Type:** string

### issueIdOrKey (required)

of the issue the comment belongs to

**Type:** string

### $body

**Type:** object

```json
{ }
```

### expand

optional flags: renderedBody (provides body rendered in HTML)

**Type:** string

</details>

## update_component

Modify a component via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field
 is not present, it is silently ignored.
 
 If leadUserName is an empty string ("") the component lead will be removed.

<details><summary>Parameters</summary>

### id (required)

The component to delete.

**Type:** string

### $body

**Type:** string

</details>

## update_default

Set the default workflow for the passed workflow scheme.
 
 The passed representation can have its
 updateDraftIfNeeded flag set to true to indicate that the draft should be created/updated when the actual scheme
 cannot be edited.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## update_draft

Update a draft workflow scheme. The draft will created if necessary.
 
 The body is a representation of the workflow scheme. Values not passed are assumed to indicate no change for that field.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## update_draft_default

Set the default workflow for the passed draft workflow scheme.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## update_draft_workflow_mapping

Update the draft scheme to include the passed mapping.
 
 The body is a representation of the workflow mapping.
 Values not passed are assumed to indicate no change for that field.

<details><summary>Parameters</summary>

### id (required)

the id of the parent scheme.

**Type:** integer

### $body

**Type:** object

```json
{ }
```

### workflowName

the name of the workflow mapping to update.

**Type:** string

</details>

## update_issue_link_type

Update the specified issue link type.

<details><summary>Parameters</summary>

### issueLinkTypeId (required)

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## update_issue_type

Updates the specified issue type from a JSON representation.

<details><summary>Parameters</summary>

### id (required)

the id of the issue type to update.

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## update_logged_in_user

Modify currently logged user. The "value" fields present will override the existing value.
 Fields skipped in request will not be changed. Only email and display name can be change that way.
 Requires user password.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## update_permission_scheme

Updates a permission scheme.
 
 If the permissions list is present then it will be set in the permission scheme, which basically means it will overwrite any permission grants that
 existed in the permission scheme. Sending an empty list will remove all permission grants from the permission scheme.
 
 
 To update just the name and description, do not send permissions list at all.
 
 
 To add or remove a single permission grant instead of updating the whole list at once use the {schemeId}/permission/ resource.
 

<details><summary>Parameters</summary>

### schemeId (required)

**Type:** integer

### $body

**Type:** object

```json
{ }
```

### expand

**Type:** string

</details>

## update_project

Updates a project.
 
 Only non null values sent in JSON will be updated in the project.
 
 Values available for the assigneeType field are: "PROJECT_LEAD" and "UNASSIGNED".

<details><summary>Parameters</summary>

### projectIdOrKey (required)

the project id or project key

**Type:** string

### $body

**Type:** object

```json
{ }
```

### expand

the parameters to expand in returned project

**Type:** string

</details>

## update_project_avatar_for_project



<details><summary>Parameters</summary>

### projectIdOrKey (required)

**Type:** string

### $body

**Type:** string

</details>

## update_project_avatar_for_user



<details><summary>Parameters</summary>

### $body

**Type:** string

### username

**Type:** string

</details>

## update_project_category

Modify a project category via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field
 is not present, it is silently ignored.

<details><summary>Parameters</summary>

### id (required)

**Type:** integer

### $body

**Type:** object

```json
{ }
```

</details>

## update_project_type

Updates the type of a project.

<details><summary>Parameters</summary>

### newProjectTypeKey (required)

The key of the new project type

**Type:** string

### projectIdOrKey (required)

identity of the project to update

**Type:** string

</details>

## update_property

Update/add new property to a transition. Trying to update a property that does
 not exist will result in a new property being added.

<details><summary>Parameters</summary>

### id (required)

the ID of the transition within the workflow.

**Type:** integer

### $body

**Type:** object

```json
{ }
```

### key

the name of the property to add.

**Type:** string

### workflowMode

the type of workflow to use. Can either be "live" or "draft".

**Type:** string

### workflowName

the name of the workflow to use.

**Type:** string

</details>

## update_remote_issue_link

Updates a remote issue link from a JSON representation. Any fields not provided are set to null.

<details><summary>Parameters</summary>

### issueIdOrKey (required)

the issue to create the remote issue link for

**Type:** string

### linkId (required)

the id of the remote issue link

**Type:** string

### $body

**Type:** object

```json
{ }
```

</details>

## update_user

Modify user. The "value" fields present will override the existing value.
 Fields skipped in request will not be changed.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

### key

user key

**Type:** string

### username

the username

**Type:** string

</details>

## update_version

Modify a version via PUT. Any fields present in the PUT will override existing values. As a convenience, if a field
 is not present, it is silently ignored.

<details><summary>Parameters</summary>

### id (required)

The version to delete

**Type:** string

### $body

**Type:** string

</details>

## update_workflow_mapping

Update the scheme to include the passed mapping.
 
 The body is a representation of the workflow mapping.
 Values not passed are assumed to indicate no change for that field.
 
 The passed representation can have its updateDraftIfNeeded flag set to true to indicate that the draft
 should be created/updated when the actual scheme cannot be edited.

<details><summary>Parameters</summary>

### id (required)

the id of the scheme.

**Type:** integer

### $body

**Type:** object

```json
{ }
```

### workflowName

the name of the workflow mapping to update.

**Type:** string

</details>

## update_worklog

Updates an existing worklog entry.
 Note that:
  
      Fields possible for editing are: comment, visibility, started, timeSpent and timeSpentSeconds.
      Either timeSpent or timeSpentSeconds can be set.
      Fields which are not set will not be updated.
      For a request to be valid, it has to have at least one field change.
  

<details><summary>Parameters</summary>

### id (required)

id of the worklog to be deleted

**Type:** string

### issueIdOrKey (required)

a string containing the issue id or key the worklog belongs to

**Type:** string

### $body

**Type:** string

### adjustEstimate

(optional) allows you to provide specific instructions to update the remaining time estimate of the issue.  Valid values are
                       
                       "new" - sets the estimate to a specific value
                       "leave"- leaves the estimate as is
                       "auto"- Default option.  Will automatically adjust the value based on the new timeSpent specified on the worklog 

**Type:** string

### newEstimate

(required when "new" is selected for adjustEstimate) the new value for the remaining estimate field.

**Type:** string

</details>

## validate



<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

