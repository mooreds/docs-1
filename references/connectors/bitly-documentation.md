---
id: bitly-documentation
title: Bitly (version v1.*.*)
sidebar_label: Bitly
layout: docs.mustache
---

## add_custom_bitlink

Add a Keyword to a Bitlink

<details><summary>Parameters</summary>

### $body

The object used to add a custom Bitlink

**Type:** object

```json
{
  "bitlink_id" : "string",
  "custom_bitlink" : "string"
}
```

</details>

## create_bitlink

Convert a long url to a Bitlink

<details><summary>Parameters</summary>

### $body

The object used to create a Bitlink

**Type:** object

```json
{
  "group_guid" : "string",
  "domain" : "string",
  "long_url" : "Required string"
}
```

</details>

## create_campaign

Create a new campaign

<details><summary>Parameters</summary>

### $body

The object used for creating/updating a campaign

**Type:** object

```json
{
  "group_guid" : "string",
  "channel_guids" : [ "string" ],
  "name" : "string",
  "description" : "string"
}
```

</details>

## create_channel

Create a new channel

<details><summary>Parameters</summary>

### $body

The object used for creating/updating a channel

**Type:** object

```json
{
  "group_guid" : "string",
  "created" : "ISO TIMESTAMP",
  "name" : "string",
  "guid" : "string",
  "modified" : "ISO_TIMESTAMP",
  "bitlinks" : [ {
    "campaign_guid" : "string",
    "bitlink_id" : "string"
  } ]
}
```

</details>

## create_full_bitlink

Convert a long url to a Bitlink and set additional parameters

<details><summary>Parameters</summary>

### $body

The object used to create a Bitlink

**Type:** object

```json
{
  "group_guid" : "string",
  "deeplinks" : [ {
    "install_url" : "string",
    "app_uri_path" : "string",
    "app_id" : "string",
    "install_type" : "string"
  } ],
  "domain" : "string",
  "title" : "string",
  "long_url" : "Required string",
  "tags" : [ "string" ]
}
```

</details>

## expand_bitlink

This endpoint returns public information for a Bitlink.

<details><summary>Parameters</summary>

### $body

The object used to expand a Bitlink

**Type:** object

```json
{
  "bitlink_id" : "string"
}
```

</details>

## get_bitlink

This endpoint returns information for a Bitlink.

<details><summary>Parameters</summary>

### bitlink (required)

A Bitlink made of the domain and hash

**Type:** string

</details>

## get_campaign

Retrive details for a campaign

<details><summary>Parameters</summary>

### campaign_guid (required)

A GUID for a Bitly campaign

**Type:** string

</details>

## get_channel

Get a channel's details

<details><summary>Parameters</summary>

### channel_guid (required)

A GUID for a Bitly Channel

**Type:** string

</details>

## get_clicks_for_bitlink

This will return the click counts for a specified Bitlink. This returns an array with clicks based on a date.

<details><summary>Parameters</summary>

### bitlink (required)

A Bitlink made of the domain and hash

**Type:** string

### unit (required)

A unit of time

**Type:** string

**Potential values:** minute, hour, day, week, month

### units (required)

An integer representing the time units to query data for. pass -1 to return all units of time.

**Type:** integer

### size

The quantity of items to be be returned

**Type:** integer

### unit_reference

An ISO-8601 timestamp, indicating the most recent time for which to pull metrics. Will default to current time.

**Type:** string

</details>

## get_clicks_summary_for_bitlink

This will return the click counts for a specified Bitlink. This rolls up all the data into a single field of clicks.

<details><summary>Parameters</summary>

### bitlink (required)

A Bitlink made of the domain and hash

**Type:** string

### unit (required)

A unit of time

**Type:** string

**Potential values:** minute, hour, day, week, month

### units (required)

An integer representing the time units to query data for. pass -1 to return all units of time.

**Type:** integer

### size

The quantity of items to be be returned

**Type:** integer

### unit_reference

An ISO-8601 timestamp, indicating the most recent time for which to pull metrics. Will default to current time.

**Type:** string

</details>

## get_custom_bitlink

Retrieve the details and history of a Custom Bitlink

<details><summary>Parameters</summary>

### custom_bitlink (required)

A Custom Bitlink made of the domain and keyword

**Type:** string

</details>

## get_custom_bitlink_metrics_by_destination

Get Click Metrics for a Custom Bitlink by historical Bitlink destinations

<details><summary>Parameters</summary>

### custom_bitlink (required)

A Custom Bitlink made of the domain and keyword

**Type:** string

</details>

## get_group

Retrive details for a group

<details><summary>Parameters</summary>

### group_guid (required)

A GUID for a Bitly group

**Type:** string

</details>

## get_group_metrics_by_countries

This endpoint will return metrics about the countries referring click traffic rolled up to a Group

<details><summary>Parameters</summary>

### group_guid (required)

A GUID for a Bitly group

**Type:** string

</details>

## get_group_metrics_by_referring_networks

This endpoint will return metrics about the referring network click traffic rolled up to a Group

<details><summary>Parameters</summary>

### group_guid (required)

A GUID for a Bitly group

**Type:** string

</details>

## get_group_preferences

Retrieve preferences for a specific group

<details><summary>Parameters</summary>

### group_guid (required)

A GUID for a Bitly group

**Type:** string

</details>

## get_group_shorten_counts

Get all the shorten counts for a specific group

<details><summary>Parameters</summary>

### group_guid (required)

A GUID for a Bitly group

**Type:** string

</details>

## get_metrics_for_bitlink_by_countries

This endpoint will return metrics about the countries referring click traffic to a single Bitlink.

<details><summary>Parameters</summary>

### bitlink (required)

A Bitlink made of the domain and hash

**Type:** string

### unit (required)

A unit of time

**Type:** string

**Potential values:** minute, hour, day, week, month

### units (required)

An integer representing the time units to query data for. pass -1 to return all units of time.

**Type:** integer

### size

The quantity of items to be be returned

**Type:** integer

### unit_reference

An ISO-8601 timestamp, indicating the most recent time for which to pull metrics. Will default to current time.

**Type:** string

</details>

## get_metrics_for_bitlink_by_referrers

This endpoint will return metrics about the referrers referring click traffic to a single Bitlink.

<details><summary>Parameters</summary>

### bitlink (required)

A Bitlink made of the domain and hash

**Type:** string

### unit (required)

A unit of time

**Type:** string

**Potential values:** minute, hour, day, week, month

### units (required)

An integer representing the time units to query data for. pass -1 to return all units of time.

**Type:** integer

### size

The quantity of items to be be returned

**Type:** integer

### unit_reference

An ISO-8601 timestamp, indicating the most recent time for which to pull metrics. Will default to current time.

**Type:** string

</details>

## get_metrics_for_bitlink_by_referrers_by_domains

This endpoint will group referrers metrics about a single Bitlink.

<details><summary>Parameters</summary>

### bitlink (required)

A Bitlink made of the domain and hash

**Type:** string

### unit (required)

A unit of time

**Type:** string

**Potential values:** minute, hour, day, week, month

### units (required)

An integer representing the time units to query data for. pass -1 to return all units of time.

**Type:** integer

### size

The quantity of items to be be returned

**Type:** integer

### unit_reference

An ISO-8601 timestamp, indicating the most recent time for which to pull metrics. Will default to current time.

**Type:** string

</details>

## get_metrics_for_bitlink_by_referring_domains

This endpoint will rollup the click counts to a referrer about a single Bitlink.

<details><summary>Parameters</summary>

### bitlink (required)

A Bitlink made of the domain and hash

**Type:** string

### unit (required)

A unit of time

**Type:** string

**Potential values:** minute, hour, day, week, month

### units (required)

An integer representing the time units to query data for. pass -1 to return all units of time.

**Type:** integer

### size

The quantity of items to be be returned

**Type:** integer

### unit_reference

An ISO-8601 timestamp, indicating the most recent time for which to pull metrics. Will default to current time.

**Type:** string

</details>

## get_oauth_app

Retrieve the details for the provided OAuth App client ID

<details><summary>Parameters</summary>

### client_id (required)

The client ID of an OAuth app

**Type:** string

</details>

## get_organization

Retrive details for an organization

<details><summary>Parameters</summary>

### organization_guid (required)

A GUID for a Bitly organization

**Type:** string

</details>

## get_organization_shorten_counts

Retrieve all the shorten counts for a specific organization

<details><summary>Parameters</summary>

### organization_guid (required)

A GUID for a Bitly organization

**Type:** string

</details>

## get_user



*This operation has no parameters*

## list_bitlinks_by_group

Retrieve a paginated collection of Bitlinks for a Group

<details><summary>Parameters</summary>

### group_guid (required)

A GUID for a Bitly group

**Type:** string

### archived

Whether or not to include archived bitlinks

**Type:** string

**Potential values:** on, off, both

### campaign_guid

Filter to return only links for the given campaign GUID, can be provided

**Type:** string

### channel_guid

Filter to return only links for the given channel GUID, can be provided, overrides all other parameters

**Type:** string

### created_after

Timestamp as an integer unix epoch

**Type:** integer

### created_before

Timestamp as an integer unix epoch

**Type:** integer

### custom_bitlink

**Type:** string

**Potential values:** on, off, both

### deeplinks

Filter to only Bitlinks that contain deeplinks

**Type:** string

**Potential values:** on, off, both

### domain_deeplinks

Filter to only Bitlinks that contain deeplinks configured with a custom domain

**Type:** string

**Potential values:** on, off, both

### encoding_login

Filter by the login of the authenticated user that created the Bitlink

**Type:** array

```json
[ "string" ]
```

### keyword

Custom keyword to filter on history entries

**Type:** string

### modified_after

Timestamp as an integer unix epoch

**Type:** integer

### query

the value that you would like to search

**Type:** string

### tags

filter by given tags

**Type:** array

```json
[ "string" ]
```

</details>

## list_bsds



*This operation has no parameters*

## list_campaigns

Retrieve the campaigns for the current user

<details><summary>Parameters</summary>

### group_guid

A GUID for a Bitly group

**Type:** string

</details>

## list_channels

Retrieve the channels available to a user

<details><summary>Parameters</summary>

### campaign_guid

A GUID for a Bitly campaign

**Type:** string

### group_guid

A GUID for a Bitly group

**Type:** string

</details>

## list_group_tags

Retrieve the currently used tags for a group

<details><summary>Parameters</summary>

### group_guid (required)

A GUID for a Bitly group

**Type:** string

</details>

## list_groups

Retrieve a list of Groups

<details><summary>Parameters</summary>

### organization_guid

A GUID for a Bitly rganization

**Type:** string

</details>

## list_organizations



*This operation has no parameters*

## list_sorted_bitlinks

This will retrieve a paginated response for Bitlinks that are sorted for the Group

<details><summary>Parameters</summary>

### group_guid (required)

A GUID for a Bitly group

**Type:** string

### sort (required)

The type of sorting that you would like to do

**Type:** string

**Potential values:** clicks

### unit (required)

A unit of time

**Type:** string

**Potential values:** minute, hour, day, week, month

### units (required)

An integer representing the time units to query data for. pass -1 to return all units of time.

**Type:** integer

### size

The quantity of items to be be returned

**Type:** integer

### unit_reference

An ISO-8601 timestamp, indicating the most recent time for which to pull metrics. Will default to current time.

**Type:** string

</details>

## update_bitlink

Update fields in the Bitlink

<details><summary>Parameters</summary>

### bitlink (required)

A Bitlink made of the domain and hash

**Type:** string

### $body

The object used to update attributes on a Bitlink

**Type:** object

```json
{
  "references" : "object",
  "archived" : "boolean",
  "deeplinks" : [ {
    "app_guid" : "string",
    "bitlink" : "string",
    "install_url" : "string",
    "os" : "string",
    "created" : "ISO timestamp",
    "app_uri_path" : "string",
    "modified" : "ISO timestamp",
    "guid" : "string",
    "install_type" : "string"
  } ],
  "custom_bitlinks" : [ "string" ],
  "link" : "string",
  "created_at" : "string",
  "id" : "string",
  "title" : "string",
  "long_url" : "string",
  "created_by" : "string",
  "client_id" : "string",
  "tags" : [ "string" ]
}
```

</details>

## update_campaign

Update a campaign's details

<details><summary>Parameters</summary>

### campaign_guid (required)

A GUID for a Bitly campaign

**Type:** string

### $body

The object used for creating/updating a campaign

**Type:** object

```json
{
  "group_guid" : "string",
  "channel_guids" : [ "string" ],
  "name" : "string",
  "description" : "string"
}
```

</details>

## update_channel

Update an existing Channel

<details><summary>Parameters</summary>

### channel_guid (required)

A GUID for a Bitly Channel

**Type:** string

### $body

The object used for creating/updating a channel

**Type:** object

```json
{
  "group_guid" : "string",
  "created" : "ISO TIMESTAMP",
  "name" : "string",
  "guid" : "string",
  "modified" : "ISO_TIMESTAMP",
  "bitlinks" : [ {
    "campaign_guid" : "string",
    "bitlink_id" : "string"
  } ]
}
```

</details>

## update_custom_bitlink

Move a Keyword to a different Bitlink

<details><summary>Parameters</summary>

### custom_bitlink (required)

A Custom Bitlink made of the domain and keyword

**Type:** string

### $body

The object used to update a custom Bitlink

**Type:** object

```json
{
  "bitlink_id" : "string"
}
```

</details>

## update_group

Update the details of a group

<details><summary>Parameters</summary>

### group_guid (required)

A GUID for a Bitly group

**Type:** string

### $body

The object used for updating a group

**Type:** object

```json
{
  "name" : "string",
  "organization_guid" : "string"
}
```

</details>

## update_group_preferences

Update preferences for a specific group

<details><summary>Parameters</summary>

### group_guid (required)

A GUID for a Bitly group

**Type:** string

### $body

The object used to update group preferences

**Type:** object

```json
{
  "group_guid" : "string",
  "domain_preference" : "string"
}
```

</details>

## update_user

Update fields in the user

<details><summary>Parameters</summary>

### $body

The object used for updating a user

**Type:** object

```json
{
  "default_group_guid" : "string",
  "name" : "string"
}
```

</details>

