---
id: lambda-documentation
title: Lambda (version v1.*.*)
---

## invoke_function



<details><summary>Parameters</summary>

#### functionName (required)

The Lambda function name

**Type:** string

#### $body

Payload containing params used by lambda function

**Type:** object

#### Qualifier

Using this optional parameter to specify a function version or an alias name

**Type:** string

#### X-Amz-Invocation-Type

Whether to invoke synchronously, asynchronously, or as a dry run

**Type:** string

**Potential values:** Event, RequestResponse, DryRun

</details>

## list_functions



<details><summary>Parameters</summary>

#### functionVersion

Optional string. If not specified, only the unqualified functions ARNs (Amazon Resource Names) will be returned.

**Type:** string

#### marker

Optional string. An opaque pagination token returned from a previous ListFunctions operation. If present, indicates where to continue the listing.

**Type:** string

#### masterRegion

Optional string. If not specified, will return only regular function versions (i.e., non-replicated versions).

**Type:** string

#### maxItems

Optional integer. Specifies the maximum number of AWS Lambda functions to return in response. This parameter value must be greater than 0.

**Type:** string

</details>

