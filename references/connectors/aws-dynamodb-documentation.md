---
id: aws-dynamodb-documentation
title: AWS DynamoDB (version v4.*.*)
sidebar_label: AWS DynamoDB
layout: docs.mustache
---

## batch_get_item

The BatchGetItem operation returns the attributes of one or more items from one or more tables. You identify requested items by primary key. 
A single operation can retrieve up to 16 MB of data, which can contain as many as 100 items. BatchGetItem will return a partial result if the response size limit is exceeded, the table's provisioned throughput is exceeded, or an internal processing failure occurs. If a partial result is returned, the operation returns a value for UnprocessedKeys. You can use this value to retry the operation starting with the next item to get.  
If you request more than 100 items BatchGetItem will return a ValidationException with the message "Too many items requested for the BatchGetItem call".  
For example, if you ask to retrieve 100 items, but each individual item is 300 KB in size, the system returns 52 items (so as not to exceed the 16 MB limit). It also returns an appropriate UnprocessedKeys value so you can get the next page of results. If desired, your application can include its own logic to assemble the pages of results into one data set. 
If none of the items can be processed due to insufficient provisioned throughput on all of the tables in the request, then BatchGetItem will return a ProvisionedThroughputExceededException. If at least one of the items is successfully processed, then BatchGetItem completes successfully, while returning the keys of the unread items in UnprocessedKeys.  
If DynamoDB returns any unprocessed items, you should retry the batch operation on those items. However, we strongly recommend that you use an exponential backoff algorithm. If you retry the batch operation immediately, the underlying read or write requests can still fail due to throttling on the individual tables. If you delay the batch operation using exponential backoff, the individual requests in the batch are much more likely to succeed. 
For more information, see Batch Operations and Error Handling in the Amazon DynamoDB Developer Guide.  
By default, BatchGetItem performs eventually consistent reads on every table in the request. If you want strongly consistent reads instead, you can set ConsistentRead to true for any or all tables. 
In order to minimize response latency, BatchGetItem retrieves items in parallel. 
When designing your application, keep in mind that DynamoDB does not return items in any particular order. To help parse the response by item, include the primary key values for the items in your request in the ProjectionExpression parameter. 
If a requested item does not exist, it is not returned in the result. Requests for nonexistent items consume the minimum read capacity units according to the type of read. For more information, see Capacity Units Calculations in the Amazon DynamoDB Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents the input of a BatchGetItem operation.

**Type:** object

```json
{
  "RequestItems" : "A map of one or more table names and, for each table, a map that describes one or more items to retrieve from that table. Each table name can be used only once per BatchGetItem request. \nEach element in the map of items to retrieve consists of the following:  \n  ConsistentRead - If true, a strongly consistent read is used; if false (the default), an eventually consistent read is used.  \n  ExpressionAttributeNames - One or more substitution tokens for attribute names in the ProjectionExpression parameter. The following are some use cases for using ExpressionAttributeNames:   To access an attribute whose name conflicts with a DynamoDB reserved word.   To create a placeholder for repeating occurrences of an attribute name in an expression.   To prevent special characters in an attribute name from being misinterpreted in an expression.   Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name:    Percentile    The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames:    {\"#P\":\"Percentile\"}    You could then use this substitution in an expression, as in this example:    #P = :val     Tokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime.  For more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.  \n  Keys - An array of primary key attribute values that define specific items in the table. For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide the partition key value. For a composite key, you must provide both the partition key value and the sort key value.  \n  ProjectionExpression - A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result. For more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.  \n  AttributesToGet - This is a legacy parameter. Use ProjectionExpression instead. For more information, see AttributesToGet in the Amazon DynamoDB Developer Guide.  ",
  "ReturnConsumedCapacity" : "string. Possible values: INDEXES | TOTAL | NONE"
}
```

</details>

## batch_write_item

The BatchWriteItem operation puts or deletes multiple items in one or more tables. A single call to BatchWriteItem can write up to 16 MB of data, which can comprise as many as 25 put or delete requests. Individual items to be written can be as large as 400 KB.  
 BatchWriteItem cannot update items. To update items, use the UpdateItem action.  
The individual PutItem and DeleteItem operations specified in BatchWriteItem are atomic; however BatchWriteItem as a whole is not. If any requested operations fail because the table's provisioned throughput is exceeded or an internal processing failure occurs, the failed operations are returned in the UnprocessedItems response parameter. You can investigate and optionally resend the requests. Typically, you would call BatchWriteItem in a loop. Each iteration would check for unprocessed items and submit a new BatchWriteItem request with those unprocessed items until all items have been processed. 
Note that if none of the items can be processed due to insufficient provisioned throughput on all of the tables in the request, then BatchWriteItem will return a ProvisionedThroughputExceededException.  
If DynamoDB returns any unprocessed items, you should retry the batch operation on those items. However, we strongly recommend that you use an exponential backoff algorithm. If you retry the batch operation immediately, the underlying read or write requests can still fail due to throttling on the individual tables. If you delay the batch operation using exponential backoff, the individual requests in the batch are much more likely to succeed. 
For more information, see Batch Operations and Error Handling in the Amazon DynamoDB Developer Guide.  
With BatchWriteItem, you can efficiently write or delete large amounts of data, such as from Amazon Elastic MapReduce (EMR), or copy data from another database into DynamoDB. In order to improve performance with these large-scale operations, BatchWriteItem does not behave in the same way as individual PutItem and DeleteItem calls would. For example, you cannot specify conditions on individual put and delete requests, and BatchWriteItem does not return deleted items in the response. 
If you use a programming language that supports concurrency, you can use threads to write items in parallel. Your application must include the necessary logic to manage the threads. With languages that don't support threading, you must update or delete the specified items one at a time. In both situations, BatchWriteItem performs the specified put and delete operations in parallel, giving you the power of the thread pool approach without having to introduce complexity into your application. 
Parallel processing reduces latency, but each specified put and delete request consumes the same number of write capacity units whether it is processed in parallel or not. Delete operations on nonexistent items consume one write capacity unit. 
If one or more of the following is true, DynamoDB rejects the entire batch write operation:  
 One or more tables specified in the BatchWriteItem request does not exist.  
 Primary key attributes specified on an item in the request do not match those in the corresponding table's primary key schema.  
 You try to perform multiple operations on the same item in the same BatchWriteItem request. For example, you cannot put and delete the same item in the same BatchWriteItem request.   
  Your request contains at least two items with identical hash and range keys (which essentially is two put operations).   
 There are more than 25 requests in the batch.  
 Any individual item in a batch exceeds 400 KB.  
 The total request size exceeds 16 MB. 

<details><summary>Parameters</summary>

### $body

Represents the input of a BatchWriteItem operation.

**Type:** object

```json
{
  "RequestItems" : "A map of one or more table names and, for each table, a list of operations to be performed (DeleteRequest or PutRequest). Each element in the map consists of the following:  \n  DeleteRequest - Perform a DeleteItem operation on the specified item. The item to be deleted is identified by a Key subelement:    Key - A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value. For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.    \n  PutRequest - Perform a PutItem operation on the specified item. The item to be put is identified by an Item subelement:    Item - A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values will be rejected with a ValidationException exception. If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table's attribute definition.   ",
  "ReturnConsumedCapacity" : "string. Possible values: INDEXES | TOTAL | NONE",
  "ReturnItemCollectionMetrics" : "Determines whether item collection metrics are returned. If set to SIZE, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned."
}
```

</details>

## create_backup

Creates a backup for an existing table. 
 Each time you create an On-Demand Backup, the entire table data is backed up. There is no limit to the number of on-demand backups that can be taken.  
 When you create an On-Demand Backup, a time marker of the request is cataloged, and the backup is created asynchronously, by applying all changes until the time of the request to the last full table snapshot. Backup requests are processed instantaneously and become available for restore within minutes.  
You can call CreateBackup at a maximum rate of 50 times per second. 
All backups in DynamoDB work without consuming any provisioned throughput on the table. 
 If you submit a backup request on 2018-12-14 at 14:25:00, the backup is guaranteed to contain all data committed to the table up to 14:24:00, and data committed after 14:26:00 will not be. The backup may or may not contain data modifications made between 14:24:00 and 14:26:00. On-Demand Backup does not support causal consistency.  
 Along with data, the following are also included on the backups:   
 Global secondary indexes (GSIs)  
 Local secondary indexes (LSIs)  
 Streams  
 Provisioned read and write capacity 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "TableName" : "The name of the table.",
  "BackupName" : "Specified name for the backup."
}
```

</details>

## create_global_table

Creates a global table from an existing table. A global table creates a replication relationship between two or more DynamoDB tables with the same table name in the provided regions.  
If you want to add a new replica table to a global table, each of the following conditions must be true:  
 The table must have the same primary key as all of the other replicas.  
 The table must have the same name as all of the other replicas.  
 The table must have DynamoDB Streams enabled, with the stream containing both the new and the old images of the item.  
 None of the replica tables in the global table can contain any data.   
 If global secondary indexes are specified, then the following conditions must also be met:   
  The global secondary indexes must have the same name.   
  The global secondary indexes must have the same hash key and sort key (if present).     
 Write capacity settings should be set consistently across your replica tables and secondary indexes. DynamoDB strongly recommends enabling auto scaling to manage the write capacity settings for all of your global tables replicas and indexes.  
 If you prefer to manage write capacity settings manually, you should provision equal replicated write capacity units to your replica tables. You should also provision equal replicated write capacity units to matching secondary indexes across your global table. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ReplicationGroup" : [ {
    "RegionName" : "The region where the replica needs to be created."
  } ],
  "GlobalTableName" : "The global table name."
}
```

</details>

## create_table

The CreateTable operation adds a new table to your account. In an AWS account, table names must be unique within each region. That is, you can have two tables with same name if you create the tables in different regions. 
 CreateTable is an asynchronous operation. Upon receiving a CreateTable request, DynamoDB immediately returns a response with a TableStatus of CREATING. After the table is created, DynamoDB sets the TableStatus to ACTIVE. You can perform read and write operations only on an ACTIVE table.  
You can optionally define secondary indexes on the new table, as part of the CreateTable operation. If you want to create multiple tables with secondary indexes on them, you must create the tables sequentially. Only one table with secondary indexes can be in the CREATING state at any given time. 
You can use the DescribeTable action to check the table status.

<details><summary>Parameters</summary>

### $body

Represents the input of a CreateTable operation.

**Type:** object

```json
{
  "TableName" : "The name of the table to create.",
  "SSESpecification" : {
    "SSEType" : "Server-side encryption type:  \n  AES256 - Server-side encryption which uses the AES256 algorithm.  \n  KMS - Server-side encryption which uses AWS Key Management Service. (default) ",
    "Enabled" : "Indicates whether server-side encryption is enabled (true) or disabled (false) on the table.",
    "KMSMasterKeyId" : "The KMS Master Key (CMK) which should be used for the KMS encryption. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS Master Key alias/aws/dynamodb."
  },
  "AttributeDefinitions" : [ {
    "AttributeType" : "The data type for the attribute, where:  \n  S - the attribute is of type String  \n  N - the attribute is of type Number  \n  B - the attribute is of type Binary ",
    "AttributeName" : "A name for the attribute."
  } ],
  "StreamSpecification" : {
    "StreamEnabled" : "Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.",
    "StreamViewType" : " When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:  \n  KEYS_ONLY - Only the key attributes of the modified item are written to the stream.  \n  NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.  \n  OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.  \n  NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream. "
  },
  "GlobalSecondaryIndexes" : [ {
    "IndexName" : "The name of the global secondary index. The name must be unique among all other indexes on this table.",
    "Projection" : {
      "NonKeyAttributes" : [ "string" ],
      "ProjectionType" : "The set of attributes that are projected into the index:  \n  KEYS_ONLY - Only the index and primary keys are projected into the index.  \n  INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes are in NonKeyAttributes.  \n  ALL - All of the table attributes are projected into the index. "
    },
    "ProvisionedThroughput" : {
      "WriteCapacityUnits" : "The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide.",
      "ReadCapacityUnits" : "The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide."
    },
    "KeySchema" : [ {
      "KeyType" : "The role that this key attribute will assume:  \n  HASH - partition key  \n  RANGE - sort key    \nThe partition key of an item is also known as its hash attribute. The term \"hash attribute\" derives from DynamoDB' usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values. \nThe sort key of an item is also known as its range attribute. The term \"range attribute\" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.",
      "AttributeName" : "The name of a key attribute."
    } ]
  } ],
  "ProvisionedThroughput" : {
    "WriteCapacityUnits" : "The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide.",
    "ReadCapacityUnits" : "The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide."
  },
  "KeySchema" : [ {
    "KeyType" : "The role that this key attribute will assume:  \n  HASH - partition key  \n  RANGE - sort key    \nThe partition key of an item is also known as its hash attribute. The term \"hash attribute\" derives from DynamoDB' usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values. \nThe sort key of an item is also known as its range attribute. The term \"range attribute\" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.",
    "AttributeName" : "The name of a key attribute."
  } ],
  "LocalSecondaryIndexes" : [ {
    "IndexName" : "The name of the local secondary index. The name must be unique among all other indexes on this table.",
    "Projection" : {
      "NonKeyAttributes" : [ "string" ],
      "ProjectionType" : "The set of attributes that are projected into the index:  \n  KEYS_ONLY - Only the index and primary keys are projected into the index.  \n  INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes are in NonKeyAttributes.  \n  ALL - All of the table attributes are projected into the index. "
    },
    "KeySchema" : [ {
      "KeyType" : "The role that this key attribute will assume:  \n  HASH - partition key  \n  RANGE - sort key    \nThe partition key of an item is also known as its hash attribute. The term \"hash attribute\" derives from DynamoDB' usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values. \nThe sort key of an item is also known as its range attribute. The term \"range attribute\" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.",
      "AttributeName" : "The name of a key attribute."
    } ]
  } ]
}
```

</details>

## delete_backup

Deletes an existing backup of a table. 
You can call DeleteBackup at a maximum rate of 10 times per second.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "BackupArn" : "The ARN associated with the backup."
}
```

</details>

## delete_item

Deletes a single item in a table by primary key. You can perform a conditional delete operation that deletes the item if it exists, or if it has an expected attribute value. 
In addition to deleting an item, you can also return the item's attribute values in the same operation, using the ReturnValues parameter. 
Unless you specify conditions, the DeleteItem is an idempotent operation; running it multiple times on the same item or attribute does not result in an error response. 
Conditional deletes are useful for deleting items only if specific conditions are met. If those conditions are met, DynamoDB performs the delete. Otherwise, the item is not deleted.

<details><summary>Parameters</summary>

### $body

Represents the input of a DeleteItem operation.

**Type:** object

```json
{
  "TableName" : "The name of the table from which to delete the item.",
  "Expected" : "This is a legacy parameter. Use ConditionExpression instead. For more information, see Expected in the Amazon DynamoDB Developer Guide.",
  "ConditionalOperator" : "This is a legacy parameter. Use ConditionExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.",
  "ReturnConsumedCapacity" : "string. Possible values: INDEXES | TOTAL | NONE",
  "ConditionExpression" : "A condition that must be satisfied in order for a conditional DeleteItem to succeed. \nAn expression can contain any of the following:  \n Functions: attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size  These function names are case-sensitive.  \n Comparison operators: = | &lt;&gt; | &lt; | &gt; | &lt;= | &gt;= | BETWEEN | IN    \n  Logical operators: AND | OR | NOT    \nFor more information on condition expressions, see Specifying Conditions in the Amazon DynamoDB Developer Guide.",
  "ExpressionAttributeNames" : "One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames:  \n To access an attribute whose name conflicts with a DynamoDB reserved word.  \n To create a placeholder for repeating occurrences of an attribute name in an expression.  \n To prevent special characters in an attribute name from being misinterpreted in an expression.   \nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:  \n  Percentile    \nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames:  \n  {\"#P\":\"Percentile\"}    \nYou could then use this substitution in an expression, as in this example:  \n  #P = :val     \nTokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime.  \nFor more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.",
  "Key" : "A map of attribute names to AttributeValue objects, representing the primary key of the item to delete. \nFor the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.",
  "ReturnValues" : "Use ReturnValues if you want to get the item attributes as they appeared before they were deleted. For DeleteItem, the valid values are:  \n  NONE - If ReturnValues is not specified, or if its value is NONE, then nothing is returned. (This setting is the default for ReturnValues.)  \n  ALL_OLD - The content of the old item is returned.    \nThe ReturnValues parameter is used by several DynamoDB operations; however, DeleteItem does not recognize any values other than NONE or ALL_OLD.",
  "ReturnItemCollectionMetrics" : "Determines whether item collection metrics are returned. If set to SIZE, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.",
  "ExpressionAttributeValues" : "One or more values that can be substituted in an expression. \nUse the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:  \n Available | Backordered | Discontinued  \nYou would first need to specify ExpressionAttributeValues as follows: \n { \":avail\":{\"S\":\"Available\"}, \":back\":{\"S\":\"Backordered\"}, \":disc\":{\"S\":\"Discontinued\"} }  \nYou could then use these values in an expression, such as this: \n ProductStatus IN (:avail, :back, :disc)  \nFor more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide."
}
```

</details>

## delete_table

The DeleteTable operation deletes a table and all of its items. After a DeleteTable request, the specified table is in the DELETING state until DynamoDB completes the deletion. If the table is in the ACTIVE state, you can delete it. If a table is in CREATING or UPDATING states, then DynamoDB returns a ResourceInUseException. If the specified table does not exist, DynamoDB returns a ResourceNotFoundException. If table is already in the DELETING state, no error is returned.   
DynamoDB might continue to accept data read and write operations, such as GetItem and PutItem, on a table in the DELETING state until the table deletion is complete.  
When you delete a table, any indexes on that table are also deleted. 
If you have DynamoDB Streams enabled on the table, then the corresponding stream on that table goes into the DISABLED state, and the stream is automatically deleted after 24 hours. 
Use the DescribeTable action to check the status of the table. 

<details><summary>Parameters</summary>

### $body

Represents the input of a DeleteTable operation.

**Type:** object

```json
{
  "TableName" : "The name of the table to delete."
}
```

</details>

## describe_backup

Describes an existing backup of a table. 
You can call DescribeBackup at a maximum rate of 10 times per second.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "BackupArn" : "The ARN associated with the backup."
}
```

</details>

## describe_continuous_backups

Checks the status of continuous backups and point in time recovery on the specified table. Continuous backups are ENABLED on all tables at table creation. If point in time recovery is enabled, PointInTimeRecoveryStatus will be set to ENABLED. 
 Once continuous backups and point in time recovery are enabled, you can restore to any point in time within EarliestRestorableDateTime and LatestRestorableDateTime.  
 LatestRestorableDateTime is typically 5 minutes before the current time. You can restore your table to any point in time during the last 35 days.  
You can call DescribeContinuousBackups at a maximum rate of 10 times per second.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "TableName" : "Name of the table for which the customer wants to check the continuous backups and point in time recovery settings."
}
```

</details>

## describe_endpoints



<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{ }
```

</details>

## describe_global_table

Returns information about the specified global table.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "GlobalTableName" : "The name of the global table."
}
```

</details>

## describe_global_table_settings

Describes region specific settings for a global table.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "GlobalTableName" : "The name of the global table to describe."
}
```

</details>

## describe_limits

Returns the current provisioned-capacity limits for your AWS account in a region, both for the region as a whole and for any one DynamoDB table that you create there. 
When you establish an AWS account, the account has initial limits on the maximum read capacity units and write capacity units that you can provision across all of your DynamoDB tables in a given region. Also, there are per-table limits that apply when you create a table there. For more information, see Limits page in the Amazon DynamoDB Developer Guide. 
Although you can increase these limits by filing a case at AWS Support Center, obtaining the increase is not instantaneous. The DescribeLimits action lets you write code to compare the capacity you are currently using to those limits imposed by your account so that you have enough time to apply for an increase before you hit a limit. 
For example, you could use one of the AWS SDKs to do the following:  
 Call DescribeLimits for a particular region to obtain your current account limits on provisioned capacity there.  
 Create a variable to hold the aggregate read capacity units provisioned for all your tables in that region, and one to hold the aggregate write capacity units. Zero them both.  
 Call ListTables to obtain a list of all your DynamoDB tables.  
 For each table name listed by ListTables, do the following:   Call DescribeTable with the table name.   Use the data returned by DescribeTable to add the read capacity units and write capacity units provisioned for the table itself to your variables.   If the table has one or more global secondary indexes (GSIs), loop over these GSIs and add their provisioned capacity values to your variables as well.    
 Report the account limits for that region returned by DescribeLimits, along with the total current provisioned capacity levels you have calculated.   
This will let you see whether you are getting close to your account-level limits. 
The per-table limits apply only when you are creating a new table. They restrict the sum of the provisioned capacity of the new table itself and all its global secondary indexes. 
For existing tables and their GSIs, DynamoDB will not let you increase provisioned capacity extremely rapidly, but the only upper limit that applies is that the aggregate provisioned capacity over all your tables and GSIs cannot exceed either of the per-account limits.  
 DescribeLimits should only be called periodically. You can expect throttling errors if you call it more than once in a minute.  
The DescribeLimits Request element has no content.

<details><summary>Parameters</summary>

### $body

Represents the input of a DescribeLimits operation. Has no content.

**Type:** object

```json
{ }
```

</details>

## describe_table

Returns information about the table, including the current status of the table, when it was created, the primary key schema, and any indexes on the table.  
If you issue a DescribeTable request immediately after a CreateTable request, DynamoDB might return a ResourceNotFoundException. This is because DescribeTable uses an eventually consistent query, and the metadata for your table might not be available at that moment. Wait for a few seconds, and then try the DescribeTable request again.

<details><summary>Parameters</summary>

### $body

Represents the input of a DescribeTable operation.

**Type:** object

```json
{
  "TableName" : "The name of the table to describe."
}
```

</details>

## describe_time_to_live

Gives a description of the Time to Live (TTL) status on the specified table. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "TableName" : "The name of the table to be described."
}
```

</details>

## get_item

The GetItem operation returns a set of attributes for the item with the given primary key. If there is no matching item, GetItem does not return any data and there will be no Item element in the response. 
 GetItem provides an eventually consistent read by default. If your application requires a strongly consistent read, set ConsistentRead to true. Although a strongly consistent read might take more time than an eventually consistent read, it always returns the last updated value.

<details><summary>Parameters</summary>

### $body

Represents the input of a GetItem operation.

**Type:** object

```json
{
  "TableName" : "The name of the table containing the requested item.",
  "ProjectionExpression" : "A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. \nIf no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result. \nFor more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.",
  "ReturnConsumedCapacity" : "string. Possible values: INDEXES | TOTAL | NONE",
  "AttributesToGet" : [ "string" ],
  "ExpressionAttributeNames" : "One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames:  \n To access an attribute whose name conflicts with a DynamoDB reserved word.  \n To create a placeholder for repeating occurrences of an attribute name in an expression.  \n To prevent special characters in an attribute name from being misinterpreted in an expression.   \nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:  \n  Percentile    \nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames:  \n  {\"#P\":\"Percentile\"}    \nYou could then use this substitution in an expression, as in this example:  \n  #P = :val     \nTokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime.  \nFor more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.",
  "Key" : "A map of attribute names to AttributeValue objects, representing the primary key of the item to retrieve. \nFor the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.",
  "ConsistentRead" : "Determines the read consistency model: If set to true, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads."
}
```

</details>

## list_backups

List backups associated with an AWS account. To list backups for a given table, specify TableName. ListBackups returns a paginated list of results with at most 1MB worth of items in a page. You can also specify a limit for the maximum number of entries to be returned in a page.  
In the request, start time is inclusive but end time is exclusive. Note that these limits are for the time at which the original backup was requested. 
You can call ListBackups a maximum of 5 times per second.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "TableName" : "The backups from the table specified by TableName are listed. ",
  "TimeRangeLowerBound" : "Only backups created after this time are listed. TimeRangeLowerBound is inclusive.",
  "TimeRangeUpperBound" : "Only backups created before this time are listed. TimeRangeUpperBound is exclusive. ",
  "BackupType" : "The backups from the table specified by BackupType are listed. \nWhere BackupType can be:  \n  USER - On-demand backup created by you.  \n  SYSTEM - On-demand backup automatically created by DynamoDB.  \n  ALL - All types of on-demand backups (USER and SYSTEM). "
}
```

</details>

## list_global_tables

Lists all global tables that have a replica in the specified region.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ExclusiveStartGlobalTableName" : "The first global table name that this operation will evaluate.",
  "RegionName" : "Lists the global tables in a specific region.",
  "Limit" : "The maximum number of table names to return."
}
```

</details>

## list_tables

Returns an array of table names associated with the current account and endpoint. The output from ListTables is paginated, with each page returning a maximum of 100 table names.

*This operation has no parameters*

## list_tags_of_resource

List all tags on an Amazon DynamoDB resource. You can call ListTagsOfResource up to 10 times per second, per account. 
For an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ResourceArn" : "The Amazon DynamoDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).",
  "NextToken" : "An optional string that, if supplied, must be copied from the output of a previous call to ListTagOfResource. When provided in this manner, this API fetches the next page of results."
}
```

</details>

## put_item

Creates a new item, or replaces an old item with a new item. If an item that has the same primary key as the new item already exists in the specified table, the new item completely replaces the existing item. You can perform a conditional put operation (add a new item if one with the specified primary key doesn't exist), or replace an existing item if it has certain attribute values. You can return the item's attribute values in the same operation, using the ReturnValues parameter.  
This topic provides general information about the PutItem API. 
For information on how to call the PutItem API using the AWS SDK in specific languages, see the following:  
   PutItem in the AWS Command Line Interface    
   PutItem in the AWS SDK for .NET    
   PutItem in the AWS SDK for C++    
   PutItem in the AWS SDK for Go    
   PutItem in the AWS SDK for Java    
   PutItem in the AWS SDK for JavaScript    
   PutItem in the AWS SDK for PHP V3    
   PutItem in the AWS SDK for Python    
   PutItem in the AWS SDK for Ruby V2      
When you add an item, the primary key attribute(s) are the only required attributes. Attribute values cannot be null. String and Binary type attributes must have lengths greater than zero. Set type attributes cannot be empty. Requests with empty values will be rejected with a ValidationException exception.  
To prevent a new item from replacing an existing item, use a conditional expression that contains the attribute_not_exists function with the name of the attribute being used as the partition key for the table. Since every record must contain that attribute, the attribute_not_exists function will only succeed if no matching item exists.  
For more information about PutItem, see Working with Items in the Amazon DynamoDB Developer Guide.

<details><summary>Parameters</summary>

### $body

Represents the input of a PutItem operation.

**Type:** object

```json
{
  "TableName" : "The name of the table to contain the item.",
  "Item" : "A map of attribute name/value pairs, one for each attribute. Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item. \nYou must provide all of the attributes for the primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide both values for both the partition key and the sort key. \nIf you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table's attribute definition. \nFor more information about primary keys, see Primary Key in the Amazon DynamoDB Developer Guide. \nEach element in the Item map is an AttributeValue object.",
  "Expected" : "This is a legacy parameter. Use ConditionExpression instead. For more information, see Expected in the Amazon DynamoDB Developer Guide.",
  "ConditionalOperator" : "This is a legacy parameter. Use ConditionExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.",
  "ReturnConsumedCapacity" : "string. Possible values: INDEXES | TOTAL | NONE",
  "ConditionExpression" : "A condition that must be satisfied in order for a conditional PutItem operation to succeed. \nAn expression can contain any of the following:  \n Functions: attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size  These function names are case-sensitive.  \n Comparison operators: = | &lt;&gt; | &lt; | &gt; | &lt;= | &gt;= | BETWEEN | IN    \n  Logical operators: AND | OR | NOT    \nFor more information on condition expressions, see Specifying Conditions in the Amazon DynamoDB Developer Guide.",
  "ExpressionAttributeNames" : "One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames:  \n To access an attribute whose name conflicts with a DynamoDB reserved word.  \n To create a placeholder for repeating occurrences of an attribute name in an expression.  \n To prevent special characters in an attribute name from being misinterpreted in an expression.   \nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:  \n  Percentile    \nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames:  \n  {\"#P\":\"Percentile\"}    \nYou could then use this substitution in an expression, as in this example:  \n  #P = :val     \nTokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime.  \nFor more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.",
  "ReturnValues" : "Use ReturnValues if you want to get the item attributes as they appeared before they were updated with the PutItem request. For PutItem, the valid values are:  \n  NONE - If ReturnValues is not specified, or if its value is NONE, then nothing is returned. (This setting is the default for ReturnValues.)  \n  ALL_OLD - If PutItem overwrote an attribute name-value pair, then the content of the old item is returned.    \nThe ReturnValues parameter is used by several DynamoDB operations; however, PutItem does not recognize any values other than NONE or ALL_OLD.",
  "ReturnItemCollectionMetrics" : "Determines whether item collection metrics are returned. If set to SIZE, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.",
  "ExpressionAttributeValues" : "One or more values that can be substituted in an expression. \nUse the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:  \n Available | Backordered | Discontinued  \nYou would first need to specify ExpressionAttributeValues as follows: \n { \":avail\":{\"S\":\"Available\"}, \":back\":{\"S\":\"Backordered\"}, \":disc\":{\"S\":\"Discontinued\"} }  \nYou could then use these values in an expression, such as this: \n ProductStatus IN (:avail, :back, :disc)  \nFor more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide."
}
```

</details>

## query

The Query operation finds items based on primary key values. You can query any table or secondary index that has a composite primary key (a partition key and a sort key).  
Use the KeyConditionExpression parameter to provide a specific value for the partition key. The Query operation will return all of the items from the table or index with that partition key value. You can optionally narrow the scope of the Query operation by specifying a sort key value and a comparison operator in KeyConditionExpression. To further refine the Query results, you can optionally provide a FilterExpression. A FilterExpression determines which items within the results should be returned to you. All of the other results are discarded.  
 A Query operation always returns a result set. If no matching items are found, the result set will be empty. Queries that do not return results consume the minimum number of read capacity units for that type of read operation.   
 DynamoDB calculates the number of read capacity units consumed based on item size, not on the amount of data that is returned to an application. The number of capacity units consumed will be the same whether you request all of the attributes (the default behavior) or just some of them (using a projection expression). The number will also be the same whether or not you use a FilterExpression.   
 Query results are always sorted by the sort key value. If the data type of the sort key is Number, the results are returned in numeric order; otherwise, the results are returned in order of UTF-8 bytes. By default, the sort order is ascending. To reverse the order, set the ScanIndexForward parameter to false.  
 A single Query operation will read up to the maximum number of items set (if using the Limit parameter) or a maximum of 1 MB of data and then apply any filtering to the results using FilterExpression. If LastEvaluatedKey is present in the response, you will need to paginate the result set. For more information, see Paginating the Results in the Amazon DynamoDB Developer Guide.  
 FilterExpression is applied after a Query finishes, but before the results are returned. A FilterExpression cannot contain partition key or sort key attributes. You need to specify those attributes in the KeyConditionExpression.   
 A Query operation can return an empty result set and a LastEvaluatedKey if all the items read for the page of results are filtered out.   
You can query a table, a local secondary index, or a global secondary index. For a query on a table or on a local secondary index, you can set the ConsistentRead parameter to true and obtain a strongly consistent result. Global secondary indexes support eventually consistent reads only, so do not specify ConsistentRead when querying a global secondary index.

<details><summary>Parameters</summary>

### $body

Represents the input of a Query operation.

**Type:** object

```json
{
  "ProjectionExpression" : "A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. \nIf no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result. \nFor more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.",
  "ConditionalOperator" : "This is a legacy parameter. Use FilterExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.",
  "AttributesToGet" : [ "string" ],
  "ExpressionAttributeNames" : "One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames:  \n To access an attribute whose name conflicts with a DynamoDB reserved word.  \n To create a placeholder for repeating occurrences of an attribute name in an expression.  \n To prevent special characters in an attribute name from being misinterpreted in an expression.   \nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:  \n  Percentile    \nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames:  \n  {\"#P\":\"Percentile\"}    \nYou could then use this substitution in an expression, as in this example:  \n  #P = :val     \nTokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime.  \nFor more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.",
  "ConsistentRead" : "Determines the read consistency model: If set to true, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads. \nStrongly consistent reads are not supported on global secondary indexes. If you query a global secondary index with ConsistentRead set to true, you will receive a ValidationException.",
  "ExpressionAttributeValues" : "One or more values that can be substituted in an expression. \nUse the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:  \n Available | Backordered | Discontinued  \nYou would first need to specify ExpressionAttributeValues as follows: \n { \":avail\":{\"S\":\"Available\"}, \":back\":{\"S\":\"Backordered\"}, \":disc\":{\"S\":\"Discontinued\"} }  \nYou could then use these values in an expression, such as this: \n ProductStatus IN (:avail, :back, :disc)  \nFor more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide.",
  "IndexName" : "The name of an index to query. This index can be any local secondary index or global secondary index on the table. Note that if you use the IndexName parameter, you must also provide TableName. ",
  "KeyConditions" : "This is a legacy parameter. Use KeyConditionExpression instead. For more information, see KeyConditions in the Amazon DynamoDB Developer Guide.",
  "TableName" : "The name of the table containing the requested items.",
  "ScanIndexForward" : "Specifies the order for index traversal: If true (default), the traversal is performed in ascending order; if false, the traversal is performed in descending order.  \nItems with the same partition key value are stored in sorted order by sort key. If the sort key data type is Number, the results are stored in numeric order. For type String, the results are stored in order of UTF-8 bytes. For type Binary, DynamoDB treats each byte of the binary data as unsigned. \nIf ScanIndexForward is true, DynamoDB returns the results in the order in which they are stored (by sort key value). This is the default behavior. If ScanIndexForward is false, DynamoDB reads the results in reverse order by sort key value, and then returns the results to the client.",
  "QueryFilter" : "This is a legacy parameter. Use FilterExpression instead. For more information, see QueryFilter in the Amazon DynamoDB Developer Guide.",
  "ReturnConsumedCapacity" : "string. Possible values: INDEXES | TOTAL | NONE",
  "Select" : "The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.  \n  ALL_ATTRIBUTES - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index DynamoDB will fetch the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.  \n  ALL_PROJECTED_ATTRIBUTES - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying ALL_ATTRIBUTES.  \n  COUNT - Returns the number of matching items, rather than the matching items themselves.  \n  SPECIFIC_ATTRIBUTES - Returns only the attributes listed in AttributesToGet. This return value is equivalent to specifying AttributesToGet without specifying any value for Select. If you query or scan a local secondary index and request only attributes that are projected into that index, the operation will read only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB will fetch each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency. If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table.   \nIf neither Select nor AttributesToGet are specified, DynamoDB defaults to ALL_ATTRIBUTES when accessing a table, and ALL_PROJECTED_ATTRIBUTES when accessing an index. You cannot use both Select and AttributesToGet together in a single request, unless the value for Select is SPECIFIC_ATTRIBUTES. (This usage is equivalent to specifying AttributesToGet without any value for Select.)  \nIf you use the ProjectionExpression parameter, then the value for Select can only be SPECIFIC_ATTRIBUTES. Any other value for Select will return an error.",
  "FilterExpression" : "A string that contains conditions that DynamoDB applies after the Query operation, but before the data is returned to you. Items that do not satisfy the FilterExpression criteria are not returned. \nA FilterExpression does not allow key attributes. You cannot define a filter expression based on a partition key or a sort key.  \nA FilterExpression is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.  \nFor more information, see Filter Expressions in the Amazon DynamoDB Developer Guide.",
  "KeyConditionExpression" : "The condition that specifies the key value(s) for items to be retrieved by the Query action. \nThe condition must perform an equality test on a single partition key value. \nThe condition can optionally perform one of several comparison tests on a single sort key value. This allows Query to retrieve one item with a given partition key value and sort key value, or several items that have the same partition key value but different sort key values. \nThe partition key equality test is required, and must be specified in the following format: \n partitionKeyName = :partitionkeyval  \nIf you also want to provide a condition for the sort key, it must be combined using AND with the condition for the sort key. Following is an example, using the = comparison operator for the sort key: \n partitionKeyName = :partitionkeyval AND sortKeyName = :sortkeyval  \nValid comparisons for the sort key condition are as follows:  \n  sortKeyName = :sortkeyval - true if the sort key value is equal to :sortkeyval.  \n  sortKeyName &lt; :sortkeyval - true if the sort key value is less than :sortkeyval.  \n  sortKeyName &lt;= :sortkeyval - true if the sort key value is less than or equal to :sortkeyval.  \n  sortKeyName &gt; :sortkeyval - true if the sort key value is greater than :sortkeyval.  \n  sortKeyName &gt;=  :sortkeyval - true if the sort key value is greater than or equal to :sortkeyval.  \n  sortKeyName BETWEEN :sortkeyval1 AND :sortkeyval2 - true if the sort key value is greater than or equal to :sortkeyval1, and less than or equal to :sortkeyval2.  \n  begins_with ( sortKeyName, :sortkeyval ) - true if the sort key value begins with a particular operand. (You cannot use this function with a sort key that is of type Number.) Note that the function name begins_with is case-sensitive.   \nUse the ExpressionAttributeValues parameter to replace tokens such as :partitionval and :sortval with actual values at runtime. \nYou can optionally use the ExpressionAttributeNames parameter to replace the names of the partition key and sort key with placeholder tokens. This option might be necessary if an attribute name conflicts with a DynamoDB reserved word. For example, the following KeyConditionExpression parameter causes an error because Size is a reserved word:  \n  Size = :myval    \nTo work around this, define a placeholder (such a #S) to represent the attribute name Size. KeyConditionExpression then is as follows:  \n  #S = :myval    \nFor a list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide. \nFor more information on ExpressionAttributeNames and ExpressionAttributeValues, see Using Placeholders for Attribute Names and Values in the Amazon DynamoDB Developer Guide."
}
```

</details>

## restore_table_from_backup

Creates a new table from an existing backup. Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.  
You can call RestoreTableFromBackup at a maximum rate of 10 times per second. 
You must manually set up the following on the restored table:  
 Auto scaling policies  
 IAM policies  
 Cloudwatch metrics and alarms  
 Tags  
 Stream settings  
 Time to Live (TTL) settings 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "BackupArn" : "The ARN associated with the backup.",
  "TargetTableName" : "The name of the new table to which the backup must be restored."
}
```

</details>

## restore_table_to_point_in_time

Restores the specified table to the specified point in time within EarliestRestorableDateTime and LatestRestorableDateTime. You can restore your table to any point in time during the last 35 days. Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.  
 When you restore using point in time recovery, DynamoDB restores your table data to the state based on the selected date and time (day:hour:minute:second) to a new table.  
 Along with data, the following are also included on the new restored table using point in time recovery:   
 Global secondary indexes (GSIs)  
 Local secondary indexes (LSIs)  
 Provisioned read and write capacity  
 Encryption settings   All these settings come from the current settings of the source table at the time of restore.     
You must manually set up the following on the restored table:  
 Auto scaling policies  
 IAM policies  
 Cloudwatch metrics and alarms  
 Tags  
 Stream settings  
 Time to Live (TTL) settings  
 Point in time recovery settings 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "SourceTableName" : "Name of the source table that is being restored.",
  "TargetTableName" : "The name of the new table to which it must be restored to.",
  "UseLatestRestorableTime" : "Restore the table to the latest possible time. LatestRestorableDateTime is typically 5 minutes before the current time. ",
  "RestoreDateTime" : "Time in the past to restore the table to."
}
```

</details>

## scan

The Scan operation returns one or more items and item attributes by accessing every item in a table or a secondary index. To have DynamoDB return fewer items, you can provide a FilterExpression operation. 
If the total number of scanned items exceeds the maximum data set size limit of 1 MB, the scan stops and results are returned to the user as a LastEvaluatedKey value to continue the scan in a subsequent operation. The results also include the number of items exceeding the limit. A scan can result in no table data meeting the filter criteria.  
A single Scan operation will read up to the maximum number of items set (if using the Limit parameter) or a maximum of 1 MB of data and then apply any filtering to the results using FilterExpression. If LastEvaluatedKey is present in the response, you will need to paginate the result set. For more information, see Paginating the Results in the Amazon DynamoDB Developer Guide.  
 Scan operations proceed sequentially; however, for faster performance on a large table or secondary index, applications can request a parallel Scan operation by providing the Segment and TotalSegments parameters. For more information, see Parallel Scan in the Amazon DynamoDB Developer Guide. 
 Scan uses eventually consistent reads when accessing the data in a table; therefore, the result set might not include the changes to data in the table immediately before the operation began. If you need a consistent copy of the data, as of the time that the Scan begins, you can set the ConsistentRead parameter to true.

<details><summary>Parameters</summary>

### $body

Represents the input of a Scan operation.

**Type:** object

```json
{
  "ProjectionExpression" : "A string that identifies one or more attributes to retrieve from the specified table or index. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. \nIf no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result. \nFor more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.",
  "ConditionalOperator" : "This is a legacy parameter. Use FilterExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.",
  "ScanFilter" : "This is a legacy parameter. Use FilterExpression instead. For more information, see ScanFilter in the Amazon DynamoDB Developer Guide.",
  "TotalSegments" : "For a parallel Scan request, TotalSegments represents the total number of segments into which the Scan operation will be divided. The value of TotalSegments corresponds to the number of application workers that will perform the parallel scan. For example, if you want to use four application threads to scan a table or an index, specify a TotalSegments value of 4. \nThe value for TotalSegments must be greater than or equal to 1, and less than or equal to 1000000. If you specify a TotalSegments value of 1, the Scan operation will be sequential rather than parallel. \nIf you specify TotalSegments, you must also specify Segment.",
  "AttributesToGet" : [ "string" ],
  "ExpressionAttributeNames" : "One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames:  \n To access an attribute whose name conflicts with a DynamoDB reserved word.  \n To create a placeholder for repeating occurrences of an attribute name in an expression.  \n To prevent special characters in an attribute name from being misinterpreted in an expression.   \nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:  \n  Percentile    \nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames:  \n  {\"#P\":\"Percentile\"}    \nYou could then use this substitution in an expression, as in this example:  \n  #P = :val     \nTokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime.  \nFor more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.",
  "Segment" : "For a parallel Scan request, Segment identifies an individual segment to be scanned by an application worker. \nSegment IDs are zero-based, so the first segment is always 0. For example, if you want to use four application threads to scan a table or an index, then the first thread specifies a Segment value of 0, the second thread specifies 1, and so on. \nThe value of LastEvaluatedKey returned from a parallel Scan request must be used as ExclusiveStartKey with the same segment ID in a subsequent Scan operation. \nThe value for Segment must be greater than or equal to 0, and less than the value provided for TotalSegments. \nIf you provide Segment, you must also provide TotalSegments.",
  "ConsistentRead" : "A Boolean value that determines the read consistency model during the scan:  \n If ConsistentRead is false, then the data returned from Scan might not contain the results from other recently completed write operations (PutItem, UpdateItem or DeleteItem).  \n If ConsistentRead is true, then all of the write operations that completed before the Scan began are guaranteed to be contained in the Scan response.   \nThe default setting for ConsistentRead is false. \nThe ConsistentRead parameter is not supported on global secondary indexes. If you scan a global secondary index with ConsistentRead set to true, you will receive a ValidationException.",
  "ExpressionAttributeValues" : "One or more values that can be substituted in an expression. \nUse the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:  \n Available | Backordered | Discontinued  \nYou would first need to specify ExpressionAttributeValues as follows: \n { \":avail\":{\"S\":\"Available\"}, \":back\":{\"S\":\"Backordered\"}, \":disc\":{\"S\":\"Discontinued\"} }  \nYou could then use these values in an expression, such as this: \n ProductStatus IN (:avail, :back, :disc)  \nFor more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide.",
  "IndexName" : "The name of a secondary index to scan. This index can be any local secondary index or global secondary index. Note that if you use the IndexName parameter, you must also provide TableName.",
  "TableName" : "The name of the table containing the requested items; or, if you provide IndexName, the name of the table to which that index belongs.",
  "ReturnConsumedCapacity" : "string. Possible values: INDEXES | TOTAL | NONE",
  "Select" : "The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.  \n  ALL_ATTRIBUTES - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index DynamoDB will fetch the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.  \n  ALL_PROJECTED_ATTRIBUTES - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying ALL_ATTRIBUTES.  \n  COUNT - Returns the number of matching items, rather than the matching items themselves.  \n  SPECIFIC_ATTRIBUTES - Returns only the attributes listed in AttributesToGet. This return value is equivalent to specifying AttributesToGet without specifying any value for Select. If you query or scan a local secondary index and request only attributes that are projected into that index, the operation will read only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB will fetch each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency. If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table.   \nIf neither Select nor AttributesToGet are specified, DynamoDB defaults to ALL_ATTRIBUTES when accessing a table, and ALL_PROJECTED_ATTRIBUTES when accessing an index. You cannot use both Select and AttributesToGet together in a single request, unless the value for Select is SPECIFIC_ATTRIBUTES. (This usage is equivalent to specifying AttributesToGet without any value for Select.)  \nIf you use the ProjectionExpression parameter, then the value for Select can only be SPECIFIC_ATTRIBUTES. Any other value for Select will return an error.",
  "FilterExpression" : "A string that contains conditions that DynamoDB applies after the Scan operation, but before the data is returned to you. Items that do not satisfy the FilterExpression criteria are not returned.  \nA FilterExpression is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.  \nFor more information, see Filter Expressions in the Amazon DynamoDB Developer Guide."
}
```

</details>

## tag_resource

Associate a set of tags with an Amazon DynamoDB resource. You can then activate these user-defined tags so that they appear on the Billing and Cost Management console for cost allocation tracking. You can call TagResource up to 5 times per second, per account.  
For an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ResourceArn" : "Identifies the Amazon DynamoDB resource to which tags should be added. This value is an Amazon Resource Name (ARN).",
  "Tags" : [ {
    "Value" : "The value of the tag. Tag values are case-sensitive and can be null.",
    "Key" : "The key of the tag.Tag keys are case sensitive. Each DynamoDB table can only have up to one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value. "
  } ]
}
```

</details>

## untag_resource

Removes the association of tags from an Amazon DynamoDB resource. You can call UntagResource up to 5 times per second, per account.  
For an overview on tagging DynamoDB resources, see Tagging for DynamoDB in the Amazon DynamoDB Developer Guide.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ResourceArn" : "The Amazon DyanamoDB resource the tags will be removed from. This value is an Amazon Resource Name (ARN).",
  "TagKeys" : [ "string" ]
}
```

</details>

## update_continuous_backups

 UpdateContinuousBackups enables or disables point in time recovery for the specified table. A successful UpdateContinuousBackups call returns the current ContinuousBackupsDescription. Continuous backups are ENABLED on all tables at table creation. If point in time recovery is enabled, PointInTimeRecoveryStatus will be set to ENABLED. 
 Once continuous backups and point in time recovery are enabled, you can restore to any point in time within EarliestRestorableDateTime and LatestRestorableDateTime.  
 LatestRestorableDateTime is typically 5 minutes before the current time. You can restore your table to any point in time during the last 35 days.. 

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "TableName" : "The name of the table.",
  "PointInTimeRecoverySpecification" : {
    "PointInTimeRecoveryEnabled" : "Indicates whether point in time recovery is enabled (true) or disabled (false) on the table."
  }
}
```

</details>

## update_global_table

Adds or removes replicas in the specified global table. The global table must already exist to be able to use this operation. Any replica to be added must be empty, must have the same name as the global table, must have the same key schema, and must have DynamoDB Streams enabled and must have same provisioned and maximum write capacity units.  
Although you can use UpdateGlobalTable to add replicas and remove replicas in a single request, for simplicity we recommend that you issue separate requests for adding or removing replicas.  
 If global secondary indexes are specified, then the following conditions must also be met:   
  The global secondary indexes must have the same name.   
  The global secondary indexes must have the same hash key and sort key (if present).   
  The global secondary indexes must have the same provisioned and maximum write capacity units.  

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "ReplicaUpdates" : [ {
    "Delete" : {
      "RegionName" : "The region of the replica to be removed."
    },
    "Create" : {
      "RegionName" : "The region of the replica to be added."
    }
  } ],
  "GlobalTableName" : "The global table name."
}
```

</details>

## update_global_table_settings

Updates settings for a global table.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate" : {
    "MaximumUnits" : "The maximum capacity units that a global table or global secondary index should be scaled up to.",
    "ScalingPolicyUpdate" : {
      "PolicyName" : "The name of the scaling policy.",
      "TargetTrackingScalingPolicyConfiguration" : {
        "ScaleOutCooldown" : "The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.",
        "TargetValue" : "The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).",
        "DisableScaleIn" : "Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.",
        "ScaleInCooldown" : "The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application's availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application autoscaling scales out your scalable target immediately. "
      }
    },
    "MinimumUnits" : "The minimum capacity units that a global table or global secondary index should be scaled down to.",
    "AutoScalingRoleArn" : "Role ARN used for configuring autoscaling policy.",
    "AutoScalingDisabled" : "Disabled autoscaling for this global table or global secondary index."
  },
  "GlobalTableGlobalSecondaryIndexSettingsUpdate" : [ {
    "IndexName" : "The name of the global secondary index. The name must be unique among all other indexes on this table.",
    "ProvisionedWriteCapacityUnits" : "The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException. ",
    "ProvisionedWriteCapacityAutoScalingSettingsUpdate" : {
      "MaximumUnits" : "The maximum capacity units that a global table or global secondary index should be scaled up to.",
      "ScalingPolicyUpdate" : {
        "PolicyName" : "The name of the scaling policy.",
        "TargetTrackingScalingPolicyConfiguration" : {
          "ScaleOutCooldown" : "The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.",
          "TargetValue" : "The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).",
          "DisableScaleIn" : "Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.",
          "ScaleInCooldown" : "The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application's availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application autoscaling scales out your scalable target immediately. "
        }
      },
      "MinimumUnits" : "The minimum capacity units that a global table or global secondary index should be scaled down to.",
      "AutoScalingRoleArn" : "Role ARN used for configuring autoscaling policy.",
      "AutoScalingDisabled" : "Disabled autoscaling for this global table or global secondary index."
    }
  } ],
  "ReplicaSettingsUpdate" : [ {
    "ReplicaProvisionedReadCapacityUnits" : "The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide. ",
    "RegionName" : "The region of the replica to be added.",
    "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate" : {
      "MaximumUnits" : "The maximum capacity units that a global table or global secondary index should be scaled up to.",
      "ScalingPolicyUpdate" : {
        "PolicyName" : "The name of the scaling policy.",
        "TargetTrackingScalingPolicyConfiguration" : {
          "ScaleOutCooldown" : "The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.",
          "TargetValue" : "The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).",
          "DisableScaleIn" : "Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.",
          "ScaleInCooldown" : "The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application's availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application autoscaling scales out your scalable target immediately. "
        }
      },
      "MinimumUnits" : "The minimum capacity units that a global table or global secondary index should be scaled down to.",
      "AutoScalingRoleArn" : "Role ARN used for configuring autoscaling policy.",
      "AutoScalingDisabled" : "Disabled autoscaling for this global table or global secondary index."
    },
    "ReplicaGlobalSecondaryIndexSettingsUpdate" : [ {
      "IndexName" : "The name of the global secondary index. The name must be unique among all other indexes on this table.",
      "ProvisionedReadCapacityUnits" : "The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException.",
      "ProvisionedReadCapacityAutoScalingSettingsUpdate" : {
        "MaximumUnits" : "The maximum capacity units that a global table or global secondary index should be scaled up to.",
        "ScalingPolicyUpdate" : {
          "PolicyName" : "The name of the scaling policy.",
          "TargetTrackingScalingPolicyConfiguration" : {
            "ScaleOutCooldown" : "The amount of time, in seconds, after a scale out activity completes before another scale out activity can start. While the cooldown period is in effect, the capacity that has been added by the previous scale out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out. You should continuously (but not excessively) scale out.",
            "TargetValue" : "The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10) or 2e-360 to 2e360 (Base 2).",
            "DisableScaleIn" : "Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is false.",
            "ScaleInCooldown" : "The amount of time, in seconds, after a scale in activity completes before another scale in activity can start. The cooldown period is used to block subsequent scale in requests until it has expired. You should scale in conservatively to protect your application's availability. However, if another alarm triggers a scale out policy during the cooldown period after a scale-in, application autoscaling scales out your scalable target immediately. "
          }
        },
        "MinimumUnits" : "The minimum capacity units that a global table or global secondary index should be scaled down to.",
        "AutoScalingRoleArn" : "Role ARN used for configuring autoscaling policy.",
        "AutoScalingDisabled" : "Disabled autoscaling for this global table or global secondary index."
      }
    } ]
  } ],
  "GlobalTableName" : "The name of the global table",
  "GlobalTableProvisionedWriteCapacityUnits" : "The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException. "
}
```

</details>

## update_item

Edits an existing item's attributes, or adds a new item to the table if it does not already exist. You can put, delete, or add attribute values. You can also perform a conditional update on an existing item (insert a new attribute name-value pair if it doesn't exist, or replace an existing name-value pair if it has certain expected attribute values). 
You can also return the item's attribute values in the same UpdateItem operation using the ReturnValues parameter.

<details><summary>Parameters</summary>

### $body

Represents the input of an UpdateItem operation.

**Type:** object

```json
{
  "TableName" : "The name of the table containing the item to update.",
  "Expected" : "This is a legacy parameter. Use ConditionExpression instead. For more information, see Expected in the Amazon DynamoDB Developer Guide.",
  "ConditionalOperator" : "This is a legacy parameter. Use ConditionExpression instead. For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.",
  "ReturnConsumedCapacity" : "string. Possible values: INDEXES | TOTAL | NONE",
  "ConditionExpression" : "A condition that must be satisfied in order for a conditional update to succeed. \nAn expression can contain any of the following:  \n Functions: attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size  These function names are case-sensitive.  \n Comparison operators: = | &lt;&gt; | &lt; | &gt; | &lt;= | &gt;= | BETWEEN | IN    \n  Logical operators: AND | OR | NOT    \nFor more information on condition expressions, see Specifying Conditions in the Amazon DynamoDB Developer Guide.",
  "ExpressionAttributeNames" : "One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames:  \n To access an attribute whose name conflicts with a DynamoDB reserved word.  \n To create a placeholder for repeating occurrences of an attribute name in an expression.  \n To prevent special characters in an attribute name from being misinterpreted in an expression.   \nUse the # character in an expression to dereference an attribute name. For example, consider the following attribute name:  \n  Percentile    \nThe name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames:  \n  {\"#P\":\"Percentile\"}    \nYou could then use this substitution in an expression, as in this example:  \n  #P = :val     \nTokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime.  \nFor more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.",
  "UpdateExpression" : "An expression that defines one or more attributes to be updated, the action to be performed on them, and new value(s) for them. \nThe following action values are available for UpdateExpression.  \n  SET - Adds one or more attributes and values to an item. If any of these attribute already exist, they are replaced by the new values. You can also use SET to add or subtract from an attribute that is of type Number. For example: SET myNum = myNum + :val   SET supports the following functions:    if_not_exists (path, operand) - if the item does not contain an attribute at the specified path, then if_not_exists evaluates to operand; otherwise, it evaluates to path. You can use this function to avoid overwriting an attribute that may already be present in the item.    list_append (operand, operand) - evaluates to a list with a new element added to it. You can append the new element to the start or the end of the list by reversing the order of the operands.   These function names are case-sensitive.  \n  REMOVE - Removes one or more attributes from an item.  \n  ADD - Adds the specified value to the item, if the attribute does not already exist. If the attribute does exist, then the behavior of ADD depends on the data type of the attribute:   If the existing attribute is a number, and if Value is also a number, then Value is mathematically added to the existing attribute. If Value is a negative number, then it is subtracted from the existing attribute.  If you use ADD to increment or decrement a number value for an item that doesn't exist before the update, DynamoDB uses 0 as the initial value. Similarly, if you use ADD for an existing item to increment or decrement an attribute value that doesn't exist before the update, DynamoDB uses 0 as the initial value. For example, suppose that the item you want to update doesn't have an attribute named itemcount, but you decide to ADD the number 3 to this attribute anyway. DynamoDB will create the itemcount attribute, set its initial value to 0, and finally add 3 to it. The result will be a new itemcount attribute in the item, with a value of 3.    If the existing data type is a set and if Value is also a set, then Value is added to the existing set. For example, if the attribute value is the set [1,2], and the ADD action specified [3], then the final attribute value is [1,2,3]. An error occurs if an ADD action is specified for a set attribute and the attribute type specified does not match the existing set type.  Both sets must have the same primitive data type. For example, if the existing data type is a set of strings, the Value must also be a set of strings.    The ADD action only supports Number and set data types. In addition, ADD can only be used on top-level attributes, not nested attributes.   \n  DELETE - Deletes an element from a set. If a set of values is specified, then those values are subtracted from the old set. For example, if the attribute value was the set [a,b,c] and the DELETE action specifies [a,c], then the final attribute value is [b]. Specifying an empty set is an error.  The DELETE action only supports set data types. In addition, DELETE can only be used on top-level attributes, not nested attributes.    \nYou can have many actions in a single expression, such as the following: SET a=:value1, b=:value2 DELETE :value3, :value4, :value5  \nFor more information on update expressions, see Modifying Items and Attributes in the Amazon DynamoDB Developer Guide.",
  "Key" : "The primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute. \nFor the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.",
  "AttributeUpdates" : "This is a legacy parameter. Use UpdateExpression instead. For more information, see AttributeUpdates in the Amazon DynamoDB Developer Guide.",
  "ReturnValues" : "Use ReturnValues if you want to get the item attributes as they appear before or after they are updated. For UpdateItem, the valid values are:  \n  NONE - If ReturnValues is not specified, or if its value is NONE, then nothing is returned. (This setting is the default for ReturnValues.)  \n  ALL_OLD - Returns all of the attributes of the item, as they appeared before the UpdateItem operation.  \n  UPDATED_OLD - Returns only the updated attributes, as they appeared before the UpdateItem operation.  \n  ALL_NEW - Returns all of the attributes of the item, as they appear after the UpdateItem operation.  \n  UPDATED_NEW - Returns only the updated attributes, as they appear after the UpdateItem operation.   \nThere is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed. \nThe values returned are strongly consistent.",
  "ReturnItemCollectionMetrics" : "Determines whether item collection metrics are returned. If set to SIZE, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.",
  "ExpressionAttributeValues" : "One or more values that can be substituted in an expression. \nUse the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:  \n Available | Backordered | Discontinued  \nYou would first need to specify ExpressionAttributeValues as follows: \n { \":avail\":{\"S\":\"Available\"}, \":back\":{\"S\":\"Backordered\"}, \":disc\":{\"S\":\"Discontinued\"} }  \nYou could then use these values in an expression, such as this: \n ProductStatus IN (:avail, :back, :disc)  \nFor more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide."
}
```

</details>

## update_table

Modifies the provisioned throughput settings, global secondary indexes, or DynamoDB Streams settings for a given table. 
You can only perform one of the following operations at once:  
 Modify the provisioned throughput settings of the table.  
 Enable or disable Streams on the table.  
 Remove a global secondary index from the table.  
 Create a new global secondary index on the table. Once the index begins backfilling, you can use UpdateTable to perform other operations.   
 UpdateTable is an asynchronous operation; while it is executing, the table status changes from ACTIVE to UPDATING. While it is UPDATING, you cannot issue another UpdateTable request. When the table returns to the ACTIVE state, the UpdateTable operation is complete.

<details><summary>Parameters</summary>

### $body

Represents the input of an UpdateTable operation.

**Type:** object

```json
{
  "TableName" : "The name of the table to be updated.",
  "SSESpecification" : {
    "SSEType" : "Server-side encryption type:  \n  AES256 - Server-side encryption which uses the AES256 algorithm.  \n  KMS - Server-side encryption which uses AWS Key Management Service. (default) ",
    "Enabled" : "Indicates whether server-side encryption is enabled (true) or disabled (false) on the table.",
    "KMSMasterKeyId" : "The KMS Master Key (CMK) which should be used for the KMS encryption. To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN. Note that you should only provide this parameter if the key is different from the default DynamoDB KMS Master Key alias/aws/dynamodb."
  },
  "AttributeDefinitions" : [ {
    "AttributeType" : "The data type for the attribute, where:  \n  S - the attribute is of type String  \n  N - the attribute is of type Number  \n  B - the attribute is of type Binary ",
    "AttributeName" : "A name for the attribute."
  } ],
  "StreamSpecification" : {
    "StreamEnabled" : "Indicates whether DynamoDB Streams is enabled (true) or disabled (false) on the table.",
    "StreamViewType" : " When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are:  \n  KEYS_ONLY - Only the key attributes of the modified item are written to the stream.  \n  NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream.  \n  OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream.  \n  NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream. "
  },
  "ProvisionedThroughput" : {
    "WriteCapacityUnits" : "The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide.",
    "ReadCapacityUnits" : "The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide."
  },
  "GlobalSecondaryIndexUpdates" : [ {
    "Delete" : {
      "IndexName" : "The name of the global secondary index to be deleted."
    },
    "Create" : {
      "IndexName" : "The name of the global secondary index to be created.",
      "Projection" : {
        "NonKeyAttributes" : [ "string" ],
        "ProjectionType" : "The set of attributes that are projected into the index:  \n  KEYS_ONLY - Only the index and primary keys are projected into the index.  \n  INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes are in NonKeyAttributes.  \n  ALL - All of the table attributes are projected into the index. "
      },
      "ProvisionedThroughput" : {
        "WriteCapacityUnits" : "The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide.",
        "ReadCapacityUnits" : "The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide."
      },
      "KeySchema" : [ {
        "KeyType" : "The role that this key attribute will assume:  \n  HASH - partition key  \n  RANGE - sort key    \nThe partition key of an item is also known as its hash attribute. The term \"hash attribute\" derives from DynamoDB' usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values. \nThe sort key of an item is also known as its range attribute. The term \"range attribute\" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.",
        "AttributeName" : "The name of a key attribute."
      } ]
    },
    "Update" : {
      "IndexName" : "The name of the global secondary index to be updated.",
      "ProvisionedThroughput" : {
        "WriteCapacityUnits" : "The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide.",
        "ReadCapacityUnits" : "The maximum number of strongly consistent reads consumed per second before DynamoDB returns a ThrottlingException. For more information, see Specifying Read and Write Requirements in the Amazon DynamoDB Developer Guide."
      }
    }
  } ]
}
```

</details>

## update_time_to_live

The UpdateTimeToLive method will enable or disable TTL for the specified table. A successful UpdateTimeToLive call returns the current TimeToLiveSpecification; it may take up to one hour for the change to fully process. Any additional UpdateTimeToLive calls for the same table during this one hour duration result in a ValidationException.  
TTL compares the current time in epoch time format to the time stored in the TTL attribute of an item. If the epoch time value stored in the attribute is less than the current time, the item is marked as expired and subsequently deleted.  
 The epoch time format is the number of seconds elapsed since 12:00:00 AM January 1st, 1970 UTC.   
DynamoDB deletes expired items on a best-effort basis to ensure availability of throughput for other data operations.   
DynamoDB typically deletes expired items within two days of expiration. The exact duration within which an item gets deleted after expiration is specific to the nature of the workload. Items that have expired and not been deleted will still show up in reads, queries, and scans.  
As items are deleted, they are removed from any Local Secondary Index and Global Secondary Index immediately in the same eventually consistent way as a standard delete operation. 
For more information, see Time To Live in the Amazon DynamoDB Developer Guide. 

<details><summary>Parameters</summary>

### $body

Represents the input of an UpdateTimeToLive operation.

**Type:** object

```json
{
  "TableName" : "The name of the table to be configured.",
  "TimeToLiveSpecification" : {
    "Enabled" : "Indicates whether Time To Live is to be enabled (true) or disabled (false) on the table.",
    "AttributeName" : "The name of the Time to Live attribute used to store the expiration time for items in the table."
  }
}
```

</details>

