---
id: gcp-bigquery-documentation
title: GCP BigQuery (version v1.*.*)
sidebar_label: GCP BigQuery
layout: docs.mustache
---

## cancel_job

Requests that a job be cancelled. This call will return immediately, and the client will need to poll for the job status to see if the cancel completed successfully. Cancelled jobs may still incur costs.

<details><summary>Parameters</summary>

### jobId (required)

[Required] Job ID of the job to cancel

**Type:** string

### projectId (required)

[Required] Project ID of the job to cancel

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### location

The geographic location of the job. Required except for US and EU. See details at https://cloud.google.com/bigquery/docs/locations#specifying_your_location.

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

## create_dataset

Creates a new empty dataset.

<details><summary>Parameters</summary>

### projectId (required)

Project ID of the new dataset

**Type:** string

### $body

**Type:** object

```json
{
  "access" : [ {
    "view" : {
      "datasetId" : "[Required] The ID of the dataset containing this table.",
      "tableId" : "[Required] The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.",
      "projectId" : "[Required] The ID of the project containing this table."
    },
    "role" : "[Required] An IAM role ID that should be granted to the user, group, or domain specified in this access entry. The following legacy mappings will be applied: OWNER roles/bigquery.dataOwner WRITER roles/bigquery.dataEditor READER roles/bigquery.dataViewer This field will accept any of the above formats, but will return only the legacy format. For example, if you set this field to \"roles/bigquery.dataOwner\", it will be returned back as \"OWNER\".",
    "userByEmail" : "[Pick one] An email address of a user to grant access to. For example: fred@example.com. Maps to IAM policy member \"user:EMAIL\" or \"serviceAccount:EMAIL\".",
    "domain" : "[Pick one] A domain to grant access to. Any users signed in with the domain specified will be granted the specified access. Example: \"example.com\". Maps to IAM policy member \"domain:DOMAIN\".",
    "specialGroup" : "[Pick one] A special group to grant access to. Possible values include: projectOwners: Owners of the enclosing project. projectReaders: Readers of the enclosing project. projectWriters: Writers of the enclosing project. allAuthenticatedUsers: All authenticated BigQuery users. Maps to similarly-named IAM members.",
    "iamMember" : "[Pick one] Some other type of member that appears in the IAM Policy but isn't a user, group, domain, or special group.",
    "groupByEmail" : "[Pick one] An email address of a Google Group to grant access to. Maps to IAM policy member \"group:GROUP\"."
  } ],
  "lastModifiedTime" : "[Output-only] The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.",
  "creationTime" : "[Output-only] The time when this dataset was created, in milliseconds since the epoch.",
  "kind" : "[Output-only] The resource type.",
  "description" : "[Optional] A user-friendly description of the dataset.",
  "datasetReference" : {
    "datasetId" : "[Required] A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.",
    "projectId" : "[Optional] The ID of the project containing this dataset."
  },
  "labels" : "The labels associated with this dataset. You can use these to organize and group your datasets. You can set this property when inserting or updating a dataset. See Creating and Updating Dataset Labels for more information.",
  "selfLink" : "[Output-only] A URL that can be used to access the resource again. You can use this URL in Get or Update requests to the resource.",
  "defaultPartitionExpirationMs" : "[Optional] The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set, all newly-created partitioned tables in the dataset will have an expirationMs property in the timePartitioning settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of defaultTableExpirationMs for partitioned tables: only one of defaultTableExpirationMs and defaultPartitionExpirationMs will be used for any new partitioned table. If you provide an explicit timePartitioning.expirationMs when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property.",
  "etag" : "[Output-only] A hash of the resource.",
  "location" : "The geographic location where the dataset should reside. The default value is US. See details at https://cloud.google.com/bigquery/docs/locations.",
  "defaultTableExpirationMs" : "[Optional] The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). Once this property is set, all newly-created tables in the dataset will have an expirationTime property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the expirationTime for a given table is reached, that table will be deleted automatically. If a table's expirationTime is modified or removed before the table expires, or if you provide an explicit expirationTime when creating a table, that value takes precedence over the default expiration time indicated by this property.",
  "id" : "[Output-only] The fully-qualified unique name of the dataset in the format projectId:datasetId. The dataset name without the project name is given in the datasetId field. When creating a new dataset, leave this field blank, and instead specify the datasetId field.",
  "friendlyName" : "[Optional] A descriptive name for the dataset."
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

## create_table

Creates a new, empty table in the dataset.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the new table

**Type:** string

### projectId (required)

Project ID of the new table

**Type:** string

### $body

**Type:** object

```json
{
  "schema" : {
    "fields" : [ {
      "mode" : "[Optional] The field mode. Possible values include NULLABLE, REQUIRED and REPEATED. The default value is NULLABLE.",
      "name" : "[Required] The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters.",
      "description" : "[Optional] The field description. The maximum length is 1,024 characters.",
      "categories" : {
        "names" : [ "string" ]
      },
      "fields" : [ { } ],
      "type" : "[Required] The field data type. Possible values include STRING, BYTES, INTEGER, INT64 (same as INTEGER), FLOAT, FLOAT64 (same as FLOAT), BOOLEAN, BOOL (same as BOOLEAN), TIMESTAMP, DATE, TIME, DATETIME, RECORD (where RECORD indicates that the field contains a nested schema) or STRUCT (same as RECORD)."
    } ]
  },
  "lastModifiedTime" : "[Output-only] The time when this table was last modified, in milliseconds since the epoch.",
  "creationTime" : "[Output-only] The time when this table was created, in milliseconds since the epoch.",
  "numRows" : "[Output-only] The number of rows of data in this table, excluding any data in the streaming buffer.",
  "description" : "[Optional] A user-friendly description of this table.",
  "requirePartitionFilter" : "[Beta] [Optional] If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.",
  "type" : "[Output-only] Describes the table type. The following values are supported: TABLE: A normal BigQuery table. VIEW: A virtual table defined by a SQL query. [TrustedTester] MATERIALIZED_VIEW: SQL query whose result is persisted. EXTERNAL: A table that references data stored in an external storage system, such as Google Cloud Storage. The default value is TABLE.",
  "numBytes" : "[Output-only] The size of this table in bytes, excluding any data in the streaming buffer.",
  "externalDataConfiguration" : {
    "schema" : {
      "fields" : [ {
        "mode" : "[Optional] The field mode. Possible values include NULLABLE, REQUIRED and REPEATED. The default value is NULLABLE.",
        "name" : "[Required] The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters.",
        "description" : "[Optional] The field description. The maximum length is 1,024 characters.",
        "categories" : {
          "names" : [ "string" ]
        },
        "fields" : [ { } ],
        "type" : "[Required] The field data type. Possible values include STRING, BYTES, INTEGER, INT64 (same as INTEGER), FLOAT, FLOAT64 (same as FLOAT), BOOLEAN, BOOL (same as BOOLEAN), TIMESTAMP, DATE, TIME, DATETIME, RECORD (where RECORD indicates that the field contains a nested schema) or STRUCT (same as RECORD)."
      } ]
    },
    "autodetect" : "Try to detect schema and format options automatically. Any option specified explicitly will be honored.",
    "sourceUris" : [ "string" ],
    "bigtableOptions" : {
      "columnFamilies" : [ {
        "familyId" : "Identifier of the column family.",
        "columns" : [ {
          "qualifierEncoded" : "[Required] Qualifier of the column. Columns in the parent column family that has this exact qualifier are exposed as . field. If the qualifier is valid UTF-8 string, it can be specified in the qualifier_string field. Otherwise, a base-64 encoded value must be set to qualifier_encoded. The column field name is the same as the column qualifier. However, if the qualifier is not a valid BigQuery field identifier i.e. does not match [a-zA-Z][a-zA-Z0-9_]*, a valid identifier must be provided as field_name.",
          "fieldName" : "[Optional] If the qualifier is not a valid BigQuery field identifier i.e. does not match [a-zA-Z][a-zA-Z0-9_]*, a valid identifier must be provided as the column field name and is used as field name in queries.",
          "encoding" : "[Optional] The encoding of the values when the type is not STRING. Acceptable encoding values are: TEXT - indicates values are alphanumeric text strings. BINARY - indicates values are encoded using HBase Bytes.toBytes family of functions. 'encoding' can also be set at the column family level. However, the setting at this level takes precedence if 'encoding' is set at both levels.",
          "qualifierString" : "string",
          "type" : "[Optional] The type to convert the value in cells of this column. The values are expected to be encoded using HBase Bytes.toBytes function when using the BINARY encoding value. Following BigQuery types are allowed (case-sensitive) - BYTES STRING INTEGER FLOAT BOOLEAN Default type is BYTES. 'type' can also be set at the column family level. However, the setting at this level takes precedence if 'type' is set at both levels.",
          "onlyReadLatest" : "[Optional] If this is set, only the latest version of value in this column are exposed. 'onlyReadLatest' can also be set at the column family level. However, the setting at this level takes precedence if 'onlyReadLatest' is set at both levels."
        } ],
        "encoding" : "[Optional] The encoding of the values when the type is not STRING. Acceptable encoding values are: TEXT - indicates values are alphanumeric text strings. BINARY - indicates values are encoded using HBase Bytes.toBytes family of functions. This can be overridden for a specific column by listing that column in 'columns' and specifying an encoding for it.",
        "type" : "[Optional] The type to convert the value in cells of this column family. The values are expected to be encoded using HBase Bytes.toBytes function when using the BINARY encoding value. Following BigQuery types are allowed (case-sensitive) - BYTES STRING INTEGER FLOAT BOOLEAN Default type is BYTES. This can be overridden for a specific column by listing that column in 'columns' and specifying a type for it.",
        "onlyReadLatest" : "[Optional] If this is set only the latest version of value are exposed for all columns in this column family. This can be overridden for a specific column by listing that column in 'columns' and specifying a different setting for that column."
      } ],
      "ignoreUnspecifiedColumnFamilies" : "[Optional] If field is true, then the column families that are not specified in columnFamilies list are not exposed in the table schema. Otherwise, they are read with BYTES type values. The default value is false.",
      "readRowkeyAsString" : "[Optional] If field is true, then the rowkey column families will be read and converted to string. Otherwise they are read with BYTES type values and users need to manually cast them with CAST if necessary. The default value is false."
    },
    "csvOptions" : {
      "allowQuotedNewlines" : "[Optional] Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file. The default value is false.",
      "skipLeadingRows" : "[Optional] The number of rows at the top of a CSV file that BigQuery will skip when reading the data. The default value is 0. This property is useful if you have header rows in the file that should be skipped.",
      "quote" : "[Optional] The value that is used to quote data sections in a CSV file. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. The default value is a double-quote ('\"'). If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allowQuotedNewlines property to true.",
      "encoding" : "[Optional] The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. The default value is UTF-8. BigQuery decodes the data after the raw, binary data has been split using the values of the quote and fieldDelimiter properties.",
      "fieldDelimiter" : "[Optional] The separator for fields in a CSV file. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. BigQuery also supports the escape sequence \"\\t\" to specify a tab separator. The default value is a comma (',').",
      "allowJaggedRows" : "[Optional] Indicates if BigQuery should accept rows that are missing trailing optional columns. If true, BigQuery treats missing trailing columns as null values. If false, records with missing trailing columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false."
    },
    "hivePartitioningMode" : "[Optional, Experimental] If hive partitioning is enabled, which mode to use. Two modes are supported: - AUTO: automatically infer partition key name(s) and type(s). - STRINGS: automatic infer partition key name(s). All types are strings. Not all storage formats support hive partitioning -- requesting hive partitioning on an unsupported format will lead to an error.",
    "ignoreUnknownValues" : "[Optional] Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. The sourceFormat property determines what BigQuery treats as an extra value: CSV: Trailing columns JSON: Named values that don't match any column names Google Cloud Bigtable: This setting is ignored. Google Cloud Datastore backups: This setting is ignored. Avro: This setting is ignored.",
    "googleSheetsOptions" : {
      "skipLeadingRows" : "[Optional] The number of rows at the top of a sheet that BigQuery will skip when reading the data. The default value is 0. This property is useful if you have header rows that should be skipped. When autodetect is on, behavior is the following: * skipLeadingRows unspecified - Autodetect tries to detect headers in the first row. If they are not detected, the row is read as data. Otherwise data is read starting from the second row. * skipLeadingRows is 0 - Instructs autodetect that there are no headers and data should be read starting from the first row. * skipLeadingRows = N &gt; 0 - Autodetect skips N-1 rows and tries to detect headers in row N. If headers are not detected, row N is just skipped. Otherwise row N is used to extract column names for the detected schema.",
      "range" : "[Beta] [Optional] Range of a sheet to query from. Only used when non-empty. Typical format: sheet_name!top_left_cell_id:bottom_right_cell_id For example: sheet1!A1:B20"
    },
    "compression" : "[Optional] The compression type of the data source. Possible values include GZIP and NONE. The default value is NONE. This setting is ignored for Google Cloud Bigtable, Google Cloud Datastore backups and Avro formats.",
    "sourceFormat" : "[Required] The data format. For CSV files, specify \"CSV\". For Google sheets, specify \"GOOGLE_SHEETS\". For newline-delimited JSON, specify \"NEWLINE_DELIMITED_JSON\". For Avro files, specify \"AVRO\". For Google Cloud Datastore backups, specify \"DATASTORE_BACKUP\". [Beta] For Google Cloud Bigtable, specify \"BIGTABLE\".",
    "maxBadRecords" : "[Optional] The maximum number of bad records that BigQuery can ignore when reading data. If the number of bad records exceeds this value, an invalid error is returned in the job result. This is only valid for CSV, JSON, and Google Sheets. The default value is 0, which requires that all records are valid. This setting is ignored for Google Cloud Bigtable, Google Cloud Datastore backups and Avro formats."
  },
  "view" : {
    "userDefinedFunctionResources" : [ {
      "resourceUri" : "[Pick one] A code resource to load from a Google Cloud Storage URI (gs://bucket/path).",
      "inlineCode" : "[Pick one] An inline resource that contains code for a user-defined function (UDF). Providing a inline code resource is equivalent to providing a URI for a file containing the same code."
    } ],
    "query" : "[Required] A query that BigQuery executes when the view is referenced.",
    "useLegacySql" : "Specifies whether to use BigQuery's legacy SQL for this view. The default value is true. If set to false, the view will use BigQuery's standard SQL: https://cloud.google.com/bigquery/sql-reference/ Queries and views that reference this view must use the same flag value."
  },
  "numLongTermBytes" : "[Output-only] The number of bytes in the table that are considered \"long-term storage\".",
  "encryptionConfiguration" : {
    "kmsKeyName" : "[Optional] Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key."
  },
  "model" : {
    "trainingRuns" : [ {
      "trainingOptions" : {
        "earlyStop" : "boolean",
        "l1Reg" : "number",
        "maxIteration" : "int64",
        "l2Reg" : "number",
        "learnRate" : "number",
        "lineSearchInitLearnRate" : "number",
        "warmStart" : "boolean",
        "learnRateStrategy" : "string",
        "minRelProgress" : "number"
      },
      "iterationResults" : [ {
        "index" : "[Output-only, Beta] Index of the ML training iteration, starting from zero for each training run.",
        "learnRate" : "[Output-only, Beta] Learning rate used for this iteration, it varies for different training iterations if learn_rate_strategy option is not constant.",
        "durationMs" : "[Output-only, Beta] Time taken to run the training iteration in milliseconds.",
        "evalLoss" : "[Output-only, Beta] Eval loss computed on the eval data at the end of the iteration. The eval loss is used for early stopping to avoid overfitting. No eval loss if eval_split_method option is specified as no_split or auto_split with input data size less than 500 rows.",
        "trainingLoss" : "[Output-only, Beta] Training loss computed on the training data at the end of the iteration. The training loss function is defined by model type."
      } ],
      "startTime" : "[Output-only, Beta] Training run start time in milliseconds since the epoch.",
      "state" : "[Output-only, Beta] Different state applicable for a training run. IN PROGRESS: Training run is in progress. FAILED: Training run ended due to a non-retryable failure. SUCCEEDED: Training run successfully completed. CANCELLED: Training run cancelled by the user."
    } ],
    "modelOptions" : {
      "lossType" : "string",
      "modelType" : "string",
      "labels" : [ "string" ]
    }
  },
  "id" : "[Output-only] An opaque ID uniquely identifying the table.",
  "friendlyName" : "[Optional] A descriptive name for this table.",
  "materializedView" : {
    "query" : "[Required] A query whose result is persisted.",
    "lastRefreshTime" : "[Output-only] [TrustedTester] The time when this materialized view was last modified, in milliseconds since the epoch."
  },
  "timePartitioning" : {
    "field" : "[Beta] [Optional] If not set, the table is partitioned by pseudo column, referenced via either '_PARTITIONTIME' as TIMESTAMP type, or '_PARTITIONDATE' as DATE type. If field is specified, the table is instead partitioned by this field. The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED.",
    "expirationMs" : "[Optional] Number of milliseconds for which to keep the storage for partitions in the table. The storage in a partition will have an expiration time of its partition time plus this value.",
    "requirePartitionFilter" : "boolean",
    "type" : "[Required] The only type supported is DAY, which will generate one partition per day."
  },
  "streamingBuffer" : {
    "estimatedBytes" : "[Output-only] A lower-bound estimate of the number of bytes currently in the streaming buffer.",
    "oldestEntryTime" : "[Output-only] Contains the timestamp of the oldest entry in the streaming buffer, in milliseconds since the epoch, if the streaming buffer is available.",
    "estimatedRows" : "[Output-only] A lower-bound estimate of the number of rows currently in the streaming buffer."
  },
  "kind" : "[Output-only] The type of the resource.",
  "labels" : "The labels associated with this table. You can use these to organize and group your tables. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key.",
  "selfLink" : "[Output-only] A URL that can be used to access this resource again.",
  "numPhysicalBytes" : "[Output-only] [TrustedTester] The physical size of this table in bytes, excluding any data in the streaming buffer. This includes compression and storage used for time travel.",
  "tableReference" : {
    "datasetId" : "[Required] The ID of the dataset containing this table.",
    "tableId" : "[Required] The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.",
    "projectId" : "[Required] The ID of the project containing this table."
  },
  "expirationTime" : "[Optional] The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. The defaultTableExpirationMs property of the encapsulating dataset can be used to set a default expirationTime on newly created tables.",
  "rangePartitioning" : {
    "field" : "[TrustedTester] [Required] The table is partitioned by this field. The field must be a top-level NULLABLE/REQUIRED field. The only supported type is INTEGER/INT64.",
    "range" : {
      "start" : "[TrustedTester] [Required] The start of range partitioning, inclusive.",
      "end" : "[TrustedTester] [Required] The end of range partitioning, exclusive.",
      "interval" : "[TrustedTester] [Required] The width of each interval."
    }
  },
  "clustering" : {
    "fields" : [ "string" ]
  },
  "etag" : "[Output-only] A hash of the table metadata. Used to ensure there were no concurrent modifications to the resource when attempting an update. Not guaranteed to change when the table contents or the fields numRows, numBytes, numLongTermBytes or lastModifiedTime change.",
  "location" : "[Output-only] The geographic location where the table resides. This value is inherited from the dataset."
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

## delete_dataset

Deletes the dataset specified by the datasetId value. Before you can delete a dataset, you must delete all its tables, either manually or by specifying deleteContents. Immediately after deletion, you can create another dataset with the same name.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of dataset being deleted

**Type:** string

### projectId (required)

Project ID of the dataset being deleted

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### deleteContents

If True, delete all the tables in the dataset. If False and the dataset contains tables, the request will fail. Default is False

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

## delete_table

Deletes the table specified by tableId from the dataset. If the table contains data, all the data will be deleted.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the table to delete

**Type:** string

### projectId (required)

Project ID of the table to delete

**Type:** string

### tableId (required)

Table ID of the table to delete

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

## execute_query

Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout.

<details><summary>Parameters</summary>

### projectId (required)

Project ID of the project billed for the query

**Type:** string

### $body

**Type:** object

```json
{
  "dryRun" : "[Optional] If set to true, BigQuery doesn't run the job. Instead, if the query is valid, BigQuery returns statistics about the job such as how many bytes would be processed. If the query is invalid, an error returns. The default value is false.",
  "parameterMode" : "Standard SQL only. Set to POSITIONAL to use positional (?) query parameters or to NAMED to use named (@myparam) query parameters in this query.",
  "useQueryCache" : "[Optional] Whether to look for the result in the query cache. The query cache is a best-effort cache that will be flushed whenever tables in the query are modified. The default value is true.",
  "queryParameters" : [ {
    "parameterType" : {
      "arrayType" : "[Optional] The type of the array's elements, if this is an array.",
      "type" : "[Required] The top level type of this field.",
      "structTypes" : [ {
        "name" : "[Optional] The name of this field.",
        "description" : "[Optional] Human-oriented description of the field.",
        "type" : "[Required] The type of this field."
      } ]
    },
    "name" : "[Optional] If unset, this is a positional parameter. Otherwise, should be unique within a query.",
    "parameterValue" : {
      "structValues" : "[Optional] The struct field values, in order of the struct type's declaration.",
      "value" : "[Optional] The value of this value, if a simple scalar type.",
      "arrayValues" : [ { } ]
    }
  } ],
  "kind" : "The resource type of the request.",
  "maxResults" : "[Optional] The maximum number of rows of data to return per page of results. Setting this flag to a small value such as 1000 and then paging through results might improve reliability when the query result set is large. In addition to this limit, responses are also limited to 10 MB. By default, there is no maximum row count, and only the byte limit applies.",
  "timeoutMs" : "[Optional] How long to wait for the query to complete, in milliseconds, before the request times out and returns. Note that this is only a timeout for the request, not the query. If the query takes longer to run than the timeout value, the call returns without any results and with the 'jobComplete' flag set to false. You can call GetQueryResults() to wait for the query to complete and read the results. The default value is 10000 milliseconds (10 seconds).",
  "preserveNulls" : "[Deprecated] This property is deprecated.",
  "query" : "[Required] A query string, following the BigQuery query syntax, of the query to execute. Example: \"SELECT count(f1) FROM [myProjectId:myDatasetId.myTableId]\".",
  "location" : "The geographic location where the job should run. See details at https://cloud.google.com/bigquery/docs/locations#specifying_your_location.",
  "defaultDataset" : {
    "datasetId" : "[Required] A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.",
    "projectId" : "[Optional] The ID of the project containing this dataset."
  },
  "useLegacySql" : "Specifies whether to use BigQuery's legacy SQL dialect for this query. The default value is true. If set to false, the query will use BigQuery's standard SQL: https://cloud.google.com/bigquery/sql-reference/ When useLegacySql is set to false, the value of flattenResults is ignored; query will be run as if flattenResults is false."
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

## get_dataset

Returns the dataset specified by datasetID.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the requested dataset

**Type:** string

### projectId (required)

Project ID of the requested dataset

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

## get_job

Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role.

<details><summary>Parameters</summary>

### jobId (required)

[Required] Job ID of the requested job

**Type:** string

### projectId (required)

[Required] Project ID of the requested job

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### location

The geographic location of the job. Required except for US and EU. See details at https://cloud.google.com/bigquery/docs/locations#specifying_your_location.

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

## get_query_results

Retrieves the results of a query job.

<details><summary>Parameters</summary>

### jobId (required)

[Required] Job ID of the query job

**Type:** string

### projectId (required)

[Required] Project ID of the query job

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### location

The geographic location where the job should run. Required except for US and EU. See details at https://cloud.google.com/bigquery/docs/locations#specifying_your_location.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### startIndex

Zero-based index of the starting row

**Type:** string

### timeoutMs

How long to wait for the query to complete, in milliseconds, before returning. Default is 10 seconds. If the timeout passes before the job completes, the 'jobComplete' field in the response will be false

**Type:** integer

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## get_service_account

Returns the email address of the service account for your project used for interactions with Google Cloud KMS.

<details><summary>Parameters</summary>

### projectId (required)

Project ID for which the service account is requested.

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

## get_table

Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the requested table

**Type:** string

### projectId (required)

Project ID of the requested table

**Type:** string

### tableId (required)

Table ID of the requested table

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

### selectedFields

List of fields to return (comma-separated). If unspecified, all fields are returned

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_datasets

Lists all datasets in the specified project to which you have been granted the READER dataset role.

<details><summary>Parameters</summary>

### projectId (required)

Project ID of the datasets to be listed

**Type:** string

### all

Whether to list all datasets, including hidden ones

**Type:** boolean

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### filter

An expression for filtering the results of the request by label. The syntax is "labels.[:]". Multiple filters can be ANDed together by connecting with a space. Example: "labels.department:receiving labels.active". See Filtering datasets using labels for details.

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

## list_jobs

Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property.

<details><summary>Parameters</summary>

### projectId (required)

Project ID of the jobs to list

**Type:** string

### allUsers

Whether to display jobs owned by all users in the project. Default false

**Type:** boolean

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### maxCreationTime

Max value for job creation time, in milliseconds since the POSIX epoch. If set, only jobs created before or at this timestamp are returned

**Type:** string

### minCreationTime

Min value for job creation time, in milliseconds since the POSIX epoch. If set, only jobs created after or at this timestamp are returned

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### projection

Restrict information returned to a set of selected fields

**Type:** string

**Potential values:** full, minimal

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### stateFilter

Filter for job state

**Type:** array

```json
[ "string. Possible values: done | pending | running" ]
```

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## list_projects

Lists all projects to which you have been granted any project role.

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

## list_tables

Lists all tables in the specified dataset. Requires the READER dataset role.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the tables to list

**Type:** string

### projectId (required)

Project ID of the tables to list

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

## patch_dataset

Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource. This method supports patch semantics.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the dataset being updated

**Type:** string

### projectId (required)

Project ID of the dataset being updated

**Type:** string

### $body

**Type:** object

```json
{
  "access" : [ {
    "view" : {
      "datasetId" : "[Required] The ID of the dataset containing this table.",
      "tableId" : "[Required] The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.",
      "projectId" : "[Required] The ID of the project containing this table."
    },
    "role" : "[Required] An IAM role ID that should be granted to the user, group, or domain specified in this access entry. The following legacy mappings will be applied: OWNER roles/bigquery.dataOwner WRITER roles/bigquery.dataEditor READER roles/bigquery.dataViewer This field will accept any of the above formats, but will return only the legacy format. For example, if you set this field to \"roles/bigquery.dataOwner\", it will be returned back as \"OWNER\".",
    "userByEmail" : "[Pick one] An email address of a user to grant access to. For example: fred@example.com. Maps to IAM policy member \"user:EMAIL\" or \"serviceAccount:EMAIL\".",
    "domain" : "[Pick one] A domain to grant access to. Any users signed in with the domain specified will be granted the specified access. Example: \"example.com\". Maps to IAM policy member \"domain:DOMAIN\".",
    "specialGroup" : "[Pick one] A special group to grant access to. Possible values include: projectOwners: Owners of the enclosing project. projectReaders: Readers of the enclosing project. projectWriters: Writers of the enclosing project. allAuthenticatedUsers: All authenticated BigQuery users. Maps to similarly-named IAM members.",
    "iamMember" : "[Pick one] Some other type of member that appears in the IAM Policy but isn't a user, group, domain, or special group.",
    "groupByEmail" : "[Pick one] An email address of a Google Group to grant access to. Maps to IAM policy member \"group:GROUP\"."
  } ],
  "lastModifiedTime" : "[Output-only] The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.",
  "creationTime" : "[Output-only] The time when this dataset was created, in milliseconds since the epoch.",
  "kind" : "[Output-only] The resource type.",
  "description" : "[Optional] A user-friendly description of the dataset.",
  "datasetReference" : {
    "datasetId" : "[Required] A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.",
    "projectId" : "[Optional] The ID of the project containing this dataset."
  },
  "labels" : "The labels associated with this dataset. You can use these to organize and group your datasets. You can set this property when inserting or updating a dataset. See Creating and Updating Dataset Labels for more information.",
  "selfLink" : "[Output-only] A URL that can be used to access the resource again. You can use this URL in Get or Update requests to the resource.",
  "defaultPartitionExpirationMs" : "[Optional] The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set, all newly-created partitioned tables in the dataset will have an expirationMs property in the timePartitioning settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of defaultTableExpirationMs for partitioned tables: only one of defaultTableExpirationMs and defaultPartitionExpirationMs will be used for any new partitioned table. If you provide an explicit timePartitioning.expirationMs when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property.",
  "etag" : "[Output-only] A hash of the resource.",
  "location" : "The geographic location where the dataset should reside. The default value is US. See details at https://cloud.google.com/bigquery/docs/locations.",
  "defaultTableExpirationMs" : "[Optional] The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). Once this property is set, all newly-created tables in the dataset will have an expirationTime property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the expirationTime for a given table is reached, that table will be deleted automatically. If a table's expirationTime is modified or removed before the table expires, or if you provide an explicit expirationTime when creating a table, that value takes precedence over the default expiration time indicated by this property.",
  "id" : "[Output-only] The fully-qualified unique name of the dataset in the format projectId:datasetId. The dataset name without the project name is given in the datasetId field. When creating a new dataset, leave this field blank, and instead specify the datasetId field.",
  "friendlyName" : "[Optional] A descriptive name for the dataset."
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

## patch_table

Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports patch semantics.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the table to update

**Type:** string

### projectId (required)

Project ID of the table to update

**Type:** string

### tableId (required)

Table ID of the table to update

**Type:** string

### $body

**Type:** object

```json
{
  "schema" : {
    "fields" : [ {
      "mode" : "[Optional] The field mode. Possible values include NULLABLE, REQUIRED and REPEATED. The default value is NULLABLE.",
      "name" : "[Required] The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters.",
      "description" : "[Optional] The field description. The maximum length is 1,024 characters.",
      "categories" : {
        "names" : [ "string" ]
      },
      "fields" : [ { } ],
      "type" : "[Required] The field data type. Possible values include STRING, BYTES, INTEGER, INT64 (same as INTEGER), FLOAT, FLOAT64 (same as FLOAT), BOOLEAN, BOOL (same as BOOLEAN), TIMESTAMP, DATE, TIME, DATETIME, RECORD (where RECORD indicates that the field contains a nested schema) or STRUCT (same as RECORD)."
    } ]
  },
  "lastModifiedTime" : "[Output-only] The time when this table was last modified, in milliseconds since the epoch.",
  "creationTime" : "[Output-only] The time when this table was created, in milliseconds since the epoch.",
  "numRows" : "[Output-only] The number of rows of data in this table, excluding any data in the streaming buffer.",
  "description" : "[Optional] A user-friendly description of this table.",
  "requirePartitionFilter" : "[Beta] [Optional] If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.",
  "type" : "[Output-only] Describes the table type. The following values are supported: TABLE: A normal BigQuery table. VIEW: A virtual table defined by a SQL query. [TrustedTester] MATERIALIZED_VIEW: SQL query whose result is persisted. EXTERNAL: A table that references data stored in an external storage system, such as Google Cloud Storage. The default value is TABLE.",
  "numBytes" : "[Output-only] The size of this table in bytes, excluding any data in the streaming buffer.",
  "externalDataConfiguration" : {
    "schema" : {
      "fields" : [ {
        "mode" : "[Optional] The field mode. Possible values include NULLABLE, REQUIRED and REPEATED. The default value is NULLABLE.",
        "name" : "[Required] The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters.",
        "description" : "[Optional] The field description. The maximum length is 1,024 characters.",
        "categories" : {
          "names" : [ "string" ]
        },
        "fields" : [ { } ],
        "type" : "[Required] The field data type. Possible values include STRING, BYTES, INTEGER, INT64 (same as INTEGER), FLOAT, FLOAT64 (same as FLOAT), BOOLEAN, BOOL (same as BOOLEAN), TIMESTAMP, DATE, TIME, DATETIME, RECORD (where RECORD indicates that the field contains a nested schema) or STRUCT (same as RECORD)."
      } ]
    },
    "autodetect" : "Try to detect schema and format options automatically. Any option specified explicitly will be honored.",
    "sourceUris" : [ "string" ],
    "bigtableOptions" : {
      "columnFamilies" : [ {
        "familyId" : "Identifier of the column family.",
        "columns" : [ {
          "qualifierEncoded" : "[Required] Qualifier of the column. Columns in the parent column family that has this exact qualifier are exposed as . field. If the qualifier is valid UTF-8 string, it can be specified in the qualifier_string field. Otherwise, a base-64 encoded value must be set to qualifier_encoded. The column field name is the same as the column qualifier. However, if the qualifier is not a valid BigQuery field identifier i.e. does not match [a-zA-Z][a-zA-Z0-9_]*, a valid identifier must be provided as field_name.",
          "fieldName" : "[Optional] If the qualifier is not a valid BigQuery field identifier i.e. does not match [a-zA-Z][a-zA-Z0-9_]*, a valid identifier must be provided as the column field name and is used as field name in queries.",
          "encoding" : "[Optional] The encoding of the values when the type is not STRING. Acceptable encoding values are: TEXT - indicates values are alphanumeric text strings. BINARY - indicates values are encoded using HBase Bytes.toBytes family of functions. 'encoding' can also be set at the column family level. However, the setting at this level takes precedence if 'encoding' is set at both levels.",
          "qualifierString" : "string",
          "type" : "[Optional] The type to convert the value in cells of this column. The values are expected to be encoded using HBase Bytes.toBytes function when using the BINARY encoding value. Following BigQuery types are allowed (case-sensitive) - BYTES STRING INTEGER FLOAT BOOLEAN Default type is BYTES. 'type' can also be set at the column family level. However, the setting at this level takes precedence if 'type' is set at both levels.",
          "onlyReadLatest" : "[Optional] If this is set, only the latest version of value in this column are exposed. 'onlyReadLatest' can also be set at the column family level. However, the setting at this level takes precedence if 'onlyReadLatest' is set at both levels."
        } ],
        "encoding" : "[Optional] The encoding of the values when the type is not STRING. Acceptable encoding values are: TEXT - indicates values are alphanumeric text strings. BINARY - indicates values are encoded using HBase Bytes.toBytes family of functions. This can be overridden for a specific column by listing that column in 'columns' and specifying an encoding for it.",
        "type" : "[Optional] The type to convert the value in cells of this column family. The values are expected to be encoded using HBase Bytes.toBytes function when using the BINARY encoding value. Following BigQuery types are allowed (case-sensitive) - BYTES STRING INTEGER FLOAT BOOLEAN Default type is BYTES. This can be overridden for a specific column by listing that column in 'columns' and specifying a type for it.",
        "onlyReadLatest" : "[Optional] If this is set only the latest version of value are exposed for all columns in this column family. This can be overridden for a specific column by listing that column in 'columns' and specifying a different setting for that column."
      } ],
      "ignoreUnspecifiedColumnFamilies" : "[Optional] If field is true, then the column families that are not specified in columnFamilies list are not exposed in the table schema. Otherwise, they are read with BYTES type values. The default value is false.",
      "readRowkeyAsString" : "[Optional] If field is true, then the rowkey column families will be read and converted to string. Otherwise they are read with BYTES type values and users need to manually cast them with CAST if necessary. The default value is false."
    },
    "csvOptions" : {
      "allowQuotedNewlines" : "[Optional] Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file. The default value is false.",
      "skipLeadingRows" : "[Optional] The number of rows at the top of a CSV file that BigQuery will skip when reading the data. The default value is 0. This property is useful if you have header rows in the file that should be skipped.",
      "quote" : "[Optional] The value that is used to quote data sections in a CSV file. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. The default value is a double-quote ('\"'). If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allowQuotedNewlines property to true.",
      "encoding" : "[Optional] The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. The default value is UTF-8. BigQuery decodes the data after the raw, binary data has been split using the values of the quote and fieldDelimiter properties.",
      "fieldDelimiter" : "[Optional] The separator for fields in a CSV file. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. BigQuery also supports the escape sequence \"\\t\" to specify a tab separator. The default value is a comma (',').",
      "allowJaggedRows" : "[Optional] Indicates if BigQuery should accept rows that are missing trailing optional columns. If true, BigQuery treats missing trailing columns as null values. If false, records with missing trailing columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false."
    },
    "hivePartitioningMode" : "[Optional, Experimental] If hive partitioning is enabled, which mode to use. Two modes are supported: - AUTO: automatically infer partition key name(s) and type(s). - STRINGS: automatic infer partition key name(s). All types are strings. Not all storage formats support hive partitioning -- requesting hive partitioning on an unsupported format will lead to an error.",
    "ignoreUnknownValues" : "[Optional] Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. The sourceFormat property determines what BigQuery treats as an extra value: CSV: Trailing columns JSON: Named values that don't match any column names Google Cloud Bigtable: This setting is ignored. Google Cloud Datastore backups: This setting is ignored. Avro: This setting is ignored.",
    "googleSheetsOptions" : {
      "skipLeadingRows" : "[Optional] The number of rows at the top of a sheet that BigQuery will skip when reading the data. The default value is 0. This property is useful if you have header rows that should be skipped. When autodetect is on, behavior is the following: * skipLeadingRows unspecified - Autodetect tries to detect headers in the first row. If they are not detected, the row is read as data. Otherwise data is read starting from the second row. * skipLeadingRows is 0 - Instructs autodetect that there are no headers and data should be read starting from the first row. * skipLeadingRows = N &gt; 0 - Autodetect skips N-1 rows and tries to detect headers in row N. If headers are not detected, row N is just skipped. Otherwise row N is used to extract column names for the detected schema.",
      "range" : "[Beta] [Optional] Range of a sheet to query from. Only used when non-empty. Typical format: sheet_name!top_left_cell_id:bottom_right_cell_id For example: sheet1!A1:B20"
    },
    "compression" : "[Optional] The compression type of the data source. Possible values include GZIP and NONE. The default value is NONE. This setting is ignored for Google Cloud Bigtable, Google Cloud Datastore backups and Avro formats.",
    "sourceFormat" : "[Required] The data format. For CSV files, specify \"CSV\". For Google sheets, specify \"GOOGLE_SHEETS\". For newline-delimited JSON, specify \"NEWLINE_DELIMITED_JSON\". For Avro files, specify \"AVRO\". For Google Cloud Datastore backups, specify \"DATASTORE_BACKUP\". [Beta] For Google Cloud Bigtable, specify \"BIGTABLE\".",
    "maxBadRecords" : "[Optional] The maximum number of bad records that BigQuery can ignore when reading data. If the number of bad records exceeds this value, an invalid error is returned in the job result. This is only valid for CSV, JSON, and Google Sheets. The default value is 0, which requires that all records are valid. This setting is ignored for Google Cloud Bigtable, Google Cloud Datastore backups and Avro formats."
  },
  "view" : {
    "userDefinedFunctionResources" : [ {
      "resourceUri" : "[Pick one] A code resource to load from a Google Cloud Storage URI (gs://bucket/path).",
      "inlineCode" : "[Pick one] An inline resource that contains code for a user-defined function (UDF). Providing a inline code resource is equivalent to providing a URI for a file containing the same code."
    } ],
    "query" : "[Required] A query that BigQuery executes when the view is referenced.",
    "useLegacySql" : "Specifies whether to use BigQuery's legacy SQL for this view. The default value is true. If set to false, the view will use BigQuery's standard SQL: https://cloud.google.com/bigquery/sql-reference/ Queries and views that reference this view must use the same flag value."
  },
  "numLongTermBytes" : "[Output-only] The number of bytes in the table that are considered \"long-term storage\".",
  "encryptionConfiguration" : {
    "kmsKeyName" : "[Optional] Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key."
  },
  "model" : {
    "trainingRuns" : [ {
      "trainingOptions" : {
        "earlyStop" : "boolean",
        "l1Reg" : "number",
        "maxIteration" : "int64",
        "l2Reg" : "number",
        "learnRate" : "number",
        "lineSearchInitLearnRate" : "number",
        "warmStart" : "boolean",
        "learnRateStrategy" : "string",
        "minRelProgress" : "number"
      },
      "iterationResults" : [ {
        "index" : "[Output-only, Beta] Index of the ML training iteration, starting from zero for each training run.",
        "learnRate" : "[Output-only, Beta] Learning rate used for this iteration, it varies for different training iterations if learn_rate_strategy option is not constant.",
        "durationMs" : "[Output-only, Beta] Time taken to run the training iteration in milliseconds.",
        "evalLoss" : "[Output-only, Beta] Eval loss computed on the eval data at the end of the iteration. The eval loss is used for early stopping to avoid overfitting. No eval loss if eval_split_method option is specified as no_split or auto_split with input data size less than 500 rows.",
        "trainingLoss" : "[Output-only, Beta] Training loss computed on the training data at the end of the iteration. The training loss function is defined by model type."
      } ],
      "startTime" : "[Output-only, Beta] Training run start time in milliseconds since the epoch.",
      "state" : "[Output-only, Beta] Different state applicable for a training run. IN PROGRESS: Training run is in progress. FAILED: Training run ended due to a non-retryable failure. SUCCEEDED: Training run successfully completed. CANCELLED: Training run cancelled by the user."
    } ],
    "modelOptions" : {
      "lossType" : "string",
      "modelType" : "string",
      "labels" : [ "string" ]
    }
  },
  "id" : "[Output-only] An opaque ID uniquely identifying the table.",
  "friendlyName" : "[Optional] A descriptive name for this table.",
  "materializedView" : {
    "query" : "[Required] A query whose result is persisted.",
    "lastRefreshTime" : "[Output-only] [TrustedTester] The time when this materialized view was last modified, in milliseconds since the epoch."
  },
  "timePartitioning" : {
    "field" : "[Beta] [Optional] If not set, the table is partitioned by pseudo column, referenced via either '_PARTITIONTIME' as TIMESTAMP type, or '_PARTITIONDATE' as DATE type. If field is specified, the table is instead partitioned by this field. The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED.",
    "expirationMs" : "[Optional] Number of milliseconds for which to keep the storage for partitions in the table. The storage in a partition will have an expiration time of its partition time plus this value.",
    "requirePartitionFilter" : "boolean",
    "type" : "[Required] The only type supported is DAY, which will generate one partition per day."
  },
  "streamingBuffer" : {
    "estimatedBytes" : "[Output-only] A lower-bound estimate of the number of bytes currently in the streaming buffer.",
    "oldestEntryTime" : "[Output-only] Contains the timestamp of the oldest entry in the streaming buffer, in milliseconds since the epoch, if the streaming buffer is available.",
    "estimatedRows" : "[Output-only] A lower-bound estimate of the number of rows currently in the streaming buffer."
  },
  "kind" : "[Output-only] The type of the resource.",
  "labels" : "The labels associated with this table. You can use these to organize and group your tables. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key.",
  "selfLink" : "[Output-only] A URL that can be used to access this resource again.",
  "numPhysicalBytes" : "[Output-only] [TrustedTester] The physical size of this table in bytes, excluding any data in the streaming buffer. This includes compression and storage used for time travel.",
  "tableReference" : {
    "datasetId" : "[Required] The ID of the dataset containing this table.",
    "tableId" : "[Required] The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.",
    "projectId" : "[Required] The ID of the project containing this table."
  },
  "expirationTime" : "[Optional] The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. The defaultTableExpirationMs property of the encapsulating dataset can be used to set a default expirationTime on newly created tables.",
  "rangePartitioning" : {
    "field" : "[TrustedTester] [Required] The table is partitioned by this field. The field must be a top-level NULLABLE/REQUIRED field. The only supported type is INTEGER/INT64.",
    "range" : {
      "start" : "[TrustedTester] [Required] The start of range partitioning, inclusive.",
      "end" : "[TrustedTester] [Required] The end of range partitioning, exclusive.",
      "interval" : "[TrustedTester] [Required] The width of each interval."
    }
  },
  "clustering" : {
    "fields" : [ "string" ]
  },
  "etag" : "[Output-only] A hash of the table metadata. Used to ensure there were no concurrent modifications to the resource when attempting an update. Not guaranteed to change when the table contents or the fields numRows, numBytes, numLongTermBytes or lastModifiedTime change.",
  "location" : "[Output-only] The geographic location where the table resides. This value is inherited from the dataset."
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

## start_job



*This operation has no parameters*

## stream_data_to_table

Streams data into BigQuery one record at a time without needing to run a load job. Requires the WRITER dataset role.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the destination table.

**Type:** string

### projectId (required)

Project ID of the destination table.

**Type:** string

### tableId (required)

Table ID of the destination table.

**Type:** string

### $body

**Type:** object

```json
{
  "skipInvalidRows" : "[Optional] Insert all valid rows of a request, even if invalid rows exist. The default value is false, which causes the entire request to fail if any invalid rows exist.",
  "kind" : "The resource type of the response.",
  "templateSuffix" : "If specified, treats the destination table as a base template, and inserts the rows into an instance table named \"{destination}{templateSuffix}\". BigQuery will manage creation of the instance table, using the schema of the base template table. See https://cloud.google.com/bigquery/streaming-data-into-bigquery#template-tables for considerations when working with templates tables.",
  "ignoreUnknownValues" : "[Optional] Accept rows that contain values that do not match the schema. The unknown values are ignored. Default is false, which treats unknown values as errors.",
  "rows" : [ {
    "json" : "Represents a single JSON object.",
    "insertId" : "[Optional] A unique ID for each row. BigQuery uses this property to detect duplicate insertion requests on a best-effort basis."
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

## tabledata.list

Retrieves table data from a specified set of rows. Requires the READER dataset role.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the table to read

**Type:** string

### projectId (required)

Project ID of the table to read

**Type:** string

### tableId (required)

Table ID of the table to read

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

### selectedFields

List of fields to return (comma-separated). If unspecified, all fields are returned

**Type:** string

### startIndex

Zero-based index of the starting row to read

**Type:** string

### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## update_dataset

Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the dataset being updated

**Type:** string

### projectId (required)

Project ID of the dataset being updated

**Type:** string

### $body

**Type:** object

```json
{
  "access" : [ {
    "view" : {
      "datasetId" : "[Required] The ID of the dataset containing this table.",
      "tableId" : "[Required] The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.",
      "projectId" : "[Required] The ID of the project containing this table."
    },
    "role" : "[Required] An IAM role ID that should be granted to the user, group, or domain specified in this access entry. The following legacy mappings will be applied: OWNER roles/bigquery.dataOwner WRITER roles/bigquery.dataEditor READER roles/bigquery.dataViewer This field will accept any of the above formats, but will return only the legacy format. For example, if you set this field to \"roles/bigquery.dataOwner\", it will be returned back as \"OWNER\".",
    "userByEmail" : "[Pick one] An email address of a user to grant access to. For example: fred@example.com. Maps to IAM policy member \"user:EMAIL\" or \"serviceAccount:EMAIL\".",
    "domain" : "[Pick one] A domain to grant access to. Any users signed in with the domain specified will be granted the specified access. Example: \"example.com\". Maps to IAM policy member \"domain:DOMAIN\".",
    "specialGroup" : "[Pick one] A special group to grant access to. Possible values include: projectOwners: Owners of the enclosing project. projectReaders: Readers of the enclosing project. projectWriters: Writers of the enclosing project. allAuthenticatedUsers: All authenticated BigQuery users. Maps to similarly-named IAM members.",
    "iamMember" : "[Pick one] Some other type of member that appears in the IAM Policy but isn't a user, group, domain, or special group.",
    "groupByEmail" : "[Pick one] An email address of a Google Group to grant access to. Maps to IAM policy member \"group:GROUP\"."
  } ],
  "lastModifiedTime" : "[Output-only] The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.",
  "creationTime" : "[Output-only] The time when this dataset was created, in milliseconds since the epoch.",
  "kind" : "[Output-only] The resource type.",
  "description" : "[Optional] A user-friendly description of the dataset.",
  "datasetReference" : {
    "datasetId" : "[Required] A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.",
    "projectId" : "[Optional] The ID of the project containing this dataset."
  },
  "labels" : "The labels associated with this dataset. You can use these to organize and group your datasets. You can set this property when inserting or updating a dataset. See Creating and Updating Dataset Labels for more information.",
  "selfLink" : "[Output-only] A URL that can be used to access the resource again. You can use this URL in Get or Update requests to the resource.",
  "defaultPartitionExpirationMs" : "[Optional] The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set, all newly-created partitioned tables in the dataset will have an expirationMs property in the timePartitioning settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of defaultTableExpirationMs for partitioned tables: only one of defaultTableExpirationMs and defaultPartitionExpirationMs will be used for any new partitioned table. If you provide an explicit timePartitioning.expirationMs when creating or updating a partitioned table, that value takes precedence over the default partition expiration time indicated by this property.",
  "etag" : "[Output-only] A hash of the resource.",
  "location" : "The geographic location where the dataset should reside. The default value is US. See details at https://cloud.google.com/bigquery/docs/locations.",
  "defaultTableExpirationMs" : "[Optional] The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one hour). Once this property is set, all newly-created tables in the dataset will have an expirationTime property set to the creation time plus the value in this property, and changing the value will only affect new tables, not existing ones. When the expirationTime for a given table is reached, that table will be deleted automatically. If a table's expirationTime is modified or removed before the table expires, or if you provide an explicit expirationTime when creating a table, that value takes precedence over the default expiration time indicated by this property.",
  "id" : "[Output-only] The fully-qualified unique name of the dataset in the format projectId:datasetId. The dataset name without the project name is given in the datasetId field. When creating a new dataset, leave this field blank, and instead specify the datasetId field.",
  "friendlyName" : "[Optional] A descriptive name for the dataset."
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

## update_table

Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource.

<details><summary>Parameters</summary>

### datasetId (required)

Dataset ID of the table to update

**Type:** string

### projectId (required)

Project ID of the table to update

**Type:** string

### tableId (required)

Table ID of the table to update

**Type:** string

### $body

**Type:** object

```json
{
  "schema" : {
    "fields" : [ {
      "mode" : "[Optional] The field mode. Possible values include NULLABLE, REQUIRED and REPEATED. The default value is NULLABLE.",
      "name" : "[Required] The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters.",
      "description" : "[Optional] The field description. The maximum length is 1,024 characters.",
      "categories" : {
        "names" : [ "string" ]
      },
      "fields" : [ { } ],
      "type" : "[Required] The field data type. Possible values include STRING, BYTES, INTEGER, INT64 (same as INTEGER), FLOAT, FLOAT64 (same as FLOAT), BOOLEAN, BOOL (same as BOOLEAN), TIMESTAMP, DATE, TIME, DATETIME, RECORD (where RECORD indicates that the field contains a nested schema) or STRUCT (same as RECORD)."
    } ]
  },
  "lastModifiedTime" : "[Output-only] The time when this table was last modified, in milliseconds since the epoch.",
  "creationTime" : "[Output-only] The time when this table was created, in milliseconds since the epoch.",
  "numRows" : "[Output-only] The number of rows of data in this table, excluding any data in the streaming buffer.",
  "description" : "[Optional] A user-friendly description of this table.",
  "requirePartitionFilter" : "[Beta] [Optional] If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.",
  "type" : "[Output-only] Describes the table type. The following values are supported: TABLE: A normal BigQuery table. VIEW: A virtual table defined by a SQL query. [TrustedTester] MATERIALIZED_VIEW: SQL query whose result is persisted. EXTERNAL: A table that references data stored in an external storage system, such as Google Cloud Storage. The default value is TABLE.",
  "numBytes" : "[Output-only] The size of this table in bytes, excluding any data in the streaming buffer.",
  "externalDataConfiguration" : {
    "schema" : {
      "fields" : [ {
        "mode" : "[Optional] The field mode. Possible values include NULLABLE, REQUIRED and REPEATED. The default value is NULLABLE.",
        "name" : "[Required] The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters.",
        "description" : "[Optional] The field description. The maximum length is 1,024 characters.",
        "categories" : {
          "names" : [ "string" ]
        },
        "fields" : [ { } ],
        "type" : "[Required] The field data type. Possible values include STRING, BYTES, INTEGER, INT64 (same as INTEGER), FLOAT, FLOAT64 (same as FLOAT), BOOLEAN, BOOL (same as BOOLEAN), TIMESTAMP, DATE, TIME, DATETIME, RECORD (where RECORD indicates that the field contains a nested schema) or STRUCT (same as RECORD)."
      } ]
    },
    "autodetect" : "Try to detect schema and format options automatically. Any option specified explicitly will be honored.",
    "sourceUris" : [ "string" ],
    "bigtableOptions" : {
      "columnFamilies" : [ {
        "familyId" : "Identifier of the column family.",
        "columns" : [ {
          "qualifierEncoded" : "[Required] Qualifier of the column. Columns in the parent column family that has this exact qualifier are exposed as . field. If the qualifier is valid UTF-8 string, it can be specified in the qualifier_string field. Otherwise, a base-64 encoded value must be set to qualifier_encoded. The column field name is the same as the column qualifier. However, if the qualifier is not a valid BigQuery field identifier i.e. does not match [a-zA-Z][a-zA-Z0-9_]*, a valid identifier must be provided as field_name.",
          "fieldName" : "[Optional] If the qualifier is not a valid BigQuery field identifier i.e. does not match [a-zA-Z][a-zA-Z0-9_]*, a valid identifier must be provided as the column field name and is used as field name in queries.",
          "encoding" : "[Optional] The encoding of the values when the type is not STRING. Acceptable encoding values are: TEXT - indicates values are alphanumeric text strings. BINARY - indicates values are encoded using HBase Bytes.toBytes family of functions. 'encoding' can also be set at the column family level. However, the setting at this level takes precedence if 'encoding' is set at both levels.",
          "qualifierString" : "string",
          "type" : "[Optional] The type to convert the value in cells of this column. The values are expected to be encoded using HBase Bytes.toBytes function when using the BINARY encoding value. Following BigQuery types are allowed (case-sensitive) - BYTES STRING INTEGER FLOAT BOOLEAN Default type is BYTES. 'type' can also be set at the column family level. However, the setting at this level takes precedence if 'type' is set at both levels.",
          "onlyReadLatest" : "[Optional] If this is set, only the latest version of value in this column are exposed. 'onlyReadLatest' can also be set at the column family level. However, the setting at this level takes precedence if 'onlyReadLatest' is set at both levels."
        } ],
        "encoding" : "[Optional] The encoding of the values when the type is not STRING. Acceptable encoding values are: TEXT - indicates values are alphanumeric text strings. BINARY - indicates values are encoded using HBase Bytes.toBytes family of functions. This can be overridden for a specific column by listing that column in 'columns' and specifying an encoding for it.",
        "type" : "[Optional] The type to convert the value in cells of this column family. The values are expected to be encoded using HBase Bytes.toBytes function when using the BINARY encoding value. Following BigQuery types are allowed (case-sensitive) - BYTES STRING INTEGER FLOAT BOOLEAN Default type is BYTES. This can be overridden for a specific column by listing that column in 'columns' and specifying a type for it.",
        "onlyReadLatest" : "[Optional] If this is set only the latest version of value are exposed for all columns in this column family. This can be overridden for a specific column by listing that column in 'columns' and specifying a different setting for that column."
      } ],
      "ignoreUnspecifiedColumnFamilies" : "[Optional] If field is true, then the column families that are not specified in columnFamilies list are not exposed in the table schema. Otherwise, they are read with BYTES type values. The default value is false.",
      "readRowkeyAsString" : "[Optional] If field is true, then the rowkey column families will be read and converted to string. Otherwise they are read with BYTES type values and users need to manually cast them with CAST if necessary. The default value is false."
    },
    "csvOptions" : {
      "allowQuotedNewlines" : "[Optional] Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file. The default value is false.",
      "skipLeadingRows" : "[Optional] The number of rows at the top of a CSV file that BigQuery will skip when reading the data. The default value is 0. This property is useful if you have header rows in the file that should be skipped.",
      "quote" : "[Optional] The value that is used to quote data sections in a CSV file. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. The default value is a double-quote ('\"'). If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allowQuotedNewlines property to true.",
      "encoding" : "[Optional] The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. The default value is UTF-8. BigQuery decodes the data after the raw, binary data has been split using the values of the quote and fieldDelimiter properties.",
      "fieldDelimiter" : "[Optional] The separator for fields in a CSV file. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. BigQuery also supports the escape sequence \"\\t\" to specify a tab separator. The default value is a comma (',').",
      "allowJaggedRows" : "[Optional] Indicates if BigQuery should accept rows that are missing trailing optional columns. If true, BigQuery treats missing trailing columns as null values. If false, records with missing trailing columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false."
    },
    "hivePartitioningMode" : "[Optional, Experimental] If hive partitioning is enabled, which mode to use. Two modes are supported: - AUTO: automatically infer partition key name(s) and type(s). - STRINGS: automatic infer partition key name(s). All types are strings. Not all storage formats support hive partitioning -- requesting hive partitioning on an unsupported format will lead to an error.",
    "ignoreUnknownValues" : "[Optional] Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. The sourceFormat property determines what BigQuery treats as an extra value: CSV: Trailing columns JSON: Named values that don't match any column names Google Cloud Bigtable: This setting is ignored. Google Cloud Datastore backups: This setting is ignored. Avro: This setting is ignored.",
    "googleSheetsOptions" : {
      "skipLeadingRows" : "[Optional] The number of rows at the top of a sheet that BigQuery will skip when reading the data. The default value is 0. This property is useful if you have header rows that should be skipped. When autodetect is on, behavior is the following: * skipLeadingRows unspecified - Autodetect tries to detect headers in the first row. If they are not detected, the row is read as data. Otherwise data is read starting from the second row. * skipLeadingRows is 0 - Instructs autodetect that there are no headers and data should be read starting from the first row. * skipLeadingRows = N &gt; 0 - Autodetect skips N-1 rows and tries to detect headers in row N. If headers are not detected, row N is just skipped. Otherwise row N is used to extract column names for the detected schema.",
      "range" : "[Beta] [Optional] Range of a sheet to query from. Only used when non-empty. Typical format: sheet_name!top_left_cell_id:bottom_right_cell_id For example: sheet1!A1:B20"
    },
    "compression" : "[Optional] The compression type of the data source. Possible values include GZIP and NONE. The default value is NONE. This setting is ignored for Google Cloud Bigtable, Google Cloud Datastore backups and Avro formats.",
    "sourceFormat" : "[Required] The data format. For CSV files, specify \"CSV\". For Google sheets, specify \"GOOGLE_SHEETS\". For newline-delimited JSON, specify \"NEWLINE_DELIMITED_JSON\". For Avro files, specify \"AVRO\". For Google Cloud Datastore backups, specify \"DATASTORE_BACKUP\". [Beta] For Google Cloud Bigtable, specify \"BIGTABLE\".",
    "maxBadRecords" : "[Optional] The maximum number of bad records that BigQuery can ignore when reading data. If the number of bad records exceeds this value, an invalid error is returned in the job result. This is only valid for CSV, JSON, and Google Sheets. The default value is 0, which requires that all records are valid. This setting is ignored for Google Cloud Bigtable, Google Cloud Datastore backups and Avro formats."
  },
  "view" : {
    "userDefinedFunctionResources" : [ {
      "resourceUri" : "[Pick one] A code resource to load from a Google Cloud Storage URI (gs://bucket/path).",
      "inlineCode" : "[Pick one] An inline resource that contains code for a user-defined function (UDF). Providing a inline code resource is equivalent to providing a URI for a file containing the same code."
    } ],
    "query" : "[Required] A query that BigQuery executes when the view is referenced.",
    "useLegacySql" : "Specifies whether to use BigQuery's legacy SQL for this view. The default value is true. If set to false, the view will use BigQuery's standard SQL: https://cloud.google.com/bigquery/sql-reference/ Queries and views that reference this view must use the same flag value."
  },
  "numLongTermBytes" : "[Output-only] The number of bytes in the table that are considered \"long-term storage\".",
  "encryptionConfiguration" : {
    "kmsKeyName" : "[Optional] Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key."
  },
  "model" : {
    "trainingRuns" : [ {
      "trainingOptions" : {
        "earlyStop" : "boolean",
        "l1Reg" : "number",
        "maxIteration" : "int64",
        "l2Reg" : "number",
        "learnRate" : "number",
        "lineSearchInitLearnRate" : "number",
        "warmStart" : "boolean",
        "learnRateStrategy" : "string",
        "minRelProgress" : "number"
      },
      "iterationResults" : [ {
        "index" : "[Output-only, Beta] Index of the ML training iteration, starting from zero for each training run.",
        "learnRate" : "[Output-only, Beta] Learning rate used for this iteration, it varies for different training iterations if learn_rate_strategy option is not constant.",
        "durationMs" : "[Output-only, Beta] Time taken to run the training iteration in milliseconds.",
        "evalLoss" : "[Output-only, Beta] Eval loss computed on the eval data at the end of the iteration. The eval loss is used for early stopping to avoid overfitting. No eval loss if eval_split_method option is specified as no_split or auto_split with input data size less than 500 rows.",
        "trainingLoss" : "[Output-only, Beta] Training loss computed on the training data at the end of the iteration. The training loss function is defined by model type."
      } ],
      "startTime" : "[Output-only, Beta] Training run start time in milliseconds since the epoch.",
      "state" : "[Output-only, Beta] Different state applicable for a training run. IN PROGRESS: Training run is in progress. FAILED: Training run ended due to a non-retryable failure. SUCCEEDED: Training run successfully completed. CANCELLED: Training run cancelled by the user."
    } ],
    "modelOptions" : {
      "lossType" : "string",
      "modelType" : "string",
      "labels" : [ "string" ]
    }
  },
  "id" : "[Output-only] An opaque ID uniquely identifying the table.",
  "friendlyName" : "[Optional] A descriptive name for this table.",
  "materializedView" : {
    "query" : "[Required] A query whose result is persisted.",
    "lastRefreshTime" : "[Output-only] [TrustedTester] The time when this materialized view was last modified, in milliseconds since the epoch."
  },
  "timePartitioning" : {
    "field" : "[Beta] [Optional] If not set, the table is partitioned by pseudo column, referenced via either '_PARTITIONTIME' as TIMESTAMP type, or '_PARTITIONDATE' as DATE type. If field is specified, the table is instead partitioned by this field. The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED.",
    "expirationMs" : "[Optional] Number of milliseconds for which to keep the storage for partitions in the table. The storage in a partition will have an expiration time of its partition time plus this value.",
    "requirePartitionFilter" : "boolean",
    "type" : "[Required] The only type supported is DAY, which will generate one partition per day."
  },
  "streamingBuffer" : {
    "estimatedBytes" : "[Output-only] A lower-bound estimate of the number of bytes currently in the streaming buffer.",
    "oldestEntryTime" : "[Output-only] Contains the timestamp of the oldest entry in the streaming buffer, in milliseconds since the epoch, if the streaming buffer is available.",
    "estimatedRows" : "[Output-only] A lower-bound estimate of the number of rows currently in the streaming buffer."
  },
  "kind" : "[Output-only] The type of the resource.",
  "labels" : "The labels associated with this table. You can use these to organize and group your tables. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key.",
  "selfLink" : "[Output-only] A URL that can be used to access this resource again.",
  "numPhysicalBytes" : "[Output-only] [TrustedTester] The physical size of this table in bytes, excluding any data in the streaming buffer. This includes compression and storage used for time travel.",
  "tableReference" : {
    "datasetId" : "[Required] The ID of the dataset containing this table.",
    "tableId" : "[Required] The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters.",
    "projectId" : "[Required] The ID of the project containing this table."
  },
  "expirationTime" : "[Optional] The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. The defaultTableExpirationMs property of the encapsulating dataset can be used to set a default expirationTime on newly created tables.",
  "rangePartitioning" : {
    "field" : "[TrustedTester] [Required] The table is partitioned by this field. The field must be a top-level NULLABLE/REQUIRED field. The only supported type is INTEGER/INT64.",
    "range" : {
      "start" : "[TrustedTester] [Required] The start of range partitioning, inclusive.",
      "end" : "[TrustedTester] [Required] The end of range partitioning, exclusive.",
      "interval" : "[TrustedTester] [Required] The width of each interval."
    }
  },
  "clustering" : {
    "fields" : [ "string" ]
  },
  "etag" : "[Output-only] A hash of the table metadata. Used to ensure there were no concurrent modifications to the resource when attempting an update. Not guaranteed to change when the table contents or the fields numRows, numBytes, numLongTermBytes or lastModifiedTime change.",
  "location" : "[Output-only] The geographic location where the table resides. This value is inherited from the dataset."
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

