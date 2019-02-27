---
id: google-sheets-documentation
title: Google Sheets (version v1.*.*)
sidebar_label: Google Sheets
---

## append_sheet_values

Appends values to a spreadsheet. The input range is used to search for
existing data and find a "table" within that range. Values will be
appended to the next row of the table, starting with the first column of
the table. See the
[guide](/sheets/api/guides/values#appending_values)
and
[sample code](/sheets/api/samples/writing#append_values)
for specific details of how tables are detected and data is appended.

The caller must specify the spreadsheet ID, range, and
a valueInputOption.  The `valueInputOption` only
controls how the input data will be added to the sheet (column-wise or
row-wise), it does not influence what cell the data starts being written
to.

<details><summary>Parameters</summary>

#### range (required)

The A1 notation of a range to search for a logical table of data.
Values will be appended after the last row of the table.

**Type:** string

#### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

#### valueInputOption (required)

How the input data should be interpreted.

**Type:** string

**Potential values:** INPUT_VALUE_OPTION_UNSPECIFIED, RAW, USER_ENTERED

#### $body

Data within a range of the spreadsheet.

**Type:** object

#### includeValuesInResponse

Determines if the update response should include the values
of the cells that were appended. By default, responses
do not include the updated values.

**Type:** boolean

#### insertDataOption

How the input data should be inserted.

**Type:** string

**Potential values:** OVERWRITE, INSERT_ROWS

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### responseDateTimeRenderOption

Determines how dates, times, and durations in the response should be
rendered. This is ignored if response_value_render_option is
FORMATTED_VALUE.
The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].

**Type:** string

**Potential values:** SERIAL_NUMBER, FORMATTED_STRING

#### responseValueRenderOption

Determines how values in the response should be rendered.
The default render option is ValueRenderOption.FORMATTED_VALUE.

**Type:** string

**Potential values:** FORMATTED_VALUE, UNFORMATTED_VALUE, FORMULA

</details>

## clear_sheet_values

Clears values from a spreadsheet.
The caller must specify the spreadsheet ID and range.
Only values are cleared -- all other properties of the cell (such as
formatting, data validation, etc..) are kept.

<details><summary>Parameters</summary>

#### range (required)

The A1 notation of the values to clear.

**Type:** string

#### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

#### $body

The request for clearing a range of values in a spreadsheet.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## clear_sheet_values_by_data_filter

Clears one or more ranges of values from a spreadsheet.
The caller must specify the spreadsheet ID and one or more
DataFilters. Ranges matching any of the specified data
filters will be cleared.  Only values are cleared -- all other properties
of the cell (such as formatting, data validation, etc..) are kept.

<details><summary>Parameters</summary>

#### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

#### $body

The request for clearing more than one range selected by a
DataFilter in a spreadsheet.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## clear_sheet_values_in_batch

Clears one or more ranges of values from a spreadsheet.
The caller must specify the spreadsheet ID and one or more ranges.
Only values are cleared -- all other properties of the cell (such as
formatting, data validation, etc..) are kept.

<details><summary>Parameters</summary>

#### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

#### $body

The request for clearing more than one range of values in a spreadsheet.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## copy_sheet

Copies a single sheet from a spreadsheet to another spreadsheet.
Returns the properties of the newly created sheet.

<details><summary>Parameters</summary>

#### sheetId (required)

The ID of the sheet to copy.

**Type:** integer

#### spreadsheetId (required)

The ID of the spreadsheet containing the sheet to copy.

**Type:** string

#### $body

The request to copy a sheet across spreadsheets.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## create_sheet

Creates a spreadsheet, returning the newly created spreadsheet.

<details><summary>Parameters</summary>

#### $body

Resource that represents a spreadsheet.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## get_sheet

Returns the spreadsheet at the given ID.
The caller must specify the spreadsheet ID.

By default, data within grids will not be returned.
You can include grid data one of two ways:

* Specify a field mask listing your desired fields using the `fields` URL
parameter in HTTP

* Set the includeGridData
URL parameter to true.  If a field mask is set, the `includeGridData`
parameter is ignored

For large spreadsheets, it is recommended to retrieve only the specific
fields of the spreadsheet that you want.

To retrieve only subsets of the spreadsheet, use the
ranges URL parameter.
Multiple ranges can be specified.  Limiting the range will
return only the portions of the spreadsheet that intersect the requested
ranges. Ranges are specified using A1 notation.

<details><summary>Parameters</summary>

#### spreadsheetId (required)

The spreadsheet to request.

**Type:** string

#### includeGridData

True if grid data should be returned.
This parameter is ignored if a field mask was set in the request.

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### ranges

The ranges to retrieve from the spreadsheet.

**Type:** array

</details>

## get_sheet_by_data_filter

Returns the spreadsheet at the given ID.
The caller must specify the spreadsheet ID.

This method differs from GetSpreadsheet in that it allows selecting
which subsets of spreadsheet data to return by specifying a
dataFilters parameter.
Multiple DataFilters can be specified.  Specifying one or
more data filters will return the portions of the spreadsheet that
intersect ranges matched by any of the filters.

By default, data within grids will not be returned.
You can include grid data one of two ways:

* Specify a field mask listing your desired fields using the `fields` URL
parameter in HTTP

* Set the includeGridData
parameter to true.  If a field mask is set, the `includeGridData`
parameter is ignored

For large spreadsheets, it is recommended to retrieve only the specific
fields of the spreadsheet that you want.

<details><summary>Parameters</summary>

#### spreadsheetId (required)

The spreadsheet to request.

**Type:** string

#### $body

The request for retrieving a Spreadsheet.

**Type:** object

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## get_sheet_metadata

Returns the developer metadata with the specified ID.
The caller must specify the spreadsheet ID and the developer metadata's
unique metadataId.

<details><summary>Parameters</summary>

#### metadataId (required)

The ID of the developer metadata to retrieve.

**Type:** integer

#### spreadsheetId (required)

The ID of the spreadsheet to retrieve metadata from.

**Type:** string

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## get_sheet_values

Returns a range of values from a spreadsheet.
The caller must specify the spreadsheet ID and a range.

<details><summary>Parameters</summary>

#### range (required)

The A1 notation of the values to retrieve.

**Type:** string

#### spreadsheetId (required)

The ID of the spreadsheet to retrieve data from.

**Type:** string

#### dateTimeRenderOption

How dates, times, and durations should be represented in the output.
This is ignored if value_render_option is
FORMATTED_VALUE.
The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].

**Type:** string

**Potential values:** SERIAL_NUMBER, FORMATTED_STRING

#### majorDimension

The major dimension that results should use.

For example, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`,
then requesting `range=A1:B2,majorDimension=ROWS` will return
`[[1,2],[3,4]]`,
whereas requesting `range=A1:B2,majorDimension=COLUMNS` will return
`[[1,3],[2,4]]`.

**Type:** string

**Potential values:** DIMENSION_UNSPECIFIED, ROWS, COLUMNS

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### valueRenderOption

How values should be represented in the output.
The default render option is ValueRenderOption.FORMATTED_VALUE.

**Type:** string

**Potential values:** FORMATTED_VALUE, UNFORMATTED_VALUE, FORMULA

</details>

## get_sheet_values_by_data_filter

Returns one or more ranges of values that match the specified data filters.
The caller must specify the spreadsheet ID and one or more
DataFilters.  Ranges that match any of the data filters in
the request will be returned.

<details><summary>Parameters</summary>

#### spreadsheetId (required)

The ID of the spreadsheet to retrieve data from.

**Type:** string

#### $body

The request for retrieving a range of values in a spreadsheet selected by a
set of DataFilters.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## get_sheet_values_in_batch

Returns one or more ranges of values from a spreadsheet.
The caller must specify the spreadsheet ID and one or more ranges.

<details><summary>Parameters</summary>

#### spreadsheetId (required)

The ID of the spreadsheet to retrieve data from.

**Type:** string

#### dateTimeRenderOption

How dates, times, and durations should be represented in the output.
This is ignored if value_render_option is
FORMATTED_VALUE.
The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].

**Type:** string

**Potential values:** SERIAL_NUMBER, FORMATTED_STRING

#### majorDimension

The major dimension that results should use.

For example, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`,
then requesting `range=A1:B2,majorDimension=ROWS` will return
`[[1,2],[3,4]]`,
whereas requesting `range=A1:B2,majorDimension=COLUMNS` will return
`[[1,3],[2,4]]`.

**Type:** string

**Potential values:** DIMENSION_UNSPECIFIED, ROWS, COLUMNS

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### ranges

The A1 notation of the values to retrieve.

**Type:** array

#### valueRenderOption

How values should be represented in the output.
The default render option is ValueRenderOption.FORMATTED_VALUE.

**Type:** string

**Potential values:** FORMATTED_VALUE, UNFORMATTED_VALUE, FORMULA

</details>

## search_sheet_metadata

Returns all developer metadata matching the specified DataFilter.
If the provided DataFilter represents a DeveloperMetadataLookup object,
this will return all DeveloperMetadata entries selected by it. If the
DataFilter represents a location in a spreadsheet, this will return all
developer metadata associated with locations intersecting that region.

<details><summary>Parameters</summary>

#### spreadsheetId (required)

The ID of the spreadsheet to retrieve metadata from.

**Type:** string

#### $body

A request to retrieve all developer metadata matching the set of specified
criteria.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## update_sheet_in_batch

Applies one or more updates to the spreadsheet.

Each request is validated before
being applied. If any request is not valid then the entire request will
fail and nothing will be applied.

Some requests have replies to
give you some information about how
they are applied. The replies will mirror the requests.  For example,
if you applied 4 updates and the 3rd one had a reply, then the
response will have 2 empty replies, the actual reply, and another empty
reply, in that order.

Due to the collaborative nature of spreadsheets, it is not guaranteed that
the spreadsheet will reflect exactly your changes after this completes,
however it is guaranteed that the updates in the request will be
applied together atomically. Your changes may be altered with respect to
collaborator changes. If there are no collaborators, the spreadsheet
should reflect your changes.

<details><summary>Parameters</summary>

#### spreadsheetId (required)

The spreadsheet to apply the updates to.

**Type:** string

#### $body

The request for updating any aspect of a spreadsheet.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## update_sheet_values

Sets values in a range of a spreadsheet.
The caller must specify the spreadsheet ID, range, and
a valueInputOption.

<details><summary>Parameters</summary>

#### range (required)

The A1 notation of the values to update.

**Type:** string

#### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

#### $body

Data within a range of the spreadsheet.

**Type:** object

#### includeValuesInResponse

Determines if the update response should include the values
of the cells that were updated. By default, responses
do not include the updated values.
If the range to write was larger than than the range actually written,
the response will include all values in the requested range (excluding
trailing empty rows and columns).

**Type:** boolean

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

#### responseDateTimeRenderOption

Determines how dates, times, and durations in the response should be
rendered. This is ignored if response_value_render_option is
FORMATTED_VALUE.
The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].

**Type:** string

**Potential values:** SERIAL_NUMBER, FORMATTED_STRING

#### responseValueRenderOption

Determines how values in the response should be rendered.
The default render option is ValueRenderOption.FORMATTED_VALUE.

**Type:** string

**Potential values:** FORMATTED_VALUE, UNFORMATTED_VALUE, FORMULA

#### valueInputOption

How the input data should be interpreted.

**Type:** string

**Potential values:** INPUT_VALUE_OPTION_UNSPECIFIED, RAW, USER_ENTERED

</details>

## update_sheet_values_by_data_filter

Sets values in one or more ranges of a spreadsheet.
The caller must specify the spreadsheet ID,
a valueInputOption, and one or more
DataFilterValueRanges.

<details><summary>Parameters</summary>

#### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

#### $body

The request for updating more than one range of values in a spreadsheet.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

## update_sheet_values_in_batch

Sets values in one or more ranges of a spreadsheet.
The caller must specify the spreadsheet ID,
a valueInputOption, and one or more
ValueRanges.

<details><summary>Parameters</summary>

#### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

#### $body

The request for updating more than one range of values in a spreadsheet.

**Type:** object

#### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

</details>

