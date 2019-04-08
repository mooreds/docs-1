---
id: google-hire-documentation
title: Google Hire (version v1.*.*)
sidebar_label: Google Hire
---

## create_job



<details><summary>Parameters</summary>

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

#### $body

**Type:** object

</details>

## create_registration



<details><summary>Parameters</summary>

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

#### $body

**Type:** object

</details>

## delete_job



<details><summary>Parameters</summary>

#### name (required)

Required.The name of the job to delete.

**Type:** string

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## delete_registration



<details><summary>Parameters</summary>

#### name (required)

Required. The name of the Registration to be deleted.

**Type:** string

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## get_application



<details><summary>Parameters</summary>

#### name (required)

The name of the application to retrieve.

**Type:** string

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## get_candidate



<details><summary>Parameters</summary>

#### name (required)

The name of the candidate to retrieve.

**Type:** string

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## get_custom_field_specs



<details><summary>Parameters</summary>

#### name (required)

The name of the custom field spec to retrieve.

**Type:** string

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## get_job



<details><summary>Parameters</summary>

#### name (required)

Required.The name of the job to delete.

**Type:** string

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## get_user



<details><summary>Parameters</summary>

#### name (required)

The name of the application to retrieve.

**Type:** string

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## list_applications



<details><summary>Parameters</summary>

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

#### filter

Optional filter on applications fields. Attempts to query with an unrecognized filter dimension will result in an INVALID_ARGUMENT error. Supported querying are as follows:
  status.state=[Application.Status.State]
  status.update_time>=[RFS 3339 formatted Timestamp]
For filtering on multiple fields, we only support AND operations. Sample Query:
  status.state=ACTIVE AND status.update_time>="2018-01-02T06:23:10.843Z"

**Type:** string

</details>

## list_candidates



<details><summary>Parameters</summary>

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

#### filter

Optional filter on candidate fields. Supported dimensions for querying are as follows:
  applications.status.state=[Application.Status.State]
Attempts to query with an unrecognized filter dimension will result in an INVALID_ARGUMENT error. Sample Query:
  applications.status.state=ACCEPTED

**Type:** string

</details>

## list_custom_field_specs



<details><summary>Parameters</summary>

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

#### filter

Optional filter on custom field spec. Attempts to query with an unrecognized filter dimension will result in an INVALID_ARGUMENT error. Supported querying are as follows:
  objectTypes[]=[CustomFieldSpec.ObjectType]
Sample Query:
  objectTypes[]=JOB

**Type:** string

</details>

## list_jobs



<details><summary>Parameters</summary>

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

#### filter

Optional.Supported dimensions for querying are as follows:
  state=[Job.State]
Attempts to query with an unrecognized filter dimension will result in an INVALID_ARGUMENT error. Sample Query:
  state=OPEN

**Type:** string

</details>

## update_job



<details><summary>Parameters</summary>

#### name (required)

Required.The name of the job to delete.

**Type:** string

#### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

#### $body

**Type:** object

</details>

