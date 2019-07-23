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

#### $body

**Type:** object

</details>

## batch_delete_image

Deletes a list of specified images within a specified repository. Images are specified with either imageTag or imageDigest. 
You can remove a tag from an image by specifying the image's tag in your request. When you remove the last tag from an image, the image is deleted from your repository. 
You can completely delete an image (and all of its tags) by specifying the image's digest in your request.

<details><summary>Parameters</summary>

#### $body

Deletes specified images within a specified repository. Images are specified with either the imageTag or imageDigest.

**Type:** object

</details>

## batch_get_image

Gets detailed information for specified images within a specified repository. Images are specified with either imageTag or imageDigest.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## complete_layer_upload

Informs Amazon ECR that the image layer upload has completed for a specified registry, repository name, and upload ID. You can optionally provide a sha256 digest of the image layer for data validation purposes.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## create_repository

Creates an image repository.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_lifecycle_policy

Deletes the specified lifecycle policy.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_repository

Deletes an existing image repository. If a repository contains images, you must use the force option to delete it.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## delete_repository_policy

Deletes the repository policy from a specified repository.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## describe_images

Returns metadata about the images in a repository, including image size, image tags, and creation date.  
Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the docker images command shows the uncompressed image size, so it may return a larger image size than the image sizes returned by DescribeImages.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## describe_repositories

Describes image repositories in a registry.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_authorization_token

Retrieves a token that is valid for a specified registry for 12 hours. This command allows you to use the docker CLI to push and pull images with Amazon ECR. If you do not specify a registry, the default registry is assumed. 
The authorizationToken returned for each registry specified is a base64 encoded string that can be decoded and used in a docker login command to authenticate to a registry. The AWS CLI offers an aws ecr get-login command that simplifies the login process.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_download_url_for_layer

Retrieves the pre-signed Amazon S3 download URL corresponding to an image layer. You can only get URLs for image layers that are referenced in an image.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_lifecycle_policy

Retrieves the specified lifecycle policy.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_lifecycle_policy_preview

Retrieves the results of the specified lifecycle policy preview request.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## get_repository_policy

Retrieves the repository policy for a specified repository.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## initiate_layer_upload

Notify Amazon ECR that you intend to upload an image layer.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## list_images

Lists all the image IDs for a given repository. 
You can filter images based on whether or not they are tagged by setting the tagStatus parameter to TAGGED or UNTAGGED. For example, you can filter your results to return only UNTAGGED images and then pipe that result to a BatchDeleteImage operation to delete them. Or, you can filter your results to return only TAGGED images to list all of the tags in your repository.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## put_image

Creates or updates the image manifest and tags associated with an image.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## put_lifecycle_policy

Creates or updates a lifecycle policy. For information about lifecycle policy syntax, see Lifecycle Policy Template.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## set_repository_policy

Applies a repository policy on a specified repository to control access permissions.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## start_lifecycle_policy_preview

Starts a preview of the specified lifecycle policy. This allows you to see the results before creating the lifecycle policy.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

## upload_layer_part

Uploads an image layer part to Amazon ECR.  
This operation is used by the Amazon ECR proxy, and it is not intended for general use by customers for pulling and pushing images. In most cases, you should use the docker CLI to pull, tag, and push images.

<details><summary>Parameters</summary>

#### $body

**Type:** object

</details>

