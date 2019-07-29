---
id: google-sheets-documentation
title: Google Sheets (version v1.*.*)
sidebar_label: Google Sheets
layout: docs.mustache
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

### range (required)

The A1 notation of a range to search for a logical table of data.
Values will be appended after the last row of the table.

**Type:** string

### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

### valueInputOption (required)

How the input data should be interpreted.

**Type:** string

**Potential values:** INPUT_VALUE_OPTION_UNSPECIFIED, RAW, USER_ENTERED

### $body

Data within a range of the spreadsheet.

**Type:** object

```json
{
  "majorDimension" : "The major dimension of the values.\n\nFor output, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`,\nthen requesting `range=A1:B2,majorDimension=ROWS` will return\n`[[1,2],[3,4]]`,\nwhereas requesting `range=A1:B2,majorDimension=COLUMNS` will return\n`[[1,3],[2,4]]`.\n\nFor input, with `range=A1:B2,majorDimension=ROWS` then `[[1,2],[3,4]]`\nwill set `A1=1,B1=2,A2=3,B2=4`. With `range=A1:B2,majorDimension=COLUMNS`\nthen `[[1,2],[3,4]]` will set `A1=1,B1=3,A2=2,B2=4`.\n\nWhen writing, if this field is not set, it defaults to ROWS.",
  "values" : [ [ { } ] ],
  "range" : "The range the values cover, in A1 notation.\nFor output, this range indicates the entire requested range,\neven though the values will exclude trailing rows and columns.\nWhen appending values, this field represents the range to search for a\ntable, after which values will be appended."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeValuesInResponse

Determines if the update response should include the values
of the cells that were appended. By default, responses
do not include the updated values.

**Type:** boolean

### insertDataOption

How the input data should be inserted.

**Type:** string

**Potential values:** OVERWRITE, INSERT_ROWS

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### responseDateTimeRenderOption

Determines how dates, times, and durations in the response should be
rendered. This is ignored if response_value_render_option is
FORMATTED_VALUE.
The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].

**Type:** string

**Potential values:** SERIAL_NUMBER, FORMATTED_STRING

### responseValueRenderOption

Determines how values in the response should be rendered.
The default render option is ValueRenderOption.FORMATTED_VALUE.

**Type:** string

**Potential values:** FORMATTED_VALUE, UNFORMATTED_VALUE, FORMULA

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## clear_sheet_values

Clears values from a spreadsheet.
The caller must specify the spreadsheet ID and range.
Only values are cleared -- all other properties of the cell (such as
formatting, data validation, etc..) are kept.

<details><summary>Parameters</summary>

### range (required)

The A1 notation of the values to clear.

**Type:** string

### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

### $body

The request for clearing a range of values in a spreadsheet.

**Type:** object

```json
{ }
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## clear_sheet_values_by_data_filter

Clears one or more ranges of values from a spreadsheet.
The caller must specify the spreadsheet ID and one or more
DataFilters. Ranges matching any of the specified data
filters will be cleared.  Only values are cleared -- all other properties
of the cell (such as formatting, data validation, etc..) are kept.

<details><summary>Parameters</summary>

### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

### $body

The request for clearing more than one range selected by a
DataFilter in a spreadsheet.

**Type:** object

```json
{
  "dataFilters" : [ {
    "developerMetadataLookup" : {
      "metadataId" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_id.",
      "metadataKey" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_key.",
      "visibility" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.visibility.  If left unspecified, all developer\nmetadata visibile to the requesting project is considered.",
      "metadataValue" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_value.",
      "locationMatchingStrategy" : "Determines how this lookup matches the location.  If this field is\nspecified as EXACT, only developer metadata associated on the exact\nlocation specified is matched.  If this field is specified to INTERSECTING,\ndeveloper metadata associated on intersecting locations is also\nmatched.  If left unspecified, this field assumes a default value of\nINTERSECTING.\nIf this field is specified, a metadataLocation\nmust also be specified.",
      "metadataLocation" : {
        "dimensionRange" : {
          "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
          "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
          "sheetId" : "The sheet this span is on.",
          "dimension" : "The dimension of the span."
        },
        "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
        "locationType" : "The type of location this object represents. This field is read-only.",
        "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
      },
      "locationType" : "Limits the selected developer metadata to those entries which are\nassociated with locations of the specified type.  For example, when this\nfield is specified as ROW this lookup\nonly considers developer metadata associated on rows.  If the field is left\nunspecified, all location types are considered.  This field cannot be\nspecified as SPREADSHEET when\nthe locationMatchingStrategy\nis specified as INTERSECTING or when the\nmetadataLocation is specified as a\nnon-spreadsheet location: spreadsheet metadata cannot intersect any other\ndeveloper metadata location.  This field also must be left unspecified when\nthe locationMatchingStrategy\nis specified as EXACT."
    },
    "gridRange" : {
      "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
      "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
      "sheetId" : "The sheet this range is on.",
      "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
      "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
    },
    "a1Range" : "Selects data that matches the specified A1 range."
  } ]
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## clear_sheet_values_in_batch

Clears one or more ranges of values from a spreadsheet.
The caller must specify the spreadsheet ID and one or more ranges.
Only values are cleared -- all other properties of the cell (such as
formatting, data validation, etc..) are kept.

<details><summary>Parameters</summary>

### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

### $body

The request for clearing more than one range of values in a spreadsheet.

**Type:** object

```json
{
  "ranges" : [ "string" ]
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## copy_sheet

Copies a single sheet from a spreadsheet to another spreadsheet.
Returns the properties of the newly created sheet.

<details><summary>Parameters</summary>

### sheetId (required)

The ID of the sheet to copy.

**Type:** integer

### spreadsheetId (required)

The ID of the spreadsheet containing the sheet to copy.

**Type:** string

### $body

The request to copy a sheet across spreadsheets.

**Type:** object

```json
{
  "destinationSpreadsheetId" : "The ID of the spreadsheet to copy the sheet to."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## create_sheet

Creates a spreadsheet, returning the newly created spreadsheet.

<details><summary>Parameters</summary>

### $body

Resource that represents a spreadsheet.

**Type:** object

```json
{
  "sheets" : [ {
    "conditionalFormats" : [ {
      "gradientRule" : {
        "midpoint" : {
          "color" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "type" : "How the value should be interpreted.",
          "value" : "The value this interpolation point uses.  May be a formula.\nUnused if type is MIN or\nMAX."
        },
        "maxpoint" : {
          "color" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "type" : "How the value should be interpreted.",
          "value" : "The value this interpolation point uses.  May be a formula.\nUnused if type is MIN or\nMAX."
        },
        "minpoint" : {
          "color" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "type" : "How the value should be interpreted.",
          "value" : "The value this interpolation point uses.  May be a formula.\nUnused if type is MIN or\nMAX."
        }
      },
      "ranges" : [ {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      } ],
      "booleanRule" : {
        "condition" : {
          "values" : [ {
            "relativeDate" : "A relative date (based on the current date).\nValid only if the type is\nDATE_BEFORE,\nDATE_AFTER,\nDATE_ON_OR_BEFORE or\nDATE_ON_OR_AFTER.\n\nRelative dates are not supported in data validation.\nThey are supported only in conditional formatting and\nconditional filters.",
            "userEnteredValue" : "A value the condition is based on.\nThe value will be parsed as if the user typed into a cell.\nFormulas are supported (and must begin with an `=`)."
          } ],
          "type" : "The type of condition."
        },
        "format" : {
          "textDirection" : "The direction of the text in the cell.",
          "padding" : {
            "top" : "The top padding of the cell.",
            "left" : "The left padding of the cell.",
            "bottom" : "The bottom padding of the cell.",
            "right" : "The right padding of the cell."
          },
          "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
          "backgroundColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "numberFormat" : {
            "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
            "type" : "The type of the number format.\nWhen writing, this field must be set."
          },
          "wrapStrategy" : "The wrap strategy for the value in the cell.",
          "borders" : {
            "top" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "left" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "bottom" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "right" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            }
          },
          "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
          "textRotation" : {
            "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
            "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
          },
          "verticalAlignment" : "The vertical alignment of the value in the cell.",
          "textFormat" : {
            "fontFamily" : "The font family.",
            "underline" : "True if the text is underlined.",
            "foregroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "fontSize" : "The size of the font.",
            "bold" : "True if the text is bold.",
            "strikethrough" : "True if the text has a strikethrough.",
            "italic" : "True if the text is italicized."
          }
        }
      }
    } ],
    "charts" : [ {
      "chartId" : "The ID of the chart.",
      "position" : {
        "newSheet" : "If true, the embedded object will be put on a new sheet whose ID\nis chosen for you. Used only when writing.",
        "overlayPosition" : {
          "offsetXPixels" : "The horizontal offset, in pixels, that the object is offset\nfrom the anchor cell.",
          "offsetYPixels" : "The vertical offset, in pixels, that the object is offset\nfrom the anchor cell.",
          "heightPixels" : "The height of the object, in pixels. Defaults to 371.",
          "widthPixels" : "The width of the object, in pixels. Defaults to 600.",
          "anchorCell" : {
            "sheetId" : "The sheet this coordinate is on.",
            "rowIndex" : "The row index of the coordinate.",
            "columnIndex" : "The column index of the coordinate."
          }
        },
        "sheetId" : "The sheet this is on. Set only if the embedded object\nis on its own sheet. Must be non-negative."
      },
      "spec" : {
        "basicChart" : {
          "compareMode" : "The behavior of tooltips and data highlighting when hovering on data and\nchart area.",
          "stackedType" : "The stacked type for charts that support vertical stacking.\nApplies to Area, Bar, Column, and Stepped Area charts.",
          "lineSmoothing" : "Gets whether all lines should be rendered smooth or straight by default.\nApplies to Line charts.",
          "threeDimensional" : "True to make the chart 3D.\nApplies to Bar and Column charts.",
          "series" : [ {
            "lineStyle" : {
              "width" : "The thickness of the line, in px.",
              "type" : "The dash type of the line."
            },
            "series" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "targetAxis" : "The minor axis that will specify the range of values for this series.\nFor example, if charting stocks over time, the \"Volume\" series\nmay want to be pinned to the right with the prices pinned to the left,\nbecause the scale of trading volume is different than the scale of\nprices.\nIt is an error to specify an axis that isn't a valid minor axis\nfor the chart's type.",
            "type" : "The type of this series. Valid only if the\nchartType is\nCOMBO.\nDifferent types will change the way the series is visualized.\nOnly LINE, AREA,\nand COLUMN are supported."
          } ],
          "interpolateNulls" : "If some values in a series are missing, gaps may appear in the chart (e.g,\nsegments of lines in a line chart will be missing).  To eliminate these\ngaps set this to true.\nApplies to Line, Area, and Combo charts.",
          "chartType" : "The type of the chart.",
          "domains" : [ {
            "domain" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "reversed" : "True to reverse the order of the domain values (horizontal axis)."
          } ],
          "headerCount" : "The number of rows or columns in the data that are \"headers\".\nIf not set, Google Sheets will guess how many rows are headers based\non the data.\n\n(Note that BasicChartAxis.title may override the axis title\n inferred from the header values.)",
          "legendPosition" : "The position of the chart legend.",
          "axis" : [ {
            "titleTextPosition" : {
              "horizontalAlignment" : "Horizontal alignment setting for the piece of text."
            },
            "format" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            },
            "position" : "The position of this axis.",
            "title" : "The title of this axis. If set, this overrides any title inferred\nfrom headers of the data."
          } ]
        },
        "backgroundColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "waterfallChart" : {
          "hideConnectorLines" : "True to hide connector lines between columns.",
          "stackedType" : "The stacked type.",
          "series" : [ {
            "subtotalColumnsStyle" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "label" : "The label of the column's legend."
            },
            "data" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "negativeColumnsStyle" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "label" : "The label of the column's legend."
            },
            "hideTrailingSubtotal" : "True to hide the subtotal column from the end of the series. By default,\na subtotal column will appear at the end of each series. Setting this\nfield to true will hide that subtotal column for this series.",
            "positiveColumnsStyle" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "label" : "The label of the column's legend."
            },
            "customSubtotals" : [ {
              "dataIsSubtotal" : "True if the data point at subtotal_index is the subtotal. If false,\nthe subtotal will be computed and appear after the data point.",
              "subtotalIndex" : "The 0-based index of a data point within the series. If\ndata_is_subtotal is true, the data point at this index is the\nsubtotal. Otherwise, the subtotal appears after the data point with\nthis index. A series can have multiple subtotals at arbitrary indices,\nbut subtotals do not affect the indices of the data points. For\nexample, if a series has 3 data points, their indices will always be 0,\n1, and 2, regardless of how many subtotals exist on the series or what\ndata points they are associated with.",
              "label" : "A label for the subtotal column."
            } ]
          } ],
          "domain" : {
            "data" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "reversed" : "True to reverse the order of the domain values (horizontal axis)."
          },
          "firstValueIsTotal" : "True to interpret the first value as a total.",
          "connectorLineStyle" : {
            "width" : "The thickness of the line, in px.",
            "type" : "The dash type of the line."
          }
        },
        "altText" : "The alternative text that describes the chart.  This is often used\nfor accessibility.",
        "maximized" : "True to make a chart fill the entire space in which it's rendered with\nminimum padding.  False to use the default padding.\n(Not applicable to Geo and Org charts.)",
        "subtitleTextPosition" : {
          "horizontalAlignment" : "Horizontal alignment setting for the piece of text."
        },
        "title" : "The title of the chart.",
        "bubbleChart" : {
          "bubbleMinRadiusSize" : "The minimum radius size of the bubbles, in pixels.\nIf specific, the field must be a positive value.",
          "bubbleTextStyle" : {
            "fontFamily" : "The font family.",
            "underline" : "True if the text is underlined.",
            "foregroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "fontSize" : "The size of the font.",
            "bold" : "True if the text is bold.",
            "strikethrough" : "True if the text has a strikethrough.",
            "italic" : "True if the text is italicized."
          },
          "series" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "bubbleSizes" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "domain" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "bubbleOpacity" : "The opacity of the bubbles between 0 and 1.0.\n0 is fully transparent and 1 is fully opaque.",
          "bubbleMaxRadiusSize" : "The max radius size of the bubbles, in pixels.\nIf specified, the field must be a positive value.",
          "groupIds" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "bubbleBorderColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "legendPosition" : "Where the legend of the chart should be drawn.",
          "bubbleLabels" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          }
        },
        "titleTextFormat" : {
          "fontFamily" : "The font family.",
          "underline" : "True if the text is underlined.",
          "foregroundColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "fontSize" : "The size of the font.",
          "bold" : "True if the text is bold.",
          "strikethrough" : "True if the text has a strikethrough.",
          "italic" : "True if the text is italicized."
        },
        "histogramChart" : {
          "series" : [ {
            "data" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "barColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            }
          } ],
          "showItemDividers" : "Whether horizontal divider lines should be displayed between items in each\ncolumn.",
          "legendPosition" : "The position of the chart legend.",
          "bucketSize" : "By default the bucket size (the range of values stacked in a single\ncolumn) is chosen automatically, but it may be overridden here.\nE.g., A bucket size of 1.5 results in buckets from 0 - 1.5, 1.5 - 3.0, etc.\nCannot be negative.\nThis field is optional.",
          "outlierPercentile" : "The outlier percentile is used to ensure that outliers do not adversely\naffect the calculation of bucket sizes.  For example, setting an outlier\npercentile of 0.05 indicates that the top and bottom 5% of values when\ncalculating buckets.  The values are still included in the chart, they will\nbe added to the first or last buckets instead of their own buckets.\nMust be between 0.0 and 0.5."
        },
        "fontName" : "The name of the font to use by default for all chart text (e.g. title,\naxis labels, legend).  If a font is specified for a specific part of the\nchart it will override this font name.",
        "subtitleTextFormat" : {
          "fontFamily" : "The font family.",
          "underline" : "True if the text is underlined.",
          "foregroundColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "fontSize" : "The size of the font.",
          "bold" : "True if the text is bold.",
          "strikethrough" : "True if the text has a strikethrough.",
          "italic" : "True if the text is italicized."
        },
        "titleTextPosition" : {
          "horizontalAlignment" : "Horizontal alignment setting for the piece of text."
        },
        "candlestickChart" : {
          "data" : [ {
            "openSeries" : {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              }
            },
            "closeSeries" : {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              }
            },
            "highSeries" : {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              }
            },
            "lowSeries" : {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              }
            }
          } ],
          "domain" : {
            "data" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "reversed" : "True to reverse the order of the domain values (horizontal axis)."
          }
        },
        "orgChart" : {
          "nodeSize" : "The size of the org chart nodes.",
          "parentLabels" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "nodeColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "selectedNodeColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "tooltips" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "labels" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          }
        },
        "subtitle" : "The subtitle of the chart.",
        "pieChart" : {
          "pieHole" : "The size of the hole in the pie chart.",
          "threeDimensional" : "True if the pie is three dimensional.",
          "series" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "domain" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "legendPosition" : "Where the legend of the pie chart should be drawn."
        },
        "hiddenDimensionStrategy" : "Determines how the charts will use hidden rows or columns."
      }
    } ],
    "data" : [ {
      "startRow" : "The first row this GridData refers to, zero-based.",
      "columnMetadata" : [ {
        "hiddenByUser" : "True if this dimension is explicitly hidden.",
        "developerMetadata" : [ {
          "metadataId" : "The spreadsheet-scoped unique ID that identifies the metadata. IDs may be\nspecified when metadata is created, otherwise one will be randomly\ngenerated and assigned. Must be positive.",
          "metadataKey" : "The metadata key. There may be multiple metadata in a spreadsheet with the\nsame key.  Developer metadata must always have a key specified.",
          "visibility" : "The metadata visibility.  Developer metadata must always have a visibility\nspecified.",
          "metadataValue" : "Data associated with the metadata's key.",
          "location" : {
            "dimensionRange" : {
              "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
              "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
              "sheetId" : "The sheet this span is on.",
              "dimension" : "The dimension of the span."
            },
            "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
            "locationType" : "The type of location this object represents. This field is read-only.",
            "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
          }
        } ],
        "hiddenByFilter" : "True if this dimension is being filtered.\nThis field is read-only.",
        "pixelSize" : "The height (if a row) or width (if a column) of the dimension in pixels."
      } ],
      "startColumn" : "The first column this GridData refers to, zero-based.",
      "rowData" : [ {
        "values" : [ {
          "hyperlink" : "A hyperlink this cell points to, if any.\nThis field is read-only.  (To set it, use a `=HYPERLINK` formula\nin the userEnteredValue.formulaValue\nfield.)",
          "note" : "Any note on the cell.",
          "userEnteredFormat" : {
            "textDirection" : "The direction of the text in the cell.",
            "padding" : {
              "top" : "The top padding of the cell.",
              "left" : "The left padding of the cell.",
              "bottom" : "The bottom padding of the cell.",
              "right" : "The right padding of the cell."
            },
            "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
            "backgroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "numberFormat" : {
              "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
              "type" : "The type of the number format.\nWhen writing, this field must be set."
            },
            "wrapStrategy" : "The wrap strategy for the value in the cell.",
            "borders" : {
              "top" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "left" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "bottom" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "right" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              }
            },
            "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
            "textRotation" : {
              "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
              "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
            },
            "verticalAlignment" : "The vertical alignment of the value in the cell.",
            "textFormat" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          },
          "effectiveValue" : {
            "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
            "errorValue" : {
              "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
              "type" : "The type of error."
            },
            "formulaValue" : "Represents a formula.",
            "boolValue" : "Represents a boolean value.",
            "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
          },
          "effectiveFormat" : {
            "textDirection" : "The direction of the text in the cell.",
            "padding" : {
              "top" : "The top padding of the cell.",
              "left" : "The left padding of the cell.",
              "bottom" : "The bottom padding of the cell.",
              "right" : "The right padding of the cell."
            },
            "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
            "backgroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "numberFormat" : {
              "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
              "type" : "The type of the number format.\nWhen writing, this field must be set."
            },
            "wrapStrategy" : "The wrap strategy for the value in the cell.",
            "borders" : {
              "top" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "left" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "bottom" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "right" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              }
            },
            "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
            "textRotation" : {
              "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
              "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
            },
            "verticalAlignment" : "The vertical alignment of the value in the cell.",
            "textFormat" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          },
          "formattedValue" : "The formatted value of the cell.\nThis is the value as it's shown to the user.\nThis field is read-only.",
          "textFormatRuns" : [ {
            "startIndex" : "The character index where this run starts.",
            "format" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          } ],
          "dataValidation" : {
            "condition" : {
              "values" : [ {
                "relativeDate" : "A relative date (based on the current date).\nValid only if the type is\nDATE_BEFORE,\nDATE_AFTER,\nDATE_ON_OR_BEFORE or\nDATE_ON_OR_AFTER.\n\nRelative dates are not supported in data validation.\nThey are supported only in conditional formatting and\nconditional filters.",
                "userEnteredValue" : "A value the condition is based on.\nThe value will be parsed as if the user typed into a cell.\nFormulas are supported (and must begin with an `=`)."
              } ],
              "type" : "The type of condition."
            },
            "inputMessage" : "A message to show the user when adding data to the cell.",
            "showCustomUi" : "True if the UI should be customized based on the kind of condition.\nIf true, \"List\" conditions will show a dropdown.",
            "strict" : "True if invalid data should be rejected."
          },
          "pivotTable" : {
            "valueLayout" : "Whether values should be listed horizontally (as columns)\nor vertically (as rows).",
            "criteria" : "An optional mapping of filters per source column offset.\n\nThe filters will be applied before aggregating data into the pivot table.\nThe map's key is the column offset of the source range that you want to\nfilter, and the value is the criteria for that column.\n\nFor example, if the source was `C10:E15`, a key of `0` will have the filter\nfor column `C`, whereas the key `1` is for column `D`.",
            "columns" : [ {
              "showTotals" : "True if the pivot table should include the totals for this grouping.",
              "valueBucket" : {
                "valuesIndex" : "The offset in the PivotTable.values list which the values in this\ngrouping should be sorted by.",
                "buckets" : [ {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                } ]
              },
              "groupRule" : {
                "histogramRule" : {
                  "start" : "Optional. The minimum value at which items will be placed into buckets\nof constant size. Values below start will be lumped into a single bucket.",
                  "interval" : "Required. The size of the buckets that will be created. Must be positive.",
                  "end" : "Optional. The maximum value at which items will be placed into buckets\nof constant size. Values above end will be lumped into a single bucket."
                },
                "manualRule" : {
                  "groups" : [ {
                    "groupName" : {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    },
                    "items" : [ {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    } ]
                  } ]
                }
              },
              "sortOrder" : "The order the values in this group should be sorted.",
              "valueMetadata" : [ {
                "collapsed" : "True if the data corresponding to the value is collapsed.",
                "value" : {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                }
              } ],
              "label" : "The labels to use for the row/column groups which can be customized. For\nexample, in the following pivot table, the row label is `Region` (which\ncould be renamed to `State`) and the column label is `Product` (which\ncould be renamed `Item`). Pivot tables created before December 2017 do\nnot have header labels. If you'd like to add header labels to an existing\npivot table, please delete the existing pivot table and then create a new\npivot table with same parameters.\n\n    +--------------+---------+-------+\n    | SUM of Units | Product |       |\n    | Region       | Pen     | Paper |\n    +--------------+---------+-------+\n    | New York     |     345 |    98 |\n    | Oregon       |     234 |   123 |\n    | Tennessee    |     531 |   415 |\n    +--------------+---------+-------+\n    | Grand Total  |    1110 |   636 |\n    +--------------+---------+-------+",
              "repeatHeadings" : "True if the headings in this pivot group should be repeated.\nThis is only valid for row groupings and will be ignored by columns.\n\nBy default, we minimize repitition of headings by not showing higher\nlevel headings where they are the same. For example, even though the\nthird row below corresponds to \"Q1 Mar\", \"Q1\" is not shown because\nit is redundant with previous rows. Setting repeat_headings to true\nwould cause \"Q1\" to be repeated for \"Feb\" and \"Mar\".\n\n    +--------------+\n    | Q1     | Jan |\n    |        | Feb |\n    |        | Mar |\n    +--------+-----+\n    | Q1 Total     |\n    +--------------+",
              "sourceColumnOffset" : "The column offset of the source range that this grouping is based on.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this group refers to column `C`, whereas the offset `1` would refer\nto column `D`."
            } ],
            "values" : [ {
              "summarizeFunction" : "A function to summarize the value.\nIf formula is set, the only supported values are\nSUM and\nCUSTOM.\nIf sourceColumnOffset is set, then `CUSTOM`\nis not supported.",
              "name" : "A name to use for the value.",
              "formula" : "A custom formula to calculate the value.  The formula must start\nwith an `=` character.",
              "calculatedDisplayType" : "If specified, indicates that pivot values should be displayed as\nthe result of a calculation with another pivot value. For example, if\ncalculated_display_type is specified as PERCENT_OF_GRAND_TOTAL, all the\npivot values will be displayed as the percentage of the grand total. In\nthe Sheets UI, this is referred to as \"Show As\" in the value section of a\npivot table.",
              "sourceColumnOffset" : "The column offset of the source range that this value reads from.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this value refers to column `C`, whereas the offset `1` would\nrefer to column `D`."
            } ],
            "source" : {
              "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
              "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
              "sheetId" : "The sheet this range is on.",
              "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
              "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
            },
            "rows" : [ {
              "showTotals" : "True if the pivot table should include the totals for this grouping.",
              "valueBucket" : {
                "valuesIndex" : "The offset in the PivotTable.values list which the values in this\ngrouping should be sorted by.",
                "buckets" : [ {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                } ]
              },
              "groupRule" : {
                "histogramRule" : {
                  "start" : "Optional. The minimum value at which items will be placed into buckets\nof constant size. Values below start will be lumped into a single bucket.",
                  "interval" : "Required. The size of the buckets that will be created. Must be positive.",
                  "end" : "Optional. The maximum value at which items will be placed into buckets\nof constant size. Values above end will be lumped into a single bucket."
                },
                "manualRule" : {
                  "groups" : [ {
                    "groupName" : {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    },
                    "items" : [ {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    } ]
                  } ]
                }
              },
              "sortOrder" : "The order the values in this group should be sorted.",
              "valueMetadata" : [ {
                "collapsed" : "True if the data corresponding to the value is collapsed.",
                "value" : {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                }
              } ],
              "label" : "The labels to use for the row/column groups which can be customized. For\nexample, in the following pivot table, the row label is `Region` (which\ncould be renamed to `State`) and the column label is `Product` (which\ncould be renamed `Item`). Pivot tables created before December 2017 do\nnot have header labels. If you'd like to add header labels to an existing\npivot table, please delete the existing pivot table and then create a new\npivot table with same parameters.\n\n    +--------------+---------+-------+\n    | SUM of Units | Product |       |\n    | Region       | Pen     | Paper |\n    +--------------+---------+-------+\n    | New York     |     345 |    98 |\n    | Oregon       |     234 |   123 |\n    | Tennessee    |     531 |   415 |\n    +--------------+---------+-------+\n    | Grand Total  |    1110 |   636 |\n    +--------------+---------+-------+",
              "repeatHeadings" : "True if the headings in this pivot group should be repeated.\nThis is only valid for row groupings and will be ignored by columns.\n\nBy default, we minimize repitition of headings by not showing higher\nlevel headings where they are the same. For example, even though the\nthird row below corresponds to \"Q1 Mar\", \"Q1\" is not shown because\nit is redundant with previous rows. Setting repeat_headings to true\nwould cause \"Q1\" to be repeated for \"Feb\" and \"Mar\".\n\n    +--------------+\n    | Q1     | Jan |\n    |        | Feb |\n    |        | Mar |\n    +--------+-----+\n    | Q1 Total     |\n    +--------------+",
              "sourceColumnOffset" : "The column offset of the source range that this grouping is based on.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this group refers to column `C`, whereas the offset `1` would refer\nto column `D`."
            } ]
          },
          "userEnteredValue" : {
            "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
            "errorValue" : {
              "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
              "type" : "The type of error."
            },
            "formulaValue" : "Represents a formula.",
            "boolValue" : "Represents a boolean value.",
            "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
          }
        } ]
      } ],
      "rowMetadata" : [ {
        "hiddenByUser" : "True if this dimension is explicitly hidden.",
        "developerMetadata" : [ {
          "metadataId" : "The spreadsheet-scoped unique ID that identifies the metadata. IDs may be\nspecified when metadata is created, otherwise one will be randomly\ngenerated and assigned. Must be positive.",
          "metadataKey" : "The metadata key. There may be multiple metadata in a spreadsheet with the\nsame key.  Developer metadata must always have a key specified.",
          "visibility" : "The metadata visibility.  Developer metadata must always have a visibility\nspecified.",
          "metadataValue" : "Data associated with the metadata's key.",
          "location" : {
            "dimensionRange" : {
              "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
              "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
              "sheetId" : "The sheet this span is on.",
              "dimension" : "The dimension of the span."
            },
            "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
            "locationType" : "The type of location this object represents. This field is read-only.",
            "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
          }
        } ],
        "hiddenByFilter" : "True if this dimension is being filtered.\nThis field is read-only.",
        "pixelSize" : "The height (if a row) or width (if a column) of the dimension in pixels."
      } ]
    } ],
    "basicFilter" : {
      "sortSpecs" : [ {
        "sortOrder" : "The order data should be sorted.",
        "dimensionIndex" : "The dimension the sort should be applied to."
      } ],
      "criteria" : "The criteria for showing/hiding values per column.\nThe map's key is the column index, and the value is the criteria for\nthat column.",
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      }
    },
    "filterViews" : [ {
      "filterViewId" : "The ID of the filter view.",
      "sortSpecs" : [ {
        "sortOrder" : "The order data should be sorted.",
        "dimensionIndex" : "The dimension the sort should be applied to."
      } ],
      "namedRangeId" : "The named range this filter view is backed by, if any.\n\nWhen writing, only one of range or named_range_id\nmay be set.",
      "criteria" : "The criteria for showing/hiding values per column.\nThe map's key is the column index, and the value is the criteria for\nthat column.",
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "title" : "The name of the filter view."
    } ],
    "protectedRanges" : [ {
      "namedRangeId" : "The named range this protected range is backed by, if any.\n\nWhen writing, only one of range or named_range_id\nmay be set.",
      "unprotectedRanges" : [ {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      } ],
      "description" : "The description of this protected range.",
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "warningOnly" : "True if this protected range will show a warning when editing.\nWarning-based protection means that every user can edit data in the\nprotected range, except editing will prompt a warning asking the user\nto confirm the edit.\n\nWhen writing: if this field is true, then editors is ignored.\nAdditionally, if this field is changed from true to false and the\n`editors` field is not set (nor included in the field mask), then\nthe editors will be set to all the editors in the document.",
      "requestingUserCanEdit" : "True if the user who requested this protected range can edit the\nprotected area.\nThis field is read-only.",
      "protectedRangeId" : "The ID of the protected range.\nThis field is read-only.",
      "editors" : {
        "domainUsersCanEdit" : "True if anyone in the document's domain has edit access to the protected\nrange.  Domain protection is only supported on documents within a domain.",
        "groups" : [ "string" ],
        "users" : [ "string" ]
      }
    } ],
    "developerMetadata" : [ {
      "metadataId" : "The spreadsheet-scoped unique ID that identifies the metadata. IDs may be\nspecified when metadata is created, otherwise one will be randomly\ngenerated and assigned. Must be positive.",
      "metadataKey" : "The metadata key. There may be multiple metadata in a spreadsheet with the\nsame key.  Developer metadata must always have a key specified.",
      "visibility" : "The metadata visibility.  Developer metadata must always have a visibility\nspecified.",
      "metadataValue" : "Data associated with the metadata's key.",
      "location" : {
        "dimensionRange" : {
          "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
          "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
          "sheetId" : "The sheet this span is on.",
          "dimension" : "The dimension of the span."
        },
        "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
        "locationType" : "The type of location this object represents. This field is read-only.",
        "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
      }
    } ],
    "bandedRanges" : [ {
      "bandedRangeId" : "The id of the banded range.",
      "rowProperties" : {
        "headerColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "footerColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "firstBandColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "secondBandColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        }
      },
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "columnProperties" : {
        "headerColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "footerColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "firstBandColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "secondBandColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        }
      }
    } ],
    "properties" : {
      "hidden" : "True if the sheet is hidden in the UI, false if it's visible.",
      "sheetType" : "The type of sheet. Defaults to GRID.\nThis field cannot be changed once set.",
      "index" : "The index of the sheet within the spreadsheet.\nWhen adding or updating sheet properties, if this field\nis excluded then the sheet will be added or moved to the end\nof the sheet list. When updating sheet indices or inserting\nsheets, movement is considered in \"before the move\" indexes.\nFor example, if there were 3 sheets (S1, S2, S3) in order to\nmove S1 ahead of S2 the index would have to be set to 2. A sheet\nindex update request will be ignored if the requested index is\nidentical to the sheets current index or if the requested new\nindex is equal to the current sheet index + 1.",
      "sheetId" : "The ID of the sheet. Must be non-negative.\nThis field cannot be changed once set.",
      "rightToLeft" : "True if the sheet is an RTL sheet instead of an LTR sheet.",
      "title" : "The name of the sheet.",
      "tabColor" : {
        "red" : "The amount of red in the color as a value in the interval [0, 1].",
        "green" : "The amount of green in the color as a value in the interval [0, 1].",
        "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
        "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
      },
      "gridProperties" : {
        "frozenRowCount" : "The number of rows that are frozen in the grid.",
        "frozenColumnCount" : "The number of columns that are frozen in the grid.",
        "hideGridlines" : "True if the grid isn't showing gridlines in the UI.",
        "columnCount" : "The number of columns in the grid.",
        "rowCount" : "The number of rows in the grid."
      }
    },
    "merges" : [ {
      "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
      "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
      "sheetId" : "The sheet this range is on.",
      "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
      "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
    } ]
  } ],
  "spreadsheetUrl" : "The url of the spreadsheet.\nThis field is read-only.",
  "namedRanges" : [ {
    "namedRangeId" : "The ID of the named range.",
    "name" : "The name of the named range.",
    "range" : {
      "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
      "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
      "sheetId" : "The sheet this range is on.",
      "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
      "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
    }
  } ],
  "developerMetadata" : [ {
    "metadataId" : "The spreadsheet-scoped unique ID that identifies the metadata. IDs may be\nspecified when metadata is created, otherwise one will be randomly\ngenerated and assigned. Must be positive.",
    "metadataKey" : "The metadata key. There may be multiple metadata in a spreadsheet with the\nsame key.  Developer metadata must always have a key specified.",
    "visibility" : "The metadata visibility.  Developer metadata must always have a visibility\nspecified.",
    "metadataValue" : "Data associated with the metadata's key.",
    "location" : {
      "dimensionRange" : {
        "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
        "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
        "sheetId" : "The sheet this span is on.",
        "dimension" : "The dimension of the span."
      },
      "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
      "locationType" : "The type of location this object represents. This field is read-only.",
      "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
    }
  } ],
  "spreadsheetId" : "The ID of the spreadsheet.\nThis field is read-only.",
  "properties" : {
    "autoRecalc" : "The amount of time to wait before volatile functions are recalculated.",
    "timeZone" : "The time zone of the spreadsheet, in CLDR format such as\n`America/New_York`. If the time zone isn't recognized, this may\nbe a custom time zone such as `GMT-07:00`.",
    "iterativeCalculationSettings" : {
      "maxIterations" : "When iterative calculation is enabled, the maximum number of calculation\nrounds to perform.",
      "convergenceThreshold" : "When iterative calculation is enabled and successive results differ by\nless than this threshold value, the calculation rounds stop."
    },
    "title" : "The title of the spreadsheet.",
    "locale" : "The locale of the spreadsheet in one of the following formats:\n\n* an ISO 639-1 language code such as `en`\n\n* an ISO 639-2 language code such as `fil`, if no 639-1 code exists\n\n* a combination of the ISO language code and country code, such as `en_US`\n\nNote: when updating this field, not all locales/languages are supported.",
    "defaultFormat" : {
      "textDirection" : "The direction of the text in the cell.",
      "padding" : {
        "top" : "The top padding of the cell.",
        "left" : "The left padding of the cell.",
        "bottom" : "The bottom padding of the cell.",
        "right" : "The right padding of the cell."
      },
      "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
      "backgroundColor" : {
        "red" : "The amount of red in the color as a value in the interval [0, 1].",
        "green" : "The amount of green in the color as a value in the interval [0, 1].",
        "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
        "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
      },
      "numberFormat" : {
        "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
        "type" : "The type of the number format.\nWhen writing, this field must be set."
      },
      "wrapStrategy" : "The wrap strategy for the value in the cell.",
      "borders" : {
        "top" : {
          "color" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
          "style" : "The style of the border."
        },
        "left" : {
          "color" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
          "style" : "The style of the border."
        },
        "bottom" : {
          "color" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
          "style" : "The style of the border."
        },
        "right" : {
          "color" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
          "style" : "The style of the border."
        }
      },
      "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
      "textRotation" : {
        "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
        "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
      },
      "verticalAlignment" : "The vertical alignment of the value in the cell.",
      "textFormat" : {
        "fontFamily" : "The font family.",
        "underline" : "True if the text is underlined.",
        "foregroundColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "fontSize" : "The size of the font.",
        "bold" : "True if the text is bold.",
        "strikethrough" : "True if the text has a strikethrough.",
        "italic" : "True if the text is italicized."
      }
    }
  }
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

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

### spreadsheetId (required)

The spreadsheet to request.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeGridData

True if grid data should be returned.
This parameter is ignored if a field mask was set in the request.

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### ranges

The ranges to retrieve from the spreadsheet.

**Type:** array

```json
[ "string" ]
```

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

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

### spreadsheetId (required)

The spreadsheet to request.

**Type:** string

### $body

The request for retrieving a Spreadsheet.

**Type:** object

```json
{
  "dataFilters" : [ {
    "developerMetadataLookup" : {
      "metadataId" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_id.",
      "metadataKey" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_key.",
      "visibility" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.visibility.  If left unspecified, all developer\nmetadata visibile to the requesting project is considered.",
      "metadataValue" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_value.",
      "locationMatchingStrategy" : "Determines how this lookup matches the location.  If this field is\nspecified as EXACT, only developer metadata associated on the exact\nlocation specified is matched.  If this field is specified to INTERSECTING,\ndeveloper metadata associated on intersecting locations is also\nmatched.  If left unspecified, this field assumes a default value of\nINTERSECTING.\nIf this field is specified, a metadataLocation\nmust also be specified.",
      "metadataLocation" : {
        "dimensionRange" : {
          "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
          "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
          "sheetId" : "The sheet this span is on.",
          "dimension" : "The dimension of the span."
        },
        "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
        "locationType" : "The type of location this object represents. This field is read-only.",
        "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
      },
      "locationType" : "Limits the selected developer metadata to those entries which are\nassociated with locations of the specified type.  For example, when this\nfield is specified as ROW this lookup\nonly considers developer metadata associated on rows.  If the field is left\nunspecified, all location types are considered.  This field cannot be\nspecified as SPREADSHEET when\nthe locationMatchingStrategy\nis specified as INTERSECTING or when the\nmetadataLocation is specified as a\nnon-spreadsheet location: spreadsheet metadata cannot intersect any other\ndeveloper metadata location.  This field also must be left unspecified when\nthe locationMatchingStrategy\nis specified as EXACT."
    },
    "gridRange" : {
      "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
      "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
      "sheetId" : "The sheet this range is on.",
      "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
      "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
    },
    "a1Range" : "Selects data that matches the specified A1 range."
  } ],
  "includeGridData" : "True if grid data should be returned.\nThis parameter is ignored if a field mask was set in the request."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## get_sheet_metadata

Returns the developer metadata with the specified ID.
The caller must specify the spreadsheet ID and the developer metadata's
unique metadataId.

<details><summary>Parameters</summary>

### metadataId (required)

The ID of the developer metadata to retrieve.

**Type:** integer

### spreadsheetId (required)

The ID of the spreadsheet to retrieve metadata from.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## get_sheet_values

Returns a range of values from a spreadsheet.
The caller must specify the spreadsheet ID and a range.

<details><summary>Parameters</summary>

### range (required)

The A1 notation of the values to retrieve.

**Type:** string

### spreadsheetId (required)

The ID of the spreadsheet to retrieve data from.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### dateTimeRenderOption

How dates, times, and durations should be represented in the output.
This is ignored if value_render_option is
FORMATTED_VALUE.
The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].

**Type:** string

**Potential values:** SERIAL_NUMBER, FORMATTED_STRING

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### majorDimension

The major dimension that results should use.

For example, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`,
then requesting `range=A1:B2,majorDimension=ROWS` will return
`[[1,2],[3,4]]`,
whereas requesting `range=A1:B2,majorDimension=COLUMNS` will return
`[[1,3],[2,4]]`.

**Type:** string

**Potential values:** DIMENSION_UNSPECIFIED, ROWS, COLUMNS

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

### valueRenderOption

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

### spreadsheetId (required)

The ID of the spreadsheet to retrieve data from.

**Type:** string

### $body

The request for retrieving a range of values in a spreadsheet selected by a
set of DataFilters.

**Type:** object

```json
{
  "majorDimension" : "The major dimension that results should use.\n\nFor example, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`,\nthen a request that selects that range and sets `majorDimension=ROWS` will\nreturn `[[1,2],[3,4]]`,\nwhereas a request that sets `majorDimension=COLUMNS` will return\n`[[1,3],[2,4]]`.",
  "valueRenderOption" : "How values should be represented in the output.\nThe default render option is ValueRenderOption.FORMATTED_VALUE.",
  "dataFilters" : [ {
    "developerMetadataLookup" : {
      "metadataId" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_id.",
      "metadataKey" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_key.",
      "visibility" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.visibility.  If left unspecified, all developer\nmetadata visibile to the requesting project is considered.",
      "metadataValue" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_value.",
      "locationMatchingStrategy" : "Determines how this lookup matches the location.  If this field is\nspecified as EXACT, only developer metadata associated on the exact\nlocation specified is matched.  If this field is specified to INTERSECTING,\ndeveloper metadata associated on intersecting locations is also\nmatched.  If left unspecified, this field assumes a default value of\nINTERSECTING.\nIf this field is specified, a metadataLocation\nmust also be specified.",
      "metadataLocation" : {
        "dimensionRange" : {
          "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
          "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
          "sheetId" : "The sheet this span is on.",
          "dimension" : "The dimension of the span."
        },
        "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
        "locationType" : "The type of location this object represents. This field is read-only.",
        "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
      },
      "locationType" : "Limits the selected developer metadata to those entries which are\nassociated with locations of the specified type.  For example, when this\nfield is specified as ROW this lookup\nonly considers developer metadata associated on rows.  If the field is left\nunspecified, all location types are considered.  This field cannot be\nspecified as SPREADSHEET when\nthe locationMatchingStrategy\nis specified as INTERSECTING or when the\nmetadataLocation is specified as a\nnon-spreadsheet location: spreadsheet metadata cannot intersect any other\ndeveloper metadata location.  This field also must be left unspecified when\nthe locationMatchingStrategy\nis specified as EXACT."
    },
    "gridRange" : {
      "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
      "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
      "sheetId" : "The sheet this range is on.",
      "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
      "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
    },
    "a1Range" : "Selects data that matches the specified A1 range."
  } ],
  "dateTimeRenderOption" : "How dates, times, and durations should be represented in the output.\nThis is ignored if value_render_option is\nFORMATTED_VALUE.\nThe default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER]."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## get_sheet_values_in_batch

Returns one or more ranges of values from a spreadsheet.
The caller must specify the spreadsheet ID and one or more ranges.

<details><summary>Parameters</summary>

### spreadsheetId (required)

The ID of the spreadsheet to retrieve data from.

**Type:** string

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### dateTimeRenderOption

How dates, times, and durations should be represented in the output.
This is ignored if value_render_option is
FORMATTED_VALUE.
The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].

**Type:** string

**Potential values:** SERIAL_NUMBER, FORMATTED_STRING

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### majorDimension

The major dimension that results should use.

For example, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`,
then requesting `range=A1:B2,majorDimension=ROWS` will return
`[[1,2],[3,4]]`,
whereas requesting `range=A1:B2,majorDimension=COLUMNS` will return
`[[1,3],[2,4]]`.

**Type:** string

**Potential values:** DIMENSION_UNSPECIFIED, ROWS, COLUMNS

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### ranges

The A1 notation of the values to retrieve.

**Type:** array

```json
[ "string" ]
```

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

### valueRenderOption

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

### spreadsheetId (required)

The ID of the spreadsheet to retrieve metadata from.

**Type:** string

### $body

A request to retrieve all developer metadata matching the set of specified
criteria.

**Type:** object

```json
{
  "dataFilters" : [ {
    "developerMetadataLookup" : {
      "metadataId" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_id.",
      "metadataKey" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_key.",
      "visibility" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.visibility.  If left unspecified, all developer\nmetadata visibile to the requesting project is considered.",
      "metadataValue" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_value.",
      "locationMatchingStrategy" : "Determines how this lookup matches the location.  If this field is\nspecified as EXACT, only developer metadata associated on the exact\nlocation specified is matched.  If this field is specified to INTERSECTING,\ndeveloper metadata associated on intersecting locations is also\nmatched.  If left unspecified, this field assumes a default value of\nINTERSECTING.\nIf this field is specified, a metadataLocation\nmust also be specified.",
      "metadataLocation" : {
        "dimensionRange" : {
          "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
          "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
          "sheetId" : "The sheet this span is on.",
          "dimension" : "The dimension of the span."
        },
        "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
        "locationType" : "The type of location this object represents. This field is read-only.",
        "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
      },
      "locationType" : "Limits the selected developer metadata to those entries which are\nassociated with locations of the specified type.  For example, when this\nfield is specified as ROW this lookup\nonly considers developer metadata associated on rows.  If the field is left\nunspecified, all location types are considered.  This field cannot be\nspecified as SPREADSHEET when\nthe locationMatchingStrategy\nis specified as INTERSECTING or when the\nmetadataLocation is specified as a\nnon-spreadsheet location: spreadsheet metadata cannot intersect any other\ndeveloper metadata location.  This field also must be left unspecified when\nthe locationMatchingStrategy\nis specified as EXACT."
    },
    "gridRange" : {
      "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
      "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
      "sheetId" : "The sheet this range is on.",
      "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
      "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
    },
    "a1Range" : "Selects data that matches the specified A1 range."
  } ]
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

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

### spreadsheetId (required)

The spreadsheet to apply the updates to.

**Type:** string

### $body

The request for updating any aspect of a spreadsheet.

**Type:** object

```json
{
  "responseRanges" : [ "string" ],
  "includeSpreadsheetInResponse" : "Determines if the update response should include the spreadsheet\nresource.",
  "responseIncludeGridData" : "True if grid data should be returned. Meaningful only if\nif include_spreadsheet_response is 'true'.\nThis parameter is ignored if a field mask was set in the request.",
  "requests" : [ {
    "deleteFilterView" : {
      "filterId" : "The ID of the filter to delete."
    },
    "deleteSheet" : {
      "sheetId" : "The ID of the sheet to delete."
    },
    "repeatCell" : {
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "cell" : {
        "hyperlink" : "A hyperlink this cell points to, if any.\nThis field is read-only.  (To set it, use a `=HYPERLINK` formula\nin the userEnteredValue.formulaValue\nfield.)",
        "note" : "Any note on the cell.",
        "userEnteredFormat" : {
          "textDirection" : "The direction of the text in the cell.",
          "padding" : {
            "top" : "The top padding of the cell.",
            "left" : "The left padding of the cell.",
            "bottom" : "The bottom padding of the cell.",
            "right" : "The right padding of the cell."
          },
          "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
          "backgroundColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "numberFormat" : {
            "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
            "type" : "The type of the number format.\nWhen writing, this field must be set."
          },
          "wrapStrategy" : "The wrap strategy for the value in the cell.",
          "borders" : {
            "top" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "left" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "bottom" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "right" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            }
          },
          "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
          "textRotation" : {
            "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
            "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
          },
          "verticalAlignment" : "The vertical alignment of the value in the cell.",
          "textFormat" : {
            "fontFamily" : "The font family.",
            "underline" : "True if the text is underlined.",
            "foregroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "fontSize" : "The size of the font.",
            "bold" : "True if the text is bold.",
            "strikethrough" : "True if the text has a strikethrough.",
            "italic" : "True if the text is italicized."
          }
        },
        "effectiveValue" : {
          "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
          "errorValue" : {
            "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
            "type" : "The type of error."
          },
          "formulaValue" : "Represents a formula.",
          "boolValue" : "Represents a boolean value.",
          "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
        },
        "effectiveFormat" : {
          "textDirection" : "The direction of the text in the cell.",
          "padding" : {
            "top" : "The top padding of the cell.",
            "left" : "The left padding of the cell.",
            "bottom" : "The bottom padding of the cell.",
            "right" : "The right padding of the cell."
          },
          "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
          "backgroundColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "numberFormat" : {
            "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
            "type" : "The type of the number format.\nWhen writing, this field must be set."
          },
          "wrapStrategy" : "The wrap strategy for the value in the cell.",
          "borders" : {
            "top" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "left" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "bottom" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "right" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            }
          },
          "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
          "textRotation" : {
            "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
            "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
          },
          "verticalAlignment" : "The vertical alignment of the value in the cell.",
          "textFormat" : {
            "fontFamily" : "The font family.",
            "underline" : "True if the text is underlined.",
            "foregroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "fontSize" : "The size of the font.",
            "bold" : "True if the text is bold.",
            "strikethrough" : "True if the text has a strikethrough.",
            "italic" : "True if the text is italicized."
          }
        },
        "formattedValue" : "The formatted value of the cell.\nThis is the value as it's shown to the user.\nThis field is read-only.",
        "textFormatRuns" : [ {
          "startIndex" : "The character index where this run starts.",
          "format" : {
            "fontFamily" : "The font family.",
            "underline" : "True if the text is underlined.",
            "foregroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "fontSize" : "The size of the font.",
            "bold" : "True if the text is bold.",
            "strikethrough" : "True if the text has a strikethrough.",
            "italic" : "True if the text is italicized."
          }
        } ],
        "dataValidation" : {
          "condition" : {
            "values" : [ {
              "relativeDate" : "A relative date (based on the current date).\nValid only if the type is\nDATE_BEFORE,\nDATE_AFTER,\nDATE_ON_OR_BEFORE or\nDATE_ON_OR_AFTER.\n\nRelative dates are not supported in data validation.\nThey are supported only in conditional formatting and\nconditional filters.",
              "userEnteredValue" : "A value the condition is based on.\nThe value will be parsed as if the user typed into a cell.\nFormulas are supported (and must begin with an `=`)."
            } ],
            "type" : "The type of condition."
          },
          "inputMessage" : "A message to show the user when adding data to the cell.",
          "showCustomUi" : "True if the UI should be customized based on the kind of condition.\nIf true, \"List\" conditions will show a dropdown.",
          "strict" : "True if invalid data should be rejected."
        },
        "pivotTable" : {
          "valueLayout" : "Whether values should be listed horizontally (as columns)\nor vertically (as rows).",
          "criteria" : "An optional mapping of filters per source column offset.\n\nThe filters will be applied before aggregating data into the pivot table.\nThe map's key is the column offset of the source range that you want to\nfilter, and the value is the criteria for that column.\n\nFor example, if the source was `C10:E15`, a key of `0` will have the filter\nfor column `C`, whereas the key `1` is for column `D`.",
          "columns" : [ {
            "showTotals" : "True if the pivot table should include the totals for this grouping.",
            "valueBucket" : {
              "valuesIndex" : "The offset in the PivotTable.values list which the values in this\ngrouping should be sorted by.",
              "buckets" : [ {
                "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                "errorValue" : {
                  "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                  "type" : "The type of error."
                },
                "formulaValue" : "Represents a formula.",
                "boolValue" : "Represents a boolean value.",
                "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
              } ]
            },
            "groupRule" : {
              "histogramRule" : {
                "start" : "Optional. The minimum value at which items will be placed into buckets\nof constant size. Values below start will be lumped into a single bucket.",
                "interval" : "Required. The size of the buckets that will be created. Must be positive.",
                "end" : "Optional. The maximum value at which items will be placed into buckets\nof constant size. Values above end will be lumped into a single bucket."
              },
              "manualRule" : {
                "groups" : [ {
                  "groupName" : {
                    "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                    "errorValue" : {
                      "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                      "type" : "The type of error."
                    },
                    "formulaValue" : "Represents a formula.",
                    "boolValue" : "Represents a boolean value.",
                    "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                  },
                  "items" : [ {
                    "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                    "errorValue" : {
                      "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                      "type" : "The type of error."
                    },
                    "formulaValue" : "Represents a formula.",
                    "boolValue" : "Represents a boolean value.",
                    "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                  } ]
                } ]
              }
            },
            "sortOrder" : "The order the values in this group should be sorted.",
            "valueMetadata" : [ {
              "collapsed" : "True if the data corresponding to the value is collapsed.",
              "value" : {
                "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                "errorValue" : {
                  "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                  "type" : "The type of error."
                },
                "formulaValue" : "Represents a formula.",
                "boolValue" : "Represents a boolean value.",
                "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
              }
            } ],
            "label" : "The labels to use for the row/column groups which can be customized. For\nexample, in the following pivot table, the row label is `Region` (which\ncould be renamed to `State`) and the column label is `Product` (which\ncould be renamed `Item`). Pivot tables created before December 2017 do\nnot have header labels. If you'd like to add header labels to an existing\npivot table, please delete the existing pivot table and then create a new\npivot table with same parameters.\n\n    +--------------+---------+-------+\n    | SUM of Units | Product |       |\n    | Region       | Pen     | Paper |\n    +--------------+---------+-------+\n    | New York     |     345 |    98 |\n    | Oregon       |     234 |   123 |\n    | Tennessee    |     531 |   415 |\n    +--------------+---------+-------+\n    | Grand Total  |    1110 |   636 |\n    +--------------+---------+-------+",
            "repeatHeadings" : "True if the headings in this pivot group should be repeated.\nThis is only valid for row groupings and will be ignored by columns.\n\nBy default, we minimize repitition of headings by not showing higher\nlevel headings where they are the same. For example, even though the\nthird row below corresponds to \"Q1 Mar\", \"Q1\" is not shown because\nit is redundant with previous rows. Setting repeat_headings to true\nwould cause \"Q1\" to be repeated for \"Feb\" and \"Mar\".\n\n    +--------------+\n    | Q1     | Jan |\n    |        | Feb |\n    |        | Mar |\n    +--------+-----+\n    | Q1 Total     |\n    +--------------+",
            "sourceColumnOffset" : "The column offset of the source range that this grouping is based on.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this group refers to column `C`, whereas the offset `1` would refer\nto column `D`."
          } ],
          "values" : [ {
            "summarizeFunction" : "A function to summarize the value.\nIf formula is set, the only supported values are\nSUM and\nCUSTOM.\nIf sourceColumnOffset is set, then `CUSTOM`\nis not supported.",
            "name" : "A name to use for the value.",
            "formula" : "A custom formula to calculate the value.  The formula must start\nwith an `=` character.",
            "calculatedDisplayType" : "If specified, indicates that pivot values should be displayed as\nthe result of a calculation with another pivot value. For example, if\ncalculated_display_type is specified as PERCENT_OF_GRAND_TOTAL, all the\npivot values will be displayed as the percentage of the grand total. In\nthe Sheets UI, this is referred to as \"Show As\" in the value section of a\npivot table.",
            "sourceColumnOffset" : "The column offset of the source range that this value reads from.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this value refers to column `C`, whereas the offset `1` would\nrefer to column `D`."
          } ],
          "source" : {
            "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
            "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
            "sheetId" : "The sheet this range is on.",
            "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
            "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
          },
          "rows" : [ {
            "showTotals" : "True if the pivot table should include the totals for this grouping.",
            "valueBucket" : {
              "valuesIndex" : "The offset in the PivotTable.values list which the values in this\ngrouping should be sorted by.",
              "buckets" : [ {
                "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                "errorValue" : {
                  "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                  "type" : "The type of error."
                },
                "formulaValue" : "Represents a formula.",
                "boolValue" : "Represents a boolean value.",
                "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
              } ]
            },
            "groupRule" : {
              "histogramRule" : {
                "start" : "Optional. The minimum value at which items will be placed into buckets\nof constant size. Values below start will be lumped into a single bucket.",
                "interval" : "Required. The size of the buckets that will be created. Must be positive.",
                "end" : "Optional. The maximum value at which items will be placed into buckets\nof constant size. Values above end will be lumped into a single bucket."
              },
              "manualRule" : {
                "groups" : [ {
                  "groupName" : {
                    "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                    "errorValue" : {
                      "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                      "type" : "The type of error."
                    },
                    "formulaValue" : "Represents a formula.",
                    "boolValue" : "Represents a boolean value.",
                    "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                  },
                  "items" : [ {
                    "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                    "errorValue" : {
                      "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                      "type" : "The type of error."
                    },
                    "formulaValue" : "Represents a formula.",
                    "boolValue" : "Represents a boolean value.",
                    "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                  } ]
                } ]
              }
            },
            "sortOrder" : "The order the values in this group should be sorted.",
            "valueMetadata" : [ {
              "collapsed" : "True if the data corresponding to the value is collapsed.",
              "value" : {
                "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                "errorValue" : {
                  "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                  "type" : "The type of error."
                },
                "formulaValue" : "Represents a formula.",
                "boolValue" : "Represents a boolean value.",
                "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
              }
            } ],
            "label" : "The labels to use for the row/column groups which can be customized. For\nexample, in the following pivot table, the row label is `Region` (which\ncould be renamed to `State`) and the column label is `Product` (which\ncould be renamed `Item`). Pivot tables created before December 2017 do\nnot have header labels. If you'd like to add header labels to an existing\npivot table, please delete the existing pivot table and then create a new\npivot table with same parameters.\n\n    +--------------+---------+-------+\n    | SUM of Units | Product |       |\n    | Region       | Pen     | Paper |\n    +--------------+---------+-------+\n    | New York     |     345 |    98 |\n    | Oregon       |     234 |   123 |\n    | Tennessee    |     531 |   415 |\n    +--------------+---------+-------+\n    | Grand Total  |    1110 |   636 |\n    +--------------+---------+-------+",
            "repeatHeadings" : "True if the headings in this pivot group should be repeated.\nThis is only valid for row groupings and will be ignored by columns.\n\nBy default, we minimize repitition of headings by not showing higher\nlevel headings where they are the same. For example, even though the\nthird row below corresponds to \"Q1 Mar\", \"Q1\" is not shown because\nit is redundant with previous rows. Setting repeat_headings to true\nwould cause \"Q1\" to be repeated for \"Feb\" and \"Mar\".\n\n    +--------------+\n    | Q1     | Jan |\n    |        | Feb |\n    |        | Mar |\n    +--------+-----+\n    | Q1 Total     |\n    +--------------+",
            "sourceColumnOffset" : "The column offset of the source range that this grouping is based on.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this group refers to column `C`, whereas the offset `1` would refer\nto column `D`."
          } ]
        },
        "userEnteredValue" : {
          "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
          "errorValue" : {
            "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
            "type" : "The type of error."
          },
          "formulaValue" : "Represents a formula.",
          "boolValue" : "Represents a boolean value.",
          "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
        }
      },
      "fields" : "The fields that should be updated.  At least one field must be specified.\nThe root `cell` is implied and should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field."
    },
    "unmergeCells" : {
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      }
    },
    "pasteData" : {
      "coordinate" : {
        "sheetId" : "The sheet this coordinate is on.",
        "rowIndex" : "The row index of the coordinate.",
        "columnIndex" : "The column index of the coordinate."
      },
      "data" : "The data to insert.",
      "delimiter" : "The delimiter in the data.",
      "html" : "True if the data is HTML.",
      "type" : "How the data should be pasted."
    },
    "updateFilterView" : {
      "filter" : {
        "filterViewId" : "The ID of the filter view.",
        "sortSpecs" : [ {
          "sortOrder" : "The order data should be sorted.",
          "dimensionIndex" : "The dimension the sort should be applied to."
        } ],
        "namedRangeId" : "The named range this filter view is backed by, if any.\n\nWhen writing, only one of range or named_range_id\nmay be set.",
        "criteria" : "The criteria for showing/hiding values per column.\nThe map's key is the column index, and the value is the criteria for\nthat column.",
        "range" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        },
        "title" : "The name of the filter view."
      },
      "fields" : "The fields that should be updated.  At least one field must be specified.\nThe root `filter` is implied and should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field."
    },
    "addBanding" : {
      "bandedRange" : {
        "bandedRangeId" : "The id of the banded range.",
        "rowProperties" : {
          "headerColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "footerColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "firstBandColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "secondBandColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          }
        },
        "range" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        },
        "columnProperties" : {
          "headerColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "footerColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "firstBandColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "secondBandColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          }
        }
      }
    },
    "addSheet" : {
      "properties" : {
        "hidden" : "True if the sheet is hidden in the UI, false if it's visible.",
        "sheetType" : "The type of sheet. Defaults to GRID.\nThis field cannot be changed once set.",
        "index" : "The index of the sheet within the spreadsheet.\nWhen adding or updating sheet properties, if this field\nis excluded then the sheet will be added or moved to the end\nof the sheet list. When updating sheet indices or inserting\nsheets, movement is considered in \"before the move\" indexes.\nFor example, if there were 3 sheets (S1, S2, S3) in order to\nmove S1 ahead of S2 the index would have to be set to 2. A sheet\nindex update request will be ignored if the requested index is\nidentical to the sheets current index or if the requested new\nindex is equal to the current sheet index + 1.",
        "sheetId" : "The ID of the sheet. Must be non-negative.\nThis field cannot be changed once set.",
        "rightToLeft" : "True if the sheet is an RTL sheet instead of an LTR sheet.",
        "title" : "The name of the sheet.",
        "tabColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "gridProperties" : {
          "frozenRowCount" : "The number of rows that are frozen in the grid.",
          "frozenColumnCount" : "The number of columns that are frozen in the grid.",
          "hideGridlines" : "True if the grid isn't showing gridlines in the UI.",
          "columnCount" : "The number of columns in the grid.",
          "rowCount" : "The number of rows in the grid."
        }
      }
    },
    "duplicateSheet" : {
      "insertSheetIndex" : "The zero-based index where the new sheet should be inserted.\nThe index of all sheets after this are incremented.",
      "newSheetName" : "The name of the new sheet. If empty, a new name is chosen for you.",
      "sourceSheetId" : "The sheet to duplicate.",
      "newSheetId" : "If set, the ID of the new sheet. If not set, an ID is chosen.\nIf set, the ID must not conflict with any existing sheet ID.\nIf set, it must be non-negative."
    },
    "mergeCells" : {
      "mergeType" : "How the cells should be merged.",
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      }
    },
    "insertRange" : {
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "shiftDimension" : "The dimension which will be shifted when inserting cells.\nIf ROWS, existing cells will be shifted down.\nIf COLUMNS, existing cells will be shifted right."
    },
    "addFilterView" : {
      "filter" : {
        "filterViewId" : "The ID of the filter view.",
        "sortSpecs" : [ {
          "sortOrder" : "The order data should be sorted.",
          "dimensionIndex" : "The dimension the sort should be applied to."
        } ],
        "namedRangeId" : "The named range this filter view is backed by, if any.\n\nWhen writing, only one of range or named_range_id\nmay be set.",
        "criteria" : "The criteria for showing/hiding values per column.\nThe map's key is the column index, and the value is the criteria for\nthat column.",
        "range" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        },
        "title" : "The name of the filter view."
      }
    },
    "updateProtectedRange" : {
      "protectedRange" : {
        "namedRangeId" : "The named range this protected range is backed by, if any.\n\nWhen writing, only one of range or named_range_id\nmay be set.",
        "unprotectedRanges" : [ {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        } ],
        "description" : "The description of this protected range.",
        "range" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        },
        "warningOnly" : "True if this protected range will show a warning when editing.\nWarning-based protection means that every user can edit data in the\nprotected range, except editing will prompt a warning asking the user\nto confirm the edit.\n\nWhen writing: if this field is true, then editors is ignored.\nAdditionally, if this field is changed from true to false and the\n`editors` field is not set (nor included in the field mask), then\nthe editors will be set to all the editors in the document.",
        "requestingUserCanEdit" : "True if the user who requested this protected range can edit the\nprotected area.\nThis field is read-only.",
        "protectedRangeId" : "The ID of the protected range.\nThis field is read-only.",
        "editors" : {
          "domainUsersCanEdit" : "True if anyone in the document's domain has edit access to the protected\nrange.  Domain protection is only supported on documents within a domain.",
          "groups" : [ "string" ],
          "users" : [ "string" ]
        }
      },
      "fields" : "The fields that should be updated.  At least one field must be specified.\nThe root `protectedRange` is implied and should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field."
    },
    "deleteDimension" : {
      "range" : {
        "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
        "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
        "sheetId" : "The sheet this span is on.",
        "dimension" : "The dimension of the span."
      }
    },
    "randomizeRange" : {
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      }
    },
    "insertDimension" : {
      "range" : {
        "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
        "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
        "sheetId" : "The sheet this span is on.",
        "dimension" : "The dimension of the span."
      },
      "inheritFromBefore" : "Whether dimension properties should be extended from the dimensions\nbefore or after the newly inserted dimensions.\nTrue to inherit from the dimensions before (in which case the start\nindex must be greater than 0), and false to inherit from the dimensions\nafter.\n\nFor example, if row index 0 has red background and row index 1\nhas a green background, then inserting 2 rows at index 1 can inherit\neither the green or red background.  If `inheritFromBefore` is true,\nthe two new rows will be red (because the row before the insertion point\nwas red), whereas if `inheritFromBefore` is false, the two new rows will\nbe green (because the row after the insertion point was green)."
    },
    "cutPaste" : {
      "pasteType" : "What kind of data to paste.  All the source data will be cut, regardless\nof what is pasted.",
      "destination" : {
        "sheetId" : "The sheet this coordinate is on.",
        "rowIndex" : "The row index of the coordinate.",
        "columnIndex" : "The column index of the coordinate."
      },
      "source" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      }
    },
    "addConditionalFormatRule" : {
      "index" : "The zero-based index where the rule should be inserted.",
      "rule" : {
        "gradientRule" : {
          "midpoint" : {
            "color" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "type" : "How the value should be interpreted.",
            "value" : "The value this interpolation point uses.  May be a formula.\nUnused if type is MIN or\nMAX."
          },
          "maxpoint" : {
            "color" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "type" : "How the value should be interpreted.",
            "value" : "The value this interpolation point uses.  May be a formula.\nUnused if type is MIN or\nMAX."
          },
          "minpoint" : {
            "color" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "type" : "How the value should be interpreted.",
            "value" : "The value this interpolation point uses.  May be a formula.\nUnused if type is MIN or\nMAX."
          }
        },
        "ranges" : [ {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        } ],
        "booleanRule" : {
          "condition" : {
            "values" : [ {
              "relativeDate" : "A relative date (based on the current date).\nValid only if the type is\nDATE_BEFORE,\nDATE_AFTER,\nDATE_ON_OR_BEFORE or\nDATE_ON_OR_AFTER.\n\nRelative dates are not supported in data validation.\nThey are supported only in conditional formatting and\nconditional filters.",
              "userEnteredValue" : "A value the condition is based on.\nThe value will be parsed as if the user typed into a cell.\nFormulas are supported (and must begin with an `=`)."
            } ],
            "type" : "The type of condition."
          },
          "format" : {
            "textDirection" : "The direction of the text in the cell.",
            "padding" : {
              "top" : "The top padding of the cell.",
              "left" : "The left padding of the cell.",
              "bottom" : "The bottom padding of the cell.",
              "right" : "The right padding of the cell."
            },
            "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
            "backgroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "numberFormat" : {
              "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
              "type" : "The type of the number format.\nWhen writing, this field must be set."
            },
            "wrapStrategy" : "The wrap strategy for the value in the cell.",
            "borders" : {
              "top" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "left" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "bottom" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "right" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              }
            },
            "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
            "textRotation" : {
              "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
              "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
            },
            "verticalAlignment" : "The vertical alignment of the value in the cell.",
            "textFormat" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          }
        }
      }
    },
    "deleteProtectedRange" : {
      "protectedRangeId" : "The ID of the protected range to delete."
    },
    "updateNamedRange" : {
      "fields" : "The fields that should be updated.  At least one field must be specified.\nThe root `namedRange` is implied and should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field.",
      "namedRange" : {
        "namedRangeId" : "The ID of the named range.",
        "name" : "The name of the named range.",
        "range" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        }
      }
    },
    "findReplace" : {
      "searchByRegex" : "True if the find value is a regex.\nThe regular expression and replacement should follow Java regex rules\nat https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html.\nThe replacement string is allowed to refer to capturing groups.\nFor example, if one cell has the contents `\"Google Sheets\"` and another\nhas `\"Google Docs\"`, then searching for `\"o.* (.*)\"` with a replacement of\n`\"$1 Rocks\"` would change the contents of the cells to\n`\"GSheets Rocks\"` and `\"GDocs Rocks\"` respectively.",
      "matchCase" : "True if the search is case sensitive.",
      "includeFormulas" : "True if the search should include cells with formulas.\nFalse to skip cells with formulas.",
      "find" : "The value to search.",
      "matchEntireCell" : "True if the find value should match the entire cell.",
      "sheetId" : "The sheet to find/replace over.",
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "allSheets" : "True to find/replace over all sheets.",
      "replacement" : "The value to use as the replacement."
    },
    "updateConditionalFormatRule" : {
      "index" : "The zero-based index of the rule that should be replaced or moved.",
      "rule" : {
        "gradientRule" : {
          "midpoint" : {
            "color" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "type" : "How the value should be interpreted.",
            "value" : "The value this interpolation point uses.  May be a formula.\nUnused if type is MIN or\nMAX."
          },
          "maxpoint" : {
            "color" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "type" : "How the value should be interpreted.",
            "value" : "The value this interpolation point uses.  May be a formula.\nUnused if type is MIN or\nMAX."
          },
          "minpoint" : {
            "color" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "type" : "How the value should be interpreted.",
            "value" : "The value this interpolation point uses.  May be a formula.\nUnused if type is MIN or\nMAX."
          }
        },
        "ranges" : [ {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        } ],
        "booleanRule" : {
          "condition" : {
            "values" : [ {
              "relativeDate" : "A relative date (based on the current date).\nValid only if the type is\nDATE_BEFORE,\nDATE_AFTER,\nDATE_ON_OR_BEFORE or\nDATE_ON_OR_AFTER.\n\nRelative dates are not supported in data validation.\nThey are supported only in conditional formatting and\nconditional filters.",
              "userEnteredValue" : "A value the condition is based on.\nThe value will be parsed as if the user typed into a cell.\nFormulas are supported (and must begin with an `=`)."
            } ],
            "type" : "The type of condition."
          },
          "format" : {
            "textDirection" : "The direction of the text in the cell.",
            "padding" : {
              "top" : "The top padding of the cell.",
              "left" : "The left padding of the cell.",
              "bottom" : "The bottom padding of the cell.",
              "right" : "The right padding of the cell."
            },
            "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
            "backgroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "numberFormat" : {
              "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
              "type" : "The type of the number format.\nWhen writing, this field must be set."
            },
            "wrapStrategy" : "The wrap strategy for the value in the cell.",
            "borders" : {
              "top" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "left" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "bottom" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "right" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              }
            },
            "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
            "textRotation" : {
              "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
              "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
            },
            "verticalAlignment" : "The vertical alignment of the value in the cell.",
            "textFormat" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          }
        }
      },
      "sheetId" : "The sheet of the rule to move.  Required if new_index is set,\nunused otherwise.",
      "newIndex" : "The zero-based new index the rule should end up at."
    },
    "clearBasicFilter" : {
      "sheetId" : "The sheet ID on which the basic filter should be cleared."
    },
    "setBasicFilter" : {
      "filter" : {
        "sortSpecs" : [ {
          "sortOrder" : "The order data should be sorted.",
          "dimensionIndex" : "The dimension the sort should be applied to."
        } ],
        "criteria" : "The criteria for showing/hiding values per column.\nThe map's key is the column index, and the value is the criteria for\nthat column.",
        "range" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        }
      }
    },
    "deleteRange" : {
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "shiftDimension" : "The dimension from which deleted cells will be replaced with.\nIf ROWS, existing cells will be shifted upward to\nreplace the deleted cells. If COLUMNS, existing cells\nwill be shifted left to replace the deleted cells."
    },
    "addProtectedRange" : {
      "protectedRange" : {
        "namedRangeId" : "The named range this protected range is backed by, if any.\n\nWhen writing, only one of range or named_range_id\nmay be set.",
        "unprotectedRanges" : [ {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        } ],
        "description" : "The description of this protected range.",
        "range" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        },
        "warningOnly" : "True if this protected range will show a warning when editing.\nWarning-based protection means that every user can edit data in the\nprotected range, except editing will prompt a warning asking the user\nto confirm the edit.\n\nWhen writing: if this field is true, then editors is ignored.\nAdditionally, if this field is changed from true to false and the\n`editors` field is not set (nor included in the field mask), then\nthe editors will be set to all the editors in the document.",
        "requestingUserCanEdit" : "True if the user who requested this protected range can edit the\nprotected area.\nThis field is read-only.",
        "protectedRangeId" : "The ID of the protected range.\nThis field is read-only.",
        "editors" : {
          "domainUsersCanEdit" : "True if anyone in the document's domain has edit access to the protected\nrange.  Domain protection is only supported on documents within a domain.",
          "groups" : [ "string" ],
          "users" : [ "string" ]
        }
      }
    },
    "createDeveloperMetadata" : {
      "developerMetadata" : {
        "metadataId" : "The spreadsheet-scoped unique ID that identifies the metadata. IDs may be\nspecified when metadata is created, otherwise one will be randomly\ngenerated and assigned. Must be positive.",
        "metadataKey" : "The metadata key. There may be multiple metadata in a spreadsheet with the\nsame key.  Developer metadata must always have a key specified.",
        "visibility" : "The metadata visibility.  Developer metadata must always have a visibility\nspecified.",
        "metadataValue" : "Data associated with the metadata's key.",
        "location" : {
          "dimensionRange" : {
            "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
            "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
            "sheetId" : "The sheet this span is on.",
            "dimension" : "The dimension of the span."
          },
          "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
          "locationType" : "The type of location this object represents. This field is read-only.",
          "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
        }
      }
    },
    "sortRange" : {
      "sortSpecs" : [ {
        "sortOrder" : "The order data should be sorted.",
        "dimensionIndex" : "The dimension the sort should be applied to."
      } ],
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      }
    },
    "updateSheetProperties" : {
      "fields" : "The fields that should be updated.  At least one field must be specified.\nThe root `properties` is implied and should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field.",
      "properties" : {
        "hidden" : "True if the sheet is hidden in the UI, false if it's visible.",
        "sheetType" : "The type of sheet. Defaults to GRID.\nThis field cannot be changed once set.",
        "index" : "The index of the sheet within the spreadsheet.\nWhen adding or updating sheet properties, if this field\nis excluded then the sheet will be added or moved to the end\nof the sheet list. When updating sheet indices or inserting\nsheets, movement is considered in \"before the move\" indexes.\nFor example, if there were 3 sheets (S1, S2, S3) in order to\nmove S1 ahead of S2 the index would have to be set to 2. A sheet\nindex update request will be ignored if the requested index is\nidentical to the sheets current index or if the requested new\nindex is equal to the current sheet index + 1.",
        "sheetId" : "The ID of the sheet. Must be non-negative.\nThis field cannot be changed once set.",
        "rightToLeft" : "True if the sheet is an RTL sheet instead of an LTR sheet.",
        "title" : "The name of the sheet.",
        "tabColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "gridProperties" : {
          "frozenRowCount" : "The number of rows that are frozen in the grid.",
          "frozenColumnCount" : "The number of columns that are frozen in the grid.",
          "hideGridlines" : "True if the grid isn't showing gridlines in the UI.",
          "columnCount" : "The number of columns in the grid.",
          "rowCount" : "The number of rows in the grid."
        }
      }
    },
    "addNamedRange" : {
      "namedRange" : {
        "namedRangeId" : "The ID of the named range.",
        "name" : "The name of the named range.",
        "range" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        }
      }
    },
    "updateBanding" : {
      "bandedRange" : {
        "bandedRangeId" : "The id of the banded range.",
        "rowProperties" : {
          "headerColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "footerColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "firstBandColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "secondBandColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          }
        },
        "range" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        },
        "columnProperties" : {
          "headerColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "footerColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "firstBandColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "secondBandColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          }
        }
      },
      "fields" : "The fields that should be updated.  At least one field must be specified.\nThe root `bandedRange` is implied and should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field."
    },
    "deleteDeveloperMetadata" : {
      "dataFilter" : {
        "developerMetadataLookup" : {
          "metadataId" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_id.",
          "metadataKey" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_key.",
          "visibility" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.visibility.  If left unspecified, all developer\nmetadata visibile to the requesting project is considered.",
          "metadataValue" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_value.",
          "locationMatchingStrategy" : "Determines how this lookup matches the location.  If this field is\nspecified as EXACT, only developer metadata associated on the exact\nlocation specified is matched.  If this field is specified to INTERSECTING,\ndeveloper metadata associated on intersecting locations is also\nmatched.  If left unspecified, this field assumes a default value of\nINTERSECTING.\nIf this field is specified, a metadataLocation\nmust also be specified.",
          "metadataLocation" : {
            "dimensionRange" : {
              "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
              "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
              "sheetId" : "The sheet this span is on.",
              "dimension" : "The dimension of the span."
            },
            "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
            "locationType" : "The type of location this object represents. This field is read-only.",
            "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
          },
          "locationType" : "Limits the selected developer metadata to those entries which are\nassociated with locations of the specified type.  For example, when this\nfield is specified as ROW this lookup\nonly considers developer metadata associated on rows.  If the field is left\nunspecified, all location types are considered.  This field cannot be\nspecified as SPREADSHEET when\nthe locationMatchingStrategy\nis specified as INTERSECTING or when the\nmetadataLocation is specified as a\nnon-spreadsheet location: spreadsheet metadata cannot intersect any other\ndeveloper metadata location.  This field also must be left unspecified when\nthe locationMatchingStrategy\nis specified as EXACT."
        },
        "gridRange" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        },
        "a1Range" : "Selects data that matches the specified A1 range."
      }
    },
    "updateCells" : {
      "start" : {
        "sheetId" : "The sheet this coordinate is on.",
        "rowIndex" : "The row index of the coordinate.",
        "columnIndex" : "The column index of the coordinate."
      },
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "fields" : "The fields of CellData that should be updated.\nAt least one field must be specified.\nThe root is the CellData; 'row.values.' should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field.",
      "rows" : [ {
        "values" : [ {
          "hyperlink" : "A hyperlink this cell points to, if any.\nThis field is read-only.  (To set it, use a `=HYPERLINK` formula\nin the userEnteredValue.formulaValue\nfield.)",
          "note" : "Any note on the cell.",
          "userEnteredFormat" : {
            "textDirection" : "The direction of the text in the cell.",
            "padding" : {
              "top" : "The top padding of the cell.",
              "left" : "The left padding of the cell.",
              "bottom" : "The bottom padding of the cell.",
              "right" : "The right padding of the cell."
            },
            "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
            "backgroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "numberFormat" : {
              "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
              "type" : "The type of the number format.\nWhen writing, this field must be set."
            },
            "wrapStrategy" : "The wrap strategy for the value in the cell.",
            "borders" : {
              "top" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "left" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "bottom" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "right" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              }
            },
            "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
            "textRotation" : {
              "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
              "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
            },
            "verticalAlignment" : "The vertical alignment of the value in the cell.",
            "textFormat" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          },
          "effectiveValue" : {
            "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
            "errorValue" : {
              "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
              "type" : "The type of error."
            },
            "formulaValue" : "Represents a formula.",
            "boolValue" : "Represents a boolean value.",
            "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
          },
          "effectiveFormat" : {
            "textDirection" : "The direction of the text in the cell.",
            "padding" : {
              "top" : "The top padding of the cell.",
              "left" : "The left padding of the cell.",
              "bottom" : "The bottom padding of the cell.",
              "right" : "The right padding of the cell."
            },
            "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
            "backgroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "numberFormat" : {
              "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
              "type" : "The type of the number format.\nWhen writing, this field must be set."
            },
            "wrapStrategy" : "The wrap strategy for the value in the cell.",
            "borders" : {
              "top" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "left" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "bottom" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "right" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              }
            },
            "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
            "textRotation" : {
              "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
              "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
            },
            "verticalAlignment" : "The vertical alignment of the value in the cell.",
            "textFormat" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          },
          "formattedValue" : "The formatted value of the cell.\nThis is the value as it's shown to the user.\nThis field is read-only.",
          "textFormatRuns" : [ {
            "startIndex" : "The character index where this run starts.",
            "format" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          } ],
          "dataValidation" : {
            "condition" : {
              "values" : [ {
                "relativeDate" : "A relative date (based on the current date).\nValid only if the type is\nDATE_BEFORE,\nDATE_AFTER,\nDATE_ON_OR_BEFORE or\nDATE_ON_OR_AFTER.\n\nRelative dates are not supported in data validation.\nThey are supported only in conditional formatting and\nconditional filters.",
                "userEnteredValue" : "A value the condition is based on.\nThe value will be parsed as if the user typed into a cell.\nFormulas are supported (and must begin with an `=`)."
              } ],
              "type" : "The type of condition."
            },
            "inputMessage" : "A message to show the user when adding data to the cell.",
            "showCustomUi" : "True if the UI should be customized based on the kind of condition.\nIf true, \"List\" conditions will show a dropdown.",
            "strict" : "True if invalid data should be rejected."
          },
          "pivotTable" : {
            "valueLayout" : "Whether values should be listed horizontally (as columns)\nor vertically (as rows).",
            "criteria" : "An optional mapping of filters per source column offset.\n\nThe filters will be applied before aggregating data into the pivot table.\nThe map's key is the column offset of the source range that you want to\nfilter, and the value is the criteria for that column.\n\nFor example, if the source was `C10:E15`, a key of `0` will have the filter\nfor column `C`, whereas the key `1` is for column `D`.",
            "columns" : [ {
              "showTotals" : "True if the pivot table should include the totals for this grouping.",
              "valueBucket" : {
                "valuesIndex" : "The offset in the PivotTable.values list which the values in this\ngrouping should be sorted by.",
                "buckets" : [ {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                } ]
              },
              "groupRule" : {
                "histogramRule" : {
                  "start" : "Optional. The minimum value at which items will be placed into buckets\nof constant size. Values below start will be lumped into a single bucket.",
                  "interval" : "Required. The size of the buckets that will be created. Must be positive.",
                  "end" : "Optional. The maximum value at which items will be placed into buckets\nof constant size. Values above end will be lumped into a single bucket."
                },
                "manualRule" : {
                  "groups" : [ {
                    "groupName" : {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    },
                    "items" : [ {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    } ]
                  } ]
                }
              },
              "sortOrder" : "The order the values in this group should be sorted.",
              "valueMetadata" : [ {
                "collapsed" : "True if the data corresponding to the value is collapsed.",
                "value" : {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                }
              } ],
              "label" : "The labels to use for the row/column groups which can be customized. For\nexample, in the following pivot table, the row label is `Region` (which\ncould be renamed to `State`) and the column label is `Product` (which\ncould be renamed `Item`). Pivot tables created before December 2017 do\nnot have header labels. If you'd like to add header labels to an existing\npivot table, please delete the existing pivot table and then create a new\npivot table with same parameters.\n\n    +--------------+---------+-------+\n    | SUM of Units | Product |       |\n    | Region       | Pen     | Paper |\n    +--------------+---------+-------+\n    | New York     |     345 |    98 |\n    | Oregon       |     234 |   123 |\n    | Tennessee    |     531 |   415 |\n    +--------------+---------+-------+\n    | Grand Total  |    1110 |   636 |\n    +--------------+---------+-------+",
              "repeatHeadings" : "True if the headings in this pivot group should be repeated.\nThis is only valid for row groupings and will be ignored by columns.\n\nBy default, we minimize repitition of headings by not showing higher\nlevel headings where they are the same. For example, even though the\nthird row below corresponds to \"Q1 Mar\", \"Q1\" is not shown because\nit is redundant with previous rows. Setting repeat_headings to true\nwould cause \"Q1\" to be repeated for \"Feb\" and \"Mar\".\n\n    +--------------+\n    | Q1     | Jan |\n    |        | Feb |\n    |        | Mar |\n    +--------+-----+\n    | Q1 Total     |\n    +--------------+",
              "sourceColumnOffset" : "The column offset of the source range that this grouping is based on.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this group refers to column `C`, whereas the offset `1` would refer\nto column `D`."
            } ],
            "values" : [ {
              "summarizeFunction" : "A function to summarize the value.\nIf formula is set, the only supported values are\nSUM and\nCUSTOM.\nIf sourceColumnOffset is set, then `CUSTOM`\nis not supported.",
              "name" : "A name to use for the value.",
              "formula" : "A custom formula to calculate the value.  The formula must start\nwith an `=` character.",
              "calculatedDisplayType" : "If specified, indicates that pivot values should be displayed as\nthe result of a calculation with another pivot value. For example, if\ncalculated_display_type is specified as PERCENT_OF_GRAND_TOTAL, all the\npivot values will be displayed as the percentage of the grand total. In\nthe Sheets UI, this is referred to as \"Show As\" in the value section of a\npivot table.",
              "sourceColumnOffset" : "The column offset of the source range that this value reads from.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this value refers to column `C`, whereas the offset `1` would\nrefer to column `D`."
            } ],
            "source" : {
              "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
              "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
              "sheetId" : "The sheet this range is on.",
              "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
              "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
            },
            "rows" : [ {
              "showTotals" : "True if the pivot table should include the totals for this grouping.",
              "valueBucket" : {
                "valuesIndex" : "The offset in the PivotTable.values list which the values in this\ngrouping should be sorted by.",
                "buckets" : [ {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                } ]
              },
              "groupRule" : {
                "histogramRule" : {
                  "start" : "Optional. The minimum value at which items will be placed into buckets\nof constant size. Values below start will be lumped into a single bucket.",
                  "interval" : "Required. The size of the buckets that will be created. Must be positive.",
                  "end" : "Optional. The maximum value at which items will be placed into buckets\nof constant size. Values above end will be lumped into a single bucket."
                },
                "manualRule" : {
                  "groups" : [ {
                    "groupName" : {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    },
                    "items" : [ {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    } ]
                  } ]
                }
              },
              "sortOrder" : "The order the values in this group should be sorted.",
              "valueMetadata" : [ {
                "collapsed" : "True if the data corresponding to the value is collapsed.",
                "value" : {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                }
              } ],
              "label" : "The labels to use for the row/column groups which can be customized. For\nexample, in the following pivot table, the row label is `Region` (which\ncould be renamed to `State`) and the column label is `Product` (which\ncould be renamed `Item`). Pivot tables created before December 2017 do\nnot have header labels. If you'd like to add header labels to an existing\npivot table, please delete the existing pivot table and then create a new\npivot table with same parameters.\n\n    +--------------+---------+-------+\n    | SUM of Units | Product |       |\n    | Region       | Pen     | Paper |\n    +--------------+---------+-------+\n    | New York     |     345 |    98 |\n    | Oregon       |     234 |   123 |\n    | Tennessee    |     531 |   415 |\n    +--------------+---------+-------+\n    | Grand Total  |    1110 |   636 |\n    +--------------+---------+-------+",
              "repeatHeadings" : "True if the headings in this pivot group should be repeated.\nThis is only valid for row groupings and will be ignored by columns.\n\nBy default, we minimize repitition of headings by not showing higher\nlevel headings where they are the same. For example, even though the\nthird row below corresponds to \"Q1 Mar\", \"Q1\" is not shown because\nit is redundant with previous rows. Setting repeat_headings to true\nwould cause \"Q1\" to be repeated for \"Feb\" and \"Mar\".\n\n    +--------------+\n    | Q1     | Jan |\n    |        | Feb |\n    |        | Mar |\n    +--------+-----+\n    | Q1 Total     |\n    +--------------+",
              "sourceColumnOffset" : "The column offset of the source range that this grouping is based on.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this group refers to column `C`, whereas the offset `1` would refer\nto column `D`."
            } ]
          },
          "userEnteredValue" : {
            "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
            "errorValue" : {
              "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
              "type" : "The type of error."
            },
            "formulaValue" : "Represents a formula.",
            "boolValue" : "Represents a boolean value.",
            "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
          }
        } ]
      } ]
    },
    "updateDimensionProperties" : {
      "range" : {
        "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
        "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
        "sheetId" : "The sheet this span is on.",
        "dimension" : "The dimension of the span."
      },
      "fields" : "The fields that should be updated.  At least one field must be specified.\nThe root `properties` is implied and should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field.",
      "properties" : {
        "hiddenByUser" : "True if this dimension is explicitly hidden.",
        "developerMetadata" : [ {
          "metadataId" : "The spreadsheet-scoped unique ID that identifies the metadata. IDs may be\nspecified when metadata is created, otherwise one will be randomly\ngenerated and assigned. Must be positive.",
          "metadataKey" : "The metadata key. There may be multiple metadata in a spreadsheet with the\nsame key.  Developer metadata must always have a key specified.",
          "visibility" : "The metadata visibility.  Developer metadata must always have a visibility\nspecified.",
          "metadataValue" : "Data associated with the metadata's key.",
          "location" : {
            "dimensionRange" : {
              "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
              "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
              "sheetId" : "The sheet this span is on.",
              "dimension" : "The dimension of the span."
            },
            "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
            "locationType" : "The type of location this object represents. This field is read-only.",
            "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
          }
        } ],
        "hiddenByFilter" : "True if this dimension is being filtered.\nThis field is read-only.",
        "pixelSize" : "The height (if a row) or width (if a column) of the dimension in pixels."
      }
    },
    "duplicateFilterView" : {
      "filterId" : "The ID of the filter being duplicated."
    },
    "deleteBanding" : {
      "bandedRangeId" : "The ID of the banded range to delete."
    },
    "appendCells" : {
      "sheetId" : "The sheet ID to append the data to.",
      "fields" : "The fields of CellData that should be updated.\nAt least one field must be specified.\nThe root is the CellData; 'row.values.' should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field.",
      "rows" : [ {
        "values" : [ {
          "hyperlink" : "A hyperlink this cell points to, if any.\nThis field is read-only.  (To set it, use a `=HYPERLINK` formula\nin the userEnteredValue.formulaValue\nfield.)",
          "note" : "Any note on the cell.",
          "userEnteredFormat" : {
            "textDirection" : "The direction of the text in the cell.",
            "padding" : {
              "top" : "The top padding of the cell.",
              "left" : "The left padding of the cell.",
              "bottom" : "The bottom padding of the cell.",
              "right" : "The right padding of the cell."
            },
            "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
            "backgroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "numberFormat" : {
              "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
              "type" : "The type of the number format.\nWhen writing, this field must be set."
            },
            "wrapStrategy" : "The wrap strategy for the value in the cell.",
            "borders" : {
              "top" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "left" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "bottom" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "right" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              }
            },
            "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
            "textRotation" : {
              "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
              "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
            },
            "verticalAlignment" : "The vertical alignment of the value in the cell.",
            "textFormat" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          },
          "effectiveValue" : {
            "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
            "errorValue" : {
              "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
              "type" : "The type of error."
            },
            "formulaValue" : "Represents a formula.",
            "boolValue" : "Represents a boolean value.",
            "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
          },
          "effectiveFormat" : {
            "textDirection" : "The direction of the text in the cell.",
            "padding" : {
              "top" : "The top padding of the cell.",
              "left" : "The left padding of the cell.",
              "bottom" : "The bottom padding of the cell.",
              "right" : "The right padding of the cell."
            },
            "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
            "backgroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "numberFormat" : {
              "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
              "type" : "The type of the number format.\nWhen writing, this field must be set."
            },
            "wrapStrategy" : "The wrap strategy for the value in the cell.",
            "borders" : {
              "top" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "left" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "bottom" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              },
              "right" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
                "style" : "The style of the border."
              }
            },
            "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
            "textRotation" : {
              "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
              "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
            },
            "verticalAlignment" : "The vertical alignment of the value in the cell.",
            "textFormat" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          },
          "formattedValue" : "The formatted value of the cell.\nThis is the value as it's shown to the user.\nThis field is read-only.",
          "textFormatRuns" : [ {
            "startIndex" : "The character index where this run starts.",
            "format" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            }
          } ],
          "dataValidation" : {
            "condition" : {
              "values" : [ {
                "relativeDate" : "A relative date (based on the current date).\nValid only if the type is\nDATE_BEFORE,\nDATE_AFTER,\nDATE_ON_OR_BEFORE or\nDATE_ON_OR_AFTER.\n\nRelative dates are not supported in data validation.\nThey are supported only in conditional formatting and\nconditional filters.",
                "userEnteredValue" : "A value the condition is based on.\nThe value will be parsed as if the user typed into a cell.\nFormulas are supported (and must begin with an `=`)."
              } ],
              "type" : "The type of condition."
            },
            "inputMessage" : "A message to show the user when adding data to the cell.",
            "showCustomUi" : "True if the UI should be customized based on the kind of condition.\nIf true, \"List\" conditions will show a dropdown.",
            "strict" : "True if invalid data should be rejected."
          },
          "pivotTable" : {
            "valueLayout" : "Whether values should be listed horizontally (as columns)\nor vertically (as rows).",
            "criteria" : "An optional mapping of filters per source column offset.\n\nThe filters will be applied before aggregating data into the pivot table.\nThe map's key is the column offset of the source range that you want to\nfilter, and the value is the criteria for that column.\n\nFor example, if the source was `C10:E15`, a key of `0` will have the filter\nfor column `C`, whereas the key `1` is for column `D`.",
            "columns" : [ {
              "showTotals" : "True if the pivot table should include the totals for this grouping.",
              "valueBucket" : {
                "valuesIndex" : "The offset in the PivotTable.values list which the values in this\ngrouping should be sorted by.",
                "buckets" : [ {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                } ]
              },
              "groupRule" : {
                "histogramRule" : {
                  "start" : "Optional. The minimum value at which items will be placed into buckets\nof constant size. Values below start will be lumped into a single bucket.",
                  "interval" : "Required. The size of the buckets that will be created. Must be positive.",
                  "end" : "Optional. The maximum value at which items will be placed into buckets\nof constant size. Values above end will be lumped into a single bucket."
                },
                "manualRule" : {
                  "groups" : [ {
                    "groupName" : {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    },
                    "items" : [ {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    } ]
                  } ]
                }
              },
              "sortOrder" : "The order the values in this group should be sorted.",
              "valueMetadata" : [ {
                "collapsed" : "True if the data corresponding to the value is collapsed.",
                "value" : {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                }
              } ],
              "label" : "The labels to use for the row/column groups which can be customized. For\nexample, in the following pivot table, the row label is `Region` (which\ncould be renamed to `State`) and the column label is `Product` (which\ncould be renamed `Item`). Pivot tables created before December 2017 do\nnot have header labels. If you'd like to add header labels to an existing\npivot table, please delete the existing pivot table and then create a new\npivot table with same parameters.\n\n    +--------------+---------+-------+\n    | SUM of Units | Product |       |\n    | Region       | Pen     | Paper |\n    +--------------+---------+-------+\n    | New York     |     345 |    98 |\n    | Oregon       |     234 |   123 |\n    | Tennessee    |     531 |   415 |\n    +--------------+---------+-------+\n    | Grand Total  |    1110 |   636 |\n    +--------------+---------+-------+",
              "repeatHeadings" : "True if the headings in this pivot group should be repeated.\nThis is only valid for row groupings and will be ignored by columns.\n\nBy default, we minimize repitition of headings by not showing higher\nlevel headings where they are the same. For example, even though the\nthird row below corresponds to \"Q1 Mar\", \"Q1\" is not shown because\nit is redundant with previous rows. Setting repeat_headings to true\nwould cause \"Q1\" to be repeated for \"Feb\" and \"Mar\".\n\n    +--------------+\n    | Q1     | Jan |\n    |        | Feb |\n    |        | Mar |\n    +--------+-----+\n    | Q1 Total     |\n    +--------------+",
              "sourceColumnOffset" : "The column offset of the source range that this grouping is based on.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this group refers to column `C`, whereas the offset `1` would refer\nto column `D`."
            } ],
            "values" : [ {
              "summarizeFunction" : "A function to summarize the value.\nIf formula is set, the only supported values are\nSUM and\nCUSTOM.\nIf sourceColumnOffset is set, then `CUSTOM`\nis not supported.",
              "name" : "A name to use for the value.",
              "formula" : "A custom formula to calculate the value.  The formula must start\nwith an `=` character.",
              "calculatedDisplayType" : "If specified, indicates that pivot values should be displayed as\nthe result of a calculation with another pivot value. For example, if\ncalculated_display_type is specified as PERCENT_OF_GRAND_TOTAL, all the\npivot values will be displayed as the percentage of the grand total. In\nthe Sheets UI, this is referred to as \"Show As\" in the value section of a\npivot table.",
              "sourceColumnOffset" : "The column offset of the source range that this value reads from.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this value refers to column `C`, whereas the offset `1` would\nrefer to column `D`."
            } ],
            "source" : {
              "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
              "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
              "sheetId" : "The sheet this range is on.",
              "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
              "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
            },
            "rows" : [ {
              "showTotals" : "True if the pivot table should include the totals for this grouping.",
              "valueBucket" : {
                "valuesIndex" : "The offset in the PivotTable.values list which the values in this\ngrouping should be sorted by.",
                "buckets" : [ {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                } ]
              },
              "groupRule" : {
                "histogramRule" : {
                  "start" : "Optional. The minimum value at which items will be placed into buckets\nof constant size. Values below start will be lumped into a single bucket.",
                  "interval" : "Required. The size of the buckets that will be created. Must be positive.",
                  "end" : "Optional. The maximum value at which items will be placed into buckets\nof constant size. Values above end will be lumped into a single bucket."
                },
                "manualRule" : {
                  "groups" : [ {
                    "groupName" : {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    },
                    "items" : [ {
                      "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                      "errorValue" : {
                        "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                        "type" : "The type of error."
                      },
                      "formulaValue" : "Represents a formula.",
                      "boolValue" : "Represents a boolean value.",
                      "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                    } ]
                  } ]
                }
              },
              "sortOrder" : "The order the values in this group should be sorted.",
              "valueMetadata" : [ {
                "collapsed" : "True if the data corresponding to the value is collapsed.",
                "value" : {
                  "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
                  "errorValue" : {
                    "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
                    "type" : "The type of error."
                  },
                  "formulaValue" : "Represents a formula.",
                  "boolValue" : "Represents a boolean value.",
                  "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
                }
              } ],
              "label" : "The labels to use for the row/column groups which can be customized. For\nexample, in the following pivot table, the row label is `Region` (which\ncould be renamed to `State`) and the column label is `Product` (which\ncould be renamed `Item`). Pivot tables created before December 2017 do\nnot have header labels. If you'd like to add header labels to an existing\npivot table, please delete the existing pivot table and then create a new\npivot table with same parameters.\n\n    +--------------+---------+-------+\n    | SUM of Units | Product |       |\n    | Region       | Pen     | Paper |\n    +--------------+---------+-------+\n    | New York     |     345 |    98 |\n    | Oregon       |     234 |   123 |\n    | Tennessee    |     531 |   415 |\n    +--------------+---------+-------+\n    | Grand Total  |    1110 |   636 |\n    +--------------+---------+-------+",
              "repeatHeadings" : "True if the headings in this pivot group should be repeated.\nThis is only valid for row groupings and will be ignored by columns.\n\nBy default, we minimize repitition of headings by not showing higher\nlevel headings where they are the same. For example, even though the\nthird row below corresponds to \"Q1 Mar\", \"Q1\" is not shown because\nit is redundant with previous rows. Setting repeat_headings to true\nwould cause \"Q1\" to be repeated for \"Feb\" and \"Mar\".\n\n    +--------------+\n    | Q1     | Jan |\n    |        | Feb |\n    |        | Mar |\n    +--------+-----+\n    | Q1 Total     |\n    +--------------+",
              "sourceColumnOffset" : "The column offset of the source range that this grouping is based on.\n\nFor example, if the source was `C10:E15`, a `sourceColumnOffset` of `0`\nmeans this group refers to column `C`, whereas the offset `1` would refer\nto column `D`."
            } ]
          },
          "userEnteredValue" : {
            "stringValue" : "Represents a string value.\nLeading single quotes are not included. For example, if the user typed\n`'123` into the UI, this would be represented as a `stringValue` of\n`\"123\"`.",
            "errorValue" : {
              "message" : "A message with more information about the error\n(in the spreadsheet's locale).",
              "type" : "The type of error."
            },
            "formulaValue" : "Represents a formula.",
            "boolValue" : "Represents a boolean value.",
            "numberValue" : "Represents a double value.\nNote: Dates, Times and DateTimes are represented as doubles in\n\"serial number\" format."
          }
        } ]
      } ]
    },
    "appendDimension" : {
      "length" : "The number of rows or columns to append.",
      "sheetId" : "The sheet to append rows or columns to.",
      "dimension" : "Whether rows or columns should be appended."
    },
    "deleteConditionalFormatRule" : {
      "index" : "The zero-based index of the rule to be deleted.",
      "sheetId" : "The sheet the rule is being deleted from."
    },
    "updateSpreadsheetProperties" : {
      "fields" : "The fields that should be updated.  At least one field must be specified.\nThe root 'properties' is implied and should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field.",
      "properties" : {
        "autoRecalc" : "The amount of time to wait before volatile functions are recalculated.",
        "timeZone" : "The time zone of the spreadsheet, in CLDR format such as\n`America/New_York`. If the time zone isn't recognized, this may\nbe a custom time zone such as `GMT-07:00`.",
        "iterativeCalculationSettings" : {
          "maxIterations" : "When iterative calculation is enabled, the maximum number of calculation\nrounds to perform.",
          "convergenceThreshold" : "When iterative calculation is enabled and successive results differ by\nless than this threshold value, the calculation rounds stop."
        },
        "title" : "The title of the spreadsheet.",
        "locale" : "The locale of the spreadsheet in one of the following formats:\n\n* an ISO 639-1 language code such as `en`\n\n* an ISO 639-2 language code such as `fil`, if no 639-1 code exists\n\n* a combination of the ISO language code and country code, such as `en_US`\n\nNote: when updating this field, not all locales/languages are supported.",
        "defaultFormat" : {
          "textDirection" : "The direction of the text in the cell.",
          "padding" : {
            "top" : "The top padding of the cell.",
            "left" : "The left padding of the cell.",
            "bottom" : "The bottom padding of the cell.",
            "right" : "The right padding of the cell."
          },
          "horizontalAlignment" : "The horizontal alignment of the value in the cell.",
          "backgroundColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "numberFormat" : {
            "pattern" : "Pattern string used for formatting.  If not set, a default pattern based on\nthe user's locale will be used if necessary for the given type.\nSee the [Date and Number Formats guide](/sheets/api/guides/formats) for more\ninformation about the supported patterns.",
            "type" : "The type of the number format.\nWhen writing, this field must be set."
          },
          "wrapStrategy" : "The wrap strategy for the value in the cell.",
          "borders" : {
            "top" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "left" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "bottom" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            },
            "right" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
              "style" : "The style of the border."
            }
          },
          "hyperlinkDisplayType" : "How a hyperlink, if it exists, should be displayed in the cell.",
          "textRotation" : {
            "angle" : "The angle between the standard orientation and the desired orientation.\nMeasured in degrees. Valid values are between -90 and 90. Positive\nangles are angled upwards, negative are angled downwards.\n\nNote: For LTR text direction positive angles are in the counterclockwise\ndirection, whereas for RTL they are in the clockwise direction",
            "vertical" : "If true, text reads top to bottom, but the orientation of individual\ncharacters is unchanged.\nFor example:\n\n    | V |\n    | e |\n    | r |\n    | t |\n    | i |\n    | c |\n    | a |\n    | l |"
          },
          "verticalAlignment" : "The vertical alignment of the value in the cell.",
          "textFormat" : {
            "fontFamily" : "The font family.",
            "underline" : "True if the text is underlined.",
            "foregroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "fontSize" : "The size of the font.",
            "bold" : "True if the text is bold.",
            "strikethrough" : "True if the text has a strikethrough.",
            "italic" : "True if the text is italicized."
          }
        }
      }
    },
    "autoFill" : {
      "sourceAndDestination" : {
        "source" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        },
        "dimension" : "The dimension that data should be filled into.",
        "fillLength" : "The number of rows or columns that data should be filled into.\nPositive numbers expand beyond the last row or last column\nof the source.  Negative numbers expand before the first row\nor first column of the source."
      },
      "useAlternateSeries" : "True if we should generate data with the \"alternate\" series.\nThis differs based on the type and amount of source data.",
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      }
    },
    "updateBorders" : {
      "top" : {
        "color" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
        "style" : "The style of the border."
      },
      "left" : {
        "color" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
        "style" : "The style of the border."
      },
      "bottom" : {
        "color" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
        "style" : "The style of the border."
      },
      "innerHorizontal" : {
        "color" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
        "style" : "The style of the border."
      },
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "right" : {
        "color" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
        "style" : "The style of the border."
      },
      "innerVertical" : {
        "color" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "width" : "The width of the border, in pixels.\nDeprecated; the width is determined by the \"style\" field.",
        "style" : "The style of the border."
      }
    },
    "updateChartSpec" : {
      "chartId" : "The ID of the chart to update.",
      "spec" : {
        "basicChart" : {
          "compareMode" : "The behavior of tooltips and data highlighting when hovering on data and\nchart area.",
          "stackedType" : "The stacked type for charts that support vertical stacking.\nApplies to Area, Bar, Column, and Stepped Area charts.",
          "lineSmoothing" : "Gets whether all lines should be rendered smooth or straight by default.\nApplies to Line charts.",
          "threeDimensional" : "True to make the chart 3D.\nApplies to Bar and Column charts.",
          "series" : [ {
            "lineStyle" : {
              "width" : "The thickness of the line, in px.",
              "type" : "The dash type of the line."
            },
            "series" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "targetAxis" : "The minor axis that will specify the range of values for this series.\nFor example, if charting stocks over time, the \"Volume\" series\nmay want to be pinned to the right with the prices pinned to the left,\nbecause the scale of trading volume is different than the scale of\nprices.\nIt is an error to specify an axis that isn't a valid minor axis\nfor the chart's type.",
            "type" : "The type of this series. Valid only if the\nchartType is\nCOMBO.\nDifferent types will change the way the series is visualized.\nOnly LINE, AREA,\nand COLUMN are supported."
          } ],
          "interpolateNulls" : "If some values in a series are missing, gaps may appear in the chart (e.g,\nsegments of lines in a line chart will be missing).  To eliminate these\ngaps set this to true.\nApplies to Line, Area, and Combo charts.",
          "chartType" : "The type of the chart.",
          "domains" : [ {
            "domain" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "reversed" : "True to reverse the order of the domain values (horizontal axis)."
          } ],
          "headerCount" : "The number of rows or columns in the data that are \"headers\".\nIf not set, Google Sheets will guess how many rows are headers based\non the data.\n\n(Note that BasicChartAxis.title may override the axis title\n inferred from the header values.)",
          "legendPosition" : "The position of the chart legend.",
          "axis" : [ {
            "titleTextPosition" : {
              "horizontalAlignment" : "Horizontal alignment setting for the piece of text."
            },
            "format" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            },
            "position" : "The position of this axis.",
            "title" : "The title of this axis. If set, this overrides any title inferred\nfrom headers of the data."
          } ]
        },
        "backgroundColor" : {
          "red" : "The amount of red in the color as a value in the interval [0, 1].",
          "green" : "The amount of green in the color as a value in the interval [0, 1].",
          "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
          "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
        },
        "waterfallChart" : {
          "hideConnectorLines" : "True to hide connector lines between columns.",
          "stackedType" : "The stacked type.",
          "series" : [ {
            "subtotalColumnsStyle" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "label" : "The label of the column's legend."
            },
            "data" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "negativeColumnsStyle" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "label" : "The label of the column's legend."
            },
            "hideTrailingSubtotal" : "True to hide the subtotal column from the end of the series. By default,\na subtotal column will appear at the end of each series. Setting this\nfield to true will hide that subtotal column for this series.",
            "positiveColumnsStyle" : {
              "color" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "label" : "The label of the column's legend."
            },
            "customSubtotals" : [ {
              "dataIsSubtotal" : "True if the data point at subtotal_index is the subtotal. If false,\nthe subtotal will be computed and appear after the data point.",
              "subtotalIndex" : "The 0-based index of a data point within the series. If\ndata_is_subtotal is true, the data point at this index is the\nsubtotal. Otherwise, the subtotal appears after the data point with\nthis index. A series can have multiple subtotals at arbitrary indices,\nbut subtotals do not affect the indices of the data points. For\nexample, if a series has 3 data points, their indices will always be 0,\n1, and 2, regardless of how many subtotals exist on the series or what\ndata points they are associated with.",
              "label" : "A label for the subtotal column."
            } ]
          } ],
          "domain" : {
            "data" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "reversed" : "True to reverse the order of the domain values (horizontal axis)."
          },
          "firstValueIsTotal" : "True to interpret the first value as a total.",
          "connectorLineStyle" : {
            "width" : "The thickness of the line, in px.",
            "type" : "The dash type of the line."
          }
        },
        "altText" : "The alternative text that describes the chart.  This is often used\nfor accessibility.",
        "maximized" : "True to make a chart fill the entire space in which it's rendered with\nminimum padding.  False to use the default padding.\n(Not applicable to Geo and Org charts.)",
        "subtitleTextPosition" : {
          "horizontalAlignment" : "Horizontal alignment setting for the piece of text."
        },
        "title" : "The title of the chart.",
        "bubbleChart" : {
          "bubbleMinRadiusSize" : "The minimum radius size of the bubbles, in pixels.\nIf specific, the field must be a positive value.",
          "bubbleTextStyle" : {
            "fontFamily" : "The font family.",
            "underline" : "True if the text is underlined.",
            "foregroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "fontSize" : "The size of the font.",
            "bold" : "True if the text is bold.",
            "strikethrough" : "True if the text has a strikethrough.",
            "italic" : "True if the text is italicized."
          },
          "series" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "bubbleSizes" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "domain" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "bubbleOpacity" : "The opacity of the bubbles between 0 and 1.0.\n0 is fully transparent and 1 is fully opaque.",
          "bubbleMaxRadiusSize" : "The max radius size of the bubbles, in pixels.\nIf specified, the field must be a positive value.",
          "groupIds" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "bubbleBorderColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "legendPosition" : "Where the legend of the chart should be drawn.",
          "bubbleLabels" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          }
        },
        "titleTextFormat" : {
          "fontFamily" : "The font family.",
          "underline" : "True if the text is underlined.",
          "foregroundColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "fontSize" : "The size of the font.",
          "bold" : "True if the text is bold.",
          "strikethrough" : "True if the text has a strikethrough.",
          "italic" : "True if the text is italicized."
        },
        "histogramChart" : {
          "series" : [ {
            "data" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "barColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            }
          } ],
          "showItemDividers" : "Whether horizontal divider lines should be displayed between items in each\ncolumn.",
          "legendPosition" : "The position of the chart legend.",
          "bucketSize" : "By default the bucket size (the range of values stacked in a single\ncolumn) is chosen automatically, but it may be overridden here.\nE.g., A bucket size of 1.5 results in buckets from 0 - 1.5, 1.5 - 3.0, etc.\nCannot be negative.\nThis field is optional.",
          "outlierPercentile" : "The outlier percentile is used to ensure that outliers do not adversely\naffect the calculation of bucket sizes.  For example, setting an outlier\npercentile of 0.05 indicates that the top and bottom 5% of values when\ncalculating buckets.  The values are still included in the chart, they will\nbe added to the first or last buckets instead of their own buckets.\nMust be between 0.0 and 0.5."
        },
        "fontName" : "The name of the font to use by default for all chart text (e.g. title,\naxis labels, legend).  If a font is specified for a specific part of the\nchart it will override this font name.",
        "subtitleTextFormat" : {
          "fontFamily" : "The font family.",
          "underline" : "True if the text is underlined.",
          "foregroundColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "fontSize" : "The size of the font.",
          "bold" : "True if the text is bold.",
          "strikethrough" : "True if the text has a strikethrough.",
          "italic" : "True if the text is italicized."
        },
        "titleTextPosition" : {
          "horizontalAlignment" : "Horizontal alignment setting for the piece of text."
        },
        "candlestickChart" : {
          "data" : [ {
            "openSeries" : {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              }
            },
            "closeSeries" : {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              }
            },
            "highSeries" : {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              }
            },
            "lowSeries" : {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              }
            }
          } ],
          "domain" : {
            "data" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "reversed" : "True to reverse the order of the domain values (horizontal axis)."
          }
        },
        "orgChart" : {
          "nodeSize" : "The size of the org chart nodes.",
          "parentLabels" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "nodeColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "selectedNodeColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "tooltips" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "labels" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          }
        },
        "subtitle" : "The subtitle of the chart.",
        "pieChart" : {
          "pieHole" : "The size of the hole in the pie chart.",
          "threeDimensional" : "True if the pie is three dimensional.",
          "series" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "domain" : {
            "sourceRange" : {
              "sources" : [ {
                "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                "sheetId" : "The sheet this range is on.",
                "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
              } ]
            }
          },
          "legendPosition" : "Where the legend of the pie chart should be drawn."
        },
        "hiddenDimensionStrategy" : "Determines how the charts will use hidden rows or columns."
      }
    },
    "textToColumns" : {
      "delimiter" : "The delimiter to use. Used only if delimiterType is\nCUSTOM.",
      "delimiterType" : "The delimiter type to use.",
      "source" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      }
    },
    "deleteNamedRange" : {
      "namedRangeId" : "The ID of the named range to delete."
    },
    "autoResizeDimensions" : {
      "dimensions" : {
        "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
        "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
        "sheetId" : "The sheet this span is on.",
        "dimension" : "The dimension of the span."
      }
    },
    "setDataValidation" : {
      "range" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "rule" : {
        "condition" : {
          "values" : [ {
            "relativeDate" : "A relative date (based on the current date).\nValid only if the type is\nDATE_BEFORE,\nDATE_AFTER,\nDATE_ON_OR_BEFORE or\nDATE_ON_OR_AFTER.\n\nRelative dates are not supported in data validation.\nThey are supported only in conditional formatting and\nconditional filters.",
            "userEnteredValue" : "A value the condition is based on.\nThe value will be parsed as if the user typed into a cell.\nFormulas are supported (and must begin with an `=`)."
          } ],
          "type" : "The type of condition."
        },
        "inputMessage" : "A message to show the user when adding data to the cell.",
        "showCustomUi" : "True if the UI should be customized based on the kind of condition.\nIf true, \"List\" conditions will show a dropdown.",
        "strict" : "True if invalid data should be rejected."
      }
    },
    "updateDeveloperMetadata" : {
      "dataFilters" : [ {
        "developerMetadataLookup" : {
          "metadataId" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_id.",
          "metadataKey" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_key.",
          "visibility" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.visibility.  If left unspecified, all developer\nmetadata visibile to the requesting project is considered.",
          "metadataValue" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_value.",
          "locationMatchingStrategy" : "Determines how this lookup matches the location.  If this field is\nspecified as EXACT, only developer metadata associated on the exact\nlocation specified is matched.  If this field is specified to INTERSECTING,\ndeveloper metadata associated on intersecting locations is also\nmatched.  If left unspecified, this field assumes a default value of\nINTERSECTING.\nIf this field is specified, a metadataLocation\nmust also be specified.",
          "metadataLocation" : {
            "dimensionRange" : {
              "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
              "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
              "sheetId" : "The sheet this span is on.",
              "dimension" : "The dimension of the span."
            },
            "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
            "locationType" : "The type of location this object represents. This field is read-only.",
            "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
          },
          "locationType" : "Limits the selected developer metadata to those entries which are\nassociated with locations of the specified type.  For example, when this\nfield is specified as ROW this lookup\nonly considers developer metadata associated on rows.  If the field is left\nunspecified, all location types are considered.  This field cannot be\nspecified as SPREADSHEET when\nthe locationMatchingStrategy\nis specified as INTERSECTING or when the\nmetadataLocation is specified as a\nnon-spreadsheet location: spreadsheet metadata cannot intersect any other\ndeveloper metadata location.  This field also must be left unspecified when\nthe locationMatchingStrategy\nis specified as EXACT."
        },
        "gridRange" : {
          "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
          "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
          "sheetId" : "The sheet this range is on.",
          "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
          "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
        },
        "a1Range" : "Selects data that matches the specified A1 range."
      } ],
      "developerMetadata" : {
        "metadataId" : "The spreadsheet-scoped unique ID that identifies the metadata. IDs may be\nspecified when metadata is created, otherwise one will be randomly\ngenerated and assigned. Must be positive.",
        "metadataKey" : "The metadata key. There may be multiple metadata in a spreadsheet with the\nsame key.  Developer metadata must always have a key specified.",
        "visibility" : "The metadata visibility.  Developer metadata must always have a visibility\nspecified.",
        "metadataValue" : "Data associated with the metadata's key.",
        "location" : {
          "dimensionRange" : {
            "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
            "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
            "sheetId" : "The sheet this span is on.",
            "dimension" : "The dimension of the span."
          },
          "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
          "locationType" : "The type of location this object represents. This field is read-only.",
          "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
        }
      },
      "fields" : "The fields that should be updated.  At least one field must be specified.\nThe root `developerMetadata` is implied and should not be specified.\nA single `\"*\"` can be used as short-hand for listing every field."
    },
    "moveDimension" : {
      "destinationIndex" : "The zero-based start index of where to move the source data to,\nbased on the coordinates *before* the source data is removed\nfrom the grid.  Existing data will be shifted down or right\n(depending on the dimension) to make room for the moved dimensions.\nThe source dimensions are removed from the grid, so the\nthe data may end up in a different index than specified.\n\nFor example, given `A1..A5` of `0, 1, 2, 3, 4` and wanting to move\n`\"1\"` and `\"2\"` to between `\"3\"` and `\"4\"`, the source would be\n`ROWS [1..3)`,and the destination index would be `\"4\"`\n(the zero-based index of row 5).\nThe end result would be `A1..A5` of `0, 3, 1, 2, 4`.",
      "source" : {
        "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
        "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
        "sheetId" : "The sheet this span is on.",
        "dimension" : "The dimension of the span."
      }
    },
    "deleteEmbeddedObject" : {
      "objectId" : "The ID of the embedded object to delete."
    },
    "updateEmbeddedObjectPosition" : {
      "newPosition" : {
        "newSheet" : "If true, the embedded object will be put on a new sheet whose ID\nis chosen for you. Used only when writing.",
        "overlayPosition" : {
          "offsetXPixels" : "The horizontal offset, in pixels, that the object is offset\nfrom the anchor cell.",
          "offsetYPixels" : "The vertical offset, in pixels, that the object is offset\nfrom the anchor cell.",
          "heightPixels" : "The height of the object, in pixels. Defaults to 371.",
          "widthPixels" : "The width of the object, in pixels. Defaults to 600.",
          "anchorCell" : {
            "sheetId" : "The sheet this coordinate is on.",
            "rowIndex" : "The row index of the coordinate.",
            "columnIndex" : "The column index of the coordinate."
          }
        },
        "sheetId" : "The sheet this is on. Set only if the embedded object\nis on its own sheet. Must be non-negative."
      },
      "fields" : "The fields of OverlayPosition\nthat should be updated when setting a new position. Used only if\nnewPosition.overlayPosition\nis set, in which case at least one field must\nbe specified.  The root `newPosition.overlayPosition` is implied and\nshould not be specified.\nA single `\"*\"` can be used as short-hand for listing every field.",
      "objectId" : "The ID of the object to moved."
    },
    "addChart" : {
      "chart" : {
        "chartId" : "The ID of the chart.",
        "position" : {
          "newSheet" : "If true, the embedded object will be put on a new sheet whose ID\nis chosen for you. Used only when writing.",
          "overlayPosition" : {
            "offsetXPixels" : "The horizontal offset, in pixels, that the object is offset\nfrom the anchor cell.",
            "offsetYPixels" : "The vertical offset, in pixels, that the object is offset\nfrom the anchor cell.",
            "heightPixels" : "The height of the object, in pixels. Defaults to 371.",
            "widthPixels" : "The width of the object, in pixels. Defaults to 600.",
            "anchorCell" : {
              "sheetId" : "The sheet this coordinate is on.",
              "rowIndex" : "The row index of the coordinate.",
              "columnIndex" : "The column index of the coordinate."
            }
          },
          "sheetId" : "The sheet this is on. Set only if the embedded object\nis on its own sheet. Must be non-negative."
        },
        "spec" : {
          "basicChart" : {
            "compareMode" : "The behavior of tooltips and data highlighting when hovering on data and\nchart area.",
            "stackedType" : "The stacked type for charts that support vertical stacking.\nApplies to Area, Bar, Column, and Stepped Area charts.",
            "lineSmoothing" : "Gets whether all lines should be rendered smooth or straight by default.\nApplies to Line charts.",
            "threeDimensional" : "True to make the chart 3D.\nApplies to Bar and Column charts.",
            "series" : [ {
              "lineStyle" : {
                "width" : "The thickness of the line, in px.",
                "type" : "The dash type of the line."
              },
              "series" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              },
              "targetAxis" : "The minor axis that will specify the range of values for this series.\nFor example, if charting stocks over time, the \"Volume\" series\nmay want to be pinned to the right with the prices pinned to the left,\nbecause the scale of trading volume is different than the scale of\nprices.\nIt is an error to specify an axis that isn't a valid minor axis\nfor the chart's type.",
              "type" : "The type of this series. Valid only if the\nchartType is\nCOMBO.\nDifferent types will change the way the series is visualized.\nOnly LINE, AREA,\nand COLUMN are supported."
            } ],
            "interpolateNulls" : "If some values in a series are missing, gaps may appear in the chart (e.g,\nsegments of lines in a line chart will be missing).  To eliminate these\ngaps set this to true.\nApplies to Line, Area, and Combo charts.",
            "chartType" : "The type of the chart.",
            "domains" : [ {
              "domain" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              },
              "reversed" : "True to reverse the order of the domain values (horizontal axis)."
            } ],
            "headerCount" : "The number of rows or columns in the data that are \"headers\".\nIf not set, Google Sheets will guess how many rows are headers based\non the data.\n\n(Note that BasicChartAxis.title may override the axis title\n inferred from the header values.)",
            "legendPosition" : "The position of the chart legend.",
            "axis" : [ {
              "titleTextPosition" : {
                "horizontalAlignment" : "Horizontal alignment setting for the piece of text."
              },
              "format" : {
                "fontFamily" : "The font family.",
                "underline" : "True if the text is underlined.",
                "foregroundColor" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "fontSize" : "The size of the font.",
                "bold" : "True if the text is bold.",
                "strikethrough" : "True if the text has a strikethrough.",
                "italic" : "True if the text is italicized."
              },
              "position" : "The position of this axis.",
              "title" : "The title of this axis. If set, this overrides any title inferred\nfrom headers of the data."
            } ]
          },
          "backgroundColor" : {
            "red" : "The amount of red in the color as a value in the interval [0, 1].",
            "green" : "The amount of green in the color as a value in the interval [0, 1].",
            "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
            "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
          },
          "waterfallChart" : {
            "hideConnectorLines" : "True to hide connector lines between columns.",
            "stackedType" : "The stacked type.",
            "series" : [ {
              "subtotalColumnsStyle" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "label" : "The label of the column's legend."
              },
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              },
              "negativeColumnsStyle" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "label" : "The label of the column's legend."
              },
              "hideTrailingSubtotal" : "True to hide the subtotal column from the end of the series. By default,\na subtotal column will appear at the end of each series. Setting this\nfield to true will hide that subtotal column for this series.",
              "positiveColumnsStyle" : {
                "color" : {
                  "red" : "The amount of red in the color as a value in the interval [0, 1].",
                  "green" : "The amount of green in the color as a value in the interval [0, 1].",
                  "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                  "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
                },
                "label" : "The label of the column's legend."
              },
              "customSubtotals" : [ {
                "dataIsSubtotal" : "True if the data point at subtotal_index is the subtotal. If false,\nthe subtotal will be computed and appear after the data point.",
                "subtotalIndex" : "The 0-based index of a data point within the series. If\ndata_is_subtotal is true, the data point at this index is the\nsubtotal. Otherwise, the subtotal appears after the data point with\nthis index. A series can have multiple subtotals at arbitrary indices,\nbut subtotals do not affect the indices of the data points. For\nexample, if a series has 3 data points, their indices will always be 0,\n1, and 2, regardless of how many subtotals exist on the series or what\ndata points they are associated with.",
                "label" : "A label for the subtotal column."
              } ]
            } ],
            "domain" : {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              },
              "reversed" : "True to reverse the order of the domain values (horizontal axis)."
            },
            "firstValueIsTotal" : "True to interpret the first value as a total.",
            "connectorLineStyle" : {
              "width" : "The thickness of the line, in px.",
              "type" : "The dash type of the line."
            }
          },
          "altText" : "The alternative text that describes the chart.  This is often used\nfor accessibility.",
          "maximized" : "True to make a chart fill the entire space in which it's rendered with\nminimum padding.  False to use the default padding.\n(Not applicable to Geo and Org charts.)",
          "subtitleTextPosition" : {
            "horizontalAlignment" : "Horizontal alignment setting for the piece of text."
          },
          "title" : "The title of the chart.",
          "bubbleChart" : {
            "bubbleMinRadiusSize" : "The minimum radius size of the bubbles, in pixels.\nIf specific, the field must be a positive value.",
            "bubbleTextStyle" : {
              "fontFamily" : "The font family.",
              "underline" : "True if the text is underlined.",
              "foregroundColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              },
              "fontSize" : "The size of the font.",
              "bold" : "True if the text is bold.",
              "strikethrough" : "True if the text has a strikethrough.",
              "italic" : "True if the text is italicized."
            },
            "series" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "bubbleSizes" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "domain" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "bubbleOpacity" : "The opacity of the bubbles between 0 and 1.0.\n0 is fully transparent and 1 is fully opaque.",
            "bubbleMaxRadiusSize" : "The max radius size of the bubbles, in pixels.\nIf specified, the field must be a positive value.",
            "groupIds" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "bubbleBorderColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "legendPosition" : "Where the legend of the chart should be drawn.",
            "bubbleLabels" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            }
          },
          "titleTextFormat" : {
            "fontFamily" : "The font family.",
            "underline" : "True if the text is underlined.",
            "foregroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "fontSize" : "The size of the font.",
            "bold" : "True if the text is bold.",
            "strikethrough" : "True if the text has a strikethrough.",
            "italic" : "True if the text is italicized."
          },
          "histogramChart" : {
            "series" : [ {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              },
              "barColor" : {
                "red" : "The amount of red in the color as a value in the interval [0, 1].",
                "green" : "The amount of green in the color as a value in the interval [0, 1].",
                "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
                "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
              }
            } ],
            "showItemDividers" : "Whether horizontal divider lines should be displayed between items in each\ncolumn.",
            "legendPosition" : "The position of the chart legend.",
            "bucketSize" : "By default the bucket size (the range of values stacked in a single\ncolumn) is chosen automatically, but it may be overridden here.\nE.g., A bucket size of 1.5 results in buckets from 0 - 1.5, 1.5 - 3.0, etc.\nCannot be negative.\nThis field is optional.",
            "outlierPercentile" : "The outlier percentile is used to ensure that outliers do not adversely\naffect the calculation of bucket sizes.  For example, setting an outlier\npercentile of 0.05 indicates that the top and bottom 5% of values when\ncalculating buckets.  The values are still included in the chart, they will\nbe added to the first or last buckets instead of their own buckets.\nMust be between 0.0 and 0.5."
          },
          "fontName" : "The name of the font to use by default for all chart text (e.g. title,\naxis labels, legend).  If a font is specified for a specific part of the\nchart it will override this font name.",
          "subtitleTextFormat" : {
            "fontFamily" : "The font family.",
            "underline" : "True if the text is underlined.",
            "foregroundColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "fontSize" : "The size of the font.",
            "bold" : "True if the text is bold.",
            "strikethrough" : "True if the text has a strikethrough.",
            "italic" : "True if the text is italicized."
          },
          "titleTextPosition" : {
            "horizontalAlignment" : "Horizontal alignment setting for the piece of text."
          },
          "candlestickChart" : {
            "data" : [ {
              "openSeries" : {
                "data" : {
                  "sourceRange" : {
                    "sources" : [ {
                      "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                      "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                      "sheetId" : "The sheet this range is on.",
                      "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                      "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                    } ]
                  }
                }
              },
              "closeSeries" : {
                "data" : {
                  "sourceRange" : {
                    "sources" : [ {
                      "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                      "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                      "sheetId" : "The sheet this range is on.",
                      "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                      "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                    } ]
                  }
                }
              },
              "highSeries" : {
                "data" : {
                  "sourceRange" : {
                    "sources" : [ {
                      "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                      "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                      "sheetId" : "The sheet this range is on.",
                      "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                      "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                    } ]
                  }
                }
              },
              "lowSeries" : {
                "data" : {
                  "sourceRange" : {
                    "sources" : [ {
                      "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                      "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                      "sheetId" : "The sheet this range is on.",
                      "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                      "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                    } ]
                  }
                }
              }
            } ],
            "domain" : {
              "data" : {
                "sourceRange" : {
                  "sources" : [ {
                    "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                    "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                    "sheetId" : "The sheet this range is on.",
                    "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                    "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                  } ]
                }
              },
              "reversed" : "True to reverse the order of the domain values (horizontal axis)."
            }
          },
          "orgChart" : {
            "nodeSize" : "The size of the org chart nodes.",
            "parentLabels" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "nodeColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "selectedNodeColor" : {
              "red" : "The amount of red in the color as a value in the interval [0, 1].",
              "green" : "The amount of green in the color as a value in the interval [0, 1].",
              "blue" : "The amount of blue in the color as a value in the interval [0, 1].",
              "alpha" : "The fraction of this color that should be applied to the pixel. That is,\nthe final pixel color is defined by the equation:\n\n  pixel color = alpha * (this color) + (1.0 - alpha) * (background color)\n\nThis means that a value of 1.0 corresponds to a solid color, whereas\na value of 0.0 corresponds to a completely transparent color. This\nuses a wrapper message rather than a simple float scalar so that it is\npossible to distinguish between a default value and the value being unset.\nIf omitted, this color object is to be rendered as a solid color\n(as if the alpha value had been explicitly given with a value of 1.0)."
            },
            "tooltips" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "labels" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            }
          },
          "subtitle" : "The subtitle of the chart.",
          "pieChart" : {
            "pieHole" : "The size of the hole in the pie chart.",
            "threeDimensional" : "True if the pie is three dimensional.",
            "series" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "domain" : {
              "sourceRange" : {
                "sources" : [ {
                  "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
                  "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
                  "sheetId" : "The sheet this range is on.",
                  "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
                  "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
                } ]
              }
            },
            "legendPosition" : "Where the legend of the pie chart should be drawn."
          },
          "hiddenDimensionStrategy" : "Determines how the charts will use hidden rows or columns."
        }
      }
    },
    "copyPaste" : {
      "pasteType" : "What kind of data to paste.",
      "destination" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "pasteOrientation" : "How that data should be oriented when pasting.",
      "source" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      }
    }
  } ]
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## update_sheet_values

Sets values in a range of a spreadsheet.
The caller must specify the spreadsheet ID, range, and
a valueInputOption.

<details><summary>Parameters</summary>

### range (required)

The A1 notation of the values to update.

**Type:** string

### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

### $body

Data within a range of the spreadsheet.

**Type:** object

```json
{
  "majorDimension" : "The major dimension of the values.\n\nFor output, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`,\nthen requesting `range=A1:B2,majorDimension=ROWS` will return\n`[[1,2],[3,4]]`,\nwhereas requesting `range=A1:B2,majorDimension=COLUMNS` will return\n`[[1,3],[2,4]]`.\n\nFor input, with `range=A1:B2,majorDimension=ROWS` then `[[1,2],[3,4]]`\nwill set `A1=1,B1=2,A2=3,B2=4`. With `range=A1:B2,majorDimension=COLUMNS`\nthen `[[1,2],[3,4]]` will set `A1=1,B1=3,A2=2,B2=4`.\n\nWhen writing, if this field is not set, it defaults to ROWS.",
  "values" : [ [ { } ] ],
  "range" : "The range the values cover, in A1 notation.\nFor output, this range indicates the entire requested range,\neven though the values will exclude trailing rows and columns.\nWhen appending values, this field represents the range to search for a\ntable, after which values will be appended."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### includeValuesInResponse

Determines if the update response should include the values
of the cells that were updated. By default, responses
do not include the updated values.
If the range to write was larger than than the range actually written,
the response will include all values in the requested range (excluding
trailing empty rows and columns).

**Type:** boolean

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### responseDateTimeRenderOption

Determines how dates, times, and durations in the response should be
rendered. This is ignored if response_value_render_option is
FORMATTED_VALUE.
The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].

**Type:** string

**Potential values:** SERIAL_NUMBER, FORMATTED_STRING

### responseValueRenderOption

Determines how values in the response should be rendered.
The default render option is ValueRenderOption.FORMATTED_VALUE.

**Type:** string

**Potential values:** FORMATTED_VALUE, UNFORMATTED_VALUE, FORMULA

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

### valueInputOption

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

### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

### $body

The request for updating more than one range of values in a spreadsheet.

**Type:** object

```json
{
  "responseValueRenderOption" : "Determines how values in the response should be rendered.\nThe default render option is ValueRenderOption.FORMATTED_VALUE.",
  "valueInputOption" : "How the input data should be interpreted.",
  "data" : [ {
    "dataFilter" : {
      "developerMetadataLookup" : {
        "metadataId" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_id.",
        "metadataKey" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_key.",
        "visibility" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.visibility.  If left unspecified, all developer\nmetadata visibile to the requesting project is considered.",
        "metadataValue" : "Limits the selected developer metadata to that which has a matching\nDeveloperMetadata.metadata_value.",
        "locationMatchingStrategy" : "Determines how this lookup matches the location.  If this field is\nspecified as EXACT, only developer metadata associated on the exact\nlocation specified is matched.  If this field is specified to INTERSECTING,\ndeveloper metadata associated on intersecting locations is also\nmatched.  If left unspecified, this field assumes a default value of\nINTERSECTING.\nIf this field is specified, a metadataLocation\nmust also be specified.",
        "metadataLocation" : {
          "dimensionRange" : {
            "startIndex" : "The start (inclusive) of the span, or not set if unbounded.",
            "endIndex" : "The end (exclusive) of the span, or not set if unbounded.",
            "sheetId" : "The sheet this span is on.",
            "dimension" : "The dimension of the span."
          },
          "spreadsheet" : "True when metadata is associated with an entire spreadsheet.",
          "locationType" : "The type of location this object represents. This field is read-only.",
          "sheetId" : "The ID of the sheet when metadata is associated with an entire sheet."
        },
        "locationType" : "Limits the selected developer metadata to those entries which are\nassociated with locations of the specified type.  For example, when this\nfield is specified as ROW this lookup\nonly considers developer metadata associated on rows.  If the field is left\nunspecified, all location types are considered.  This field cannot be\nspecified as SPREADSHEET when\nthe locationMatchingStrategy\nis specified as INTERSECTING or when the\nmetadataLocation is specified as a\nnon-spreadsheet location: spreadsheet metadata cannot intersect any other\ndeveloper metadata location.  This field also must be left unspecified when\nthe locationMatchingStrategy\nis specified as EXACT."
      },
      "gridRange" : {
        "endColumnIndex" : "The end column (exclusive) of the range, or not set if unbounded.",
        "endRowIndex" : "The end row (exclusive) of the range, or not set if unbounded.",
        "sheetId" : "The sheet this range is on.",
        "startColumnIndex" : "The start column (inclusive) of the range, or not set if unbounded.",
        "startRowIndex" : "The start row (inclusive) of the range, or not set if unbounded."
      },
      "a1Range" : "Selects data that matches the specified A1 range."
    },
    "majorDimension" : "The major dimension of the values.",
    "values" : [ [ { } ] ]
  } ],
  "responseDateTimeRenderOption" : "Determines how dates, times, and durations in the response should be\nrendered. This is ignored if response_value_render_option is\nFORMATTED_VALUE.\nThe default dateTime render option is\nDateTimeRenderOption.SERIAL_NUMBER.",
  "includeValuesInResponse" : "Determines if the update response should include the values\nof the cells that were updated. By default, responses\ndo not include the updated values. The `updatedData` field within\neach of the BatchUpdateValuesResponse.responses will contain\nthe updated values. If the range to write was larger than than the range\nactually written, the response will include all values in the requested\nrange (excluding trailing empty rows and columns)."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

## update_sheet_values_in_batch

Sets values in one or more ranges of a spreadsheet.
The caller must specify the spreadsheet ID,
a valueInputOption, and one or more
ValueRanges.

<details><summary>Parameters</summary>

### spreadsheetId (required)

The ID of the spreadsheet to update.

**Type:** string

### $body

The request for updating more than one range of values in a spreadsheet.

**Type:** object

```json
{
  "responseValueRenderOption" : "Determines how values in the response should be rendered.\nThe default render option is ValueRenderOption.FORMATTED_VALUE.",
  "valueInputOption" : "How the input data should be interpreted.",
  "data" : [ {
    "majorDimension" : "The major dimension of the values.\n\nFor output, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`,\nthen requesting `range=A1:B2,majorDimension=ROWS` will return\n`[[1,2],[3,4]]`,\nwhereas requesting `range=A1:B2,majorDimension=COLUMNS` will return\n`[[1,3],[2,4]]`.\n\nFor input, with `range=A1:B2,majorDimension=ROWS` then `[[1,2],[3,4]]`\nwill set `A1=1,B1=2,A2=3,B2=4`. With `range=A1:B2,majorDimension=COLUMNS`\nthen `[[1,2],[3,4]]` will set `A1=1,B1=3,A2=2,B2=4`.\n\nWhen writing, if this field is not set, it defaults to ROWS.",
    "values" : [ [ { } ] ],
    "range" : "The range the values cover, in A1 notation.\nFor output, this range indicates the entire requested range,\neven though the values will exclude trailing rows and columns.\nWhen appending values, this field represents the range to search for a\ntable, after which values will be appended."
  } ],
  "responseDateTimeRenderOption" : "Determines how dates, times, and durations in the response should be\nrendered. This is ignored if response_value_render_option is\nFORMATTED_VALUE.\nThe default dateTime render option is\nDateTimeRenderOption.SERIAL_NUMBER.",
  "includeValuesInResponse" : "Determines if the update response should include the values\nof the cells that were updated. By default, responses\ndo not include the updated values. The `updatedData` field within\neach of the BatchUpdateValuesResponse.responses will contain\nthe updated values. If the range to write was larger than than the range\nactually written, the response will include all values in the requested\nrange (excluding trailing empty rows and columns)."
}
```

### alt

Data format for response.

**Type:** string

**Potential values:** json, media, proto

### callback

JSONP

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.

**Type:** string

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

