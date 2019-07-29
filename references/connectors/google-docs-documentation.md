---
id: google-docs-documentation
title: Google Docs (version v1.*.*)
sidebar_label: Google Docs
layout: docs.mustache
---

## batch_update_document

Applies one or more updates to the document. Each request is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests. For example, suppose you call batchUpdate with four updates, and only the third one returns information. The response would have two empty replies, the reply to the third request, and another empty reply, in that order. Because other users may be editing the document, the document might not exactly reflect your changes: your changes may be altered with respect to collaborator changes. If there are no collaborators, the document should reflect your changes. In any case, the updates in your request are guaranteed to be applied together atomically.

<details><summary>Parameters</summary>

### documentId (required)

The ID of the document to update.

**Type:** string

### $body

Request message for BatchUpdateDocument.

**Type:** object

```json
{
  "requests" : [ {
    "deleteParagraphBullets" : {
      "range" : {
        "startIndex" : "The zero-based start index of this range, in UTF-16 code units.\n\nIn all current uses, a start index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "endIndex" : "The zero-based end index of this range, exclusive, in UTF-16 code units.\n\nIn all current uses, an end index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "segmentId" : "The ID of the header, footer or footnote that this range is contained in.\nAn empty segment ID signifies the document's body."
      }
    },
    "updateParagraphStyle" : {
      "paragraphStyle" : {
        "indentFirstLine" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "shading" : {
          "backgroundColor" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          }
        },
        "indentStart" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "borderTop" : {
          "padding" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "color" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          },
          "dashStyle" : "The dash style of the border.",
          "width" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "lineSpacing" : "The amount of space between lines, as a percentage of normal, where normal\nis represented as 100.0. If unset, the value is inherited from the parent.",
        "indentEnd" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "borderLeft" : {
          "padding" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "color" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          },
          "dashStyle" : "The dash style of the border.",
          "width" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "spaceAbove" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "keepWithNext" : "Whether at least a part of this paragraph should be laid out on the same\npage or column as the next paragraph if possible. If unset, the value is\ninherited from the parent.",
        "spacingMode" : "The spacing mode for the paragraph.",
        "borderRight" : {
          "padding" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "color" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          },
          "dashStyle" : "The dash style of the border.",
          "width" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "borderBetween" : {
          "padding" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "color" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          },
          "dashStyle" : "The dash style of the border.",
          "width" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "keepLinesTogether" : "Whether all lines of the paragraph should be laid out on the same page or\ncolumn if possible. If unset, the value is inherited from the parent.",
        "tabStops" : [ {
          "offset" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "alignment" : "The alignment of this tab stop. If unset, the value defaults to START."
        } ],
        "alignment" : "The text alignment for this paragraph.",
        "avoidWidowAndOrphan" : "Whether to avoid widows and orphans for the paragraph. If unset, the value\nis inherited from the parent.",
        "borderBottom" : {
          "padding" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "color" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          },
          "dashStyle" : "The dash style of the border.",
          "width" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "headingId" : "The heading ID of the paragraph. If empty, then this paragraph is not a\nheading. This property is read-only.",
        "direction" : "The text direction of this paragraph. If unset, the value defaults to\nLEFT_TO_RIGHT since\nparagraph direction is not inherited.",
        "namedStyleType" : "The named style type of the paragraph.\n\nSince updating the named style type affects other properties within\nParagraphStyle, the named style type is applied before the other properties\nare updated.",
        "spaceBelow" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        }
      },
      "range" : {
        "startIndex" : "The zero-based start index of this range, in UTF-16 code units.\n\nIn all current uses, a start index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "endIndex" : "The zero-based end index of this range, exclusive, in UTF-16 code units.\n\nIn all current uses, an end index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "segmentId" : "The ID of the header, footer or footnote that this range is contained in.\nAn empty segment ID signifies the document's body."
      },
      "fields" : "The fields that should be updated.\n\nAt least one field must be specified. The root `paragraph_style` is implied\nand should not be specified.\n\nFor example, to update the paragraph style's alignment property, set\n`fields` to `\"alignment\"`.\n\nTo reset a property to its default value, include its field name in the\nfield mask but leave the field itself unset."
    },
    "updateTextStyle" : {
      "range" : {
        "startIndex" : "The zero-based start index of this range, in UTF-16 code units.\n\nIn all current uses, a start index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "endIndex" : "The zero-based end index of this range, exclusive, in UTF-16 code units.\n\nIn all current uses, an end index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "segmentId" : "The ID of the header, footer or footnote that this range is contained in.\nAn empty segment ID signifies the document's body."
      },
      "textStyle" : {
        "backgroundColor" : {
          "color" : {
            "rgbColor" : {
              "red" : "The red component of the color, from 0.0 to 1.0.",
              "green" : "The green component of the color, from 0.0 to 1.0.",
              "blue" : "The blue component of the color, from 0.0 to 1.0."
            }
          }
        },
        "underline" : "Whether or not the text is underlined.",
        "link" : {
          "bookmarkId" : "The ID of a bookmark in this document.",
          "headingId" : "The ID of a heading in this document.",
          "url" : "An external URL."
        },
        "fontSize" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "foregroundColor" : {
          "color" : {
            "rgbColor" : {
              "red" : "The red component of the color, from 0.0 to 1.0.",
              "green" : "The green component of the color, from 0.0 to 1.0.",
              "blue" : "The blue component of the color, from 0.0 to 1.0."
            }
          }
        },
        "bold" : "Whether or not the text is rendered as bold.",
        "strikethrough" : "Whether or not the text is struck through.",
        "baselineOffset" : "The text's vertical offset from its normal position.\n\nText with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically\nrendered in a smaller font size, computed based on the `font_size` field.\nThe `font_size` itself is not affected by changes in this field.",
        "italic" : "Whether or not the text is italicized.",
        "weightedFontFamily" : {
          "fontFamily" : "The font family of the text.\n\nThe font family can be any font from the Font menu in Docs or from\n[Google Fonts] (https://fonts.google.com/). If the font name is\nunrecognized, the text is rendered in `Arial`.",
          "weight" : "The weight of the font. This field can have any value that is a multiple of\n`100` between `100` and `900`, inclusive. This range corresponds to the\nnumerical values described in the CSS 2.1 Specification,\n[section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with\nnon-numerical values disallowed.\n\nThe default value is `400` (\"normal\").\n\nThe font weight makes up just one component of the rendered font weight.\nThe rendered weight is determined by a combination of the `weight` and the\ntext style's resolved `bold` value, after accounting for inheritance:\n\n* If the text is bold and the weight is less than `400`, the rendered\n  weight is 400.\n* If the text is bold and the weight is greater than or equal to `400` but\n  is less than `700`, the rendered weight is `700`.\n* If the weight is greater than or equal to `700`, the rendered weight is\n  equal to the weight.\n* If the text is not bold, the rendered weight is equal to the weight."
        },
        "smallCaps" : "Whether or not the text is in small capital letters."
      },
      "fields" : "The fields that should be updated.\n\nAt least one field must be specified. The root `text_style` is implied and\nshould not be specified. A single `\"*\"` can be used as short-hand for\nlisting every field.\n\nFor example, to update the text style to bold, set `fields` to `\"bold\"`.\n\nTo reset a property to its default value, include its field name in the\nfield mask but leave the field itself unset."
    },
    "deleteContentRange" : {
      "range" : {
        "startIndex" : "The zero-based start index of this range, in UTF-16 code units.\n\nIn all current uses, a start index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "endIndex" : "The zero-based end index of this range, exclusive, in UTF-16 code units.\n\nIn all current uses, an end index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "segmentId" : "The ID of the header, footer or footnote that this range is contained in.\nAn empty segment ID signifies the document's body."
      }
    },
    "insertTable" : {
      "columns" : "The number of columns in the table.",
      "location" : {
        "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body.",
        "index" : "The zero-based index, in UTF-16 code units.\n\nThe index is relative to the beginning of the segment specified by\nsegment_id."
      },
      "endOfSegmentLocation" : {
        "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body."
      },
      "rows" : "The number of rows in the table."
    },
    "insertInlineImage" : {
      "objectSize" : {
        "width" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "height" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        }
      },
      "location" : {
        "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body.",
        "index" : "The zero-based index, in UTF-16 code units.\n\nThe index is relative to the beginning of the segment specified by\nsegment_id."
      },
      "endOfSegmentLocation" : {
        "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body."
      },
      "uri" : "The image URI.\n\nThe image is fetched once at insertion time and a copy is stored for\ndisplay inside the document. Images must be less than 50MB in size, cannot\nexceed 25 megapixels, and must be in one of PNG, JPEG, or GIF format.\n\nThe provided URI can be at most 2 kB in length. The URI itself is saved\nwith the image, and exposed via the ImageProperties.content_uri field."
    },
    "createParagraphBullets" : {
      "bulletPreset" : "The kinds of bullet glyphs to be used.",
      "range" : {
        "startIndex" : "The zero-based start index of this range, in UTF-16 code units.\n\nIn all current uses, a start index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "endIndex" : "The zero-based end index of this range, exclusive, in UTF-16 code units.\n\nIn all current uses, an end index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "segmentId" : "The ID of the header, footer or footnote that this range is contained in.\nAn empty segment ID signifies the document's body."
      }
    },
    "deleteNamedRange" : {
      "namedRangeId" : "The ID of the named range to delete.",
      "name" : "The name of the range(s) to delete. All named ranges with the given\nname will be deleted."
    },
    "deleteTableColumn" : {
      "tableCellLocation" : {
        "columnIndex" : "The zero-based column index. For example, the second column in the table\nhas a column index of 1.",
        "rowIndex" : "The zero-based row index. For example, the second row in the table has a\nrow index of 1.",
        "tableStartLocation" : {
          "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body.",
          "index" : "The zero-based index, in UTF-16 code units.\n\nThe index is relative to the beginning of the segment specified by\nsegment_id."
        }
      }
    },
    "deletePositionedObject" : {
      "objectId" : "The ID of the positioned object to delete."
    },
    "insertText" : {
      "location" : {
        "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body.",
        "index" : "The zero-based index, in UTF-16 code units.\n\nThe index is relative to the beginning of the segment specified by\nsegment_id."
      },
      "text" : "The text to be inserted.\n\nInserting a newline character will implicitly create a new\nParagraph at that index.\nThe paragraph style of the new paragraph will be copied from the paragraph\nat the current insertion index, including lists and bullets.\n\nText styles for inserted text will be determined automatically, generally\npreserving the styling of neighboring text. In most cases, the text style\nfor the inserted text will match the text immediately before the insertion\nindex.\n\nSome control characters (U+0000-U+0008, U+000C-U+001F) and characters\nfrom the Unicode Basic Multilingual Plane Private Use Area (U+E000-U+F8FF)\nwill be stripped out of the inserted text.",
      "endOfSegmentLocation" : {
        "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body."
      }
    },
    "insertPageBreak" : {
      "location" : {
        "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body.",
        "index" : "The zero-based index, in UTF-16 code units.\n\nThe index is relative to the beginning of the segment specified by\nsegment_id."
      },
      "endOfSegmentLocation" : {
        "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body."
      }
    },
    "deleteTableRow" : {
      "tableCellLocation" : {
        "columnIndex" : "The zero-based column index. For example, the second column in the table\nhas a column index of 1.",
        "rowIndex" : "The zero-based row index. For example, the second row in the table has a\nrow index of 1.",
        "tableStartLocation" : {
          "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body.",
          "index" : "The zero-based index, in UTF-16 code units.\n\nThe index is relative to the beginning of the segment specified by\nsegment_id."
        }
      }
    },
    "createNamedRange" : {
      "name" : "The name of the NamedRange. Names do not need to be unique.\n\nNames must be at least 1 character and no more than 256 characters,\nmeasured in UTF-16 code units.",
      "range" : {
        "startIndex" : "The zero-based start index of this range, in UTF-16 code units.\n\nIn all current uses, a start index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "endIndex" : "The zero-based end index of this range, exclusive, in UTF-16 code units.\n\nIn all current uses, an end index must be provided. This field is an\nInt32Value in order to accommodate future use cases with open-ended ranges.",
        "segmentId" : "The ID of the header, footer or footnote that this range is contained in.\nAn empty segment ID signifies the document's body."
      }
    },
    "insertTableRow" : {
      "insertBelow" : "Whether to insert new row below the reference cell location.\n\n- `True`: insert below the cell.\n- `False`: insert above the cell.",
      "tableCellLocation" : {
        "columnIndex" : "The zero-based column index. For example, the second column in the table\nhas a column index of 1.",
        "rowIndex" : "The zero-based row index. For example, the second row in the table has a\nrow index of 1.",
        "tableStartLocation" : {
          "segmentId" : "The ID of the header, footer or footnote the location is in. An empty\nsegment ID signifies the document's body.",
          "index" : "The zero-based index, in UTF-16 code units.\n\nThe index is relative to the beginning of the segment specified by\nsegment_id."
        }
      }
    },
    "replaceAllText" : {
      "replaceText" : "The text that will replace the matched text.",
      "containsText" : {
        "matchCase" : "Indicates whether the search should respect case:\n\n- `True`: the search is case sensitive.\n- `False`: the search is case insensitive.",
        "text" : "The text to search for in the document."
      }
    }
  } ],
  "writeControl" : {
    "targetRevisionId" : "The target revision ID of the\ndocument that the write request will be applied to.\n\nIf collaborator changes have occurred after the document was read using\nthe API, the changes produced by this write request will be transformed\nagainst the collaborator changes. This results in a new revision of the\ndocument which incorporates both the changes in the request and the\ncollaborator changes, and the Docs server will resolve conflicting\nchanges. When using `target_revision_id`, the API client can be thought\nof as another collaborator of the document.\n\nThe target revision ID may only be used to write to recent versions of a\ndocument. If the target revision is too far behind the latest revision,\nthe request will not be processed and will return a 400 bad request error\nand the request should be retried after reading the latest version of the\ndocument. In most cases a `revision_id` will remain valid for use as a\ntarget revision for several minutes after it is read, but for\nfrequently-edited documents this window may be shorter.",
    "requiredRevisionId" : "The revision ID of the\ndocument that the write request will be applied to. If this is not the\nlatest revision of the document, the request will not be processed and\nwill return a 400 bad request error.\n\nWhen a required revision ID is returned in a response, it indicates the\nrevision ID of the document after the request was applied."
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

## create_document

Creates a blank document using the title given in the request. Other fields in the request, including any provided content, are ignored. Returns the created document.

<details><summary>Parameters</summary>

### $body

A Google Docs document.

**Type:** object

```json
{
  "headers" : "The headers in the document, keyed by header ID.",
  "positionedObjects" : "The positioned objects in the document, keyed by object ID.",
  "inlineObjects" : "The inline objects in the document, keyed by object ID.",
  "namedStyles" : {
    "styles" : [ {
      "paragraphStyle" : {
        "indentFirstLine" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "shading" : {
          "backgroundColor" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          }
        },
        "indentStart" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "borderTop" : {
          "padding" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "color" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          },
          "dashStyle" : "The dash style of the border.",
          "width" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "lineSpacing" : "The amount of space between lines, as a percentage of normal, where normal\nis represented as 100.0. If unset, the value is inherited from the parent.",
        "indentEnd" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "borderLeft" : {
          "padding" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "color" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          },
          "dashStyle" : "The dash style of the border.",
          "width" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "spaceAbove" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "keepWithNext" : "Whether at least a part of this paragraph should be laid out on the same\npage or column as the next paragraph if possible. If unset, the value is\ninherited from the parent.",
        "spacingMode" : "The spacing mode for the paragraph.",
        "borderRight" : {
          "padding" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "color" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          },
          "dashStyle" : "The dash style of the border.",
          "width" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "borderBetween" : {
          "padding" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "color" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          },
          "dashStyle" : "The dash style of the border.",
          "width" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "keepLinesTogether" : "Whether all lines of the paragraph should be laid out on the same page or\ncolumn if possible. If unset, the value is inherited from the parent.",
        "tabStops" : [ {
          "offset" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "alignment" : "The alignment of this tab stop. If unset, the value defaults to START."
        } ],
        "alignment" : "The text alignment for this paragraph.",
        "avoidWidowAndOrphan" : "Whether to avoid widows and orphans for the paragraph. If unset, the value\nis inherited from the parent.",
        "borderBottom" : {
          "padding" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "color" : {
            "color" : {
              "rgbColor" : {
                "red" : "The red component of the color, from 0.0 to 1.0.",
                "green" : "The green component of the color, from 0.0 to 1.0.",
                "blue" : "The blue component of the color, from 0.0 to 1.0."
              }
            }
          },
          "dashStyle" : "The dash style of the border.",
          "width" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "headingId" : "The heading ID of the paragraph. If empty, then this paragraph is not a\nheading. This property is read-only.",
        "direction" : "The text direction of this paragraph. If unset, the value defaults to\nLEFT_TO_RIGHT since\nparagraph direction is not inherited.",
        "namedStyleType" : "The named style type of the paragraph.\n\nSince updating the named style type affects other properties within\nParagraphStyle, the named style type is applied before the other properties\nare updated.",
        "spaceBelow" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        }
      },
      "textStyle" : {
        "backgroundColor" : {
          "color" : {
            "rgbColor" : {
              "red" : "The red component of the color, from 0.0 to 1.0.",
              "green" : "The green component of the color, from 0.0 to 1.0.",
              "blue" : "The blue component of the color, from 0.0 to 1.0."
            }
          }
        },
        "underline" : "Whether or not the text is underlined.",
        "link" : {
          "bookmarkId" : "The ID of a bookmark in this document.",
          "headingId" : "The ID of a heading in this document.",
          "url" : "An external URL."
        },
        "fontSize" : {
          "unit" : "The units for magnitude.",
          "magnitude" : "The magnitude."
        },
        "foregroundColor" : {
          "color" : {
            "rgbColor" : {
              "red" : "The red component of the color, from 0.0 to 1.0.",
              "green" : "The green component of the color, from 0.0 to 1.0.",
              "blue" : "The blue component of the color, from 0.0 to 1.0."
            }
          }
        },
        "bold" : "Whether or not the text is rendered as bold.",
        "strikethrough" : "Whether or not the text is struck through.",
        "baselineOffset" : "The text's vertical offset from its normal position.\n\nText with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically\nrendered in a smaller font size, computed based on the `font_size` field.\nThe `font_size` itself is not affected by changes in this field.",
        "italic" : "Whether or not the text is italicized.",
        "weightedFontFamily" : {
          "fontFamily" : "The font family of the text.\n\nThe font family can be any font from the Font menu in Docs or from\n[Google Fonts] (https://fonts.google.com/). If the font name is\nunrecognized, the text is rendered in `Arial`.",
          "weight" : "The weight of the font. This field can have any value that is a multiple of\n`100` between `100` and `900`, inclusive. This range corresponds to the\nnumerical values described in the CSS 2.1 Specification,\n[section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with\nnon-numerical values disallowed.\n\nThe default value is `400` (\"normal\").\n\nThe font weight makes up just one component of the rendered font weight.\nThe rendered weight is determined by a combination of the `weight` and the\ntext style's resolved `bold` value, after accounting for inheritance:\n\n* If the text is bold and the weight is less than `400`, the rendered\n  weight is 400.\n* If the text is bold and the weight is greater than or equal to `400` but\n  is less than `700`, the rendered weight is `700`.\n* If the weight is greater than or equal to `700`, the rendered weight is\n  equal to the weight.\n* If the text is not bold, the rendered weight is equal to the weight."
        },
        "smallCaps" : "Whether or not the text is in small capital letters."
      },
      "namedStyleType" : "The type of this named style."
    } ]
  },
  "suggestedNamedStylesChanges" : "The suggested changes to the named styles of the document, keyed by\nsuggestion ID.",
  "body" : {
    "content" : [ {
      "paragraph" : {
        "paragraphStyle" : {
          "indentFirstLine" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "shading" : {
            "backgroundColor" : {
              "color" : {
                "rgbColor" : {
                  "red" : "The red component of the color, from 0.0 to 1.0.",
                  "green" : "The green component of the color, from 0.0 to 1.0.",
                  "blue" : "The blue component of the color, from 0.0 to 1.0."
                }
              }
            }
          },
          "indentStart" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "borderTop" : {
            "padding" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            },
            "color" : {
              "color" : {
                "rgbColor" : {
                  "red" : "The red component of the color, from 0.0 to 1.0.",
                  "green" : "The green component of the color, from 0.0 to 1.0.",
                  "blue" : "The blue component of the color, from 0.0 to 1.0."
                }
              }
            },
            "dashStyle" : "The dash style of the border.",
            "width" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            }
          },
          "lineSpacing" : "The amount of space between lines, as a percentage of normal, where normal\nis represented as 100.0. If unset, the value is inherited from the parent.",
          "indentEnd" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "borderLeft" : {
            "padding" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            },
            "color" : {
              "color" : {
                "rgbColor" : {
                  "red" : "The red component of the color, from 0.0 to 1.0.",
                  "green" : "The green component of the color, from 0.0 to 1.0.",
                  "blue" : "The blue component of the color, from 0.0 to 1.0."
                }
              }
            },
            "dashStyle" : "The dash style of the border.",
            "width" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            }
          },
          "spaceAbove" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          },
          "keepWithNext" : "Whether at least a part of this paragraph should be laid out on the same\npage or column as the next paragraph if possible. If unset, the value is\ninherited from the parent.",
          "spacingMode" : "The spacing mode for the paragraph.",
          "borderRight" : {
            "padding" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            },
            "color" : {
              "color" : {
                "rgbColor" : {
                  "red" : "The red component of the color, from 0.0 to 1.0.",
                  "green" : "The green component of the color, from 0.0 to 1.0.",
                  "blue" : "The blue component of the color, from 0.0 to 1.0."
                }
              }
            },
            "dashStyle" : "The dash style of the border.",
            "width" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            }
          },
          "borderBetween" : {
            "padding" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            },
            "color" : {
              "color" : {
                "rgbColor" : {
                  "red" : "The red component of the color, from 0.0 to 1.0.",
                  "green" : "The green component of the color, from 0.0 to 1.0.",
                  "blue" : "The blue component of the color, from 0.0 to 1.0."
                }
              }
            },
            "dashStyle" : "The dash style of the border.",
            "width" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            }
          },
          "keepLinesTogether" : "Whether all lines of the paragraph should be laid out on the same page or\ncolumn if possible. If unset, the value is inherited from the parent.",
          "tabStops" : [ {
            "offset" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            },
            "alignment" : "The alignment of this tab stop. If unset, the value defaults to START."
          } ],
          "alignment" : "The text alignment for this paragraph.",
          "avoidWidowAndOrphan" : "Whether to avoid widows and orphans for the paragraph. If unset, the value\nis inherited from the parent.",
          "borderBottom" : {
            "padding" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            },
            "color" : {
              "color" : {
                "rgbColor" : {
                  "red" : "The red component of the color, from 0.0 to 1.0.",
                  "green" : "The green component of the color, from 0.0 to 1.0.",
                  "blue" : "The blue component of the color, from 0.0 to 1.0."
                }
              }
            },
            "dashStyle" : "The dash style of the border.",
            "width" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            }
          },
          "headingId" : "The heading ID of the paragraph. If empty, then this paragraph is not a\nheading. This property is read-only.",
          "direction" : "The text direction of this paragraph. If unset, the value defaults to\nLEFT_TO_RIGHT since\nparagraph direction is not inherited.",
          "namedStyleType" : "The named style type of the paragraph.\n\nSince updating the named style type affects other properties within\nParagraphStyle, the named style type is applied before the other properties\nare updated.",
          "spaceBelow" : {
            "unit" : "The units for magnitude.",
            "magnitude" : "The magnitude."
          }
        },
        "suggestedPositionedObjectIds" : "The IDs of the positioned objects that are suggested to be attached to this\nparagraph, keyed by suggestion ID.",
        "suggestedBulletChanges" : "The suggested changes to this paragraph's bullet.",
        "elements" : [ {
          "footnoteReference" : {
            "suggestedTextStyleChanges" : "The suggested text style changes to this FootnoteReference, keyed by\nsuggestion ID.",
            "footnoteNumber" : "The rendered number of this footnote.",
            "footnoteId" : "The ID of the footnote that\ncontains the content of this footnote reference.",
            "suggestedDeletionIds" : [ "string" ],
            "textStyle" : {
              "backgroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "underline" : "Whether or not the text is underlined.",
              "link" : {
                "bookmarkId" : "The ID of a bookmark in this document.",
                "headingId" : "The ID of a heading in this document.",
                "url" : "An external URL."
              },
              "fontSize" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              },
              "foregroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "bold" : "Whether or not the text is rendered as bold.",
              "strikethrough" : "Whether or not the text is struck through.",
              "baselineOffset" : "The text's vertical offset from its normal position.\n\nText with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically\nrendered in a smaller font size, computed based on the `font_size` field.\nThe `font_size` itself is not affected by changes in this field.",
              "italic" : "Whether or not the text is italicized.",
              "weightedFontFamily" : {
                "fontFamily" : "The font family of the text.\n\nThe font family can be any font from the Font menu in Docs or from\n[Google Fonts] (https://fonts.google.com/). If the font name is\nunrecognized, the text is rendered in `Arial`.",
                "weight" : "The weight of the font. This field can have any value that is a multiple of\n`100` between `100` and `900`, inclusive. This range corresponds to the\nnumerical values described in the CSS 2.1 Specification,\n[section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with\nnon-numerical values disallowed.\n\nThe default value is `400` (\"normal\").\n\nThe font weight makes up just one component of the rendered font weight.\nThe rendered weight is determined by a combination of the `weight` and the\ntext style's resolved `bold` value, after accounting for inheritance:\n\n* If the text is bold and the weight is less than `400`, the rendered\n  weight is 400.\n* If the text is bold and the weight is greater than or equal to `400` but\n  is less than `700`, the rendered weight is `700`.\n* If the weight is greater than or equal to `700`, the rendered weight is\n  equal to the weight.\n* If the text is not bold, the rendered weight is equal to the weight."
              },
              "smallCaps" : "Whether or not the text is in small capital letters."
            },
            "suggestedInsertionIds" : [ "string" ]
          },
          "horizontalRule" : {
            "suggestedTextStyleChanges" : "The suggested text style changes to this HorizontalRule, keyed by\nsuggestion ID.",
            "suggestedDeletionIds" : [ "string" ],
            "textStyle" : {
              "backgroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "underline" : "Whether or not the text is underlined.",
              "link" : {
                "bookmarkId" : "The ID of a bookmark in this document.",
                "headingId" : "The ID of a heading in this document.",
                "url" : "An external URL."
              },
              "fontSize" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              },
              "foregroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "bold" : "Whether or not the text is rendered as bold.",
              "strikethrough" : "Whether or not the text is struck through.",
              "baselineOffset" : "The text's vertical offset from its normal position.\n\nText with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically\nrendered in a smaller font size, computed based on the `font_size` field.\nThe `font_size` itself is not affected by changes in this field.",
              "italic" : "Whether or not the text is italicized.",
              "weightedFontFamily" : {
                "fontFamily" : "The font family of the text.\n\nThe font family can be any font from the Font menu in Docs or from\n[Google Fonts] (https://fonts.google.com/). If the font name is\nunrecognized, the text is rendered in `Arial`.",
                "weight" : "The weight of the font. This field can have any value that is a multiple of\n`100` between `100` and `900`, inclusive. This range corresponds to the\nnumerical values described in the CSS 2.1 Specification,\n[section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with\nnon-numerical values disallowed.\n\nThe default value is `400` (\"normal\").\n\nThe font weight makes up just one component of the rendered font weight.\nThe rendered weight is determined by a combination of the `weight` and the\ntext style's resolved `bold` value, after accounting for inheritance:\n\n* If the text is bold and the weight is less than `400`, the rendered\n  weight is 400.\n* If the text is bold and the weight is greater than or equal to `400` but\n  is less than `700`, the rendered weight is `700`.\n* If the weight is greater than or equal to `700`, the rendered weight is\n  equal to the weight.\n* If the text is not bold, the rendered weight is equal to the weight."
              },
              "smallCaps" : "Whether or not the text is in small capital letters."
            },
            "suggestedInsertionIds" : [ "string" ]
          },
          "startIndex" : "The zero-based start index of this paragraph element, in UTF-16 code units.",
          "textRun" : {
            "suggestedTextStyleChanges" : "The suggested text style changes to this run, keyed by suggestion ID.",
            "suggestedDeletionIds" : [ "string" ],
            "textStyle" : {
              "backgroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "underline" : "Whether or not the text is underlined.",
              "link" : {
                "bookmarkId" : "The ID of a bookmark in this document.",
                "headingId" : "The ID of a heading in this document.",
                "url" : "An external URL."
              },
              "fontSize" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              },
              "foregroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "bold" : "Whether or not the text is rendered as bold.",
              "strikethrough" : "Whether or not the text is struck through.",
              "baselineOffset" : "The text's vertical offset from its normal position.\n\nText with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically\nrendered in a smaller font size, computed based on the `font_size` field.\nThe `font_size` itself is not affected by changes in this field.",
              "italic" : "Whether or not the text is italicized.",
              "weightedFontFamily" : {
                "fontFamily" : "The font family of the text.\n\nThe font family can be any font from the Font menu in Docs or from\n[Google Fonts] (https://fonts.google.com/). If the font name is\nunrecognized, the text is rendered in `Arial`.",
                "weight" : "The weight of the font. This field can have any value that is a multiple of\n`100` between `100` and `900`, inclusive. This range corresponds to the\nnumerical values described in the CSS 2.1 Specification,\n[section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with\nnon-numerical values disallowed.\n\nThe default value is `400` (\"normal\").\n\nThe font weight makes up just one component of the rendered font weight.\nThe rendered weight is determined by a combination of the `weight` and the\ntext style's resolved `bold` value, after accounting for inheritance:\n\n* If the text is bold and the weight is less than `400`, the rendered\n  weight is 400.\n* If the text is bold and the weight is greater than or equal to `400` but\n  is less than `700`, the rendered weight is `700`.\n* If the weight is greater than or equal to `700`, the rendered weight is\n  equal to the weight.\n* If the text is not bold, the rendered weight is equal to the weight."
              },
              "smallCaps" : "Whether or not the text is in small capital letters."
            },
            "content" : "The text of this run.\n\nAny non-text elements in the run are replaced with the Unicode character\nU+E907.",
            "suggestedInsertionIds" : [ "string" ]
          },
          "pageBreak" : {
            "suggestedTextStyleChanges" : "The suggested text style changes to this PageBreak, keyed by suggestion ID.",
            "suggestedDeletionIds" : [ "string" ],
            "textStyle" : {
              "backgroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "underline" : "Whether or not the text is underlined.",
              "link" : {
                "bookmarkId" : "The ID of a bookmark in this document.",
                "headingId" : "The ID of a heading in this document.",
                "url" : "An external URL."
              },
              "fontSize" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              },
              "foregroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "bold" : "Whether or not the text is rendered as bold.",
              "strikethrough" : "Whether or not the text is struck through.",
              "baselineOffset" : "The text's vertical offset from its normal position.\n\nText with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically\nrendered in a smaller font size, computed based on the `font_size` field.\nThe `font_size` itself is not affected by changes in this field.",
              "italic" : "Whether or not the text is italicized.",
              "weightedFontFamily" : {
                "fontFamily" : "The font family of the text.\n\nThe font family can be any font from the Font menu in Docs or from\n[Google Fonts] (https://fonts.google.com/). If the font name is\nunrecognized, the text is rendered in `Arial`.",
                "weight" : "The weight of the font. This field can have any value that is a multiple of\n`100` between `100` and `900`, inclusive. This range corresponds to the\nnumerical values described in the CSS 2.1 Specification,\n[section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with\nnon-numerical values disallowed.\n\nThe default value is `400` (\"normal\").\n\nThe font weight makes up just one component of the rendered font weight.\nThe rendered weight is determined by a combination of the `weight` and the\ntext style's resolved `bold` value, after accounting for inheritance:\n\n* If the text is bold and the weight is less than `400`, the rendered\n  weight is 400.\n* If the text is bold and the weight is greater than or equal to `400` but\n  is less than `700`, the rendered weight is `700`.\n* If the weight is greater than or equal to `700`, the rendered weight is\n  equal to the weight.\n* If the text is not bold, the rendered weight is equal to the weight."
              },
              "smallCaps" : "Whether or not the text is in small capital letters."
            },
            "suggestedInsertionIds" : [ "string" ]
          },
          "endIndex" : "The zero-base end index of this paragraph element, exclusive, in UTF-16\ncode units.",
          "equation" : {
            "suggestedDeletionIds" : [ "string" ],
            "suggestedInsertionIds" : [ "string" ]
          },
          "inlineObjectElement" : {
            "inlineObjectId" : "The ID of the InlineObject this\nelement contains.",
            "suggestedTextStyleChanges" : "The suggested text style changes to this InlineObject, keyed by suggestion\nID.",
            "suggestedDeletionIds" : [ "string" ],
            "textStyle" : {
              "backgroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "underline" : "Whether or not the text is underlined.",
              "link" : {
                "bookmarkId" : "The ID of a bookmark in this document.",
                "headingId" : "The ID of a heading in this document.",
                "url" : "An external URL."
              },
              "fontSize" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              },
              "foregroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "bold" : "Whether or not the text is rendered as bold.",
              "strikethrough" : "Whether or not the text is struck through.",
              "baselineOffset" : "The text's vertical offset from its normal position.\n\nText with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically\nrendered in a smaller font size, computed based on the `font_size` field.\nThe `font_size` itself is not affected by changes in this field.",
              "italic" : "Whether or not the text is italicized.",
              "weightedFontFamily" : {
                "fontFamily" : "The font family of the text.\n\nThe font family can be any font from the Font menu in Docs or from\n[Google Fonts] (https://fonts.google.com/). If the font name is\nunrecognized, the text is rendered in `Arial`.",
                "weight" : "The weight of the font. This field can have any value that is a multiple of\n`100` between `100` and `900`, inclusive. This range corresponds to the\nnumerical values described in the CSS 2.1 Specification,\n[section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with\nnon-numerical values disallowed.\n\nThe default value is `400` (\"normal\").\n\nThe font weight makes up just one component of the rendered font weight.\nThe rendered weight is determined by a combination of the `weight` and the\ntext style's resolved `bold` value, after accounting for inheritance:\n\n* If the text is bold and the weight is less than `400`, the rendered\n  weight is 400.\n* If the text is bold and the weight is greater than or equal to `400` but\n  is less than `700`, the rendered weight is `700`.\n* If the weight is greater than or equal to `700`, the rendered weight is\n  equal to the weight.\n* If the text is not bold, the rendered weight is equal to the weight."
              },
              "smallCaps" : "Whether or not the text is in small capital letters."
            },
            "suggestedInsertionIds" : [ "string" ]
          },
          "columnBreak" : {
            "suggestedTextStyleChanges" : "The suggested text style changes to this ColumnBreak, keyed by suggestion\nID.",
            "suggestedDeletionIds" : [ "string" ],
            "textStyle" : {
              "backgroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "underline" : "Whether or not the text is underlined.",
              "link" : {
                "bookmarkId" : "The ID of a bookmark in this document.",
                "headingId" : "The ID of a heading in this document.",
                "url" : "An external URL."
              },
              "fontSize" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              },
              "foregroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "bold" : "Whether or not the text is rendered as bold.",
              "strikethrough" : "Whether or not the text is struck through.",
              "baselineOffset" : "The text's vertical offset from its normal position.\n\nText with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically\nrendered in a smaller font size, computed based on the `font_size` field.\nThe `font_size` itself is not affected by changes in this field.",
              "italic" : "Whether or not the text is italicized.",
              "weightedFontFamily" : {
                "fontFamily" : "The font family of the text.\n\nThe font family can be any font from the Font menu in Docs or from\n[Google Fonts] (https://fonts.google.com/). If the font name is\nunrecognized, the text is rendered in `Arial`.",
                "weight" : "The weight of the font. This field can have any value that is a multiple of\n`100` between `100` and `900`, inclusive. This range corresponds to the\nnumerical values described in the CSS 2.1 Specification,\n[section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with\nnon-numerical values disallowed.\n\nThe default value is `400` (\"normal\").\n\nThe font weight makes up just one component of the rendered font weight.\nThe rendered weight is determined by a combination of the `weight` and the\ntext style's resolved `bold` value, after accounting for inheritance:\n\n* If the text is bold and the weight is less than `400`, the rendered\n  weight is 400.\n* If the text is bold and the weight is greater than or equal to `400` but\n  is less than `700`, the rendered weight is `700`.\n* If the weight is greater than or equal to `700`, the rendered weight is\n  equal to the weight.\n* If the text is not bold, the rendered weight is equal to the weight."
              },
              "smallCaps" : "Whether or not the text is in small capital letters."
            },
            "suggestedInsertionIds" : [ "string" ]
          },
          "autoText" : {
            "suggestedTextStyleChanges" : "The suggested text style changes to this AutoText, keyed by suggestion ID.",
            "suggestedDeletionIds" : [ "string" ],
            "textStyle" : {
              "backgroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "underline" : "Whether or not the text is underlined.",
              "link" : {
                "bookmarkId" : "The ID of a bookmark in this document.",
                "headingId" : "The ID of a heading in this document.",
                "url" : "An external URL."
              },
              "fontSize" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              },
              "foregroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "bold" : "Whether or not the text is rendered as bold.",
              "strikethrough" : "Whether or not the text is struck through.",
              "baselineOffset" : "The text's vertical offset from its normal position.\n\nText with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically\nrendered in a smaller font size, computed based on the `font_size` field.\nThe `font_size` itself is not affected by changes in this field.",
              "italic" : "Whether or not the text is italicized.",
              "weightedFontFamily" : {
                "fontFamily" : "The font family of the text.\n\nThe font family can be any font from the Font menu in Docs or from\n[Google Fonts] (https://fonts.google.com/). If the font name is\nunrecognized, the text is rendered in `Arial`.",
                "weight" : "The weight of the font. This field can have any value that is a multiple of\n`100` between `100` and `900`, inclusive. This range corresponds to the\nnumerical values described in the CSS 2.1 Specification,\n[section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with\nnon-numerical values disallowed.\n\nThe default value is `400` (\"normal\").\n\nThe font weight makes up just one component of the rendered font weight.\nThe rendered weight is determined by a combination of the `weight` and the\ntext style's resolved `bold` value, after accounting for inheritance:\n\n* If the text is bold and the weight is less than `400`, the rendered\n  weight is 400.\n* If the text is bold and the weight is greater than or equal to `400` but\n  is less than `700`, the rendered weight is `700`.\n* If the weight is greater than or equal to `700`, the rendered weight is\n  equal to the weight.\n* If the text is not bold, the rendered weight is equal to the weight."
              },
              "smallCaps" : "Whether or not the text is in small capital letters."
            },
            "type" : "The type of this auto text.",
            "suggestedInsertionIds" : [ "string" ]
          }
        } ],
        "positionedObjectIds" : [ "string" ],
        "bullet" : {
          "listId" : "The ID of the list this paragraph belongs to.",
          "nestingLevel" : "The nesting level of this paragraph in the list.",
          "textStyle" : {
            "backgroundColor" : {
              "color" : {
                "rgbColor" : {
                  "red" : "The red component of the color, from 0.0 to 1.0.",
                  "green" : "The green component of the color, from 0.0 to 1.0.",
                  "blue" : "The blue component of the color, from 0.0 to 1.0."
                }
              }
            },
            "underline" : "Whether or not the text is underlined.",
            "link" : {
              "bookmarkId" : "The ID of a bookmark in this document.",
              "headingId" : "The ID of a heading in this document.",
              "url" : "An external URL."
            },
            "fontSize" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            },
            "foregroundColor" : {
              "color" : {
                "rgbColor" : {
                  "red" : "The red component of the color, from 0.0 to 1.0.",
                  "green" : "The green component of the color, from 0.0 to 1.0.",
                  "blue" : "The blue component of the color, from 0.0 to 1.0."
                }
              }
            },
            "bold" : "Whether or not the text is rendered as bold.",
            "strikethrough" : "Whether or not the text is struck through.",
            "baselineOffset" : "The text's vertical offset from its normal position.\n\nText with `SUPERSCRIPT` or `SUBSCRIPT` baseline offsets is automatically\nrendered in a smaller font size, computed based on the `font_size` field.\nThe `font_size` itself is not affected by changes in this field.",
            "italic" : "Whether or not the text is italicized.",
            "weightedFontFamily" : {
              "fontFamily" : "The font family of the text.\n\nThe font family can be any font from the Font menu in Docs or from\n[Google Fonts] (https://fonts.google.com/). If the font name is\nunrecognized, the text is rendered in `Arial`.",
              "weight" : "The weight of the font. This field can have any value that is a multiple of\n`100` between `100` and `900`, inclusive. This range corresponds to the\nnumerical values described in the CSS 2.1 Specification,\n[section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with\nnon-numerical values disallowed.\n\nThe default value is `400` (\"normal\").\n\nThe font weight makes up just one component of the rendered font weight.\nThe rendered weight is determined by a combination of the `weight` and the\ntext style's resolved `bold` value, after accounting for inheritance:\n\n* If the text is bold and the weight is less than `400`, the rendered\n  weight is 400.\n* If the text is bold and the weight is greater than or equal to `400` but\n  is less than `700`, the rendered weight is `700`.\n* If the weight is greater than or equal to `700`, the rendered weight is\n  equal to the weight.\n* If the text is not bold, the rendered weight is equal to the weight."
            },
            "smallCaps" : "Whether or not the text is in small capital letters."
          }
        },
        "suggestedParagraphStyleChanges" : "The suggested paragraph style changes to this paragraph, keyed by\nsuggestion ID."
      },
      "startIndex" : "The zero-based start index of this structural element, in UTF-16 code\nunits.",
      "endIndex" : "The zero-based end index of this structural element, exclusive, in UTF-16\ncode units.",
      "sectionBreak" : {
        "sectionStyle" : {
          "columnSeparatorStyle" : "The style of column separators.\n\nThis style can be set even when there is one column in the section.",
          "contentDirection" : "The content direction of this section. If unset, the value defaults to\nLEFT_TO_RIGHT.",
          "columnProperties" : [ {
            "paddingEnd" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            },
            "width" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            }
          } ]
        },
        "suggestedDeletionIds" : [ "string" ],
        "suggestedInsertionIds" : [ "string" ]
      },
      "tableOfContents" : {
        "suggestedDeletionIds" : [ "string" ],
        "content" : [ { } ],
        "suggestedInsertionIds" : [ "string" ]
      },
      "table" : {
        "columns" : "Number of columns in the table.\n\nIt is possible for a table to be non-rectangular, so some rows may have a\ndifferent number of cells.",
        "x" : [ "string" ],
        "tableStyle" : {
          "tableColumnProperties" : [ {
            "width" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            },
            "widthType" : "The width type of the column."
          } ]
        },
        "suggestedDeletionIds" : [ "string" ],
        "rows" : "Number of rows in the table.",
        "tableRows" : [ {
          "tableCells" : [ {
            "startIndex" : "The zero-based start index of this cell, in UTF-16 code units.",
            "suggestedTableCellStyleChanges" : "The suggested changes to the table cell style, keyed by suggestion ID.",
            "endIndex" : "The zero-based end index of this cell, exclusive, in UTF-16 code units.",
            "suggestedDeletionIds" : [ "string" ],
            "content" : [ { } ],
            "suggestedInsertionIds" : [ "string" ],
            "tableCellStyle" : {
              "columnSpan" : "The column span of the cell. This property is read-only.",
              "rowSpan" : "The row span of the cell. This property is read-only.",
              "borderLeft" : {
                "color" : {
                  "color" : {
                    "rgbColor" : {
                      "red" : "The red component of the color, from 0.0 to 1.0.",
                      "green" : "The green component of the color, from 0.0 to 1.0.",
                      "blue" : "The blue component of the color, from 0.0 to 1.0."
                    }
                  }
                },
                "dashStyle" : "The dash style of the border.",
                "width" : {
                  "unit" : "The units for magnitude.",
                  "magnitude" : "The magnitude."
                }
              },
              "contentAlignment" : "The alignment of the content in the table cell. The default alignment\nmatches the alignment for newly created table cells in the Docs editor.",
              "backgroundColor" : {
                "color" : {
                  "rgbColor" : {
                    "red" : "The red component of the color, from 0.0 to 1.0.",
                    "green" : "The green component of the color, from 0.0 to 1.0.",
                    "blue" : "The blue component of the color, from 0.0 to 1.0."
                  }
                }
              },
              "paddingBottom" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              },
              "borderRight" : {
                "color" : {
                  "color" : {
                    "rgbColor" : {
                      "red" : "The red component of the color, from 0.0 to 1.0.",
                      "green" : "The green component of the color, from 0.0 to 1.0.",
                      "blue" : "The blue component of the color, from 0.0 to 1.0."
                    }
                  }
                },
                "dashStyle" : "The dash style of the border.",
                "width" : {
                  "unit" : "The units for magnitude.",
                  "magnitude" : "The magnitude."
                }
              },
              "paddingRight" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              },
              "paddingTop" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              },
              "borderBottom" : {
                "color" : {
                  "color" : {
                    "rgbColor" : {
                      "red" : "The red component of the color, from 0.0 to 1.0.",
                      "green" : "The green component of the color, from 0.0 to 1.0.",
                      "blue" : "The blue component of the color, from 0.0 to 1.0."
                    }
                  }
                },
                "dashStyle" : "The dash style of the border.",
                "width" : {
                  "unit" : "The units for magnitude.",
                  "magnitude" : "The magnitude."
                }
              },
              "borderTop" : {
                "color" : {
                  "color" : {
                    "rgbColor" : {
                      "red" : "The red component of the color, from 0.0 to 1.0.",
                      "green" : "The green component of the color, from 0.0 to 1.0.",
                      "blue" : "The blue component of the color, from 0.0 to 1.0."
                    }
                  }
                },
                "dashStyle" : "The dash style of the border.",
                "width" : {
                  "unit" : "The units for magnitude.",
                  "magnitude" : "The magnitude."
                }
              },
              "paddingLeft" : {
                "unit" : "The units for magnitude.",
                "magnitude" : "The magnitude."
              }
            }
          } ],
          "startIndex" : "The zero-based start index of this row, in UTF-16 code units.",
          "suggestedTableRowStyleChanges" : "The suggested style changes to this row, keyed by suggestion ID.",
          "endIndex" : "The zero-based end index of this row, exclusive, in UTF-16 code units.",
          "tableRowStyle" : {
            "minRowHeight" : {
              "unit" : "The units for magnitude.",
              "magnitude" : "The magnitude."
            }
          },
          "suggestedDeletionIds" : [ "string" ],
          "suggestedInsertionIds" : [ "string" ]
        } ]
      }
    } ]
  },
  "title" : "The title of the document.",
  "documentStyle" : {
    "evenPageHeaderId" : "The ID of the header used only for even pages. The value of\nuse_even_page_header_footer determines\nwhether to use the default_header_id or this value for the\nheader on even pages. If not set, there is no even page header.",
    "firstPageFooterId" : "The ID of the footer used only for the first page. If not set then\na unique footer for the first page does not exist. The value of\nuse_first_page_header_footer determines\nwhether to use the default_footer_id or this value for the\nfooter on the first page. If not set, there is no first page footer.",
    "evenPageFooterId" : "The ID of the footer used only for even pages. The value of\nuse_even_page_header_footer determines\nwhether to use the default_footer_id or this value for the\nfooter on even pages. If not set, there is no even page footer.",
    "pageSize" : {
      "width" : {
        "unit" : "The units for magnitude.",
        "magnitude" : "The magnitude."
      },
      "height" : {
        "unit" : "The units for magnitude.",
        "magnitude" : "The magnitude."
      }
    },
    "useEvenPageHeaderFooter" : "Indicates whether to use the even page header / footer IDs for the even\npages.",
    "marginLeft" : {
      "unit" : "The units for magnitude.",
      "magnitude" : "The magnitude."
    },
    "marginRight" : {
      "unit" : "The units for magnitude.",
      "magnitude" : "The magnitude."
    },
    "background" : {
      "color" : {
        "color" : {
          "rgbColor" : {
            "red" : "The red component of the color, from 0.0 to 1.0.",
            "green" : "The green component of the color, from 0.0 to 1.0.",
            "blue" : "The blue component of the color, from 0.0 to 1.0."
          }
        }
      }
    },
    "defaultFooterId" : "The ID of the default footer. If not set, there is no default footer.",
    "defaultHeaderId" : "The ID of the default header. If not set, there is no default header.",
    "firstPageHeaderId" : "The ID of the header used only for the first page. If not set then\na unique header for the first page does not exist.\nThe value of use_first_page_header_footer determines\nwhether to use the default_header_id or this value for the\nheader on the first page. If not set, there is no first page header.",
    "marginBottom" : {
      "unit" : "The units for magnitude.",
      "magnitude" : "The magnitude."
    },
    "pageNumberStart" : "The page number from which to start counting the number of pages.",
    "useFirstPageHeaderFooter" : "Indicates whether to use the first page header / footer IDs for the first\npage.",
    "marginTop" : {
      "unit" : "The units for magnitude.",
      "magnitude" : "The magnitude."
    }
  },
  "footers" : "The footers in the document, keyed by footer ID.",
  "revisionId" : "The revision ID of the document. Can be used in update requests to specify\nwhich revision of a document to apply updates to and how the request should\nbehave if the document has been edited since that revision. Only populated\nif the user has edit access to the document.\n\nThe format of the revision ID may change over time, so it should be treated\nopaquely. A returned revision ID is only guaranteed to be valid for 24\nhours after it has been returned and cannot be shared across users. If the\nrevision ID is unchanged between calls, then the document has not changed.\nConversely, a changed ID (for the same document and user) usually means the\ndocument has been updated; however, a changed ID can also be due to\ninternal factors such as ID format changes.",
  "suggestedDocumentStyleChanges" : "The suggested changes to the style of the document, keyed by suggestion ID.",
  "lists" : "The lists in the document, keyed by list ID.",
  "namedRanges" : "The named ranges in the document, keyed by name.",
  "suggestionsViewMode" : "The suggestions view mode applied to the document.\n\nNote: When editing a document, changes must be based on a document with\nSUGGESTIONS_INLINE.",
  "documentId" : "The ID of the document.",
  "footnotes" : "The footnotes in the document, keyed by footnote ID."
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

## get_document

Gets the latest version of the specified document.

<details><summary>Parameters</summary>

### documentId (required)

The ID of the document to retrieve.

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

### suggestionsViewMode

The suggestions view mode to apply to the document. This allows viewing the document with all suggestions inline, accepted or rejected. If one is not specified, DEFAULT_FOR_CURRENT_ACCESS is used.

**Type:** string

**Potential values:** DEFAULT_FOR_CURRENT_ACCESS, SUGGESTIONS_INLINE, PREVIEW_SUGGESTIONS_ACCEPTED, PREVIEW_WITHOUT_SUGGESTIONS

### uploadType

Legacy upload protocol for media (e.g. "media", "multipart").

**Type:** string

### upload_protocol

Upload protocol for media (e.g. "raw", "multipart").

**Type:** string

</details>

