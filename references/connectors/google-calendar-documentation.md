---
id: google-calendar-documentation
title: Google Calendar (version v1.*.*)
sidebar_label: Google Calendar
layout: docs.mustache
---

## clear_calendar

Clears a primary calendar. This operation deletes all events associated with the primary calendar of an account.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_acl_rule

Creates an access control rule.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### $body

**Type:** object

```json
{
  "role" : "The role assigned to the scope. Possible values are:  \n- \"none\" - Provides no access. \n- \"freeBusyReader\" - Provides read access to free/busy information. \n- \"reader\" - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden. \n- \"writer\" - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible. \n- \"owner\" - Provides ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs.",
  "kind" : "Type of the resource (\"calendar#aclRule\").",
  "scope" : {
    "type" : "The type of the scope. Possible values are:  \n- \"default\" - The public scope. This is the default value. \n- \"user\" - Limits the scope to a single user. \n- \"group\" - Limits the scope to a group. \n- \"domain\" - Limits the scope to a domain.  Note: The permissions granted to the \"default\", or public, scope apply to any user, authenticated or not.",
    "value" : "The email address of a user or group, or the name of a domain, depending on the scope type. Omitted for type \"default\"."
  },
  "etag" : "ETag of the resource.",
  "id" : "Identifier of the ACL rule."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sendNotifications

Deprecated. Use sendUpdates instead

**Type:** boolean

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_calendar

Creates a secondary calendar.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "conferenceProperties" : {
    "allowedConferenceSolutionTypes" : [ "string" ]
  },
  "summary" : "Title of the calendar. Required on a create_calendar operation",
  "kind" : "Type of the resource (\"calendar#calendar\").",
  "description" : "Description of the calendar. Optional.",
  "timeZone" : "The time zone of the calendar. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) Optional.",
  "etag" : "ETag of the resource.",
  "location" : "Geographic location of the calendar as free-form text. Optional.",
  "id" : "Identifier of the calendar. To retrieve IDs call the get_calendarlist method. Note that when creating a calendar, this field should not be filled out."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_calendar_event

Creates an event.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### $body

**Type:** object

```json
{
  "reminders" : {
    "overrides" : [ {
      "method" : "The method used by this reminder. Possible values are:  \n- \"email\" - Reminders are sent via email. \n- \"sms\" - Deprecated. Reminders are sent via SMS. These are only available for G Suite customers. Requests to set SMS reminders for other account types are ignored. \n- \"popup\" - Reminders are sent via a UI popup.",
      "minutes" : "Number of minutes before the start of the event when the reminder should trigger. Valid values are between 0 and 40320 (4 weeks in minutes)."
    } ],
    "useDefault" : "Whether the default reminders of the calendar apply to the event."
  },
  "attachments" : [ {
    "iconLink" : "URL link to the attachment's icon. Read-only.",
    "fileUrl" : "URL link to the attachment.\nFor adding Google Drive file attachments use the same format as in alternateLink property of the Files resource in the Drive API. Required when adding an attachment.",
    "mimeType" : "Internet media type (MIME type) of the attachment.",
    "title" : "Attachment title.",
    "fileId" : "ID of the attached file. Read-only.\nFor Google Drive files, this is the ID of the corresponding Files resource entry in the Drive API."
  } ],
  "gadget" : {
    "preferences" : "Preferences.",
    "iconLink" : "The gadget's icon URL. The URL scheme must be HTTPS.",
    "display" : "The gadget's display mode. Optional. Possible values are:  \n- \"icon\" - The gadget displays next to the event's title in the calendar view. \n- \"chip\" - The gadget displays when the event is clicked.",
    "link" : "The gadget's URL. The URL scheme must be HTTPS.",
    "width" : "The gadget's width in pixels. The width must be an integer greater than 0. Optional.",
    "title" : "The gadget's title.",
    "type" : "The gadget's type.",
    "height" : "The gadget's height in pixels. The height must be an integer greater than 0. Optional."
  },
  "colorId" : "The color of the event. This is an ID referring to an entry in the event section of the colors definition (see the colors endpoint). Optional.",
  "hangoutLink" : "An absolute link to the Google+ hangout associated with this event. Read-only.",
  "attendeesOmitted" : "Whether attendees may have been omitted from the event's representation. When retrieving an event, this may be due to a restriction specified by the maxAttendee query parameter. When updating an event, this can be used to only update the participant's response. Optional. The default is False.",
  "description" : "Description of the event. Optional.",
  "source" : {
    "title" : "Title of the source; for example a title of a web page or an email subject.",
    "url" : "URL of the source pointing to a resource. The URL scheme must be HTTP or HTTPS."
  },
  "extendedProperties" : {
    "shared" : "Properties that are shared between copies of the event on other attendees' calendars.",
    "private" : "Properties that are private to the copy of the event that appears on this calendar."
  },
  "guestsCanModify" : "Whether attendees other than the organizer can modify the event. Optional. The default is False.",
  "recurringEventId" : "For an instance of a recurring event, this is the id of the recurring event to which this instance belongs. Immutable.",
  "endTimeUnspecified" : "Whether the end time is actually unspecified. An end time is still provided for compatibility reasons, even if this attribute is set to True. The default is False.",
  "guestsCanSeeOtherGuests" : "Whether attendees other than the organizer can see who the event's attendees are. Optional. The default is True.",
  "end" : {
    "date" : "The date, in the format \"yyyy-mm-dd\", if this is an all-day event.",
    "dateTime" : "The time, as a combined date-time value (formatted according to RFC3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.",
    "timeZone" : "The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end."
  },
  "id" : "Opaque identifier of the event. When creating new single or recurring events, you can specify their IDs. Provided IDs must follow these rules:  \n- characters allowed in the ID are those used in base32hex encoding, i.e. lowercase letters a-v and digits 0-9, see section 3.1.2 in RFC2938 \n- the length of the ID must be between 5 and 1024 characters \n- the ID must be unique per calendar  Due to the globally distributed nature of the system, we cannot guarantee that ID collisions will be detected at event creation time. To minimize the risk of collisions we recommend using an established UUID algorithm such as one described in RFC4122.\nIf you do not specify an ID, it will be automatically generated by the server.\nNote that the icalUID and the id are not identical and only one of them should be supplied at event creation time. One difference in their semantics is that in recurring events, all occurrences of one event have different ids while they all share the same icalUIDs.",
  "locked" : "Whether this is a locked event copy where no changes can be made to the main event fields \"summary\", \"description\", \"location\", \"start\", \"end\" or \"recurrence\". The default is False. Read-Only.",
  "anyoneCanAddSelf" : "Whether anyone can invite themselves to the event (currently works for Google+ events only). Optional. The default is False.",
  "summary" : "Title of the event.",
  "creator" : {
    "displayName" : "The creator's name, if available.",
    "self" : "Whether the creator corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.",
    "id" : "The creator's Profile ID, if available. It corresponds to the id field in the People collection of the Google+ API",
    "email" : "The creator's email address, if available."
  },
  "privateCopy" : "Whether this is a private event copy where changes are not shared with other copies on other calendars. Optional. Immutable. The default is False.",
  "visibility" : "Visibility of the event. Optional. Possible values are:  \n- \"default\" - Uses the default visibility for events on the calendar. This is the default value. \n- \"public\" - The event is public and event details are visible to all readers of the calendar. \n- \"private\" - The event is private and only event attendees may view event details. \n- \"confidential\" - The event is private. This value is provided for compatibility reasons.",
  "attendees" : [ {
    "additionalGuests" : "Number of additional guests. Optional. The default is 0.",
    "resource" : "Whether the attendee is a resource. Can only be set when the attendee is added to the event for the first time. Subsequent modifications are ignored. Optional. The default is False.",
    "displayName" : "The attendee's name, if available. Optional.",
    "organizer" : "Whether the attendee is the organizer of the event. Read-only. The default is False.",
    "self" : "Whether this entry represents the calendar on which this copy of the event appears. Read-only. The default is False.",
    "comment" : "The attendee's response comment. Optional.",
    "optional" : "Whether this is an optional attendee. Optional. The default is False.",
    "id" : "The attendee's Profile ID, if available. It corresponds to the id field in the People collection of the Google+ API",
    "responseStatus" : "The attendee's response status. Possible values are:  \n- \"needsAction\" - The attendee has not responded to the invitation. \n- \"declined\" - The attendee has declined the invitation. \n- \"tentative\" - The attendee has tentatively accepted the invitation. \n- \"accepted\" - The attendee has accepted the invitation.",
    "email" : "The attendee's email address, if available. This field must be present when adding an attendee. It must be a valid email address as per RFC5322."
  } ],
  "created" : "Creation time of the event (as a RFC3339 timestamp). Read-only.",
  "htmlLink" : "An absolute link to this event in the Google Calendar Web UI. Read-only.",
  "kind" : "Type of the resource (\"calendar#event\").",
  "iCalUID" : "Event unique identifier as defined in RFC5545. It is used to uniquely identify events accross calendaring systems and must be supplied when importing events via the import method.\nNote that the icalUID and the id are not identical and only one of them should be supplied at event creation time. One difference in their semantics is that in recurring events, all occurrences of one event have different ids while they all share the same icalUIDs.",
  "start" : {
    "date" : "The date, in the format \"yyyy-mm-dd\", if this is an all-day event.",
    "dateTime" : "The time, as a combined date-time value (formatted according to RFC3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.",
    "timeZone" : "The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end."
  },
  "originalStartTime" : {
    "date" : "The date, in the format \"yyyy-mm-dd\", if this is an all-day event.",
    "dateTime" : "The time, as a combined date-time value (formatted according to RFC3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.",
    "timeZone" : "The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end."
  },
  "recurrence" : [ "string" ],
  "sequence" : "Sequence number as per iCalendar.",
  "organizer" : {
    "displayName" : "The organizer's name, if available.",
    "self" : "Whether the organizer corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.",
    "id" : "The organizer's Profile ID, if available. It corresponds to the id field in the People collection of the Google+ API",
    "email" : "The organizer's email address, if available. It must be a valid email address as per RFC5322."
  },
  "transparency" : "Whether the event blocks time on the calendar. Optional. Possible values are:  \n- \"opaque\" - Default value. The event does block time on the calendar. This is equivalent to setting Show me as to Busy in the Calendar UI. \n- \"transparent\" - The event does not block time on the calendar. This is equivalent to setting Show me as to Available in the Calendar UI.",
  "conferenceData" : {
    "entryPoints" : [ {
      "entryPointFeatures" : [ "string" ],
      "password" : "The password to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "regionCode" : "The CLDR/ISO 3166 region code for the country associated with this phone access. Example: \"SE\" for Sweden.\nCalendar backend will populate this field only for EntryPointType.PHONE.",
      "pin" : "The PIN to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "entryPointType" : "The type of the conference entry point.\nPossible values are:  \n- \"video\" - joining a conference over HTTP. A conference can have zero or one video entry point.\n- \"phone\" - joining a conference by dialing a phone number. A conference can have zero or more phone entry points.\n- \"sip\" - joining a conference over SIP. A conference can have zero or one sip entry point.\n- \"more\" - further conference joining instructions, for example additional phone numbers. A conference can have zero or one more entry point. A conference with only a more entry point is not a valid conference.",
      "accessCode" : "The access code to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "meetingCode" : "The meeting code to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "label" : "The label for the URI. Visible to end users. Not localized. The maximum length is 512 characters.\nExamples:  \n- for video: meet.google.com/aaa-bbbb-ccc\n- for phone: +1 123 268 2601\n- for sip: 12345678@altostrat.com\n- for more: should not be filled  \nOptional.",
      "uri" : "The URI of the entry point. The maximum length is 1300 characters.\nFormat:  \n- for video, http: or https: schema is required.\n- for phone, tel: schema is required. The URI should include the entire dial sequence (e.g., tel:+12345678900,,,123456789;1234).\n- for sip, sip: schema is required, e.g., sip:12345678@myprovider.com.\n- for more, http: or https: schema is required.",
      "passcode" : "The passcode to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed."
    } ],
    "notes" : "Additional notes (such as instructions from the domain administrator, legal notices) to display to the user. Can contain HTML. The maximum length is 2048 characters. Optional.",
    "conferenceId" : "The ID of the conference.\nCan be used by developers to keep track of conferences, should not be displayed to users.\nValues for solution types:  \n- \"eventHangout\": unset.\n- \"eventNamedHangout\": the name of the Hangout.\n- \"hangoutsMeet\": the 10-letter meeting code, for example \"aaa-bbbb-ccc\".  Optional.",
    "createRequest" : {
      "requestId" : "The client-generated unique ID for this request.\nClients should regenerate this ID for every new request. If an ID provided is the same as for the previous request, the request is ignored.",
      "conferenceSolutionKey" : {
        "type" : "The conference solution type.\nIf a client encounters an unfamiliar or empty type, it should still be able to display the entry points. However, it should disallow modifications.\nThe possible values are:  \n- \"eventHangout\" for Hangouts for consumers (http://hangouts.google.com)\n- \"eventNamedHangout\" for classic Hangouts for G Suite users (http://hangouts.google.com)\n- \"hangoutsMeet\" for Hangouts Meet (http://meet.google.com)"
      },
      "status" : {
        "statusCode" : "The current status of the conference create request. Read-only.\nThe possible values are:  \n- \"pending\": the conference create request is still being processed.\n- \"success\": the conference create request succeeded, the entry points are populated.\n- \"failure\": the conference create request failed, there are no entry points."
      }
    },
    "signature" : "The signature of the conference data.\nGenereated on server side. Must be preserved while copying the conference data between events, otherwise the conference data will not be copied.\nUnset for a conference with a failed create request.\nOptional for a conference with a pending create request.",
    "conferenceSolution" : {
      "name" : "The user-visible name of this solution. Not localized.",
      "iconUri" : "The user-visible icon for this solution.",
      "key" : {
        "type" : "The conference solution type.\nIf a client encounters an unfamiliar or empty type, it should still be able to display the entry points. However, it should disallow modifications.\nThe possible values are:  \n- \"eventHangout\" for Hangouts for consumers (http://hangouts.google.com)\n- \"eventNamedHangout\" for classic Hangouts for G Suite users (http://hangouts.google.com)\n- \"hangoutsMeet\" for Hangouts Meet (http://meet.google.com)"
      }
    },
    "parameters" : {
      "addOnParameters" : {
        "parameters" : "object"
      }
    }
  },
  "etag" : "ETag of the resource.",
  "location" : "Geographic location of the event as free-form text. Optional.",
  "guestsCanInviteOthers" : "Whether attendees other than the organizer can invite others to the event. Optional. The default is True.",
  "updated" : "Last modification time of the event (as a RFC3339 timestamp). Read-only.",
  "status" : "Status of the event. Optional. Possible values are:  \n- \"confirmed\" - The event is confirmed. This is the default status. \n- \"tentative\" - The event is tentatively confirmed. \n- \"cancelled\" - The event is cancelled (deleted). The list method returns cancelled events only on incremental sync (when syncToken or updatedMin are specified) or if the showDeleted flag is set to true. The get method always returns them.\nA cancelled status represents two different states depending on the event type:  \n- Cancelled exceptions of an uncancelled recurring event indicate that this instance should no longer be presented to the user. Clients should store these events for the lifetime of the parent recurring event.\nCancelled exceptions are only guaranteed to have values for the id, recurringEventId and originalStartTime fields populated. The other fields might be empty.  \n- All other cancelled events represent deleted events. Clients should remove their locally synced copies. Such cancelled events will eventually disappear, so do not rely on them being available indefinitely.\nDeleted events are only guaranteed to have the id field populated.   On the organizer's calendar, cancelled events continue to expose event details (summary, location, etc.) so that they can be restored (undeleted). Similarly, the events to which the user was invited and that they manually removed continue to provide details. However, incremental sync requests with showDeleted set to false will not return these details.\nIf an event changes its organizer (for example via the move operation) and the original organizer is not on the attendee list, it will leave behind a cancelled event where only the id field is guaranteed to be populated."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### conferenceDataVersion

Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.

**Type:** integer

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### maxAttendees

The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.

**Type:** integer

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sendNotifications

Deprecated. Use sendUpdates instead

**Type:** boolean

### supportsAttachments

Whether API client performing operation supports event attachments. Optional. The default is False.

**Type:** boolean

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## create_calendarlist_entry

Adds an entry to the user's calendar list.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "conferenceProperties" : {
    "allowedConferenceSolutionTypes" : [ "string" ]
  },
  "summary" : "Title of the calendar. Read-only.",
  "backgroundColor" : "The main color of the calendar in the hexadecimal format \"#0088aa\". This property supersedes the index-based colorId property. To set or change this property, you need to specify colorRgbFormat=true in the parameters of the insert, update and patch methods. Optional.",
  "hidden" : "Whether the calendar has been hidden from the list. Optional. The default is False.",
  "colorId" : "The color of the calendar. This is an ID referring to an entry in the calendar section of the colors definition (see the colors endpoint). This property is superseded by the backgroundColor and foregroundColor properties and can be ignored when using these properties. Optional.",
  "kind" : "Type of the resource (\"calendar#calendarListEntry\").",
  "description" : "Description of the calendar. Optional. Read-only.",
  "timeZone" : "The time zone of the calendar. Optional. Read-only.",
  "foregroundColor" : "The foreground color of the calendar in the hexadecimal format \"#ffffff\". This property supersedes the index-based colorId property. To set or change this property, you need to specify colorRgbFormat=true in the parameters of the insert, update and patch methods. Optional.",
  "notificationSettings" : {
    "notifications" : [ {
      "method" : "The method used to deliver the notification. Possible values are:  \n- \"email\" - Reminders are sent via email. \n- \"sms\" - Deprecated. Reminders are sent via SMS. This value is read-only and is ignored on inserts and updates. SMS reminders are only available for G Suite customers.",
      "type" : "The type of notification. Possible values are:  \n- \"eventCreation\" - Notification sent when a new event is put on the calendar. \n- \"eventChange\" - Notification sent when an event is changed. \n- \"eventCancellation\" - Notification sent when an event is cancelled. \n- \"eventResponse\" - Notification sent when an attendee responds to the event invitation. \n- \"agenda\" - An agenda with the events of the day (sent out in the morning). Required when adding a notifcaiton."
    } ]
  },
  "deleted" : "Whether this calendar list entry has been deleted from the calendar list. Read-only. Optional. The default is False.",
  "summaryOverride" : "The summary that the authenticated user has set for this calendar. Optional.",
  "defaultReminders" : [ {
    "method" : "The method used by this reminder. Possible values are:  \n- \"email\" - Reminders are sent via email. \n- \"sms\" - Deprecated. Reminders are sent via SMS. These are only available for G Suite customers. Requests to set SMS reminders for other account types are ignored. \n- \"popup\" - Reminders are sent via a UI popup.",
    "minutes" : "Number of minutes before the start of the event when the reminder should trigger. Valid values are between 0 and 40320 (4 weeks in minutes)."
  } ],
  "accessRole" : "The effective access role that the authenticated user has on the calendar. Read-only. Possible values are:  \n- \"freeBusyReader\" - Provides read access to free/busy information. \n- \"reader\" - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden. \n- \"writer\" - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible. \n- \"owner\" - Provides ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs.",
  "etag" : "ETag of the resource.",
  "location" : "Geographic location of the calendar as free-form text. Optional. Read-only.",
  "id" : "Identifier of the calendar.",
  "selected" : "Whether the calendar content shows up in the calendar UI. Optional. The default is False.",
  "primary" : "Whether the calendar is the primary calendar of the authenticated user. Read-only. Optional. The default is False."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### colorRgbFormat

Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.

**Type:** boolean

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_acl_rule

Deletes an access control rule.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### ruleId (required)

ACL rule identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_calendar

Deletes a secondary calendar. Use calendars.clear for clearing all events on primary calendars.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_calendar_event

Deletes an event.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### eventId (required)

Event identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sendNotifications

Deprecated. Use sendUpdates instead

**Type:** boolean

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## delete_calendarlist_entry

Deletes an entry on the user's calendar list.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_acl_rule

Returns an access control rule.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### ruleId (required)

ACL rule identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_acl_rules

Returns the rules in the access control list for the calendar.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### showDeleted

Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to "none". Deleted ACLs will always be included if syncToken is provided. Optional. The default is False.

**Type:** boolean

### syncToken

Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False.
If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.
Learn more about incremental synchronization.
Optional. The default is to return all entries.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_calendar

Returns metadata for a calendar.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_calendar_colors

Returns the color definitions for calendars and events.

<details><summary>Parameters</summary>

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_calendar_event

Returns an event.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### eventId (required)

Event identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### alwaysIncludeEmail

Whether to always include a value in the email field for the organizer, creator and attendees, even if no real email is available (i.e. a generated, non-working value will be provided). The use of this option is discouraged and should only be used by clients which cannot handle the absence of an email address value in the mentioned places. Optional. The default is False.

**Type:** boolean

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### maxAttendees

The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.

**Type:** integer

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### timeZone

Time zone used in the response. Optional. The default is the time zone of the calendar.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_calendar_event_instances

Returns instances of the specified recurring event.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### eventId (required)

Recurring event identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### alwaysIncludeEmail

Whether to always include a value in the email field for the organizer, creator and attendees, even if no real email is available (i.e. a generated, non-working value will be provided). The use of this option is discouraged and should only be used by clients which cannot handle the absence of an email address value in the mentioned places. Optional. The default is False.

**Type:** boolean

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### maxAttendees

The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.

**Type:** integer

### originalStart

The original start time of the instance in the result. Optional.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### showDeleted

Whether to include deleted events (with status equals "cancelled") in the result. Cancelled instances of recurring events will still be included if singleEvents is False. Optional. The default is False.

**Type:** boolean

### timeMax

Upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset.

**Type:** string

### timeMin

Lower bound (inclusive) for an event's end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset.

**Type:** string

### timeZone

Time zone used in the response. Optional. The default is the time zone of the calendar.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_calendar_events

Returns events on the specified calendar.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### alwaysIncludeEmail

Whether to always include a value in the email field for the organizer, creator and attendees, even if no real email is available (i.e. a generated, non-working value will be provided). The use of this option is discouraged and should only be used by clients which cannot handle the absence of an email address value in the mentioned places. Optional. The default is False.

**Type:** boolean

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### iCalUID

Specifies event ID in the iCalendar format to be included in the response. Optional.

**Type:** string

### maxAttendees

The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.

**Type:** integer

### orderBy

The order of the events returned in the result. Optional. The default is an unspecified, stable order. Note that if you want to order by startTime, you must also set the parameter "singleEvents" to true

**Type:** string

**Potential values:** startTime, updated

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### privateExtendedProperty

Extended properties constraint specified as propertyName=value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints.

**Type:** array

```json
[ "string" ]
```

### q

Free text search terms to find events that match these terms in any field, except for extended properties. Optional.

**Type:** string

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sharedExtendedProperty

Extended properties constraint specified as propertyName=value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints.

**Type:** array

```json
[ "string" ]
```

### showDeleted

Whether to include deleted events (with status equals "cancelled") in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False.

**Type:** boolean

### showHiddenInvitations

Whether to include hidden invitations in the result. Optional. The default is False.

**Type:** boolean

### singleEvents

Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False.

**Type:** boolean

### syncToken

Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False.
There are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state.

These are: 
- iCalUID 
- orderBy 
- privateExtendedProperty 
- q 
- sharedExtendedProperty 
- timeMin 
- timeMax 
- updatedMin If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.
Learn more about incremental synchronization.
Optional. The default is to return all entries.

**Type:** string

### timeMax

Upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, e.g., 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but will be ignored. If timeMin is set, timeMax must be greater than timeMin.

**Type:** string

### timeMin

Lower bound (inclusive) for an event's end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, e.g., 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but will be ignored. If timeMax is set, timeMin must be smaller than timeMax.

**Type:** string

### timeZone

Time zone used in the response. Optional. The default is the time zone of the calendar.

**Type:** string

### updatedMin

Lower bound for an event's last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. Optional. The default is not to filter by last modification time.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_calendarlist

Returns entries on the user's calendar list. The CalendarList is a collection of all calendar entries that a user has added to their list (shown in the left panel of the web UI). You can use it to add and remove existing calendars to/from the users’ list. You also use it to retrieve and set the values of user-specific calendar properties, such as default reminders. Another example is foreground color, since different users can have different colors set for the same calendar.

<details><summary>Parameters</summary>

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### minAccessRole

The minimum access role for the user in the returned entries. Optional. The default is no restriction.

**Type:** string

**Potential values:** freeBusyReader, owner, reader, writer

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### showDeleted

Whether to include deleted calendar list entries in the result. Optional. The default is False.

**Type:** boolean

### showHidden

Whether to show hidden entries. Optional. The default is False.

**Type:** boolean

### syncToken

Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. If only read-only fields such as calendar properties or ACLs have changed, the entry won't be returned. All entries deleted and hidden since the previous list request will always be in the result set and it is not allowed to set showDeleted neither showHidden to False.
To ensure client state consistency minAccessRole query parameter cannot be specified together with nextSyncToken.
If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.
Learn more about incremental synchronization.
Optional. The default is to return all entries.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_calendarlist_entry

Returns an entry on the user's calendar list.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_calendars_freebusy

Returns free/busy information for a set of calendars.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "timeMax" : "The end of the interval for the query formatted as per RFC3339.",
  "timeZone" : "Time zone used in the response. Optional. The default is UTC.",
  "calendarExpansionMax" : "Maximal number of calendars for which FreeBusy information is to be provided. Optional. Maximum value is 50.",
  "groupExpansionMax" : "Maximal number of calendar identifiers to be provided for a single group. Optional. An error will be returned for a group with more members than this value. Maximum value if 100.",
  "timeMin" : "The start of the interval for the query formatted as per RFC3339.",
  "items" : [ {
    "id" : "The identifier of a calendar or a group."
  } ]
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_my_settings

Returns all user settings for the authenticated user.

<details><summary>Parameters</summary>

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### syncToken

Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then.
If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.
Learn more about incremental synchronization.
Optional. The default is to return all entries.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_setting

Returns a single user setting.

<details><summary>Parameters</summary>

### setting (required)

The id of the user setting.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## import_calendar_event

Imports an event. This operation is used to add a private copy of an existing event to a calendar.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### $body

**Type:** object

```json
{
  "reminders" : {
    "overrides" : [ {
      "method" : "The method used by this reminder. Possible values are:  \n- \"email\" - Reminders are sent via email. \n- \"sms\" - Deprecated. Reminders are sent via SMS. These are only available for G Suite customers. Requests to set SMS reminders for other account types are ignored. \n- \"popup\" - Reminders are sent via a UI popup.",
      "minutes" : "Number of minutes before the start of the event when the reminder should trigger. Valid values are between 0 and 40320 (4 weeks in minutes)."
    } ],
    "useDefault" : "Whether the default reminders of the calendar apply to the event."
  },
  "attachments" : [ {
    "iconLink" : "URL link to the attachment's icon. Read-only.",
    "fileUrl" : "URL link to the attachment.\nFor adding Google Drive file attachments use the same format as in alternateLink property of the Files resource in the Drive API. Required when adding an attachment.",
    "mimeType" : "Internet media type (MIME type) of the attachment.",
    "title" : "Attachment title.",
    "fileId" : "ID of the attached file. Read-only.\nFor Google Drive files, this is the ID of the corresponding Files resource entry in the Drive API."
  } ],
  "gadget" : {
    "preferences" : "Preferences.",
    "iconLink" : "The gadget's icon URL. The URL scheme must be HTTPS.",
    "display" : "The gadget's display mode. Optional. Possible values are:  \n- \"icon\" - The gadget displays next to the event's title in the calendar view. \n- \"chip\" - The gadget displays when the event is clicked.",
    "link" : "The gadget's URL. The URL scheme must be HTTPS.",
    "width" : "The gadget's width in pixels. The width must be an integer greater than 0. Optional.",
    "title" : "The gadget's title.",
    "type" : "The gadget's type.",
    "height" : "The gadget's height in pixels. The height must be an integer greater than 0. Optional."
  },
  "colorId" : "The color of the event. This is an ID referring to an entry in the event section of the colors definition (see the colors endpoint). Optional.",
  "hangoutLink" : "An absolute link to the Google+ hangout associated with this event. Read-only.",
  "attendeesOmitted" : "Whether attendees may have been omitted from the event's representation. When retrieving an event, this may be due to a restriction specified by the maxAttendee query parameter. When updating an event, this can be used to only update the participant's response. Optional. The default is False.",
  "description" : "Description of the event. Optional.",
  "source" : {
    "title" : "Title of the source; for example a title of a web page or an email subject.",
    "url" : "URL of the source pointing to a resource. The URL scheme must be HTTP or HTTPS."
  },
  "extendedProperties" : {
    "shared" : "Properties that are shared between copies of the event on other attendees' calendars.",
    "private" : "Properties that are private to the copy of the event that appears on this calendar."
  },
  "guestsCanModify" : "Whether attendees other than the organizer can modify the event. Optional. The default is False.",
  "recurringEventId" : "For an instance of a recurring event, this is the id of the recurring event to which this instance belongs. Immutable.",
  "endTimeUnspecified" : "Whether the end time is actually unspecified. An end time is still provided for compatibility reasons, even if this attribute is set to True. The default is False.",
  "guestsCanSeeOtherGuests" : "Whether attendees other than the organizer can see who the event's attendees are. Optional. The default is True.",
  "end" : {
    "date" : "The date, in the format \"yyyy-mm-dd\", if this is an all-day event.",
    "dateTime" : "The time, as a combined date-time value (formatted according to RFC3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.",
    "timeZone" : "The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end."
  },
  "id" : "Opaque identifier of the event. When creating new single or recurring events, you can specify their IDs. Provided IDs must follow these rules:  \n- characters allowed in the ID are those used in base32hex encoding, i.e. lowercase letters a-v and digits 0-9, see section 3.1.2 in RFC2938 \n- the length of the ID must be between 5 and 1024 characters \n- the ID must be unique per calendar  Due to the globally distributed nature of the system, we cannot guarantee that ID collisions will be detected at event creation time. To minimize the risk of collisions we recommend using an established UUID algorithm such as one described in RFC4122.\nIf you do not specify an ID, it will be automatically generated by the server.\nNote that the icalUID and the id are not identical and only one of them should be supplied at event creation time. One difference in their semantics is that in recurring events, all occurrences of one event have different ids while they all share the same icalUIDs.",
  "locked" : "Whether this is a locked event copy where no changes can be made to the main event fields \"summary\", \"description\", \"location\", \"start\", \"end\" or \"recurrence\". The default is False. Read-Only.",
  "anyoneCanAddSelf" : "Whether anyone can invite themselves to the event (currently works for Google+ events only). Optional. The default is False.",
  "summary" : "Title of the event.",
  "creator" : {
    "displayName" : "The creator's name, if available.",
    "self" : "Whether the creator corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.",
    "id" : "The creator's Profile ID, if available. It corresponds to the id field in the People collection of the Google+ API",
    "email" : "The creator's email address, if available."
  },
  "privateCopy" : "Whether this is a private event copy where changes are not shared with other copies on other calendars. Optional. Immutable. The default is False.",
  "visibility" : "Visibility of the event. Optional. Possible values are:  \n- \"default\" - Uses the default visibility for events on the calendar. This is the default value. \n- \"public\" - The event is public and event details are visible to all readers of the calendar. \n- \"private\" - The event is private and only event attendees may view event details. \n- \"confidential\" - The event is private. This value is provided for compatibility reasons.",
  "attendees" : [ {
    "additionalGuests" : "Number of additional guests. Optional. The default is 0.",
    "resource" : "Whether the attendee is a resource. Can only be set when the attendee is added to the event for the first time. Subsequent modifications are ignored. Optional. The default is False.",
    "displayName" : "The attendee's name, if available. Optional.",
    "organizer" : "Whether the attendee is the organizer of the event. Read-only. The default is False.",
    "self" : "Whether this entry represents the calendar on which this copy of the event appears. Read-only. The default is False.",
    "comment" : "The attendee's response comment. Optional.",
    "optional" : "Whether this is an optional attendee. Optional. The default is False.",
    "id" : "The attendee's Profile ID, if available. It corresponds to the id field in the People collection of the Google+ API",
    "responseStatus" : "The attendee's response status. Possible values are:  \n- \"needsAction\" - The attendee has not responded to the invitation. \n- \"declined\" - The attendee has declined the invitation. \n- \"tentative\" - The attendee has tentatively accepted the invitation. \n- \"accepted\" - The attendee has accepted the invitation.",
    "email" : "The attendee's email address, if available. This field must be present when adding an attendee. It must be a valid email address as per RFC5322."
  } ],
  "created" : "Creation time of the event (as a RFC3339 timestamp). Read-only.",
  "htmlLink" : "An absolute link to this event in the Google Calendar Web UI. Read-only.",
  "kind" : "Type of the resource (\"calendar#event\").",
  "iCalUID" : "Event unique identifier as defined in RFC5545. It is used to uniquely identify events accross calendaring systems and must be supplied when importing events via the import method.\nNote that the icalUID and the id are not identical and only one of them should be supplied at event creation time. One difference in their semantics is that in recurring events, all occurrences of one event have different ids while they all share the same icalUIDs.",
  "start" : {
    "date" : "The date, in the format \"yyyy-mm-dd\", if this is an all-day event.",
    "dateTime" : "The time, as a combined date-time value (formatted according to RFC3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.",
    "timeZone" : "The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end."
  },
  "originalStartTime" : {
    "date" : "The date, in the format \"yyyy-mm-dd\", if this is an all-day event.",
    "dateTime" : "The time, as a combined date-time value (formatted according to RFC3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.",
    "timeZone" : "The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end."
  },
  "recurrence" : [ "string" ],
  "sequence" : "Sequence number as per iCalendar.",
  "organizer" : {
    "displayName" : "The organizer's name, if available.",
    "self" : "Whether the organizer corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.",
    "id" : "The organizer's Profile ID, if available. It corresponds to the id field in the People collection of the Google+ API",
    "email" : "The organizer's email address, if available. It must be a valid email address as per RFC5322."
  },
  "transparency" : "Whether the event blocks time on the calendar. Optional. Possible values are:  \n- \"opaque\" - Default value. The event does block time on the calendar. This is equivalent to setting Show me as to Busy in the Calendar UI. \n- \"transparent\" - The event does not block time on the calendar. This is equivalent to setting Show me as to Available in the Calendar UI.",
  "conferenceData" : {
    "entryPoints" : [ {
      "entryPointFeatures" : [ "string" ],
      "password" : "The password to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "regionCode" : "The CLDR/ISO 3166 region code for the country associated with this phone access. Example: \"SE\" for Sweden.\nCalendar backend will populate this field only for EntryPointType.PHONE.",
      "pin" : "The PIN to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "entryPointType" : "The type of the conference entry point.\nPossible values are:  \n- \"video\" - joining a conference over HTTP. A conference can have zero or one video entry point.\n- \"phone\" - joining a conference by dialing a phone number. A conference can have zero or more phone entry points.\n- \"sip\" - joining a conference over SIP. A conference can have zero or one sip entry point.\n- \"more\" - further conference joining instructions, for example additional phone numbers. A conference can have zero or one more entry point. A conference with only a more entry point is not a valid conference.",
      "accessCode" : "The access code to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "meetingCode" : "The meeting code to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "label" : "The label for the URI. Visible to end users. Not localized. The maximum length is 512 characters.\nExamples:  \n- for video: meet.google.com/aaa-bbbb-ccc\n- for phone: +1 123 268 2601\n- for sip: 12345678@altostrat.com\n- for more: should not be filled  \nOptional.",
      "uri" : "The URI of the entry point. The maximum length is 1300 characters.\nFormat:  \n- for video, http: or https: schema is required.\n- for phone, tel: schema is required. The URI should include the entire dial sequence (e.g., tel:+12345678900,,,123456789;1234).\n- for sip, sip: schema is required, e.g., sip:12345678@myprovider.com.\n- for more, http: or https: schema is required.",
      "passcode" : "The passcode to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed."
    } ],
    "notes" : "Additional notes (such as instructions from the domain administrator, legal notices) to display to the user. Can contain HTML. The maximum length is 2048 characters. Optional.",
    "conferenceId" : "The ID of the conference.\nCan be used by developers to keep track of conferences, should not be displayed to users.\nValues for solution types:  \n- \"eventHangout\": unset.\n- \"eventNamedHangout\": the name of the Hangout.\n- \"hangoutsMeet\": the 10-letter meeting code, for example \"aaa-bbbb-ccc\".  Optional.",
    "createRequest" : {
      "requestId" : "The client-generated unique ID for this request.\nClients should regenerate this ID for every new request. If an ID provided is the same as for the previous request, the request is ignored.",
      "conferenceSolutionKey" : {
        "type" : "The conference solution type.\nIf a client encounters an unfamiliar or empty type, it should still be able to display the entry points. However, it should disallow modifications.\nThe possible values are:  \n- \"eventHangout\" for Hangouts for consumers (http://hangouts.google.com)\n- \"eventNamedHangout\" for classic Hangouts for G Suite users (http://hangouts.google.com)\n- \"hangoutsMeet\" for Hangouts Meet (http://meet.google.com)"
      },
      "status" : {
        "statusCode" : "The current status of the conference create request. Read-only.\nThe possible values are:  \n- \"pending\": the conference create request is still being processed.\n- \"success\": the conference create request succeeded, the entry points are populated.\n- \"failure\": the conference create request failed, there are no entry points."
      }
    },
    "signature" : "The signature of the conference data.\nGenereated on server side. Must be preserved while copying the conference data between events, otherwise the conference data will not be copied.\nUnset for a conference with a failed create request.\nOptional for a conference with a pending create request.",
    "conferenceSolution" : {
      "name" : "The user-visible name of this solution. Not localized.",
      "iconUri" : "The user-visible icon for this solution.",
      "key" : {
        "type" : "The conference solution type.\nIf a client encounters an unfamiliar or empty type, it should still be able to display the entry points. However, it should disallow modifications.\nThe possible values are:  \n- \"eventHangout\" for Hangouts for consumers (http://hangouts.google.com)\n- \"eventNamedHangout\" for classic Hangouts for G Suite users (http://hangouts.google.com)\n- \"hangoutsMeet\" for Hangouts Meet (http://meet.google.com)"
      }
    },
    "parameters" : {
      "addOnParameters" : {
        "parameters" : "object"
      }
    }
  },
  "etag" : "ETag of the resource.",
  "location" : "Geographic location of the event as free-form text. Optional.",
  "guestsCanInviteOthers" : "Whether attendees other than the organizer can invite others to the event. Optional. The default is True.",
  "updated" : "Last modification time of the event (as a RFC3339 timestamp). Read-only.",
  "status" : "Status of the event. Optional. Possible values are:  \n- \"confirmed\" - The event is confirmed. This is the default status. \n- \"tentative\" - The event is tentatively confirmed. \n- \"cancelled\" - The event is cancelled (deleted). The list method returns cancelled events only on incremental sync (when syncToken or updatedMin are specified) or if the showDeleted flag is set to true. The get method always returns them.\nA cancelled status represents two different states depending on the event type:  \n- Cancelled exceptions of an uncancelled recurring event indicate that this instance should no longer be presented to the user. Clients should store these events for the lifetime of the parent recurring event.\nCancelled exceptions are only guaranteed to have values for the id, recurringEventId and originalStartTime fields populated. The other fields might be empty.  \n- All other cancelled events represent deleted events. Clients should remove their locally synced copies. Such cancelled events will eventually disappear, so do not rely on them being available indefinitely.\nDeleted events are only guaranteed to have the id field populated.   On the organizer's calendar, cancelled events continue to expose event details (summary, location, etc.) so that they can be restored (undeleted). Similarly, the events to which the user was invited and that they manually removed continue to provide details. However, incremental sync requests with showDeleted set to false will not return these details.\nIf an event changes its organizer (for example via the move operation) and the original organizer is not on the attendee list, it will leave behind a cancelled event where only the id field is guaranteed to be populated."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### conferenceDataVersion

Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.

**Type:** integer

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### supportsAttachments

Whether API client performing operation supports event attachments. Optional. The default is False.

**Type:** boolean

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## move_calendar_event

Moves an event to another calendar, i.e. changes an event's organizer.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier of the source calendar where the event currently is on.

**Type:** string

### destination (required)

Calendar identifier of the target calendar where the event is to be moved to.

**Type:** string

### eventId (required)

Event identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sendNotifications

Deprecated. Use sendUpdates instead

**Type:** boolean

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## quick_add_calendar_event

Creates an event based on a simple text string.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### text (required)

The text describing the event to be created.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sendNotifications

Deprecated. Use sendUpdates instead

**Type:** boolean

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## stop_channel

Stop watching resources through this channel

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "resourceId" : "An opaque ID that identifies the resource being watched on this channel. Stable across different API versions.",
  "address" : "The address where notifications are delivered for this channel.",
  "payload" : "A Boolean value to indicate whether payload is wanted. Optional.",
  "kind" : "Identifies this as a notification channel used to watch for changes to a resource. Value: the fixed string \"api#channel\".",
  "expiration" : "Date and time of notification channel expiration, expressed as a Unix timestamp, in milliseconds. Optional.",
  "id" : "A UUID or similar unique string that identifies this channel.",
  "resourceUri" : "A version-specific identifier for the watched resource.",
  "params" : "Additional parameters controlling delivery channel behavior. Optional.",
  "type" : "The type of delivery mechanism used for this channel.",
  "token" : "An arbitrary string delivered to the target address with each notification delivered over this channel. Optional."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_acl_rule

Updates an access control rule with patch semantics.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### ruleId (required)

ACL rule identifier.

**Type:** string

### $body

**Type:** object

```json
{
  "role" : "The role assigned to the scope. Possible values are:  \n- \"none\" - Provides no access. \n- \"freeBusyReader\" - Provides read access to free/busy information. \n- \"reader\" - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden. \n- \"writer\" - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible. \n- \"owner\" - Provides ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs.",
  "kind" : "Type of the resource (\"calendar#aclRule\").",
  "scope" : {
    "type" : "The type of the scope. Possible values are:  \n- \"default\" - The public scope. This is the default value. \n- \"user\" - Limits the scope to a single user. \n- \"group\" - Limits the scope to a group. \n- \"domain\" - Limits the scope to a domain.  Note: The permissions granted to the \"default\", or public, scope apply to any user, authenticated or not.",
    "value" : "The email address of a user or group, or the name of a domain, depending on the scope type. Omitted for type \"default\"."
  },
  "etag" : "ETag of the resource.",
  "id" : "Identifier of the ACL rule."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sendNotifications

Deprecated. Use sendUpdates instead

**Type:** boolean

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_calendar

Updates some metadata for a calendar, using patch semantics.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### $body

**Type:** object

```json
{
  "conferenceProperties" : {
    "allowedConferenceSolutionTypes" : [ "string" ]
  },
  "summary" : "Title of the calendar. Required on a create_calendar operation",
  "kind" : "Type of the resource (\"calendar#calendar\").",
  "description" : "Description of the calendar. Optional.",
  "timeZone" : "The time zone of the calendar. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) Optional.",
  "etag" : "ETag of the resource.",
  "location" : "Geographic location of the calendar as free-form text. Optional.",
  "id" : "Identifier of the calendar. To retrieve IDs call the get_calendarlist method. Note that when creating a calendar, this field should not be filled out."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_calendar_event

Updates an event with patch semantics.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### eventId (required)

Event identifier.

**Type:** string

### $body

**Type:** object

```json
{
  "reminders" : {
    "overrides" : [ {
      "method" : "The method used by this reminder. Possible values are:  \n- \"email\" - Reminders are sent via email. \n- \"sms\" - Deprecated. Reminders are sent via SMS. These are only available for G Suite customers. Requests to set SMS reminders for other account types are ignored. \n- \"popup\" - Reminders are sent via a UI popup.",
      "minutes" : "Number of minutes before the start of the event when the reminder should trigger. Valid values are between 0 and 40320 (4 weeks in minutes)."
    } ],
    "useDefault" : "Whether the default reminders of the calendar apply to the event."
  },
  "attachments" : [ {
    "iconLink" : "URL link to the attachment's icon. Read-only.",
    "fileUrl" : "URL link to the attachment.\nFor adding Google Drive file attachments use the same format as in alternateLink property of the Files resource in the Drive API. Required when adding an attachment.",
    "mimeType" : "Internet media type (MIME type) of the attachment.",
    "title" : "Attachment title.",
    "fileId" : "ID of the attached file. Read-only.\nFor Google Drive files, this is the ID of the corresponding Files resource entry in the Drive API."
  } ],
  "gadget" : {
    "preferences" : "Preferences.",
    "iconLink" : "The gadget's icon URL. The URL scheme must be HTTPS.",
    "display" : "The gadget's display mode. Optional. Possible values are:  \n- \"icon\" - The gadget displays next to the event's title in the calendar view. \n- \"chip\" - The gadget displays when the event is clicked.",
    "link" : "The gadget's URL. The URL scheme must be HTTPS.",
    "width" : "The gadget's width in pixels. The width must be an integer greater than 0. Optional.",
    "title" : "The gadget's title.",
    "type" : "The gadget's type.",
    "height" : "The gadget's height in pixels. The height must be an integer greater than 0. Optional."
  },
  "colorId" : "The color of the event. This is an ID referring to an entry in the event section of the colors definition (see the colors endpoint). Optional.",
  "hangoutLink" : "An absolute link to the Google+ hangout associated with this event. Read-only.",
  "attendeesOmitted" : "Whether attendees may have been omitted from the event's representation. When retrieving an event, this may be due to a restriction specified by the maxAttendee query parameter. When updating an event, this can be used to only update the participant's response. Optional. The default is False.",
  "description" : "Description of the event. Optional.",
  "source" : {
    "title" : "Title of the source; for example a title of a web page or an email subject.",
    "url" : "URL of the source pointing to a resource. The URL scheme must be HTTP or HTTPS."
  },
  "extendedProperties" : {
    "shared" : "Properties that are shared between copies of the event on other attendees' calendars.",
    "private" : "Properties that are private to the copy of the event that appears on this calendar."
  },
  "guestsCanModify" : "Whether attendees other than the organizer can modify the event. Optional. The default is False.",
  "recurringEventId" : "For an instance of a recurring event, this is the id of the recurring event to which this instance belongs. Immutable.",
  "endTimeUnspecified" : "Whether the end time is actually unspecified. An end time is still provided for compatibility reasons, even if this attribute is set to True. The default is False.",
  "guestsCanSeeOtherGuests" : "Whether attendees other than the organizer can see who the event's attendees are. Optional. The default is True.",
  "end" : {
    "date" : "The date, in the format \"yyyy-mm-dd\", if this is an all-day event.",
    "dateTime" : "The time, as a combined date-time value (formatted according to RFC3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.",
    "timeZone" : "The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end."
  },
  "id" : "Opaque identifier of the event. When creating new single or recurring events, you can specify their IDs. Provided IDs must follow these rules:  \n- characters allowed in the ID are those used in base32hex encoding, i.e. lowercase letters a-v and digits 0-9, see section 3.1.2 in RFC2938 \n- the length of the ID must be between 5 and 1024 characters \n- the ID must be unique per calendar  Due to the globally distributed nature of the system, we cannot guarantee that ID collisions will be detected at event creation time. To minimize the risk of collisions we recommend using an established UUID algorithm such as one described in RFC4122.\nIf you do not specify an ID, it will be automatically generated by the server.\nNote that the icalUID and the id are not identical and only one of them should be supplied at event creation time. One difference in their semantics is that in recurring events, all occurrences of one event have different ids while they all share the same icalUIDs.",
  "locked" : "Whether this is a locked event copy where no changes can be made to the main event fields \"summary\", \"description\", \"location\", \"start\", \"end\" or \"recurrence\". The default is False. Read-Only.",
  "anyoneCanAddSelf" : "Whether anyone can invite themselves to the event (currently works for Google+ events only). Optional. The default is False.",
  "summary" : "Title of the event.",
  "creator" : {
    "displayName" : "The creator's name, if available.",
    "self" : "Whether the creator corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.",
    "id" : "The creator's Profile ID, if available. It corresponds to the id field in the People collection of the Google+ API",
    "email" : "The creator's email address, if available."
  },
  "privateCopy" : "Whether this is a private event copy where changes are not shared with other copies on other calendars. Optional. Immutable. The default is False.",
  "visibility" : "Visibility of the event. Optional. Possible values are:  \n- \"default\" - Uses the default visibility for events on the calendar. This is the default value. \n- \"public\" - The event is public and event details are visible to all readers of the calendar. \n- \"private\" - The event is private and only event attendees may view event details. \n- \"confidential\" - The event is private. This value is provided for compatibility reasons.",
  "attendees" : [ {
    "additionalGuests" : "Number of additional guests. Optional. The default is 0.",
    "resource" : "Whether the attendee is a resource. Can only be set when the attendee is added to the event for the first time. Subsequent modifications are ignored. Optional. The default is False.",
    "displayName" : "The attendee's name, if available. Optional.",
    "organizer" : "Whether the attendee is the organizer of the event. Read-only. The default is False.",
    "self" : "Whether this entry represents the calendar on which this copy of the event appears. Read-only. The default is False.",
    "comment" : "The attendee's response comment. Optional.",
    "optional" : "Whether this is an optional attendee. Optional. The default is False.",
    "id" : "The attendee's Profile ID, if available. It corresponds to the id field in the People collection of the Google+ API",
    "responseStatus" : "The attendee's response status. Possible values are:  \n- \"needsAction\" - The attendee has not responded to the invitation. \n- \"declined\" - The attendee has declined the invitation. \n- \"tentative\" - The attendee has tentatively accepted the invitation. \n- \"accepted\" - The attendee has accepted the invitation.",
    "email" : "The attendee's email address, if available. This field must be present when adding an attendee. It must be a valid email address as per RFC5322."
  } ],
  "created" : "Creation time of the event (as a RFC3339 timestamp). Read-only.",
  "htmlLink" : "An absolute link to this event in the Google Calendar Web UI. Read-only.",
  "kind" : "Type of the resource (\"calendar#event\").",
  "iCalUID" : "Event unique identifier as defined in RFC5545. It is used to uniquely identify events accross calendaring systems and must be supplied when importing events via the import method.\nNote that the icalUID and the id are not identical and only one of them should be supplied at event creation time. One difference in their semantics is that in recurring events, all occurrences of one event have different ids while they all share the same icalUIDs.",
  "start" : {
    "date" : "The date, in the format \"yyyy-mm-dd\", if this is an all-day event.",
    "dateTime" : "The time, as a combined date-time value (formatted according to RFC3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.",
    "timeZone" : "The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end."
  },
  "originalStartTime" : {
    "date" : "The date, in the format \"yyyy-mm-dd\", if this is an all-day event.",
    "dateTime" : "The time, as a combined date-time value (formatted according to RFC3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.",
    "timeZone" : "The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. \"Europe/Zurich\".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end."
  },
  "recurrence" : [ "string" ],
  "sequence" : "Sequence number as per iCalendar.",
  "organizer" : {
    "displayName" : "The organizer's name, if available.",
    "self" : "Whether the organizer corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.",
    "id" : "The organizer's Profile ID, if available. It corresponds to the id field in the People collection of the Google+ API",
    "email" : "The organizer's email address, if available. It must be a valid email address as per RFC5322."
  },
  "transparency" : "Whether the event blocks time on the calendar. Optional. Possible values are:  \n- \"opaque\" - Default value. The event does block time on the calendar. This is equivalent to setting Show me as to Busy in the Calendar UI. \n- \"transparent\" - The event does not block time on the calendar. This is equivalent to setting Show me as to Available in the Calendar UI.",
  "conferenceData" : {
    "entryPoints" : [ {
      "entryPointFeatures" : [ "string" ],
      "password" : "The password to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "regionCode" : "The CLDR/ISO 3166 region code for the country associated with this phone access. Example: \"SE\" for Sweden.\nCalendar backend will populate this field only for EntryPointType.PHONE.",
      "pin" : "The PIN to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "entryPointType" : "The type of the conference entry point.\nPossible values are:  \n- \"video\" - joining a conference over HTTP. A conference can have zero or one video entry point.\n- \"phone\" - joining a conference by dialing a phone number. A conference can have zero or more phone entry points.\n- \"sip\" - joining a conference over SIP. A conference can have zero or one sip entry point.\n- \"more\" - further conference joining instructions, for example additional phone numbers. A conference can have zero or one more entry point. A conference with only a more entry point is not a valid conference.",
      "accessCode" : "The access code to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "meetingCode" : "The meeting code to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed.\nOptional.",
      "label" : "The label for the URI. Visible to end users. Not localized. The maximum length is 512 characters.\nExamples:  \n- for video: meet.google.com/aaa-bbbb-ccc\n- for phone: +1 123 268 2601\n- for sip: 12345678@altostrat.com\n- for more: should not be filled  \nOptional.",
      "uri" : "The URI of the entry point. The maximum length is 1300 characters.\nFormat:  \n- for video, http: or https: schema is required.\n- for phone, tel: schema is required. The URI should include the entire dial sequence (e.g., tel:+12345678900,,,123456789;1234).\n- for sip, sip: schema is required, e.g., sip:12345678@myprovider.com.\n- for more, http: or https: schema is required.",
      "passcode" : "The passcode to access the conference. The maximum length is 128 characters.\nWhen creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password, pin} fields that match the terminology that the conference provider uses. Only the populated fields should be displayed."
    } ],
    "notes" : "Additional notes (such as instructions from the domain administrator, legal notices) to display to the user. Can contain HTML. The maximum length is 2048 characters. Optional.",
    "conferenceId" : "The ID of the conference.\nCan be used by developers to keep track of conferences, should not be displayed to users.\nValues for solution types:  \n- \"eventHangout\": unset.\n- \"eventNamedHangout\": the name of the Hangout.\n- \"hangoutsMeet\": the 10-letter meeting code, for example \"aaa-bbbb-ccc\".  Optional.",
    "createRequest" : {
      "requestId" : "The client-generated unique ID for this request.\nClients should regenerate this ID for every new request. If an ID provided is the same as for the previous request, the request is ignored.",
      "conferenceSolutionKey" : {
        "type" : "The conference solution type.\nIf a client encounters an unfamiliar or empty type, it should still be able to display the entry points. However, it should disallow modifications.\nThe possible values are:  \n- \"eventHangout\" for Hangouts for consumers (http://hangouts.google.com)\n- \"eventNamedHangout\" for classic Hangouts for G Suite users (http://hangouts.google.com)\n- \"hangoutsMeet\" for Hangouts Meet (http://meet.google.com)"
      },
      "status" : {
        "statusCode" : "The current status of the conference create request. Read-only.\nThe possible values are:  \n- \"pending\": the conference create request is still being processed.\n- \"success\": the conference create request succeeded, the entry points are populated.\n- \"failure\": the conference create request failed, there are no entry points."
      }
    },
    "signature" : "The signature of the conference data.\nGenereated on server side. Must be preserved while copying the conference data between events, otherwise the conference data will not be copied.\nUnset for a conference with a failed create request.\nOptional for a conference with a pending create request.",
    "conferenceSolution" : {
      "name" : "The user-visible name of this solution. Not localized.",
      "iconUri" : "The user-visible icon for this solution.",
      "key" : {
        "type" : "The conference solution type.\nIf a client encounters an unfamiliar or empty type, it should still be able to display the entry points. However, it should disallow modifications.\nThe possible values are:  \n- \"eventHangout\" for Hangouts for consumers (http://hangouts.google.com)\n- \"eventNamedHangout\" for classic Hangouts for G Suite users (http://hangouts.google.com)\n- \"hangoutsMeet\" for Hangouts Meet (http://meet.google.com)"
      }
    },
    "parameters" : {
      "addOnParameters" : {
        "parameters" : "object"
      }
    }
  },
  "etag" : "ETag of the resource.",
  "location" : "Geographic location of the event as free-form text. Optional.",
  "guestsCanInviteOthers" : "Whether attendees other than the organizer can invite others to the event. Optional. The default is True.",
  "updated" : "Last modification time of the event (as a RFC3339 timestamp). Read-only.",
  "status" : "Status of the event. Optional. Possible values are:  \n- \"confirmed\" - The event is confirmed. This is the default status. \n- \"tentative\" - The event is tentatively confirmed. \n- \"cancelled\" - The event is cancelled (deleted). The list method returns cancelled events only on incremental sync (when syncToken or updatedMin are specified) or if the showDeleted flag is set to true. The get method always returns them.\nA cancelled status represents two different states depending on the event type:  \n- Cancelled exceptions of an uncancelled recurring event indicate that this instance should no longer be presented to the user. Clients should store these events for the lifetime of the parent recurring event.\nCancelled exceptions are only guaranteed to have values for the id, recurringEventId and originalStartTime fields populated. The other fields might be empty.  \n- All other cancelled events represent deleted events. Clients should remove their locally synced copies. Such cancelled events will eventually disappear, so do not rely on them being available indefinitely.\nDeleted events are only guaranteed to have the id field populated.   On the organizer's calendar, cancelled events continue to expose event details (summary, location, etc.) so that they can be restored (undeleted). Similarly, the events to which the user was invited and that they manually removed continue to provide details. However, incremental sync requests with showDeleted set to false will not return these details.\nIf an event changes its organizer (for example via the move operation) and the original organizer is not on the attendee list, it will leave behind a cancelled event where only the id field is guaranteed to be populated."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### alwaysIncludeEmail

Whether to always include a value in the email field for the organizer, creator and attendees, even if no real email is available (i.e. a generated, non-working value will be provided). The use of this option is discouraged and should only be used by clients which cannot handle the absence of an email address value in the mentioned places. Optional. The default is False.

**Type:** boolean

### conferenceDataVersion

Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event's body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.

**Type:** integer

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### maxAttendees

The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.

**Type:** integer

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sendNotifications

Deprecated. Use sendUpdates instead

**Type:** boolean

### supportsAttachments

Whether API client performing operation supports event attachments. Optional. The default is False.

**Type:** boolean

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_calendarlist_entry

Updates an entry on the user's calendar list, with patch semantics.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### $body

**Type:** object

```json
{
  "conferenceProperties" : {
    "allowedConferenceSolutionTypes" : [ "string" ]
  },
  "summary" : "Title of the calendar. Read-only.",
  "backgroundColor" : "The main color of the calendar in the hexadecimal format \"#0088aa\". This property supersedes the index-based colorId property. To set or change this property, you need to specify colorRgbFormat=true in the parameters of the insert, update and patch methods. Optional.",
  "hidden" : "Whether the calendar has been hidden from the list. Optional. The default is False.",
  "colorId" : "The color of the calendar. This is an ID referring to an entry in the calendar section of the colors definition (see the colors endpoint). This property is superseded by the backgroundColor and foregroundColor properties and can be ignored when using these properties. Optional.",
  "kind" : "Type of the resource (\"calendar#calendarListEntry\").",
  "description" : "Description of the calendar. Optional. Read-only.",
  "timeZone" : "The time zone of the calendar. Optional. Read-only.",
  "foregroundColor" : "The foreground color of the calendar in the hexadecimal format \"#ffffff\". This property supersedes the index-based colorId property. To set or change this property, you need to specify colorRgbFormat=true in the parameters of the insert, update and patch methods. Optional.",
  "notificationSettings" : {
    "notifications" : [ {
      "method" : "The method used to deliver the notification. Possible values are:  \n- \"email\" - Reminders are sent via email. \n- \"sms\" - Deprecated. Reminders are sent via SMS. This value is read-only and is ignored on inserts and updates. SMS reminders are only available for G Suite customers.",
      "type" : "The type of notification. Possible values are:  \n- \"eventCreation\" - Notification sent when a new event is put on the calendar. \n- \"eventChange\" - Notification sent when an event is changed. \n- \"eventCancellation\" - Notification sent when an event is cancelled. \n- \"eventResponse\" - Notification sent when an attendee responds to the event invitation. \n- \"agenda\" - An agenda with the events of the day (sent out in the morning). Required when adding a notifcaiton."
    } ]
  },
  "deleted" : "Whether this calendar list entry has been deleted from the calendar list. Read-only. Optional. The default is False.",
  "summaryOverride" : "The summary that the authenticated user has set for this calendar. Optional.",
  "defaultReminders" : [ {
    "method" : "The method used by this reminder. Possible values are:  \n- \"email\" - Reminders are sent via email. \n- \"sms\" - Deprecated. Reminders are sent via SMS. These are only available for G Suite customers. Requests to set SMS reminders for other account types are ignored. \n- \"popup\" - Reminders are sent via a UI popup.",
    "minutes" : "Number of minutes before the start of the event when the reminder should trigger. Valid values are between 0 and 40320 (4 weeks in minutes)."
  } ],
  "accessRole" : "The effective access role that the authenticated user has on the calendar. Read-only. Possible values are:  \n- \"freeBusyReader\" - Provides read access to free/busy information. \n- \"reader\" - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden. \n- \"writer\" - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible. \n- \"owner\" - Provides ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs.",
  "etag" : "ETag of the resource.",
  "location" : "Geographic location of the calendar as free-form text. Optional. Read-only.",
  "id" : "Identifier of the calendar.",
  "selected" : "Whether the calendar content shows up in the calendar UI. Optional. The default is False.",
  "primary" : "Whether the calendar is the primary calendar of the authenticated user. Read-only. Optional. The default is False."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### colorRgbFormat

Whether to use the foregroundColor and backgroundColor fields to write the calendar colors (RGB). If this feature is used, the index-based colorId field will be set to the best matching option automatically. Optional. The default is False.

**Type:** boolean

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## watch_acl

Watch for changes to ACL resources.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### $body

**Type:** object

```json
{
  "resourceId" : "An opaque ID that identifies the resource being watched on this channel. Stable across different API versions.",
  "address" : "The address where notifications are delivered for this channel.",
  "payload" : "A Boolean value to indicate whether payload is wanted. Optional.",
  "kind" : "Identifies this as a notification channel used to watch for changes to a resource. Value: the fixed string \"api#channel\".",
  "expiration" : "Date and time of notification channel expiration, expressed as a Unix timestamp, in milliseconds. Optional.",
  "id" : "A UUID or similar unique string that identifies this channel.",
  "resourceUri" : "A version-specific identifier for the watched resource.",
  "params" : "Additional parameters controlling delivery channel behavior. Optional.",
  "type" : "The type of delivery mechanism used for this channel.",
  "token" : "An arbitrary string delivered to the target address with each notification delivered over this channel. Optional."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### showDeleted

Whether to include deleted ACLs in the result. Deleted ACLs are represented by role equal to "none". Deleted ACLs will always be included if syncToken is provided. Optional. The default is False.

**Type:** boolean

### syncToken

Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All entries deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False.
If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.
Learn more about incremental synchronization.
Optional. The default is to return all entries.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## watch_calendar_events

Watch for changes to Events resources.

<details><summary>Parameters</summary>

### calendarId (required)

Calendar identifier. To retrieve calendar IDs call the get_calendarlist method. If you want to access the primary calendar of the currently logged in user, use the "primary" keyword.

**Type:** string

### $body

**Type:** object

```json
{
  "resourceId" : "An opaque ID that identifies the resource being watched on this channel. Stable across different API versions.",
  "address" : "The address where notifications are delivered for this channel.",
  "payload" : "A Boolean value to indicate whether payload is wanted. Optional.",
  "kind" : "Identifies this as a notification channel used to watch for changes to a resource. Value: the fixed string \"api#channel\".",
  "expiration" : "Date and time of notification channel expiration, expressed as a Unix timestamp, in milliseconds. Optional.",
  "id" : "A UUID or similar unique string that identifies this channel.",
  "resourceUri" : "A version-specific identifier for the watched resource.",
  "params" : "Additional parameters controlling delivery channel behavior. Optional.",
  "type" : "The type of delivery mechanism used for this channel.",
  "token" : "An arbitrary string delivered to the target address with each notification delivered over this channel. Optional."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### alwaysIncludeEmail

Whether to always include a value in the email field for the organizer, creator and attendees, even if no real email is available (i.e. a generated, non-working value will be provided). The use of this option is discouraged and should only be used by clients which cannot handle the absence of an email address value in the mentioned places. Optional. The default is False.

**Type:** boolean

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### iCalUID

Specifies event ID in the iCalendar format to be included in the response. Optional.

**Type:** string

### maxAttendees

The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.

**Type:** integer

### orderBy

The order of the events returned in the result. Optional. The default is an unspecified, stable order.

**Type:** string

**Potential values:** startTime, updated

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### privateExtendedProperty

Extended properties constraint specified as propertyName=value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints.

**Type:** array

```json
[ "string" ]
```

### q

Free text search terms to find events that match these terms in any field, except for extended properties. Optional.

**Type:** string

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### sharedExtendedProperty

Extended properties constraint specified as propertyName=value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints.

**Type:** array

```json
[ "string" ]
```

### showDeleted

Whether to include deleted events (with status equals "cancelled") in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False.

**Type:** boolean

### showHiddenInvitations

Whether to include hidden invitations in the result. Optional. The default is False.

**Type:** boolean

### singleEvents

Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False.

**Type:** boolean

### syncToken

Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False.
There are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state.

These are:
- iCalUID
- orderBy
- privateExtendedProperty
- q
- sharedExtendedProperty
- timeMin
- timeMax
- updatedMin If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.
Learn more about incremental synchronization.
Optional. The default is to return all entries.

**Type:** string

### timeMax

Upper bound (exclusive) for an event's start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, e.g., 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but will be ignored. If timeMin is set, timeMax must be greater than timeMin.

**Type:** string

### timeMin

Lower bound (inclusive) for an event's end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, e.g., 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but will be ignored. If timeMax is set, timeMin must be smaller than timeMax.

**Type:** string

### timeZone

Time zone used in the response. Optional. The default is the time zone of the calendar.

**Type:** string

### updatedMin

Lower bound for an event's last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. Optional. The default is not to filter by last modification time.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## watch_calendarlist

Watch for changes to CalendarList resources.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "resourceId" : "An opaque ID that identifies the resource being watched on this channel. Stable across different API versions.",
  "address" : "The address where notifications are delivered for this channel.",
  "payload" : "A Boolean value to indicate whether payload is wanted. Optional.",
  "kind" : "Identifies this as a notification channel used to watch for changes to a resource. Value: the fixed string \"api#channel\".",
  "expiration" : "Date and time of notification channel expiration, expressed as a Unix timestamp, in milliseconds. Optional.",
  "id" : "A UUID or similar unique string that identifies this channel.",
  "resourceUri" : "A version-specific identifier for the watched resource.",
  "params" : "Additional parameters controlling delivery channel behavior. Optional.",
  "type" : "The type of delivery mechanism used for this channel.",
  "token" : "An arbitrary string delivered to the target address with each notification delivered over this channel. Optional."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### minAccessRole

The minimum access role for the user in the returned entries. Optional. The default is no restriction.

**Type:** string

**Potential values:** freeBusyReader, owner, reader, writer

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### showDeleted

Whether to include deleted calendar list entries in the result. Optional. The default is False.

**Type:** boolean

### showHidden

Whether to show hidden entries. Optional. The default is False.

**Type:** boolean

### syncToken

Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. If only read-only fields such as calendar properties or ACLs have changed, the entry won't be returned. All entries deleted and hidden since the previous list request will always be in the result set and it is not allowed to set showDeleted neither showHidden to False.
To ensure client state consistency minAccessRole query parameter cannot be specified together with nextSyncToken.
If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.
Learn more about incremental synchronization.
Optional. The default is to return all entries.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## watch_settings

Watch for changes to Settings resources.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "resourceId" : "An opaque ID that identifies the resource being watched on this channel. Stable across different API versions.",
  "address" : "The address where notifications are delivered for this channel.",
  "payload" : "A Boolean value to indicate whether payload is wanted. Optional.",
  "kind" : "Identifies this as a notification channel used to watch for changes to a resource. Value: the fixed string \"api#channel\".",
  "expiration" : "Date and time of notification channel expiration, expressed as a Unix timestamp, in milliseconds. Optional.",
  "id" : "A UUID or similar unique string that identifies this channel.",
  "resourceUri" : "A version-specific identifier for the watched resource.",
  "params" : "Additional parameters controlling delivery channel behavior. Optional.",
  "type" : "The type of delivery mechanism used for this channel.",
  "token" : "An arbitrary string delivered to the target address with each notification delivered over this channel. Optional."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### syncToken

Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then.
If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken.
Learn more about incremental synchronization.
Optional. The default is to return all entries.

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

