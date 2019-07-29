---
id: algorithmia-documentation
title: Algorithmia (version v1.*.*)
sidebar_label: Algorithmia
layout: docs.mustache
---

## call_algorithm



<details><summary>Parameters</summary>

### algorithm (required)

Name of the algorithm. If a specific version is required, specify as "{algorithm}/{version}", where version is in the format "1.x.x" and "x" can be the wildcard "*".

**Type:** string

### user (required)

username of the algorithm

**Type:** string

### $body

see sample input for the specific Algorithm from http://algorithmia.com/algorithms

**Type:** string

### output

If "raw", returns the result of the algorithm call without the JSON-RPC wrapper. If the algorithm returned an error then an HTTP 400 status code will be used. If "void", returns immediately and does not wait for the algorithm to run. The result of the algorithm will not be accessible; this is useful in some cases where an algorithm outputs to a data:// file with a long running time.

**Type:** string

**Potential values:** raw, void

### stdout

Indicates algorithm stdout should be returned in the response metadata (ignored unless you are the algorithm owner)

**Type:** boolean

### timeout

Specifies a timeout for the call in seconds.

**Type:** number

</details>

## create_directory

Create a new directory with the specified path as the parent directory.

<details><summary>Parameters</summary>

### connector (required)

The data source: data, dropbox, s3, or a labeled variant (e.g. dropbox+mylabel).

**Type:** string

### path (required)

The path, relative to the root of a given data source.

**Type:** string

### $body

**Type:** object

```json
{
  "name" : "Name of the directory to create",
  "acl" : {
    "read" : [ "string" ]
  }
}
```

</details>

## delete_object

Delete a specified directory or file.

<details><summary>Parameters</summary>

### connector (required)

The data source: data, dropbox, s3, or a labeled variant (e.g. dropbox+mylabel).

**Type:** string

### path (required)

The path, relative to the root of a given data source.

**Type:** string

### force

If true, enables recursive delete of a non-empty directory

**Type:** boolean

</details>

## list_path

This operation either lists the contents of a directory, if a directory is specified in the path, or gets a file. If you aren’t sure if a path refers to a file or directory, you should first check if it exists. The `exists` methods make a `HEAD` request that check the `X-Data-Type` response header.

<details><summary>Parameters</summary>

### connector (required)

The data source: data, dropbox, s3, or a labeled variant (e.g. dropbox+mylabel).

**Type:** string

### path (required)

The path, relative to the root of a given data source.

**Type:** string

### acl

Include the directory ACL in the response.

**Type:** boolean

### marker

Indicates the page of results to return. Only valid when using markers previously returned by this API. If this parameter is omitted then the first page is returned.

**Type:** string

</details>

## update_directory

Update specified directory's ACL.

<details><summary>Parameters</summary>

### connector (required)

The data source: data, dropbox, s3, or a labeled variant (e.g. dropbox+mylabel).

**Type:** string

### path (required)

The path, relative to the root of a given data source.

**Type:** string

### $body

**Type:** object

```json
{
  "acl" : {
    "read" : [ "string" ]
  }
}
```

</details>

## upload_file

Upload a file through the Algorithmia Data API.

<details><summary>Parameters</summary>

### connector (required)

The data source: data, dropbox, s3, or a labeled variant (e.g. dropbox+mylabel).

**Type:** string

### path (required)

The path, relative to the root of a given data source.

**Type:** string

### $body

**Type:** string

</details>

