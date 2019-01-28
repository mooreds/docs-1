---
id: pagerduty-documentation
title: PagerDuty (version v1.*.*)
---

## delete_addons_by_id

Remove an existing add-on.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_escalation_policies_by_id

Deletes an existing escalation policy and rules. The escalation policy must not be in use by any services.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_extensions_by_id

Delete an existing extension. Once the extension is deleted, it will not be accessible from the web UI and new incidents won't be able to be created for this extension.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_maintenance_windows_by_id

Delete an existing maintenance window if it's in the future, or end it if it's currently on-going. If the maintenance window has already ended it cannot be deleted.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_schedules_by_id

Delete an on-call schedule.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_schedules_by_id_overrides_by_override_id

Remove an override. You cannot remove a past override. If the override start time is before the current time, but the end time is after the current time, the override will be truncated to the current time. If the override is truncated, the status code will be 200 OK, as opposed to a 204 No Content for a successful delete.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### override_id (required)

The override ID on the schedule.

**Type:** string

</details>

## delete_services_by_id

Delete an existing service. Once the service is deleted, it will not be accessible from the web UI and new incidents won't be able to be created for this service.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_teams_by_id

Remove an existing team.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_teams_by_id_escalation_policies_by_escalation_policy_id

Remove an escalation policy from a team.

<details><summary>Parameters</summary>

#### escalation_policy_id (required)

The escalation policy ID on the team.

**Type:** string

#### id (required)

**Type:** string

</details>

## delete_teams_by_id_users_by_user_id

Remove a user from a team.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### user_id (required)

The user ID on the team.

**Type:** string

</details>

## delete_users_by_id

Remove an existing user.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## delete_users_by_id_contact_methods_by_contact_method_id

Remove a user's contact method.

<details><summary>Parameters</summary>

#### contact_method_id (required)

The contact method ID on the user.

**Type:** string

#### id (required)

**Type:** string

</details>

## delete_users_by_id_notification_rules_by_notification_rule_id

Remove a user's notification rule.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### notification_rule_id (required)

The notification rule ID on the user.

**Type:** string

</details>

## get_abilities



*This operation has no parameters*

## get_abilities_by_id

Test whether your account has a given ability.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_addons

List all of the add-ons installed on your account.

<details><summary>Parameters</summary>

#### filter

Filters the results, showing only add-ons of the given type

**Type:** string

**Potential values:** full_page_addon, incident_show_addon

#### include[]

Array of additional details to include.

**Type:** array

#### service_ids[]

Filters the results, showing only add-ons for the given services

**Type:** array

</details>

## get_addons_by_id

Get details about an existing add-on.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_api_reference



*This operation has no parameters*

## get_escalation_policies

List all of the existing escalation policies.

<details><summary>Parameters</summary>

#### include[]

Array of additional details to include.

**Type:** array

#### query

Filters the results, showing only the escalation policies whose names contain the query.

**Type:** string

#### sort_by

Used to specify the field you wish to sort the results on.

**Type:** string

**Potential values:** name, name:asc, name:desc

#### team_ids[]

An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.

**Type:** array

#### user_ids[]

Filters the results, showing only escalation policies on which any of the users is a target.

**Type:** array

</details>

## get_escalation_policies_by_id

Get information about an existing escalation policy and its rules.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

</details>

## get_extension_schemas

List all extension schemas.

*This operation has no parameters*

## get_extension_schemas_by_id

Get details about one specific extension vendor.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_extensions

List existing extensions.

<details><summary>Parameters</summary>

#### extension_object_id

The id of the extension object you want to filter by.

**Type:** string

#### extension_schema_id

Filter the extensions by extension vendor id.

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

#### query

Filters the result, showing only the extensions whose name matches the query.

**Type:** string

</details>

## get_extensions_by_id

Get details about an existing extension.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

</details>

## get_incidents

List existing incidents.

<details><summary>Parameters</summary>

#### date_range

When set to all, the since and until parameters and defaults are ignored.

**Type:** string

**Potential values:** all

#### incident_key

Incident de-duplication key. Incidents with child alerts do not have an incident key; querying by incident key will return incidents whose alerts have alert_key matching the given incident key.

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

#### service_ids[]

Returns only the incidents associated with the passed service(s). This expects one or more service IDs.

**Type:** array

#### since

The start of the date range over which you want to search.

**Type:** date-time

#### sort_by

Used to specify both the field you wish to sort the results on (incident_number/created_at/resolved_at/urgency), as well as the direction (asc/desc) of the results. The sort_by field and direction should be separated by a colon. A maximum of two fields can be included, separated by a comma. Sort direction defaults to ascending. The account must have the `urgencies` ability to sort by the urgency.

**Type:** array

#### statuses[]

Return only incidents with the given statuses. (More status codes may be introduced in the future.)

**Type:** array

#### team_ids[]

An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.

**Type:** array

#### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

#### until

The end of the date range over which you want to search.

**Type:** date-time

#### urgencies[]

Array of the urgencies of the incidents to be returned. Defaults to all urgencies. Account must have the `urgencies` ability to do this.

**Type:** array

#### user_ids[]

Returns only the incidents currently assigned to the passed user(s). This expects one or more user IDs. Note: When using the assigned_to_user filter, you will only receive incidents with statuses of triggered or acknowledged. This is because resolved incidents are not assigned to any user.

**Type:** array

</details>

## get_incidents_by_id

Show detailed information about an incident. Accepts either an incident id, or an incident number.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_incidents_by_id_alerts

List alerts for the specified incident.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### alert_key

Alert de-duplication key.

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

#### sort_by

Used to specify both the field you wish to sort the results on (created_at/resolved_at), as well as the direction (asc/desc) of the results. The sort_by field and direction should be separated by a colon. A maximum of two fields can be included, separated by a comma. Sort direction defaults to ascending.

**Type:** array

#### statuses[]

Return only alerts with the given statuses. (More status codes may be introduced in the future.)

**Type:** array

</details>

## get_incidents_by_id_alerts_by_alert_id

Show detailed information about an alert. Accepts an alert id.

<details><summary>Parameters</summary>

#### alert_id (required)

The id of the alert to retrieve.

**Type:** string

#### id (required)

**Type:** string

</details>

## get_incidents_by_id_log_entries

List log entries for the specified incident.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

#### is_overview

If `true`, will return a subset of log entries that show only the most important changes to the incident.

**Type:** boolean

#### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

</details>

## get_incidents_by_id_notes

List existing notes for the specified incident.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_log_entries

List all of the incident log entries across the entire account.

<details><summary>Parameters</summary>

#### include[]

Array of additional details to include.

**Type:** array

#### is_overview

If `true`, will return a subset of log entries that show only the most important changes to the incident.

**Type:** boolean

#### since

The start of the date range over which you want to search.

**Type:** date-time

#### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

#### until

The end of the date range over which you want to search.

**Type:** date-time

</details>

## get_log_entries_by_id

Get details for a specific incident log entry. This method provides additional information you can use to get at raw event data.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

#### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

</details>

## get_maintenance_windows

List existing maintenance windows, optionally filtered by service and/or team, or whether they are from the past, present or future.

<details><summary>Parameters</summary>

#### filter

Only return maintenance windows in a given state.

**Type:** string

**Potential values:** past, future, ongoing, open, all

#### include[]

Array of additional details to include.

**Type:** array

#### query

Filters the results, showing only the maintenance windows whose descriptions contain the query.

**Type:** string

#### service_ids[]

An array of service IDs. Only results related to these services will be returned.

**Type:** array

#### team_ids[]

An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.

**Type:** array

</details>

## get_maintenance_windows_by_id

Get an existing maintenance window.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

</details>

## get_notifications

List notifications for a given time range, optionally filtered by type (sms_notification, email_notification, phone_notification, or push_notification).

<details><summary>Parameters</summary>

#### since (required)

The start of the date range over which you want to search. The time element is optional.

**Type:** date-time

#### until (required)

The end of the date range over which you want to search. This should be in the same format as since. The size of the date range must be less than 3 months.

**Type:** date-time

#### filter

Return notification of this type only.

**Type:** string

**Potential values:** sms_notification, email_notification, phone_notification, push_notification

#### include[]

Array of additional details to include.

**Type:** array

#### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

</details>

## get_oncalls

List the on-call entries during a given time range.

<details><summary>Parameters</summary>

#### earliest

This will filter on-calls such that only the earliest on-call for each combination of escalation policy, escalation level, and user is returned. This is useful for determining when the "next" on-calls are for a given set of filters.

**Type:** boolean

#### escalation_policy_ids[]

Filters the results, showing only on-calls for the specified escalation policy IDs.

**Type:** array

#### include[]

Array of additional details to include.

**Type:** array

#### schedule_ids[]

Filters the results, showing only on-calls for the specified schedule IDs. If `null` is provided in the array, it includes permanent on-calls due to direct user escalation targets.

**Type:** array

#### since

The start of the time range over which you want to search. If an on-call period overlaps with the range, it will be included in the result. Defaults to current time. The search range cannot exceed 3 months.

**Type:** date-time

#### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

#### until

The end of the time range over which you want to search. If an on-call period overlaps with the range, it will be included in the result. Defaults to current time. The search range cannot exceed 3 months, and the `until` time cannot be before the `since` time.

**Type:** date-time

#### user_ids[]

Filters the results, showing only on-calls for the specified user IDs.

**Type:** array

</details>

## get_priorities

List existing priorities, in order (most to least severe).

*This operation has no parameters*

## get_schedules

List the on-call schedules.

<details><summary>Parameters</summary>

#### query

Filters the result, showing only the schedules whose name matches the query.

**Type:** string

</details>

## get_schedules_by_id

Show detailed information about a schedule, including entries for each layer and sub-schedule.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### since

The start of the date range over which you want to search.

**Type:** date-time

#### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

#### until

The end of the date range over which you want to search.

**Type:** date-time

</details>

## get_schedules_by_id_overrides

List overrides for a given time range.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### since (required)

The start of the date range over which you want to search.

**Type:** date-time

#### until (required)

The end of the date range over which you want to search.

**Type:** date-time

#### editable

When this parameter is present, only editable overrides will be returned. The result will only include the id of the override if this parameter is present. Only future overrides are editable.

**Type:** boolean

#### overflow

Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter overflow=true is passed. This parameter defaults to false.

**Type:** boolean

</details>

## get_schedules_by_id_users

List all of the users on call in a given schedule for a given time range.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### since

The start of the date range over which you want to search.

**Type:** date-time

#### until

The end of the date range over which you want to search.

**Type:** date-time

</details>

## get_services

List existing services.

<details><summary>Parameters</summary>

#### include[]

Array of additional details to include.

**Type:** array

#### query

Filters the result, showing only the services whose name or service_key matches the query.

**Type:** string

#### sort_by

Used to specify the field you wish to sort the results on.

**Type:** string

**Potential values:** name, name:asc, name:desc

#### team_ids[]

An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.

**Type:** array

#### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

</details>

## get_services_by_id

Get details about an existing service.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

</details>

## get_services_by_id_integrations_by_integration_id

Get details about an integration belonging to a service.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### integration_id (required)

The integration ID on the service.

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

</details>

## get_teams

List teams of your PagerDuty account, optionally filtered by a search query.

<details><summary>Parameters</summary>

#### query

Filters the result, showing only the teams whose names or email addresses match the query.

**Type:** string

</details>

## get_teams_by_id

Get details about an existing team.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_users

List users of your PagerDuty account, optionally filtered by a search query.

<details><summary>Parameters</summary>

#### include[]

Array of additional details to include.

**Type:** array

#### query

Filters the result, showing only the users whose names or email addresses match the query.

**Type:** string

#### team_ids[]

An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.

**Type:** array

</details>

## get_users_by_id

Get details about an existing user.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

</details>

## get_users_by_id_contact_methods

List contact methods of your PagerDuty user.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## get_users_by_id_contact_methods_by_contact_method_id

Get details about a user's contact method.

<details><summary>Parameters</summary>

#### contact_method_id (required)

The contact method ID on the user.

**Type:** string

#### id (required)

**Type:** string

</details>

## get_users_by_id_notification_rules

List notification rules of your PagerDuty user.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

</details>

## get_users_by_id_notification_rules_by_notification_rule_id

Get details about a user's notification rule.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### notification_rule_id (required)

The notification rule ID on the user.

**Type:** string

#### include[]

Array of additional details to include.

**Type:** array

</details>

## get_vendors

List all vendors.

*This operation has no parameters*

## get_vendors_by_id

Get details about one specific vendor.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

</details>

## post_addons

Install an add-on for your account.

<details><summary>Parameters</summary>

#### $body

The add-on to be installed.

**Type:** object

</details>

## post_escalation_policies

Creates a new escalation policy. There must be at least one existing escalation rule added to create a new escalation policy.

<details><summary>Parameters</summary>

#### $body

The escalation policy to be created.

**Type:** object

#### From

The email address of a valid user associated with the account making the request. This is optional, and is only used for change tracking.

**Type:** email

</details>

## post_extensions

Create a new extension.

<details><summary>Parameters</summary>

#### $body

The extension to be created

**Type:** object

</details>

## post_incidents

Create an incident synchronously without a corresponding event from a monitoring service.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### $body

**Type:** object

</details>

## post_incidents_by_id_notes

Create a new note for the specified incident.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## post_incidents_by_id_snooze

Snooze an incident.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## post_incidents_by_id_status_updates

Create a new status update for the specified incident.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## post_maintenance_windows

Create a new maintenance window for the specified services. No new incidents will be created for a service that is in maintenance.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### $body

The maintenance window object.

**Type:** object

</details>

## post_schedules

Create a new on-call schedule.

<details><summary>Parameters</summary>

#### $body

The schedule to be created.

**Type:** object

#### overflow

Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter `overflow=true` is passed. This parameter defaults to false.
For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from `2011-06-01T10:00:00Z` to `2011-06-01T14:00:00Z`:

- If you don't pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T10:00:00Z` and end of `2011-06-01T14:00:00Z`.
- If you do pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T00:00:00Z` and end of `2011-06-02T00:00:00Z`.


**Type:** boolean

</details>

## post_schedules_by_id_overrides

Create an override for a specific user covering the specified time range. If you create an override on top of an existing one, the last created override will have priority.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The override to be created

**Type:** object

</details>

## post_schedules_preview

Preview what an on-call schedule would look like without saving it.

<details><summary>Parameters</summary>

#### $body

The schedule to be previewed.

**Type:** object

#### overflow

Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter `overflow=true` is passed. This parameter defaults to false.
For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from `2011-06-01T10:00:00Z` to `2011-06-01T14:00:00Z`:

- If you don't pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T10:00:00Z` and end of `2011-06-01T14:00:00Z`.
- If you do pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T00:00:00Z` and end of `2011-06-02T00:00:00Z`.


**Type:** boolean

#### since

The start of the date range over which you want to search.

**Type:** date-time

#### until

The end of the date range over which you want to search.

**Type:** date-time

</details>

## post_services

Create a new service.

<details><summary>Parameters</summary>

#### $body

The service to be created

**Type:** object

</details>

## post_services_by_id_integrations

Create a new integration belonging to a service.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The integration to be created

**Type:** object

</details>

## post_teams

Create a new team.

<details><summary>Parameters</summary>

#### $body

The team to be created.

**Type:** object

</details>

## post_users

Create a new user. Note that you must also supply a `password` property to create a user--it will not be returned by any API.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### $body

The user to be created.

**Type:** object

</details>

## post_users_by_id_contact_methods

Create a new contact method.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The contact method to be created.

**Type:** object

</details>

## post_users_by_id_notification_rules

Create a new notification rule.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The notification rule to be created.

**Type:** object

</details>

## put_addons_by_id

Update an existing add-on.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The add-on to be updated.

**Type:** object

</details>

## put_escalation_policies_by_id

Updates an existing escalation policy and rules.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The escalation policy to be updated.

**Type:** object

</details>

## put_extensions_by_id

Update an existing extension.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The extension to be updated.

**Type:** object

</details>

## put_incidents

Acknowledge, resolve, escalate or reassign one or more incidents.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### $body

**Type:** object

</details>

## put_incidents_by_id

Acknowledge, resolve, escalate or reassign an incident.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## put_incidents_by_id_alerts

Resolve multiple alerts or associate them with different incidents.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## put_incidents_by_id_alerts_by_alert_id

Resolve an alert or associate an alert with a new parent incident.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### alert_id (required)

The id of the alert to update.

**Type:** string

#### id (required)

**Type:** string

#### $body

The parameters of the alert to update.

**Type:** object

</details>

## put_incidents_by_id_merge

Merge a list of source incidents into this incident.

<details><summary>Parameters</summary>

#### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

#### id (required)

**Type:** string

#### $body

**Type:** object

</details>

## put_maintenance_windows_by_id

Update an existing maintenance window.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The maintenance window to be updated.

**Type:** object

</details>

## put_schedules_by_id

Update an existing on-call schedule.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The schedule to be updated.

**Type:** object

#### overflow

Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter `overflow=true` is passed. This parameter defaults to false.
For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from `2011-06-01T10:00:00Z` to `2011-06-01T14:00:00Z`:

- If you don't pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T10:00:00Z` and end of `2011-06-01T14:00:00Z`.
- If you do pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T00:00:00Z` and end of `2011-06-02T00:00:00Z`.


**Type:** boolean

</details>

## put_services_by_id

Update an existing service.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The service to be updated.

**Type:** object

</details>

## put_services_by_id_integrations_by_integration_id

Update an integration belonging to a service.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### integration_id (required)

The integration ID on the service.

**Type:** string

#### $body

The integration to be updated

**Type:** object

</details>

## put_teams_by_id

Update an existing team.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The team to be updated.

**Type:** object

</details>

## put_teams_by_id_escalation_policies_by_escalation_policy_id

Add an escalation policy to a team.

<details><summary>Parameters</summary>

#### escalation_policy_id (required)

The escalation policy ID on the team.

**Type:** string

#### id (required)

**Type:** string

</details>

## put_teams_by_id_users_by_user_id

Add a user to a team. Attempting to add a user with the `read_only_user` role will return a 400 error.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### user_id (required)

The user ID on the team.

**Type:** string

</details>

## put_users_by_id

Update an existing user. Note that you may also supply a `password` property--it will not be returned by any API.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### $body

The user to be updated.

**Type:** object

</details>

## put_users_by_id_contact_methods_by_contact_method_id

Update a user's contact method.

<details><summary>Parameters</summary>

#### contact_method_id (required)

The contact method ID on the user.

**Type:** string

#### id (required)

**Type:** string

#### $body

The user's contact method to be updated.

**Type:** object

</details>

## put_users_by_id_notification_rules_by_notification_rule_id

Update a user's notification rule.

<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### notification_rule_id (required)

The notification rule ID on the user.

**Type:** string

#### $body

The user's notification rule to be updated.

**Type:** object

</details>

