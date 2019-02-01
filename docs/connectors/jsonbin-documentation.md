---
id: jsonbin-documentation
title: JSONbin (version v1.*.*)
sidebar_label: JSONbin
---

## create_bin

Creates a bin

<details><summary>Parameters</summary>

#### $body

Bin content to create

**Type:** object

#### collection-id

In-order to add a bin to a specific collection instead of the unsorted category which is the default, you need to pass the collection-id in the header. You can Create a Collection on the Collections page after signing-in. For more info on Creating Collections, please refer to our Create Collections API.

**Type:** string

#### name

In order to set a name for the Bin, you can pass this header with a name for the bin. There are no restrictions to set the name except for the length which is limited to 128 characters.

**Type:** string

#### private

By default, if you pass the secret-key in the header, it will Create a Private record. In-order to Create a Public record but also list the record you created on your dashboard, you need to pass private: false header along with the secret-key header.

**Type:** boolean

</details>

## create_collection

Creates a collection

<details><summary>Parameters</summary>

#### $body

Collection to create

**Type:** object

</details>

## delete_bin

Delete a bin by ID

<details><summary>Parameters</summary>

#### id (required)

The ID of the bin

**Type:** string

</details>

## get_bin

Get a bin by ID

<details><summary>Parameters</summary>

#### id (required)

The ID of the bin

**Type:** string

</details>

## get_bin_by_version

Get a bin by ID at a specific version

<details><summary>Parameters</summary>

#### id (required)

The ID of the bin

**Type:** string

#### version (required)

The version of the bin; use 'latest' to get the last updated record

**Type:** string

</details>

## update_bin

Update a bin by ID

<details><summary>Parameters</summary>

#### id (required)

The ID of the bin

**Type:** string

#### $body

Bin content to update with

**Type:** object

#### versioning

You need to pass versioning: false header to disable versioning while you are Updating a record. Note that you can disable versioning on Private records only.

**Type:** boolean

</details>

## update_collection

Update a collection by ID

<details><summary>Parameters</summary>

#### id (required)

The ID of the collection

**Type:** string

#### $body

Collection to update with

**Type:** object

</details>

