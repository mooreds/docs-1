---
id: gcp-cloud-storage-documentation
title: GCP Cloud Storage (version v1.*.*)
sidebar_label: GCP Cloud Storage
layout: docs.mustache
---

## copy_object

Copies a source object to a destination object. Optionally overrides metadata.

<details><summary>Parameters</summary>

#### destinationBucket (required)

Name of the bucket in which to store the new object. Overrides the provided object metadata's bucket value, if any.For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### destinationObject (required)

Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any.

**Type:** string

#### sourceBucket (required)

Name of the bucket in which to find the source object.

**Type:** string

#### sourceObject (required)

Name of the source object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### $body

An object.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### destinationPredefinedAcl

Apply a predefined set of access controls to the destination object.

**Type:** string

**Potential values:** authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### ifGenerationMatch

Makes the operation conditional on whether the destination object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.

**Type:** string

#### ifGenerationNotMatch

Makes the operation conditional on whether the destination object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.

**Type:** string

#### ifMetagenerationMatch

Makes the operation conditional on whether the destination object's current metageneration matches the given value.

**Type:** string

#### ifMetagenerationNotMatch

Makes the operation conditional on whether the destination object's current metageneration does not match the given value.

**Type:** string

#### ifSourceGenerationMatch

Makes the operation conditional on whether the source object's current generation matches the given value.

**Type:** string

#### ifSourceGenerationNotMatch

Makes the operation conditional on whether the source object's current generation does not match the given value.

**Type:** string

#### ifSourceMetagenerationMatch

Makes the operation conditional on whether the source object's current metageneration matches the given value.

**Type:** string

#### ifSourceMetagenerationNotMatch

Makes the operation conditional on whether the source object's current metageneration does not match the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### sourceGeneration

If present, selects a specific revision of the source object (as opposed to the latest version, the default).

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## create_bucket

Creates a new bucket.

<details><summary>Parameters</summary>

#### project (required)

A valid API project identifier.

**Type:** string

#### $body

A bucket.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### predefinedAcl

Apply a predefined set of access controls to this bucket.

**Type:** string

**Potential values:** authenticatedRead, private, projectPrivate, publicRead, publicReadWrite

#### predefinedDefaultObjectAcl

Apply a predefined set of default object access controls to this bucket.

**Type:** string

**Potential values:** authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to noAcl, unless the bucket resource specifies acl or defaultObjectAcl properties, when it defaults to full.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request.

**Type:** string

</details>

## create_bucket_access_control

Creates a new ACL entry on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### $body

An access-control entry.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## create_default_object_acl

Creates a new default object ACL entry on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### $body

An access-control entry.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## create_notification_subscription

Creates a notification subscription for a given bucket.

<details><summary>Parameters</summary>

#### bucket (required)

The parent bucket of the notification.

**Type:** string

#### $body

A subscription to receive Google PubSub notifications.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## create_object_access_control

Creates a new ACL entry on the specified object.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### $body

An access-control entry.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## delete_bucket

Permanently deletes an empty bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### ifMetagenerationMatch

If set, only deletes the bucket if its metageneration matches this value.

**Type:** string

#### ifMetagenerationNotMatch

If set, only deletes the bucket if its metageneration does not match this value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## delete_bucket_access_control

Permanently deletes the ACL entry for the specified entity on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## delete_default_object_acl

Permanently deletes the default object ACL entry for the specified entity on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## delete_notification_subscription

Permanently deletes a notification subscription.

<details><summary>Parameters</summary>

#### bucket (required)

The parent bucket of the notification.

**Type:** string

#### notification (required)

ID of the notification to delete.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## delete_object

Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used.

<details><summary>Parameters</summary>

#### bucket (required)

Name of the bucket in which the object resides.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, permanently deletes a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### ifGenerationMatch

Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.

**Type:** string

#### ifGenerationNotMatch

Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.

**Type:** string

#### ifMetagenerationMatch

Makes the operation conditional on whether the object's current metageneration matches the given value.

**Type:** string

#### ifMetagenerationNotMatch

Makes the operation conditional on whether the object's current metageneration does not match the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## delete_object_access_control

Permanently deletes the ACL entry for the specified entity on the specified object.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## get_bucket

Returns metadata for the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### ifMetagenerationMatch

Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.

**Type:** string

#### ifMetagenerationNotMatch

Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to noAcl.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## get_bucket_access_control

Returns the ACL entry for the specified entity on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## get_bucket_iam_policy

Returns an IAM policy for the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## get_default_object_acl

Returns the default object ACL entry for the specified entity on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## get_notification

View a notification configuration.

<details><summary>Parameters</summary>

#### bucket (required)

The parent bucket of the notification.

**Type:** string

#### notification (required)

Notification ID

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## get_object

Retrieves an object or its metadata.

<details><summary>Parameters</summary>

#### bucket (required)

Name of the bucket in which the object resides.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### ifGenerationMatch

Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.

**Type:** string

#### ifGenerationNotMatch

Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.

**Type:** string

#### ifMetagenerationMatch

Makes the operation conditional on whether the object's current metageneration matches the given value.

**Type:** string

#### ifMetagenerationNotMatch

Makes the operation conditional on whether the object's current metageneration does not match the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to noAcl.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## get_object_access_control

Returns the ACL entry for the specified entity on the specified object.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## get_object_iam_policy

Returns an IAM policy for the specified object.

<details><summary>Parameters</summary>

#### bucket (required)

Name of the bucket in which the object resides.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## get_service_account_email

Get the email address of this project's Google Cloud Storage service account.

<details><summary>Parameters</summary>

#### projectId (required)

Project ID

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request.

**Type:** string

</details>

## list_bucket_access_controls

Retrieves ACL entries on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## list_buckets

Retrieves a list of buckets for a given project.

<details><summary>Parameters</summary>

#### project (required)

A valid API project identifier.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prefix

Filter results to buckets whose names begin with this prefix.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to noAcl.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request.

**Type:** string

</details>

## list_default_object_acls

Retrieves default object ACL entries on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### ifMetagenerationMatch

If present, only return default ACL listing if the bucket's current metageneration matches this value.

**Type:** string

#### ifMetagenerationNotMatch

If present, only return default ACL listing if the bucket's current metageneration does not match the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## list_notification_subscriptions

Retrieves a list of notification subscriptions for a given bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a Google Cloud Storage bucket.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## list_object_access_controls

Retrieves ACL entries on the specified object.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## list_objects

Retrieves a list of objects matching the criteria.

<details><summary>Parameters</summary>

#### bucket (required)

Name of the bucket in which to look for objects.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### delimiter

Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### includeTrailingDelimiter

If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes.

**Type:** boolean

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prefix

Filter results to objects whose names begin with this prefix.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to noAcl.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

#### versions

If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning.

**Type:** boolean

</details>

## lock_bucket_retention_policy

Locks retention policy on a bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### ifMetagenerationMatch (required)

Makes the operation conditional on whether bucket's current metageneration matches the given value.

**Type:** string

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## patch_bucket

Patches a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### $body

A bucket.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### ifMetagenerationMatch

Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.

**Type:** string

#### ifMetagenerationNotMatch

Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### predefinedAcl

Apply a predefined set of access controls to this bucket.

**Type:** string

**Potential values:** authenticatedRead, private, projectPrivate, publicRead, publicReadWrite

#### predefinedDefaultObjectAcl

Apply a predefined set of default object access controls to this bucket.

**Type:** string

**Potential values:** authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to full.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## patch_bucket_access_control

Patches an ACL entry on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### $body

An access-control entry.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## patch_default_object_acl

Patches a default object ACL entry on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### $body

An access-control entry.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## patch_object_access_control

Patches an ACL entry on the specified object.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### $body

An access-control entry.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## patch_object_metadata

Patches an object's metadata.

<details><summary>Parameters</summary>

#### bucket (required)

Name of the bucket in which the object resides.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### $body

An object.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### ifGenerationMatch

Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.

**Type:** string

#### ifGenerationNotMatch

Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.

**Type:** string

#### ifMetagenerationMatch

Makes the operation conditional on whether the object's current metageneration matches the given value.

**Type:** string

#### ifMetagenerationNotMatch

Makes the operation conditional on whether the object's current metageneration does not match the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### predefinedAcl

Apply a predefined set of access controls to this object.

**Type:** string

**Potential values:** authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to full.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request, for Requester Pays buckets.

**Type:** string

</details>

## rewrite_object

Rewrites a source object to a destination object. Optionally overrides metadata.

<details><summary>Parameters</summary>

#### destinationBucket (required)

Name of the bucket in which to store the new object. Overrides the provided object metadata's bucket value, if any.

**Type:** string

#### destinationObject (required)

Name of the new object. Required when the object metadata is not otherwise provided. Overrides the object metadata's name value, if any. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### sourceBucket (required)

Name of the bucket in which to find the source object.

**Type:** string

#### sourceObject (required)

Name of the source object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### $body

An object.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### destinationKmsKeyName

Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata's kms_key_name value, if any.

**Type:** string

#### destinationPredefinedAcl

Apply a predefined set of access controls to the destination object.

**Type:** string

**Potential values:** authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### ifGenerationMatch

Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.

**Type:** string

#### ifGenerationNotMatch

Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.

**Type:** string

#### ifMetagenerationMatch

Makes the operation conditional on whether the destination object's current metageneration matches the given value.

**Type:** string

#### ifMetagenerationNotMatch

Makes the operation conditional on whether the destination object's current metageneration does not match the given value.

**Type:** string

#### ifSourceGenerationMatch

Makes the operation conditional on whether the source object's current generation matches the given value.

**Type:** string

#### ifSourceGenerationNotMatch

Makes the operation conditional on whether the source object's current generation does not match the given value.

**Type:** string

#### ifSourceMetagenerationMatch

Makes the operation conditional on whether the source object's current metageneration matches the given value.

**Type:** string

#### ifSourceMetagenerationNotMatch

Makes the operation conditional on whether the source object's current metageneration does not match the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### maxBytesRewrittenPerCall

The maximum number of bytes that will be rewritten per rewrite request. Most callers shouldn't need to specify this parameter - it is primarily in place to support testing. If specified the value must be an integral multiple of 1 MiB (1048576). Also, this only applies to requests where the source and destination span locations and/or storage classes. Finally, this value must not change across rewrite calls else you'll get an error that the rewriteToken is invalid.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to noAcl, unless the object resource specifies the acl property, when it defaults to full.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### rewriteToken

Include this field (from the previous rewrite response) on each rewrite request after the first one, until the rewrite response 'done' flag is true. Calls that provide a rewriteToken can omit all other request fields, but if included those fields must match the values provided in the first rewrite request.

**Type:** string

#### sourceGeneration

If present, selects a specific revision of the source object (as opposed to the latest version, the default).

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## stop_watching_channel

Stop watching resources through this channel

<details><summary>Parameters</summary>

#### $body

An notification channel used to watch for resource changes.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

</details>

## store_list_as_object

Concatenates a list of existing objects into a new object in the same bucket.

<details><summary>Parameters</summary>

#### destinationBucket (required)

Name of the bucket containing the source objects. The destination object is stored in this bucket.

**Type:** string

#### destinationObject (required)

Name of the new object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### $body

A Compose request.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### destinationPredefinedAcl

Apply a predefined set of access controls to the destination object.

**Type:** string

**Potential values:** authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### ifGenerationMatch

Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.

**Type:** string

#### ifMetagenerationMatch

Makes the operation conditional on whether the object's current metageneration matches the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### kmsKeyName

Resource name of the Cloud KMS key, of the form projects/my-project/locations/global/keyRings/my-kr/cryptoKeys/my-key, that will be used to encrypt the object. Overrides the object metadata's kms_key_name value, if any.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## test_bucket_iam_permissions

Tests a set of permissions on the given bucket to see which, if any, are held by the caller.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### permissions (required)

Permissions to test.

**Type:** array

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## test_object_iam_permissions

Tests a set of permissions on the given object to see which, if any, are held by the caller.

<details><summary>Parameters</summary>

#### bucket (required)

Name of the bucket in which the object resides.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### permissions (required)

Permissions to test.

**Type:** array

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## update_bucket

Updates a bucket. Changes to the bucket will be readable immediately after writing, but configuration changes may take time to propagate.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### $body

A bucket.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### ifMetagenerationMatch

Makes the return of the bucket metadata conditional on whether the bucket's current metageneration matches the given value.

**Type:** string

#### ifMetagenerationNotMatch

Makes the return of the bucket metadata conditional on whether the bucket's current metageneration does not match the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### predefinedAcl

Apply a predefined set of access controls to this bucket.

**Type:** string

**Potential values:** authenticatedRead, private, projectPrivate, publicRead, publicReadWrite

#### predefinedDefaultObjectAcl

Apply a predefined set of default object access controls to this bucket.

**Type:** string

**Potential values:** authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to full.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## update_bucket_access_control

Updates an ACL entry on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### $body

An access-control entry.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## update_bucket_iam_policy

Updates an IAM policy for the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### $body

A bucket/object IAM policy.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## update_default_object_acl

Updates a default object ACL entry on the specified bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### $body

An access-control entry.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## update_object_access_control

Updates an ACL entry on the specified object.

<details><summary>Parameters</summary>

#### bucket (required)

Name of a bucket.

**Type:** string

#### entity (required)

The entity holding the permission. Can be user-userId, user-emailAddress, group-groupId, group-emailAddress, allUsers, or allAuthenticatedUsers.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### $body

An access-control entry.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## update_object_iam_policy

Updates an IAM policy for the specified object.

<details><summary>Parameters</summary>

#### bucket (required)

Name of the bucket in which the object resides.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### $body

A bucket/object IAM policy.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## update_object_metadata

Updates an object's metadata.

<details><summary>Parameters</summary>

#### bucket (required)

Name of the bucket in which the object resides.

**Type:** string

#### object (required)

Name of the object. For information about how to URL encode object names to be path safe, see Encoding URI Path Parts.

**Type:** string

#### $body

An object.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### generation

If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Type:** string

#### ifGenerationMatch

Makes the operation conditional on whether the object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object.

**Type:** string

#### ifGenerationNotMatch

Makes the operation conditional on whether the object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object.

**Type:** string

#### ifMetagenerationMatch

Makes the operation conditional on whether the object's current metageneration matches the given value.

**Type:** string

#### ifMetagenerationNotMatch

Makes the operation conditional on whether the object's current metageneration does not match the given value.

**Type:** string

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### predefinedAcl

Apply a predefined set of access controls to this object.

**Type:** string

**Potential values:** authenticatedRead, bucketOwnerFullControl, bucketOwnerRead, private, projectPrivate, publicRead

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to full.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

</details>

## watch_all_objects

Watch for changes on all objects in a bucket.

<details><summary>Parameters</summary>

#### bucket (required)

Name of the bucket in which to look for objects.

**Type:** string

#### $body

An notification channel used to watch for resource changes.

**Type:** object

#### alt

Data format for the response.

**Type:** string

**Potential values:** json

#### delimiter

Returns results in a directory-like mode. items will contain only objects whose names, aside from the prefix, do not contain delimiter. Objects whose names, aside from the prefix, contain delimiter will have their name, truncated after the delimiter, returned in prefixes. Duplicate prefixes are omitted.

**Type:** string

#### fields

Selector specifying which fields to include in a partial response.

**Type:** string

#### includeTrailingDelimiter

If true, objects that end in exactly one instance of delimiter will have their metadata included in items in addition to prefixes.

**Type:** boolean

#### key

API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.

**Type:** string

#### maxResults

Maximum number of items plus prefixes to return in a single page of responses. As duplicate prefixes are omitted, fewer total results may be returned than requested. The service will use this parameter or 1,000 items, whichever is smaller.

**Type:** integer

#### pageToken

A previously-returned page token representing part of the larger set of results to view.

**Type:** string

#### prefix

Filter results to objects whose names begin with this prefix.

**Type:** string

#### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

#### projection

Set of properties to return. Defaults to noAcl.

**Type:** string

**Potential values:** full, noAcl

#### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

#### userIp

Deprecated. Please use quotaUser instead.

**Type:** string

#### userProject

The project to be billed for this request. Required for Requester Pays buckets.

**Type:** string

#### versions

If true, lists all versions of an object as distinct results. The default is false. For more information, see Object Versioning.

**Type:** boolean

</details>

