---
id: google-directory-documentation
title: Google Directory (version v1.*.*)
sidebar_label: Google Directory
layout: docs.mustache
---

## delete_calendar_resource



<details><summary>Parameters</summary>

#### calendarResourceId (required)

The unique ID of the calendar resource to delete.

**Type:** string

#### customer (required)

The unique ID for the customer's Google account. As an account administrator, you can also use the my_customer alias to represent your account's customer ID.

**Type:** string

</details>

## get_calendar_resource



<details><summary>Parameters</summary>

#### calendarResourceId (required)

The unique ID of the calendar resource to retrieve.

**Type:** string

#### customer (required)

The unique ID for the customer's Google account. As an account administrator, you can also use the my_customer alias to represent your account's customer ID.

**Type:** string

</details>

## insert_calendar_resource



<details><summary>Parameters</summary>

#### customer (required)

The unique ID for the customer's Google account. As an account administrator, you can also use the my_customer alias to represent your account's customer ID.

**Type:** string

#### $body

**Type:** object

</details>

## list_calendar_resources



<details><summary>Parameters</summary>

#### customer (required)

The unique ID for the customer's Google account. As an account administrator, you can also use the my_customer alias to represent your account's customer ID.

**Type:** string

#### maxResults

Maximum number of results to return. Acceptable values are 1 to 500, inclusive.

**Type:** integer

#### pageToken

Token to specify the next page in the list.

**Type:** string

</details>

## update_calendar_resource



<details><summary>Parameters</summary>

#### calendarResourceId (required)

The unique ID of the calendar resource to update.

**Type:** string

#### customer (required)

The unique ID for the customer's Google account. As an account administrator, you can also use the my_customer alias to represent your account's customer ID.

**Type:** string

#### $body

**Type:** object

</details>

