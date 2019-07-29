---
id: aws-kinesis-firehose-documentation
title: AWS Kinesis Firehose (version v2.*.*)
sidebar_label: AWS Kinesis Firehose
layout: docs.mustache
---

## create_delivery_stream

Creates a Kinesis Data Firehose delivery stream. 
By default, you can create up to 50 delivery streams per AWS Region. 
This is an asynchronous operation that immediately returns. The initial status of the delivery stream is CREATING. After the delivery stream is created, its status is ACTIVE and it now accepts data. Attempts to send data to a delivery stream that is not in the ACTIVE state cause an exception. To check the state of a delivery stream, use DescribeDeliveryStream. 
A Kinesis Data Firehose delivery stream can be configured to receive records directly from providers using PutRecord or PutRecordBatch, or it can be configured to use an existing Kinesis stream as its source. To specify a Kinesis data stream as input, set the DeliveryStreamType parameter to KinesisStreamAsSource, and provide the Kinesis stream Amazon Resource Name (ARN) and role ARN in the KinesisStreamSourceConfiguration parameter. 
A delivery stream is configured with a single destination: Amazon S3, Amazon ES, Amazon Redshift, or Splunk. You must specify only one of the following destination configuration parameters: ExtendedS3DestinationConfiguration, S3DestinationConfiguration, ElasticsearchDestinationConfiguration, RedshiftDestinationConfiguration, or SplunkDestinationConfiguration. 
When you specify S3DestinationConfiguration, you can also provide the following optional values: BufferingHints, EncryptionConfiguration, and CompressionFormat. By default, if no BufferingHints value is provided, Kinesis Data Firehose buffers data up to 5 MB or for 5 minutes, whichever condition is satisfied first. BufferingHints is a hint, so there are some cases where the service cannot adhere to these conditions strictly. For example, record boundaries might be such that the size is a little over or under the configured buffering size. By default, no encryption is performed. We strongly recommend that you enable encryption to ensure secure data storage in Amazon S3. 
A few notes about Amazon Redshift as a destination:  
 An Amazon Redshift destination requires an S3 bucket as intermediate location. Kinesis Data Firehose first delivers data to Amazon S3 and then uses COPY syntax to load data into an Amazon Redshift table. This is specified in the RedshiftDestinationConfiguration.S3Configuration parameter.  
 The compression formats SNAPPY or ZIP cannot be specified in RedshiftDestinationConfiguration.S3Configuration because the Amazon Redshift COPY operation that reads from the S3 bucket doesn't support these compression formats.  
 We strongly recommend that you use the user name and password you provide exclusively with Kinesis Data Firehose, and that the permissions for the account are restricted for Amazon Redshift INSERT permissions.   
Kinesis Data Firehose assumes the IAM role that is configured as part of the destination. The role should allow the Kinesis Data Firehose principal to assume the role, and the role should have permissions that allow the service to deliver the data. For more information, see Grant Kinesis Data Firehose Access to an Amazon S3 Destination in the Amazon Kinesis Data Firehose Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "KinesisStreamSourceConfiguration" : {
    "KinesisStreamARN" : "The ARN of the source Kinesis data stream. For more information, see Amazon Kinesis Data Streams ARN Format.",
    "RoleARN" : "The ARN of the role that provides access to the source Kinesis data stream. For more information, see AWS Identity and Access Management (IAM) ARN Format."
  },
  "ElasticsearchDestinationConfiguration" : {
    "IndexName" : "The Elasticsearch index name.",
    "TypeName" : "The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Kinesis Data Firehose returns an error during run time.",
    "S3Configuration" : {
      "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "BufferingHints" : {
        "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
        "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
      },
      "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
      "EncryptionConfiguration" : {
        "KMSEncryptionConfig" : {
          "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
        },
        "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
      },
      "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
      "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "CloudWatchLoggingOptions" : {
        "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
        "Enabled" : "Enables or disables CloudWatch logging.",
        "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
      }
    },
    "BufferingHints" : {
      "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).",
      "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
    },
    "IndexRotationPeriod" : "The Elasticsearch index rotation period. Index rotation appends a time stamp to the IndexName to facilitate the expiration of old data. For more information, see Index Rotation for the Amazon ES Destination. The default value is&nbsp;OneDay.",
    "RetryOptions" : {
      "DurationInSeconds" : "After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries."
    },
    "ProcessingConfiguration" : {
      "Enabled" : "Enables or disables data processing.",
      "Processors" : [ {
        "Type" : "The type of processor.",
        "Parameters" : [ {
          "ParameterValue" : "The parameter value.",
          "ParameterName" : "The name of the parameter."
        } ]
      } ]
    },
    "RoleARN" : "The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see Grant Kinesis Data Firehose Access to an Amazon S3 Destination and Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "DomainARN" : "The ARN of the Amazon ES domain. The IAM role must have permissions for&nbsp;DescribeElasticsearchDomain, DescribeElasticsearchDomains, and DescribeElasticsearchDomainConfig&nbsp;after assuming the role specified in RoleARN. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "CloudWatchLoggingOptions" : {
      "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
      "Enabled" : "Enables or disables CloudWatch logging.",
      "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
    },
    "S3BackupMode" : "Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly, Kinesis Data Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with elasticsearch-failed/ appended to the key prefix. When set to AllDocuments, Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents with elasticsearch-failed/ appended to the prefix. For more information, see Amazon S3 Backup for the Amazon ES Destination. Default value is FailedDocumentsOnly."
  },
  "DeliveryStreamType" : "The delivery stream type. This parameter can be one of the following values:  \n  DirectPut: Provider applications access the delivery stream directly.  \n  KinesisStreamAsSource: The delivery stream uses a Kinesis data stream as a source. ",
  "S3DestinationConfiguration" : {
    "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "BufferingHints" : {
      "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
      "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
    },
    "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
    "EncryptionConfiguration" : {
      "KMSEncryptionConfig" : {
        "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
      },
      "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
    },
    "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
    "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "CloudWatchLoggingOptions" : {
      "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
      "Enabled" : "Enables or disables CloudWatch logging.",
      "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
    }
  },
  "RedshiftDestinationConfiguration" : {
    "S3BackupConfiguration" : {
      "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "BufferingHints" : {
        "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
        "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
      },
      "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
      "EncryptionConfiguration" : {
        "KMSEncryptionConfig" : {
          "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
        },
        "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
      },
      "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
      "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "CloudWatchLoggingOptions" : {
        "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
        "Enabled" : "Enables or disables CloudWatch logging.",
        "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
      }
    },
    "S3Configuration" : {
      "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "BufferingHints" : {
        "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
        "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
      },
      "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
      "EncryptionConfiguration" : {
        "KMSEncryptionConfig" : {
          "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
        },
        "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
      },
      "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
      "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "CloudWatchLoggingOptions" : {
        "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
        "Enabled" : "Enables or disables CloudWatch logging.",
        "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
      }
    },
    "Username" : "The name of the user.",
    "CopyCommand" : {
      "DataTableName" : "The name of the target table. The table must already exist in the database.",
      "DataTableColumns" : "A comma-separated list of column names.",
      "CopyOptions" : "Optional parameters to use with the Amazon Redshift COPY command. For more information, see the \"Optional Parameters\" section of Amazon Redshift COPY command. Some possible examples that would apply to Kinesis Data Firehose are as follows: \n delimiter '\\t' lzop; - fields are delimited with \"\\t\" (TAB character) and compressed using lzop. \n delimiter '|' - fields are delimited with \"|\" (this is the default delimiter). \n delimiter '|' escape - the delimiter should be escaped. \n fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6' - fields are fixed width in the source, with each width specified after every column in the table. \n JSON 's3://mybucket/jsonpaths.txt' - data is in JSON format, and the path specified is the format of the data. \nFor more examples, see Amazon Redshift COPY command examples."
    },
    "RetryOptions" : {
      "DurationInSeconds" : "The length of time during which Kinesis Data Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value."
    },
    "ProcessingConfiguration" : {
      "Enabled" : "Enables or disables data processing.",
      "Processors" : [ {
        "Type" : "The type of processor.",
        "Parameters" : [ {
          "ParameterValue" : "The parameter value.",
          "ParameterName" : "The name of the parameter."
        } ]
      } ]
    },
    "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "ClusterJDBCURL" : "The database connection string.",
    "CloudWatchLoggingOptions" : {
      "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
      "Enabled" : "Enables or disables CloudWatch logging.",
      "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
    },
    "Password" : "The user password.",
    "S3BackupMode" : "The Amazon S3 backup mode."
  },
  "DeliveryStreamName" : "The name of the delivery stream. This name must be unique per AWS account in the same AWS Region. If the delivery streams are in different accounts or different Regions, you can have multiple delivery streams with the same name.",
  "SplunkDestinationConfiguration" : {
    "HECEndpoint" : "The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.",
    "S3Configuration" : {
      "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "BufferingHints" : {
        "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
        "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
      },
      "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
      "EncryptionConfiguration" : {
        "KMSEncryptionConfig" : {
          "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
        },
        "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
      },
      "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
      "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "CloudWatchLoggingOptions" : {
        "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
        "Enabled" : "Enables or disables CloudWatch logging.",
        "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
      }
    },
    "HECToken" : "This is a GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.",
    "RetryOptions" : {
      "DurationInSeconds" : "The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn't include the periods during which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt."
    },
    "HECEndpointType" : "This type can be either \"Raw\" or \"Event.\"",
    "HECAcknowledgmentTimeoutInSeconds" : "The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Kinesis Data Firehose either tries to send the data again or considers it an error, based on your retry settings.",
    "ProcessingConfiguration" : {
      "Enabled" : "Enables or disables data processing.",
      "Processors" : [ {
        "Type" : "The type of processor.",
        "Parameters" : [ {
          "ParameterValue" : "The parameter value.",
          "ParameterName" : "The name of the parameter."
        } ]
      } ]
    },
    "CloudWatchLoggingOptions" : {
      "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
      "Enabled" : "Enables or disables CloudWatch logging.",
      "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
    },
    "S3BackupMode" : "Defines how documents should be delivered to Amazon S3. When set to FailedDocumentsOnly, Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to AllDocuments, Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is FailedDocumentsOnly. "
  },
  "ExtendedS3DestinationConfiguration" : {
    "S3BackupConfiguration" : {
      "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "BufferingHints" : {
        "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
        "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
      },
      "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
      "EncryptionConfiguration" : {
        "KMSEncryptionConfig" : {
          "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
        },
        "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
      },
      "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
      "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "CloudWatchLoggingOptions" : {
        "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
        "Enabled" : "Enables or disables CloudWatch logging.",
        "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
      }
    },
    "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "BufferingHints" : {
      "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
      "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
    },
    "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED.",
    "EncryptionConfiguration" : {
      "KMSEncryptionConfig" : {
        "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
      },
      "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
    },
    "DataFormatConversionConfiguration" : {
      "InputFormatConfiguration" : {
        "Deserializer" : {
          "HiveJsonSerDe" : {
            "TimestampFormats" : [ "string" ]
          },
          "OpenXJsonSerDe" : {
            "ConvertDotsInJsonKeysToUnderscores" : "When set to true, specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is \"a.b\", you can define the column name to be \"a_b\" when using this option. \nThe default is false.",
            "ColumnToJsonKeyMappings" : "Maps column names to JSON keys that aren't identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp, set this parameter to {\"ts\": \"timestamp\"} to map this key to a column named ts.",
            "CaseInsensitive" : "When set to true, which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them."
          }
        }
      },
      "Enabled" : "Defaults to true. Set it to false if you want to disable format conversion while preserving the configuration details.",
      "SchemaConfiguration" : {
        "VersionId" : "Specifies the table version for the output data schema. If you don't specify this version ID, or if you set it to LATEST, Kinesis Data Firehose uses the most recent version. This means that any updates to the table are automatically picked up.",
        "TableName" : "Specifies the AWS Glue table that contains the column information that constitutes your data schema.",
        "DatabaseName" : "Specifies the name of the AWS Glue database that contains the schema for the output data.",
        "Region" : "If you don't specify an AWS Region, the default is the current Region.",
        "CatalogId" : "The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used by default.",
        "RoleARN" : "The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren't allowed."
      },
      "OutputFormatConfiguration" : {
        "Serializer" : {
          "OrcSerDe" : {
            "PaddingTolerance" : "A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size. \nFor the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. \nKinesis Data Firehose ignores this parameter when OrcSerDe$EnablePadding is false.",
            "Compression" : "The compression code to use over data blocks. The default is SNAPPY.",
            "StripeSizeBytes" : "The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.",
            "BloomFilterColumns" : [ "string" ],
            "EnablePadding" : "Set this to true to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is false.",
            "BloomFilterFalsePositiveProbability" : "The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.",
            "RowIndexStride" : "The number of rows between index entries. The default is 10,000 and the minimum is 1,000.",
            "FormatVersion" : "The version of the file to write. The possible values are V0_11 and V0_12. The default is V0_12.",
            "BlockSizeBytes" : "The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.",
            "DictionaryKeyThreshold" : "Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1."
          },
          "ParquetSerDe" : {
            "Compression" : "The compression code to use over data blocks. The possible values are UNCOMPRESSED, SNAPPY, and GZIP, with the default being SNAPPY. Use SNAPPY for higher decompression speed. Use GZIP if the compression ration is more important than speed.",
            "BlockSizeBytes" : "The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.",
            "PageSizeBytes" : "The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.",
            "EnableDictionaryCompression" : "Indicates whether to enable dictionary compression.",
            "MaxPaddingBytes" : "The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.",
            "WriterVersion" : "Indicates the version of row format to output. The possible values are V1 and V2. The default is V1."
          }
        }
      }
    },
    "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
    "ProcessingConfiguration" : {
      "Enabled" : "Enables or disables data processing.",
      "Processors" : [ {
        "Type" : "The type of processor.",
        "Parameters" : [ {
          "ParameterValue" : "The parameter value.",
          "ParameterName" : "The name of the parameter."
        } ]
      } ]
    },
    "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "CloudWatchLoggingOptions" : {
      "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
      "Enabled" : "Enables or disables CloudWatch logging.",
      "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
    },
    "S3BackupMode" : "The Amazon S3 backup mode."
  }
}
```

</details>

## delete_delivery_stream

Deletes a delivery stream and its data. 
You can delete a delivery stream only if it is in ACTIVE or DELETING state, and not in the CREATING state. While the deletion request is in process, the delivery stream is in the DELETING state. 
To check the state of a delivery stream, use DescribeDeliveryStream. 
While the delivery stream is DELETING state, the service might continue to accept the records, but it doesn't make any guarantees with respect to delivering the data. Therefore, as a best practice, you should first stop any applications that are sending records before deleting a delivery stream.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DeliveryStreamName" : "The name of the delivery stream."
}
```

</details>

## describe_delivery_stream

Describes the specified delivery stream and gets the status. For example, after your delivery stream is created, call DescribeDeliveryStream to see whether the delivery stream is ACTIVE and therefore ready for data to be sent to it.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ExclusiveStartDestinationId" : "The ID of the destination to start returning the destination information. Kinesis Data Firehose supports one destination per delivery stream.",
  "DeliveryStreamName" : "The name of the delivery stream.",
  "Limit" : "The limit on the number of destinations to return. You can have one destination per delivery stream."
}
```

</details>

## list_delivery_streams

Lists your delivery streams. 
The number of delivery streams might be too large to return using a single call to ListDeliveryStreams. You can limit the number of delivery streams returned, using the Limit parameter. To determine whether there are more delivery streams to list, check the value of HasMoreDeliveryStreams in the output. If there are more delivery streams to list, you can request them by specifying the name of the last delivery stream returned in the call in the ExclusiveStartDeliveryStreamName parameter of a subsequent call.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DeliveryStreamType" : "The delivery stream type. This can be one of the following values:  \n  DirectPut: Provider applications access the delivery stream directly.  \n  KinesisStreamAsSource: The delivery stream uses a Kinesis data stream as a source.   \nThis parameter is optional. If this parameter is omitted, delivery streams of all types are returned.",
  "Limit" : "The maximum number of delivery streams to list. The default value is 10.",
  "ExclusiveStartDeliveryStreamName" : "The name of the delivery stream to start the list with."
}
```

</details>

## list_tags_for_delivery_stream

Lists the tags for the specified delivery stream. This operation has a limit of five transactions per second per account. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ExclusiveStartTagKey" : "The key to use as the starting point for the list of tags. If you set this parameter, ListTagsForDeliveryStream gets all tags that occur after ExclusiveStartTagKey.",
  "DeliveryStreamName" : "The name of the delivery stream whose tags you want to list.",
  "Limit" : "The number of tags to return. If this number is less than the total number of tags associated with the delivery stream, HasMoreTags is set to true in the response. To list additional tags, set ExclusiveStartTagKey to the last key in the response. "
}
```

</details>

## put_record

Writes a single data record into an Amazon Kinesis Data Firehose delivery stream. To write multiple data records into a delivery stream, use PutRecordBatch. Applications using these operations are referred to as producers. 
By default, each delivery stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. If you use PutRecord and PutRecordBatch, the limits are an aggregate across these two operations for each delivery stream. For more information about limits and how to request an increase, see Amazon Kinesis Data Firehose Limits.  
You must specify the name of the delivery stream and the data record when using PutRecord. The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data. For example, it can be a segment from a log file, geographic location data, website clickstream data, and so on. 
Kinesis Data Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (\n) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination. 
The PutRecord operation returns a RecordId, which is a unique string assigned to each record. Producer applications can use this ID for purposes such as auditability and investigation. 
If the PutRecord operation throws a ServiceUnavailableException, back off and retry. If the exception persists, it is possible that the throughput limits have been exceeded for the delivery stream.  
Data records sent to Kinesis Data Firehose are stored for 24 hours from the time they are added to a delivery stream as it tries to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DeliveryStreamName" : "The name of the delivery stream.",
  "Record" : {
    "Data" : "The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KB."
  }
}
```

</details>

## put_record_batch

Writes multiple data records into a delivery stream in a single call, which can achieve higher throughput per producer than when writing single records. To write single data records into a delivery stream, use PutRecord. Applications using these operations are referred to as producers. 
By default, each delivery stream can take in up to 2,000 transactions per second, 5,000 records per second, or 5 MB per second. If you use PutRecord and PutRecordBatch, the limits are an aggregate across these two operations for each delivery stream. For more information about limits, see Amazon Kinesis Data Firehose Limits. 
Each PutRecordBatch request supports up to 500 records. Each record in the request can be as large as 1,000 KB (before 64-bit encoding), up to a limit of 4 MB for the entire request. These limits cannot be changed. 
You must specify the name of the delivery stream and the data record when using PutRecord. The data record consists of a data blob that can be up to 1,000 KB in size, and any kind of data. For example, it could be a segment from a log file, geographic location data, website clickstream data, and so on. 
Kinesis Data Firehose buffers records before delivering them to the destination. To disambiguate the data blobs at the destination, a common solution is to use delimiters in the data, such as a newline (\n) or some other character unique within the data. This allows the consumer application to parse individual data items when reading the data from the destination. 
The PutRecordBatch response includes a count of failed records, FailedPutCount, and an array of responses, RequestResponses. Each entry in the RequestResponses array provides additional information about the processed record. It directly correlates with a record in the request array using the same ordering, from the top to the bottom. The response array always includes the same number of records as the request array. RequestResponses includes both successfully and unsuccessfully processed records. Kinesis Data Firehose tries to process all records in each PutRecordBatch request. A single record failure does not stop the processing of subsequent records. 
A successfully processed record includes a RecordId value, which is unique for the record. An unsuccessfully processed record includes ErrorCode and ErrorMessage values. ErrorCode reflects the type of error, and is one of the following values: ServiceUnavailable or InternalFailure. ErrorMessage provides more detailed information about the error. 
If there is an internal server error or a timeout, the write might have completed or it might have failed. If FailedPutCount is greater than 0, retry the request, resending only those records that might have failed processing. This minimizes the possible duplicate records and also reduces the total bytes sent (and corresponding charges). We recommend that you handle any duplicates at the destination. 
If PutRecordBatch throws ServiceUnavailableException, back off and retry. If the exception persists, it is possible that the throughput limits have been exceeded for the delivery stream. 
Data records sent to Kinesis Data Firehose are stored for 24 hours from the time they are added to a delivery stream as it attempts to send the records to the destination. If the destination is unreachable for more than 24 hours, the data is no longer available.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DeliveryStreamName" : "The name of the delivery stream.",
  "Records" : [ {
    "Data" : "The data blob, which is base64-encoded when the blob is serialized. The maximum size of the data blob, before base64-encoding, is 1,000 KB."
  } ]
}
```

</details>

## tag_delivery_stream

Adds or updates tags for the specified delivery stream. A tag is a key-value pair (the value is optional) that you can define and assign to AWS resources. If you specify a tag that already exists, the tag value is replaced with the value that you specify in the request. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the delivery stream. For more information about tags, see Using Cost Allocation Tags in the AWS Billing and Cost Management User Guide.  
 Each delivery stream can have up to 50 tags.  
 This operation has a limit of five transactions per second per account. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DeliveryStreamName" : "The name of the delivery stream to which you want to add the tags.",
  "Tags" : [ {
    "Value" : "An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @",
    "Key" : "A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @"
  } ]
}
```

</details>

## untag_delivery_stream

Removes tags from the specified delivery stream. Removed tags are deleted, and you can't recover them after this operation successfully completes. 
If you specify a tag that doesn't exist, the operation ignores it. 
This operation has a limit of five transactions per second per account. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "DeliveryStreamName" : "The name of the delivery stream.",
  "TagKeys" : [ "string" ]
}
```

</details>

## update_destination

Updates the specified destination of the specified delivery stream. 
Use this operation to change the destination type (for example, to replace the Amazon S3 destination with Amazon Redshift) or change the parameters associated with a destination (for example, to change the bucket name of the Amazon S3 destination). The update might not occur immediately. The target delivery stream remains active while the configurations are updated, so data writes to the delivery stream can continue during this process. The updated configurations are usually effective within a few minutes. 
Switching between Amazon ES and other services is not supported. For an Amazon ES destination, you can only update to another Amazon ES destination. 
If the destination type is the same, Kinesis Data Firehose merges the configuration parameters specified with the destination configuration that already exists on the delivery stream. If any of the parameters are not specified in the call, the existing values are retained. For example, in the Amazon S3 destination, if EncryptionConfiguration is not specified, then the existing EncryptionConfiguration is maintained on the destination. 
If the destination type is not the same, for example, changing the destination from Amazon S3 to Amazon Redshift, Kinesis Data Firehose does not merge any parameters. In this case, all parameters must be specified. 
Kinesis Data Firehose uses CurrentDeliveryStreamVersionId to avoid race conditions and conflicting merges. This is a required field, and the service updates the configuration only if the existing configuration has a version ID that matches. After the update is applied successfully, the version ID is updated, and can be retrieved using DescribeDeliveryStream. Use the new version ID to set CurrentDeliveryStreamVersionId in the next call.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "S3DestinationUpdate" : {
    "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "BufferingHints" : {
      "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
      "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
    },
    "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
    "EncryptionConfiguration" : {
      "KMSEncryptionConfig" : {
        "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
      },
      "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
    },
    "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
    "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "CloudWatchLoggingOptions" : {
      "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
      "Enabled" : "Enables or disables CloudWatch logging.",
      "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
    }
  },
  "ElasticsearchDestinationUpdate" : {
    "IndexName" : "The Elasticsearch index name.",
    "TypeName" : "The Elasticsearch type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Kinesis Data Firehose returns an error during runtime.",
    "BufferingHints" : {
      "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).",
      "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
    },
    "IndexRotationPeriod" : "The Elasticsearch index rotation period. Index rotation appends a time stamp to IndexName to facilitate the expiration of old data. For more information, see Index Rotation for the Amazon ES Destination. Default value is&nbsp;OneDay.",
    "RetryOptions" : {
      "DurationInSeconds" : "After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries."
    },
    "ProcessingConfiguration" : {
      "Enabled" : "Enables or disables data processing.",
      "Processors" : [ {
        "Type" : "The type of processor.",
        "Parameters" : [ {
          "ParameterValue" : "The parameter value.",
          "ParameterName" : "The name of the parameter."
        } ]
      } ]
    },
    "S3Update" : {
      "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "BufferingHints" : {
        "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
        "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
      },
      "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
      "EncryptionConfiguration" : {
        "KMSEncryptionConfig" : {
          "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
        },
        "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
      },
      "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
      "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "CloudWatchLoggingOptions" : {
        "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
        "Enabled" : "Enables or disables CloudWatch logging.",
        "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
      }
    },
    "RoleARN" : "The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see Grant Kinesis Data Firehose Access to an Amazon S3 Destination and Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "DomainARN" : "The ARN of the Amazon ES domain. The IAM role must have permissions for&nbsp;DescribeElasticsearchDomain, DescribeElasticsearchDomains, and DescribeElasticsearchDomainConfig&nbsp;after assuming the IAM role specified in RoleARN. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "CloudWatchLoggingOptions" : {
      "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
      "Enabled" : "Enables or disables CloudWatch logging.",
      "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
    }
  },
  "CurrentDeliveryStreamVersionId" : "Obtain this value from the VersionId result of DeliveryStreamDescription. This value is required, and helps the service perform conditional operations. For example, if there is an interleaving update and this value is null, then the update destination fails. After the update is successful, the VersionId value is updated. The service then performs a merge of the old configuration with the new configuration.",
  "RedshiftDestinationUpdate" : {
    "Username" : "The name of the user.",
    "CopyCommand" : {
      "DataTableName" : "The name of the target table. The table must already exist in the database.",
      "DataTableColumns" : "A comma-separated list of column names.",
      "CopyOptions" : "Optional parameters to use with the Amazon Redshift COPY command. For more information, see the \"Optional Parameters\" section of Amazon Redshift COPY command. Some possible examples that would apply to Kinesis Data Firehose are as follows: \n delimiter '\\t' lzop; - fields are delimited with \"\\t\" (TAB character) and compressed using lzop. \n delimiter '|' - fields are delimited with \"|\" (this is the default delimiter). \n delimiter '|' escape - the delimiter should be escaped. \n fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6' - fields are fixed width in the source, with each width specified after every column in the table. \n JSON 's3://mybucket/jsonpaths.txt' - data is in JSON format, and the path specified is the format of the data. \nFor more examples, see Amazon Redshift COPY command examples."
    },
    "RetryOptions" : {
      "DurationInSeconds" : "The length of time during which Kinesis Data Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Kinesis Data Firehose does not retry if the value of DurationInSeconds is 0 (zero) or if the first delivery attempt takes longer than the current value."
    },
    "S3BackupUpdate" : {
      "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "BufferingHints" : {
        "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
        "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
      },
      "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
      "EncryptionConfiguration" : {
        "KMSEncryptionConfig" : {
          "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
        },
        "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
      },
      "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
      "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "CloudWatchLoggingOptions" : {
        "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
        "Enabled" : "Enables or disables CloudWatch logging.",
        "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
      }
    },
    "ProcessingConfiguration" : {
      "Enabled" : "Enables or disables data processing.",
      "Processors" : [ {
        "Type" : "The type of processor.",
        "Parameters" : [ {
          "ParameterValue" : "The parameter value.",
          "ParameterName" : "The name of the parameter."
        } ]
      } ]
    },
    "S3Update" : {
      "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "BufferingHints" : {
        "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
        "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
      },
      "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
      "EncryptionConfiguration" : {
        "KMSEncryptionConfig" : {
          "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
        },
        "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
      },
      "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
      "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "CloudWatchLoggingOptions" : {
        "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
        "Enabled" : "Enables or disables CloudWatch logging.",
        "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
      }
    },
    "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "ClusterJDBCURL" : "The database connection string.",
    "CloudWatchLoggingOptions" : {
      "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
      "Enabled" : "Enables or disables CloudWatch logging.",
      "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
    },
    "Password" : "The user password.",
    "S3BackupMode" : "The Amazon S3 backup mode."
  },
  "ExtendedS3DestinationUpdate" : {
    "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "BufferingHints" : {
      "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
      "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
    },
    "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. ",
    "EncryptionConfiguration" : {
      "KMSEncryptionConfig" : {
        "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
      },
      "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
    },
    "DataFormatConversionConfiguration" : {
      "InputFormatConfiguration" : {
        "Deserializer" : {
          "HiveJsonSerDe" : {
            "TimestampFormats" : [ "string" ]
          },
          "OpenXJsonSerDe" : {
            "ConvertDotsInJsonKeysToUnderscores" : "When set to true, specifies that the names of the keys include dots and that you want Kinesis Data Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is \"a.b\", you can define the column name to be \"a_b\" when using this option. \nThe default is false.",
            "ColumnToJsonKeyMappings" : "Maps column names to JSON keys that aren't identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, timestamp is a Hive keyword. If you have a JSON key named timestamp, set this parameter to {\"ts\": \"timestamp\"} to map this key to a column named ts.",
            "CaseInsensitive" : "When set to true, which is the default, Kinesis Data Firehose converts JSON keys to lowercase before deserializing them."
          }
        }
      },
      "Enabled" : "Defaults to true. Set it to false if you want to disable format conversion while preserving the configuration details.",
      "SchemaConfiguration" : {
        "VersionId" : "Specifies the table version for the output data schema. If you don't specify this version ID, or if you set it to LATEST, Kinesis Data Firehose uses the most recent version. This means that any updates to the table are automatically picked up.",
        "TableName" : "Specifies the AWS Glue table that contains the column information that constitutes your data schema.",
        "DatabaseName" : "Specifies the name of the AWS Glue database that contains the schema for the output data.",
        "Region" : "If you don't specify an AWS Region, the default is the current Region.",
        "CatalogId" : "The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used by default.",
        "RoleARN" : "The role that Kinesis Data Firehose can use to access AWS Glue. This role must be in the same account you use for Kinesis Data Firehose. Cross-account roles aren't allowed."
      },
      "OutputFormatConfiguration" : {
        "Serializer" : {
          "OrcSerDe" : {
            "PaddingTolerance" : "A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size. \nFor the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. \nKinesis Data Firehose ignores this parameter when OrcSerDe$EnablePadding is false.",
            "Compression" : "The compression code to use over data blocks. The default is SNAPPY.",
            "StripeSizeBytes" : "The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.",
            "BloomFilterColumns" : [ "string" ],
            "EnablePadding" : "Set this to true to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is false.",
            "BloomFilterFalsePositiveProbability" : "The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.",
            "RowIndexStride" : "The number of rows between index entries. The default is 10,000 and the minimum is 1,000.",
            "FormatVersion" : "The version of the file to write. The possible values are V0_11 and V0_12. The default is V0_12.",
            "BlockSizeBytes" : "The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.",
            "DictionaryKeyThreshold" : "Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1."
          },
          "ParquetSerDe" : {
            "Compression" : "The compression code to use over data blocks. The possible values are UNCOMPRESSED, SNAPPY, and GZIP, with the default being SNAPPY. Use SNAPPY for higher decompression speed. Use GZIP if the compression ration is more important than speed.",
            "BlockSizeBytes" : "The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Kinesis Data Firehose uses this value for padding calculations.",
            "PageSizeBytes" : "The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.",
            "EnableDictionaryCompression" : "Indicates whether to enable dictionary compression.",
            "MaxPaddingBytes" : "The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.",
            "WriterVersion" : "Indicates the version of row format to output. The possible values are V1 and V2. The default is V1."
          }
        }
      }
    },
    "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
    "S3BackupUpdate" : {
      "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "BufferingHints" : {
        "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
        "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
      },
      "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
      "EncryptionConfiguration" : {
        "KMSEncryptionConfig" : {
          "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
        },
        "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
      },
      "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
      "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "CloudWatchLoggingOptions" : {
        "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
        "Enabled" : "Enables or disables CloudWatch logging.",
        "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
      }
    },
    "ProcessingConfiguration" : {
      "Enabled" : "Enables or disables data processing.",
      "Processors" : [ {
        "Type" : "The type of processor.",
        "Parameters" : [ {
          "ParameterValue" : "The parameter value.",
          "ParameterName" : "The name of the parameter."
        } ]
      } ]
    },
    "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
    "CloudWatchLoggingOptions" : {
      "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
      "Enabled" : "Enables or disables CloudWatch logging.",
      "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
    },
    "S3BackupMode" : "Enables or disables Amazon S3 backup mode."
  },
  "DeliveryStreamName" : "The name of the delivery stream.",
  "SplunkDestinationUpdate" : {
    "HECEndpoint" : "The HTTP Event Collector (HEC) endpoint to which Kinesis Data Firehose sends your data.",
    "HECToken" : "A GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.",
    "RetryOptions" : {
      "DurationInSeconds" : "The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn't include the periods during which Kinesis Data Firehose waits for acknowledgment from Splunk after each attempt."
    },
    "HECEndpointType" : "This type can be either \"Raw\" or \"Event.\"",
    "HECAcknowledgmentTimeoutInSeconds" : "The amount of time that Kinesis Data Firehose waits to receive an acknowledgment from Splunk after it sends data. At the end of the timeout period, Kinesis Data Firehose either tries to send the data again or considers it an error, based on your retry settings.",
    "ProcessingConfiguration" : {
      "Enabled" : "Enables or disables data processing.",
      "Processors" : [ {
        "Type" : "The type of processor.",
        "Parameters" : [ {
          "ParameterValue" : "The parameter value.",
          "ParameterName" : "The name of the parameter."
        } ]
      } ]
    },
    "S3Update" : {
      "BucketARN" : "The ARN of the S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "BufferingHints" : {
        "IntervalInSeconds" : "Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300.",
        "SizeInMBs" : "Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. \nWe recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher."
      },
      "CompressionFormat" : "The compression format. If no value is specified, the default is UNCOMPRESSED. \nThe compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket.",
      "EncryptionConfiguration" : {
        "KMSEncryptionConfig" : {
          "AWSKMSKeyARN" : "The Amazon Resource Name (ARN) of the encryption key. Must belong to the same AWS Region as the destination Amazon S3 bucket. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
        },
        "NoEncryptionConfig" : "Specifically override existing encryption information to ensure that no encryption is used."
      },
      "Prefix" : "The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can specify an extra prefix to be added in front of the time format prefix. If the prefix ends with a slash, it appears as a folder in the S3 bucket. For more information, see Amazon S3 Object Name Format in the Amazon Kinesis Data Firehose Developer Guide.",
      "RoleARN" : "The Amazon Resource Name (ARN) of the AWS credentials. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces.",
      "CloudWatchLoggingOptions" : {
        "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
        "Enabled" : "Enables or disables CloudWatch logging.",
        "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
      }
    },
    "CloudWatchLoggingOptions" : {
      "LogStreamName" : "The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.",
      "Enabled" : "Enables or disables CloudWatch logging.",
      "LogGroupName" : "The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled."
    },
    "S3BackupMode" : "Defines how documents should be delivered to Amazon S3. When set to FailedDocumentsOnly, Kinesis Data Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to AllDocuments, Kinesis Data Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is FailedDocumentsOnly. "
  },
  "DestinationId" : "The ID of the destination."
}
```

</details>

