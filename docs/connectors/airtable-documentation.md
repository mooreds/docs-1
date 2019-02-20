---
id: airtable-documentation
title: Airtable (version v2.*.*)
sidebar_label: Airtable
---

## create_record



<details><summary>Parameters</summary>

#### baseId (required)

The Airtable base ID. This can be found as part of the API documentation URL. Go to https://airtable.com/api and select the base you're interested in, then find the base ID in the resulting URL: https://airtable.com/<baseId>/api/docs.

**Type:** string

#### table (required)

The name of the table being referenced within the base. This table must already exist.

**Type:** string

#### $body

New record to add

**Type:** object

</details>

## delete_record



<details><summary>Parameters</summary>

#### baseId (required)

The Airtable base ID. This can be found as part of the API documentation URL. Go to https://airtable.com/api and select the base you're interested in, then find the base ID in the resulting URL: https://airtable.com/<baseId>/api/docs.

**Type:** string

#### recordId (required)

The record being referenced. Find the record through a get_records call, then find its recordId there.

**Type:** string

#### table (required)

The name of the table being referenced within the base. This table must already exist.

**Type:** string

</details>

## get_record



<details><summary>Parameters</summary>

#### baseId (required)

The Airtable base ID. This can be found as part of the API documentation URL. Go to https://airtable.com/api and select the base you're interested in, then find the base ID in the resulting URL: https://airtable.com/<baseId>/api/docs.

**Type:** string

#### recordId (required)

The record being referenced. Find the record through a get_records call, then find its recordId there.

**Type:** string

#### table (required)

The name of the table being referenced within the base. This table must already exist.

**Type:** string

</details>

## get_records



<details><summary>Parameters</summary>

#### baseId (required)

The Airtable base ID. This can be found as part of the API documentation URL. Go to https://airtable.com/api and select the base you're interested in, then find the base ID in the resulting URL: https://airtable.com/<baseId>/api/docs.

**Type:** string

#### table (required)

The name of the table being referenced within the base. This table must already exist.

**Type:** string

#### cellFormat

The format that should be used for cell values. Supported values are: "json": cells will be formatted as JSON, depending on the field type. "string": cells will be formatted as user-facing strings, regardless of the field type. Note: You should not rely on the format of these strings, as it is subject to change. The default is "json".

**Type:** string

#### filterByFormula

**Type:** string

#### maxRecords

The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total.

**Type:** integer

#### sort

**Type:** array

#### timeZone

The time zone that should be used to format dates when using "string" as the cellFormat. This parameter is required when using "string" as the cellFormat.

**Type:** string

#### userLocale

The user locale that should be used to format dates when using "string" as the cellFormat. This parameter is required when using "string" as the cellFormat.

**Type:** string

#### view

The name or ID of a view in the endpoints table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view.

**Type:** string

</details>

## update_all_fields_of_record

To update all fields of a endpoints record. Any fields that are not included will be cleared.

<details><summary>Parameters</summary>

#### baseId (required)

The Airtable base ID. This can be found as part of the API documentation URL. Go to https://airtable.com/api and select the base you're interested in, then find the base ID in the resulting URL: https://airtable.com/<baseId>/api/docs.

**Type:** string

#### recordId (required)

The record being referenced. Find the record through a get_records call, then find its recordId there.

**Type:** string

#### table (required)

The name of the table being referenced within the base. This table must already exist.

**Type:** string

#### $body

Record to update

**Type:** object

</details>

## update_record

To update some (but not all) fields of a endpoints record. Any fields that are not included will not be updated.

<details><summary>Parameters</summary>

#### baseId (required)

The Airtable base ID. This can be found as part of the API documentation URL. Go to https://airtable.com/api and select the base you're interested in, then find the base ID in the resulting URL: https://airtable.com/<baseId>/api/docs.

**Type:** string

#### recordId (required)

The record being referenced. Find the record through a get_records call, then find its recordId there.

**Type:** string

#### table (required)

The name of the table being referenced within the base. This table must already exist.

**Type:** string

#### $body

Record to update

**Type:** object

</details>

