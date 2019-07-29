---
id: pagerduty-documentation
title: PagerDuty (version v1.*.*)
sidebar_label: PagerDuty
layout: docs.mustache
---

## delete_addons_by_id

Remove an existing add-on.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## delete_escalation_policies_by_id

Deletes an existing escalation policy and rules. The escalation policy must not be in use by any services.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## delete_extensions_by_id

Delete an existing extension. Once the extension is deleted, it will not be accessible from the web UI and new incidents won't be able to be created for this extension.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## delete_maintenance_windows_by_id

Delete an existing maintenance window if it's in the future, or end it if it's currently on-going. If the maintenance window has already ended it cannot be deleted.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## delete_schedules_by_id

Delete an on-call schedule.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## delete_schedules_by_id_overrides_by_override_id

Remove an override. You cannot remove a past override. If the override start time is before the current time, but the end time is after the current time, the override will be truncated to the current time. If the override is truncated, the status code will be 200 OK, as opposed to a 204 No Content for a successful delete.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### override_id (required)

The override ID on the schedule.

**Type:** string

</details>

## delete_services_by_id

Delete an existing service. Once the service is deleted, it will not be accessible from the web UI and new incidents won't be able to be created for this service.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## delete_teams_by_id

Remove an existing team.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## delete_teams_by_id_escalation_policies_by_escalation_policy_id

Remove an escalation policy from a team.

<details><summary>Parameters</summary>

### escalation_policy_id (required)

The escalation policy ID on the team.

**Type:** string

### id (required)

**Type:** string

</details>

## delete_teams_by_id_users_by_user_id

Remove a user from a team.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### user_id (required)

The user ID on the team.

**Type:** string

</details>

## delete_users_by_id

Remove an existing user.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## delete_users_by_id_contact_methods_by_contact_method_id

Remove a user's contact method.

<details><summary>Parameters</summary>

### contact_method_id (required)

The contact method ID on the user.

**Type:** string

### id (required)

**Type:** string

</details>

## delete_users_by_id_notification_rules_by_notification_rule_id

Remove a user's notification rule.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### notification_rule_id (required)

The notification rule ID on the user.

**Type:** string

</details>

## get_abilities



*This operation has no parameters*

## get_abilities_by_id

Test whether your account has a given ability.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## get_addons

List all of the add-ons installed on your account.

<details><summary>Parameters</summary>

### filter

Filters the results, showing only add-ons of the given type

**Type:** string

**Potential values:** full_page_addon, incident_show_addon

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### service_ids[]

Filters the results, showing only add-ons for the given services

**Type:** array

```json
[ "string" ]
```

</details>

## get_addons_by_id

Get details about an existing add-on.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## get_api_reference



*This operation has no parameters*

## get_escalation_policies

List all of the existing escalation policies.

<details><summary>Parameters</summary>

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### query

Filters the results, showing only the escalation policies whose names contain the query.

**Type:** string

### sort_by

Used to specify the field you wish to sort the results on.

**Type:** string

**Potential values:** name, name:asc, name:desc

### team_ids[]

An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.

**Type:** array

```json
[ "string" ]
```

### user_ids[]

Filters the results, showing only escalation policies on which any of the users is a target.

**Type:** array

```json
[ "string" ]
```

</details>

## get_escalation_policies_by_id

Get information about an existing escalation policy and its rules.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

</details>

## get_extension_schemas

List all extension schemas.

*This operation has no parameters*

## get_extension_schemas_by_id

Get details about one specific extension vendor.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## get_extensions

List existing extensions.

<details><summary>Parameters</summary>

### extension_object_id

The id of the extension object you want to filter by.

**Type:** string

### extension_schema_id

Filter the extensions by extension vendor id.

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### query

Filters the result, showing only the extensions whose name matches the query.

**Type:** string

</details>

## get_extensions_by_id

Get details about an existing extension.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

</details>

## get_incidents

List existing incidents.

<details><summary>Parameters</summary>

### date_range

When set to all, the since and until parameters and defaults are ignored.

**Type:** string

**Potential values:** all

### incident_key

Incident de-duplication key. Incidents with child alerts do not have an incident key; querying by incident key will return incidents whose alerts have alert_key matching the given incident key.

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### service_ids[]

Returns only the incidents associated with the passed service(s). This expects one or more service IDs.

**Type:** array

```json
[ "string" ]
```

### since

The start of the date range over which you want to search.

**Type:** date-time

### sort_by

Used to specify both the field you wish to sort the results on (incident_number/created_at/resolved_at/urgency), as well as the direction (asc/desc) of the results. The sort_by field and direction should be separated by a colon. A maximum of two fields can be included, separated by a comma. Sort direction defaults to ascending. The account must have the `urgencies` ability to sort by the urgency.

**Type:** array

```json
[ "string" ]
```

### statuses[]

Return only incidents with the given statuses. (More status codes may be introduced in the future.)

**Type:** array

```json
[ "string" ]
```

### team_ids[]

An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.

**Type:** array

```json
[ "string" ]
```

### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

### until

The end of the date range over which you want to search.

**Type:** date-time

### urgencies[]

Array of the urgencies of the incidents to be returned. Defaults to all urgencies. Account must have the `urgencies` ability to do this.

**Type:** array

```json
[ "string" ]
```

### user_ids[]

Returns only the incidents currently assigned to the passed user(s). This expects one or more user IDs. Note: When using the assigned_to_user filter, you will only receive incidents with statuses of triggered or acknowledged. This is because resolved incidents are not assigned to any user.

**Type:** array

```json
[ "string" ]
```

</details>

## get_incidents_by_id

Show detailed information about an incident. Accepts either an incident id, or an incident number.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## get_incidents_by_id_alerts

List alerts for the specified incident.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### alert_key

Alert de-duplication key.

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string. Possible values: services | first_trigger_log_entries | incidents" ]
```

### sort_by

Used to specify both the field you wish to sort the results on (created_at/resolved_at), as well as the direction (asc/desc) of the results. The sort_by field and direction should be separated by a colon. A maximum of two fields can be included, separated by a comma. Sort direction defaults to ascending.

**Type:** array

```json
[ "string. Possible values: created_at | resolved_at | created_at:asc | created_at:desc | resolved_at:asc | resolved_at:desc" ]
```

### statuses[]

Return only alerts with the given statuses. (More status codes may be introduced in the future.)

**Type:** array

```json
[ "string" ]
```

</details>

## get_incidents_by_id_alerts_by_alert_id

Show detailed information about an alert. Accepts an alert id.

<details><summary>Parameters</summary>

### alert_id (required)

The id of the alert to retrieve.

**Type:** string

### id (required)

**Type:** string

</details>

## get_incidents_by_id_log_entries

List log entries for the specified incident.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### is_overview

If `true`, will return a subset of log entries that show only the most important changes to the incident.

**Type:** boolean

### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

</details>

## get_incidents_by_id_notes

List existing notes for the specified incident.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## get_log_entries

List all of the incident log entries across the entire account.

<details><summary>Parameters</summary>

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### is_overview

If `true`, will return a subset of log entries that show only the most important changes to the incident.

**Type:** boolean

### since

The start of the date range over which you want to search.

**Type:** date-time

### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

### until

The end of the date range over which you want to search.

**Type:** date-time

</details>

## get_log_entries_by_id

Get details for a specific incident log entry. This method provides additional information you can use to get at raw event data.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

</details>

## get_maintenance_windows

List existing maintenance windows, optionally filtered by service and/or team, or whether they are from the past, present or future.

<details><summary>Parameters</summary>

### filter

Only return maintenance windows in a given state.

**Type:** string

**Potential values:** past, future, ongoing, open, all

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### query

Filters the results, showing only the maintenance windows whose descriptions contain the query.

**Type:** string

### service_ids[]

An array of service IDs. Only results related to these services will be returned.

**Type:** array

```json
[ "string" ]
```

### team_ids[]

An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.

**Type:** array

```json
[ "string" ]
```

</details>

## get_maintenance_windows_by_id

Get an existing maintenance window.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

</details>

## get_notifications

List notifications for a given time range, optionally filtered by type (sms_notification, email_notification, phone_notification, or push_notification).

<details><summary>Parameters</summary>

### since (required)

The start of the date range over which you want to search. The time element is optional.

**Type:** date-time

### until (required)

The end of the date range over which you want to search. This should be in the same format as since. The size of the date range must be less than 3 months.

**Type:** date-time

### filter

Return notification of this type only.

**Type:** string

**Potential values:** sms_notification, email_notification, phone_notification, push_notification

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

</details>

## get_oncalls

List the on-call entries during a given time range.

<details><summary>Parameters</summary>

### earliest

This will filter on-calls such that only the earliest on-call for each combination of escalation policy, escalation level, and user is returned. This is useful for determining when the "next" on-calls are for a given set of filters.

**Type:** boolean

### escalation_policy_ids[]

Filters the results, showing only on-calls for the specified escalation policy IDs.

**Type:** array

```json
[ "string" ]
```

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### schedule_ids[]

Filters the results, showing only on-calls for the specified schedule IDs. If `null` is provided in the array, it includes permanent on-calls due to direct user escalation targets.

**Type:** array

```json
[ "string" ]
```

### since

The start of the time range over which you want to search. If an on-call period overlaps with the range, it will be included in the result. Defaults to current time. The search range cannot exceed 3 months.

**Type:** date-time

### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

### until

The end of the time range over which you want to search. If an on-call period overlaps with the range, it will be included in the result. Defaults to current time. The search range cannot exceed 3 months, and the `until` time cannot be before the `since` time.

**Type:** date-time

### user_ids[]

Filters the results, showing only on-calls for the specified user IDs.

**Type:** array

```json
[ "string" ]
```

</details>

## get_priorities

List existing priorities, in order (most to least severe).

*This operation has no parameters*

## get_schedules

List the on-call schedules.

<details><summary>Parameters</summary>

### query

Filters the result, showing only the schedules whose name matches the query.

**Type:** string

</details>

## get_schedules_by_id

Show detailed information about a schedule, including entries for each layer and sub-schedule.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### since

The start of the date range over which you want to search.

**Type:** date-time

### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

### until

The end of the date range over which you want to search.

**Type:** date-time

</details>

## get_schedules_by_id_overrides

List overrides for a given time range.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### since (required)

The start of the date range over which you want to search.

**Type:** date-time

### until (required)

The end of the date range over which you want to search.

**Type:** date-time

### editable

When this parameter is present, only editable overrides will be returned. The result will only include the id of the override if this parameter is present. Only future overrides are editable.

**Type:** boolean

### overflow

Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter overflow=true is passed. This parameter defaults to false.

**Type:** boolean

</details>

## get_schedules_by_id_users

List all of the users on call in a given schedule for a given time range.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### since

The start of the date range over which you want to search.

**Type:** date-time

### until

The end of the date range over which you want to search.

**Type:** date-time

</details>

## get_services

List existing services.

<details><summary>Parameters</summary>

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### query

Filters the result, showing only the services whose name or service_key matches the query.

**Type:** string

### sort_by

Used to specify the field you wish to sort the results on.

**Type:** string

**Potential values:** name, name:asc, name:desc

### team_ids[]

An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.

**Type:** array

```json
[ "string" ]
```

### time_zone

Time zone in which dates in the result will be rendered.

**Type:** tzinfo

</details>

## get_services_by_id

Get details about an existing service.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

</details>

## get_services_by_id_integrations_by_integration_id

Get details about an integration belonging to a service.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### integration_id (required)

The integration ID on the service.

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

</details>

## get_teams

List teams of your PagerDuty account, optionally filtered by a search query.

<details><summary>Parameters</summary>

### query

Filters the result, showing only the teams whose names or email addresses match the query.

**Type:** string

</details>

## get_teams_by_id

Get details about an existing team.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## get_users

List users of your PagerDuty account, optionally filtered by a search query.

<details><summary>Parameters</summary>

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

### query

Filters the result, showing only the users whose names or email addresses match the query.

**Type:** string

### team_ids[]

An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.

**Type:** array

```json
[ "string" ]
```

</details>

## get_users_by_id

Get details about an existing user.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

</details>

## get_users_by_id_contact_methods

List contact methods of your PagerDuty user.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## get_users_by_id_contact_methods_by_contact_method_id

Get details about a user's contact method.

<details><summary>Parameters</summary>

### contact_method_id (required)

The contact method ID on the user.

**Type:** string

### id (required)

**Type:** string

</details>

## get_users_by_id_notification_rules

List notification rules of your PagerDuty user.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

</details>

## get_users_by_id_notification_rules_by_notification_rule_id

Get details about a user's notification rule.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### notification_rule_id (required)

The notification rule ID on the user.

**Type:** string

### include[]

Array of additional details to include.

**Type:** array

```json
[ "string" ]
```

</details>

## get_vendors

List all vendors.

*This operation has no parameters*

## get_vendors_by_id

Get details about one specific vendor.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

</details>

## post_addons

Install an add-on for your account.

<details><summary>Parameters</summary>

### $body

The add-on to be installed.

**Type:** object

```json
{
  "addon" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: full_page_addon | full_page_addon_reference | incident_show_addon | incident_show_addon_reference",
    "src" : "The source URL to display in a frame in the PagerDuty UI. HTTPS is required.",
    "name" : "The name of the add-on."
  }
}
```

</details>

## post_escalation_policies

Creates a new escalation policy. There must be at least one existing escalation rule added to create a new escalation policy.

<details><summary>Parameters</summary>

### $body

The escalation policy to be created.

**Type:** object

```json
{
  "escalation_policy" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: escalation_policy | escalation_policy_reference",
    "repeat_enabled" : "Whether or not to allow this policy to repeat its escalation rules after the last rule is finished.",
    "teams" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: team | team_reference"
    } ],
    "name" : "The name of the escalation policy.",
    "description" : "Escalation policy description.",
    "services" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    } ],
    "num_loops" : "The number of times the escalation policy will repeat after reaching the end of its escalation.",
    "escalation_rules" : [ {
      "escalation_delay_in_minutes" : "The number of minutes before an unacknowledged incident escalates away from this rule.",
      "id" : "string",
      "targets" : [ {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "string. Possible values: user | schedule | user_reference | schedule_reference"
      } ]
    } ]
  }
}
```

### From

The email address of a valid user associated with the account making the request. This is optional, and is only used for change tracking.

**Type:** email

</details>

## post_extensions

Create a new extension.

<details><summary>Parameters</summary>

### $body

The extension to be created

**Type:** object

```json
{
  "extension" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: extension | extension_reference",
    "endpoint_url" : "The url of the extension.",
    "extension_schema" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: extension_schema | extension_schema_reference"
    },
    "name" : "The name of the extension.",
    "extension_objects" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    } ]
  }
}
```

</details>

## post_incidents

Create an incident synchronously without a corresponding event from a monitoring service.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### $body

**Type:** object

```json
{
  "incident" : {
    "assignments" : [ {
      "assignee" : {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "string. Possible values: user | user_reference"
      }
    } ],
    "urgency" : "The urgency of the incident",
    "service" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    },
    "incident_key" : "A string which identifies the incident. Sending subsequent requests referencing the same service and with the same incident_key will result in those requests being rejected if an open incident matches that incident_key.",
    "type" : "Required string. Possible values: incident",
    "title" : "A succinct description of the nature, symptoms, cause, or effect of the incident.",
    "priority" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: priority | priority_reference"
    },
    "body" : {
      "details" : "Additional incident details.",
      "type" : "Required string. Possible values: incident_body"
    },
    "escalation_policy" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: escalation_policy | escalation_policy_reference"
    }
  }
}
```

</details>

## post_incidents_by_id_notes

Create a new note for the specified incident.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "note" : {
    "created_at" : "The time at which the note was submitted",
    "id" : "string",
    "user" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: user | user_reference"
    },
    "content" : "The note content"
  }
}
```

</details>

## post_incidents_by_id_snooze

Snooze an incident.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "duration" : "The number of seconds to snooze the incident for. After this number of seconds has elapsed, the incident will return to the \"triggered\" state."
}
```

</details>

## post_incidents_by_id_status_updates

Create a new status update for the specified incident.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "message" : "The message to be posted as a status update."
}
```

</details>

## post_maintenance_windows

Create a new maintenance window for the specified services. No new incidents will be created for a service that is in maintenance.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### $body

The maintenance window object.

**Type:** object

```json
{
  "maintenance_window" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: maintenance_window | maintenance_window_reference",
    "sequence_number" : "The order in which the maintenance window was created.",
    "start_time" : "This maintenance window's start time. This is when the services will stop creating incidents. If this date is in the past, it will be updated to be the current time.",
    "teams" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: team | team_reference"
    } ],
    "end_time" : "This maintenance window's end time. This is when the services will start creating incidents again. This date must be in the future and after the `start_time`.",
    "description" : "A description for this maintenance window.",
    "services" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    } ],
    "created_by" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: user | user_reference"
    }
  }
}
```

</details>

## post_schedules

Create a new on-call schedule.

<details><summary>Parameters</summary>

### $body

The schedule to be created.

**Type:** object

```json
{
  "schedule" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: schedule | schedule_reference",
    "final_schedule" : {
      "name" : "The name of the subschedule",
      "rendered_schedule_entries" : [ {
        "start" : "The start time of this entry.",
        "end" : "The end time of this entry. If null, the entry does not end.",
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ],
      "rendered_coverage_percentage" : "The percentage of the time range covered by this layer. Returns null unless since or until are set."
    },
    "schedule_layers" : [ {
      "start" : "The start time of this layer.",
      "rotation_turn_length_seconds" : "The duration of each on-call shift in seconds.",
      "name" : "The name of the schedule layer.",
      "restrictions" : [ {
        "duration_seconds" : "The duration of the restriction in seconds.",
        "start_day_of_week" : "Only required for use with a `weekly_restriction` restriction type. The first day of the weekly rotation schedule as [ISO 8601 day](https://en.wikipedia.org/wiki/ISO_week_date) (1 is Monday, etc.)",
        "type" : "Specify the types of `restriction`.",
        "start_time_of_day" : "The start time in HH:mm:ss format."
      } ],
      "end" : "The end time of this layer. If `null`, the layer does not end.",
      "id" : "string",
      "rendered_schedule_entries" : [ {
        "start" : "The start time of this entry.",
        "end" : "The end time of this entry. If null, the entry does not end.",
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ],
      "rendered_coverage_percentage" : "The percentage of the time range covered by this layer. Returns null unless since or until are set.",
      "rotation_virtual_start" : "The effective start time of the layer. This can be before the start time of the schedule.",
      "users" : [ {
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ]
    } ],
    "name" : "The name of the schedule",
    "overrides_subschedule" : {
      "name" : "The name of the subschedule",
      "rendered_schedule_entries" : [ {
        "start" : "The start time of this entry.",
        "end" : "The end time of this entry. If null, the entry does not end.",
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ],
      "rendered_coverage_percentage" : "The percentage of the time range covered by this layer. Returns null unless since or until are set."
    },
    "description" : "The description of the schedule",
    "escalation_policies" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: escalation_policy | escalation_policy_reference"
    } ],
    "time_zone" : "The time zone of the schedule.",
    "users" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: user | user_reference"
    } ]
  }
}
```

### overflow

Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter `overflow=true` is passed. This parameter defaults to false.
For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from `2011-06-01T10:00:00Z` to `2011-06-01T14:00:00Z`:

- If you don't pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T10:00:00Z` and end of `2011-06-01T14:00:00Z`.
- If you do pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T00:00:00Z` and end of `2011-06-02T00:00:00Z`.


**Type:** boolean

</details>

## post_schedules_by_id_overrides

Create an override for a specific user covering the specified time range. If you create an override on top of an existing one, the last created override will have priority.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The override to be created

**Type:** object

```json
{
  "override" : {
    "start" : "The start date and time for the override.",
    "end" : "The end date and time for the override.",
    "id" : "string",
    "user" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: user | user_reference"
    }
  }
}
```

</details>

## post_schedules_preview

Preview what an on-call schedule would look like without saving it.

<details><summary>Parameters</summary>

### $body

The schedule to be previewed.

**Type:** object

```json
{
  "schedule" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: schedule | schedule_reference",
    "final_schedule" : {
      "name" : "The name of the subschedule",
      "rendered_schedule_entries" : [ {
        "start" : "The start time of this entry.",
        "end" : "The end time of this entry. If null, the entry does not end.",
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ],
      "rendered_coverage_percentage" : "The percentage of the time range covered by this layer. Returns null unless since or until are set."
    },
    "schedule_layers" : [ {
      "start" : "The start time of this layer.",
      "rotation_turn_length_seconds" : "The duration of each on-call shift in seconds.",
      "name" : "The name of the schedule layer.",
      "restrictions" : [ {
        "duration_seconds" : "The duration of the restriction in seconds.",
        "start_day_of_week" : "Only required for use with a `weekly_restriction` restriction type. The first day of the weekly rotation schedule as [ISO 8601 day](https://en.wikipedia.org/wiki/ISO_week_date) (1 is Monday, etc.)",
        "type" : "Specify the types of `restriction`.",
        "start_time_of_day" : "The start time in HH:mm:ss format."
      } ],
      "end" : "The end time of this layer. If `null`, the layer does not end.",
      "id" : "string",
      "rendered_schedule_entries" : [ {
        "start" : "The start time of this entry.",
        "end" : "The end time of this entry. If null, the entry does not end.",
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ],
      "rendered_coverage_percentage" : "The percentage of the time range covered by this layer. Returns null unless since or until are set.",
      "rotation_virtual_start" : "The effective start time of the layer. This can be before the start time of the schedule.",
      "users" : [ {
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ]
    } ],
    "name" : "The name of the schedule",
    "overrides_subschedule" : {
      "name" : "The name of the subschedule",
      "rendered_schedule_entries" : [ {
        "start" : "The start time of this entry.",
        "end" : "The end time of this entry. If null, the entry does not end.",
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ],
      "rendered_coverage_percentage" : "The percentage of the time range covered by this layer. Returns null unless since or until are set."
    },
    "description" : "The description of the schedule",
    "escalation_policies" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: escalation_policy | escalation_policy_reference"
    } ],
    "time_zone" : "The time zone of the schedule.",
    "users" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: user | user_reference"
    } ]
  }
}
```

### overflow

Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter `overflow=true` is passed. This parameter defaults to false.
For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from `2011-06-01T10:00:00Z` to `2011-06-01T14:00:00Z`:

- If you don't pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T10:00:00Z` and end of `2011-06-01T14:00:00Z`.
- If you do pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T00:00:00Z` and end of `2011-06-02T00:00:00Z`.


**Type:** boolean

### since

The start of the date range over which you want to search.

**Type:** date-time

### until

The end of the date range over which you want to search.

**Type:** date-time

</details>

## post_services

Create a new service.

<details><summary>Parameters</summary>

### $body

The service to be created

**Type:** object

```json
{
  "service" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: service | service_reference",
    "teams" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: team | team_reference"
    } ],
    "addons" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: full_page_addon | full_page_addon_reference | incident_show_addon | incident_show_addon_reference"
    } ],
    "incident_urgency_rule" : {
      "urgency" : "The incidents' urgency, if type is constant.",
      "type" : "The type of incident urgency: whether it's constant, or it's dependent on the support hours.",
      "outside_support_hours" : {
        "urgency" : "The incidents' urgency, if type is constant.",
        "type" : "The type of incident urgency: whether it's constant, or it's dependent on the support hours."
      },
      "during_support_hours" : {
        "urgency" : "The incidents' urgency, if type is constant.",
        "type" : "The type of incident urgency: whether it's constant, or it's dependent on the support hours."
      }
    },
    "description" : "The user-provided description of the service.",
    "created_at" : "The date/time when this service was created",
    "alert_creation" : "Whether a service creates only incidents, or both alerts and incidents. A service must create alerts in order to enable incident merging.\n* \"create_incidents\" - The service will create one incident and zero alerts for each incoming event.\n* \"create_alerts_and_incidents\" - The service will create one incident and one associated alert for each incoming event.\n",
    "escalation_policy" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: escalation_policy | escalation_policy_reference"
    },
    "acknowledgement_timeout" : "Time in seconds that an incident changes to the Triggered State after being Acknowledged. Value is `null` if the feature is disabled. Value must not be negative. Setting this field to `0`, `null` (or unset in POST request) will disable the feature.",
    "scheduled_actions" : [ {
      "at" : {
        "name" : "Designates either the start or the end of support hours.",
        "type" : "Must be set to named_time."
      },
      "to_urgency" : "Urgency level. Must be set to high.",
      "type" : "The type of schedule action. Must be set to urgency_change."
    } ],
    "support_hours" : {
      "days_of_week" : [ "The days of the week (1 through 7, for Monday through Sunday)" ],
      "start_time" : "The support hours' starting time of day (date portion is ignored)",
      "end_time" : "The support hours' ending time of day (date portion is ignored)",
      "type" : "The type of support hours",
      "time_zone" : "The time zone for the support hours"
    },
    "name" : "The name of the service.",
    "integrations" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: aws_cloudwatch_inbound_integration | aws_cloudwatch_inbound_integration_reference | cloudkick_inbound_integration | cloudkick_inbound_integration_reference | event_transformer_api_inbound_integration | event_transformer_api_inbound_integration_reference | generic_email_inbound_integration | generic_email_inbound_integration_reference | generic_events_api_inbound_integration | generic_events_api_inbound_integration_reference | keynote_inbound_integration | keynote_inbound_integration_reference | nagios_inbound_integration | nagios_inbound_integration_reference | pingdom_inbound_integration | pingdom_inbound_integration_reference | sql_monitor_inbound_integration | sql_monitor_inbound_integration_reference"
    } ],
    "auto_resolve_timeout" : "Time in seconds that an incident is automatically resolved if left open for that long. Value is `null` if the feature is disabled. Value must not be negative. Setting this field to `0`, `null` (or unset in POST request) will disable the feature.",
    "status" : "The current state of the Service. Valid statuses are:\n\n- `active`: The service is enabled and has no open incidents.\n- `warning`: The service is enabled and has one or more acknowledged incidents.\n- `critical`: The service is enabled and has one or more triggered incidents.\n- `maintenance`: The service is under maintenance, no new incidents will be triggered during maintenance mode.\n- `disabled`: The service is disabled and will not have any new triggered incidents.\n",
    "last_incident_timestamp" : "The date/time when the most recent incident was created for this service."
  }
}
```

</details>

## post_services_by_id_integrations

Create a new integration belonging to a service.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The integration to be created

**Type:** object

```json
{
  "integration" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: aws_cloudwatch_inbound_integration | aws_cloudwatch_inbound_integration_reference | cloudkick_inbound_integration | cloudkick_inbound_integration_reference | event_transformer_api_inbound_integration | event_transformer_api_inbound_integration_reference | generic_email_inbound_integration | generic_email_inbound_integration_reference | generic_events_api_inbound_integration | generic_events_api_inbound_integration_reference | keynote_inbound_integration | keynote_inbound_integration_reference | nagios_inbound_integration | nagios_inbound_integration_reference | pingdom_inbound_integration | pingdom_inbound_integration_reference | sql_monitor_inbound_integration | sql_monitor_inbound_integration_reference",
    "service" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    },
    "vendor" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: vendor | vendor_reference"
    },
    "name" : "The name of this integration.",
    "created_at" : "The date/time when this integration was created."
  }
}
```

</details>

## post_teams

Create a new team.

<details><summary>Parameters</summary>

### $body

The team to be created.

**Type:** object

```json
{
  "team" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: team | team_reference",
    "name" : "The name of the team.",
    "description" : "The description of the team."
  }
}
```

</details>

## post_users

Create a new user. Note that you must also supply a `password` property to create a user--it will not be returned by any API.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### $body

The user to be created.

**Type:** object

```json
{
  "user" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: user | user_reference",
    "role" : "The user role. Account must have the `read_only_users` ability to set a user as a `read_only_user`, and must have the `permissions_service` ability to set a user as `observer` or `restricted_access`.",
    "color" : "The schedule color.",
    "avatar_url" : "The URL of the user's avatar.",
    "teams" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: team | team_reference"
    } ],
    "notification_rules" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "The type of notification rule.",
      "start_delay_in_minutes" : "The delay before firing the rule, in minutes.",
      "contact_method" : {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "The type of contact method."
      },
      "urgency" : "Which incident urgency this rule is used for. Account must have the `urgencies` ability to have a low urgency notification rule."
    } ],
    "invitation_sent" : "If true, the user has an outstanding invitation.",
    "contact_methods" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "The type of contact method."
    } ],
    "name" : "The name of the user.",
    "description" : "The user's bio.",
    "time_zone" : "The preferred time zone name. If null, the account's time zone will be used.",
    "job_title" : "The user's title.",
    "email" : "The user's email address."
  }
}
```

</details>

## post_users_by_id_contact_methods

Create a new contact method.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The contact method to be created.

**Type:** object

```json
{
  "contact_method" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "The type of contact method.",
    "address" : "The \"address\" to deliver to: email, phone number, etc., depending on the type.",
    "label" : "The label (e.g., \"Work\", \"Mobile\", etc.)."
  }
}
```

</details>

## post_users_by_id_notification_rules

Create a new notification rule.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The notification rule to be created.

**Type:** object

```json
{
  "notification_rule" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "The type of notification rule.",
    "start_delay_in_minutes" : "The delay before firing the rule, in minutes.",
    "contact_method" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "The type of contact method."
    },
    "urgency" : "Which incident urgency this rule is used for. Account must have the `urgencies` ability to have a low urgency notification rule."
  }
}
```

</details>

## put_addons_by_id

Update an existing add-on.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The add-on to be updated.

**Type:** object

```json
{
  "addon" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: full_page_addon | full_page_addon_reference | incident_show_addon | incident_show_addon_reference",
    "src" : "The source URL to display in a frame in the PagerDuty UI. HTTPS is required.",
    "name" : "The name of the add-on."
  }
}
```

</details>

## put_escalation_policies_by_id

Updates an existing escalation policy and rules.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The escalation policy to be updated.

**Type:** object

```json
{
  "escalation_policy" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: escalation_policy | escalation_policy_reference",
    "repeat_enabled" : "Whether or not to allow this policy to repeat its escalation rules after the last rule is finished.",
    "teams" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: team | team_reference"
    } ],
    "name" : "The name of the escalation policy.",
    "description" : "Escalation policy description.",
    "services" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    } ],
    "num_loops" : "The number of times the escalation policy will repeat after reaching the end of its escalation.",
    "escalation_rules" : [ {
      "escalation_delay_in_minutes" : "The number of minutes before an unacknowledged incident escalates away from this rule.",
      "id" : "string",
      "targets" : [ {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "string. Possible values: user | schedule | user_reference | schedule_reference"
      } ]
    } ]
  }
}
```

</details>

## put_extensions_by_id

Update an existing extension.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The extension to be updated.

**Type:** object

```json
{
  "extension" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: extension | extension_reference",
    "endpoint_url" : "The url of the extension.",
    "extension_schema" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: extension_schema | extension_schema_reference"
    },
    "name" : "The name of the extension.",
    "extension_objects" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    } ]
  }
}
```

</details>

## put_incidents

Acknowledge, resolve, escalate or reassign one or more incidents.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### $body

**Type:** object

```json
{
  "incidents" : [ {
    "assignments" : [ {
      "assignee" : {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "string. Possible values: user | user_reference"
      }
    } ],
    "id" : "The id of the incident to update.",
    "type" : "The incident type.",
    "title" : "A succinct description of the nature, symptoms, cause, or effect of the incident.",
    "priority" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: priority | priority_reference"
    },
    "escalation_policy" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: escalation_policy | escalation_policy_reference"
    },
    "resolution" : "The resolution for this incident if status is set to resolved.",
    "escalation_level" : "Escalate the incident to this level in the escalation policy.",
    "status" : "The new status of the incident."
  } ]
}
```

</details>

## put_incidents_by_id

Acknowledge, resolve, escalate or reassign an incident.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "incident" : {
    "assignments" : [ {
      "assignee" : {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "string. Possible values: user | user_reference"
      }
    } ],
    "urgency" : "The urgency of the incident.",
    "type" : "The incident type.",
    "priority" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: priority | priority_reference"
    },
    "title" : "The new title of the incident.",
    "escalation_policy" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: escalation_policy | escalation_policy_reference"
    },
    "resolution" : "The resolution for this incident if status is set to resolved.",
    "escalation_level" : "Escalate the incident to this level in the escalation policy.",
    "status" : "The new status of the incident."
  }
}
```

</details>

## put_incidents_by_id_alerts

Resolve multiple alerts or associate them with different incidents.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "alerts" : [ {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: alert | alert_reference",
    "severity" : "The magnitude of the problem as reported by the monitoring tool.",
    "first_trigger_log_entry" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: acknowledge_log_entry | acknowledge_log_entry_reference | annotate_log_entry | annotate_log_entry_reference | assign_log_entry | assign_log_entry_reference | escalate_log_entry | escalate_log_entry_reference | exhaust_escalation_path_log_entry | exhaust_escalation_path_log_entry_reference | notify_log_entry | notify_log_entry_reference | reach_trigger_limit_log_entry | reach_trigger_limit_log_entry_reference | repeat_escalation_path_log_entry | repeat_escalation_path_log_entry_reference | resolve_log_entry | resolve_log_entry_reference | snooze_log_entry | snooze_log_entry_reference | trigger_log_entry | trigger_log_entry_reference | unacknowledge_log_entry | unacknowledge_log_entry_reference"
    },
    "alert_key" : "The alert's de-duplication key.",
    "service" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    },
    "integration" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: aws_cloudwatch_inbound_integration | aws_cloudwatch_inbound_integration_reference | cloudkick_inbound_integration | cloudkick_inbound_integration_reference | event_transformer_api_inbound_integration | event_transformer_api_inbound_integration_reference | generic_email_inbound_integration | generic_email_inbound_integration_reference | generic_events_api_inbound_integration | generic_events_api_inbound_integration_reference | keynote_inbound_integration | keynote_inbound_integration_reference | nagios_inbound_integration | nagios_inbound_integration_reference | pingdom_inbound_integration | pingdom_inbound_integration_reference | sql_monitor_inbound_integration | sql_monitor_inbound_integration_reference",
      "service" : {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "string. Possible values: service | service_reference"
      },
      "vendor" : {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "string. Possible values: vendor | vendor_reference"
      },
      "name" : "The name of this integration.",
      "created_at" : "The date/time when this integration was created."
    },
    "created_at" : "The date/time the alert was first triggered.",
    "suppressed" : "Whether or not an alert is suppressed. Suppressed alerts are not created with a parent incident.",
    "body" : {
      "details" : { },
      "contexts" : [ {
        "src" : "The image's source url",
        "href" : "The link's target url",
        "text" : "The alternate display for an image",
        "type" : "The type of context being attached to the incident."
      } ],
      "type" : "The type of the body."
    },
    "incident" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: incident | incident_reference"
    },
    "status" : "The current status of the alert."
  } ]
}
```

</details>

## put_incidents_by_id_alerts_by_alert_id

Resolve an alert or associate an alert with a new parent incident.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### alert_id (required)

The id of the alert to update.

**Type:** string

### id (required)

**Type:** string

### $body

The parameters of the alert to update.

**Type:** object

```json
{
  "alert" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: alert | alert_reference",
    "severity" : "The magnitude of the problem as reported by the monitoring tool.",
    "first_trigger_log_entry" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: acknowledge_log_entry | acknowledge_log_entry_reference | annotate_log_entry | annotate_log_entry_reference | assign_log_entry | assign_log_entry_reference | escalate_log_entry | escalate_log_entry_reference | exhaust_escalation_path_log_entry | exhaust_escalation_path_log_entry_reference | notify_log_entry | notify_log_entry_reference | reach_trigger_limit_log_entry | reach_trigger_limit_log_entry_reference | repeat_escalation_path_log_entry | repeat_escalation_path_log_entry_reference | resolve_log_entry | resolve_log_entry_reference | snooze_log_entry | snooze_log_entry_reference | trigger_log_entry | trigger_log_entry_reference | unacknowledge_log_entry | unacknowledge_log_entry_reference"
    },
    "alert_key" : "The alert's de-duplication key.",
    "service" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    },
    "integration" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: aws_cloudwatch_inbound_integration | aws_cloudwatch_inbound_integration_reference | cloudkick_inbound_integration | cloudkick_inbound_integration_reference | event_transformer_api_inbound_integration | event_transformer_api_inbound_integration_reference | generic_email_inbound_integration | generic_email_inbound_integration_reference | generic_events_api_inbound_integration | generic_events_api_inbound_integration_reference | keynote_inbound_integration | keynote_inbound_integration_reference | nagios_inbound_integration | nagios_inbound_integration_reference | pingdom_inbound_integration | pingdom_inbound_integration_reference | sql_monitor_inbound_integration | sql_monitor_inbound_integration_reference",
      "service" : {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "string. Possible values: service | service_reference"
      },
      "vendor" : {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "string. Possible values: vendor | vendor_reference"
      },
      "name" : "The name of this integration.",
      "created_at" : "The date/time when this integration was created."
    },
    "created_at" : "The date/time the alert was first triggered.",
    "suppressed" : "Whether or not an alert is suppressed. Suppressed alerts are not created with a parent incident.",
    "body" : {
      "details" : { },
      "contexts" : [ {
        "src" : "The image's source url",
        "href" : "The link's target url",
        "text" : "The alternate display for an image",
        "type" : "The type of context being attached to the incident."
      } ],
      "type" : "The type of the body."
    },
    "incident" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: incident | incident_reference"
    },
    "status" : "The current status of the alert."
  }
}
```

</details>

## put_incidents_by_id_merge

Merge a list of source incidents into this incident.

<details><summary>Parameters</summary>

### From (required)

The email address of a valid user associated with the account making the request.

**Type:** email

### id (required)

**Type:** string

### $body

**Type:** object

```json
{
  "source_incidents" : [ {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: incident | incident_reference"
  } ]
}
```

</details>

## put_maintenance_windows_by_id

Update an existing maintenance window.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The maintenance window to be updated.

**Type:** object

```json
{
  "maintenance_window" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: maintenance_window | maintenance_window_reference",
    "sequence_number" : "The order in which the maintenance window was created.",
    "start_time" : "This maintenance window's start time. This is when the services will stop creating incidents. If this date is in the past, it will be updated to be the current time.",
    "teams" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: team | team_reference"
    } ],
    "end_time" : "This maintenance window's end time. This is when the services will start creating incidents again. This date must be in the future and after the `start_time`.",
    "description" : "A description for this maintenance window.",
    "services" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    } ],
    "created_by" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: user | user_reference"
    }
  }
}
```

</details>

## put_schedules_by_id

Update an existing on-call schedule.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The schedule to be updated.

**Type:** object

```json
{
  "schedule" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: schedule | schedule_reference",
    "final_schedule" : {
      "name" : "The name of the subschedule",
      "rendered_schedule_entries" : [ {
        "start" : "The start time of this entry.",
        "end" : "The end time of this entry. If null, the entry does not end.",
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ],
      "rendered_coverage_percentage" : "The percentage of the time range covered by this layer. Returns null unless since or until are set."
    },
    "schedule_layers" : [ {
      "start" : "The start time of this layer.",
      "rotation_turn_length_seconds" : "The duration of each on-call shift in seconds.",
      "name" : "The name of the schedule layer.",
      "restrictions" : [ {
        "duration_seconds" : "The duration of the restriction in seconds.",
        "start_day_of_week" : "Only required for use with a `weekly_restriction` restriction type. The first day of the weekly rotation schedule as [ISO 8601 day](https://en.wikipedia.org/wiki/ISO_week_date) (1 is Monday, etc.)",
        "type" : "Specify the types of `restriction`.",
        "start_time_of_day" : "The start time in HH:mm:ss format."
      } ],
      "end" : "The end time of this layer. If `null`, the layer does not end.",
      "id" : "string",
      "rendered_schedule_entries" : [ {
        "start" : "The start time of this entry.",
        "end" : "The end time of this entry. If null, the entry does not end.",
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ],
      "rendered_coverage_percentage" : "The percentage of the time range covered by this layer. Returns null unless since or until are set.",
      "rotation_virtual_start" : "The effective start time of the layer. This can be before the start time of the schedule.",
      "users" : [ {
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ]
    } ],
    "name" : "The name of the schedule",
    "overrides_subschedule" : {
      "name" : "The name of the subschedule",
      "rendered_schedule_entries" : [ {
        "start" : "The start time of this entry.",
        "end" : "The end time of this entry. If null, the entry does not end.",
        "user" : {
          "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
          "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
          "self" : "the API show URL at which the object is accessible",
          "id" : "string",
          "type" : "string. Possible values: user | user_reference"
        }
      } ],
      "rendered_coverage_percentage" : "The percentage of the time range covered by this layer. Returns null unless since or until are set."
    },
    "description" : "The description of the schedule",
    "escalation_policies" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: escalation_policy | escalation_policy_reference"
    } ],
    "time_zone" : "The time zone of the schedule.",
    "users" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: user | user_reference"
    } ]
  }
}
```

### overflow

Any on-call schedule entries that pass the date range bounds will be truncated at the bounds, unless the parameter `overflow=true` is passed. This parameter defaults to false.
For instance, if your schedule is a rotation that changes daily at midnight UTC, and your date range is from `2011-06-01T10:00:00Z` to `2011-06-01T14:00:00Z`:

- If you don't pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T10:00:00Z` and end of `2011-06-01T14:00:00Z`.
- If you do pass the `overflow=true` parameter, you will get one schedule entry returned with a start of `2011-06-01T00:00:00Z` and end of `2011-06-02T00:00:00Z`.


**Type:** boolean

</details>

## put_services_by_id

Update an existing service.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The service to be updated.

**Type:** object

```json
{
  "service" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: service | service_reference",
    "teams" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: team | team_reference"
    } ],
    "addons" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: full_page_addon | full_page_addon_reference | incident_show_addon | incident_show_addon_reference"
    } ],
    "incident_urgency_rule" : {
      "urgency" : "The incidents' urgency, if type is constant.",
      "type" : "The type of incident urgency: whether it's constant, or it's dependent on the support hours.",
      "outside_support_hours" : {
        "urgency" : "The incidents' urgency, if type is constant.",
        "type" : "The type of incident urgency: whether it's constant, or it's dependent on the support hours."
      },
      "during_support_hours" : {
        "urgency" : "The incidents' urgency, if type is constant.",
        "type" : "The type of incident urgency: whether it's constant, or it's dependent on the support hours."
      }
    },
    "description" : "The user-provided description of the service.",
    "created_at" : "The date/time when this service was created",
    "alert_creation" : "Whether a service creates only incidents, or both alerts and incidents. A service must create alerts in order to enable incident merging.\n* \"create_incidents\" - The service will create one incident and zero alerts for each incoming event.\n* \"create_alerts_and_incidents\" - The service will create one incident and one associated alert for each incoming event.\n",
    "escalation_policy" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: escalation_policy | escalation_policy_reference"
    },
    "acknowledgement_timeout" : "Time in seconds that an incident changes to the Triggered State after being Acknowledged. Value is `null` if the feature is disabled. Value must not be negative. Setting this field to `0`, `null` (or unset in POST request) will disable the feature.",
    "scheduled_actions" : [ {
      "at" : {
        "name" : "Designates either the start or the end of support hours.",
        "type" : "Must be set to named_time."
      },
      "to_urgency" : "Urgency level. Must be set to high.",
      "type" : "The type of schedule action. Must be set to urgency_change."
    } ],
    "support_hours" : {
      "days_of_week" : [ "The days of the week (1 through 7, for Monday through Sunday)" ],
      "start_time" : "The support hours' starting time of day (date portion is ignored)",
      "end_time" : "The support hours' ending time of day (date portion is ignored)",
      "type" : "The type of support hours",
      "time_zone" : "The time zone for the support hours"
    },
    "name" : "The name of the service.",
    "integrations" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: aws_cloudwatch_inbound_integration | aws_cloudwatch_inbound_integration_reference | cloudkick_inbound_integration | cloudkick_inbound_integration_reference | event_transformer_api_inbound_integration | event_transformer_api_inbound_integration_reference | generic_email_inbound_integration | generic_email_inbound_integration_reference | generic_events_api_inbound_integration | generic_events_api_inbound_integration_reference | keynote_inbound_integration | keynote_inbound_integration_reference | nagios_inbound_integration | nagios_inbound_integration_reference | pingdom_inbound_integration | pingdom_inbound_integration_reference | sql_monitor_inbound_integration | sql_monitor_inbound_integration_reference"
    } ],
    "auto_resolve_timeout" : "Time in seconds that an incident is automatically resolved if left open for that long. Value is `null` if the feature is disabled. Value must not be negative. Setting this field to `0`, `null` (or unset in POST request) will disable the feature.",
    "status" : "The current state of the Service. Valid statuses are:\n\n- `active`: The service is enabled and has no open incidents.\n- `warning`: The service is enabled and has one or more acknowledged incidents.\n- `critical`: The service is enabled and has one or more triggered incidents.\n- `maintenance`: The service is under maintenance, no new incidents will be triggered during maintenance mode.\n- `disabled`: The service is disabled and will not have any new triggered incidents.\n",
    "last_incident_timestamp" : "The date/time when the most recent incident was created for this service."
  }
}
```

</details>

## put_services_by_id_integrations_by_integration_id

Update an integration belonging to a service.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### integration_id (required)

The integration ID on the service.

**Type:** string

### $body

The integration to be updated

**Type:** object

```json
{
  "integration" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: aws_cloudwatch_inbound_integration | aws_cloudwatch_inbound_integration_reference | cloudkick_inbound_integration | cloudkick_inbound_integration_reference | event_transformer_api_inbound_integration | event_transformer_api_inbound_integration_reference | generic_email_inbound_integration | generic_email_inbound_integration_reference | generic_events_api_inbound_integration | generic_events_api_inbound_integration_reference | keynote_inbound_integration | keynote_inbound_integration_reference | nagios_inbound_integration | nagios_inbound_integration_reference | pingdom_inbound_integration | pingdom_inbound_integration_reference | sql_monitor_inbound_integration | sql_monitor_inbound_integration_reference",
    "service" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: service | service_reference"
    },
    "vendor" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: vendor | vendor_reference"
    },
    "name" : "The name of this integration.",
    "created_at" : "The date/time when this integration was created."
  }
}
```

</details>

## put_teams_by_id

Update an existing team.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The team to be updated.

**Type:** object

```json
{
  "team" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: team | team_reference",
    "name" : "The name of the team.",
    "description" : "The description of the team."
  }
}
```

</details>

## put_teams_by_id_escalation_policies_by_escalation_policy_id

Add an escalation policy to a team.

<details><summary>Parameters</summary>

### escalation_policy_id (required)

The escalation policy ID on the team.

**Type:** string

### id (required)

**Type:** string

</details>

## put_teams_by_id_users_by_user_id

Add a user to a team. Attempting to add a user with the `read_only_user` role will return a 400 error.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### user_id (required)

The user ID on the team.

**Type:** string

</details>

## put_users_by_id

Update an existing user. Note that you may also supply a `password` property--it will not be returned by any API.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### $body

The user to be updated.

**Type:** object

```json
{
  "user" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "string. Possible values: user | user_reference",
    "role" : "The user role. Account must have the `read_only_users` ability to set a user as a `read_only_user`, and must have the `permissions_service` ability to set a user as `observer` or `restricted_access`.",
    "color" : "The schedule color.",
    "avatar_url" : "The URL of the user's avatar.",
    "teams" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "string. Possible values: team | team_reference"
    } ],
    "notification_rules" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "The type of notification rule.",
      "start_delay_in_minutes" : "The delay before firing the rule, in minutes.",
      "contact_method" : {
        "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
        "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
        "self" : "the API show URL at which the object is accessible",
        "id" : "string",
        "type" : "The type of contact method."
      },
      "urgency" : "Which incident urgency this rule is used for. Account must have the `urgencies` ability to have a low urgency notification rule."
    } ],
    "invitation_sent" : "If true, the user has an outstanding invitation.",
    "contact_methods" : [ {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "The type of contact method."
    } ],
    "name" : "The name of the user.",
    "description" : "The user's bio.",
    "time_zone" : "The preferred time zone name. If null, the account's time zone will be used.",
    "job_title" : "The user's title.",
    "email" : "The user's email address."
  }
}
```

</details>

## put_users_by_id_contact_methods_by_contact_method_id

Update a user's contact method.

<details><summary>Parameters</summary>

### contact_method_id (required)

The contact method ID on the user.

**Type:** string

### id (required)

**Type:** string

### $body

The user's contact method to be updated.

**Type:** object

```json
{
  "contact_method" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "The type of contact method.",
    "address" : "The \"address\" to deliver to: email, phone number, etc., depending on the type.",
    "label" : "The label (e.g., \"Work\", \"Mobile\", etc.)."
  }
}
```

</details>

## put_users_by_id_notification_rules_by_notification_rule_id

Update a user's notification rule.

<details><summary>Parameters</summary>

### id (required)

**Type:** string

### notification_rule_id (required)

The notification rule ID on the user.

**Type:** string

### $body

The user's notification rule to be updated.

**Type:** object

```json
{
  "notification_rule" : {
    "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
    "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
    "self" : "the API show URL at which the object is accessible",
    "id" : "string",
    "type" : "The type of notification rule.",
    "start_delay_in_minutes" : "The delay before firing the rule, in minutes.",
    "contact_method" : {
      "summary" : "A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier.",
      "html_url" : "a URL at which the entity is uniquely displayed in the Web app",
      "self" : "the API show URL at which the object is accessible",
      "id" : "string",
      "type" : "The type of contact method."
    },
    "urgency" : "Which incident urgency this rule is used for. Account must have the `urgencies` ability to have a low urgency notification rule."
  }
}
```

</details>

