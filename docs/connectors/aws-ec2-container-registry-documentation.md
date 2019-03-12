---
id: aws-ec2-container-registry-documentation
title: AWS EC2 Container Registry (version v3.*.*)
sidebar_label: AWS EC2 Container Registry
---

## batch_check_layer_availability

Check the availability of multiple image layers in a specified registry and repository.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchCheckLayerAvailability.html

<details><summary>Parameters</summary>

#### layerDigests (required)

The digests of the image layers to check.

**Type:** ARRAY

#### repositoryName (required)

The name of the repository that is associated with the image layers to check.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry that contains the image layers to check. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## batch_delete_image

Deletes a list of specified images within a specified repository. Images are specified with either imageTag or imageDigest.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchDeleteImage.html

<details><summary>Parameters</summary>

#### imageIds (required)

A list of image ID references that correspond to images to delete. The format of the imageIds reference is imageTag=tag or imageDigest=digest.

**Type:** ARRAY

#### repositoryName (required)

The repository that contains the image to delete.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry that contains the image to delete. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## batch_get_image

Gets detailed information for specified images within a specified repository. Images are specified with either imageTag or imageDigest.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_BatchGetImage.html

<details><summary>Parameters</summary>

#### imageIds (required)

A list of image ID references that correspond to images to describe. The format of the imageIds reference is imageTag=tag or imageDigest=digest.

**Type:** ARRAY

#### repositoryName (required)

The repository that contains the images to describe.

**Type:** STRING

#### acceptedMediaTypes

The accepted media types for the request. Valid values: application/vnd.docker.distribution.manifest.v1+json | application/vnd.docker.distribution.manifest.v2+json | application/vnd.oci.image.manifest.v1+json

**Type:** ARRAY

#### registryId

The AWS account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## complete_layer_upload

Informs Amazon ECR that the image layer upload has completed for a specified registry, repository name, and upload ID. You can optionally provide a sha256 digest of the image layer for data validation purposes.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CompleteLayerUpload.html

<details><summary>Parameters</summary>

#### layerDigests (required)

The sha256 digest of the image layer.

**Type:** ARRAY

#### repositoryName (required)

The name of the repository to associate with the image layer.

**Type:** STRING

#### uploadId (required)

The upload ID from a previous InitiateLayerUpload operation to associate with the image layer.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry to which to upload layers. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## create_repository

Creates an image repository. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CreateRepository.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app).

**Type:** STRING

</details>

## delete_lifecycle_policy

Deletes the specified lifecycle policy. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteLifecyclePolicy.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The name of the repository.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## delete_repository

Deletes an existing image repository. If a repository contains images, you must use the force option to delete it.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRepository.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The name of the repository to delete.

**Type:** STRING

#### force

If a repository contains images, forces the deletion.

**Type:** BOOLEAN

#### registryId

The AWS account ID associated with the registry that contains the repository to delete. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## delete_repository_policy

Deletes the repository policy from a specified repository. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRepositoryPolicy.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The name of the repository that is associated with the repository policy to delete.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry that contains the repository policy to delete. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## describe_images

Returns metadata about the images in a repository, including image size, image tags, and creation date.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeImages.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The repository that contains the images to describe.

**Type:** STRING

#### filter

The filter key and value with which to filter your DescribeImages results.

**Type:** OBJECT

#### imageIds

The list of image IDs for the requested repository.

**Type:** ARRAY

#### registryId

The AWS account ID associated with the registry that contains the repository in which to describe images. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## describe_repositories

Describes image repositories in a registry. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DescribeRepositories.html

<details><summary>Parameters</summary>

#### registryId

The AWS account ID associated with the registry that contains the repositories to be described. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

#### repositoryNames

A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.

**Type:** ARRAY

</details>

## get_authorization_token

Retrieves a token that is valid for a specified registry for 12 hours. This command allows you to use the docker CLI to push and pull images with Amazon ECR. If you do not specify a registry, the default registry is assumed.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetAuthorizationToken.html

<details><summary>Parameters</summary>

#### registryIds

A list of AWS account IDs that are associated with the registries for which to get authorization tokens. If you do not specify a registry, the default registry is assumed.

**Type:** ARRAY

</details>

## get_download_url_for_layer

Retrieves the pre-signed Amazon S3 download URL corresponding to an image layer. You can only get URLs for image layers that are referenced in an image.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetDownloadUrlForLayer.html

<details><summary>Parameters</summary>

#### layerDigest (required)

The digest of the image layer to download.

**Type:** STRING

#### repositoryName (required)

The name of the repository that is associated with the image layer to download.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry that contains the image layer to download. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## get_lifecycle_policy

Retrieves the specified lifecycle policy. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetLifecyclePolicy.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The name of the repository.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## get_lifecycle_policy_preview

Retrieves the results of the specified lifecycle policy preview request. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetLifecyclePolicyPreview.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The name of the repository.

**Type:** STRING

#### filter

An optional parameter that filters results based on image tag status and all tags, if tagged.

**Type:** OBJECT

#### imageIds

The list of imageIDs to be included.

**Type:** ARRAY

#### maxResults

applicable. This option cannot be used when you specify images with imageIds.

**Type:** INTEGER

#### nextToken

null when there are no more results to return. This option cannot be used when you specify images with imageIds.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## get_repository_policy

Retrieves the repository policy for a specified repository. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_GetRepositoryPolicy.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The name of the repository with the policy to retrieve.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## initiate_layer_upload

Notify Amazon ECR that you intend to upload an image layer. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_InitiateLayerUpload.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The name of the repository to which you intend to upload layers.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry to which you intend to upload layers. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## list_images

Lists all the image IDs for a given repository. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListImages.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The repository with image IDs to be listed.

**Type:** STRING

#### filter

The filter key and value with which to filter your ListImages results.

**Type:** OBJECT

#### registryId

The AWS account ID associated with the registry that contains the repository in which to list images. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## list_tags_for_resource

List the tags for an Amazon ECR resource. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ListTagsForResource.html

<details><summary>Parameters</summary>

#### resourceArn (required)

The Amazon Resource Name (ARN) that identifies the resource for which to list the tags. Currently, the only supported resource is an Amazon ECR repository.

**Type:** STRING

</details>

## put_image

Creates or updates the image manifest and tags associated with an image. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutImage.html

<details><summary>Parameters</summary>

#### imageManifest (required)

The image manifest corresponding to the image to be uploaded.

**Type:** STRING

#### repositoryName (required)

The name of the repository in which to put the image.

**Type:** STRING

#### imageTag

The tag to associate with the image. This parameter is required for images that use the Docker Image Manifest V2 Schema 2 or OCI formats.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry that contains the repository in which to put the image. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## put_lifecycle_policy

Creates or updates a lifecycle policy. For information about lifecycle policy syntax, see Lifecycle Policy Template.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutLifecyclePolicy.html

<details><summary>Parameters</summary>

#### lifecyclePolicyText (required)

The JSON repository policy text to apply to the repository.

**Type:** STRING

#### repositoryName (required)

The name of the repository to receive the policy.

**Type:** STRING

#### registryId

not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## set_repository_policy

Applies a repository policy on a specified repository to control access permissions. For more information, see Amazon ECR Repository Policies in the Amazon Elastic Container Registry User Guide.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_SetRepositoryPolicy.html

<details><summary>Parameters</summary>

#### policyText (required)

The JSON repository policy text to apply to the repository. For more information, see Amazon ECR Repository Policy Examples in the Amazon Elastic Container Registry User Guide.

**Type:** STRING

#### repositoryName (required)

The name of the repository to receive the policy.

**Type:** STRING

#### force

If the policy you are attempting to set on a repository policy would prevent you from setting another policy in the future, you must force the SetRepositoryPolicy operation. This is intended to prevent accidental repository lock outs.

**Type:** BOOLEAN

#### registryId

The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## start_lifecycle_policy_preview

Starts a preview of the specified lifecycle policy. This allows you to see the results before creating the lifecycle policy.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_StartLifecyclePolicyPreview.html

<details><summary>Parameters</summary>

#### repositoryName (required)

The name of the repository to be evaluated.

**Type:** STRING

#### lifecyclePolicyText

The policy to be evaluated against. If you do not specify a policy, the current policy for the repository is used.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

## tag_resource

Adds specified tags to a resource with the specified ARN. Existing tags on a resource are not changed if they are not specified in the request parameters.  https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_TagResource.html

<details><summary>Parameters</summary>

#### resourceArn (required)

The Amazon Resource Name (ARN) of the the resource to which to add tags. Currently, the only supported resource is an Amazon ECR repository.

**Type:** STRING

#### tags (required)

The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

**Type:** ARRAY

</details>

## untag_resource

Deletes specified tags from a resource. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UntagResource.html

<details><summary>Parameters</summary>

#### resourceArn (required)

The Amazon Resource Name (ARN) of the resource from which to remove tags. Currently, the only supported resource is an Amazon ECR repository.

**Type:** STRING

#### tagKeys (required)

The keys of the tags to be removed.

**Type:** ARRAY

</details>

## upload_layer_part

Uploads an image layer part to Amazon ECR. https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_UploadLayerPart.html

<details><summary>Parameters</summary>

#### layerPartBlob (required)

The base64-encoded layer part payload.

**Type:** OBJECT

#### partFirstByte (required)

The integer value of the first byte of the layer part.

**Type:** OBJECT

#### partLastByte (required)

The integer value of the last byte of the layer part.

**Type:** OBJECT

#### repositoryName (required)

The name of the repository to which you are uploading layer parts.

**Type:** STRING

#### uploadId (required)

The upload ID from a previous InitiateLayerUpload operation to associate with the layer part upload.

**Type:** STRING

#### registryId

The AWS account ID associated with the registry to which you are uploading layer parts. If you do not specify a registry, the default registry is assumed.

**Type:** STRING

</details>

