---
id: aws-dynamodb-documentation
title: AWS DynamoDB (version v3.*.*)
sidebar_label: AWS DynamoDB
layout: docs.mustache
---

## batch_get_item

The BatchGetItem operation returns the attributes of one or more items from one or more tables. You identify requested items by primary key.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html

<details><summary>Parameters</summary>

#### RequestItems (required)

A map of one or more table names and, for each table, a map that describes one or more items to retrieve from that table. Each table name can be used only once per BatchGetItem request. Each element in the map of items to retrieve consists of the following: ConsistentRead - If true, a strongly consistent read is used; if false (the default), an eventually consistent read is used. ExpressionAttributeNames - One or more substitution tokens for attribute names in the ProjectionExpression parameter. The following are some use cases for using ExpressionAttributeNames: To access an attribute whose name conflicts with a DynamoDB reserved word. To create a placeholder for repeating occurrences of an attribute name in an expression. To prevent special characters in an attribute name from being misinterpreted in an expression. Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name: Percentile The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames: {"#P":"Percentile"} You could then use this substitution in an expression, as in this example: #P = :val Note Tokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime. For more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide. Keys - An array of primary key attribute values that define specific items in the table. For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide the partition key value. For a composite key, you must provide both the partition key value and the sort key value. ProjectionExpression - A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result. For more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide. AttributesToGet - This is a legacy parameter.  Use ProjectionExpression instead.  For more information, see AttributesToGet in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ReturnConsumedCapacity

Determines the level of detail about provisioned throughput consumption that is returned in the response: INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem, do not access any indexes at all.  In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s). TOTAL - The response includes only the aggregate ConsumedCapacity for the operation. NONE - No ConsumedCapacity details are included in the response.

**Type:** STRING

</details>

## batch_write_item

The BatchWriteItem operation puts or deletes multiple items in one or more tables. A single call to BatchWriteItem can write up to 16 MB of data, which can comprise as many as 25 put or delete requests. Individual items to be written can be as large as 400 KB.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html

<details><summary>Parameters</summary>

#### RequestItems (required)

A map of one or more table names and, for each table, a list of operations to be performed (DeleteRequest or PutRequest). Each element in the map consists of the following: DeleteRequest - Perform a DeleteItem operation on the specified item. The item to be deleted is identified by a Key subelement: Key - A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value. For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key. PutRequest - Perform a PutItem operation on the specified item. The item to be put is identified by an Item subelement: Item - A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values will be rejected with a ValidationException exception. If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table's attribute definition.

**Type:** ARRAY

#### ReturnConsumedCapacity

Determines the level of detail about provisioned throughput consumption that is returned in the response: INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem, do not access any indexes at all.  In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s). TOTAL - The response includes only the aggregate ConsumedCapacity for the operation. NONE - No ConsumedCapacity details are included in the response.

**Type:** STRING

#### ReturnItemCollectionMetrics

Determines whether item collection metrics are returned.  If set to SIZE, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.

**Type:** STRING

</details>

## create_backup

Creates a backup for an existing table. https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateBackup.html

<details><summary>Parameters</summary>

#### BackupName (required)

Specified name for the backup.

**Type:** STRING

#### TableName (required)

The name of the table.

**Type:** STRING

</details>

## create_global_table

Creates a global table from an existing table. A global table creates a replication relationship between two or more DynamoDB tables with the same table name in the provided regions.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateGlobalTable.html

<details><summary>Parameters</summary>

#### GlobalTableName (required)

The global table name.

**Type:** STRING

#### ReplicationGroup (required)

The regions where the global table needs to be created.

**Type:** ARRAY

</details>

## create_table

The CreateTable operation adds a new table to your account. In an AWS account, table names must be unique within each region. That is, you can have two tables with same name if you create the tables in different regions.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html

<details><summary>Parameters</summary>

#### AttributeDefinitions (required)

An array of attributes that describe the key schema for the table and indexes.

**Type:** ARRAY

#### KeySchema (required)

Specifies the attributes that make up the primary key for a table or an index. The attributes in KeySchema must also be defined in the AttributeDefinitions array. For more information, see Data Model in the Amazon DynamoDB Developer Guide. Each KeySchemaElement in the array is composed of: AttributeName - The name of this key attribute. KeyType - The role that the key attribute will assume: HASH - partition key RANGE - sort key Note The partition key of an item is also known as its hash attribute.  The term "hash attribute" derives from DynamoDB' usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values. The sort key of an item is also known as its range attribute. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value. For a simple primary key (partition key), you must provide exactly one element with a KeyType of HASH. For a composite primary key (partition key and sort key), you must provide exactly two elements, in this order: The first element must have a KeyType of HASH, and the second element must have a KeyType of RANGE. For more information, see Specifying the Primary Key in the Amazon DynamoDB Developer Guide.

**Type:** ARRAY

#### TableName (required)

The name of the table to create.

**Type:** STRING

#### BillingMode

Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later. PROVISIONED - Sets the billing mode to PROVISIONED. We recommend using PROVISIONED for predictable workloads. PAY_PER_REQUEST - Sets the billing mode to PAY_PER_REQUEST. We recommend using PAY_PER_REQUEST for unpredictable workloads.

**Type:** STRING

#### GlobalSecondaryIndexes

One or more global secondary indexes (the maximum is 20) to be created on the table. Each global secondary index in the array includes the following: IndexName - The name of the global secondary index. Must be unique only for this table. KeySchema - Specifies the key schema for the global secondary index. Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of: ProjectionType - One of the following: KEYS_ONLY - Only the index and primary keys are projected into the index. INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes are in NonKeyAttributes. ALL - All of the table attributes are projected into the index. NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total. ProvisionedThroughput - The provisioned throughput settings for the global secondary index, consisting of read and write capacity units.

**Type:** ARRAY

#### LocalSecondaryIndexes

One or more local secondary indexes (the maximum is 5) to be created on the table. Each index is scoped to a given partition key value. There is a 10 GB size limit per partition key value; otherwise, the size of a local secondary index is unconstrained. Each local secondary index in the array includes the following: IndexName - The name of the local secondary index. Must be unique only for this table. KeySchema - Specifies the key schema for the local secondary index. The key schema must begin with the same partition key as the table. Projection - Specifies attributes that are copied (projected) from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected. Each attribute specification is composed of: ProjectionType - One of the following: KEYS_ONLY - Only the index and primary keys are projected into the index. INCLUDE - Only the specified table attributes are projected into the index. The list of projected attributes are in NonKeyAttributes. ALL - All of the table attributes are projected into the index. NonKeyAttributes - A list of one or more non-key attribute names that are projected into the secondary index. The total count of attributes provided in NonKeyAttributes, summed across all of the secondary indexes, must not exceed 100. If you project the same attribute into two different indexes, this counts as two distinct attributes when determining the total.

**Type:** ARRAY

#### ProvisionedThroughput

Represents the provisioned throughput settings for a specified table or index. The settings can be modified using the UpdateTable operation. If you set BillingMode as PROVISIONED, you must specify this property. If you set BillingMode as PAY_PER_REQUEST, you cannot specify this property.  For current minimum and maximum provisioned throughput values, see Limits in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### SSESpecification

Represents the settings used to enable server-side encryption.

**Type:** OBJECT

#### StreamSpecification

The settings for DynamoDB Streams on the table. These settings consist of: StreamEnabled - Indicates whether Streams is to be enabled (true) or disabled (false). StreamViewType - When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values for StreamViewType are: KEYS_ONLY - Only the key attributes of the modified item are written to the stream. NEW_IMAGE - The entire item, as it appears after it was modified, is written to the stream. OLD_IMAGE - The entire item, as it appeared before it was modified, is written to the stream. NEW_AND_OLD_IMAGES - Both the new and the old item images of the item are written to the stream.

**Type:** OBJECT

</details>

## delete_backup

Deletes an existing backup of a table. https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteBackup.html

<details><summary>Parameters</summary>

#### BackupArn (required)

The ARN associated with the backup.

**Type:** STRING

</details>

## delete_item

Deletes a single item in a table by primary key. You can perform a conditional delete operation that deletes the item if it exists, or if it has an expected attribute value.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html

<details><summary>Parameters</summary>

#### Key (required)

A map of attribute names to AttributeValue objects, representing the primary key of the item to delete. For the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.

**Type:** OBJECT

#### TableName (required)

The name of the table from which to delete the item.

**Type:** STRING

#### ConditionExpression

A condition that must be satisfied in order for a conditional DeleteItem to succeed. An expression can contain any of the following: Functions: attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size These function names are case-sensitive. Comparison operators: = | <> | < | > | <= | >= | BETWEEN | IN  Logical operators: AND | OR | NOT For more information on condition expressions, see Specifying Conditions in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### ConditionalOperator

This is a legacy parameter.  Use ConditionExpression instead.  For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### Expected

This is a legacy parameter.  Use ConditionExpression instead.  For more information, see Expected in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ExpressionAttributeNames

One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames: To access an attribute whose name conflicts with a DynamoDB reserved word. To create a placeholder for repeating occurrences of an attribute name in an expression. To prevent special characters in an attribute name from being misinterpreted in an expression. Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name: Percentile The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames: {"#P":"Percentile"} You could then use this substitution in an expression, as in this example: #P = :val Note Tokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime. For more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ExpressionAttributeValues

One or more values that can be substituted in an expression. Use the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:  Available | Backordered | Discontinued You would first need to specify ExpressionAttributeValues as follows: { ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} } You could then use these values in an expression, such as this: ProductStatus IN (:avail, :back, :disc) For more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ReturnConsumedCapacity

Determines the level of detail about provisioned throughput consumption that is returned in the response: INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem, do not access any indexes at all.  In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s). TOTAL - The response includes only the aggregate ConsumedCapacity for the operation. NONE - No ConsumedCapacity details are included in the response.

**Type:** STRING

#### ReturnItemCollectionMetrics

Determines whether item collection metrics are returned.  If set to SIZE, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.

**Type:** STRING

#### ReturnValues

Use ReturnValues if you want to get the item attributes as they appeared before they were deleted. For DeleteItem, the valid values are: NONE - If ReturnValues is not specified, or if its value is NONE, then nothing is returned. (This setting is the default for ReturnValues.) ALL_OLD - The content of the old item is returned. Note The ReturnValues parameter is used by several DynamoDB operations; however, DeleteItem does not recognize any values other than NONE or ALL_OLD.

**Type:** STRING

</details>

## delete_table

The DeleteTable operation deletes a table and all of its items. After a DeleteTable request, the specified table is in the DELETING state until DynamoDB completes the deletion. If the table is in the ACTIVE state, you can delete it. If a table is in CREATING or UPDATING states, then DynamoDB returns a ResourceInUseException. If the specified table does not exist, DynamoDB returns a ResourceNotFoundException. If table is already in the DELETING state, no error is returned.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteTable.html

<details><summary>Parameters</summary>

#### TableName (required)

The name of the table to delete.

**Type:** STRING

</details>

## describe_backup

Describes an existing backup of a table. https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeBackup.html

<details><summary>Parameters</summary>

#### BackupArn (required)

The ARN associated with the backup.

**Type:** STRING

</details>

## describe_continuous_backups

Checks the status of continuous backups and point in time recovery on the specified table. Continuous backups are ENABLED on all tables at table creation. If point in time recovery is enabled, PointInTimeRecoveryStatus will be set to ENABLED.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeContinuousBackups.html

<details><summary>Parameters</summary>

#### TableName (required)

Name of the table for which the customer wants to check the continuous backups and point in time recovery settings.

**Type:** STRING

</details>

## describe_endpoints



*This operation has no parameters*

## describe_global_table

Returns information about the specified global table. https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTable.html

<details><summary>Parameters</summary>

#### GlobalTableName (required)

The name of the global table.

**Type:** STRING

</details>

## describe_global_table_settings

Describes region specific settings for a global table. https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeGlobalTableSettings.html

<details><summary>Parameters</summary>

#### GlobalTableName (required)

The name of the global table to describe.

**Type:** STRING

</details>

## describe_limits



*This operation has no parameters*

## describe_table

Returns information about the table, including the current status of the table, when it was created, the primary key schema, and any indexes on the table.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html

<details><summary>Parameters</summary>

#### TableName (required)

The name of the table to describe.

**Type:** STRING

</details>

## describe_time_to_live

Gives a description of the Time to Live (TTL) status on the specified table.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTimeToLive.html

<details><summary>Parameters</summary>

#### TableName (required)

The name of the table to be described.

**Type:** STRING

</details>

## get_item

The GetItem operation returns a set of attributes for the item with the given primary key. If there is no matching item, GetItem does not return any data and there will be no Item element in the response.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html

<details><summary>Parameters</summary>

#### Key (required)

A map of attribute names to AttributeValue objects, representing the primary key of the item to retrieve. For the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.

**Type:** OBJECT

#### TableName (required)

The name of the table containing the requested item.

**Type:** STRING

#### AttributesToGet

This is a legacy parameter.  Use ProjectionExpression instead.  For more information, see AttributesToGet in the Amazon DynamoDB Developer Guide.

**Type:** ARRAY

#### ConsistentRead

Determines the read consistency model:  If set to true, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.

**Type:** BOOLEAN

#### ExpressionAttributeNames

One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames: To access an attribute whose name conflicts with a DynamoDB reserved word. To create a placeholder for repeating occurrences of an attribute name in an expression. To prevent special characters in an attribute name from being misinterpreted in an expression. Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name: Percentile The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames: {"#P":"Percentile"} You could then use this substitution in an expression, as in this example: #P = :val Note Tokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime. For more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ProjectionExpression

A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result. For more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### ReturnConsumedCapacity

Determines the level of detail about provisioned throughput consumption that is returned in the response: INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem, do not access any indexes at all.  In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s). TOTAL - The response includes only the aggregate ConsumedCapacity for the operation. NONE - No ConsumedCapacity details are included in the response.

**Type:** STRING

</details>

## list_backups

List backups associated with an AWS account. To list backups for a given table, specify TableName. ListBackups returns a paginated list of results with at most 1MB worth of items in a page. You can also specify a limit for the maximum number of entries to be returned in a page.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListBackups.html

<details><summary>Parameters</summary>

#### BackupType

The backups from the table specified by BackupType are listed. Where BackupType can be: USER - On-demand backup created by you. SYSTEM - On-demand backup automatically created by DynamoDB. ALL - All types of on-demand backups (USER and SYSTEM).

**Type:** STRING

#### TableName

The backups from the table specified by TableName are listed.

**Type:** STRING

#### TimeRangeLowerBound

Only backups created after this time are listed. TimeRangeLowerBound is inclusive.

**Type:** OBJECT

#### TimeRangeUpperBound

Only backups created before this time are listed. TimeRangeUpperBound is exclusive.

**Type:** OBJECT

</details>

## list_global_tables

Lists all global tables that have a replica in the specified region. https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListGlobalTables.html

<details><summary>Parameters</summary>

#### RegionName

Lists the global tables in a specific region.

**Type:** STRING

</details>

## list_tables

Returns an array of table names associated with the current account and endpoint. The output from ListTables is paginated, with each page returning a maximum of 100 table names.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTables.html

*This operation has no parameters*

## list_tags_of_resource

List all tags on an Amazon DynamoDB resource. You can call ListTagsOfResource up to 10 times per second, per account.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTagsOfResource.html

<details><summary>Parameters</summary>

#### ResourceArn (required)

The Amazon DynamoDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).

**Type:** STRING

</details>

## put_item

Creates a new item, or replaces an old item with a new item. If an item that has the same primary key as the new item already exists in the specified table, the new item completely replaces the existing item. You can perform a conditional put operation (add a new item if one with the specified primary key doesn't exist), or replace an existing item if it has certain attribute values. You can return the item's attribute values in the same operation, using the ReturnValues parameter.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html

<details><summary>Parameters</summary>

#### Item (required)

A map of attribute name/value pairs, one for each attribute. Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item. You must provide all of the attributes for the primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide both values for both the partition key and the sort key. If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table's attribute definition. For more information about primary keys, see Primary Key in the Amazon DynamoDB Developer Guide. Each element in the Item map is an AttributeValue object.

**Type:** OBJECT

#### TableName (required)

The name of the table to contain the item.

**Type:** STRING

#### ConditionExpression

A condition that must be satisfied in order for a conditional PutItem operation to succeed. An expression can contain any of the following: Functions: attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size These function names are case-sensitive. Comparison operators: = | <> | < | > | <= | >= | BETWEEN | IN  Logical operators: AND | OR | NOT For more information on condition expressions, see Specifying Conditions in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### ConditionalOperator

This is a legacy parameter.  Use ConditionExpression instead.  For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### Expected

This is a legacy parameter.  Use ConditionExpression instead.  For more information, see Expected in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ExpressionAttributeNames

One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames: To access an attribute whose name conflicts with a DynamoDB reserved word. To create a placeholder for repeating occurrences of an attribute name in an expression. To prevent special characters in an attribute name from being misinterpreted in an expression. Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name: Percentile The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames: {"#P":"Percentile"} You could then use this substitution in an expression, as in this example: #P = :val Note Tokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime. For more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ExpressionAttributeValues

One or more values that can be substituted in an expression. Use the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:  Available | Backordered | Discontinued You would first need to specify ExpressionAttributeValues as follows: { ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} } You could then use these values in an expression, such as this: ProductStatus IN (:avail, :back, :disc) For more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ReturnConsumedCapacity

Determines the level of detail about provisioned throughput consumption that is returned in the response: INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem, do not access any indexes at all.  In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s). TOTAL - The response includes only the aggregate ConsumedCapacity for the operation. NONE - No ConsumedCapacity details are included in the response.

**Type:** STRING

#### ReturnItemCollectionMetrics

Determines whether item collection metrics are returned.  If set to SIZE, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.

**Type:** STRING

#### ReturnValues

Use ReturnValues if you want to get the item attributes as they appeared before they were updated with the PutItem request. For PutItem, the valid values are: NONE - If ReturnValues is not specified, or if its value is NONE, then nothing is returned. (This setting is the default for ReturnValues.) ALL_OLD - If PutItem overwrote an attribute name-value pair, then the content of the old item is returned. Note The ReturnValues parameter is used by several DynamoDB operations; however, PutItem does not recognize any values other than NONE or ALL_OLD.

**Type:** STRING

</details>

## query

The Query operation finds items based on primary key values. You can query any table or secondary index that has a composite primary key (a partition key and a sort key).  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html

<details><summary>Parameters</summary>

#### TableName (required)

The name of the table containing the requested items.

**Type:** STRING

#### AttributesToGet

This is a legacy parameter.  Use ProjectionExpression instead.  For more information, see AttributesToGet in the Amazon DynamoDB Developer Guide.

**Type:** ARRAY

#### ConditionalOperator

This is a legacy parameter.  Use FilterExpression instead.  For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### ConsistentRead

Determines the read consistency model:  If set to true, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads. Strongly consistent reads are not supported on global secondary indexes. If you query a global secondary index with ConsistentRead set to true, you will receive a ValidationException.

**Type:** BOOLEAN

#### ExclusiveStartKey

The primary key of the first item that this operation will evaluate. Use the value that was returned for LastEvaluatedKey in the previous operation. The data type for ExclusiveStartKey must be String, Number or Binary. No set data types are allowed.

**Type:** OBJECT

#### ExpressionAttributeNames

One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames: To access an attribute whose name conflicts with a DynamoDB reserved word. To create a placeholder for repeating occurrences of an attribute name in an expression. To prevent special characters in an attribute name from being misinterpreted in an expression. Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name: Percentile The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames: {"#P":"Percentile"} You could then use this substitution in an expression, as in this example: #P = :val Note Tokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime. For more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ExpressionAttributeValues

One or more values that can be substituted in an expression. Use the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:  Available | Backordered | Discontinued You would first need to specify ExpressionAttributeValues as follows: { ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} } You could then use these values in an expression, such as this: ProductStatus IN (:avail, :back, :disc) For more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### FilterExpression

A string that contains conditions that DynamoDB applies after the Query operation, but before the data is returned to you. Items that do not satisfy the FilterExpression criteria are not returned. A FilterExpression does not allow key attributes.  You cannot define a filter expression based on a partition key or a sort key. Note A FilterExpression is applied after the items have already been read; the process of filtering does not consume any additional read capacity units. For more information, see Filter Expressions in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### IndexName

The name of an index to query. This index can be any local secondary index or global secondary index on the table. Note that if you use the IndexName parameter, you must also provide TableName.

**Type:** STRING

#### KeyConditionExpression

The condition that specifies the key value(s) for items to be retrieved by the Query action. The condition must perform an equality test on a single partition key value. The condition can optionally perform one of several comparison tests on a single sort key value. This allows Query to retrieve one item with a given partition key value and sort key value, or several items that have the same partition key value but different sort key values. The partition key equality test is required, and must be specified in the following format: partitionKeyName = :partitionkeyval If you also want to provide a condition for the sort key, it must be combined using AND with the condition for the sort key. Following is an example, using the = comparison operator for the sort key: partitionKeyName = :partitionkeyval AND sortKeyName = :sortkeyval Valid comparisons for the sort key condition are as follows: sortKeyName = :sortkeyval - true if the sort key value is equal to :sortkeyval. sortKeyName < :sortkeyval - true if the sort key value is less than :sortkeyval. sortKeyName <= :sortkeyval - true if the sort key value is less than or equal to :sortkeyval. sortKeyName > :sortkeyval - true if the sort key value is greater than :sortkeyval. sortKeyName >=  :sortkeyval - true if the sort key value is greater than or equal to :sortkeyval. sortKeyName BETWEEN :sortkeyval1 AND :sortkeyval2 - true if the sort key value is greater than or equal to :sortkeyval1, and less than or equal to :sortkeyval2. begins_with ( sortKeyName, :sortkeyval ) - true if the sort key value begins with a particular operand. (You cannot use this function with a sort key that is of type Number.)  Note that the function name begins_with is case-sensitive. Use the ExpressionAttributeValues parameter to replace tokens such as :partitionval and :sortval with actual values at runtime. You can optionally use the ExpressionAttributeNames parameter to replace the names of the partition key and sort key with placeholder tokens. This option might be necessary if an attribute name conflicts with a DynamoDB reserved word. For example, the following KeyConditionExpression parameter causes an error because Size is a reserved word: Size = :myval To work around this, define a placeholder (such a #S) to represent the attribute name Size. KeyConditionExpression then is as follows: #S = :myval For a list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide. For more information on ExpressionAttributeNames and ExpressionAttributeValues, see Using Placeholders for Attribute Names and Values in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### KeyConditions

This is a legacy parameter.  Use KeyConditionExpression instead.   For more information, see KeyConditions in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### Limit

The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, and a key in LastEvaluatedKey to apply in a subsequent operation, so that you can pick up where you left off. Also, if the processed data set size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in LastEvaluatedKey to apply in a subsequent operation to continue the operation. For more information, see Query and Scan in the Amazon DynamoDB Developer Guide.

**Type:** INTEGER

#### ProjectionExpression

A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result. For more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### QueryFilter

This is a legacy parameter.  Use FilterExpression instead.   For more information, see QueryFilter in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ReturnConsumedCapacity

Determines the level of detail about provisioned throughput consumption that is returned in the response: INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem, do not access any indexes at all.  In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s). TOTAL - The response includes only the aggregate ConsumedCapacity for the operation. NONE - No ConsumedCapacity details are included in the response.

**Type:** STRING

#### ScanIndexForward

Specifies the order for index traversal: If true (default), the traversal is performed in ascending order; if false, the traversal is performed in descending order.  Items with the same partition key value are stored in sorted order by sort key. If the sort key data type is Number, the results are stored in numeric order. For type String, the results are stored in order of UTF-8 bytes. For type Binary, DynamoDB treats each byte of the binary data as unsigned. If ScanIndexForward is true, DynamoDB returns the results in the order in which they are stored (by sort key value). This is the default behavior. If ScanIndexForward is false, DynamoDB reads the results in reverse order by sort key value, and then returns the results to the client.

**Type:** BOOLEAN

#### Select

The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index. ALL_ATTRIBUTES - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index DynamoDB will fetch the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required. ALL_PROJECTED_ATTRIBUTES - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying ALL_ATTRIBUTES. COUNT - Returns the number of matching items, rather than the matching items themselves. SPECIFIC_ATTRIBUTES - Returns only the attributes listed in AttributesToGet. This return value is equivalent to specifying AttributesToGet without specifying any value for Select. If you query or scan a local secondary index and request only attributes that are projected into that index, the operation will read only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB will fetch each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency. If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table. If neither Select nor AttributesToGet are specified, DynamoDB defaults to ALL_ATTRIBUTES when accessing a table, and ALL_PROJECTED_ATTRIBUTES when accessing an index. You cannot use both Select and AttributesToGet together in a single request, unless the value for Select is SPECIFIC_ATTRIBUTES. (This usage is equivalent to specifying AttributesToGet without any value for Select.) Note If you use the ProjectionExpression parameter, then the value for Select can only be SPECIFIC_ATTRIBUTES. Any other value for Select will return an error.

**Type:** STRING

</details>

## restore_table_from_backup

Creates a new table from an existing backup. Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreTableFromBackup.html

<details><summary>Parameters</summary>

#### BackupArn (required)

The ARN associated with the backup.

**Type:** STRING

#### TargetTableName (required)

The name of the new table to which the backup must be restored.

**Type:** STRING

</details>

## restore_table_to_point_in_time

Restores the specified table to the specified point in time within EarliestRestorableDateTime and LatestRestorableDateTime. You can restore your table to any point in time during the last 35 days. Any number of users can execute up to 4 concurrent restores (any type of restore) in a given account.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreTableToPointInTime.html

<details><summary>Parameters</summary>

#### SourceTableName (required)

Name of the source table that is being restored.

**Type:** STRING

#### TargetTableName (required)

The name of the new table to which it must be restored to.

**Type:** STRING

#### RestoreDateTime

Time in the past to restore the table to.

**Type:** OBJECT

#### UseLatestRestorableTime

Restore the table to the latest possible time. LatestRestorableDateTime is typically 5 minutes before the current time.

**Type:** BOOLEAN

</details>

## scan

The Scan operation returns one or more items and item attributes by accessing every item in a table or a secondary index. To have DynamoDB return fewer items, you can provide a FilterExpression operation.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html

<details><summary>Parameters</summary>

#### TableName (required)

The name of the table containing the requested items; or, if you provide IndexName, the name of the table to which that index belongs.

**Type:** STRING

#### AttributesToGet

This is a legacy parameter.  Use ProjectionExpression instead.  For more information, see AttributesToGet in the Amazon DynamoDB Developer Guide.

**Type:** ARRAY

#### ConditionalOperator

This is a legacy parameter.  Use FilterExpression instead.   For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### ConsistentRead

A Boolean value that determines the read consistency model during the scan: If ConsistentRead is false, then the data returned from Scan might not contain the results from other recently completed write operations (PutItem, UpdateItem or DeleteItem). If ConsistentRead is true, then all of the write operations that completed before the Scan began are guaranteed to be contained in the Scan response. The default setting for ConsistentRead is false. The ConsistentRead parameter is not supported on global secondary indexes. If you scan a global secondary index with ConsistentRead set to true, you will receive a ValidationException.

**Type:** BOOLEAN

#### ExclusiveStartKey

The primary key of the first item that this operation will evaluate. Use the value that was returned for LastEvaluatedKey in the previous operation. The data type for ExclusiveStartKey must be String, Number or Binary. No set data types are allowed. In a parallel scan, a Scan request that includes ExclusiveStartKey must specify the same segment whose previous Scan returned the corresponding value of LastEvaluatedKey.

**Type:** OBJECT

#### ExpressionAttributeNames

One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames: To access an attribute whose name conflicts with a DynamoDB reserved word. To create a placeholder for repeating occurrences of an attribute name in an expression. To prevent special characters in an attribute name from being misinterpreted in an expression. Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name: Percentile The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames: {"#P":"Percentile"} You could then use this substitution in an expression, as in this example: #P = :val Note Tokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime. For more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ExpressionAttributeValues

One or more values that can be substituted in an expression. Use the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:  Available | Backordered | Discontinued You would first need to specify ExpressionAttributeValues as follows: { ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} } You could then use these values in an expression, such as this: ProductStatus IN (:avail, :back, :disc) For more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### FilterExpression

A string that contains conditions that DynamoDB applies after the Scan operation, but before the data is returned to you. Items that do not satisfy the FilterExpression criteria are not returned. Note A FilterExpression is applied after the items have already been read; the process of filtering does not consume any additional read capacity units. For more information, see Filter Expressions in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### IndexName

The name of a secondary index to scan. This index can be any local secondary index or global secondary index.  Note that if you use the IndexName parameter, you must also provide TableName.

**Type:** STRING

#### Limit

The maximum number of items to evaluate (not necessarily the number of matching items). If DynamoDB processes the number of items up to the limit while processing the results, it stops the operation and returns the matching values up to that point, and a key in LastEvaluatedKey to apply in a subsequent operation, so that you can pick up where you left off. Also, if the processed data set size exceeds 1 MB before DynamoDB reaches this limit, it stops the operation and returns the matching values up to the limit, and a key in LastEvaluatedKey to apply in a subsequent operation to continue the operation. For more information, see Query and Scan in the Amazon DynamoDB Developer Guide.

**Type:** INTEGER

#### ProjectionExpression

A string that identifies one or more attributes to retrieve from the specified table or index. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result. For more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### ReturnConsumedCapacity

Determines the level of detail about provisioned throughput consumption that is returned in the response: INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem, do not access any indexes at all.  In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s). TOTAL - The response includes only the aggregate ConsumedCapacity for the operation. NONE - No ConsumedCapacity details are included in the response.

**Type:** STRING

#### ScanFilter

This is a legacy parameter.  Use FilterExpression instead.   For more information, see ScanFilter in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### Segment

For a parallel Scan request, Segment identifies an individual segment to be scanned by an application worker. Segment IDs are zero-based, so the first segment is always 0. For example, if you want to use four application threads to scan a table or an index, then the first thread specifies a Segment value of 0, the second thread specifies 1, and so on. The value of LastEvaluatedKey returned from a parallel Scan request must be used as ExclusiveStartKey with the same segment ID in a subsequent Scan operation. The value for Segment must be greater than or equal to 0, and less than the value provided for TotalSegments. If you provide Segment, you must also provide TotalSegments.

**Type:** INTEGER

#### Select

The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index. ALL_ATTRIBUTES - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index DynamoDB will fetch the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required. ALL_PROJECTED_ATTRIBUTES - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying ALL_ATTRIBUTES. COUNT - Returns the number of matching items, rather than the matching items themselves. SPECIFIC_ATTRIBUTES - Returns only the attributes listed in AttributesToGet. This return value is equivalent to specifying AttributesToGet without specifying any value for Select. If you query or scan a local secondary index and request only attributes that are projected into that index, the operation will read only the index and not the table. If any of the requested attributes are not projected into the local secondary index, DynamoDB will fetch each of these attributes from the parent table. This extra fetching incurs additional throughput cost and latency. If you query or scan a global secondary index, you can only request attributes that are projected into the index. Global secondary index queries cannot fetch attributes from the parent table. If neither Select nor AttributesToGet are specified, DynamoDB defaults to ALL_ATTRIBUTES when accessing a table, and ALL_PROJECTED_ATTRIBUTES when accessing an index. You cannot use both Select and AttributesToGet together in a single request, unless the value for Select is SPECIFIC_ATTRIBUTES. (This usage is equivalent to specifying AttributesToGet without any value for Select.) Note If you use the ProjectionExpression parameter, then the value for Select can only be SPECIFIC_ATTRIBUTES. Any other value for Select will return an error.

**Type:** STRING

#### TotalSegments

For a parallel Scan request, TotalSegments represents the total number of segments into which the Scan operation will be divided. The value of TotalSegments corresponds to the number of application workers that will perform the parallel scan. For example, if you want to use four application threads to scan a table or an index, specify a TotalSegments value of 4. The value for TotalSegments must be greater than or equal to 1, and less than or equal to 1000000. If you specify a TotalSegments value of 1, the Scan operation will be sequential rather than parallel. If you specify TotalSegments, you must also specify Segment.

**Type:** INTEGER

</details>

## tag_resource

Associate a set of tags with an Amazon DynamoDB resource. You can then activate these user-defined tags so that they appear on the Billing and Cost Management console for cost allocation tracking. You can call TagResource up to 5 times per second, per account.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TagResource.html

<details><summary>Parameters</summary>

#### ResourceArn (required)

Identifies the Amazon DynamoDB resource to which tags should be added. This value is an Amazon Resource Name (ARN).

**Type:** STRING

#### Tags (required)

The tags to be assigned to the Amazon DynamoDB resource.

**Type:** ARRAY

</details>

## transact_get_items

 TransactGetItems is a synchronous operation that atomically retrieves multiple items from one or more tables (but not from indexes) in a single account and region. A TransactGetItems call can contain up to 10 TransactGetItem objects, each of which contains a Get structure that specifies an item to retrieve from a table in the account and region. A call to TransactGetItems cannot retrieve items from tables in more than one AWS account or region.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactGetItems.html

<details><summary>Parameters</summary>

#### TransactItems (required)

An ordered array of up to 10 TransactGetItem objects, each of which contains a Get structure.

**Type:** ARRAY

#### ReturnConsumedCapacity

A value of TOTAL causes consumed capacity information to be returned, and a value of NONE prevents that information from being returned. No other value is valid.

**Type:** STRING

</details>

## transact_write_items

 TransactWriteItems is a synchronous write operation that groups up to 10 action requests. These actions can target items in different tables, but not in different AWS accounts or regions, and no two actions can target the same item. For example, you cannot both ConditionCheck and Update the same item.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TransactWriteItems.html

<details><summary>Parameters</summary>

#### TransactItems (required)

An ordered array of up to 10 TransactWriteItem objects, each of which contains a ConditionCheck, Put, Update, or Delete object. These can operate on items in different tables, but the tables must reside in the same AWS account and region, and no two of them can operate on the same item.

**Type:** ARRAY

#### ClientRequestToken

Providing a ClientRequestToken makes the call to TransactWriteItems idempotent, meaning that multiple identical calls have the same effect as one single call. Although multiple identical calls using the same client request token produce the same result on the server (no side effects), the responses to the calls may not be the same. If the ReturnConsumedCapacity> parameter is set, then the initial TransactWriteItems call returns the amount of write capacity units consumed in making the changes, and subsequent TransactWriteItems calls with the same client token return the amount of read capacity units consumed in reading the item. A client request token is valid for 10 minutes after the first request that uses it completes. After 10 minutes, any request with the same client token is treated as a new request. Do not resubmit the same request with the same client token for more than 10 minutes or the result may not be idempotent. If you submit a request with the same client token but a change in other parameters within the 10 minute idempotency window, DynamoDB returns an IdempotentParameterMismatch exception.

**Type:** STRING

#### ReturnConsumedCapacity

Determines the level of detail about provisioned throughput consumption that is returned in the response: INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem, do not access any indexes at all.  In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s). TOTAL - The response includes only the aggregate ConsumedCapacity for the operation. NONE - No ConsumedCapacity details are included in the response.

**Type:** STRING

#### ReturnItemCollectionMetrics

Determines whether item collection metrics are returned. If set to SIZE, the response includes statistics about item collections (if any), that were modified during the operation and are returned in the response. If set to NONE (the default), no statistics are returned.

**Type:** STRING

</details>

## untag_resource

Removes the association of tags from an Amazon DynamoDB resource. You can call UntagResource up to 5 times per second, per account.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UntagResource.html

<details><summary>Parameters</summary>

#### ResourceArn (required)

The Amazon DyanamoDB resource the tags will be removed from. This value is an Amazon Resource Name (ARN).

**Type:** STRING

#### TagKeys (required)

A list of tag keys. Existing tags of the resource whose keys are members of this list will be removed from the Amazon DynamoDB resource.

**Type:** ARRAY

</details>

## update_continuous_backups

 UpdateContinuousBackups enables or disables point in time recovery for the specified table. A successful UpdateContinuousBackups call returns the current ContinuousBackupsDescription. Continuous backups are ENABLED on all tables at table creation. If point in time recovery is enabled, PointInTimeRecoveryStatus will be set to ENABLED.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateContinuousBackups.html

<details><summary>Parameters</summary>

#### PointInTimeRecoverySpecification (required)

Represents the settings used to enable point in time recovery.

**Type:** OBJECT

#### TableName (required)

The name of the table.

**Type:** STRING

</details>

## update_global_table

Adds or removes replicas in the specified global table. The global table must already exist to be able to use this operation. Any replica to be added must be empty, must have the same name as the global table, must have the same key schema, and must have DynamoDB Streams enabled and must have same provisioned and maximum write capacity units.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalTable.html

<details><summary>Parameters</summary>

#### GlobalTableName (required)

The global table name.

**Type:** STRING

#### ReplicaUpdates (required)

A list of regions that should be added or removed from the global table.

**Type:** ARRAY

</details>

## update_global_table_settings

Updates settings for a global table. https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateGlobalTableSettings.html

<details><summary>Parameters</summary>

#### GlobalTableName (required)

The name of the global table

**Type:** STRING

#### GlobalTableBillingMode

The billing mode of the global table. If GlobalTableBillingMode is not specified, the global table defaults to PROVISIONED capacity billing mode.

**Type:** STRING

#### GlobalTableGlobalSecondaryIndexSettingsUpdate

Represents the settings of a global secondary index for a global table that will be modified.

**Type:** ARRAY

#### GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate

AutoScaling settings for managing provisioned write capacity for the global table.

**Type:** OBJECT

#### GlobalTableProvisionedWriteCapacityUnits

The maximum number of writes consumed per second before DynamoDB returns a ThrottlingException.

**Type:** OBJECT

#### ReplicaSettingsUpdate

Represents the settings for a global table in a region that will be modified.

**Type:** ARRAY

</details>

## update_item

Edits an existing item's attributes, or adds a new item to the table if it does not already exist. You can put, delete, or add attribute values. You can also perform a conditional update on an existing item (insert a new attribute name-value pair if it doesn't exist, or replace an existing name-value pair if it has certain expected attribute values).  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html

<details><summary>Parameters</summary>

#### Key (required)

The primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute. For the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.

**Type:** OBJECT

#### TableName (required)

The name of the table containing the item to update.

**Type:** STRING

#### AttributeUpdates

This is a legacy parameter.  Use UpdateExpression instead.   For more information, see AttributeUpdates in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ConditionExpression

A condition that must be satisfied in order for a conditional update to succeed. An expression can contain any of the following: Functions: attribute_exists | attribute_not_exists | attribute_type | contains | begins_with | size These function names are case-sensitive. Comparison operators: = | <> | < | > | <= | >= | BETWEEN | IN  Logical operators: AND | OR | NOT For more information on condition expressions, see Specifying Conditions in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### ConditionalOperator

This is a legacy parameter.  Use ConditionExpression instead.   For more information, see ConditionalOperator in the Amazon DynamoDB Developer Guide.

**Type:** STRING

#### Expected

This is a legacy parameter.  Use ConditionExpression instead.   For more information, see Expected in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ExpressionAttributeNames

One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames: To access an attribute whose name conflicts with a DynamoDB reserved word. To create a placeholder for repeating occurrences of an attribute name in an expression. To prevent special characters in an attribute name from being misinterpreted in an expression. Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name: Percentile The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide). To work around this, you could specify the following for ExpressionAttributeNames: {"#P":"Percentile"} You could then use this substitution in an expression, as in this example: #P = :val Note Tokens that begin with the : character are expression attribute values, which are placeholders for the actual value at runtime. For more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ExpressionAttributeValues

One or more values that can be substituted in an expression. Use the : (colon) character in an expression to dereference an attribute value. For example, suppose that you wanted to check whether the value of the ProductStatus attribute was one of the following:  Available | Backordered | Discontinued You would first need to specify ExpressionAttributeValues as follows: { ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} } You could then use these values in an expression, such as this: ProductStatus IN (:avail, :back, :disc) For more information on expression attribute values, see Specifying Conditions in the Amazon DynamoDB Developer Guide.

**Type:** OBJECT

#### ReturnConsumedCapacity

Determines the level of detail about provisioned throughput consumption that is returned in the response: INDEXES - The response includes the aggregate ConsumedCapacity for the operation, together with ConsumedCapacity for each table and secondary index that was accessed. Note that some operations, such as GetItem and BatchGetItem, do not access any indexes at all.  In these cases, specifying INDEXES will only return ConsumedCapacity information for table(s). TOTAL - The response includes only the aggregate ConsumedCapacity for the operation. NONE - No ConsumedCapacity details are included in the response.

**Type:** STRING

#### ReturnItemCollectionMetrics

Determines whether item collection metrics are returned.  If set to SIZE, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to NONE (the default), no statistics are returned.

**Type:** STRING

#### ReturnValues

Use ReturnValues if you want to get the item attributes as they appear before or after they are updated. For UpdateItem, the valid values are: NONE - If ReturnValues is not specified, or if its value is NONE, then nothing is returned. (This setting is the default for ReturnValues.) ALL_OLD - Returns all of the attributes of the item, as they appeared before the UpdateItem operation. UPDATED_OLD - Returns only the updated attributes, as they appeared before the UpdateItem operation. ALL_NEW - Returns all of the attributes of the item, as they appear after the UpdateItem operation. UPDATED_NEW - Returns only the updated attributes, as they appear after the UpdateItem operation. There is no additional cost associated with requesting a return value aside from the small network and processing overhead of receiving a larger response. No read capacity units are consumed. The values returned are strongly consistent.

**Type:** STRING

#### UpdateExpression

An expression that defines one or more attributes to be updated, the action to be performed on them, and new value(s) for them. The following action values are available for UpdateExpression. SET - Adds one or more attributes and values to an item. If any of these attribute already exist, they are replaced by the new values. You can also use SET to add or subtract from an attribute that is of type Number.  For example: SET myNum = myNum + :val SET supports the following functions: if_not_exists (path, operand) - if the item does not contain an attribute at the specified path, then if_not_exists evaluates to operand; otherwise, it evaluates to path. You can use this function to avoid overwriting an attribute that may already be present in the item. list_append (operand, operand) - evaluates to a list with a new element added to it. You can append the new element to the start or the end of the list by reversing the order of the operands. These function names are case-sensitive. REMOVE - Removes one or more attributes from an item. ADD - Adds the specified value to the item, if the attribute does not already exist. If the attribute does exist, then the behavior of ADD depends on the data type of the attribute: If the existing attribute is a number, and if Value is also a number, then Value is mathematically added to the existing attribute. If Value is a negative number, then it is subtracted from the existing attribute. Note If you use ADD to increment or decrement a number value for an item that doesn't exist before the update, DynamoDB uses 0 as the initial value. Similarly, if you use ADD for an existing item to increment or decrement an attribute value that doesn't exist before the update, DynamoDB uses 0 as the initial value. For example, suppose that the item you want to update doesn't have an attribute named itemcount, but you decide to ADD the number 3 to this attribute anyway. DynamoDB will create the itemcount attribute, set its initial value to 0, and finally add 3 to it. The result will be a new itemcount attribute in the item, with a value of 3. If the existing data type is a set and if Value is also a set, then Value is added to the existing set. For example, if the attribute value is the set [1,2], and the ADD action specified [3], then the final attribute value is [1,2,3]. An error occurs if an ADD action is specified for a set attribute and the attribute type specified does not match the existing set type.  Both sets must have the same primitive data type. For example, if the existing data type is a set of strings, the Value must also be a set of strings. Important The ADD action only supports Number and set data types. In addition, ADD can only be used on top-level attributes, not nested attributes. DELETE - Deletes an element from a set. If a set of values is specified, then those values are subtracted from the old set. For example, if the attribute value was the set [a,b,c] and the DELETE action specifies [a,c], then the final attribute value is [b]. Specifying an empty set is an error. Important The DELETE action only supports set data types. In addition, DELETE can only be used on top-level attributes, not nested attributes. You can have many actions in a single expression, such as the following: SET a=:value1, b=:value2 DELETE :value3, :value4, :value5 For more information on update expressions, see Modifying Items and Attributes in the Amazon DynamoDB Developer Guide.

**Type:** STRING

</details>

## update_table

Modifies the provisioned throughput settings, global secondary indexes, or DynamoDB Streams settings for a given table.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html

<details><summary>Parameters</summary>

#### TableName (required)

The name of the table to be updated.

**Type:** STRING

#### AttributeDefinitions

An array of attributes that describe the key schema for the table and indexes. If you are adding a new global secondary index to the table, AttributeDefinitions must include the key element(s) of the new index.

**Type:** ARRAY

#### BillingMode

Controls how you are charged for read and write throughput and how you manage capacity. When switching from pay-per-request to provisioned capacity, initial provisioned capacity values must be set. The initial provisioned capacity values are estimated based on the consumed read and write capacity of your table and global secondary indexes  over the past 30 minutes. PROVISIONED - Sets the billing mode to PROVISIONED. We recommend using PROVISIONED for predictable workloads. PAY_PER_REQUEST - Sets the billing mode to PAY_PER_REQUEST. We recommend using PAY_PER_REQUEST for unpredictable workloads.

**Type:** STRING

#### GlobalSecondaryIndexUpdates

An array of one or more global secondary indexes for the table. For each index in the array, you can request one action: Create - add a new global secondary index to the table. Update - modify the provisioned throughput settings of an existing global secondary index. Delete - remove a global secondary index from the table. For more information, see Managing Global Secondary Indexes in the Amazon DynamoDB Developer Guide.

**Type:** ARRAY

#### ProvisionedThroughput

The new provisioned throughput settings for the specified table or index.

**Type:** OBJECT

#### SSESpecification

The new server-side encryption settings for the specified table.

**Type:** OBJECT

#### StreamSpecification

Represents the DynamoDB Streams configuration for the table. Note You will receive a ResourceInUseException if you attempt to enable a stream on a table that already has a stream, or if you attempt to disable a stream on a table which does not have a stream.

**Type:** OBJECT

</details>

## update_time_to_live

The UpdateTimeToLive method will enable or disable TTL for the specified table. A successful UpdateTimeToLive call returns the current TimeToLiveSpecification; it may take up to one hour for the change to fully process. Any additional UpdateTimeToLive calls for the same table during this one hour duration result in a ValidationException.  https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTimeToLive.html

<details><summary>Parameters</summary>

#### TableName (required)

The name of the table to be configured.

**Type:** STRING

#### TimeToLiveSpecification (required)

Represents the settings used to enable or disable Time to Live for the specified table.

**Type:** OBJECT

</details>

