---
id: aws-sqs-documentation
title: AWS SQS (version v1.*.*)
sidebar_label: AWS SQS
---

## add_permission

Adds a permission to a queue for a specific principal. This allows sharing access to the queue.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_AddPermission.html

<details><summary>Parameters</summary>

#### AWSAccountId (required)

The AWS account number of the principal who is given permission. The principal must have an AWS account, but does not need to be signed up for Amazon SQS. For information about locating the AWS account identification, see Your AWS Identifiers in the Amazon Simple Queue Service Developer Guide.

**Type:** ARRAY

#### ActionName (required)

The action the client wants to allow for the specified principal. Valid values: the name of any action or *. For more information about these actions, see Overview of Managing Access Permissions to Your Amazon Simple Queue Service Resource  in the Amazon Simple Queue Service Developer Guide. Specifying SendMessage, DeleteMessage, or ChangeMessageVisibility for ActionName also grants permissions for the corresponding batch versions of those actions: SendMessageBatch, DeleteMessageBatch, and ChangeMessageVisibilityBatch.

**Type:** ARRAY

#### Label (required)

The unique identification of the permission you're setting (for example, AliceSendMessage). Maximum 80 characters. Allowed characters include alphanumeric characters, hyphens (-), and underscores (_).

**Type:** STRING

#### QueueUrl (required)

The URL of the Amazon SQS queue to which permissions are added. Queue URLs and names are case-sensitive.

**Type:** STRING

</details>

## change_message_visibility

Changes the visibility timeout of a specified message in a queue to a new value. The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours. For more information, see Visibility Timeout in the Amazon Simple Queue Service Developer Guide.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibility.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the Amazon SQS queue whose message's visibility is changed. Queue URLs and names are case-sensitive.

**Type:** STRING

#### ReceiptHandle (required)

The receipt handle associated with the message whose visibility timeout is changed. This parameter is returned by the  ReceiveMessage action.

**Type:** STRING

#### VisibilityTimeout (required)

The new value for the message's visibility timeout (in seconds). Values values: 0 to 43200. Maximum: 12 hours.

**Type:** INTEGER

</details>

## change_message_visibility_batch

Changes the visibility timeout of multiple messages. This is a batch version of ChangeMessageVisibility. The result of the action on each message is reported individually in the response. You can send up to 10 ChangeMessageVisibility requests with each ChangeMessageVisibilityBatch action.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibilityBatch.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the Amazon SQS queue whose messages' visibility is changed. Queue URLs and names are case-sensitive.

**Type:** STRING

#### ChangeMessageVisibilityBatchRequestEntry

A list of receipt handles of the messages for which the visibility timeout must be changed.

**Type:** ARRAY

</details>

## create_queue

Creates a new standard or FIFO queue. You can pass one or more attributes in the request. Keep the following caveats in mind:  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html

<details><summary>Parameters</summary>

#### QueueName (required)

The name of the new queue. The following limits apply to this name: A queue name can have up to 80 characters. Valid values: alphanumeric characters, hyphens (-), and underscores (_). A FIFO queue name must end with the .fifo suffix. Queue URLs and names are case-sensitive.

**Type:** STRING

#### Attribute

A map of attributes with their corresponding values.

**Type:** OBJECT

</details>

## delete_message

Deletes the specified message from the specified queue. To select the message to delete, use the ReceiptHandle of the message (not the MessageId which you receive when you send the message). Amazon SQS can delete a message from a queue even if a visibility timeout setting causes the message to be locked by another consumer. Amazon SQS automatically deletes messages left in a queue longer than the retention period configured for the queue.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the Amazon SQS queue from which messages are deleted. Queue URLs and names are case-sensitive.

**Type:** STRING

#### ReceiptHandle (required)

The receipt handle associated with the message to delete.

**Type:** STRING

</details>

## delete_message_batch

Deletes up to ten messages from the specified queue. This is a batch version of DeleteMessage. The result of the action on each message is reported individually in the response.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessageBatch.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the Amazon SQS queue from which messages are deleted. Queue URLs and names are case-sensitive.

**Type:** STRING

#### DeleteMessageBatchRequestEntry

A list of receipt handles for the messages to be deleted.

**Type:** ARRAY

</details>

## delete_queue

Deletes the queue specified by the QueueUrl, regardless of the queue's contents. If the specified queue doesn't exist, Amazon SQS returns a successful response.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the Amazon SQS queue to delete. Queue URLs and names are case-sensitive.

**Type:** STRING

</details>

## get_queue_attributes

Gets attributes for the specified queue. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the Amazon SQS queue whose attribute information is retrieved. Queue URLs and names are case-sensitive.

**Type:** STRING

#### AttributeName

A list of attributes for which to retrieve information.

**Type:** ARRAY

</details>

## get_queue_url

Returns the URL of an existing Amazon SQS queue. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html

<details><summary>Parameters</summary>

#### QueueName (required)

The name of the queue whose URL must be fetched. Maximum 80 characters. Valid values: alphanumeric characters, hyphens (-), and underscores (_). Queue URLs and names are case-sensitive.

**Type:** STRING

#### QueueOwnerAWSAccountId

The AWS account ID of the account that created the queue.

**Type:** STRING

</details>

## list_dead_letter_source_queues

Returns a list of your queues that have the RedrivePolicy queue attribute configured with a dead-letter queue.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListDeadLetterSourceQueues.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of a dead-letter queue. Queue URLs and names are case-sensitive.

**Type:** STRING

</details>

## list_queue_tags

List all cost allocation tags added to the specified Amazon SQS queue. For an overview, see Tagging Your Amazon SQS Queues in the Amazon Simple Queue Service Developer Guide.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the queue.

**Type:** STRING

</details>

## list_queues

Returns a list of your queues. The maximum number of queues that can be returned is 1,000. If you specify a value for the optional QueueNamePrefix parameter, only queues with a name that begins with the specified value are returned.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html

<details><summary>Parameters</summary>

#### QueueNamePrefix

A string to use for filtering the list results. Only those queues whose name begins with the specified string are returned. Queue URLs and names are case-sensitive.

**Type:** STRING

</details>

## purge_queue

Deletes the messages in a queue specified by the QueueURL parameter.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_PurgeQueue.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the queue from which the PurgeQueue action deletes messages. Queue URLs and names are case-sensitive.

**Type:** STRING

</details>

## receive_message

Retrieves one or more messages (up to 10), from the specified queue. Using the WaitTimeSeconds parameter enables long-poll support. For more information, see Amazon SQS Long Polling in the Amazon Simple Queue Service Developer Guide.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the Amazon SQS queue from which messages are received. Queue URLs and names are case-sensitive.

**Type:** STRING

#### AttributeName

A list of attributes that need to be returned along with each message.

**Type:** ARRAY

#### MaxNumberOfMessages

The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10. Default: 1.

**Type:** INTEGER

#### MessageAttributeName

An array of names of the message attributes. The name can contain alphanumeric characters and the underscore (_), hyphen (-), and period (.). The name is case-sensitive and must be unique among all attribute names for the message. The name must not start with AWS-reserved prefixes such as AWS. or Amazon. (or any casing variants). The name must not start or end with a period (.), and it should not have periods in succession (..). The name can be up to 256 characters long. When using ReceiveMessage, you can send a list of attribute names to receive, or you can return all of the attributes by specifying All or .* in your request.  You can also use all message attributes starting with a prefix, for example bar.*.

**Type:** ARRAY

#### ReceiveRequestAttemptId

This parameter applies only to FIFO (first-in-first-out) queues. The token used for deduplication of ReceiveMessage calls. If a networking issue occurs after a ReceiveMessage action, and instead of a response you receive a generic error,  you can retry the same action with an identical ReceiveRequestAttemptId to retrieve the same set of messages, even if their visibility timeout has not yet expired. You can use ReceiveRequestAttemptId only for 5 minutes after a ReceiveMessage action. When you set FifoQueue, a caller of the ReceiveMessage action can provide a ReceiveRequestAttemptId explicitly. If a caller of the ReceiveMessage action doesn't provide a ReceiveRequestAttemptId, Amazon SQS generates a ReceiveRequestAttemptId. You can retry the ReceiveMessage action with the same ReceiveRequestAttemptId if none of the messages have been modified (deleted or had their visibility changes). During a visibility timeout, subsequent calls with the same ReceiveRequestAttemptId return the same messages and receipt handles. If a retry occurs within the deduplication interval,  it resets the visibility timeout. For more information, see Visibility Timeout in the Amazon Simple Queue Service Developer Guide. Important If a caller of the ReceiveMessage action still processes messages when the visibility timeout expires and messages become visible, another worker consuming from the same queue can receive the same messages and therefore process duplicates. Also, if a consumer whose message processing time is longer than the visibility timeout tries to delete the processed messages, the action fails with an error. To mitigate this effect, ensure that your application observes a safe threshold before the visibility timeout expires and extend the visibility timeout as necessary. While messages with a particular MessageGroupId are invisible, no more messages belonging to the same MessageGroupId are returned until the visibility timeout expires. You can still receive messages with another MessageGroupId as long as it is also visible. If a caller of ReceiveMessage can't track the ReceiveRequestAttemptId, no retries work until the original visibility timeout expires. As a result, delays might occur but the messages in the queue remain in a strict order. The length of ReceiveRequestAttemptId is 128 characters. ReceiveRequestAttemptId can contain alphanumeric characters (a-z, A-Z, 0-9) and  punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~). For best practices of using ReceiveRequestAttemptId, see Using the ReceiveRequestAttemptId Request Parameter in the Amazon Simple Queue Service Developer Guide.

**Type:** STRING

#### VisibilityTimeout

The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request.

**Type:** INTEGER

#### WaitTimeSeconds

The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than WaitTimeSeconds. If no messages are available and the wait time expires, the call returns successfully with an empty list of messages.

**Type:** INTEGER

</details>

## remove_permission

Revokes any permissions in the queue policy that matches the specified Label parameter.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_RemovePermission.html

<details><summary>Parameters</summary>

#### Label (required)

The identification of the permission to remove. This is the label added using the AddPermission action.

**Type:** STRING

#### QueueUrl (required)

The URL of the Amazon SQS queue from which permissions are removed. Queue URLs and names are case-sensitive.

**Type:** STRING

</details>

## send_message

Delivers a message to the specified queue. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html

<details><summary>Parameters</summary>

#### MessageBody (required)

The message to send. The maximum string size is 256 KB. Important A message can include only XML, JSON, and unformatted text. The following Unicode characters are allowed: #x9 | #xA | #xD | #x20 to #xD7FF | #xE000 to #xFFFD | #x10000 to #x10FFFF Any characters not included in this list will be rejected. For more information, see the W3C specification for characters.

**Type:** STRING

#### QueueUrl (required)

The URL of the Amazon SQS queue to which a message is sent. Queue URLs and names are case-sensitive.

**Type:** STRING

#### DelaySeconds

The length of time, in seconds, for which to delay a specific message. Valid values: 0 to 900. Maximum: 15 minutes. Messages with a positive DelaySeconds value become available for processing after the delay period is finished. If you don't specify a value, the default value for the queue applies. Note When you set FifoQueue, you can't set DelaySeconds per message. You can set this parameter only on a queue level.

**Type:** INTEGER

#### MessageAttribute

Each message attribute consists of a Name, Type, and Value. For more information, see Amazon SQS Message Attributes in the Amazon Simple Queue Service Developer Guide.

**Type:** OBJECT

#### MessageDeduplicationId

This parameter applies only to FIFO (first-in-first-out) queues. The token used for deduplication of sent messages. If a message with a particular MessageDeduplicationId is sent successfully, any messages sent with the same MessageDeduplicationId  are accepted successfully but aren't delivered during the 5-minute deduplication interval. For more information, see  Exactly-Once Processing in the Amazon Simple Queue Service Developer Guide. Every message must have a unique MessageDeduplicationId, You may provide a MessageDeduplicationId explicitly. If you aren't able to provide a MessageDeduplicationId and you enable ContentBasedDeduplication for your queue,  Amazon SQS uses a SHA-256 hash to generate the MessageDeduplicationId using the body of the message (but not the attributes of the message). If you don't provide a MessageDeduplicationId and the queue doesn't have ContentBasedDeduplication set, the action fails with an error. If the queue has ContentBasedDeduplication set, your MessageDeduplicationId overrides the generated one. When ContentBasedDeduplication is in effect, messages with identical content sent within the deduplication interval are treated as duplicates  and only one copy of the message is delivered. If you send one message with ContentBasedDeduplication enabled and then another message with a MessageDeduplicationId that is the same  as the one generated for the first MessageDeduplicationId, the two messages are treated as duplicates and only one copy of the message is delivered. Note The MessageDeduplicationId is available to the consumer of the message (this can be useful for troubleshooting delivery issues). If a message is sent successfully but the acknowledgement is lost and the message is resent with the same  MessageDeduplicationId after the deduplication interval, Amazon SQS can't detect duplicate messages. Amazon SQS continues to keep track of the message deduplication ID even after the message is received and deleted. The length of MessageDeduplicationId is 128 characters. MessageDeduplicationId can contain alphanumeric characters (a-z, A-Z, 0-9) and  punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~). For best practices of using MessageDeduplicationId, see Using the MessageDeduplicationId Property in the Amazon Simple Queue Service Developer Guide.

**Type:** STRING

#### MessageGroupId

This parameter applies only to FIFO (first-in-first-out) queues. The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single queue, use MessageGroupId values (for example, session data for multiple users). In this scenario, multiple consumers can process the queue, but the session data of each user is processed in a FIFO fashion. You must associate a non-empty MessageGroupId with a message. If you don't provide a MessageGroupId, the action fails. ReceiveMessage might return messages with multiple MessageGroupId values. For each MessageGroupId, the messages are sorted by time sent. The caller can't  specify a MessageGroupId. The length of MessageGroupId is 128 characters. Valid values: alphanumeric characters and punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~). For best practices of using MessageGroupId, see Using the MessageGroupId Property in the Amazon Simple Queue Service Developer Guide. Important MessageGroupId is required for FIFO queues. You can't use it for Standard queues.

**Type:** STRING

</details>

## send_message_batch

Delivers up to ten messages to the specified queue. This is a batch version of SendMessage. For a FIFO queue, multiple messages within a single batch are enqueued in the order they are sent.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the Amazon SQS queue to which batched messages are sent. Queue URLs and names are case-sensitive.

**Type:** STRING

#### SendMessageBatchRequestEntry

A list of SendMessageBatchRequestEntry items.

**Type:** ARRAY

</details>

## set_queue_attributes

Sets the value of one or more queue attributes. When you change a queue's attributes, the change can take up to 60 seconds for most of the attributes to propagate throughout the Amazon SQS system. Changes made to the MessageRetentionPeriod attribute can take up to 15 minutes.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html

<details><summary>Parameters</summary>

#### Attribute (required)

A map of attributes with their corresponding values.

**Type:** OBJECT

#### QueueUrl (required)

The URL of the Amazon SQS queue whose attributes are set. Queue URLs and names are case-sensitive.

**Type:** STRING

</details>

## tag_queue

Add cost allocation tags to the specified Amazon SQS queue. For an overview, see Tagging Your Amazon SQS Queues in the Amazon Simple Queue Service Developer Guide.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_TagQueue.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the queue.

**Type:** STRING

#### Tag (required)

The list of tags to be added to the specified queue.

**Type:** OBJECT

</details>

## untag_queue

Remove cost allocation tags from the specified Amazon SQS queue. For an overview, see Tagging Your Amazon SQS Queues in the Amazon Simple Queue Service Developer Guide.  https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_UntagQueue.html

<details><summary>Parameters</summary>

#### QueueUrl (required)

The URL of the queue.

**Type:** STRING

#### TagKey (required)

The list of tags to be removed from the specified queue.

**Type:** ARRAY

</details>

