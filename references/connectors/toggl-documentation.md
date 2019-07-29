---
id: toggl-documentation
title: Toggl (version v1.*.*)
sidebar_label: Toggl
layout: docs.mustache
---

## create_client

Create a client

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "client" : {
    "wid" : "workspace ID",
    "notes" : "notes for the client",
    "at" : "timestamp that is sent in the response",
    "name" : "name of the client"
  }
}
```

</details>

## create_group

Create a group

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "group" : {
    "wid" : "workspace ID",
    "at" : "timestamp that is sent in the response",
    "name" : "name of the group"
  }
}
```

</details>

## create_project

Create a project

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "project" : {
    "is_private" : "whether project is accessible for only project users or for all workspace users",
    "template" : "whether the project can be used as a template",
    "color" : "id of the color selected for the project",
    "active" : "whether the project is archived or not",
    "billable" : "whether the project is billable or not, available only for pro workspaces",
    "auto_estimates" : "whether the estimated hours are automatically calculated based on task estimations or manually fixed based on the value of 'estimated_hours', premium functionality",
    "wid" : "workspace ID",
    "at" : "timestamp indicating when the project was created (UTC time), read-only",
    "rate" : "hourly rate of the project, premium functionality",
    "name" : "name of the project",
    "estimated_hours" : "if auto_estimates is true then the sum of task estimations is returned, otherwise user inserted hours, premium functionality",
    "template_id" : "id of the template project used on current project's creation",
    "cid" : "client ID"
  }
}
```

</details>

## create_tag

Create tag

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "tag" : {
    "wid" : "workspace ID, where the tag will be used",
    "name" : "The name of the tag, unique in workspace"
  }
}
```

</details>

## create_task

Create a task

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "task" : {
    "uid" : "user ID, to whom the task is assigned to",
    "wid" : "workspace ID",
    "at" : "timestamp that is sent in the response for PUT, indicates the time task was last updated",
    "estimated_seconds" : "estimated duration of task in seconds",
    "name" : "The name of the task",
    "active" : "whether the task is done or not",
    "pid" : "project ID for the task",
    "tracked_seconds" : "total time tracked (in seconds) for the task"
  }
}
```

</details>

## create_time_entry

Create a time entry

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "time_entry" : {
    "duration" : "time entry duration in seconds. If the time entry is currently running, the duration attribute contains a negative value, denoting the start of the time entry in seconds since epoch (Jan 1 1970). The correct duration can be calculated as current_time + duration, where current_time is the current time in seconds since epoch.",
    "wid" : "workspace ID",
    "at" : "timestamp that is sent in the response, indicates the time item was last updated",
    "stop" : "time entry stop time, ISO 8601 date and time",
    "start" : "time entry start time, ISO 8601 date and time",
    "description" : "description",
    "pid" : "project ID",
    "created_with" : "the name of your client app",
    "billable" : "available for pro workspaces",
    "duronly" : "should Toggl show the start and stop time of this time entry?",
    "tid" : "task ID",
    "tags" : [ "string" ]
  }
}
```

</details>

## create_user_for_project

Create a project user. To create multiple project users for a single project, you must add multiple user ids separated with a comma with the uid parameter.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "project_user" : {
    "uid" : { },
    "wid" : "workspace ID",
    "at" : "timestamp that is sent in the response, indicates when the project user was last updated",
    "manager" : "admin rights for this project",
    "rate" : "hourly rate for the project user (only for pro workspaces) in the currency of the project's client or in workspace default currency.",
    "pid" : "project ID",
    "fields" : "fullname: full name of the user, who is added to the project"
  }
}
```

</details>

## delete_client

Delete a client

<details><summary>Parameters</summary>

### client_id (required)

client ID

**Type:** integer

</details>

## delete_group

Delete a group

<details><summary>Parameters</summary>

### group_id (required)

group ID

**Type:** integer

</details>

## delete_multiple_projects

Delete multiple projects

<details><summary>Parameters</summary>

### project_ids (required)

multiple project IDs

**Type:** array

```json
[ "schema_type_none" ]
```

</details>

## delete_multiple_users_for_project

Delete multiple project users

<details><summary>Parameters</summary>

### project_user_ids (required)

multiple project user IDs

**Type:** array

```json
[ "schema_type_none" ]
```

</details>

## delete_project

Delete a project

<details><summary>Parameters</summary>

### project_id (required)

project ID

**Type:** integer

</details>

## delete_tag

Delete a tag

<details><summary>Parameters</summary>

### tag_id (required)

tag ID

**Type:** integer

</details>

## delete_task

Delete a task

<details><summary>Parameters</summary>

### task_id (required)

multiple task IDs

**Type:** object

```json
{ }
```

</details>

## delete_time_entry

Delete a time entry

<details><summary>Parameters</summary>

### time_entry_id (required)

time entry ID

**Type:** integer

</details>

## delete_user_for_project

Delete a project user

<details><summary>Parameters</summary>

### project_user_id (required)

project user ID

**Type:** integer

</details>

## delete_workspace_user

Delete workspace user.

<details><summary>Parameters</summary>

### workspace_user_id (required)

workspace user ID

**Type:** integer

</details>

## get_client

Get client details

<details><summary>Parameters</summary>

### client_id (required)

client ID

**Type:** integer

</details>

## get_current_user_data

Get current user data

<details><summary>Parameters</summary>

### since

retrieve objects which have changed after certain time. The value should be a unix timestamp.

**Type:** string

### with_related_data

whether to get all the workspaces, clients, projects, tasks, time entries and tags which the user can see

**Type:** boolean

</details>

## get_dashboard_data

Get dashboard data. Dashboard's main purpose is to give an overview of what users in the workspace are doing and have been doing.

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

</details>

## get_detailed_report

The detailed report returns the time entries for the requested parameters/filters.

<details><summary>Parameters</summary>

### user_agent (required)

The name of your application or your email address so we can get in touch in case you're doing something wrong.

**Type:** string

### workspace_id (required)

The workspace whose data you want to access.

**Type:** integer

### billable

**Type:** string

**Potential values:** yes, no, both

### client_ids

A list of client IDs separated by a comma. Use "0" if you want to filter out time entries without a client.

**Type:** object

```json
{ }
```

### description

Matches against time entry descriptions.

**Type:** string

### display_hours

Determines whether to display hours as a decimal number or with minutes.

**Type:** string

**Potential values:** decimal, minutes

### distinct_rates

**Type:** string

**Potential values:** on, off

### members_of_group_ids

A list of group IDs separated by a comma. This limits provided user_ids to the members of the given groups.

**Type:** array

```json
[ "schema_type_none" ]
```

### or_members_of_group_ids

A list of group IDs separated by a comma. This extends provided user_ids with the members of the given groups.

**Type:** array

```json
[ "schema_type_none" ]
```

### order_desc

"on" for descending, or "off" for ascending order.

**Type:** string

**Potential values:** on, off

### order_field

**Type:** string

**Potential values:** date, description, duration, user

### page

**Type:** integer

### project_ids

A list of project IDs separated by a comma. Use "0" if you want to filter out time entries without a project.

**Type:** object

```json
{ }
```

### rounding

Rounds time according to workspace settings.

**Type:** string

**Potential values:** on, off

### since

ISO 8601 date (YYYY-MM-DD) format. Defaults to today - 6 days.

**Type:** string

### tag_ids

A list of tag IDs separated by a comma. Use "0" if you want to filter out time entries without a tag.

**Type:** object

```json
{ }
```

### task_ids

A list of task IDs separated by a comma. Use "0" if you want to filter out time entries without a task.

**Type:** object

```json
{ }
```

### time_entry_ids

A list of time entry IDs separated by a comma.

**Type:** array

```json
[ "schema_type_none" ]
```

### until

ISO 8601 date (YYYY-MM-DD) format. Note: Maximum date span (until - since) is one year. Defaults to today, unless since is in future or more than year ago, in this case until is since + 6 days.

**Type:** string

### user_ids

A list of user IDs separated by a comma.

**Type:** array

```json
[ "schema_type_none" ]
```

### without_description

Filters out the time entries which do not have a description (literally "(no description)").

**Type:** boolean

</details>

## get_project

Get project data

<details><summary>Parameters</summary>

### project_id (required)

project ID

**Type:** integer

</details>

## get_project_users_for_workspace

Get workspace project users

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

</details>

## get_projects_for_client

Get client projects

<details><summary>Parameters</summary>

### client_id (required)

client ID

**Type:** integer

### active

By default true. If false, only archived projects are returned.

**Type:** string

**Potential values:** true, false, both

</details>

## get_running_time_entry



*This operation has no parameters*

## get_summary_report

Summary report returns the aggregated time entries data. time entries for the requested

<details><summary>Parameters</summary>

### user_agent (required)

The name of your application or your email address so we can get in touch in case you're doing something wrong.

**Type:** string

### workspace_id (required)

The workspace whose data you want to access.

**Type:** integer

### billable

**Type:** string

**Potential values:** yes, no, both

### client_ids

A list of client IDs separated by a comma. Use "0" if you want to filter out time entries without a client.

**Type:** object

```json
{ }
```

### description

Matches against time entry descriptions.

**Type:** string

### display_hours

Determines whether to display hours as a decimal number or with minutes.

**Type:** string

**Potential values:** decimal, minutes

### distinct_rates

**Type:** string

**Potential values:** on, off

### grouped_time_entry_ids

**Type:** boolean

### grouping

**Type:** string

**Potential values:** projects, clients, users

### members_of_group_ids

A list of group IDs separated by a comma. This limits provided user_ids to the members of the given groups.

**Type:** array

```json
[ "schema_type_none" ]
```

### or_members_of_group_ids

A list of group IDs separated by a comma. This extends provided user_ids with the members of the given groups.

**Type:** array

```json
[ "schema_type_none" ]
```

### order_desc

"on" for descending, or "off" for ascending order.

**Type:** string

**Potential values:** on, off

### order_field

**Type:** string

**Potential values:** title, duration, amount

### project_ids

A list of project IDs separated by a comma. Use "0" if you want to filter out time entries without a project.

**Type:** object

```json
{ }
```

### rounding

Rounds time according to workspace settings.

**Type:** string

**Potential values:** on, off

### since

ISO 8601 date (YYYY-MM-DD) format. Defaults to today - 6 days.

**Type:** string

### subgrouping

**Type:** string

**Potential values:** time_entries, tasks, users, projects, clients

### subgrouping_ids

**Type:** boolean

### tag_ids

A list of tag IDs separated by a comma. Use "0" if you want to filter out time entries without a tag.

**Type:** object

```json
{ }
```

### task_ids

A list of task IDs separated by a comma. Use "0" if you want to filter out time entries without a task.

**Type:** object

```json
{ }
```

### time_entry_ids

A list of time entry IDs separated by a comma.

**Type:** array

```json
[ "schema_type_none" ]
```

### until

ISO 8601 date (YYYY-MM-DD) format. Note: Maximum date span (until - since) is one year. Defaults to today, unless since is in future or more than year ago, in this case until is since + 6 days.

**Type:** string

### user_ids

A list of user IDs separated by a comma.

**Type:** array

```json
[ "schema_type_none" ]
```

### without_description

Filters out the time entries which do not have a description (literally "(no description)").

**Type:** boolean

</details>

## get_task

Get task details

<details><summary>Parameters</summary>

### task_id (required)

task ID

**Type:** integer

</details>

## get_time_entry

Get time entry details

<details><summary>Parameters</summary>

### time_entry_id (required)

time entry ID

**Type:** integer

</details>

## get_weekly_report

The weekly report gives aggregated 7 day durations or earnings grouped by users and projects.

<details><summary>Parameters</summary>

### user_agent (required)

The name of your application or your email address so we can get in touch in case you're doing something wrong.

**Type:** string

### workspace_id (required)

The workspace whose data you want to access.

**Type:** integer

### billable

**Type:** string

**Potential values:** yes, no, both

### calculate

**Type:** string

**Potential values:** time, earnings

### client_ids

A list of client IDs separated by a comma. Use "0" if you want to filter out time entries without a client.

**Type:** object

```json
{ }
```

### description

Matches against time entry descriptions.

**Type:** string

### display_hours

Determines whether to display hours as a decimal number or with minutes.

**Type:** string

**Potential values:** decimal, minutes

### distinct_rates

**Type:** string

**Potential values:** on, off

### grouping

**Type:** string

**Potential values:** users, projects

### members_of_group_ids

A list of group IDs separated by a comma. This limits provided user_ids to the members of the given groups.

**Type:** array

```json
[ "schema_type_none" ]
```

### or_members_of_group_ids

A list of group IDs separated by a comma. This extends provided user_ids with the members of the given groups.

**Type:** array

```json
[ "schema_type_none" ]
```

### order_desc

"on" for descending, or "off" for ascending order.

**Type:** string

**Potential values:** on, off

### order_field

**Type:** string

**Potential values:** title, day1, day2, day3, day4, day5, day6, day7, week_total

### project_ids

A list of project IDs separated by a comma. Use "0" if you want to filter out time entries without a project.

**Type:** object

```json
{ }
```

### rounding

Rounds time according to workspace settings.

**Type:** string

**Potential values:** on, off

### since

ISO 8601 date (YYYY-MM-DD) format. Defaults to today - 6 days.

**Type:** string

### tag_ids

A list of tag IDs separated by a comma. Use "0" if you want to filter out time entries without a tag.

**Type:** object

```json
{ }
```

### task_ids

A list of task IDs separated by a comma. Use "0" if you want to filter out time entries without a task.

**Type:** object

```json
{ }
```

### time_entry_ids

A list of time entry IDs separated by a comma.

**Type:** array

```json
[ "schema_type_none" ]
```

### user_ids

A list of user IDs separated by a comma.

**Type:** array

```json
[ "schema_type_none" ]
```

### without_description

Filters out the time entries which do not have a description (literally "(no description)").

**Type:** boolean

</details>

## get_workspace

Get single workspace

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

</details>

## invite_users_to_workspace

Invite users to workspace

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

### $body

**Type:** object

```json
{
  "emails" : [ "string" ]
}
```

</details>

## list_clients



*This operation has no parameters*

## list_clients_for_workspace

Get workspace clients

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_groups_for_workspace

Get workspace groups

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_projects_for_workspace

Get workspace projects

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_tags_for_workspace

Get workspace tags

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_tasks_for_project

List project tasks

<details><summary>Parameters</summary>

### project_id (required)

project ID

**Type:** integer

</details>

## list_tasks_for_workspace

Get workspace tasks

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_time_entries

Get time entries started in a specific time range. Default is last 9 days.

<details><summary>Parameters</summary>

### end_date

**Type:** string

### start_date

**Type:** string

</details>

## list_users_for_project

List project users

<details><summary>Parameters</summary>

### project_id (required)

project ID

**Type:** integer

</details>

## list_users_for_workspace

Get workspace users

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_workspace_users

Get workspace users. This request returns not the user objects, but the workspace_user objects (the connection between user and workspace)

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_workspaces



*This operation has no parameters*

## reset_api_token



*This operation has no parameters*

## sign_up_new_user

Sign up new user

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "user" : {
    "image_url" : "url with the user's profile picture",
    "timezone" : "timezone user has set on the \"My profile\" page ( IANA TZ timezones )",
    "api_token" : "API token",
    "timeofday_format" : "string",
    "beginning_of_week" : "(integer 0-6, Sunday=0)",
    "jquery_date_format" : "string",
    "send_weekly_report" : "if user receives weekly report",
    "language" : "user's language",
    "default_wid" : "default workspace id",
    "store_start_and_stop_time" : "whether start and stop time are saved on time entry",
    "password" : "password at least 6 characters long",
    "at" : "timestamp of last changes",
    "new_blog_post" : { },
    "openid_enabled" : "google signin enabled",
    "jquery_timeofday_format" : "string",
    "date_format" : "string",
    "send_timer_notifications" : "email user about long-running (more than 8 hours) tasks",
    "fullname" : "Full name of user",
    "email" : "Email address",
    "sidebar_piechart" : "should a piechart be shown on the sidebar",
    "send_product_emails" : "Toggl can send newsletters over e-mail to the user",
    "current_password" : "password at least 6 characters long"
  }
}
```

</details>

## start_time_entry

Start a time entry

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "time_entry" : {
    "duration" : "time entry duration in seconds. If the time entry is currently running, the duration attribute contains a negative value, denoting the start of the time entry in seconds since epoch (Jan 1 1970). The correct duration can be calculated as current_time + duration, where current_time is the current time in seconds since epoch.",
    "wid" : "workspace ID",
    "at" : "timestamp that is sent in the response, indicates the time item was last updated",
    "stop" : "time entry stop time, ISO 8601 date and time",
    "start" : "time entry start time, ISO 8601 date and time",
    "description" : "description",
    "pid" : "project ID",
    "created_with" : "the name of your client app",
    "billable" : "available for pro workspaces",
    "duronly" : "should Toggl show the start and stop time of this time entry?",
    "tid" : "task ID",
    "tags" : [ "string" ]
  }
}
```

</details>

## stop_time_entry

Stop a time entry

<details><summary>Parameters</summary>

### time_entry_id (required)

time entry ID

**Type:** integer

</details>

## update_client

Update a client

<details><summary>Parameters</summary>

### client_id (required)

client ID

**Type:** integer

### $body

**Type:** object

```json
{
  "client" : {
    "wid" : "workspace ID",
    "notes" : "notes for the client",
    "at" : "timestamp that is sent in the response",
    "name" : "name of the client"
  }
}
```

</details>

## update_group

Update a group

<details><summary>Parameters</summary>

### group_id (required)

group ID

**Type:** integer

### $body

**Type:** object

```json
{
  "group" : {
    "wid" : "workspace ID",
    "at" : "timestamp that is sent in the response",
    "name" : "name of the group"
  }
}
```

</details>

## update_multiple_users_for_project

Update multiple project users

<details><summary>Parameters</summary>

### project_user_ids (required)

multiple project user IDs

**Type:** array

```json
[ "schema_type_none" ]
```

### $body

**Type:** object

```json
{
  "project_user" : {
    "uid" : { },
    "wid" : "workspace ID",
    "at" : "timestamp that is sent in the response, indicates when the project user was last updated",
    "manager" : "admin rights for this project",
    "rate" : "hourly rate for the project user (only for pro workspaces) in the currency of the project's client or in workspace default currency.",
    "pid" : "project ID",
    "fields" : "fullname: full name of the user, who is added to the project"
  }
}
```

</details>

## update_project

Update project data

<details><summary>Parameters</summary>

### project_id (required)

project ID

**Type:** integer

### $body

**Type:** object

```json
{
  "project" : {
    "is_private" : "whether project is accessible for only project users or for all workspace users",
    "template" : "whether the project can be used as a template",
    "color" : "id of the color selected for the project",
    "active" : "whether the project is archived or not",
    "billable" : "whether the project is billable or not, available only for pro workspaces",
    "auto_estimates" : "whether the estimated hours are automatically calculated based on task estimations or manually fixed based on the value of 'estimated_hours', premium functionality",
    "wid" : "workspace ID",
    "at" : "timestamp indicating when the project was created (UTC time), read-only",
    "rate" : "hourly rate of the project, premium functionality",
    "name" : "name of the project",
    "estimated_hours" : "if auto_estimates is true then the sum of task estimations is returned, otherwise user inserted hours, premium functionality",
    "template_id" : "id of the template project used on current project's creation",
    "cid" : "client ID"
  }
}
```

</details>

## update_tag

Update a tag

<details><summary>Parameters</summary>

### tag_id (required)

tag ID

**Type:** integer

### $body

**Type:** object

```json
{
  "tag" : {
    "wid" : "workspace ID, where the tag will be used",
    "name" : "The name of the tag, unique in workspace"
  }
}
```

</details>

## update_task

Update one or more tasks

<details><summary>Parameters</summary>

### task_id (required)

multiple task IDs

**Type:** object

```json
{ }
```

### $body

**Type:** object

```json
{
  "task" : {
    "uid" : "user ID, to whom the task is assigned to",
    "wid" : "workspace ID",
    "at" : "timestamp that is sent in the response for PUT, indicates the time task was last updated",
    "estimated_seconds" : "estimated duration of task in seconds",
    "name" : "The name of the task",
    "active" : "whether the task is done or not",
    "pid" : "project ID for the task",
    "tracked_seconds" : "total time tracked (in seconds) for the task"
  }
}
```

</details>

## update_time_entry

Update a time entry (or multiple time entries)

<details><summary>Parameters</summary>

### time_entry_id (required)

one or more time entry IDs

**Type:** object

```json
{ }
```

### $body

**Type:** object

```json
{
  "time_entry" : {
    "duration" : "time entry duration in seconds. If the time entry is currently running, the duration attribute contains a negative value, denoting the start of the time entry in seconds since epoch (Jan 1 1970). The correct duration can be calculated as current_time + duration, where current_time is the current time in seconds since epoch.",
    "wid" : "workspace ID",
    "at" : "timestamp that is sent in the response, indicates the time item was last updated",
    "stop" : "time entry stop time, ISO 8601 date and time",
    "start" : "time entry start time, ISO 8601 date and time",
    "description" : "description",
    "pid" : "project ID",
    "created_with" : "the name of your client app",
    "billable" : "available for pro workspaces",
    "duronly" : "should Toggl show the start and stop time of this time entry?",
    "tid" : "task ID",
    "tags" : [ "string" ]
  }
}
```

</details>

## update_user_data

Update user data

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "user" : {
    "image_url" : "url with the user's profile picture",
    "timezone" : "timezone user has set on the \"My profile\" page ( IANA TZ timezones )",
    "api_token" : "API token",
    "timeofday_format" : "string",
    "beginning_of_week" : "(integer 0-6, Sunday=0)",
    "jquery_date_format" : "string",
    "send_weekly_report" : "if user receives weekly report",
    "language" : "user's language",
    "default_wid" : "default workspace id",
    "store_start_and_stop_time" : "whether start and stop time are saved on time entry",
    "password" : "password at least 6 characters long",
    "at" : "timestamp of last changes",
    "new_blog_post" : { },
    "openid_enabled" : "google signin enabled",
    "jquery_timeofday_format" : "string",
    "date_format" : "string",
    "send_timer_notifications" : "email user about long-running (more than 8 hours) tasks",
    "fullname" : "Full name of user",
    "email" : "Email address",
    "sidebar_piechart" : "should a piechart be shown on the sidebar",
    "send_product_emails" : "Toggl can send newsletters over e-mail to the user",
    "current_password" : "password at least 6 characters long"
  }
}
```

</details>

## update_user_for_project

Update a project user

<details><summary>Parameters</summary>

### project_user_id (required)

project user ID

**Type:** integer

### $body

**Type:** object

```json
{
  "project_user" : {
    "uid" : { },
    "wid" : "workspace ID",
    "at" : "timestamp that is sent in the response, indicates when the project user was last updated",
    "manager" : "admin rights for this project",
    "rate" : "hourly rate for the project user (only for pro workspaces) in the currency of the project's client or in workspace default currency.",
    "pid" : "project ID",
    "fields" : "fullname: full name of the user, who is added to the project"
  }
}
```

</details>

## update_workspace

Update workspace

<details><summary>Parameters</summary>

### workspace_id (required)

workspace ID

**Type:** integer

### $body

**Type:** object

```json
{
  "workspace" : {
    "premium" : "If it's a pro workspace or not. Shows if someone is paying for the workspace or not",
    "at" : "timestamp that indicates the time workspace was last updated",
    "only_admins_may_create_projects" : "whether only the admins can create projects or everybody",
    "logo_url" : "URL pointing to the logo (if set, otherwise omitted)",
    "rounding_minutes" : "round up to nearest minute",
    "name" : "the name of the workspace",
    "admin" : "shows whether currently requesting user has admin access to the workspace",
    "rounding" : "type of rounding: -1 = round down, 0 = nearest, 1 = round up",
    "only_admins_see_billable_rates" : "whether only the admins can see billable rates or everybody",
    "default_hourly_rate" : "default hourly rate for workspace, won't be shown to non-admins if the only_admins_see_billable_rates flag is set to true",
    "default_currency" : "default currency for workspace"
  }
}
```

</details>

## update_workspace_user

Update workspace user. Only the admin flag can be changed.

<details><summary>Parameters</summary>

### workspace_user_id (required)

workspace user ID

**Type:** integer

### $body

**Type:** object

```json
{
  "workspace_user" : {
    "uid" : "user id of the workspace user",
    "invite_url" : "if user has not accepted the invitation the url for accepting his/her invitation is sent when the request is made by workspace_admin",
    "admin" : "if user is workspace admin",
    "active" : "if the workspace user has accepted the invitation to this workspace",
    "id" : "workspace user id"
  }
}
```

</details>

