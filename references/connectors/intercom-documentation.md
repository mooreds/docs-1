---
id: intercom-documentation
title: Intercom (version v1.*.*)
sidebar_label: Intercom
layout: docs.mustache
---

## add_customer_to_conversation



<details><summary>Parameters</summary>

#### conversation_id (required)

Conversation ID

**Type:** string

#### $body

**Type:** object

</details>

## archive_user

Archive a user. The archive action will not perform a 'hard' delete. If you want to permanently delete your user then you will need to use the [**permanent delete API**](https://developers.intercom.com/v2.0/reference#delete-users).

<details><summary>Parameters</summary>

#### email

The email you have defined for the user

**Type:** string

#### user_id

The user id you have defined for the user

**Type:** string

</details>

## convert_lead

Leads can be converted to Users. This is done by passing both Lead and User identifiers. If the User exists, then the Lead will be merged into it, the Lead deleted and the User returned. If the User does not exist, the Lead will be converted to a User, with the User identifiers replacing it's Lead identifiers.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## convert_visitor

Visitors can be converted to Users. This is done by passing both Visitor and User identifiers and a type attribute set to 'user'. If the User exists, then the Visitor will be merged into it, the Visitor deleted and the User returned. If the User does not exist, the Visitor will be converted to a User, with the User identifiers replacing its Visitor identifiers. Visitors can be converted to Leads. This is done by passing Visitor identifiers and a type attribute set to 'lead'.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_company

Create or update a company. Companies are looked up via company_id. If not found via company_id, the new company will be created. If found, that company will be updated.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_event

Create an event.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_lead

Create or update a lead

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_note

Create a note.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_tag

Create a tag by sending a tag object with a name. The tag name may contain whitespace and punctuation. If the same tag name is sent multiple times, only one tag will be created for that name - this lets you avoid checking if a tag exists first. Tag names are case insensitive - 'MyTag' and 'mytag' will result in a single tag being created. Update a tag by submitting a tag object with the id of the tag to update and a new name for the tag. A successful request will update the name value for that tag and return the updated tag in the response. Users can be tagged by supplying a users array. The array contains objects identifying users by their id, email or user_id fields. Companies can be tagged by sending a companies array. The array contains objects identifying companies by their id or company_id fields. Contacts/Leads can be tagged by supplying a users array. The array contains objects identifying leads by their id fields. Companies and user tag directives cannot be mixed in the same request - a request will not process both company and user arrays. We recommend tagging no more than 50 users at a time as larger amounts could result in a timeout. To untag a company or user, each user or company object sent in the tagging request can be submitted with an untag field whose value is set to true. Objects submitted with an untag field can be mixed with other objects being tagged. This allows tag and untag operations to be performed in a single request.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_update_user

Create a new user or update an existing user.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_user

Create a new user or update an existing user.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_company

Delete a company

<details><summary>Parameters</summary>

#### user_id

User ID

**Type:** string

</details>

## delete_company_by_id

Delete a company

<details><summary>Parameters</summary>

#### id (required)

Company ID

**Type:** string

</details>

## delete_customer_to_conversation



<details><summary>Parameters</summary>

#### conversation_id (required)

Conversation ID

**Type:** string

#### id (required)

Customer ID

**Type:** string

</details>

## delete_lead

Delete a lead

<details><summary>Parameters</summary>

#### user_id

User ID

**Type:** string

</details>

## delete_lead_by_id

Delete a lead

<details><summary>Parameters</summary>

#### id (required)

Lead ID

**Type:** string

</details>

## delete_tag

Delete a tag

<details><summary>Parameters</summary>

#### id (required)

Tag ID

**Type:** string

</details>

## delete_visitor

Delete a visitor

<details><summary>Parameters</summary>

#### user_id

User ID

**Type:** string

</details>

## delete_visitor_by_id

Delete a visitor

<details><summary>Parameters</summary>

#### id (required)

Visitor ID

**Type:** string

</details>

## find_user

Find an individual user or many users.

<details><summary>Parameters</summary>

#### email

The email you have defined for the user

**Type:** string

#### user_id

The user id you have defined for the user

**Type:** string

</details>

## get_admin

Get a particular admin

<details><summary>Parameters</summary>

#### id (required)

Admin ID

**Type:** string

</details>

## get_company

Get a company

<details><summary>Parameters</summary>

#### id (required)

Company ID

**Type:** string

</details>

## get_conversation

Get a single conversation.

<details><summary>Parameters</summary>

#### id (required)

Conversation ID

**Type:** string

#### display_as

Set to plaintext to retrieve conversation messages in plain text

**Type:** string

</details>

## get_count



<details><summary>Parameters</summary>

#### count

**Type:** number

#### type

**Type:** string

</details>

## get_current_admin_and_app



*This operation has no parameters*

## get_lead

Get a lead

<details><summary>Parameters</summary>

#### id (required)

Lead ID

**Type:** string

</details>

## get_note

Get a note.

<details><summary>Parameters</summary>

#### id (required)

Note ID

**Type:** string

</details>

## get_segment

Get a segment for an App.

<details><summary>Parameters</summary>

#### id (required)

Segment ID

**Type:** string

#### include_count

include counts in your segment model in the response

**Type:** boolean

</details>

## get_team

Get a particular team

<details><summary>Parameters</summary>

#### id (required)

Team ID

**Type:** string

</details>

## get_user

Get a user

<details><summary>Parameters</summary>

#### id (required)

System-assigned user ID

**Type:** string

</details>

## get_visitor

Get a visitor

<details><summary>Parameters</summary>

#### id (required)

Visitor ID

**Type:** string

</details>

## list_activity_logs_for_admin

Get a log of activities by all admins in an app.

<details><summary>Parameters</summary>

#### created_at_after (required)

The start date that you request data for. It must be formatted as a UNIX timestamp.

**Type:** string

#### created_at_before

The end date that you request data for. It must be formatted as a UNIX timestamp.

**Type:** string

#### resultsPath

**Type:** STRING

</details>

## list_admins

List an App's admins.

<details><summary>Parameters</summary>

#### resultsPath

**Type:** STRING

</details>

## list_companies

List Companies (or list users for company)

<details><summary>Parameters</summary>

#### company_id

Company ID

**Type:** string

#### name

Company name

**Type:** string

#### order

**Type:** string

**Potential values:** asc, desc

#### resultsPath

**Type:** STRING

#### segment_id

**Type:** number

#### tag_id

**Type:** number

#### type

**Type:** string

</details>

## list_conversations

List conversations

<details><summary>Parameters</summary>

#### admin_id

The id for the Admin whose conversations to retrieve. To retrieve all unassigned conversations, set the id to be 'nobody'.

**Type:** string

#### display_as

Set to plaintext to retrieve conversation messages in plain text

**Type:** string

#### email

**Type:** string

#### intercom_user_id

**Type:** string

#### open

when true fetches just open conversations, when false just closed conversations

**Type:** boolean

#### order

**Type:** string

**Potential values:** asc, desc

#### resultsPath

**Type:** STRING

#### sort

**Type:** string

**Potential values:** created_at, updated_at, waiting_since

#### type

The type of entity to query for.

**Type:** string

**Potential values:** admin, user

#### unread

when true fetches just unread conversations

**Type:** boolean

#### user_id

**Type:** string

</details>

## list_data_attributes_for_companies

List all the company data attributes for your app.

<details><summary>Parameters</summary>

#### include_archived

Include archived attributes in the list. By default only non-archived data attributes are returned.

**Type:** boolean

</details>

## list_data_attributes_for_customers

List all data attributes for customers. Customer attributes describe attributes belonging to users, leads and visitors. All 3 models have the same data attributes.

<details><summary>Parameters</summary>

#### include_archived

Include archived attributes in the list. By default only non-archived data attributes are returned.

**Type:** boolean

</details>

## list_events_for_user

List events for a user

<details><summary>Parameters</summary>

#### type (required)

**Type:** string

#### email

**Type:** string

#### intercom_user_id

**Type:** string

#### resultsPath

**Type:** STRING

#### summary

When set to true, event counts are returned grouped by event name.

**Type:** boolean

#### user_id

**Type:** string

</details>

## list_leads

List Leads

<details><summary>Parameters</summary>

#### email

Email address

**Type:** string

#### phone

Phone number

**Type:** string

#### resultsPath

**Type:** STRING

#### user_id

User ID

**Type:** string

</details>

## list_notes_for_user

List notes for a user

<details><summary>Parameters</summary>

#### email

**Type:** string

#### id

**Type:** string

#### resultsPath

**Type:** STRING

#### user_id

**Type:** string

</details>

## list_segments

Get a list of segments for an App.

<details><summary>Parameters</summary>

#### include_count

include counts in your segment model in the response

**Type:** boolean

#### resultsPath

**Type:** STRING

#### type

if "company", list company segments, otherwise list user segments.

**Type:** string

</details>

## list_tags



*This operation has no parameters*

## list_teams

Get a list of teams for an App.

<details><summary>Parameters</summary>

#### resultsPath

**Type:** STRING

</details>

## list_users

Find an individual user or many users.

<details><summary>Parameters</summary>

#### created_since

Limits results to users that were created in that last number of days.

**Type:** number

#### order

Returns the users in ascending or descending order.

**Type:** string

**Potential values:** asc, desc

#### resultsPath

**Type:** STRING

#### sort

What field to sort the results by.

**Type:** string

**Potential values:** created_at, last_request_at, signed_up_at, updated_at

</details>

## list_users_for_company

List users for a company

<details><summary>Parameters</summary>

#### id (required)

Company ID

**Type:** string

#### resultsPath

**Type:** STRING

</details>

## mark_conversation_as_read

Mark a conversation within Intercom as read.

<details><summary>Parameters</summary>

#### id (required)

Conversation ID

**Type:** string

#### $body

**Type:** object

</details>

## post_message



<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## post_reply



<details><summary>Parameters</summary>

#### conversation_id (required)

Conversation ID

**Type:** string

#### $body

**Type:** object

</details>

## post_reply_to_last_conversation



<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## scroll_companies

Scroll over all companies. The List Companies functionality does not work well for huge datasets, and can result in errors and performance problems when paging deeply. The Scroll API provides an efficient mechanism for iterating over all users in a dataset. Each app can only have 1 scroll open at a time. You''ll get an error message if you try to have more than one open per app. If the scroll isn''t used for 1 minute, it expires and calls with that scroll param will fail. If the end of the scroll is reached, \"companies\" will be empty and the scroll parameter will expire. Since scroll is often used on large datasets network errors such as timeouts can be encountered. When this occurs you will need to restart your scroll query as it is not possible to continue from a specific point when using scroll.When this occurs you will see a HTTP 500 error with the following message: “Request failed due to an internal network error. Please restart the scroll operation.”

<details><summary>Parameters</summary>

#### scroll

scroll parameter

**Type:** string

</details>

## scroll_leads

Scroll over all leads. The List Leads functionality does not work well for huge datasets, and can result in errors and performance problems when paging deeply. The Scroll API provides an efficient mechanism for iterating over all users in a dataset. Each app can only have 1 scroll open at a time. You''ll get an error message if you try to have more than one open per app. If the scroll isn''t used for 1 minute, it expires and calls with that scroll param will fail. If the end of the scroll is reached, \"leads\" will be empty and the scroll parameter will expire. Since scroll is often used on large datasets network errors such as timeouts can be encountered. When this occurs you will need to restart your scroll query as it is not possible to continue from a specific point when using scroll.When this occurs you will see a HTTP 500 error with the following message: “Request failed due to an internal network error. Please restart the scroll operation.”

<details><summary>Parameters</summary>

#### scroll

scroll parameter

**Type:** string

</details>

## scroll_users

Scroll over all users. The List Users functionality does not work well for huge datasets, and can result in errors and performance problems when paging deeply. The Scroll API provides an efficient mechanism for iterating over all users in a dataset. Each app can only have 1 scroll open at a time. You''ll get an error message if you try to have more than one open per app. If the scroll isn''t used for 1 minute, it expires and calls with that scroll param will fail. If the end of the scroll is reached, \"users\" will be empty and the scroll parameter will expire. Since scroll is often used on large datasets network errors such as timeouts can be encountered. When this occurs you will need to restart your scroll query as it is not possible to continue from a specific point when using scroll.When this occurs you will see a HTTP 500 error with the following message: “Request failed due to an internal network error. Please restart the scroll operation.”

<details><summary>Parameters</summary>

#### scroll

scroll parameter

**Type:** string

</details>

## set_admin_away

If you want to set an admin in away mode you can do this via a PUT request. You can also choose whether you want conversation replies to be automatically reassigned to your default inbox if you like.

<details><summary>Parameters</summary>

#### id (required)

Admin ID

**Type:** string

#### away_mode_enabled

Set to 'true' to change the status of the admin to away.

**Type:** boolean

#### away_mode_reassign

Set to 'true' to assign any new conversation replies to your default inbox.

**Type:** boolean

</details>

## update_company

Create or update a company. Companies are looked up via company_id. If not found via company_id, the new company will be created. If found, that company will be updated.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## update_lead

Create or update a lead

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## update_tag

Create a tag by sending a tag object with a name. The tag name may contain whitespace and punctuation. If the same tag name is sent multiple times, only one tag will be created for that name - this lets you avoid checking if a tag exists first. Tag names are case insensitive - 'MyTag' and 'mytag' will result in a single tag being created. Update a tag by submitting a tag object with the id of the tag to update and a new name for the tag. A successful request will update the name value for that tag and return the updated tag in the response. Users can be tagged by supplying a users array. The array contains objects identifying users by their id, email or user_id fields. Companies can be tagged by sending a companies array. The array contains objects identifying companies by their id or company_id fields. Contacts/Leads can be tagged by supplying a users array. The array contains objects identifying leads by their id fields. Companies and user tag directives cannot be mixed in the same request - a request will not process both company and user arrays. We recommend tagging no more than 50 users at a time as larger amounts could result in a timeout. To untag a company or user, each user or company object sent in the tagging request can be submitted with an untag field whose value is set to true. Objects submitted with an untag field can be mixed with other objects being tagged. This allows tag and untag operations to be performed in a single request.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## update_visitor

Update a visitor. Passing identifiers (user_id or id) in the body will result in an update of an existing Visitor.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

