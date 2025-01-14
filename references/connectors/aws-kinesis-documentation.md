---
id: aws-kinesis-documentation
title: AWS Kinesis (version v2.*.*)
sidebar_label: AWS Kinesis
layout: docs.mustache
---

## add_tags_to_stream

Adds or updates tags for the specified Kinesis data stream. Each time you invoke this operation, you can specify up to 10 tags. If you want to add more than 10 tags to your stream, you can invoke this operation multiple times. In total, each stream can have up to 50 tags. 
If tags have already been assigned to the stream, AddTagsToStream overwrites any existing tags that correspond to the specified tag keys. 
 AddTagsToStream has a limit of five transactions per second per account.

<details><summary>Parameters</summary>

### $body

Represents the input for AddTagsToStream.

**Type:** object

```json
{
  "StreamName" : "The name of the stream.",
  "Tags" : "A set of up to 10 key-value pairs to use to create the tags."
}
```

</details>

## create_stream

Creates a Kinesis data stream. A stream captures and transports data records that are continuously emitted from different data sources or producers. Scale-out within a stream is explicitly supported by means of shards, which are uniquely identified groups of data records in a stream. 
You specify and control the number of shards that a stream is composed of. Each shard can support reads up to five transactions per second, up to a maximum data read total of 2 MB per second. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second. If the amount of data input increases or decreases, you can add or remove shards. 
The stream name identifies the stream. The name is scoped to the AWS account used by the application. It is also scoped by AWS Region. That is, two streams in two different accounts can have the same name, and two streams in the same account, but in two different Regions, can have the same name. 
 CreateStream is an asynchronous operation. Upon receiving a CreateStream request, Kinesis Data Streams immediately returns and sets the stream status to CREATING. After the stream is created, Kinesis Data Streams sets the stream status to ACTIVE. You should perform read and write operations only on an ACTIVE stream.  
You receive a LimitExceededException when making a CreateStream request when you try to do one of the following:  
 Have more than five streams in the CREATING state at any point in time.  
 Create more shards than are authorized for your account.   
For the default shard limit for an AWS account, see Amazon Kinesis Data Streams Limits in the Amazon Kinesis Data Streams Developer Guide. To increase this limit, contact AWS Support. 
You can use DescribeStream to check the stream status, which is returned in StreamStatus. 
 CreateStream has a limit of five transactions per second per account.

<details><summary>Parameters</summary>

### $body

Represents the input for CreateStream.

**Type:** object

```json
{
  "StreamName" : "A name to identify the stream. The stream name is scoped to the AWS account used by the application that creates the stream. It is also scoped by AWS Region. That is, two streams in two different AWS accounts can have the same name. Two streams in the same AWS account but in two different Regions can also have the same name.",
  "ShardCount" : "The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput. \nDefaultShardLimit;"
}
```

</details>

## decrease_stream_retention_period

Decreases the Kinesis data stream's retention period, which is the length of time data records are accessible after they are added to the stream. The minimum value of a stream's retention period is 24 hours. 
This operation may result in lost data. For example, if the stream's retention period is 48 hours and is decreased to 24 hours, any data already in the stream that is older than 24 hours is inaccessible.

<details><summary>Parameters</summary>

### $body

Represents the input for DecreaseStreamRetentionPeriod.

**Type:** object

```json
{
  "StreamName" : "The name of the stream to modify.",
  "RetentionPeriodHours" : "The new retention period of the stream, in hours. Must be less than the current retention period."
}
```

</details>

## delete_stream

Deletes a Kinesis data stream and all its shards and data. You must shut down any applications that are operating on the stream before you delete the stream. If an application attempts to operate on a deleted stream, it receives the exception ResourceNotFoundException. 
If the stream is in the ACTIVE state, you can delete it. After a DeleteStream request, the specified stream is in the DELETING state until Kinesis Data Streams completes the deletion. 
 Note: Kinesis Data Streams might continue to accept data read and write operations, such as PutRecord, PutRecords, and GetRecords, on a stream in the DELETING state until the stream deletion is complete. 
When you delete a stream, any shards in that stream are also deleted, and any tags are dissociated from the stream. 
You can use the DescribeStream operation to check the state of the stream, which is returned in StreamStatus. 
 DeleteStream has a limit of five transactions per second per account.

<details><summary>Parameters</summary>

### $body

Represents the input for DeleteStream.

**Type:** object

```json
{
  "StreamName" : "The name of the stream to delete.",
  "EnforceConsumerDeletion" : "If this parameter is unset (null) or if you set it to false, and the stream has registered consumers, the call to DeleteStream fails with a ResourceInUseException. "
}
```

</details>

## deregister_stream_consumer

To deregister a consumer, provide its ARN. Alternatively, you can provide the ARN of the data stream and the name you gave the consumer when you registered it. You may also provide all three parameters, as long as they don't conflict with each other. If you don't know the name or ARN of the consumer that you want to deregister, you can use the ListStreamConsumers operation to get a list of the descriptions of all the consumers that are currently registered with a given data stream. The description of a consumer contains its name and ARN. 
This operation has a limit of five transactions per second per account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ConsumerName" : "The name that you gave to the consumer.",
  "ConsumerARN" : "The ARN returned by Kinesis Data Streams when you registered the consumer. If you don't know the ARN of the consumer that you want to deregister, you can use the ListStreamConsumers operation to get a list of the descriptions of all the consumers that are currently registered with a given data stream. The description of a consumer contains its ARN.",
  "StreamARN" : "The ARN of the Kinesis data stream that the consumer is registered with. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
}
```

</details>

## describe_limits

Describes the shard limits and usage for the account. 
If you update your account limits, the old limits might be returned for a few minutes. 
This operation has a limit of one transaction per second per account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## describe_stream

Describes the specified Kinesis data stream. 
The information returned includes the stream name, Amazon Resource Name (ARN), creation time, enhanced metric configuration, and shard map. The shard map is an array of shard objects. For each shard object, there is the hash key and sequence number ranges that the shard spans, and the IDs of any earlier shards that played in a role in creating the shard. Every record ingested in the stream is identified by a sequence number, which is assigned when the record is put into the stream. 
You can limit the number of shards returned by each call. For more information, see Retrieving Shards from a Stream in the Amazon Kinesis Data Streams Developer Guide. 
There are no guarantees about the chronological order shards returned. To process shards in chronological order, use the ID of the parent shard to track the lineage to the oldest shard. 
This operation has a limit of 10 transactions per second per account.

<details><summary>Parameters</summary>

### $body

Represents the input for DescribeStream.

**Type:** object

```json
{
  "StreamName" : "The name of the stream to describe."
}
```

</details>

## describe_stream_consumer

To get the description of a registered consumer, provide the ARN of the consumer. Alternatively, you can provide the ARN of the data stream and the name you gave the consumer when you registered it. You may also provide all three parameters, as long as they don't conflict with each other. If you don't know the name or ARN of the consumer that you want to describe, you can use the ListStreamConsumers operation to get a list of the descriptions of all the consumers that are currently registered with a given data stream. 
This operation has a limit of 20 transactions per second per account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ConsumerName" : "The name that you gave to the consumer.",
  "ConsumerARN" : "The ARN returned by Kinesis Data Streams when you registered the consumer.",
  "StreamARN" : "The ARN of the Kinesis data stream that the consumer is registered with. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
}
```

</details>

## describe_stream_summary

Provides a summarized description of the specified Kinesis data stream without the shard list. 
The information returned includes the stream name, Amazon Resource Name (ARN), status, record retention period, approximate creation time, monitoring, encryption details, and open shard count. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "StreamName" : "The name of the stream to describe."
}
```

</details>

## disable_enhanced_monitoring

Disables enhanced monitoring.

<details><summary>Parameters</summary>

### $body

Represents the input for DisableEnhancedMonitoring.

**Type:** object

```json
{
  "ShardLevelMetrics" : [ "string. Possible values: IncomingBytes | IncomingRecords | OutgoingBytes | OutgoingRecords | WriteProvisionedThroughputExceeded | ReadProvisionedThroughputExceeded | IteratorAgeMilliseconds | ALL" ],
  "StreamName" : "The name of the Kinesis data stream for which to disable enhanced monitoring."
}
```

</details>

## enable_enhanced_monitoring

Enables enhanced Kinesis data stream monitoring for shard-level metrics.

<details><summary>Parameters</summary>

### $body

Represents the input for EnableEnhancedMonitoring.

**Type:** object

```json
{
  "ShardLevelMetrics" : [ "string. Possible values: IncomingBytes | IncomingRecords | OutgoingBytes | OutgoingRecords | WriteProvisionedThroughputExceeded | ReadProvisionedThroughputExceeded | IteratorAgeMilliseconds | ALL" ],
  "StreamName" : "The name of the stream for which to enable enhanced monitoring."
}
```

</details>

## get_records

Gets data records from a Kinesis data stream's shard. 
Specify a shard iterator using the ShardIterator parameter. The shard iterator specifies the position in the shard from which you want to start reading data records sequentially. If there are no records available in the portion of the shard that the iterator points to, GetRecords returns an empty list. It might take multiple calls to get to a portion of the shard that contains records. 
You can scale by provisioning multiple shards per stream while considering service limits (for more information, see Amazon Kinesis Data Streams Limits in the Amazon Kinesis Data Streams Developer Guide). Your application should have one thread per shard, each reading continuously from its stream. To read from a stream continually, call GetRecords in a loop. Use GetShardIterator to get the shard iterator to specify in the first GetRecords call. GetRecords returns a new shard iterator in NextShardIterator. Specify the shard iterator returned in NextShardIterator in subsequent calls to GetRecords. If the shard has been closed, the shard iterator can't return more data and GetRecords returns null in NextShardIterator. You can terminate the loop when the shard is closed, or when the shard iterator reaches the record with the sequence number or other attribute that marks it as the last record to process. 
Each data record can be up to 1 MiB in size, and each shard can read up to 2 MiB per second. You can ensure that your calls don't exceed the maximum supported size or throughput by using the Limit parameter to specify the maximum number of records that GetRecords can return. Consider your average record size when determining this limit. The maximum number of records that can be returned per call is 10,000. 
The size of the data returned by GetRecords varies depending on the utilization of the shard. The maximum size of data that GetRecords can return is 10 MiB. If a call returns this amount of data, subsequent calls made within the next 5 seconds throw ProvisionedThroughputExceededException. If there is insufficient provisioned throughput on the stream, subsequent calls made within the next 1 second throw ProvisionedThroughputExceededException. GetRecords doesn't return any data when it throws an exception. For this reason, we recommend that you wait 1 second between calls to GetRecords. However, it's possible that the application will get exceptions for longer than 1 second. 
To detect whether the application is falling behind in processing, you can use the MillisBehindLatest response attribute. You can also monitor the stream using CloudWatch metrics and other mechanisms (see Monitoring in the Amazon Kinesis Data Streams Developer Guide). 
Each Amazon Kinesis record includes a value, ApproximateArrivalTimestamp, that is set when a stream successfully receives and stores a record. This is commonly referred to as a server-side time stamp, whereas a client-side time stamp is set when a data producer creates or sends the record to a stream (a data producer is any data source putting data records into a stream, for example with PutRecords). The time stamp has millisecond precision. There are no guarantees about the time stamp accuracy, or that the time stamp is always increasing. For example, records in a shard or across a stream might have time stamps that are out of order. 
This operation has a limit of five transactions per second per account.

<details><summary>Parameters</summary>

### $body

Represents the input for GetRecords.

**Type:** object

```json
{
  "ShardIterator" : "The position in the shard from which you want to start sequentially reading data records. A shard iterator specifies this position using the sequence number of a data record in the shard.",
  "Limit" : "The maximum number of records to return. Specify a value of up to 10,000. If you specify a value that is greater than 10,000, GetRecords throws InvalidArgumentException."
}
```

</details>

## get_shard_iterator

Gets an Amazon Kinesis shard iterator. A shard iterator expires 5 minutes after it is returned to the requester. 
A shard iterator specifies the shard position from which to start reading data records sequentially. The position is specified using the sequence number of a data record in a shard. A sequence number is the identifier associated with every record ingested in the stream, and is assigned when a record is put into the stream. Each stream has one or more shards. 
You must specify the shard iterator type. For example, you can set the ShardIteratorType parameter to read exactly from the position denoted by a specific sequence number by using the AT_SEQUENCE_NUMBER shard iterator type. Alternatively, the parameter can read right after the sequence number by using the AFTER_SEQUENCE_NUMBER shard iterator type, using sequence numbers returned by earlier calls to PutRecord, PutRecords, GetRecords, or DescribeStream. In the request, you can specify the shard iterator type AT_TIMESTAMP to read records from an arbitrary point in time, TRIM_HORIZON to cause ShardIterator to point to the last untrimmed record in the shard in the system (the oldest data record in the shard), or LATEST so that you always read the most recent data in the shard.  
When you read repeatedly from a stream, use a GetShardIterator request to get the first shard iterator for use in your first GetRecords request and for subsequent reads use the shard iterator returned by the GetRecords request in NextShardIterator. A new shard iterator is returned by every GetRecords request in NextShardIterator, which you use in the ShardIterator parameter of the next GetRecords request.  
If a GetShardIterator request is made too often, you receive a ProvisionedThroughputExceededException. For more information about throughput limits, see GetRecords, and Streams Limits in the Amazon Kinesis Data Streams Developer Guide. 
If the shard is closed, GetShardIterator returns a valid iterator for the last sequence number of the shard. A shard can be closed as a result of using SplitShard or MergeShards. 
 GetShardIterator has a limit of five transactions per second per account per open shard.

<details><summary>Parameters</summary>

### $body

Represents the input for GetShardIterator.

**Type:** object

```json
{
  "ShardId" : "The shard ID of the Kinesis Data Streams shard to get the iterator for.",
  "StartingSequenceNumber" : "The sequence number of the data record in the shard from which to start reading. Used with shard iterator type AT_SEQUENCE_NUMBER and AFTER_SEQUENCE_NUMBER.",
  "ShardIteratorType" : "Determines how the shard iterator is used to start reading data records from the shard. \nThe following are the valid Amazon Kinesis shard iterator types:  \n AT_SEQUENCE_NUMBER - Start reading from the position denoted by a specific sequence number, provided in the value StartingSequenceNumber.  \n AFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number, provided in the value StartingSequenceNumber.  \n AT_TIMESTAMP - Start reading from the position denoted by a specific time stamp, provided in the value Timestamp.  \n TRIM_HORIZON - Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard.  \n LATEST - Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard. ",
  "StreamName" : "The name of the Amazon Kinesis data stream.",
  "Timestamp" : "The time stamp of the data record from which to start reading. Used with shard iterator type AT_TIMESTAMP. A time stamp is the Unix epoch date with precision in milliseconds. For example, 2016-04-04T19:58:46.480-00:00 or 1459799926.480. If a record with this exact time stamp does not exist, the iterator returned is for the next (later) record. If the time stamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON)."
}
```

</details>

## increase_stream_retention_period

Increases the Kinesis data stream's retention period, which is the length of time data records are accessible after they are added to the stream. The maximum value of a stream's retention period is 168 hours (7 days). 
If you choose a longer stream retention period, this operation increases the time period during which records that have not yet expired are accessible. However, it does not make previous, expired data (older than the stream's previous retention period) accessible after the operation has been called. For example, if a stream's retention period is set to 24 hours and is increased to 168 hours, any data that is older than 24 hours remains inaccessible to consumer applications.

<details><summary>Parameters</summary>

### $body

Represents the input for IncreaseStreamRetentionPeriod.

**Type:** object

```json
{
  "StreamName" : "The name of the stream to modify.",
  "RetentionPeriodHours" : "The new retention period of the stream, in hours. Must be more than the current retention period."
}
```

</details>

## list_shards

Lists the shards in a stream and provides information about each shard. This operation has a limit of 100 transactions per second per data stream.  
This API is a new operation that is used by the Amazon Kinesis Client Library (KCL). If you have a fine-grained IAM policy that only allows specific operations, you must update your policy to allow calls to this API. For more information, see Controlling Access to Amazon Kinesis Data Streams Resources Using IAM.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "StreamName" : "The name of the data stream whose shards you want to list.  \nYou cannot specify this parameter if you specify the NextToken parameter.",
  "NextToken" : "When the number of shards in the data stream is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of shards in the data stream, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListShards to list the next set of shards. \nDon't specify StreamName or StreamCreationTimestamp if you specify NextToken because the latter unambiguously identifies the stream. \nYou can optionally specify a value for the MaxResults parameter when you specify NextToken. If you specify a MaxResults value that is less than the number of shards that the operation returns if you don't specify MaxResults, the response will contain a new NextToken value. You can use the new NextToken value in a subsequent call to the ListShards operation.  \nTokens expire after 300 seconds. When you obtain a value for NextToken in the response to a call to ListShards, you have 300 seconds to use that value. If you specify an expired token in a call to ListShards, you get ExpiredNextTokenException.",
  "StreamCreationTimestamp" : "Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the shards for. \nYou cannot specify this parameter if you specify the NextToken parameter.",
  "ExclusiveStartShardId" : "Specify this parameter to indicate that you want to list the shards starting with the shard whose ID immediately follows ExclusiveStartShardId. \nIf you don't specify this parameter, the default behavior is for ListShards to list the shards starting with the first one in the stream. \nYou cannot specify this parameter if you specify NextToken.",
  "MaxResults" : "The maximum number of shards to return in a single call to ListShards. The minimum value you can specify for this parameter is 1, and the maximum is 1,000, which is also the default. \nWhen the number of shards to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListShards to list the next set of shards."
}
```

</details>

## list_stream_consumers

Lists the consumers registered to receive data from a stream using enhanced fan-out, and provides information about each consumer. 
This operation has a limit of 10 transactions per second per account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "NextToken" : "When the number of consumers that are registered with the data stream is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of consumers that are registered with the data stream, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListStreamConsumers to list the next set of registered consumers. \nDon't specify StreamName or StreamCreationTimestamp if you specify NextToken because the latter unambiguously identifies the stream. \nYou can optionally specify a value for the MaxResults parameter when you specify NextToken. If you specify a MaxResults value that is less than the number of consumers that the operation returns if you don't specify MaxResults, the response will contain a new NextToken value. You can use the new NextToken value in a subsequent call to the ListStreamConsumers operation to list the next set of consumers.  \nTokens expire after 300 seconds. When you obtain a value for NextToken in the response to a call to ListStreamConsumers, you have 300 seconds to use that value. If you specify an expired token in a call to ListStreamConsumers, you get ExpiredNextTokenException.",
  "StreamCreationTimestamp" : "Specify this input parameter to distinguish data streams that have the same name. For example, if you create a data stream and then delete it, and you later create another data stream with the same name, you can use this input parameter to specify which of the two streams you want to list the consumers for.  \nYou can't specify this parameter if you specify the NextToken parameter. ",
  "MaxResults" : "The maximum number of consumers that you want a single call of ListStreamConsumers to return.",
  "StreamARN" : "The ARN of the Kinesis data stream for which you want to list the registered consumers. For more information, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
}
```

</details>

## list_streams

Lists your Kinesis data streams. 
The number of streams may be too large to return from a single call to ListStreams. You can limit the number of returned streams using the Limit parameter. If you do not specify a value for the Limit parameter, Kinesis Data Streams uses the default limit, which is currently 10. 
You can detect if there are more streams available to list by using the HasMoreStreams flag from the returned output. If there are more streams available, you can request more streams by using the name of the last stream returned by the ListStreams request in the ExclusiveStartStreamName parameter in a subsequent request to ListStreams. The group of stream names returned by the subsequent request is then added to the list. You can continue this process until all the stream names have been collected in the list.  
 ListStreams has a limit of five transactions per second per account.

*This operation has no parameters*

## list_tags_for_stream

Lists the tags for the specified Kinesis data stream. This operation has a limit of five transactions per second per account.

<details><summary>Parameters</summary>

### $body

Represents the input for ListTagsForStream.

**Type:** object

```json
{
  "StreamName" : "The name of the stream.",
  "ExclusiveStartTagKey" : "The key to use as the starting point for the list of tags. If this parameter is set, ListTagsForStream gets all tags that occur after ExclusiveStartTagKey. ",
  "Limit" : "The number of tags to return. If this number is less than the total number of tags associated with the stream, HasMoreTags is set to true. To list additional tags, set ExclusiveStartTagKey to the last key in the response."
}
```

</details>

## merge_shards

Merges two adjacent shards in a Kinesis data stream and combines them into a single shard to reduce the stream's capacity to ingest and transport data. Two shards are considered adjacent if the union of the hash key ranges for the two shards form a contiguous set with no gaps. For example, if you have two shards, one with a hash key range of 276...381 and the other with a hash key range of 382...454, then you could merge these two shards into a single shard that would have a hash key range of 276...454. After the merge, the single child shard receives data for all hash key values covered by the two parent shards. 
 MergeShards is called when there is a need to reduce the overall capacity of a stream because of excess capacity that is not being used. You must specify the shard to be merged and the adjacent shard for a stream. For more information about merging shards, see Merge Two Shards in the Amazon Kinesis Data Streams Developer Guide. 
If the stream is in the ACTIVE state, you can call MergeShards. If a stream is in the CREATING, UPDATING, or DELETING state, MergeShards returns a ResourceInUseException. If the specified stream does not exist, MergeShards returns a ResourceNotFoundException.  
You can use DescribeStream to check the state of the stream, which is returned in StreamStatus. 
 MergeShards is an asynchronous operation. Upon receiving a MergeShards request, Amazon Kinesis Data Streams immediately returns a response and sets the StreamStatus to UPDATING. After the operation is completed, Kinesis Data Streams sets the StreamStatus to ACTIVE. Read and write operations continue to work while the stream is in the UPDATING state.  
You use DescribeStream to determine the shard IDs that are specified in the MergeShards request.  
If you try to operate on too many streams in parallel using CreateStream, DeleteStream, MergeShards, or SplitShard, you receive a LimitExceededException.  
 MergeShards has a limit of five transactions per second per account.

<details><summary>Parameters</summary>

### $body

Represents the input for MergeShards.

**Type:** object

```json
{
  "StreamName" : "The name of the stream for the merge.",
  "AdjacentShardToMerge" : "The shard ID of the adjacent shard for the merge.",
  "ShardToMerge" : "The shard ID of the shard to combine with the adjacent shard for the merge."
}
```

</details>

## put_record

Writes a single data record into an Amazon Kinesis data stream. Call PutRecord to send data into the stream for real-time ingestion and subsequent processing, one record at a time. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second. 
You must specify the name of the stream that captures, stores, and transports the data; a partition key; and the data blob itself. 
The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on. 
The partition key is used by Kinesis Data Streams to distribute data across shards. Kinesis Data Streams segregates the data records that belong to a stream into multiple shards, using the partition key associated with each data record to determine the shard to which a given data record belongs. 
Partition keys are Unicode strings, with a maximum length limit of 256 characters for each key. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards using the hash key ranges of the shards. You can override hashing the partition key to determine the shard by explicitly specifying a hash value using the ExplicitHashKey parameter. For more information, see Adding Data to a Stream in the Amazon Kinesis Data Streams Developer Guide. 
 PutRecord returns the shard ID of where the data record was placed and the sequence number that was assigned to the data record. 
Sequence numbers increase over time and are specific to a shard within a stream, not across all shards within a stream. To guarantee strictly increasing ordering, write serially to a shard and use the SequenceNumberForOrdering parameter. For more information, see Adding Data to a Stream in the Amazon Kinesis Data Streams Developer Guide. 
If a PutRecord request cannot be processed because of insufficient provisioned throughput on the shard involved in the request, PutRecord throws ProvisionedThroughputExceededException.  
By default, data records are accessible for 24 hours from the time that they are added to a stream. You can use IncreaseStreamRetentionPeriod or DecreaseStreamRetentionPeriod to modify this retention period.

<details><summary>Parameters</summary>

### $body

Represents the input for PutRecord.

**Type:** object

```json
{
  "SequenceNumberForOrdering" : "Guarantees strictly increasing sequence numbers, for puts from the same client and to the same partition key. Usage: set the SequenceNumberForOrdering of record n to the sequence number of record n-1 (as returned in the result when putting record n-1). If this parameter is not set, records are coarsely ordered based on arrival time.",
  "StreamName" : "The name of the stream to put the data record into.",
  "ExplicitHashKey" : "The hash value used to explicitly determine the shard the data record is assigned to by overriding the partition key hash.",
  "PartitionKey" : "Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.",
  "Data" : "The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB)."
}
```

</details>

## put_records

Writes multiple data records into a Kinesis data stream in a single call (also referred to as a PutRecords request). Use this operation to send data into the stream for data ingestion and processing.  
Each PutRecords request can support up to 500 records. Each record in the request can be as large as 1 MB, up to a limit of 5 MB for the entire request, including partition keys. Each shard can support writes up to 1,000 records per second, up to a maximum data write total of 1 MB per second. 
You must specify the name of the stream that captures, stores, and transports the data; and an array of request Records, with each record in the array requiring a partition key and data blob. The record size limit applies to the total size of the partition key and data blob. 
The data blob can be any type of data; for example, a segment from a log file, geographic/location data, website clickstream data, and so on. 
The partition key is used by Kinesis Data Streams as input to a hash function that maps the partition key and associated data to a specific shard. An MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream. For more information, see Adding Data to a Stream in the Amazon Kinesis Data Streams Developer Guide. 
Each record in the Records array may include an optional parameter, ExplicitHashKey, which overrides the partition key to shard mapping. This parameter allows a data producer to determine explicitly the shard where the record is stored. For more information, see Adding Multiple Records with PutRecords in the Amazon Kinesis Data Streams Developer Guide. 
The PutRecords response includes an array of response Records. Each record in the response array directly correlates with a record in the request array using natural ordering, from the top to the bottom of the request and response. The response Records array always includes the same number of records as the request array. 
The response Records array includes both successfully and unsuccessfully processed records. Kinesis Data Streams attempts to process all records in each PutRecords request. A single record failure does not stop the processing of subsequent records. 
A successfully processed record includes ShardId and SequenceNumber values. The ShardId parameter identifies the shard in the stream where the record is stored. The SequenceNumber parameter is an identifier assigned to the put record, unique to all records in the stream. 
An unsuccessfully processed record includes ErrorCode and ErrorMessage values. ErrorCode reflects the type of error and can be one of the following values: ProvisionedThroughputExceededException or InternalFailure. ErrorMessage provides more detailed information about the ProvisionedThroughputExceededException exception including the account ID, stream name, and shard ID of the record that was throttled. For more information about partially successful responses, see Adding Multiple Records with PutRecords in the Amazon Kinesis Data Streams Developer Guide. 
By default, data records are accessible for 24 hours from the time that they are added to a stream. You can use IncreaseStreamRetentionPeriod or DecreaseStreamRetentionPeriod to modify this retention period.

<details><summary>Parameters</summary>

### $body

A PutRecords request.

**Type:** object

```json
{
  "StreamName" : "The stream name associated with the request.",
  "Records" : [ {
    "ExplicitHashKey" : "The hash value used to determine explicitly the shard that the data record is assigned to by overriding the partition key hash.",
    "PartitionKey" : "Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.",
    "Data" : "The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MB)."
  } ]
}
```

</details>

## register_stream_consumer

Registers a consumer with a Kinesis data stream. When you use this operation, the consumer you register can read data from the stream at a rate of up to 2 MiB per second. This rate is unaffected by the total number of consumers that read from the same stream. 
You can register up to 5 consumers per stream. A given consumer can only be registered with one stream. 
This operation has a limit of five transactions per second per account.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ConsumerName" : "For a given Kinesis data stream, each consumer must have a unique name. However, consumer names don't have to be unique across data streams.",
  "StreamARN" : "The ARN of the Kinesis data stream that you want to register the consumer with. For more info, see Amazon Resource Names (ARNs) and AWS Service Namespaces."
}
```

</details>

## remove_tags_from_stream

Removes tags from the specified Kinesis data stream. Removed tags are deleted and cannot be recovered after this operation successfully completes. 
If you specify a tag that does not exist, it is ignored. 
 RemoveTagsFromStream has a limit of five transactions per second per account.

<details><summary>Parameters</summary>

### $body

Represents the input for RemoveTagsFromStream.

**Type:** object

```json
{
  "StreamName" : "The name of the stream.",
  "TagKeys" : [ "string" ]
}
```

</details>

## split_shard

Splits a shard into two new shards in the Kinesis data stream, to increase the stream's capacity to ingest and transport data. SplitShard is called when there is a need to increase the overall capacity of a stream because of an expected increase in the volume of data records being ingested.  
You can also use SplitShard when a shard appears to be approaching its maximum utilization; for example, the producers sending data into the specific shard are suddenly sending more than previously anticipated. You can also call SplitShard to increase stream capacity, so that more Kinesis Data Streams applications can simultaneously read data from the stream for real-time processing.  
You must specify the shard to be split and the new hash key, which is the position in the shard where the shard gets split in two. In many cases, the new hash key might be the average of the beginning and ending hash key, but it can be any hash key value in the range being mapped into the shard. For more information, see Split a Shard in the Amazon Kinesis Data Streams Developer Guide. 
You can use DescribeStream to determine the shard ID and hash key values for the ShardToSplit and NewStartingHashKey parameters that are specified in the SplitShard request. 
 SplitShard is an asynchronous operation. Upon receiving a SplitShard request, Kinesis Data Streams immediately returns a response and sets the stream status to UPDATING. After the operation is completed, Kinesis Data Streams sets the stream status to ACTIVE. Read and write operations continue to work while the stream is in the UPDATING state.  
You can use DescribeStream to check the status of the stream, which is returned in StreamStatus. If the stream is in the ACTIVE state, you can call SplitShard. If a stream is in CREATING or UPDATING or DELETING states, DescribeStream returns a ResourceInUseException. 
If the specified stream does not exist, DescribeStream returns a ResourceNotFoundException. If you try to create more shards than are authorized for your account, you receive a LimitExceededException.  
For the default shard limit for an AWS account, see Kinesis Data Streams Limits in the Amazon Kinesis Data Streams Developer Guide. To increase this limit, contact AWS Support. 
If you try to operate on too many streams simultaneously using CreateStream, DeleteStream, MergeShards, and/or SplitShard, you receive a LimitExceededException.  
 SplitShard has a limit of five transactions per second per account.

<details><summary>Parameters</summary>

### $body

Represents the input for SplitShard.

**Type:** object

```json
{
  "StreamName" : "The name of the stream for the shard split.",
  "NewStartingHashKey" : "A hash key value for the starting hash key of one of the child shards created by the split. The hash key range for a given shard constitutes a set of ordered contiguous positive integers. The value for NewStartingHashKey must be in the range of hash keys being mapped into the shard. The NewStartingHashKey hash key value and all higher hash key values in hash key range are distributed to one of the child shards. All the lower hash key values in the range are distributed to the other child shard.",
  "ShardToSplit" : "The shard ID of the shard to split."
}
```

</details>

## start_stream_encryption

Enables or updates server-side encryption using an AWS KMS key for a specified stream.  
Starting encryption is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to UPDATING. After the update is complete, Kinesis Data Streams sets the status of the stream back to ACTIVE. Updating or applying encryption normally takes a few seconds to complete, but it can take minutes. You can continue to read and write data to your stream while its status is UPDATING. Once the status of the stream is ACTIVE, encryption begins for records written to the stream.  
API Limits: You can successfully apply a new AWS KMS key for server-side encryption 25 times in a rolling 24-hour period. 
Note: It can take up to 5 seconds after the stream is in an ACTIVE status before all records written to the stream are encrypted. After you enable encryption, you can verify that encryption is applied by inspecting the API response from PutRecord or PutRecords.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "EncryptionType" : "The encryption type to use. The only valid value is KMS.",
  "StreamName" : "The name of the stream for which to start encrypting records.",
  "KeyId" : "The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by \"alias/\".You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis.  \n Key ARN example: arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012   \n Alias ARN example: arn:aws:kms:us-east-1:123456789012:alias/MyAliasName   \n Globally unique key ID example: 12345678-1234-1234-1234-123456789012   \n Alias name example: alias/MyAliasName   \n Master key owned by Kinesis Data Streams: alias/aws/kinesis  "
}
```

</details>

## stop_stream_encryption

Disables server-side encryption for a specified stream.  
Stopping encryption is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to UPDATING. After the update is complete, Kinesis Data Streams sets the status of the stream back to ACTIVE. Stopping encryption normally takes a few seconds to complete, but it can take minutes. You can continue to read and write data to your stream while its status is UPDATING. Once the status of the stream is ACTIVE, records written to the stream are no longer encrypted by Kinesis Data Streams.  
API Limits: You can successfully disable server-side encryption 25 times in a rolling 24-hour period.  
Note: It can take up to 5 seconds after the stream is in an ACTIVE status before all records written to the stream are no longer subject to encryption. After you disabled encryption, you can verify that encryption is not applied by inspecting the API response from PutRecord or PutRecords.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "EncryptionType" : "The encryption type. The only valid value is KMS.",
  "StreamName" : "The name of the stream on which to stop encrypting records.",
  "KeyId" : "The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by \"alias/\".You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis.  \n Key ARN example: arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012   \n Alias ARN example: arn:aws:kms:us-east-1:123456789012:alias/MyAliasName   \n Globally unique key ID example: 12345678-1234-1234-1234-123456789012   \n Alias name example: alias/MyAliasName   \n Master key owned by Kinesis Data Streams: alias/aws/kinesis  "
}
```

</details>

## subscribe_to_shard

Call this operation from your consumer after you call RegisterStreamConsumer to register the consumer with Kinesis Data Streams. If the call succeeds, your consumer starts receiving events of type SubscribeToShardEvent for up to 5 minutes, after which time you need to call SubscribeToShard again to renew the subscription if you want to continue to receive records. 
You can make one call to SubscribeToShard per second per ConsumerARN. If your call succeeds, and then you call the operation again less than 5 seconds later, the second call generates a ResourceInUseException. If you call the operation a second time more than 5 seconds after the first call succeeds, the second call succeeds and the first connection gets shut down.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ShardId" : "The ID of the shard you want to subscribe to. To see a list of all the shards for a given stream, use ListShards.",
  "StartingPosition" : {
    "Type" : "Required string. Possible values: AT_SEQUENCE_NUMBER | AFTER_SEQUENCE_NUMBER | TRIM_HORIZON | LATEST | AT_TIMESTAMP",
    "SequenceNumber" : "string",
    "Timestamp" : "timestamp"
  },
  "ConsumerARN" : "For this parameter, use the value you obtained when you called RegisterStreamConsumer."
}
```

</details>

## update_shard_count

Updates the shard count of the specified stream to the specified number of shards. 
Updating the shard count is an asynchronous operation. Upon receiving the request, Kinesis Data Streams returns immediately and sets the status of the stream to UPDATING. After the update is complete, Kinesis Data Streams sets the status of the stream back to ACTIVE. Depending on the size of the stream, the scaling action could take a few minutes to complete. You can continue to read and write data to your stream while its status is UPDATING. 
To update the shard count, Kinesis Data Streams performs splits or merges on individual shards. This can cause short-lived shards to be created, in addition to the final shards. We recommend that you double or halve the shard count, as this results in the fewest number of splits or merges. 
This operation has the following default limits. By default, you cannot do the following:  
 Scale more than twice per rolling 24-hour period per stream  
 Scale up to more than double your current shard count for a stream  
 Scale down below half your current shard count for a stream  
 Scale up to more than 500 shards in a stream  
 Scale a stream with more than 500 shards down unless the result is less than 500 shards  
 Scale up to more than the shard limit for your account   
For the default limits for an AWS account, see Streams Limits in the Amazon Kinesis Data Streams Developer Guide. To request an increase in the call rate limit, the shard limit for this API, or your overall shard limit, use the limits form.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ScalingType" : "The scaling type. Uniform scaling creates shards of equal size.",
  "TargetShardCount" : "The new number of shards.",
  "StreamName" : "The name of the stream."
}
```

</details>

