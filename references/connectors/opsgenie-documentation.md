---
id: opsgenie-documentation
title: Opsgenie (version v1.*.*)
sidebar_label: Opsgenie
layout: docs.mustache
---

## acknowledge_alert

Acknowledges alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## add_details

Add details to the alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## add_note

Adds note to alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## add_responder

Add responder to alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## add_tags

Add tags to the alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## add_team

Add team to alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## add_team_member

Adds a member to team with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### $body

**Type:** object

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## assign_alert

Assign alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## authenticate_integration

Authenticates integration with given type

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## cancel_maintenance

Cancel maintenance with given id

<details><summary>Parameters</summary>

#### id (required)

Identifier of the maintenance to be searched

**Type:** string

</details>

## change_notification_rule_order

Changes order of a notification rule with given notification rule id

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

#### $body

**Type:** object

</details>

## change_policy_order

Change execution order of the policy with given id

<details><summary>Parameters</summary>

#### policyId (required)

Id of the requested policy

**Type:** string

#### $body

**Type:** object

#### teamId

TeamId of policy created if it belongs to a team

**Type:** string

</details>

## change_team_routing_rule_order

Change the order of team routing rule with given id

<details><summary>Parameters</summary>

#### id (required)

Id of the team routing rule

**Type:** string

#### identifier (required)

Identifier of the team

**Type:** string

#### $body

**Type:** object

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## close_alert

Closes alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## create_alert

Creates a new alert

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_contact

Creates a new contact

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### $body

**Type:** object

</details>

## create_custom_user_role

Creates a new custom user role

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_escalation

Creates a new escalation

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_forwarding_rule

Creates a new forwarding rule

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_heartbeat

Create a new heartbeat

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_integration

Creates a new integration

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_integration_action

Creates integration actions of given integration id

<details><summary>Parameters</summary>

#### id (required)

Integration Id

**Type:** string

#### $body

**Type:** object

</details>

## create_maintenance

Creates a new maintenance

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_notification_rule

Creates a new notification rule

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### $body

**Type:** object

</details>

## create_notification_rule_step

Creates a new notification rule step

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

#### $body

**Type:** object

</details>

## create_policy

Creates a new policy

<details><summary>Parameters</summary>

#### $body

**Type:** object

#### teamId

TeamId of policy created if it belongs to a team

**Type:** string

</details>

## create_saved_searches

Create saved search with given fields

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_schedule

Creates a new schedule

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_schedule_override

Creates a schedule override for the specified user and schedule

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### $body

**Type:** object

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## create_schedule_rotation

Creates a new schedule rotation

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### $body

**Type:** object

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## create_team

Creates a new team

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_team_role

Creates a new team role

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### $body

**Type:** object

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## create_team_routing_rule

Creates a new team routing rule

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### $body

**Type:** object

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## create_user

Creates a user with the given payload

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_alert

Deletes an alert using alert id, tiny id or alias

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

#### source

Display name of the request source

**Type:** string

#### user

Display name of the request owner

**Type:** string

</details>

## delete_contact

Delete contact using contact id

<details><summary>Parameters</summary>

#### contactId (required)

Id of the contact

**Type:** string

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## delete_custom_user_role

Deletes a custom user role using role 'id' or 'name'

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of custom user role which could be user role 'id' or 'name'

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## delete_escalation

Deletes an escalation using escalation 'id' or 'name'

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of escalation which could be escalation 'id' or 'name'

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## delete_forwarding_rule

Deletes forwarding rule with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias'

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias'

**Type:** string

**Potential values:** id, alias

</details>

## delete_heartbeat

Delete heartbeat with given name

<details><summary>Parameters</summary>

#### name (required)

Name of the heartbeat

**Type:** string

</details>

## delete_integration

Delete integration with given id

<details><summary>Parameters</summary>

#### id (required)

Integration Id

**Type:** string

</details>

## delete_maintenance

Delete maintenance with given identifier

<details><summary>Parameters</summary>

#### id (required)

Identifier of the maintenance to be searched

**Type:** string

</details>

## delete_notification_rule

Deletes a notification rule with given notification rule id

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

</details>

## delete_notification_rule_step

Deletes a notification rule step using user identifier, rule id, notification rule step id

<details><summary>Parameters</summary>

#### id (required)

Id of the rule step will be changed.

**Type:** string

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

</details>

## delete_policy

Delete policy with given id

<details><summary>Parameters</summary>

#### policyId (required)

Id of the requested policy

**Type:** string

#### teamId

TeamId of policy created if it belongs to a team

**Type:** string

</details>

## delete_saved_search

Deletes saved search using given search identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the saved search which could be 'id' or 'name'

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', or 'name'

**Type:** string

**Potential values:** id, name

</details>

## delete_schedule

Delete schedule with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## delete_schedule_override

Delete schedule override with given alias

<details><summary>Parameters</summary>

#### alias (required)

Alias of the schedule override

**Type:** string

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## delete_schedule_rotation

Delete schedule rotation with given identifier

<details><summary>Parameters</summary>

#### id (required)

Identifier of schedule rotation

**Type:** string

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## delete_team

Delete team with given id or name

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### identifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## delete_team_member

Deletes the member of team with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### memberIdentifier (required)

User id or username of member for removal

**Type:** string

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## delete_team_role

Deletes a team role using team role 'id' or 'name'

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### teamRoleIdentifier (required)

Identifier of team role which could be team role 'id' or 'name'

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## delete_team_routing_rule

Delete team routing rule with given id

<details><summary>Parameters</summary>

#### id (required)

Id of the team routing rule

**Type:** string

#### identifier (required)

Identifier of the team

**Type:** string

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## delete_user

Delete user with the given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## disable_contact

Disable the contact of the user

<details><summary>Parameters</summary>

#### contactId (required)

Id of the contact

**Type:** string

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## disable_heartbeat

Disable heartbeat request with given name

<details><summary>Parameters</summary>

#### name (required)

Name of the heartbeat

**Type:** string

</details>

## disable_integration

Disable integration with given ID

<details><summary>Parameters</summary>

#### id (required)

Integration Id

**Type:** string

</details>

## disable_notification_rule

Disables a notification rule with given notification rule id

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

</details>

## disable_notification_rule_step

Disables a new notification rule step

<details><summary>Parameters</summary>

#### id (required)

Id of the rule step will be changed.

**Type:** string

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

</details>

## disable_policy

Disable the policy with given id

<details><summary>Parameters</summary>

#### policyId (required)

Id of the requested policy

**Type:** string

#### teamId

TeamId of policy created if it belongs to a team

**Type:** string

</details>

## enable_contact

Enable the contact of the user

<details><summary>Parameters</summary>

#### contactId (required)

Id of the contact

**Type:** string

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## enable_heartbeat

Enable heartbeat request with given name

<details><summary>Parameters</summary>

#### name (required)

Name of the heartbeat

**Type:** string

</details>

## enable_integration

Enable integration with given ID

<details><summary>Parameters</summary>

#### id (required)

Integration Id

**Type:** string

</details>

## enable_notification_rule

Enables a notification rule with given notification rule id

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

</details>

## enable_notification_rule_step

Enables a new notification rule step

<details><summary>Parameters</summary>

#### id (required)

Id of the rule step will be changed.

**Type:** string

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

</details>

## enable_policy

Enable the policy with given id

<details><summary>Parameters</summary>

#### policyId (required)

Id of the requested policy

**Type:** string

#### teamId

TeamId of policy created if it belongs to a team

**Type:** string

</details>

## escalate_alert

Escalate alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## execute_custom_alert_action

Custom actions for the alert

<details><summary>Parameters</summary>

#### actionName (required)

Name of the action to execute

**Type:** string

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## export_oncall_user

Exports personal on-call timeline of 3 months to a .ics file

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user. Should be either 'id' or 'username' of the user

**Type:** string

</details>

## export_schedule

Returns an .ics file as byte array

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## get_alert

Returns alert with given id, tiny id or alias

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## get_attachment

Get alert attachment name and url for the given identifier

<details><summary>Parameters</summary>

#### attachmentId (required)

Identifier of alert attachment

**Type:** integer

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### alertIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## get_contact

Returns contact with given id

<details><summary>Parameters</summary>

#### contactId (required)

Id of the contact

**Type:** string

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## get_custom_user_role

Returns custom user role with given 'id' or 'name'

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of custom user role which could be user role 'id' or 'name'

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## get_escalation

Returns escalation with given 'id' or 'name'

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of escalation which could be escalation 'id' or 'name'

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## get_forwarding_rule

Returns forwarding rule with given id or alias

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias'

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias'

**Type:** string

**Potential values:** id, alias

</details>

## get_heartbeat

Returns heartbeat with given name

<details><summary>Parameters</summary>

#### name (required)

Name of the heartbeat

**Type:** string

</details>

## get_info



*This operation has no parameters*

## get_integration

Returns integration with given id

<details><summary>Parameters</summary>

#### id (required)

Integration Id

**Type:** string

</details>

## get_maintenance

Returns maintenance with given id

<details><summary>Parameters</summary>

#### id (required)

Identifier of the maintenance to be searched

**Type:** string

</details>

## get_next_oncalls

Gets next on-call participants of a specific schedule

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### date

Starting date of the timeline

**Type:** string

#### flat

Retrieves user names of all on call participants if enabled

**Type:** boolean

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## get_notification_rule

Returns notification rule with given id

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

</details>

## get_notification_rule_step

Returns notification rule step with given user identifier and rule id

<details><summary>Parameters</summary>

#### id (required)

Id of the rule step will be changed.

**Type:** string

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

</details>

## get_oncalls

Gets current on-call participants of a specific schedule

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### date

Starting date of the timeline

**Type:** string

#### flat

Retrieves user names of all on call participants if enabled

**Type:** boolean

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## get_policy

Used to get details of a single policy with id

<details><summary>Parameters</summary>

#### policyId (required)

Id of the requested policy

**Type:** string

#### teamId

TeamId of policy created if it belongs to a team

**Type:** string

</details>

## get_request_status

Used to track the status and alert details (if any) of the request whose identifier is given

<details><summary>Parameters</summary>

#### requestId (required)

Universally unique identifier of the questioned request

**Type:** string

</details>

## get_saved_search

Get saved search for the given search identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the saved search which could be 'id' or 'name'

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', or 'name'

**Type:** string

**Potential values:** id, name

</details>

## get_schedule

Returns schedule with given id or name

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## get_schedule_override

Gets schedule override details with given alias

<details><summary>Parameters</summary>

#### alias (required)

Alias of the schedule override

**Type:** string

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## get_schedule_rotation

Returns schedule rotation with given id

<details><summary>Parameters</summary>

#### id (required)

Identifier of schedule rotation

**Type:** string

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## get_schedule_timeline

Returns schedule timeline with given id or name

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### date

Time to return future date on-call participants. Default date is the moment of the time that request is received

**Type:** string

#### expand

Returns more detailed response with expanding it. Possible values are 'base', 'forwarding', and 'override' which is also returned with expandable field of response

**Type:** array

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

#### interval

Length of time as integer in intervalUnits to retrieve the timeline. Default value is 1

**Type:** integer

#### intervalUnit

Unit of the time to retrieve the timeline. Available values are 'days', 'weeks' and 'months'. Default value is 'weeks'

**Type:** string

**Potential values:** days, weeks, months

</details>

## get_team

Returns team with given 'id' or 'name'

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### identifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## get_team_role

Returns team role with given 'id' or 'name'

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### teamRoleIdentifier (required)

Identifier of team role which could be team role 'id' or 'name'

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## get_team_routing_rule

Returns team routing rule with given id

<details><summary>Parameters</summary>

#### id (required)

Id of the team routing rule

**Type:** string

#### identifier (required)

Identifier of the team

**Type:** string

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## get_user

Get user for the given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### expand

Comma separated list of strings to create a more detailed response. The only expandable field for user api is 'contact'

**Type:** array

</details>

## list_alert_notes

List alert notes for the given alert identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### direction

Page direction to apply for the given offset with 'next' and 'prev'

**Type:** string

**Potential values:** next, prev

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

#### order

Sorting order of the result set

**Type:** string

**Potential values:** asc, desc

</details>

## list_alert_policies

Returns the list of alert policies

<details><summary>Parameters</summary>

#### teamId

TeamId of policy created if it belongs to a team

**Type:** string

</details>

## list_alerts

Returns list of alerts

<details><summary>Parameters</summary>

#### order

Sorting order of the result set

**Type:** string

**Potential values:** asc, desc

#### query

Search query to apply while filtering the alerts

**Type:** string

#### searchIdentifier

Identifier of the saved search query to apply while filtering the alerts

**Type:** string

#### searchIdentifierType

Identifier type of the saved search query. Possible values are 'id', or 'name'

**Type:** string

**Potential values:** id, name

#### sort

Name of the field that result set will be sorted by

**Type:** string

**Potential values:** createdAt, updatedAt, tinyId, alias, message, status, acknowledged, isSeen, snoozed, snoozedUntil, count, lastOccurredAt, source, owner, integration.name, integration.type, report.ackTime, report.closeTime, report.acknowledgedBy, report.closedBy

</details>

## list_attachments

List alert attachment names and urls for related alert

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### alertIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## list_contacts

Returns list of contacts

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## list_custom_user_roles



*This operation has no parameters*

## list_escalations



*This operation has no parameters*

## list_forwarding_rules



*This operation has no parameters*

## list_integration_actions

List integration actions of given integration id

<details><summary>Parameters</summary>

#### id (required)

Integration Id

**Type:** string

</details>

## list_integrations

Returns list of integrations with given parameters

<details><summary>Parameters</summary>

#### teamId

The ID of the team. If the team ID parameter is given, the result will be filtered by teamId

**Type:** string

#### teamName

The name of the team. If the team name parameter is given, the result will be filtered by teamName

**Type:** string

#### type

Type of the integration (For instance, "API" for API Integration). If type parameter is given, the result will be filtered by type

**Type:** string

</details>

## list_logs

List alert logs for the given alert identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### direction

Page direction to apply for the given offset with 'next' and 'prev'

**Type:** string

**Potential values:** next, prev

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

#### order

Sorting order of the result set

**Type:** string

**Potential values:** asc, desc

</details>

## list_maintenance

List maintenance by type

<details><summary>Parameters</summary>

#### type

Type of the maintenance list to be searched

**Type:** string

**Potential values:** all, past, non-expired

</details>

## list_notification_policies

Returns the list of notification policies

<details><summary>Parameters</summary>

#### teamId

TeamId of policy created if it belongs to a team

**Type:** string

</details>

## list_notification_rule_steps

Returns list of notification rule steps

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

</details>

## list_notification_rules

Returns list of notification rules

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## list_recipients

List alert recipients for the given alert identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## list_saved_searches



*This operation has no parameters*

## list_schedule_override

Returns list of schedule overrides

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## list_schedule_rotations

Returns list of schedule rotations

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## list_schedules

Returns list of schedule

<details><summary>Parameters</summary>

#### expand

Returns more detailed response with expanding it. Possible value is 'rotation' which is also returned with expandable field of response

**Type:** array

</details>

## list_team_logs

Return logs of a team given with identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### identifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

#### order

Sorting order of the result set

**Type:** string

**Potential values:** asc, desc

</details>

## list_team_roles

Returns list of team roles

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## list_team_routing_rules

Returns list of team routing rules

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## list_teams



*This operation has no parameters*

## list_user_escalations

List escalations of the user for the given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## list_user_forwarding_rules

List user forwarding rules for the given user identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## list_user_schedules

List schedules of the user for the given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## list_user_teams

List user teams for the given user identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

</details>

## list_users

List users with given parameters

<details><summary>Parameters</summary>

#### order

Direction of sorting. Should be one of 'asc' or 'desc'

**Type:** string

**Potential values:** asc, desc

#### query

Field:value combinations with most of user fields to make more advanced searches. Possible fields are username, fullName, blocked, verified, role, locale, timeZone, userAddress and createdAt

**Type:** string

#### sortField

Field to use in sorting. Should be one of 'username', 'fullName' and 'insertedAt'

**Type:** string

</details>

## ping

Ping Heartbeat for given heartbeat name

<details><summary>Parameters</summary>

#### name (required)

Name of the heartbeat

**Type:** string

</details>

## remove_attachment

Remove alert attachment for the given identifier

<details><summary>Parameters</summary>

#### attachmentId (required)

Identifier of alert attachment

**Type:** integer

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### alertIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

#### user

Display name of the request owner

**Type:** string

</details>

## remove_details

Remove details of the alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### keys (required)

Comma separated list of keys to remove from the custom properties of the alert (e.g. 'key1,key2')

**Type:** array

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

#### note

Additional alert note to add

**Type:** string

#### source

Display name of the request source

**Type:** string

#### user

Display name of the request owner

**Type:** string

</details>

## remove_tags

Remove tags of the alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### tags (required)

Tags field of the given alert as comma seperated values (e.g. 'tag1, tag2')

**Type:** array

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

#### note

Additional alert note to add

**Type:** string

#### source

Display name of the request source

**Type:** string

#### user

Display name of the request owner

**Type:** string

</details>

## snooze_alert

Snooze alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## unacknowledge_alert

UnAcknowledge alert with given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of alert which could be alert id, tiny id or alert alias

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id', 'alias' or 'tiny'

**Type:** string

**Potential values:** id, alias, tiny

</details>

## update_contact

Update contact of the user

<details><summary>Parameters</summary>

#### contactId (required)

Id of the contact

**Type:** string

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### $body

**Type:** object

</details>

## update_custom_user_role

Updates the custom user role using role 'id' or 'name'

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of custom user role which could be user role 'id' or 'name'

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## update_escalation

Updates the escalation using escalation 'id' or 'name'

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of escalation which could be escalation 'id' or 'name'

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## update_forwarding_rule

Update forwarding rule with given rule id or alias

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the forwarding rule which could be forwarding rule 'id' or 'alias'

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'alias'

**Type:** string

**Potential values:** id, alias

</details>

## update_heartbeat

Update Heartbeatwith given name

<details><summary>Parameters</summary>

#### name (required)

Name of the heartbeat

**Type:** string

#### $body

**Type:** object

</details>

## update_integration

Update integration with given id

<details><summary>Parameters</summary>

#### id (required)

Integration Id

**Type:** string

#### $body

**Type:** object

</details>

## update_integration_actions

Updates integration actions of given integration id

<details><summary>Parameters</summary>

#### id (required)

Integration Id

**Type:** string

#### $body

**Type:** object

</details>

## update_maintenance

Update maintenance with given id

<details><summary>Parameters</summary>

#### id (required)

Identifier of the maintenance to be searched

**Type:** string

#### $body

**Type:** object

</details>

## update_notification_rule

Updates the notification rule with given notification rule id

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

#### $body

**Type:** object

</details>

## update_notification_rule_step

Update a notification rule step with given user identifier, rule id, and notification rule step id

<details><summary>Parameters</summary>

#### id (required)

Id of the rule step will be changed.

**Type:** string

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### ruleId (required)

Id of the notification rule that step will belong to.

**Type:** string

#### $body

**Type:** object

</details>

## update_policy

Update alert policy with given id

<details><summary>Parameters</summary>

#### policyId (required)

Id of the requested policy

**Type:** string

#### $body

**Type:** object

#### teamId

TeamId of policy created if it belongs to a team

**Type:** string

</details>

## update_schedule

Update schedule with given id or name

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## update_schedule_override

Update schedule override with given alias

<details><summary>Parameters</summary>

#### alias (required)

Alias of the schedule override

**Type:** string

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### $body

**Type:** object

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## update_schedule_rotation

Update schedule rotation with given id

<details><summary>Parameters</summary>

#### id (required)

Identifier of schedule rotation

**Type:** string

#### identifier (required)

Identifier of schedule which could be id or name

**Type:** string

#### $body

**Type:** object

#### scheduleIdentifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

</details>

## update_team

Update team with given id

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### $body

**Type:** object

</details>

## update_team_role

Updates the team role using team role 'id' or 'name'

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the team

**Type:** string

#### teamRoleIdentifier (required)

Identifier of team role which could be team role 'id' or 'name'

**Type:** string

#### $body

**Type:** object

#### identifierType

Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'

**Type:** string

**Potential values:** id, name

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## update_team_routing_rule

Update routing rule of the team

<details><summary>Parameters</summary>

#### id (required)

Id of the team routing rule

**Type:** string

#### identifier (required)

Identifier of the team

**Type:** string

#### $body

**Type:** object

#### teamIdentifierType

Type of the identifier. Possible values are 'id' and 'name'. Default value is 'id'

**Type:** string

**Potential values:** id, name

</details>

## update_user

Update user with the given identifier

<details><summary>Parameters</summary>

#### identifier (required)

Identifier of the user to be searched

**Type:** string

#### $body

**Type:** object

</details>

