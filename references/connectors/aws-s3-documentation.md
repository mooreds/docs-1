---
id: aws-s3-documentation
title: AWS S3 (version v3.*.*)
sidebar_label: AWS S3
layout: docs.mustache
---

## abort_multipart_upload

Aborts a multipart upload. 
To verify that all parts have been removed, so you don't get charged for the part storage, you should call the List Parts operation and ensure the parts list is empty.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### uploadId (required)

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

</details>

## complete_multipart_upload

Completes a multipart upload by assembling previously uploaded parts.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### uploadId (required)

**Type:** string

### $body

**Type:** object

```json
{
  "CompleteMultipartUpload" : {
    "Part" : [ {
      "PartNumber" : "Part number that identifies the part. This is a positive integer between 1 and 10,000.",
      "ETag" : "Entity tag returned when the part was uploaded."
    } ]
  }
}
```

### x-amz-request-payer

**Type:** string

**Potential values:** requester

</details>

## copy_object

Creates a copy of an object that is already stored in Amazon S3.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### x-amz-copy-source (required)

The name of the source bucket and key name of the source object, separated by a slash (/). Must be URL-encoded.

**Type:** string

### Cache-Control

Specifies caching behavior along the request/reply chain.

**Type:** string

### Content-Disposition

Specifies presentational information for the object.

**Type:** string

### Content-Encoding

Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

**Type:** string

### Content-Language

The language the content is in.

**Type:** string

### Content-Type

A standard MIME type describing the format of the object data.

**Type:** string

### Expires

The date and time at which the object is no longer cacheable.

**Type:** timestamp

### x-amz-acl

The canned ACL to apply to the object.

**Type:** string

**Potential values:** private, public-read, public-read-write, authenticated-read, aws-exec-read, bucket-owner-read, bucket-owner-full-control

### x-amz-copy-source-if-match

Copies the object if its entity tag (ETag) matches the specified tag.

**Type:** string

### x-amz-copy-source-if-modified-since

Copies the object if it has been modified since the specified time.

**Type:** timestamp

### x-amz-copy-source-if-none-match

Copies the object if its entity tag (ETag) is different than the specified ETag.

**Type:** string

### x-amz-copy-source-if-unmodified-since

Copies the object if it hasn't been modified since the specified time.

**Type:** timestamp

### x-amz-copy-source-server-side-encryption-customer-algorithm

Specifies the algorithm to use when decrypting the source object (e.g., AES256).

**Type:** string

### x-amz-copy-source-server-side-encryption-customer-key

Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.

**Type:** string

### x-amz-copy-source-server-side-encryption-customer-key-MD5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.

**Type:** string

### x-amz-grant-full-control

Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

**Type:** string

### x-amz-grant-read

Allows grantee to read the object data and its metadata.

**Type:** string

### x-amz-grant-read-acp

Allows grantee to read the object ACL.

**Type:** string

### x-amz-grant-write-acp

Allows grantee to write the ACL for the applicable object.

**Type:** string

### x-amz-meta-

A map of metadata to store with the object in S3.

**Type:** object

```json
{
  "<string>" : "string"
}
```

### x-amz-metadata-directive

Specifies whether the metadata is copied from the source object or replaced with metadata provided in the request.

**Type:** string

**Potential values:** COPY, REPLACE

### x-amz-request-payer

**Type:** string

**Potential values:** requester

### x-amz-server-side-encryption

The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).

**Type:** string

**Potential values:** AES256, aws:kms

### x-amz-server-side-encryption-aws-kms-key-id

Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version

**Type:** string

### x-amz-server-side-encryption-customer-algorithm

Specifies the algorithm to use to when encrypting the object (e.g., AES256).

**Type:** string

### x-amz-server-side-encryption-customer-key

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.

**Type:** string

### x-amz-server-side-encryption-customer-key-MD5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.

**Type:** string

### x-amz-storage-class

The type of storage to use for the object. Defaults to 'STANDARD'.

**Type:** string

**Potential values:** STANDARD, REDUCED_REDUNDANCY, STANDARD_IA, ONEZONE_IA

### x-amz-tagging

The tag-set for the object destination object this value must be used in conjunction with the TaggingDirective. The tag-set must be encoded as URL Query parameters

**Type:** string

### x-amz-tagging-directive

Specifies whether the object tag-set are copied from the source object or replaced with tag-set provided in the request.

**Type:** string

**Potential values:** COPY, REPLACE

### x-amz-website-redirect-location

If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

**Type:** string

</details>

## create_bucket

Creates a new bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "CreateBucketConfiguration" : {
    "LocationConstraint" : "Specifies the region where the bucket will be created. If you don't specify a region, the bucket will be created in US Standard."
  }
}
```

### x-amz-acl

The canned ACL to apply to the bucket.

**Type:** string

**Potential values:** private, public-read, public-read-write, authenticated-read

### x-amz-grant-full-control

Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

**Type:** string

### x-amz-grant-read

Allows grantee to list the objects in the bucket.

**Type:** string

### x-amz-grant-read-acp

Allows grantee to read the bucket ACL.

**Type:** string

### x-amz-grant-write

Allows grantee to create, overwrite, and delete any object in the bucket.

**Type:** string

### x-amz-grant-write-acp

Allows grantee to write the ACL for the applicable bucket.

**Type:** string

</details>

## create_multipart_upload

Initiates a multipart upload and returns an upload ID. 
 Note: After you initiate multipart upload and upload one or more parts, you must either complete or abort multipart upload in order to stop getting charged for storage of the uploaded parts. Only after you either complete or abort multipart upload, Amazon S3 frees up the parts storage and stops charging you for the parts storage.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### Cache-Control

Specifies caching behavior along the request/reply chain.

**Type:** string

### Content-Disposition

Specifies presentational information for the object.

**Type:** string

### Content-Encoding

Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

**Type:** string

### Content-Language

The language the content is in.

**Type:** string

### Content-Type

A standard MIME type describing the format of the object data.

**Type:** string

### Expires

The date and time at which the object is no longer cacheable.

**Type:** timestamp

### x-amz-acl

The canned ACL to apply to the object.

**Type:** string

**Potential values:** private, public-read, public-read-write, authenticated-read, aws-exec-read, bucket-owner-read, bucket-owner-full-control

### x-amz-grant-full-control

Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

**Type:** string

### x-amz-grant-read

Allows grantee to read the object data and its metadata.

**Type:** string

### x-amz-grant-read-acp

Allows grantee to read the object ACL.

**Type:** string

### x-amz-grant-write-acp

Allows grantee to write the ACL for the applicable object.

**Type:** string

### x-amz-meta-

A map of metadata to store with the object in S3.

**Type:** object

```json
{
  "<string>" : "string"
}
```

### x-amz-request-payer

**Type:** string

**Potential values:** requester

### x-amz-server-side-encryption

The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).

**Type:** string

**Potential values:** AES256, aws:kms

### x-amz-server-side-encryption-aws-kms-key-id

Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version

**Type:** string

### x-amz-server-side-encryption-customer-algorithm

Specifies the algorithm to use to when encrypting the object (e.g., AES256).

**Type:** string

### x-amz-server-side-encryption-customer-key

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.

**Type:** string

### x-amz-server-side-encryption-customer-key-MD5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.

**Type:** string

### x-amz-storage-class

The type of storage to use for the object. Defaults to 'STANDARD'.

**Type:** string

**Potential values:** STANDARD, REDUCED_REDUNDANCY, STANDARD_IA, ONEZONE_IA

### x-amz-tagging

The tag-set for the object. The tag-set must be encoded as URL Query parameters

**Type:** string

### x-amz-website-redirect-location

If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

**Type:** string

</details>

## delete_bucket

Deletes the bucket. All objects (including all object versions and Delete Markers) in the bucket must be deleted before the bucket itself can be deleted.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## delete_bucket_analytics_configuration

Deletes an analytics configuration for the bucket (specified by the analytics configuration ID).

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket from which an analytics configuration is deleted.

**Type:** string

### id (required)

The identifier used to represent an analytics configuration.

**Type:** string

</details>

## delete_bucket_cors

Deletes the cors configuration information set for the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## delete_bucket_encryption

Deletes the server-side encryption configuration from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket containing the server-side encryption configuration to delete.

**Type:** string

</details>

## delete_bucket_inventory_configuration

Deletes an inventory configuration (identified by the inventory ID) from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket containing the inventory configuration to delete.

**Type:** string

### id (required)

The ID used to identify the inventory configuration.

**Type:** string

</details>

## delete_bucket_lifecycle

Deletes the lifecycle configuration from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## delete_bucket_metrics_configuration

Deletes a metrics configuration (specified by the metrics configuration ID) from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket containing the metrics configuration to delete.

**Type:** string

### id (required)

The ID used to identify the metrics configuration.

**Type:** string

</details>

## delete_bucket_policy

Deletes the policy from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## delete_bucket_replication

Deletes the replication configuration from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

Deletes the replication subresource associated with the specified bucket.  
There is usually some time lag before replication configuration deletion is fully propagated to all the Amazon S3 systems.  
 For more information, see Cross-Region Replication (CRR) in the Amazon S3 Developer Guide. 

**Type:** string

</details>

## delete_bucket_tagging

Deletes the tags from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## delete_bucket_website

This operation removes the website configuration from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## delete_object

Removes the null version (if there is one) of an object and inserts a delete marker, which becomes the latest version of the object. If there isn't a null version, Amazon S3 does not remove any objects.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### versionId

VersionId used to reference a specific version of the object.

**Type:** string

### x-amz-mfa

The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

</details>

## delete_object_tagging

Removes the tag-set from an existing object.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### versionId

The versionId of the object that the tag-set will be removed from.

**Type:** string

</details>

## delete_objects

This operation enables you to delete multiple objects from a bucket using a single HTTP request. You may specify up to 1000 keys.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "Delete" : {
    "Quiet" : "Element to enable quiet mode for the request. When you add this element, you must set its value to true.",
    "Object" : [ {
      "VersionId" : "VersionId for the specific version of the object to delete.",
      "Key" : "Key name of the object to delete."
    } ]
  }
}
```

### x-amz-mfa

The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

</details>

## get_bucket_accelerate_configuration

Returns the accelerate configuration of a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

Name of the bucket for which the accelerate configuration is retrieved.

**Type:** string

</details>

## get_bucket_acl

Gets the access control policy for the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_analytics_configuration

Gets an analytics configuration for the bucket (specified by the analytics configuration ID).

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket from which an analytics configuration is retrieved.

**Type:** string

### id (required)

The identifier used to represent an analytics configuration.

**Type:** string

</details>

## get_bucket_cors

Returns the cors configuration for the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_encryption

Returns the server-side encryption configuration of a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket from which the server-side encryption configuration is retrieved.

**Type:** string

</details>

## get_bucket_inventory_configuration

Returns an inventory configuration (identified by the inventory ID) from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket containing the inventory configuration to retrieve.

**Type:** string

### id (required)

The ID used to identify the inventory configuration.

**Type:** string

</details>

## get_bucket_lifecycle

Deprecated, see the GetBucketLifecycleConfiguration operation.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_lifecycle_configuration

Returns the lifecycle configuration information set on the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_location

Returns the region the bucket resides in.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_logging

Returns the logging status of a bucket and the permissions users have to view and modify that status. To use GET, you must be the bucket owner.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_metrics_configuration

Gets a metrics configuration (specified by the metrics configuration ID) from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket containing the metrics configuration to retrieve.

**Type:** string

### id (required)

The ID used to identify the metrics configuration.

**Type:** string

</details>

## get_bucket_notification

Deprecated, see the GetBucketNotificationConfiguration operation.

<details><summary>Parameters</summary>

### Bucket (required)

Name of the bucket to get the notification configuration for.

**Type:** string

</details>

## get_bucket_notification_configuration

Returns the notification configuration of a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

Name of the bucket to get the notification configuration for.

**Type:** string

</details>

## get_bucket_policy

Returns the policy of a specified bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_replication

Returns the replication configuration of a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_request_payment

Returns the request payment configuration of a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_tagging

Returns the tag set associated with the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_versioning

Returns the versioning state of a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_bucket_website

Returns the website configuration for a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## get_object

Retrieves objects from Amazon S3.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### If-Match

Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).

**Type:** string

### If-Modified-Since

Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).

**Type:** timestamp

### If-None-Match

Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).

**Type:** string

### If-Unmodified-Since

Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).

**Type:** timestamp

### Range

Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.

**Type:** string

### partNumber

Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a 'ranged' GET request for the part specified. Useful for downloading just a part of an object.

**Type:** integer

### response-cache-control

Sets the Cache-Control header of the response.

**Type:** string

### response-content-disposition

Sets the Content-Disposition header of the response

**Type:** string

### response-content-encoding

Sets the Content-Encoding header of the response.

**Type:** string

### response-content-language

Sets the Content-Language header of the response.

**Type:** string

### response-content-type

Sets the Content-Type header of the response.

**Type:** string

### response-expires

Sets the Expires header of the response.

**Type:** timestamp

### versionId

VersionId used to reference a specific version of the object.

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

### x-amz-server-side-encryption-customer-algorithm

Specifies the algorithm to use to when encrypting the object (e.g., AES256).

**Type:** string

### x-amz-server-side-encryption-customer-key

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.

**Type:** string

### x-amz-server-side-encryption-customer-key-MD5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.

**Type:** string

</details>

## get_object_acl

Returns the access control list (ACL) of an object.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### versionId

VersionId used to reference a specific version of the object.

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

</details>

## get_object_tagging

Returns the tag-set of an object.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### versionId

**Type:** string

</details>

## get_object_torrent

Return torrent files from a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

</details>

## head_bucket

This operation is useful to determine if a bucket exists and you have permission to access it.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

</details>

## head_object

The HEAD operation retrieves metadata from an object without returning the object itself. This operation is useful if you're only interested in an object's metadata. To use HEAD, you must have READ access to the object.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### If-Match

Return the object only if its entity tag (ETag) is the same as the one specified, otherwise return a 412 (precondition failed).

**Type:** string

### If-Modified-Since

Return the object only if it has been modified since the specified time, otherwise return a 304 (not modified).

**Type:** timestamp

### If-None-Match

Return the object only if its entity tag (ETag) is different from the one specified, otherwise return a 304 (not modified).

**Type:** string

### If-Unmodified-Since

Return the object only if it has not been modified since the specified time, otherwise return a 412 (precondition failed).

**Type:** timestamp

### Range

Downloads the specified range bytes of an object. For more information about the HTTP Range header, go to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.

**Type:** string

### partNumber

Part number of the object being read. This is a positive integer between 1 and 10,000. Effectively performs a 'ranged' HEAD request for the part specified. Useful querying about the size of the part and the number of parts in this object.

**Type:** integer

### versionId

VersionId used to reference a specific version of the object.

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

### x-amz-server-side-encryption-customer-algorithm

Specifies the algorithm to use to when encrypting the object (e.g., AES256).

**Type:** string

### x-amz-server-side-encryption-customer-key

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.

**Type:** string

### x-amz-server-side-encryption-customer-key-MD5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.

**Type:** string

</details>

## list_bucket_analytics_configurations

Lists the analytics configurations for the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket from which analytics configurations are retrieved.

**Type:** string

### continuation-token

The ContinuationToken that represents a placeholder from where this request should begin.

**Type:** string

</details>

## list_bucket_inventory_configurations

Returns a list of inventory configurations for the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket containing the inventory configurations to retrieve.

**Type:** string

### continuation-token

The marker used to continue an inventory configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.

**Type:** string

</details>

## list_bucket_metrics_configurations

Lists the metrics configurations for the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket containing the metrics configurations to retrieve.

**Type:** string

### continuation-token

The marker that is used to continue a metrics configuration listing that has been truncated. Use the NextContinuationToken from a previously truncated list response to continue the listing. The continuation token is an opaque value that Amazon S3 understands.

**Type:** string

</details>

## list_buckets

Returns a list of all buckets owned by the authenticated sender of the request.

*This operation has no parameters*

## list_multipart_uploads

This operation lists in-progress multipart uploads.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### delimiter

Character you use to group keys.

**Type:** string

### encoding-type

**Type:** string

**Potential values:** url

### prefix

Lists in-progress uploads only for those keys that begin with the specified prefix.

**Type:** string

</details>

## list_object_versions

Returns metadata about all of the versions of objects in a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### delimiter

A delimiter is a character you use to group keys.

**Type:** string

### encoding-type

**Type:** string

**Potential values:** url

### prefix

Limits the response to keys that begin with the specified prefix.

**Type:** string

</details>

## list_objects

Returns some or all (up to 1000) of the objects in a bucket. You can use the request parameters as selection criteria to return a subset of the objects in a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### delimiter

A delimiter is a character you use to group keys.

**Type:** string

### encoding-type

**Type:** string

**Potential values:** url

### prefix

Limits the response to keys that begin with the specified prefix.

**Type:** string

### x-amz-request-payer

Confirms that the requester knows that she or he will be charged for the list objects request. Bucket owners need not specify this parameter in their requests.

**Type:** string

**Potential values:** requester

</details>

## list_objects_v2

Returns some or all (up to 1000) of the objects in a bucket. You can use the request parameters as selection criteria to return a subset of the objects in a bucket. Note: ListObjectsV2 is the revised List Objects API and we recommend you use this revised API for new application development.

<details><summary>Parameters</summary>

### Bucket (required)

Name of the bucket to list.

**Type:** string

### delimiter

A delimiter is a character you use to group keys.

**Type:** string

### encoding-type

Encoding type used by Amazon S3 to encode object keys in the response.

**Type:** string

**Potential values:** url

### fetch-owner

The owner field is not present in listV2 by default, if you want to return owner field with each key in the result then set the fetch owner field to true

**Type:** boolean

### prefix

Limits the response to keys that begin with the specified prefix.

**Type:** string

### start-after

StartAfter is where you want Amazon S3 to start listing from. Amazon S3 starts listing after this specified key. StartAfter can be any key in the bucket

**Type:** string

### x-amz-request-payer

Confirms that the requester knows that she or he will be charged for the list objects request in V2 style. Bucket owners need not specify this parameter in their requests.

**Type:** string

**Potential values:** requester

</details>

## list_parts

Lists the parts that have been uploaded for a specific multipart upload.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### uploadId (required)

Upload ID identifying the multipart upload whose parts are being listed.

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

</details>

## put_bucket_accelerate_configuration

Sets the accelerate configuration of an existing bucket.

<details><summary>Parameters</summary>

### Bucket (required)

Name of the bucket for which the accelerate configuration is set.

**Type:** string

### $body

Specifies the Accelerate Configuration you want to set for the bucket.

**Type:** object

```json
{
  "AccelerateConfiguration" : {
    "Status" : "The accelerate configuration of the bucket."
  }
}
```

</details>

## put_bucket_acl

Sets the permissions on a bucket using access control lists (ACL).

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "AccessControlPolicy" : {
    "AccessControlList" : [ {
      "Grant" : {
        "Grantee" : {
          "DisplayName" : "Screen name of the grantee.",
          "xsi:type" : "Type of grantee",
          "ID" : "The canonical user ID of the grantee.",
          "URI" : "URI of the grantee group.",
          "EmailAddress" : "Email address of the grantee."
        },
        "Permission" : "Specifies the permission given to the grantee."
      }
    } ],
    "Owner" : {
      "DisplayName" : "string",
      "ID" : "string"
    }
  }
}
```

### Content-MD5

**Type:** string

### x-amz-acl

The canned ACL to apply to the bucket.

**Type:** string

**Potential values:** private, public-read, public-read-write, authenticated-read

### x-amz-grant-full-control

Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

**Type:** string

### x-amz-grant-read

Allows grantee to list the objects in the bucket.

**Type:** string

### x-amz-grant-read-acp

Allows grantee to read the bucket ACL.

**Type:** string

### x-amz-grant-write

Allows grantee to create, overwrite, and delete any object in the bucket.

**Type:** string

### x-amz-grant-write-acp

Allows grantee to write the ACL for the applicable bucket.

**Type:** string

</details>

## put_bucket_analytics_configuration

Sets an analytics configuration for the bucket (specified by the analytics configuration ID).

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket to which an analytics configuration is stored.

**Type:** string

### id (required)

The identifier used to represent an analytics configuration.

**Type:** string

### $body

The configuration and any analyses for the analytics filter.

**Type:** object

```json
{
  "AnalyticsConfiguration" : {
    "StorageClassAnalysis" : {
      "DataExport" : {
        "Destination" : {
          "S3BucketDestination" : {
            "Format" : "The file format used when exporting data to Amazon S3.",
            "Bucket" : "The Amazon resource name (ARN) of the bucket to which data is exported.",
            "BucketAccountId" : "The account ID that owns the destination bucket. If no account ID is provided, the owner will not be validated prior to exporting data.",
            "Prefix" : "The prefix to use when exporting data. The exported data begins with this prefix."
          }
        },
        "OutputSchemaVersion" : "The version of the output schema to use when exporting data. Must be V_1."
      }
    },
    "Filter" : {
      "And" : {
        "Prefix" : "The prefix to use when evaluating an AND predicate.",
        "Tag" : [ {
          "Tag" : {
            "Value" : "Value of the tag.",
            "Key" : "Name of the tag."
          }
        } ]
      },
      "Prefix" : "The prefix to use when evaluating an analytics filter.",
      "Tag" : {
        "Value" : "Value of the tag.",
        "Key" : "Name of the tag."
      }
    },
    "Id" : "The identifier used to represent an analytics configuration."
  }
}
```

</details>

## put_bucket_cors

Sets the cors configuration for a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "CORSConfiguration" : {
    "CORSRule" : [ {
      "AllowedMethod" : [ "string" ],
      "MaxAgeSeconds" : "The time in seconds that your browser is to cache the preflight response for the specified resource.",
      "ExposeHeader" : [ "string" ],
      "AllowedOrigin" : [ "string" ],
      "AllowedHeader" : [ "string" ]
    } ]
  }
}
```

### Content-MD5

**Type:** string

</details>

## put_bucket_encryption

Creates a new server-side encryption configuration (or replaces an existing one, if present).

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket for which the server-side encryption configuration is set.

**Type:** string

### $body

**Type:** object

```json
{
  "ServerSideEncryptionConfiguration" : {
    "Rule" : [ {
      "ApplyServerSideEncryptionByDefault" : {
        "SSEAlgorithm" : "Server-side encryption algorithm to use for the default encryption.",
        "KMSMasterKeyID" : "KMS master key ID to use for the default encryption. This parameter is allowed if SSEAlgorithm is aws:kms."
      }
    } ]
  }
}
```

### Content-MD5

The base64-encoded 128-bit MD5 digest of the server-side encryption configuration.

**Type:** string

</details>

## put_bucket_inventory_configuration

Adds an inventory configuration (identified by the inventory ID) from the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket where the inventory configuration will be stored.

**Type:** string

### id (required)

The ID used to identify the inventory configuration.

**Type:** string

### $body

Specifies the inventory configuration.

**Type:** object

```json
{
  "InventoryConfiguration" : {
    "Destination" : {
      "S3BucketDestination" : {
        "AccountId" : "The ID of the account that owns the destination bucket.",
        "Format" : "Specifies the output format of the inventory results.",
        "Bucket" : "The Amazon resource name (ARN) of the bucket where inventory results will be published.",
        "Prefix" : "The prefix that is prepended to all inventory results.",
        "Encryption" : {
          "SSE-KMS" : {
            "KeyId" : "Specifies the ID of the AWS Key Management Service (KMS) master encryption key to use for encrypting Inventory reports."
          },
          "SSE-S3" : { }
        }
      }
    },
    "OptionalFields" : [ {
      "Field" : "string. Possible values: Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | ReplicationStatus | EncryptionStatus"
    } ],
    "IsEnabled" : "Specifies whether the inventory is enabled or disabled.",
    "Filter" : {
      "Prefix" : "The prefix that an object must have to be included in the inventory results."
    },
    "IncludedObjectVersions" : "Specifies which object version(s) to included in the inventory results.",
    "Schedule" : {
      "Frequency" : "Specifies how frequently inventory results are produced."
    },
    "Id" : "The ID used to identify the inventory configuration."
  }
}
```

</details>

## put_bucket_lifecycle

Deprecated, see the PutBucketLifecycleConfiguration operation.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "LifecycleConfiguration" : {
    "Rule" : [ {
      "Status" : "If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being applied.",
      "NoncurrentVersionTransition" : {
        "NoncurrentDays" : "Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide.",
        "StorageClass" : "The class of storage used to store the object."
      },
      "NoncurrentVersionExpiration" : {
        "NoncurrentDays" : "Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide."
      },
      "Expiration" : {
        "ExpiredObjectDeleteMarker" : "Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.",
        "Days" : "Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.",
        "Date" : "Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format."
      },
      "Transition" : {
        "StorageClass" : "The class of storage used to store the object.",
        "Days" : "Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.",
        "Date" : "Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format."
      },
      "ID" : "Unique identifier for the rule. The value cannot be longer than 255 characters.",
      "Prefix" : "Prefix identifying one or more objects to which the rule applies.",
      "AbortIncompleteMultipartUpload" : {
        "DaysAfterInitiation" : "Indicates the number of days that must pass since initiation for Lifecycle to abort an Incomplete Multipart Upload."
      }
    } ]
  }
}
```

### Content-MD5

**Type:** string

</details>

## put_bucket_lifecycle_configuration

Sets lifecycle configuration for your bucket. If a lifecycle configuration exists, it replaces it.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "LifecycleConfiguration" : {
    "Rule" : [ {
      "Status" : "If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being applied.",
      "NoncurrentVersionTransition" : [ {
        "NoncurrentDays" : "Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide.",
        "StorageClass" : "The class of storage used to store the object."
      } ],
      "Filter" : {
        "And" : {
          "Prefix" : "string",
          "Tag" : [ {
            "Tag" : {
              "Value" : "Value of the tag.",
              "Key" : "Name of the tag."
            }
          } ]
        },
        "Prefix" : "Prefix identifying one or more objects to which the rule applies.",
        "Tag" : {
          "Value" : "Value of the tag.",
          "Key" : "Name of the tag."
        }
      },
      "NoncurrentVersionExpiration" : {
        "NoncurrentDays" : "Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see How Amazon S3 Calculates When an Object Became Noncurrent in the Amazon Simple Storage Service Developer Guide."
      },
      "Expiration" : {
        "ExpiredObjectDeleteMarker" : "Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired; if set to false the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy.",
        "Days" : "Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.",
        "Date" : "Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format."
      },
      "Transition" : [ {
        "StorageClass" : "The class of storage used to store the object.",
        "Days" : "Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.",
        "Date" : "Indicates at what date the object is to be moved or deleted. Should be in GMT ISO 8601 Format."
      } ],
      "ID" : "Unique identifier for the rule. The value cannot be longer than 255 characters.",
      "Prefix" : "Prefix identifying one or more objects to which the rule applies. This is deprecated; use Filter instead.",
      "AbortIncompleteMultipartUpload" : {
        "DaysAfterInitiation" : "Indicates the number of days that must pass since initiation for Lifecycle to abort an Incomplete Multipart Upload."
      }
    } ]
  }
}
```

</details>

## put_bucket_logging

Set the logging parameters for a bucket and to specify permissions for who can view and modify the logging parameters. To set the logging status of a bucket, you must be the bucket owner.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "BucketLoggingStatus" : {
    "LoggingEnabled" : {
      "TargetPrefix" : "This element lets you specify a prefix for the keys that the log files will be stored under.",
      "TargetBucket" : "Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also configure multiple buckets to deliver their logs to the same target bucket. In this case you should choose a different TargetPrefix for each source bucket so that the delivered log files can be distinguished by key.",
      "TargetGrants" : [ {
        "Grant" : {
          "Grantee" : {
            "DisplayName" : "Screen name of the grantee.",
            "xsi:type" : "Type of grantee",
            "ID" : "The canonical user ID of the grantee.",
            "URI" : "URI of the grantee group.",
            "EmailAddress" : "Email address of the grantee."
          },
          "Permission" : "Logging permissions assigned to the Grantee for the bucket."
        }
      } ]
    }
  }
}
```

### Content-MD5

**Type:** string

</details>

## put_bucket_metrics_configuration

Sets a metrics configuration (specified by the metrics configuration ID) for the bucket.

<details><summary>Parameters</summary>

### Bucket (required)

The name of the bucket for which the metrics configuration is set.

**Type:** string

### id (required)

The ID used to identify the metrics configuration.

**Type:** string

### $body

Specifies the metrics configuration.

**Type:** object

```json
{
  "MetricsConfiguration" : {
    "Filter" : {
      "And" : {
        "Prefix" : "The prefix used when evaluating an AND predicate.",
        "Tag" : [ {
          "Tag" : {
            "Value" : "Value of the tag.",
            "Key" : "Name of the tag."
          }
        } ]
      },
      "Prefix" : "The prefix used when evaluating a metrics filter.",
      "Tag" : {
        "Value" : "Value of the tag.",
        "Key" : "Name of the tag."
      }
    },
    "Id" : "The ID used to identify the metrics configuration."
  }
}
```

</details>

## put_bucket_notification

Deprecated, see the PutBucketNotificationConfiguraiton operation.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "NotificationConfiguration" : {
    "CloudFunctionConfiguration" : {
      "CloudFunction" : "string",
      "InvocationRole" : "string",
      "Event" : [ "string. Possible values: s3:ReducedRedundancyLostObject | s3:ObjectCreated:* | s3:ObjectCreated:Put | s3:ObjectCreated:Post | s3:ObjectCreated:Copy | s3:ObjectCreated:CompleteMultipartUpload | s3:ObjectRemoved:* | s3:ObjectRemoved:Delete | s3:ObjectRemoved:DeleteMarkerCreated" ],
      "Id" : "string"
    },
    "QueueConfiguration" : {
      "Event" : [ "string. Possible values: s3:ReducedRedundancyLostObject | s3:ObjectCreated:* | s3:ObjectCreated:Put | s3:ObjectCreated:Post | s3:ObjectCreated:Copy | s3:ObjectCreated:CompleteMultipartUpload | s3:ObjectRemoved:* | s3:ObjectRemoved:Delete | s3:ObjectRemoved:DeleteMarkerCreated" ],
      "Id" : "string",
      "Queue" : "string"
    },
    "TopicConfiguration" : {
      "Event" : "Bucket event for which to send notifications.",
      "Id" : "string",
      "Topic" : "Amazon SNS topic to which Amazon S3 will publish a message to report the specified events for the bucket."
    }
  }
}
```

### Content-MD5

**Type:** string

</details>

## put_bucket_notification_configuration

Enables notifications of specified events for a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "NotificationConfiguration" : {
    "CloudFunctionConfiguration" : [ {
      "Filter" : {
        "S3Key" : {
          "FilterRule" : [ {
            "Value" : "string",
            "Name" : "Object key name prefix or suffix identifying one or more objects to which the filtering rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide."
          } ]
        }
      },
      "CloudFunction" : "Lambda cloud function ARN that Amazon S3 can invoke when it detects events of the specified type.",
      "Event" : [ "string. Possible values: s3:ReducedRedundancyLostObject | s3:ObjectCreated:* | s3:ObjectCreated:Put | s3:ObjectCreated:Post | s3:ObjectCreated:Copy | s3:ObjectCreated:CompleteMultipartUpload | s3:ObjectRemoved:* | s3:ObjectRemoved:Delete | s3:ObjectRemoved:DeleteMarkerCreated" ],
      "Id" : "string"
    } ],
    "QueueConfiguration" : [ {
      "Filter" : {
        "S3Key" : {
          "FilterRule" : [ {
            "Value" : "string",
            "Name" : "Object key name prefix or suffix identifying one or more objects to which the filtering rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide."
          } ]
        }
      },
      "Event" : [ "string. Possible values: s3:ReducedRedundancyLostObject | s3:ObjectCreated:* | s3:ObjectCreated:Put | s3:ObjectCreated:Post | s3:ObjectCreated:Copy | s3:ObjectCreated:CompleteMultipartUpload | s3:ObjectRemoved:* | s3:ObjectRemoved:Delete | s3:ObjectRemoved:DeleteMarkerCreated" ],
      "Id" : "string",
      "Queue" : "Amazon SQS queue ARN to which Amazon S3 will publish a message when it detects events of specified type."
    } ],
    "TopicConfiguration" : [ {
      "Filter" : {
        "S3Key" : {
          "FilterRule" : [ {
            "Value" : "string",
            "Name" : "Object key name prefix or suffix identifying one or more objects to which the filtering rule applies. Maximum prefix length can be up to 1,024 characters. Overlapping prefixes and suffixes are not supported. For more information, go to Configuring Event Notifications in the Amazon Simple Storage Service Developer Guide."
          } ]
        }
      },
      "Event" : [ "string. Possible values: s3:ReducedRedundancyLostObject | s3:ObjectCreated:* | s3:ObjectCreated:Put | s3:ObjectCreated:Post | s3:ObjectCreated:Copy | s3:ObjectCreated:CompleteMultipartUpload | s3:ObjectRemoved:* | s3:ObjectRemoved:Delete | s3:ObjectRemoved:DeleteMarkerCreated" ],
      "Id" : "string",
      "Topic" : "Amazon SNS topic ARN to which Amazon S3 will publish a message when it detects events of specified type."
    } ]
  }
}
```

</details>

## put_bucket_policy

Replaces a policy on a bucket. If the bucket already has a policy, the one in this request completely replaces it.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

The bucket policy as a JSON document.

**Type:** string

### Content-MD5

**Type:** string

### x-amz-confirm-remove-self-bucket-access

Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.

**Type:** boolean

</details>

## put_bucket_replication

 Creates a new replication configuration (or replaces an existing one, if present). For more information, see Cross-Region Replication (CRR) in the Amazon S3 Developer Guide. 

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "ReplicationConfiguration" : {
    "Role" : "Amazon Resource Name (ARN) of an IAM role for Amazon S3 to assume when replicating the objects.",
    "Rule" : [ {
      "Status" : "The rule is ignored if status is not Enabled.",
      "Destination" : {
        "AccessControlTranslation" : {
          "Owner" : "The override value for the owner of the replica object."
        },
        "Account" : " Account ID of the destination bucket. Currently Amazon S3 verifies this value only if Access Control Translation is enabled.  \n In a cross-account scenario, if you tell Amazon S3 to change replica ownership to the AWS account that owns the destination bucket by adding the AccessControlTranslation element, this is the account ID of the destination bucket owner. ",
        "Bucket" : " Amazon resource name (ARN) of the bucket where you want Amazon S3 to store replicas of the object identified by the rule.  \n If you have multiple rules in your replication configuration, all rules must specify the same bucket as the destination. A replication configuration can replicate objects only to one destination bucket. ",
        "EncryptionConfiguration" : {
          "ReplicaKmsKeyID" : " The ID of the AWS KMS key for the region where the destination bucket resides. Amazon S3 uses this key to encrypt the replica object. "
        },
        "StorageClass" : "The class of storage used to store the object."
      },
      "Filter" : {
        "And" : {
          "Prefix" : "string",
          "Tag" : [ {
            "Tag" : {
              "Value" : "Value of the tag.",
              "Key" : "Name of the tag."
            }
          } ]
        },
        "Prefix" : "Object keyname prefix that identifies subset of objects to which the rule applies.",
        "Tag" : {
          "Value" : "Value of the tag.",
          "Key" : "Name of the tag."
        }
      },
      "Priority" : "The priority associated with the rule. If you specify multiple rules in a replication configuration, then Amazon S3 applies rule priority in the event there are conflicts (two or more rules identify the same object based on filter specified). The rule with higher priority takes precedence. For example,  \n Same object quality prefix based filter criteria If prefixes you specified in multiple rules overlap.   \n Same object qualify tag based filter criteria specified in multiple rules   \nFor more information, see Cross-Region Replication (CRR) in the Amazon S3 Developer Guide.",
      "SourceSelectionCriteria" : {
        "SseKmsEncryptedObjects" : {
          "Status" : "The replication for KMS encrypted S3 objects is disabled if status is not Enabled."
        }
      },
      "ID" : "Unique identifier for the rule. The value cannot be longer than 255 characters.",
      "Prefix" : "Object keyname prefix identifying one or more objects to which the rule applies. Maximum prefix length can be up to 1,024 characters. ",
      "DeleteMarkerReplication" : {
        "Status" : "The status of the delete marker replication.  \n In the current implementation, Amazon S3 does not replicate the delete markers. Therefore, the status must be Disabled. "
      }
    } ]
  }
}
```

### Content-MD5

**Type:** string

</details>

## put_bucket_request_payment

Sets the request payment configuration for a bucket. By default, the bucket owner pays for downloads from the bucket. This configuration parameter enables the bucket owner (only) to specify that the person requesting the download will be charged for the download. Documentation on requester pays buckets can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "RequestPaymentConfiguration" : {
    "Payer" : "Specifies who pays for the download and request fees."
  }
}
```

### Content-MD5

**Type:** string

</details>

## put_bucket_tagging

Sets the tags for a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "Tagging" : {
    "TagSet" : [ {
      "Tag" : {
        "Value" : "Value of the tag.",
        "Key" : "Name of the tag."
      }
    } ]
  }
}
```

### Content-MD5

**Type:** string

</details>

## put_bucket_versioning

Sets the versioning state of an existing bucket. To set the versioning state, you must be the bucket owner.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "VersioningConfiguration" : {
    "Status" : "The versioning state of the bucket.",
    "MfaDelete" : "Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned."
  }
}
```

### Content-MD5

**Type:** string

### x-amz-mfa

The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.

**Type:** string

</details>

## put_bucket_website

Set the website configuration for a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### $body

**Type:** object

```json
{
  "WebsiteConfiguration" : {
    "IndexDocument" : {
      "Suffix" : "A suffix that is appended to a request that is for a directory on the website endpoint (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data that is returned will be for the object with the key name images/index.html) The suffix must not be empty and must not include a slash character."
    },
    "RedirectAllRequestsTo" : {
      "Protocol" : "Protocol to use (http, https) when redirecting requests. The default is the protocol that is used in the original request.",
      "HostName" : "Name of the host where requests will be redirected."
    },
    "RoutingRules" : [ {
      "RoutingRule" : {
        "Condition" : {
          "KeyPrefixEquals" : "The object key name prefix when the redirect is applied. For example, to redirect requests for ExamplePage.html, the key prefix will be ExamplePage.html. To redirect request for all pages with the prefix docs/, the key prefix will be /docs, which identifies all objects in the docs/ folder. Required when the parent element Condition is specified and sibling HttpErrorCodeReturnedEquals is not specified. If both conditions are specified, both must be true for the redirect to be applied.",
          "HttpErrorCodeReturnedEquals" : "The HTTP error code when the redirect is applied. In the event of an error, if the error code equals this value, then the specified redirect is applied. Required when parent element Condition is specified and sibling KeyPrefixEquals is not specified. If both are specified, then both must be true for the redirect to be applied."
        },
        "Redirect" : {
          "ReplaceKeyWith" : "The specific object key to use in the redirect request. For example, redirect request to error.html. Not required if one of the sibling is present. Can be present only if ReplaceKeyPrefixWith is not provided.",
          "HttpRedirectCode" : "The HTTP redirect code to use on the response. Not required if one of the siblings is present.",
          "Protocol" : "Protocol to use (http, https) when redirecting requests. The default is the protocol that is used in the original request.",
          "HostName" : "The host name to use in the redirect request.",
          "ReplaceKeyPrefixWith" : "The object key prefix to use in the redirect request. For example, to redirect requests for all pages with prefix docs/ (objects in the docs/ folder) to documents/, you can set a condition block with KeyPrefixEquals set to docs/ and in the Redirect set ReplaceKeyPrefixWith to /documents. Not required if one of the siblings is present. Can be present only if ReplaceKeyWith is not provided."
        }
      }
    } ],
    "ErrorDocument" : {
      "Key" : "The object key name to use when a 4XX class error occurs."
    }
  }
}
```

### Content-MD5

**Type:** string

</details>

## put_object

Adds an object to a bucket.

<details><summary>Parameters</summary>

### Bucket (required)

Name of the bucket to which the PUT operation was initiated.

**Type:** string

### Key (required)

Object key for which the PUT operation was initiated.

**Type:** string

### $body

Object data.

**Type:** blob

### Cache-Control

Specifies caching behavior along the request/reply chain.

**Type:** string

### Content-Disposition

Specifies presentational information for the object.

**Type:** string

### Content-Encoding

Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

**Type:** string

### Content-Language

The language the content is in.

**Type:** string

### Content-Length

Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.

**Type:** number

### Content-MD5

The base64-encoded 128-bit MD5 digest of the part data.

**Type:** string

### Content-Type

A standard MIME type describing the format of the object data.

**Type:** string

### Expires

The date and time at which the object is no longer cacheable.

**Type:** timestamp

### x-amz-acl

The canned ACL to apply to the object.

**Type:** string

**Potential values:** private, public-read, public-read-write, authenticated-read, aws-exec-read, bucket-owner-read, bucket-owner-full-control

### x-amz-grant-full-control

Gives the grantee READ, READ_ACP, and WRITE_ACP permissions on the object.

**Type:** string

### x-amz-grant-read

Allows grantee to read the object data and its metadata.

**Type:** string

### x-amz-grant-read-acp

Allows grantee to read the object ACL.

**Type:** string

### x-amz-grant-write-acp

Allows grantee to write the ACL for the applicable object.

**Type:** string

### x-amz-meta-

A map of metadata to store with the object in S3.

**Type:** object

```json
{
  "<string>" : "string"
}
```

### x-amz-request-payer

**Type:** string

**Potential values:** requester

### x-amz-server-side-encryption

The Server-side encryption algorithm used when storing this object in S3 (e.g., AES256, aws:kms).

**Type:** string

**Potential values:** AES256, aws:kms

### x-amz-server-side-encryption-aws-kms-key-id

Specifies the AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS will fail if not made via SSL or using SigV4. Documentation on configuring any of the officially supported AWS SDKs and CLI can be found at http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#specify-signature-version

**Type:** string

### x-amz-server-side-encryption-customer-algorithm

Specifies the algorithm to use to when encrypting the object (e.g., AES256).

**Type:** string

### x-amz-server-side-encryption-customer-key

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header.

**Type:** string

### x-amz-server-side-encryption-customer-key-MD5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.

**Type:** string

### x-amz-storage-class

The type of storage to use for the object. Defaults to 'STANDARD'.

**Type:** string

**Potential values:** STANDARD, REDUCED_REDUNDANCY, STANDARD_IA, ONEZONE_IA

### x-amz-tagging

The tag-set for the object. The tag-set must be encoded as URL Query parameters

**Type:** string

### x-amz-website-redirect-location

If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

**Type:** string

</details>

## put_object_acl

uses the acl subresource to set the access control list (ACL) permissions for an object that already exists in a bucket

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### $body

**Type:** object

```json
{
  "AccessControlPolicy" : {
    "AccessControlList" : [ {
      "Grant" : {
        "Grantee" : {
          "DisplayName" : "Screen name of the grantee.",
          "xsi:type" : "Type of grantee",
          "ID" : "The canonical user ID of the grantee.",
          "URI" : "URI of the grantee group.",
          "EmailAddress" : "Email address of the grantee."
        },
        "Permission" : "Specifies the permission given to the grantee."
      }
    } ],
    "Owner" : {
      "DisplayName" : "string",
      "ID" : "string"
    }
  }
}
```

### Content-MD5

**Type:** string

### versionId

VersionId used to reference a specific version of the object.

**Type:** string

### x-amz-acl

The canned ACL to apply to the object.

**Type:** string

**Potential values:** private, public-read, public-read-write, authenticated-read, aws-exec-read, bucket-owner-read, bucket-owner-full-control

### x-amz-grant-full-control

Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

**Type:** string

### x-amz-grant-read

Allows grantee to list the objects in the bucket.

**Type:** string

### x-amz-grant-read-acp

Allows grantee to read the bucket ACL.

**Type:** string

### x-amz-grant-write

Allows grantee to create, overwrite, and delete any object in the bucket.

**Type:** string

### x-amz-grant-write-acp

Allows grantee to write the ACL for the applicable bucket.

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

</details>

## put_object_tagging

Sets the supplied tag-set to an object that already exists in a bucket

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### $body

**Type:** object

```json
{
  "Tagging" : {
    "TagSet" : [ {
      "Tag" : {
        "Value" : "Value of the tag.",
        "Key" : "Name of the tag."
      }
    } ]
  }
}
```

### Content-MD5

**Type:** string

### versionId

**Type:** string

</details>

## restore_object

Restores an archived copy of an object back into Amazon S3

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### $body

**Type:** object

```json
{
  "RestoreRequest" : {
    "Type" : "Type of restore request.",
    "Description" : "The optional description for the job.",
    "Tier" : "Glacier retrieval tier at which the restore will be processed.",
    "Days" : "Lifetime of the active copy in days. Do not use with restores that specify OutputLocation.",
    "GlacierJobParameters" : {
      "Tier" : "Glacier retrieval tier at which the restore will be processed."
    },
    "SelectParameters" : {
      "Expression" : "The expression that is used to query the object.",
      "InputSerialization" : {
        "Parquet" : { },
        "CSV" : {
          "RecordDelimiter" : "Value used to separate individual records.",
          "QuoteCharacter" : "Value used for escaping where the field delimiter is part of the value.",
          "QuoteEscapeCharacter" : "Single character used for escaping the quote character inside an already escaped value.",
          "FieldDelimiter" : "Value used to separate individual fields in a record.",
          "Comments" : "Single character used to indicate a row should be ignored when present at the start of a row.",
          "AllowQuotedRecordDelimiter" : "Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.",
          "FileHeaderInfo" : "Describes the first line of input. Valid values: None, Ignore, Use."
        },
        "JSON" : {
          "Type" : "The type of JSON. Valid values: Document, Lines."
        },
        "CompressionType" : "Specifies object's compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE."
      },
      "ExpressionType" : "The type of the provided expression (e.g., SQL).",
      "OutputSerialization" : {
        "CSV" : {
          "RecordDelimiter" : "Value used to separate individual records.",
          "QuoteCharacter" : "Value used for escaping where the field delimiter is part of the value.",
          "QuoteEscapeCharacter" : "Single character used for escaping the quote character inside an already escaped value.",
          "QuoteFields" : "Indicates whether or not all output fields should be quoted.",
          "FieldDelimiter" : "Value used to separate individual fields in a record."
        },
        "JSON" : {
          "RecordDelimiter" : "The value used to separate individual records in the output."
        }
      }
    },
    "OutputLocation" : {
      "S3" : {
        "AccessControlList" : [ {
          "Grant" : {
            "Grantee" : {
              "DisplayName" : "Screen name of the grantee.",
              "xsi:type" : "Type of grantee",
              "ID" : "The canonical user ID of the grantee.",
              "URI" : "URI of the grantee group.",
              "EmailAddress" : "Email address of the grantee."
            },
            "Permission" : "Specifies the permission given to the grantee."
          }
        } ],
        "BucketName" : "The name of the bucket where the restore results will be placed.",
        "CannedACL" : "The canned ACL to apply to the restore results.",
        "StorageClass" : "The class of storage used to store the restore results.",
        "Tagging" : {
          "TagSet" : [ {
            "Tag" : {
              "Value" : "Value of the tag.",
              "Key" : "Name of the tag."
            }
          } ]
        },
        "UserMetadata" : [ {
          "MetadataEntry" : {
            "Value" : "string",
            "Name" : "string"
          }
        } ],
        "Prefix" : "The prefix that is prepended to the restore results for this request.",
        "Encryption" : {
          "EncryptionType" : "The server-side encryption algorithm used when storing job results in Amazon S3 (e.g., AES256, aws:kms).",
          "KMSKeyId" : "If the encryption type is aws:kms, this optional value specifies the AWS KMS key ID to use for encryption of job results.",
          "KMSContext" : "If the encryption type is aws:kms, this optional value can be used to specify the encryption context for the restore results."
        }
      }
    }
  }
}
```

### versionId

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

</details>

## select_object_content

This operation filters the contents of an Amazon S3 object based on a simple Structured Query Language (SQL) statement. In the request, along with the SQL expression, you must also specify a data serialization format (JSON or CSV) of the object. Amazon S3 uses this to parse object data into records, and returns only records that match the specified SQL expression. You must also specify the data serialization format for the response.

<details><summary>Parameters</summary>

### Bucket (required)

The S3 Bucket.

**Type:** string

### Key (required)

The Object Key.

**Type:** string

### $body

Request to filter the contents of an Amazon S3 object based on a simple Structured Query Language (SQL) statement. In the request, along with the SQL expression, you must also specify a data serialization format (JSON or CSV) of the object. Amazon S3 uses this to parse object data into records, and returns only records that match the specified SQL expression. You must also specify the data serialization format for the response. For more information, go to S3Select API Documentation.

**Type:** object

```json
{
  "SelectObjectContentRequest" : {
    "RequestProgress" : {
      "Enabled" : "Specifies whether periodic QueryProgress frames should be sent. Valid values: TRUE, FALSE. Default value: FALSE."
    },
    "Expression" : "The expression that is used to query the object.",
    "InputSerialization" : {
      "Parquet" : { },
      "CSV" : {
        "RecordDelimiter" : "Value used to separate individual records.",
        "QuoteCharacter" : "Value used for escaping where the field delimiter is part of the value.",
        "QuoteEscapeCharacter" : "Single character used for escaping the quote character inside an already escaped value.",
        "FieldDelimiter" : "Value used to separate individual fields in a record.",
        "Comments" : "Single character used to indicate a row should be ignored when present at the start of a row.",
        "AllowQuotedRecordDelimiter" : "Specifies that CSV field values may contain quoted record delimiters and such records should be allowed. Default value is FALSE. Setting this value to TRUE may lower performance.",
        "FileHeaderInfo" : "Describes the first line of input. Valid values: None, Ignore, Use."
      },
      "JSON" : {
        "Type" : "The type of JSON. Valid values: Document, Lines."
      },
      "CompressionType" : "Specifies object's compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE."
    },
    "ExpressionType" : "The type of the provided expression (e.g., SQL).",
    "OutputSerialization" : {
      "CSV" : {
        "RecordDelimiter" : "Value used to separate individual records.",
        "QuoteCharacter" : "Value used for escaping where the field delimiter is part of the value.",
        "QuoteEscapeCharacter" : "Single character used for escaping the quote character inside an already escaped value.",
        "QuoteFields" : "Indicates whether or not all output fields should be quoted.",
        "FieldDelimiter" : "Value used to separate individual fields in a record."
      },
      "JSON" : {
        "RecordDelimiter" : "The value used to separate individual records in the output."
      }
    }
  }
}
```

### x-amz-server-side-encryption-customer-algorithm

The SSE Algorithm used to encrypt the object. For more information, go to  Server-Side Encryption (Using Customer-Provided Encryption Keys. 

**Type:** string

### x-amz-server-side-encryption-customer-key

The SSE Customer Key. For more information, go to  Server-Side Encryption (Using Customer-Provided Encryption Keys. 

**Type:** string

### x-amz-server-side-encryption-customer-key-MD5

The SSE Customer Key MD5. For more information, go to  Server-Side Encryption (Using Customer-Provided Encryption Keys. 

**Type:** string

</details>

## upload_part

Uploads a part in a multipart upload. 
 Note: After you initiate multipart upload and upload one or more parts, you must either complete or abort multipart upload in order to stop getting charged for storage of the uploaded parts. Only after you either complete or abort multipart upload, Amazon S3 frees up the parts storage and stops charging you for the parts storage.

<details><summary>Parameters</summary>

### Bucket (required)

Name of the bucket to which the multipart upload was initiated.

**Type:** string

### Key (required)

Object key for which the multipart upload was initiated.

**Type:** string

### partNumber (required)

Part number of part being uploaded. This is a positive integer between 1 and 10,000.

**Type:** integer

### uploadId (required)

Upload ID identifying the multipart upload whose part is being uploaded.

**Type:** string

### $body

Object data.

**Type:** blob

### Content-Length

Size of the body in bytes. This parameter is useful when the size of the body cannot be determined automatically.

**Type:** number

### Content-MD5

The base64-encoded 128-bit MD5 digest of the part data.

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

### x-amz-server-side-encryption-customer-algorithm

Specifies the algorithm to use to when encrypting the object (e.g., AES256).

**Type:** string

### x-amz-server-side-encryption-customer-key

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.

**Type:** string

### x-amz-server-side-encryption-customer-key-MD5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.

**Type:** string

</details>

## upload_part_copy

Uploads a part by copying data from an existing object as data source.

<details><summary>Parameters</summary>

### Bucket (required)

**Type:** string

### Key (required)

**Type:** string

### partNumber (required)

Part number of part being copied. This is a positive integer between 1 and 10,000.

**Type:** integer

### uploadId (required)

Upload ID identifying the multipart upload whose part is being copied.

**Type:** string

### x-amz-copy-source (required)

The name of the source bucket and key name of the source object, separated by a slash (/). Must be URL-encoded.

**Type:** string

### x-amz-copy-source-if-match

Copies the object if its entity tag (ETag) matches the specified tag.

**Type:** string

### x-amz-copy-source-if-modified-since

Copies the object if it has been modified since the specified time.

**Type:** timestamp

### x-amz-copy-source-if-none-match

Copies the object if its entity tag (ETag) is different than the specified ETag.

**Type:** string

### x-amz-copy-source-if-unmodified-since

Copies the object if it hasn't been modified since the specified time.

**Type:** timestamp

### x-amz-copy-source-range

The range of bytes to copy from the source object. The range value must use the form bytes=first-last, where the first and last are the zero-based byte offsets to copy. For example, bytes=0-9 indicates that you want to copy the first ten bytes of the source. You can copy a range only if the source object is greater than 5 GB.

**Type:** string

### x-amz-copy-source-server-side-encryption-customer-algorithm

Specifies the algorithm to use when decrypting the source object (e.g., AES256).

**Type:** string

### x-amz-copy-source-server-side-encryption-customer-key

Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided in this header must be one that was used when the source object was created.

**Type:** string

### x-amz-copy-source-server-side-encryption-customer-key-MD5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.

**Type:** string

### x-amz-request-payer

**Type:** string

**Potential values:** requester

### x-amz-server-side-encryption-customer-algorithm

Specifies the algorithm to use to when encrypting the object (e.g., AES256).

**Type:** string

### x-amz-server-side-encryption-customer-key

Specifies the customer-provided encryption key for Amazon S3 to use in encrypting data. This value is used to store the object and then it is discarded; Amazon does not store the encryption key. The key must be appropriate for use with the algorithm specified in the x-amz-server-side​-encryption​-customer-algorithm header. This must be the same encryption key specified in the initiate multipart upload request.

**Type:** string

### x-amz-server-side-encryption-customer-key-MD5

Specifies the 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure the encryption key was transmitted without error.

**Type:** string

</details>

