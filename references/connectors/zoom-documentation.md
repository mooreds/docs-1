---
id: zoom-documentation
title: Zoom (version v1.*.*)
sidebar_label: Zoom
layout: docs.mustache
---

## account

Retrieve a sub account under the master account. Your account must be a master account and have this privilege to read sub accounts. Zoom only assigns this privilege to trusted partners.

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

</details>

## account_billing

Retrieve billing information for a sub account under the master account

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

</details>

## account_billing_update

Update billing information for a sub account under the master account Only for the sub account which is a paid account and paid by master account

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

### $body

Billing Contact object

**Type:** object

```json
{
  "zip" : "Billing Contact's zip/postal code",
  "country" : "Billing Contact's country",
  "address" : "Billing Contact's address",
  "apt" : "Billing Contact's apartment/suite",
  "city" : "Billing Contact's city",
  "last_name" : "Billing Contact's last name",
  "phone_number" : "Billing Contact's phone number",
  "state" : "Billing Contact's state",
  "first_name" : "Billing Contact's first name",
  "email" : "Billing Contact's email address"
}
```

</details>

## account_create

Create a sub account under the master account. Your account must be a master account and have this privilege to create sub account. Zoom only assigns this privilege to trusted partners. The created user will not receive a confirmation email..

<details><summary>Parameters</summary>

### $body

Account

**Type:** object

```json
{
  "password" : "User's password",
  "options" : {
    "meeting_connectors" : "Meeting Connector, multiple values separated by comma",
    "pay_mode" : "Payee",
    "share_rc" : "Enable Share Virtual Room Connector",
    "share_mc" : "Enable Share Meeting Connector",
    "room_connectors" : "Virtual Room Connector, multiple value separated by comma"
  },
  "last_name" : "User's last name",
  "first_name" : "User's first name",
  "email" : "User's email address"
}
```

</details>

## account_disassociate

Disassociate a sub account from the master account. This will leave the account intact but the sub account will not longer be associated with the master account.

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

</details>

## account_options_update

Update a sub account's options under the master account

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

### $body

Account options object

**Type:** object

```json
{
  "meeting_connectors" : "Meeting Connector, multiple values separated by comma",
  "pay_mode" : "Payee",
  "share_rc" : "Enable Share Virtual Room Connector",
  "share_mc" : "Enable Share Meeting Connector",
  "room_connectors" : "Virtual Room Connector, multiple value separated by comma"
}
```

</details>

## account_plan_addon_create

Add an additional plan for sub account Can only add an Additional plan for the sub account which is a paid account and paid by master account

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

### $body

Account plan object

**Type:** object

```json
{
  "hosts" : "Account plan number of hosts",
  "type" : "Account plan type"
}
```

</details>

## account_plan_addon_update

Update an additional plan for sub accountCan only update an Additional plan for the sub account which is a paid account and paid by master account

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

### $body

Account plan object

**Type:** object

```json
{
  "hosts" : "Account plan number of hosts",
  "type" : "Account plan type"
}
```

</details>

## account_plan_base_update

Update a base plan for a sub account Can only update a base plan for the sub account which is a paid account and paid by master account

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

### $body

Account base plan object

**Type:** object

```json
{
  "hosts" : "Account base plan number of hosts. For a Pro Plan, please select a value between 1 and 9. For a Business Plan, please select a value between 10 and 49. For a Education Plan, please select a value between 20 and 149. For a Free Trial Plan, please select a value between 1 and 9999.",
  "type" : "Account base plan type"
}
```

</details>

## account_plan_create

Subscribe plans for a sub account of the master account Can only subscribe plans for the sub account which is a free account and paid by master account

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

### $body

**Type:** object

```json
{
  "contact" : {
    "zip" : "Billing Contact's zip/postal code",
    "country" : "Billing Contact's country",
    "address" : "Billing Contact's address",
    "apt" : "Billing Contact's apartment/suite",
    "city" : "Billing Contact's city",
    "last_name" : "Billing Contact's last name",
    "phone_number" : "Billing Contact's phone number",
    "state" : "Billing Contact's state",
    "first_name" : "Billing Contact's first name",
    "email" : "Billing Contact's email address"
  },
  "plan_webinar" : [ {
    "hosts" : "Account plan number of hosts",
    "type" : "Account plan type"
  } ],
  "plan_large_meeting" : [ {
    "hosts" : "Account plan number of hosts",
    "type" : "Account plan type"
  } ],
  "plan_zoom_rooms" : {
    "hosts" : "Account plan number of hosts",
    "type" : "Account plan type"
  },
  "plan_recording" : "Additional Cloud Recording Plan",
  "plan_audio" : {
    "tollfree_countries" : "Toll-free countries, multiple value separated by comma",
    "premium_countries" : "Premium countries, multiple value separated by comma",
    "type" : "Additional Audio Conferencing plan type",
    "callout_countries" : "Call-out countries, multiple value separated by comma",
    "ddi_numbers" : "Dedicated Dial-In Numbers"
  },
  "plan_room_connector" : {
    "hosts" : "Account plan number of hosts",
    "type" : "Account plan type"
  },
  "plan_base" : {
    "hosts" : "Account base plan number of hosts. For a Pro Plan, please select a value between 1 and 9. For a Business Plan, please select a value between 10 and 49. For a Education Plan, please select a value between 20 and 149. For a Free Trial Plan, please select a value between 1 and 9999.",
    "type" : "Account base plan type"
  }
}
```

</details>

## account_plans

Retrieve plan information for a sub account under the master account Only for the sub account which is paid by master account

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

</details>

## account_settings

Retrieve a sub account's settings under the master account

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

</details>

## account_settings_update

Update a sub account's settings under the master account

<details><summary>Parameters</summary>

### accountId (required)

The account ID

**Type:** string

### $body

**Type:** object

```json
{
  "zoom_rooms" : {
    "hide_host_information" : "Hide host and meeting ID from private meetings",
    "start_airplay_manually" : "Start AirPlay service manually",
    "auto_start_stop_scheduled_meetings" : "Automatic start/stop for scheduled meetings",
    "cmr_for_instant_meeting" : "Cloud recording for instant meetings",
    "upcoming_meeting_alert" : "Upcoming meeting alert",
    "ultrasonic" : "Automatic direct sharing using ultrasonic proximity signal",
    "weekly_system_restart" : "Weekly system restart",
    "list_meetings_with_calendar" : "Display meeting list with calendar integration",
    "zr_post_meeting_feedback" : "Zoom Room post meeting feedback",
    "force_private_meeting" : "Transform all meetings to private"
  },
  "security" : {
    "hide_billing_info" : "Hide billing information",
    "import_photos_from_devices" : "Allow importing of photos from photo library on the user's device",
    "admin_change_name_pic" : "Only account administrators can change user's username and picture"
  },
  "feature" : {
    "meeting_capacity" : "Set the maximum number of participants this user can have in a single meeting"
  },
  "schedule_meting" : {
    "join_before_host" : "Allow participants to join the meeting before the host arrives",
    "not_store_meeting_topic" : "Always display \"Zoom Meeting\" as the meeting topic",
    "participant_video" : "Start meetings with participant video on. Participants can change this during the meeting.",
    "enforce_login_with_domains" : "Only signed-in users with a specific domain can join meetings",
    "audio_type" : "Determine how participants can join the audio portion of the meeting",
    "force_pmi_jbh_password" : "Require a password for Personal Meetings if attendees can join before host",
    "host_video" : "Start meetings with host video on",
    "enforce_login_domains" : "Only signed-in users with a specified domains",
    "enforce_login" : "Only signed-in (Zoom users) users can join meetings"
  },
  "telephony" : {
    "third_party_audio" : "Users can join the meeting using the existing 3rd party audio configuration",
    "audio_conference_info" : "3rd party audio conference info"
  },
  "integration" : {
    "google_calendar" : "Enables meetings to be scheduled using Google Calendars",
    "kubi" : "Enables users to control a connected Kubi device from within a Zoom meeting",
    "dropbox" : "Enables users who join a meeting from their mobile device to share content from their Dropbox account",
    "box" : "Enables users who join a meeting from their mobile device to share content from their Box account",
    "microsoft_one_drive" : "Enables users who join a meeting from their mobile device to share content from their Microsoft OneDrive account",
    "google_drive" : "Enables users who join a meeting from their mobile device to share content from their Google Drive"
  },
  "recording" : {
    "cloud_recording_download" : "Cloud Recording Downloads",
    "recording_audio_transcript" : "Automatically transcribe the audio of the meeting or webinar to the cloud",
    "auto_delete_cmr_days" : "When `auto_delete_cmr` is 'true' this value will set the number of days before auto deletion of cloud recordings",
    "save_chat_text" : "Save chat text from the meeting",
    "show_timestamp" : "Add a timestamp to the recording",
    "auto_recording" : "Record meetings automatically as they start",
    "account_user_access_recording" : "Cloud recordings are only accessible to account members. People outside of your organization cannot open links that provide access to cloud recordings.",
    "cloud_recording_download_host" : "Only the host can download cloud recordings",
    "auto_delete_cmr" : "Allow Zoom to automatically delete recordings permanently after a specified number of days",
    "record_speaker_view" : "Record active speaker with shared screen",
    "local_recording" : "Allow hosts and participants to record the meeting to a local file",
    "record_audio_file" : "Record an audio only file",
    "record_gallery_view" : "Record gallery view with shared screen",
    "cloud_recording" : "Allow hosts to record and save the meeting in the cloud"
  },
  "in_meeting" : {
    "breakout_room" : "Allow host to split meeting participants into separate, smaller rooms",
    "webinar_question_answer" : "Q&amp;A in webinar",
    "co_host" : "Allow the host to add co-hosts",
    "file_transfer" : "Hosts and participants can send files through the in-meeting chat",
    "use_html_format_email" : "Use HTML format email for Outlook plugin",
    "polling" : "Add 'Polls' to the meeting controls.",
    "whiteboard" : "Allow participants to share a whiteboard that includes annotation tools",
    "screen_sharing" : "Allow screen sharing",
    "feedback" : "Add a Feedback tab to the Windows Settings or Mac Preferences dialog, and also enable users to provide feedback to Zoom at the end of the meeting",
    "attendee_on_hold" : "Allow hosts to temporarily remove an attendee from the meeting",
    "closed_caption" : "Allow host to type closed captions or assign a participant/third party device to add closed captions",
    "group_hd" : "Activate higher quality video for host and participants. (This will use more bandwidth.)",
    "virtual_background" : "Allow users to replace their background with any selected image. Choose or upload an image in the Zoom Desktop application settings.",
    "auto_answer" : "Enable users to see and add contacts to 'auto-answer group' in the contact list on chat. Any call from members of this group will be automatically answered.",
    "anonymous_question_answer" : "Allow Anonymous Q&amp;A in Webinar",
    "allow_show_zoom_windows" : "Show Zoom Desktop application when sharing screen",
    "annotation" : "Allow participants to use annotation tools to add information to shared screens",
    "original_audio" : "Allow users to select original sound in their client settings",
    "p2p_ports" : "P2P listening ports range",
    "far_end_camera_control" : "Allow another user to take control of your camera during a meeting",
    "watermark" : "Add watermark when viewing shared screen",
    "sending_default_email_invites" : "Only show default email when sending email invites",
    "e2e_encryption" : "Require that all meetings are encrypted using AES",
    "p2p_connetion" : "Peer to Peer connection while only 2 people are in a meeting",
    "dscp_video" : "DSCP Video",
    "attention_tracking" : "Lets the host see an indicator in the participant panel if a meeting/webinar attendee does not have Zoom in focus during screen sharing",
    "post_meeting_feedback" : "Display a thumbs up/down survey at the end of each meeting",
    "remote_control" : "Allow users to request remote control",
    "auto_saving_chat" : "Automatically save all in-meeting chats so that hosts do not need to manually save the text of the chat after the meeting starts",
    "alert_guest_join" : "Identify guest participants in the meeting/webinar",
    "ports_range" : "Listening ports range, separated by comma (ex 55,56). The ports range must be between 1 to 65535.",
    "dscp_audio" : "DSCP Audio",
    "chat" : "Allow meeting participants to send a message visible to all participants",
    "private_chat" : "Allow meeting participants to send a private 1:1 message to another participants",
    "show_meeting_control_toolbar" : "Always show meeting control toolbar",
    "stereo_audio" : "Allow users to select stereo audio in their client settings",
    "dscp_marking" : "DSCP marking"
  },
  "email_notification" : {
    "cloud_recording_avaliable_reminder" : "Notify host when cloud recording is available",
    "low_host_count_reminder" : "Notify when host licenses are running low",
    "cancel_meeting_reminder" : "Notify host and participants when the meeting is cancelled",
    "jbh_reminder" : "Notify host when participants join the meeting before them",
    "alternative_host_reminder" : "Notify when an alternative host is set or removed from a meeting"
  }
}
```

</details>

## accounts

List all the sub accounts under the master account

*This operation has no parameters*

## dashboard_crc

Get CRC Port usage hour by hour for a specified time period We will report a maximum of one month. For example, if "from" is set to "2017-08-05" and "to" is "2017-10-10" we will adjust "from" to "2017-09-10".

<details><summary>Parameters</summary>

### from (required)

Start Date

**Type:** date

### to (required)

End Date

**Type:** date

</details>

## dashboard_im

Retrieve metrics of Zoom IM

<details><summary>Parameters</summary>

### from (required)

Start Date

**Type:** date

### to (required)

End Date

**Type:** date

</details>

## dashboard_meeting_detail

Retrieve live or past meetings detail

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

### type

The meeting type

**Type:** string

**Potential values:** past, pastOne, live

</details>

## dashboard_meeting_participant_qos

Retrieve live or past meetings participant quality of service

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

### participantId (required)

Participant ID

**Type:** string

### type

The meeting type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_meeting_participant_share

Retrieve sharing/recording details of live or past meetings participant

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

### type

The meeting type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_meeting_participants

Retrieve live or past meetings participants

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

### type

The meeting type

**Type:** string

**Potential values:** past, pastOne, live

</details>

## dashboard_meeting_participants_qos

Retrieve list of live or past meetings participants quality of service

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

### type

The meeting type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_meetings

List live meetings or past meetings for a specified period

<details><summary>Parameters</summary>

### from (required)

Start Date

**Type:** date

### to (required)

End Date

**Type:** date

### type

The meeting type

**Type:** string

**Potential values:** past, pastOne, live

</details>

## dashboard_webinar_detail

Retrieve live or past webinars detail

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_webinar_participant_qos

Retrieve live or past webinar participant quality of service

<details><summary>Parameters</summary>

### participantId (required)

Participant ID

**Type:** string

### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_webinar_participant_share

Retrieve sharing/recording details of live or past webinar participant

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_webinar_participants

Retrieve live or past webinar participants

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_webinar_participants_qos

Retrieve list of live or past webinar participants quality of service

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_webinars

List live webinars or past webinars for a specified period

<details><summary>Parameters</summary>

### from (required)

Start Date

**Type:** date

### to (required)

End Date

**Type:** date

### type

The webinar type

**Type:** string

**Potential values:** past, live

</details>

## dashboard_zoom_room

Retrieve zoom room on account

<details><summary>Parameters</summary>

### from (required)

Start Date

**Type:** date

### to (required)

End Date

**Type:** date

### zoomroomId (required)

The Zoom Room ID

**Type:** string

### page_number

Current page number of returned records

**Type:** integer

### page_size

The number of records returned within a single API call

**Type:** integer

</details>

## dashboard_zoom_rooms

List all zoom rooms on account

*This operation has no parameters*

## device_create

Create a H.323/SIP Device on your Zoom account

<details><summary>Parameters</summary>

### $body

H.323/SIP Device

**Type:** object

```json
{
  "protocol" : "Device protocol",
  "encryption" : "Device encryption",
  "ip" : "Device Ip",
  "name" : "Device name"
}
```

</details>

## device_delete

Delete a H.323/SIP Device on your Zoom account

<details><summary>Parameters</summary>

### deviceId (required)

The device ID

**Type:** string

</details>

## device_list



*This operation has no parameters*

## device_update

Update a H.323/SIP Device on your Zoom account

<details><summary>Parameters</summary>

### deviceId (required)

The device ID

**Type:** string

### $body

The H.323/SIP device object.

**Type:** object

```json
{
  "protocol" : "Device protocol",
  "encryption" : "Device encryption",
  "ip" : "Device Ip",
  "name" : "Device name"
}
```

</details>

## group

Retrieve a group under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

</details>

## group_create

Create a group under your account

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "name" : "Group name"
}
```

</details>

## group_delete

Delete a group under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

</details>

## group_members

List a group's members under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

</details>

## group_members_create

Add members to a group under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

### $body

**Type:** object

```json
{
  "members" : [ {
    "id" : "User ID",
    "email" : "User email. If ID given, email is ignored."
  } ]
}
```

</details>

## group_members_delete

Delete a member from a group under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

### memberId (required)

The member ID

**Type:** string

</details>

## group_update

Update a group under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

### $body

**Type:** object

```json
{
  "name" : "Group name. Must be unique in one account. Character length is less than 128."
}
```

</details>

## groups



*This operation has no parameters*

## im_group

Retrieve an IM Group under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

</details>

## im_group_create

Create a IM Group under your account

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "search_by_ma_account" : "Members can search others under same master account, including all sub accounts",
  "name" : "Group name, must be unique in one account",
  "type" : "IM Group type",
  "search_by_account" : "Members can search others under same account",
  "search_by_domain" : "Members can search others in the same email domain"
}
```

</details>

## im_group_delete

Delete an IM Group under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

</details>

## im_group_members

List an IM Group's members under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

</details>

## im_group_members_create

Add members to an IM Group under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

### $body

**Type:** object

```json
{
  "members" : [ {
    "id" : "User ID",
    "email" : "User email. If ID given, email is ignored."
  } ]
}
```

</details>

## im_group_members_delete

Delete a member from an IM Group under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

### memberId (required)

The member ID

**Type:** string

</details>

## im_group_update

Update an IM Group under your account

<details><summary>Parameters</summary>

### groupId (required)

The group ID

**Type:** string

### $body

**Type:** object

```json
{
  "search_by_ma_account" : "Members can search others under same master account, including all sub accounts",
  "name" : "Group name, must be unique in one account",
  "type" : "IM Group type",
  "search_by_account" : "Members can search others under same account",
  "search_by_domain" : "Members can search others in the same email domain"
}
```

</details>

## im_groups



*This operation has no parameters*

## meeting

Retrieve a meeting's details

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID

**Type:** integer

</details>

## meeting_create

Create a meeting for a user The expiration time of start_url is two hours. But for API users, the expiration time is 90 days.

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### $body

Meeting object

**Type:** object

```json
{
  "duration" : "Meeting duration (minutes). Used for scheduled meetings only",
  "recurrence" : {
    "end_times" : "Select how many times the meeting will occur before it is canceled. (Cannot be used with \"end_date_time\".)",
    "end_date_time" : "Select a date the meeting will occur before it is canceled.. Should be UTC time, such as 2017-11-25T12:00:00Z. (Cannot be used with \"end_times\".)",
    "monthly_week" : "Week for which the meeting should recur each month,",
    "monthly_week_day" : "Day for which the meeting should recur each month",
    "repeat_interval" : "At which interval should the meeting repeat? For a daily meeting, max of 90 days. For a weekly meeting, max of 12 weeks. For a monthly meeting, max of 3 months.",
    "monthly_day" : "Day of the month for the meeting to be scheduled. The value range is from 1 to 31.",
    "type" : "Recurrence meeting type",
    "weekly_days" : "Days of the week the meeting should repeat, multiple values separated by comma"
  },
  "start_time" : "Meeting start time. When using a format like \"yyyy-MM-dd'T'HH:mm:ss'Z'\", always use GMT time. When using a format like \"yyyy-MM-dd'T'HH:mm:ss\", you should use local time and you will need to specify the time zone. Only used for scheduled meetings and recurring meetings with fixed time.",
  "settings" : {
    "join_before_host" : "Allow participants to join the meeting before the host starts the meeting. Only used for scheduled or recurring meetings.",
    "cn_meeting" : "Host meeting in China",
    "watermark" : "Add watermark when viewing shared screen",
    "use_pmi" : "Use Personal Meeting ID. Only used for scheduled meetings and recurring meetings with no fixed time.",
    "approval_type" : "integer",
    "host_video" : "Start video when host joins meeting",
    "auto_recording" : "string. Possible values: local | cloud | none",
    "registration_type" : "Registration type. Used for recurring meeting with fixed time only.",
    "enforce_login" : "Only signed-in users can join this meeting",
    "alternative_hosts" : "Alternative hosts emails or IDs. Multiple value separated by comma.",
    "participant_video" : "Start video when participants join meeting",
    "audio" : "Determine how participants can join the audio portion of the meeting",
    "in_meeting" : "Host meeting in India",
    "mute_upon_entry" : "Mute participants upon entry",
    "enforce_login_domains" : "Only signed-in users with specified domains can join meetings"
  },
  "password" : "Password to join the meeting. Password may only contain the following characters: [a-z A-Z 0-9 @ - _ *]. Max of 10 characters.",
  "timezone" : "Timezone to format start_time. For example, \"America/Los_Angeles\". For scheduled meetings only. Please reference our [timezone](#timezones) list for supported timezones and their formats.",
  "topic" : "Meeting topic",
  "type" : "Meeting Type",
  "agenda" : "Meeting description"
}
```

</details>

## meeting_delete

Delete a meeting

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID

**Type:** integer

### occurrence_id

The meeting occurrence ID

**Type:** string

</details>

## meeting_registrant_create

Register a participant for a meeting

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID

**Type:** integer

### $body

**Type:** object

```json
{
  "zip" : "Zip/Postal Code",
  "country" : "Country",
  "purchasing_time_frame" : "Purchasing Time Frame",
  "custom_questions" : [ {
    "title" : "string",
    "value" : "string"
  } ],
  "address" : "Address",
  "comments" : "Questions &amp; Comments",
  "city" : "City",
  "org" : "Organization",
  "last_name" : "User’s last name",
  "no_of_employees" : "Number of Employees",
  "industry" : "Industry",
  "phone" : "Phone",
  "role_in_purchase_process" : "Role in Purchase Process",
  "state" : "State/Province",
  "first_name" : "User’s first name",
  "job_title" : "Job Title",
  "email" : "A valid email address"
}
```

### occurrence_ids

Occurrence IDs. You can find these with the meeting get API. Multiple values separated by comma.

**Type:** string

</details>

## meeting_registrant_status

Update a meeting registrant's status

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID

**Type:** integer

### $body

Registrant Status

**Type:** object

```json
{
  "registrants" : [ {
    "id" : "string",
    "email" : "string"
  } ],
  "action" : "Required string. Possible values: approve | cancel | deny"
}
```

### occurrence_id

The meeting occurrence ID

**Type:** string

</details>

## meeting_registrants

List registrants of a meeting

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID

**Type:** integer

### occurrence_id

The meeting occurrence ID

**Type:** string

### status

The registrant status

**Type:** string

**Potential values:** pending, approved, denied

</details>

## meeting_status

Update a meeting's status

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID

**Type:** integer

### $body

**Type:** object

```json
{
  "action" : "string. Possible values: end"
}
```

</details>

## meeting_update

Update a meeting's details

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID

**Type:** integer

### $body

Meeting

**Type:** object

```json
{
  "duration" : "Meeting duration (minutes). Used for scheduled meetings only",
  "recurrence" : {
    "end_times" : "Select how many times the meeting will occur before it is canceled. (Cannot be used with \"end_date_time\".)",
    "end_date_time" : "Select a date the meeting will occur before it is canceled.. Should be UTC time, such as 2017-11-25T12:00:00Z. (Cannot be used with \"end_times\".)",
    "monthly_week" : "Week for which the meeting should recur each month,",
    "monthly_week_day" : "Day for which the meeting should recur each month",
    "repeat_interval" : "At which interval should the meeting repeat? For a daily meeting, max of 90 days. For a weekly meeting, max of 12 weeks. For a monthly meeting, max of 3 months.",
    "monthly_day" : "Day of the month for the meeting to be scheduled. The value range is from 1 to 31.",
    "type" : "Recurrence meeting type",
    "weekly_days" : "Days of the week the meeting should repeat, multiple values separated by comma"
  },
  "start_time" : "Meeting start time. When using a format like \"yyyy-MM-dd'T'HH:mm:ss'Z'\", always use GMT time. When using a format like \"yyyy-MM-dd'T'HH:mm:ss\", you should use local time and you will need to specify the time zone. Only used for scheduled meetings and recurring meetings with fixed time.",
  "settings" : { },
  "password" : "Password to join the meeting. Password may only contain the following characters: [a-z A-Z 0-9 @ - _ *]. Max of 10 characters.",
  "timezone" : "Timezone to format start_time. For example, \"America/Los_Angeles\". For scheduled meetings only. Please reference our [timezone](#timezones) list for supported timezones and their formats.",
  "topic" : "Meeting topic",
  "type" : "Meeting Type",
  "agenda" : "Meeting description"
}
```

</details>

## meetings

List meetings for a user

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### type

The meeting type

**Type:** string

**Potential values:** scheduled, live, upcoming

</details>

## past_meeting_details

Retrieve ended meeting details

<details><summary>Parameters</summary>

### meetingUUID (required)

The meeting UUID.

**Type:** string

</details>

## past_meeting_participants

Retrieve ended meeting participants

<details><summary>Parameters</summary>

### meetingUUID (required)

The meeting UUID.

**Type:** string

</details>

## past_webinars

List of ended webinar instances

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

</details>

## recording_delete

Delete a meeting's recordings

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

### action

The recording delete action

**Type:** string

**Potential values:** trash, delete

</details>

## recording_delete_one

Delete one meeting recording file

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

### recordingId (required)

The recording ID

**Type:** string

### action

The recording delete action

**Type:** string

**Potential values:** trash, delete

</details>

## recording_get

Retrieve a meeting’s all recordings

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

</details>

## recording_status_update

Recover a meeting's recordings

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

### $body

**Type:** object

```json
{
  "action" : "string. Possible values: recover"
}
```

</details>

## recording_status_update_one

Recover a single recording

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

### recordingId (required)

The recording ID

**Type:** string

### $body

**Type:** object

```json
{
  "action" : "string. Possible values: recover"
}
```

</details>

## recordings_list

List all the recordings

<details><summary>Parameters</summary>

### from (required)

Start Date

**Type:** date

### to (required)

End Date

**Type:** date

### userId (required)

The user ID or email address

**Type:** string

### mc

Query mc

**Type:** string

### trash

Query trash

**Type:** boolean

</details>

## report_daily

Retrieve daily report for one month, can only get daily report for recent 6 months

<details><summary>Parameters</summary>

### month

Month for this report

**Type:** integer

### year

Year for this report

**Type:** integer

</details>

## report_meeting_details

Retrieve ended meeting details report

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

</details>

## report_meeting_participants

Retrieve ended meeting participants report

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

</details>

## report_meeting_polls

Retrieve ended meeting polls report

<details><summary>Parameters</summary>

### meetingId (required)

The meeting ID or meeting UUID. If given meeting ID, will take the last meeting instance.

**Type:** string

</details>

## report_meetings

Retrieve ended meetings report for a specified period

<details><summary>Parameters</summary>

### from (required)

Start Date

**Type:** date

### to (required)

End Date

**Type:** date

### userId (required)

The user ID or email address

**Type:** string

</details>

## report_telephone

Retrieve telephone report for a specified period Toll Report option would be removed..

<details><summary>Parameters</summary>

### from (required)

Start Date

**Type:** date

### to (required)

End Date

**Type:** date

### type

Audio type

**Type:** string

**Potential values:** 1

</details>

## report_users

Retrieve active or inactive hosts report for a specified period

<details><summary>Parameters</summary>

### from (required)

Start Date

**Type:** date

### to (required)

End Date

**Type:** date

### type

Active hosts or inactive hosts

**Type:** string

**Potential values:** active, inactive

</details>

## report_webinar_details

Retrieve ended webinar details report

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

</details>

## report_webinar_participants

Retrieve ended webinar participants report

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

</details>

## report_webinar_polls

Retrieve ended webinar polls report

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

</details>

## report_webinar_qa

Retrieve ended webinar Q&amp;A report

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID or webinar UUID. If given webinar ID, will take the last webinar instance.

**Type:** string

</details>

## tsp



*This operation has no parameters*

## user

Retrieve a user on your account

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### login_type

**Type:** string

**Potential values:** 0, 1, 99, 100, 101

</details>

## user_assistant_create

Add assistants to a user

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### $body

User assistant

**Type:** object

```json
{
  "assistants" : [ {
    "id" : "User ID",
    "email" : "User email address. Must have id or email, if given id, the email is ignored."
  } ]
}
```

</details>

## user_assistant_delete

Delete one of a user's assistants

<details><summary>Parameters</summary>

### assistantId (required)

Assistant's ID

**Type:** string

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_assistants

List a user's assistants

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_assistants_delete

Delete all of a user'sassitants

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_create

Create a user on your account

<details><summary>Parameters</summary>

### $body

User

**Type:** object

```json
{
  "user_info" : {
    "password" : "User’s password. Only for \"autoCreate\" action.",
    "last_name" : "User's last name. Cannot contain more than 5 Chinese words.",
    "type" : "User's type",
    "first_name" : "User's first name. Cannot contain more than 5 Chinese words.",
    "email" : "User's email address"
  },
  "action" : "Specify how to create the new user"
}
```

</details>

## user_delete

Delete a user on your account

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### action

Delete action type

**Type:** string

**Potential values:** disassociate, delete

### transfer_email

Transfer email

**Type:** string

### transfer_meeting

Transfer meeting

**Type:** boolean

### transfer_recording

Transfer recording

**Type:** boolean

### transfer_webinar

Transfer webinar

**Type:** boolean

</details>

## user_email

Check if the user email exists

<details><summary>Parameters</summary>

### email (required)

Zoom work email

**Type:** string

</details>

## user_pa_cs

List user's PAC accounts

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_password

Update a user's password

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### $body

User password

**Type:** object

```json
{
  "password" : "User’s password. Character length is less than 32,"
}
```

</details>

## user_permission

Retrieve a user's permissions

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_picture

Upload a user's profile picture

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### $body

**Type:** object

```json
{
  "pic_file" : "User picture file, must be a jpg/jpeg file"
}
```

</details>

## user_scheduler_delete

Delete one of a user's schedulers

<details><summary>Parameters</summary>

### schedulerId (required)

Scheduler's ID

**Type:** string

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_schedulers

List a user's schedulers

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_schedulers_delete

Delete all of a user'schedulers

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_settings

Retrieve a user's settings

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### login_type

**Type:** string

**Potential values:** 0, 1, 99, 100, 101

</details>

## user_settings_update

Update a user's settings

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### $body

User Settings

**Type:** object

```json
{
  "feature" : {
    "webinar_capacity" : "Webinar capacity, can be 100, 500, 1000, 3000, 5000 or 10000, depends on if having related webinar capacity plan subscription or not",
    "large_meeting" : "Large meting feature",
    "large_meeting_capacity" : "Large meeting capacity, can be 100, 200, 300 or 500, depends on if having related large meeting capacity plan subscription or not",
    "meeting_capacity" : "User’s meeting capacity",
    "webinar" : "Webinar feature"
  },
  "telephony" : {
    "third_party_audio" : "3rd party audio conference",
    "audio_conference_info" : "3rd party audio conference info",
    "show_international_numbers_link" : "Show international numbers link on the invitation email"
  },
  "scheduled_meeting" : {
    "participants_video" : "Participants video",
    "join_before_host" : "Join before host",
    "audio_type" : "Determine how participants can join the audio portion of the meeting",
    "force_pmi_jbh_password" : "Require a password for Personal Meetings if attendees can join before host",
    "pstn_password_protected" : "Generate and require password for participants joining by phone",
    "host_video" : "Host video"
  },
  "recording" : {
    "auto_delete_cmr" : "Auto delete cloud recordings",
    "record_speaker_view" : "Record the active speaker view",
    "recording_audio_transcript" : "Audio transcript",
    "local_recording" : "Local recording",
    "auto_delete_cmr_days" : "A specified number of days of auto delete cloud recordings",
    "record_audio_file" : "Record an audio only file",
    "save_chat_text" : "Save chat text from the meeting",
    "show_timestamp" : "Show timestamp on video",
    "record_gallery_view" : "Record the gallery view",
    "auto_recording" : "Automatic recording",
    "cloud_recording" : "Cloud recording"
  },
  "in_meeting" : {
    "annotation" : "Annotation",
    "breakout_room" : "Breakout room",
    "far_end_camera_control" : "Far end camera control",
    "co_host" : "Co-host",
    "e2e_encryption" : "End-to-end encryption",
    "file_transfer" : "File transfer",
    "polling" : "Polling",
    "record_play_voice" : "Record and play their own voice",
    "feedback" : "Feedback to Zoom",
    "attendee_on_hold" : "Allow host to put attendee on hold",
    "attention_tracking" : "Attention tracking",
    "closed_caption" : "Closed caption",
    "group_hd" : "Group HD video",
    "remote_control" : "Remote control",
    "virtual_background" : "Virtual background",
    "waiting_room" : "Waiting room",
    "auto_saving_chat" : "Auto saving chats",
    "chat" : "Chat",
    "private_chat" : "Private chat",
    "entry_exit_chime" : "Play sound on join/leave",
    "non_verbal_feedback" : "Non-verbal feedback",
    "share_dual_camera" : "Share dual camera (Deprecated)",
    "remote_support" : "Remote support"
  },
  "email_notification" : {
    "cancel_meeting_reminder" : "When a meeting is cancelled",
    "jbh_reminder" : "When attendees join meeting before host",
    "alternative_host_reminder" : "When an alternative host is set or removed from a meeting"
  }
}
```

</details>

## user_sso_token_delete

Revoke a user's SSO token

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_status

Update a user's status

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### $body

User status

**Type:** object

```json
{
  "action" : "The action type"
}
```

</details>

## user_token

Retrieve a user's token

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### type

User token type

**Type:** string

**Potential values:** token, zpk, zak

</details>

## user_ts_ps

List user's TSP accounts

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_tsp

Retrieve a user's TSP account

<details><summary>Parameters</summary>

### tspId (required)

TSP account index

**Type:** string

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_tsp_create

Add a user's TSP account

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### $body

TSP Account

**Type:** object

```json
{
  "dial_in_numbers" : [ {
    "number" : "Dial-in number, length is less than 16.",
    "code" : "Country Code",
    "type" : "Dial-in number type."
  } ],
  "conference_code" : "Conference code, numeric value, length is less than 16.",
  "leader_pin" : "Leader PIN, numeric value, length is less than 16."
}
```

</details>

## user_tsp_delete

Delete a user's TSP account

<details><summary>Parameters</summary>

### tspId (required)

TSP account index

**Type:** string

### userId (required)

The user ID or email address

**Type:** string

</details>

## user_tsp_update

Update a user's TSP account

<details><summary>Parameters</summary>

### tspId (required)

TSP account index

**Type:** string

### userId (required)

The user ID or email address

**Type:** string

### $body

TSP Account

**Type:** object

```json
{
  "dial_in_numbers" : [ {
    "number" : "Dial-in number, length is less than 16.",
    "code" : "Country Code",
    "type" : "Dial-in number type."
  } ],
  "conference_code" : "Conference code, numeric value, length is less than 16.",
  "leader_pin" : "Leader PIN, numeric value, length is less than 16."
}
```

</details>

## user_update

Update a user on your account

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### $body

User

**Type:** object

```json
{
  "host_key" : "Host Key, should be 6-digit number",
  "vanity_name" : "Personal meeting room name",
  "timezone" : "The time zone id for user profile. For this parameter value please refer to the id value in [timezone](#timezones) list.",
  "cms_user_id" : "Kaltura User Id",
  "last_name" : "User's last name. Cannot contain more than 5 Chinese words.",
  "dept" : "Department for user profile, use for report",
  "type" : "User's type",
  "first_name" : "User's first name. Cannot contain more than 5 Chinese words.",
  "pmi" : "Personal Meeting ID,length must be 10"
}
```

</details>

## user_vanity_name

Check if the user's personal meeting room name exists

<details><summary>Parameters</summary>

### vanity_name (required)

Personal meeting room name

**Type:** string

</details>

## user_zpk

Check if the zpk is expired. The zpk is used to authenticate a user.

<details><summary>Parameters</summary>

### zpk (required)

User zpk

**Type:** string

</details>

## users

List users on your account

<details><summary>Parameters</summary>

### status

User status

**Type:** string

**Potential values:** active, inactive, pending

</details>

## webhook

Retrieve a webhook

<details><summary>Parameters</summary>

### webhookId (required)

The webhook ID

**Type:** string

</details>

## webhook_create

Create a webhook for a account

<details><summary>Parameters</summary>

### $body

Webhook

**Type:** object

```json
{
  "auth_user" : "Webhook auth user name",
  "auth_password" : "Webhook auth password",
  "url" : "Webhook endpoint",
  "events" : [ "string" ]
}
```

</details>

## webhook_delete

Delete a webhook

<details><summary>Parameters</summary>

### webhookId (required)

The webhook ID

**Type:** string

</details>

## webhook_switch

Switch webhook version

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "version" : "Required string. Possible values: v1 | v2"
}
```

</details>

## webhook_update

Update a webhook

<details><summary>Parameters</summary>

### webhookId (required)

The webhook ID

**Type:** string

### $body

Webhook

**Type:** object

```json
{
  "auth_user" : "Webhook auth user name",
  "auth_password" : "Webhook auth password",
  "url" : "Webhook endpoint",
  "events" : [ "string" ]
}
```

</details>

## webhooks



*This operation has no parameters*

## webinar

Retrieve a webinar

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

</details>

## webinar_create

Create a webinar for a user The expiration time of start_url is two hours. But for API users, the expiration time is 90 days.

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

### $body

User

**Type:** object

```json
{
  "duration" : "Webinar duration (minutes). Used for scheduled webinar only",
  "recurrence" : {
    "end_times" : "Select how many times the meeting will occur before it is canceled. (Cannot be used with \"end_date_time\".)",
    "end_date_time" : "Select a date the meeting will occur before it is canceled.. Should be UTC time, such as 2017-11-25T12:00:00Z. (Cannot be used with \"end_times\".)",
    "monthly_week" : "Week for which the meeting should recur each month,",
    "monthly_week_day" : "Day for which the meeting should recur each month",
    "repeat_interval" : "At which interval should the meeting repeat? For a daily meeting, max of 90 days. For a weekly meeting, max of 12 weeks. For a monthly meeting, max of 3 months.",
    "monthly_day" : "Day of the month for the meeting to be scheduled. The value range is from 1 to 31.",
    "type" : "Recurrence meeting type",
    "weekly_days" : "Days of the week the meeting should repeat, multiple values separated by comma"
  },
  "start_time" : "Webinar start time, in the format \"yyyy-MM-dd'T'HH:mm:ss'Z'\", should be GMT time. In the format \"yyyy-MM-dd'T'HH:mm:ss\", should be local time, need to specify the time zone. Only used for scheduled webinar and recurring webinar with fixed time.",
  "settings" : {
    "approval_type" : "integer",
    "close_registration" : "Close registration after event date",
    "host_video" : "Start video when host joins webinar",
    "panelists_video" : "Start video when panelists join webinar",
    "auto_recording" : "string. Possible values: local | cloud | none",
    "show_share_button" : "Show social share buttons on registration page",
    "hd_video" : "Default to HD Video",
    "registration_type" : "Registration type. Used for recurring webinar with fixed time only.",
    "enforce_login" : "Only signed-in users can join this meeting",
    "allow_multiple_devices" : "Allow attendees to join from multiple devices",
    "alternative_hosts" : "Alternative hosts emails or IDs. Multiple values separated by comma.",
    "audio" : "Determine how participants can join the audio portion of the meeting",
    "practice_session" : "Enable Practice Session",
    "enforce_login_domains" : "Only signed-in users with specified domains can join meetings"
  },
  "password" : "Webinar password. Password may only contain the following characters: [a-z A-Z 0-9 @ - _ *]. Max of 10 characters.",
  "timezone" : "Timezone to format start_time. For example, \"America/Los_Angeles\". For scheduled meetings only. Please reference our [timezone](#timezones) list for supported timezones and their formats.",
  "topic" : "Webinar topic",
  "type" : "Webinar Type",
  "agenda" : "Webinar description"
}
```

</details>

## webinar_delete

Delete a webinar

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

### occurrence_id

The meeting occurrence ID

**Type:** string

</details>

## webinar_panelist_create

Add panelist to webinar

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

### $body

Webinar panelist

**Type:** object

```json
{
  "panelists" : [ { } ]
}
```

</details>

## webinar_panelist_delete

Remove a panelist from a webinar

<details><summary>Parameters</summary>

### panelistId (required)

The panelist ID

**Type:** integer

### webinarId (required)

The webinar ID

**Type:** integer

</details>

## webinar_panelists

List panelists for a webinar

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

</details>

## webinar_panelists_delete

Remove all panelists from a webinar

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

</details>

## webinar_registrant_create

Add a registrant for a webinar

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

### $body

**Type:** object

```json
{
  "zip" : "Zip/Postal Code",
  "country" : "Country",
  "purchasing_time_frame" : "Purchasing Time Frame",
  "custom_questions" : [ {
    "title" : "string",
    "value" : "string"
  } ],
  "address" : "Address",
  "comments" : "Questions &amp; Comments",
  "city" : "City",
  "org" : "Organization",
  "last_name" : "User’s last name",
  "no_of_employees" : "Number of Employees",
  "industry" : "Industry",
  "phone" : "Phone",
  "role_in_purchase_process" : "Role in Purchase Process",
  "state" : "State/Province",
  "first_name" : "User’s first name",
  "job_title" : "Job Title",
  "email" : "A valid email address"
}
```

### occurrence_ids

Occurrence IDs, could get this value from Webinar Get API. Multiple value separated by comma.

**Type:** string

</details>

## webinar_registrant_status

Update a webinar registrant's status

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

### $body

**Type:** object

```json
{
  "registrants" : [ {
    "id" : "string",
    "email" : "string"
  } ],
  "action" : "Required string. Possible values: approve | cancel | deny"
}
```

### occurrence_id

The meeting occurrence ID

**Type:** string

</details>

## webinar_registrants

List registrants for a webinar

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

### occurrence_id

The meeting occurrence ID

**Type:** string

### status

The registrant status

**Type:** string

**Potential values:** pending, approved, denied

</details>

## webinar_status

Update a webinar's status

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

### $body

**Type:** object

```json
{
  "status" : "string. Possible values: end"
}
```

</details>

## webinar_update

Update a webinar

<details><summary>Parameters</summary>

### webinarId (required)

The webinar ID

**Type:** integer

### $body

Webinar

**Type:** object

```json
{
  "duration" : "Webinar duration (minutes). Used for scheduled webinar only",
  "recurrence" : {
    "end_times" : "Select how many times the meeting will occur before it is canceled. (Cannot be used with \"end_date_time\".)",
    "end_date_time" : "Select a date the meeting will occur before it is canceled.. Should be UTC time, such as 2017-11-25T12:00:00Z. (Cannot be used with \"end_times\".)",
    "monthly_week" : "Week for which the meeting should recur each month,",
    "monthly_week_day" : "Day for which the meeting should recur each month",
    "repeat_interval" : "At which interval should the meeting repeat? For a daily meeting, max of 90 days. For a weekly meeting, max of 12 weeks. For a monthly meeting, max of 3 months.",
    "monthly_day" : "Day of the month for the meeting to be scheduled. The value range is from 1 to 31.",
    "type" : "Recurrence meeting type",
    "weekly_days" : "Days of the week the meeting should repeat, multiple values separated by comma"
  },
  "start_time" : "Webinar start time, in the format \"yyyy-MM-dd'T'HH:mm:ss'Z'\", should be GMT time. In the format \"yyyy-MM-dd'T'HH:mm:ss\", should be local time, need to specify the time zone. Only used for scheduled webinar and recurring webinar with fixed time.",
  "settings" : { },
  "password" : "Webinar password. Password may only contain the following characters: [a-z A-Z 0-9 @ - _ *]. Max of 10 characters.",
  "timezone" : "Timezone to format start_time. For example, \"America/Los_Angeles\". For scheduled meetings only. Please reference our [timezone](#timezones) list for supported timezones and their formats.",
  "topic" : "Webinar topic",
  "type" : "Webinar Type",
  "agenda" : "Webinar description"
}
```

</details>

## webinars

List webinars for a user

<details><summary>Parameters</summary>

### userId (required)

The user ID or email address

**Type:** string

</details>

