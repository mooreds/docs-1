---
id: zoom-documentation
title: Zoom (version v1.*.*)
sidebar_label: Zoom
---

## account

Retrieve a sub account under the master account. <aside>Your account must be a master account and have this privilege to read sub accounts. Zoom only assigns this privilege to trusted partners</aside>.

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

</details>

## account_billing

Retrieve billing information for a sub account under the master account

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

</details>

## account_billing_update

Update billing information for a sub account under the master account <aside>Only for the sub account which is a paid account and paid by master account</aside>

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

#### $body

Billing Contact object

**Type:** object

</details>

## account_create

Create a sub account under the master account. <aside>Your account must be a master account and have this privilege to create sub account. Zoom only assigns this privilege to trusted partners. The created user will not receive a confirmation email.</aside>.

<details><summary>Parameters</summary>

#### $body

Account

**Type:** object

</details>

## account_disassociate

Disassociate a sub account from the master account. This will leave the account intact but the sub account will not longer be associated with the master account.

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

</details>

## account_options_update

Update a sub account's options under the master account

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

#### $body

Account options object

**Type:** object

</details>

## account_plan_addon_create

Add an additional plan for sub account <aside>Can only add an Additional plan for the sub account which is a paid account and paid by master account</aside>

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

#### $body

Account plan object

**Type:** object

</details>

## account_plan_addon_update

Update an additional plan for sub account<aside>Can only update an Additional plan for the sub account which is a paid account and paid by master account</aside>

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

#### $body

Account plan object

**Type:** object

</details>

## account_plan_base_update

Update a base plan for a sub account <aside>Can only update a base plan for the sub account which is a paid account and paid by master account</aside>

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

#### $body

Account base plan object

**Type:** object

</details>

## account_plan_create

Subscribe plans for a sub account of the master account <aside>Can only subscribe plans for the sub account which is a free account and paid by master account</aside>

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

#### $body

**Type:** object

</details>

## account_plans

Retrieve plan information for a sub account under the master account  <aside>Only for the sub account which is paid by master account</aside>

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

</details>

## account_settings

Retrieve a sub account's settings under the master account

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

</details>

## account_settings_update

Update a sub account's settings under the master account

<details><summary>Parameters</summary>

#### accountId (required)

The account ID

**Type:** string

#### $body

**Type:** object

</details>

## accounts

List all the sub accounts under the master account

*This operation has no parameters*

## dashboard_crc

Get CRC Port usage hour by hour for a specified time period <aside class='notice'>We will report a maximum of one month. For example, if "from" is set to "2017-08-05" and "to" is "2017-10-10" we will adjust "from" to "2017-09-10"</aside>.

<details><summary>Parameters</summary>

#### from (required)

Start Date

**Type:** date

#### to (required)

End Date

**Type:** date

</details>

## dashboard_im

Retrieve metrics of Zoom IM

<details><summary>Parameters</summary>

#### from (required)

Start Date

**Type:** date

#### to (required)

End Date

**Type:** date

</details>

## dashboard_meeting_detail

Retrieve live or past meetings detail

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

#### type

The meeting type

**Type:** string

**Potential values:** past, pastOne, live

</details>

## dashboard_meeting_participant_qos

Retrieve live or past meetings participant quality of service

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

#### participantId (required)

Participant ID

**Type:** string

#### type

The meeting type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_meeting_participant_share

Retrieve sharing/recording details of live or past meetings participant

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

#### type

The meeting type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_meeting_participants

Retrieve live or past meetings participants

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

#### type

The meeting type

**Type:** string

**Potential values:** past, pastOne, live

</details>

## dashboard_meeting_participants_qos

Retrieve list of live or past meetings participants quality of service

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

#### type

The meeting type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_meetings

List live meetings or past meetings for a specified period

<details><summary>Parameters</summary>

#### from (required)

Start Date

**Type:** date

#### to (required)

End Date

**Type:** date

#### type

The meeting type

**Type:** string

**Potential values:** past, pastOne, live

</details>

## dashboard_webinar_detail

Retrieve live  or past webinars detail

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

#### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_webinar_participant_qos

Retrieve live or past webinar participant quality of service

<details><summary>Parameters</summary>

#### participantId (required)

Participant ID

**Type:** string

#### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

#### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_webinar_participant_share

Retrieve sharing/recording details of live or past webinar participant

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

#### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_webinar_participants

Retrieve live or past webinar participants

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

#### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_webinar_participants_qos

Retrieve list of live or past webinar participants quality of service

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

#### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_webinars

List live webinars or past webinars for a specified period

<details><summary>Parameters</summary>

#### from (required)

Start Date

**Type:** date

#### to (required)

End Date

**Type:** date

#### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_zoom_room

Retrieve zoom room on account

<details><summary>Parameters</summary>

#### from (required)

Start Date

**Type:** date

#### to (required)

End Date

**Type:** date

#### zoomroomId (required)

The Zoom Room ID

**Type:** string

#### page_number

Current page number of returned records

**Type:** integer

#### page_size

The number of records returned within a single API call

**Type:** integer

</details>

## dashboard_zoom_rooms

List all zoom rooms on account

*This operation has no parameters*

## device_create

Create a H.323/SIP Device on your Zoom account

<details><summary>Parameters</summary>

#### $body

H.323/SIP Device

**Type:** object

</details>

## device_delete

Delete a H.323/SIP Device on your Zoom account

<details><summary>Parameters</summary>

#### deviceId (required)

The device ID

**Type:** string

</details>

## device_list



*This operation has no parameters*

## device_update

Update a H.323/SIP Device on your Zoom account

<details><summary>Parameters</summary>

#### deviceId (required)

The device ID

**Type:** string

#### $body

The H.323/SIP device object.

**Type:** object

</details>

## group

Retrieve a group under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

</details>

## group_create

Create a group under your account

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## group_delete

Delete a group under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

</details>

## group_members

List a group's members under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

</details>

## group_members_create

Add members to a group under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

#### $body

**Type:** object

</details>

## group_members_delete

Delete a member from a group under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

#### memberId (required)

The member ID

**Type:** string

</details>

## group_update

Update a group under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

#### $body

**Type:** object

</details>

## groups



*This operation has no parameters*

## im_group

Retrieve an IM Group under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

</details>

## im_group_create

Create a IM Group under your account

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## im_group_delete

Delete an IM Group under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

</details>

## im_group_members

List an IM Group's members under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

</details>

## im_group_members_create

Add members to an IM Group under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

#### $body

**Type:** object

</details>

## im_group_members_delete

Delete a member from an IM Group under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

#### memberId (required)

The member ID

**Type:** string

</details>

## im_group_update

Update an IM Group under your account

<details><summary>Parameters</summary>

#### groupId (required)

The group ID

**Type:** string

#### $body

**Type:** object

</details>

## im_groups



*This operation has no parameters*

## meeting

Retrieve a meeting's details

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID

**Type:** integer

</details>

## meeting_create

Create a meeting for a user <aside>The expiration time of start_url is two hours. But for API users, the expiration time is 90 days.</aside>

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### $body

Meeting object

**Type:** object

</details>

## meeting_delete

Delete a meeting

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID

**Type:** integer

#### occurrence_id

The meeting occurrence ID

**Type:** string

</details>

## meeting_registrant_create

Register a participant for a meeting

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID

**Type:** integer

#### $body

**Type:** object

#### occurrence_ids

Occurrence IDs. You can find these with the meeting get API. Multiple values separated by comma.

**Type:** string

</details>

## meeting_registrant_status

Update a meeting registrant's status

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID

**Type:** integer

#### $body

Registrant Status

**Type:** object

#### occurrence_id

The meeting occurrence ID

**Type:** string

</details>

## meeting_registrants

List registrants of a meeting

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID

**Type:** integer

#### occurrence_id

The meeting occurrence ID

**Type:** string

#### status

The registrant status

**Type:** string

**Potential values:** pending, approved, denied

</details>

## meeting_status

Update a meeting's status

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID

**Type:** integer

#### $body

**Type:** object

</details>

## meeting_update

Update a meeting's details

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID

**Type:** integer

#### $body

Meeting

**Type:** object

</details>

## meetings

List meetings for a user

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### type

The meeting type

**Type:** string

**Potential values:** scheduled, live, upcoming

</details>

## past_meeting_details

Retrieve ended meeting details

<details><summary>Parameters</summary>

#### meetingUUID (required)

The meeting UUID.

**Type:** string

</details>

## past_meeting_participants

Retrieve ended meeting participants

<details><summary>Parameters</summary>

#### meetingUUID (required)

The meeting UUID.

**Type:** string

</details>

## past_webinars

List of ended webinar instances

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

</details>

## recording_delete

Delete a meeting's recordings

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

#### action

The recording delete action

**Type:** string

**Potential values:** trash, delete

</details>

## recording_delete_one

Delete one meeting recording file

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

#### recordingId (required)

The recording ID

**Type:** string

#### action

The recording delete action

**Type:** string

**Potential values:** trash, delete

</details>

## recording_get

Retrieve a meeting’s all recordings

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

</details>

## recording_status_update

Recover a meeting's recordings

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

#### $body

**Type:** object

</details>

## recording_status_update_one

Recover a single recording

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

#### recordingId (required)

The recording ID

**Type:** string

#### $body

**Type:** object

</details>

## recordings_list

List all the recordings

<details><summary>Parameters</summary>

#### from (required)

Start Date

**Type:** date

#### to (required)

End Date

**Type:** date

#### userId (required)

The user ID or email address

**Type:** string

#### mc

Query mc 

**Type:** string

#### trash

Query trash 

**Type:** boolean

</details>

## report_daily

Retrieve daily report for one month, can only get daily report for recent 6 months

<details><summary>Parameters</summary>

#### month

Month for this report

**Type:** integer

#### year

Year for this report

**Type:** integer

</details>

## report_meeting_details

Retrieve ended meeting details report

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

</details>

## report_meeting_participants

Retrieve ended meeting participants report

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

</details>

## report_meeting_polls

Retrieve ended meeting polls report

<details><summary>Parameters</summary>

#### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

</details>

## report_meetings

Retrieve ended meetings report for a specified period

<details><summary>Parameters</summary>

#### from (required)

Start Date

**Type:** date

#### to (required)

End Date

**Type:** date

#### userId (required)

The user ID or email address

**Type:** string

</details>

## report_telephone

Retrieve telephone report for a specified period <aside>Toll Report option would be removed.</aside>.

<details><summary>Parameters</summary>

#### from (required)

Start Date

**Type:** date

#### to (required)

End Date

**Type:** date

#### type

Audio type

**Type:** string

**Potential values:** 1

</details>

## report_users

Retrieve active or inactive hosts report for a specified period

<details><summary>Parameters</summary>

#### from (required)

Start Date

**Type:** date

#### to (required)

End Date

**Type:** date

#### type

Active hosts or inactive hosts

**Type:** string

**Potential values:** active, inactive

</details>

## report_webinar_details

Retrieve ended webinar details report

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

</details>

## report_webinar_participants

Retrieve ended webinar participants report

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

</details>

## report_webinar_polls

Retrieve ended webinar polls report

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

</details>

## report_webinar_qa

Retrieve ended webinar Q&A report

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

</details>

## tsp



*This operation has no parameters*

## user

Retrieve a user on your account

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### login_type

**Type:** string

**Potential values:** 0, 1, 99, 100, 101

</details>

## user_assistant_create

Add assistants to a user

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### $body

User assistant

**Type:** object

</details>

## user_assistant_delete

Delete one of a user's assistants

<details><summary>Parameters</summary>

#### assistantId (required)

Assistant's ID

**Type:** string

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_assistants

List a user's assistants

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_assistants_delete

Delete all of a user'sassitants

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_create

Create a user on your account

<details><summary>Parameters</summary>

#### $body

User

**Type:** object

</details>

## user_delete

Delete a user on your account

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### action

Delete action type

**Type:** string

**Potential values:** disassociate, delete

#### transfer_email

Transfer email

**Type:** string

#### transfer_meeting

Transfer meeting

**Type:** boolean

#### transfer_recording

Transfer recording

**Type:** boolean

#### transfer_webinar

Transfer webinar

**Type:** boolean

</details>

## user_email

Check if the user email exists

<details><summary>Parameters</summary>

#### email (required)

Zoom work email

**Type:** string

</details>

## user_pa_cs

List user's PAC accounts

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_password

Update a user's password

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### $body

User password

**Type:** object

</details>

## user_permission

Retrieve a user's permissions

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_picture

Upload a user's profile picture

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### $body

**Type:** object

</details>

## user_scheduler_delete

Delete one of a user's schedulers

<details><summary>Parameters</summary>

#### schedulerId (required)

Scheduler's ID

**Type:** string

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_schedulers

List a user's schedulers

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_schedulers_delete

Delete all of a user'schedulers

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_settings

Retrieve a user's settings

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### login_type

**Type:** string

**Potential values:** 0, 1, 99, 100, 101

</details>

## user_settings_update

Update a user's settings

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### $body

User Settings

**Type:** object

</details>

## user_sso_token_delete

Revoke a user's SSO token

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_status

Update a user's status

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### $body

User status

**Type:** object

</details>

## user_token

Retrieve a user's token

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### type

User token type

**Type:** string

**Potential values:** token, zpk, zak

</details>

## user_ts_ps

List user's TSP accounts

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_tsp

Retrieve a user's TSP account

<details><summary>Parameters</summary>

#### tspId (required)

TSP account index

**Type:** string

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_tsp_create

Add a user's TSP account

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### $body

TSP Account

**Type:** object

</details>

## user_tsp_delete

Delete a user's TSP account

<details><summary>Parameters</summary>

#### tspId (required)

TSP account index

**Type:** string

#### userId (required)

The user ID or email address

**Type:** string

</details>

## user_tsp_update

Update a user's TSP account

<details><summary>Parameters</summary>

#### tspId (required)

TSP account index

**Type:** string

#### userId (required)

The user ID or email address

**Type:** string

#### $body

TSP Account

**Type:** object

</details>

## user_update

Update a user on your account

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### $body

User

**Type:** object

</details>

## user_vanity_name

Check if the user's personal meeting room name exists

<details><summary>Parameters</summary>

#### vanity_name (required)

Personal meeting room name

**Type:** string

</details>

## user_zpk

Check if the zpk is expired. The zpk is used to authenticate a user.

<details><summary>Parameters</summary>

#### zpk (required)

User zpk

**Type:** string

</details>

## users

List users on your account

<details><summary>Parameters</summary>

#### status

User status

**Type:** string

**Potential values:** active, inactive, pending

</details>

## webhook

Retrieve a webhook

<details><summary>Parameters</summary>

#### webhookId (required)

The webhook ID

**Type:** string

</details>

## webhook_create

Create a webhook for a account

<details><summary>Parameters</summary>

#### $body

Webhook

**Type:** object

</details>

## webhook_delete

Delete a webhook

<details><summary>Parameters</summary>

#### webhookId (required)

The webhook ID

**Type:** string

</details>

## webhook_switch

Switch webhook version

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## webhook_update

Update a webhook

<details><summary>Parameters</summary>

#### webhookId (required)

The webhook ID

**Type:** string

#### $body

Webhook

**Type:** object

</details>

## webhooks



*This operation has no parameters*

## webinar

Retrieve a webinar

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

</details>

## webinar_create

Create a webinar for a user <aside>The expiration time of start_url is two hours. But for API users, the expiration time is 90 days.</aside>

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

#### $body

User

**Type:** object

</details>

## webinar_delete

Delete a webinar

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

#### occurrence_id

The meeting occurrence ID

**Type:** string

</details>

## webinar_panelist_create

Add panelist to webinar

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

#### $body

Webinar panelist

**Type:** object

</details>

## webinar_panelist_delete

Remove a panelist from a webinar

<details><summary>Parameters</summary>

#### panelistId (required)

The panelist ID

**Type:** integer

#### webinarId (required)

The webinar ID

**Type:** integer

</details>

## webinar_panelists

List panelists for a webinar

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

</details>

## webinar_panelists_delete

Remove all panelists from a webinar

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

</details>

## webinar_registrant_create

Add a registrant for a webinar

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

#### $body

**Type:** object

#### occurrence_ids

Occurrence IDs, could get this value from Webinar Get API. Multiple value separated by comma.

**Type:** string

</details>

## webinar_registrant_status

Update a webinar registrant's status

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

#### $body

**Type:** object

#### occurrence_id

The meeting occurrence ID

**Type:** string

</details>

## webinar_registrants

List registrants for a webinar

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

#### occurrence_id

The meeting occurrence ID

**Type:** string

#### status

The registrant status

**Type:** string

**Potential values:** pending, approved, denied

</details>

## webinar_status

Update a webinar's status

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

#### $body

**Type:** object

</details>

## webinar_update

Update a webinar

<details><summary>Parameters</summary>

#### webinarId (required)

The webinar ID

**Type:** integer

#### $body

Webinar

**Type:** object

</details>

## webinars

List webinars for a user

<details><summary>Parameters</summary>

#### userId (required)

The user ID or email address

**Type:** string

</details>

