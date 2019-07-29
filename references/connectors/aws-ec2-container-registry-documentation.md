---
id: aws-ec2-container-registry-documentation
title: AWS EC2 Container Registry (version v5.*.*)
sidebar_label: AWS EC2 Container Registry
layout: docs.mustache
---

## batch_check_layer_availability

Check the availability of multiple image layers in a specified registry and repository.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "registryId" : "The AWS account ID associated with the registry that contains the image layers to check. If you do not specify a registry, the default registry is assumed.",
  "layerDigests" : [ "string" ],
  "repositoryName" : "The name of the repository that is associated with the image layers to check."
}
```

</details>

## batch_delete_image

Deletes a list of specified images within a specified repository. Images are specified with either imageTag or imageDigest. 
You can remove a tag from an image by specifying the image's tag in your request. When you remove the last tag from an image, the image is deleted from your repository. 
You can completely delete an image (and all of its tags) by specifying the image's digest in your request.

<details><summary>Parameters</summary>

### $body

Deletes specified images within a specified repository. Images are specified with either the imageTag or imageDigest.

**Type:** object

```json
{
  "registryId" : "The AWS account ID associated with the registry that contains the image to delete. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The repository that contains the image to delete.",
  "imageIds" : [ {
    "imageTag" : "The tag used for the image.",
    "imageDigest" : "The sha256 digest of the image manifest."
  } ]
}
```

</details>

## batch_get_image

Gets detailed information for specified images within a specified repository. Images are specified with either imageTag or imageDigest.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "acceptedMediaTypes" : [ "string" ],
  "registryId" : "The AWS account ID associated with the registry that contains the images to describe. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The repository that contains the images to describe.",
  "imageIds" : [ {
    "imageTag" : "The tag used for the image.",
    "imageDigest" : "The sha256 digest of the image manifest."
  } ]
}
```

</details>

## complete_layer_upload

Informs Amazon ECR that the image layer upload has completed for a specified registry, repository name, and upload ID. You can optionally provide a sha256 digest of the image layer for data validation purposes.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "uploadId" : "The upload ID from a previous InitiateLayerUpload operation to associate with the image layer.",
  "registryId" : "The AWS account ID associated with the registry to which to upload layers. If you do not specify a registry, the default registry is assumed.",
  "layerDigests" : [ "string" ],
  "repositoryName" : "The name of the repository to associate with the image layer."
}
```

</details>

## create_repository

Creates an image repository.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "repositoryName" : "The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app)."
}
```

</details>

## delete_lifecycle_policy

Deletes the specified lifecycle policy.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "registryId" : "The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository."
}
```

</details>

## delete_repository

Deletes an existing image repository. If a repository contains images, you must use the force option to delete it.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "registryId" : "The AWS account ID associated with the registry that contains the repository to delete. If you do not specify a registry, the default registry is assumed.",
  "force" : " If a repository contains images, forces the deletion.",
  "repositoryName" : "The name of the repository to delete."
}
```

</details>

## delete_repository_policy

Deletes the repository policy from a specified repository.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "registryId" : "The AWS account ID associated with the registry that contains the repository policy to delete. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository that is associated with the repository policy to delete."
}
```

</details>

## describe_images

Returns metadata about the images in a repository, including image size, image tags, and creation date.  
Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the docker images command shows the uncompressed image size, so it may return a larger image size than the image sizes returned by DescribeImages.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "filter" : {
    "tagStatus" : "The tag status with which to filter your DescribeImages results. You can filter results based on whether they are TAGGED or UNTAGGED."
  },
  "registryId" : "The AWS account ID associated with the registry that contains the repository in which to describe images. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.",
  "imageIds" : [ {
    "imageTag" : "The tag used for the image.",
    "imageDigest" : "The sha256 digest of the image manifest."
  } ]
}
```

</details>

## describe_repositories

Describes image repositories in a registry.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "repositoryNames" : [ "string" ],
  "registryId" : "The AWS account ID associated with the registry that contains the repositories to be described. If you do not specify a registry, the default registry is assumed."
}
```

</details>

## get_authorization_token

Retrieves a token that is valid for a specified registry for 12 hours. This command allows you to use the docker CLI to push and pull images with Amazon ECR. If you do not specify a registry, the default registry is assumed. 
The authorizationToken returned for each registry specified is a base64 encoded string that can be decoded and used in a docker login command to authenticate to a registry. The AWS CLI offers an aws ecr get-login command that simplifies the login process.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "registryIds" : [ "string" ]
}
```

</details>

## get_download_url_for_layer

Retrieves the pre-signed Amazon S3 download URL corresponding to an image layer. You can only get URLs for image layers that are referenced in an image.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "layerDigest" : "The digest of the image layer to download.",
  "registryId" : "The AWS account ID associated with the registry that contains the image layer to download. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository that is associated with the image layer to download."
}
```

</details>

## get_lifecycle_policy

Retrieves the specified lifecycle policy.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "registryId" : "The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository."
}
```

</details>

## get_lifecycle_policy_preview

Retrieves the results of the specified lifecycle policy preview request.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "filter" : {
    "tagStatus" : "The tag status of the image."
  },
  "nextToken" : "The nextToken value returned from a previous paginated  GetLifecyclePolicyPreviewRequest request where maxResults was used and the  results exceeded the value of that parameter. Pagination continues from the end of the  previous results that returned the nextToken value. This value is  null when there are no more results to return. This option cannot be used when you specify images with imageIds.",
  "maxResults" : "The maximum number of repository results returned by GetLifecyclePolicyPreviewRequest in  paginated output. When this parameter is used, GetLifecyclePolicyPreviewRequest only returns  maxResults results in a single page along with a nextToken  response element. The remaining results of the initial request can be seen by sending  another GetLifecyclePolicyPreviewRequest request with the returned nextToken  value. This value can be between 1 and 100. If this  parameter is not used, then GetLifecyclePolicyPreviewRequest returns up to  100 results and a nextToken value, if  applicable. This option cannot be used when you specify images with imageIds.",
  "registryId" : "The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository.",
  "imageIds" : [ {
    "imageTag" : "The tag used for the image.",
    "imageDigest" : "The sha256 digest of the image manifest."
  } ]
}
```

</details>

## get_repository_policy

Retrieves the repository policy for a specified repository.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "registryId" : "The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository with the policy to retrieve."
}
```

</details>

## initiate_layer_upload

Notify Amazon ECR that you intend to upload an image layer.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "registryId" : "The AWS account ID associated with the registry to which you intend to upload layers. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository to which you intend to upload layers."
}
```

</details>

## list_images

Lists all the image IDs for a given repository. 
You can filter images based on whether or not they are tagged by setting the tagStatus parameter to TAGGED or UNTAGGED. For example, you can filter your results to return only UNTAGGED images and then pipe that result to a BatchDeleteImage operation to delete them. Or, you can filter your results to return only TAGGED images to list all of the tags in your repository.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "filter" : {
    "tagStatus" : "The tag status with which to filter your ListImages results. You can filter results based on whether they are TAGGED or UNTAGGED."
  },
  "registryId" : "The AWS account ID associated with the registry that contains the repository in which to list images. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The repository with image IDs to be listed."
}
```

</details>

## put_image

Creates or updates the image manifest and tags associated with an image.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "imageManifest" : "The image manifest corresponding to the image to be uploaded.",
  "registryId" : "The AWS account ID associated with the registry that contains the repository in which to put the image. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository in which to put the image.",
  "imageTag" : "The tag to associate with the image. This parameter is required for images that use the Docker Image Manifest V2 Schema 2 or OCI formats."
}
```

</details>

## put_lifecycle_policy

Creates or updates a lifecycle policy. For information about lifecycle policy syntax, see Lifecycle Policy Template.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "registryId" : "The AWS account ID associated with the registry that contains the repository. If you do  not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository to receive the policy.",
  "lifecyclePolicyText" : "The JSON repository policy text to apply to the repository."
}
```

</details>

## set_repository_policy

Applies a repository policy on a specified repository to control access permissions.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "policyText" : "The JSON repository policy text to apply to the repository.",
  "registryId" : "The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.",
  "force" : "If the policy you are attempting to set on a repository policy would prevent you from setting another policy in the future, you must force the SetRepositoryPolicy operation. This is intended to prevent accidental repository lock outs.",
  "repositoryName" : "The name of the repository to receive the policy."
}
```

</details>

## start_lifecycle_policy_preview

Starts a preview of the specified lifecycle policy. This allows you to see the results before creating the lifecycle policy.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "registryId" : "The AWS account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository to be evaluated.",
  "lifecyclePolicyText" : "The policy to be evaluated against. If you do not specify a policy, the current policy for the repository is used."
}
```

</details>

## upload_layer_part

Uploads an image layer part to Amazon ECR.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "uploadId" : "The upload ID from a previous InitiateLayerUpload operation to associate with the layer part upload.",
  "layerPartBlob" : "The base64-encoded layer part payload.",
  "registryId" : "The AWS account ID associated with the registry to which you are uploading layer parts. If you do not specify a registry, the default registry is assumed.",
  "repositoryName" : "The name of the repository to which you are uploading layer parts.",
  "partFirstByte" : "The integer value of the first byte of the layer part.",
  "partLastByte" : "The integer value of the last byte of the layer part."
}
```

</details>

