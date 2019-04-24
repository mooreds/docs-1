---
id: toggl-documentation
title: Toggl (version v1.*.*)
sidebar_label: Toggl
---

## create_client

Create a client

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_group

Create a group

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_project

Create a project

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_tag

Create tag

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_task

Create a task

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_time_entry

Create a time entry

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_user_for_project

Create a project user. To create multiple project users for a single project, you must add multiple user ids separated with a comma with the uid parameter.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_client

Delete a client

<details><summary>Parameters</summary>

#### client_id (required)

client ID

**Type:** integer

</details>

## delete_group

Delete a group

<details><summary>Parameters</summary>

#### group_id (required)

group ID

**Type:** integer

</details>

## delete_multiple_projects

Delete multiple projects

<details><summary>Parameters</summary>

#### project_ids (required)

multiple project IDs

**Type:** array

</details>

## delete_multiple_users_for_project

Delete multiple project users

<details><summary>Parameters</summary>

#### project_user_ids (required)

multiple project user IDs

**Type:** array

</details>

## delete_project

Delete a project

<details><summary>Parameters</summary>

#### project_id (required)

project ID

**Type:** integer

</details>

## delete_tag

Delete a tag

<details><summary>Parameters</summary>

#### tag_id (required)

tag ID

**Type:** integer

</details>

## delete_task

Delete a task

<details><summary>Parameters</summary>

#### task_id (required)

multiple task IDs

**Type:** object

</details>

## delete_time_entry

Delete a time entry

<details><summary>Parameters</summary>

#### time_entry_id (required)

time entry ID

**Type:** integer

</details>

## delete_user_for_project

Delete a project user

<details><summary>Parameters</summary>

#### project_user_id (required)

project user ID

**Type:** integer

</details>

## delete_workspace_user

Delete workspace user.

<details><summary>Parameters</summary>

#### workspace_user_id (required)

workspace user ID

**Type:** integer

</details>

## get_client

Get client details

<details><summary>Parameters</summary>

#### client_id (required)

client ID

**Type:** integer

</details>

## get_current_user_data

Get current user data

<details><summary>Parameters</summary>

#### since

retrieve objects which have changed after certain time. The value should be a unix timestamp.

**Type:** string

#### with_related_data

whether to get all the workspaces, clients, projects, tasks, time entries and tags which the user can see

**Type:** boolean

</details>

## get_dashboard_data

Get dashboard data. Dashboard's main purpose is to give an overview of what users in the workspace are doing and have been doing.

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

</details>

## get_detailed_report

The detailed report returns the time entries for the requested parameters/filters.

<details><summary>Parameters</summary>

#### user_agent (required)

The name of your application or your email address so we can get in touch in case you're doing something wrong.

**Type:** string

#### workspace_id (required)

The workspace whose data you want to access.

**Type:** integer

#### billable

**Type:** string

**Potential values:** yes, no, both

#### client_ids

A list of client IDs separated by a comma. Use "0" if you want to filter out time entries without a client.

**Type:** object

#### description

Matches against time entry descriptions.

**Type:** string

#### display_hours

Determines whether to display hours as a decimal number or with minutes.

**Type:** string

**Potential values:** decimal, minutes

#### distinct_rates

**Type:** string

**Potential values:** on, off

#### members_of_group_ids

A list of group IDs separated by a comma. This limits provided user_ids to the members of the given groups.

**Type:** array

#### or_members_of_group_ids

A list of group IDs separated by a comma. This extends provided user_ids with the members of the given groups.

**Type:** array

#### order_desc

"on" for descending, or "off" for ascending order.

**Type:** string

**Potential values:** on, off

#### order_field

**Type:** string

**Potential values:** date, description, duration, user

#### page

**Type:** integer

#### project_ids

A list of project IDs separated by a comma. Use "0" if you want to filter out time entries without a project.

**Type:** object

#### rounding

Rounds time according to workspace settings.

**Type:** string

**Potential values:** on, off

#### since

ISO 8601 date (YYYY-MM-DD) format. Defaults to today - 6 days.

**Type:** string

#### tag_ids

A list of tag IDs separated by a comma. Use "0" if you want to filter out time entries without a tag.

**Type:** object

#### task_ids

A list of task IDs separated by a comma. Use "0" if you want to filter out time entries without a task.

**Type:** object

#### time_entry_ids

A list of time entry IDs separated by a comma.

**Type:** array

#### until

ISO 8601 date (YYYY-MM-DD) format. Note: Maximum date span (until - since) is one year. Defaults to today, unless since is in future or more than year ago, in this case until is since + 6 days.

**Type:** string

#### user_ids

A list of user IDs separated by a comma.

**Type:** array

#### without_description

Filters out the time entries which do not have a description (literally "(no description)").

**Type:** boolean

</details>

## get_project

Get project data

<details><summary>Parameters</summary>

#### project_id (required)

project ID

**Type:** integer

</details>

## get_project_users_for_workspace

Get workspace project users

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

</details>

## get_projects_for_client

Get client projects

<details><summary>Parameters</summary>

#### client_id (required)

client ID

**Type:** integer

#### active

By default true. If false, only archived projects are returned.

**Type:** string

**Potential values:** true, false, both

</details>

## get_running_time_entry



*This operation has no parameters*

## get_summary_report

Summary report returns the aggregated time entries data. time entries for the requested

<details><summary>Parameters</summary>

#### user_agent (required)

The name of your application or your email address so we can get in touch in case you're doing something wrong.

**Type:** string

#### workspace_id (required)

The workspace whose data you want to access.

**Type:** integer

#### billable

**Type:** string

**Potential values:** yes, no, both

#### client_ids

A list of client IDs separated by a comma. Use "0" if you want to filter out time entries without a client.

**Type:** object

#### description

Matches against time entry descriptions.

**Type:** string

#### display_hours

Determines whether to display hours as a decimal number or with minutes.

**Type:** string

**Potential values:** decimal, minutes

#### distinct_rates

**Type:** string

**Potential values:** on, off

#### grouped_time_entry_ids

**Type:** boolean

#### grouping

**Type:** string

**Potential values:** projects, clients, users

#### members_of_group_ids

A list of group IDs separated by a comma. This limits provided user_ids to the members of the given groups.

**Type:** array

#### or_members_of_group_ids

A list of group IDs separated by a comma. This extends provided user_ids with the members of the given groups.

**Type:** array

#### order_desc

"on" for descending, or "off" for ascending order.

**Type:** string

**Potential values:** on, off

#### order_field

**Type:** string

**Potential values:** title, duration, amount

#### project_ids

A list of project IDs separated by a comma. Use "0" if you want to filter out time entries without a project.

**Type:** object

#### rounding

Rounds time according to workspace settings.

**Type:** string

**Potential values:** on, off

#### since

ISO 8601 date (YYYY-MM-DD) format. Defaults to today - 6 days.

**Type:** string

#### subgrouping

**Type:** string

**Potential values:** time_entries, tasks, users, projects, clients

#### subgrouping_ids

**Type:** boolean

#### tag_ids

A list of tag IDs separated by a comma. Use "0" if you want to filter out time entries without a tag.

**Type:** object

#### task_ids

A list of task IDs separated by a comma. Use "0" if you want to filter out time entries without a task.

**Type:** object

#### time_entry_ids

A list of time entry IDs separated by a comma.

**Type:** array

#### until

ISO 8601 date (YYYY-MM-DD) format. Note: Maximum date span (until - since) is one year. Defaults to today, unless since is in future or more than year ago, in this case until is since + 6 days.

**Type:** string

#### user_ids

A list of user IDs separated by a comma.

**Type:** array

#### without_description

Filters out the time entries which do not have a description (literally "(no description)").

**Type:** boolean

</details>

## get_task

Get task details

<details><summary>Parameters</summary>

#### task_id (required)

task ID

**Type:** integer

</details>

## get_time_entry

Get time entry details

<details><summary>Parameters</summary>

#### time_entry_id (required)

time entry ID

**Type:** integer

</details>

## get_weekly_report

The weekly report gives aggregated 7 day durations or earnings grouped by users and projects.

<details><summary>Parameters</summary>

#### user_agent (required)

The name of your application or your email address so we can get in touch in case you're doing something wrong.

**Type:** string

#### workspace_id (required)

The workspace whose data you want to access.

**Type:** integer

#### billable

**Type:** string

**Potential values:** yes, no, both

#### calculate

**Type:** string

**Potential values:** time, earnings

#### client_ids

A list of client IDs separated by a comma. Use "0" if you want to filter out time entries without a client.

**Type:** object

#### description

Matches against time entry descriptions.

**Type:** string

#### display_hours

Determines whether to display hours as a decimal number or with minutes.

**Type:** string

**Potential values:** decimal, minutes

#### distinct_rates

**Type:** string

**Potential values:** on, off

#### grouping

**Type:** string

**Potential values:** users, projects

#### members_of_group_ids

A list of group IDs separated by a comma. This limits provided user_ids to the members of the given groups.

**Type:** array

#### or_members_of_group_ids

A list of group IDs separated by a comma. This extends provided user_ids with the members of the given groups.

**Type:** array

#### order_desc

"on" for descending, or "off" for ascending order.

**Type:** string

**Potential values:** on, off

#### order_field

**Type:** string

**Potential values:** title, day1, day2, day3, day4, day5, day6, day7, week_total

#### project_ids

A list of project IDs separated by a comma. Use "0" if you want to filter out time entries without a project.

**Type:** object

#### rounding

Rounds time according to workspace settings.

**Type:** string

**Potential values:** on, off

#### since

ISO 8601 date (YYYY-MM-DD) format. Defaults to today - 6 days.

**Type:** string

#### tag_ids

A list of tag IDs separated by a comma. Use "0" if you want to filter out time entries without a tag.

**Type:** object

#### task_ids

A list of task IDs separated by a comma. Use "0" if you want to filter out time entries without a task.

**Type:** object

#### time_entry_ids

A list of time entry IDs separated by a comma.

**Type:** array

#### user_ids

A list of user IDs separated by a comma.

**Type:** array

#### without_description

Filters out the time entries which do not have a description (literally "(no description)").

**Type:** boolean

</details>

## get_workspace

Get single workspace

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

</details>

## invite_users_to_workspace

Invite users to workspace

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

#### $body

**Type:** object

</details>

## list_clients



*This operation has no parameters*

## list_clients_for_workspace

Get workspace clients

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_groups_for_workspace

Get workspace groups

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_projects_for_workspace

Get workspace projects

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_tags_for_workspace

Get workspace tags

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_tasks_for_project

List project tasks

<details><summary>Parameters</summary>

#### project_id (required)

project ID

**Type:** integer

</details>

## list_tasks_for_workspace

Get workspace tasks

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_time_entries

Get time entries started in a specific time range. Default is last 9 days.

<details><summary>Parameters</summary>

#### end_date

**Type:** string

#### start_date

**Type:** string

</details>

## list_users_for_project

List project users

<details><summary>Parameters</summary>

#### project_id (required)

project ID

**Type:** integer

</details>

## list_users_for_workspace

Get workspace users

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

</details>

## list_workspace_users

Get workspace users. This request returns not the user objects, but the workspace_user objects (the connection between user and workspace)

<details><summary>Parameters</summary>

#### workspace_id (required)

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

#### $body

**Type:** object

</details>

## start_time_entry

Start a time entry

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## stop_time_entry

Stop a time entry

<details><summary>Parameters</summary>

#### time_entry_id (required)

time entry ID

**Type:** integer

</details>

## update_client

Update a client

<details><summary>Parameters</summary>

#### client_id (required)

client ID

**Type:** integer

#### $body

**Type:** object

</details>

## update_group

Update a group

<details><summary>Parameters</summary>

#### group_id (required)

group ID

**Type:** integer

#### $body

**Type:** object

</details>

## update_multiple_users_for_project

Update multiple project users

<details><summary>Parameters</summary>

#### project_user_ids (required)

multiple project user IDs

**Type:** array

#### $body

**Type:** object

</details>

## update_project

Update project data

<details><summary>Parameters</summary>

#### project_id (required)

project ID

**Type:** integer

#### $body

**Type:** object

</details>

## update_tag

Update a tag

<details><summary>Parameters</summary>

#### tag_id (required)

tag ID

**Type:** integer

#### $body

**Type:** object

</details>

## update_task

Update one or more tasks

<details><summary>Parameters</summary>

#### task_id (required)

multiple task IDs

**Type:** object

#### $body

**Type:** object

</details>

## update_time_entry

Update a time entry (or multiple time entries)

<details><summary>Parameters</summary>

#### time_entry_id (required)

one or more time entry IDs

**Type:** object

#### $body

**Type:** object

</details>

## update_user_data

Update user data

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## update_user_for_project

Update a project user

<details><summary>Parameters</summary>

#### project_user_id (required)

project user ID

**Type:** integer

#### $body

**Type:** object

</details>

## update_workspace

Update workspace

<details><summary>Parameters</summary>

#### workspace_id (required)

workspace ID

**Type:** integer

#### $body

**Type:** object

</details>

## update_workspace_user

Update workspace user. Only the admin flag can be changed.

<details><summary>Parameters</summary>

#### workspace_user_id (required)

workspace user ID

**Type:** integer

#### $body

**Type:** object

</details>

