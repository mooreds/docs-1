---
id: google-hire-documentation
title: Google Hire (version v1.*.*)
sidebar_label: Google Hire
layout: docs.mustache
---

## create_job



<details><summary>Parameters</summary>

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

### $body

**Type:** object

```json
{
  "job" : {
    "publishState" : "string",
    "employmentType" : "string",
    "customFields" : { },
    "description" : "Optional.Description of the job.",
    "timeCommitment" : "string",
    "title" : "Required.The human readable job title.",
    "compensationInfo" : {
      "compensation_amount" : {
        "nanos" : "Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If units is positive, nanos must be positive or zero. If units is zero, nanos can be positive, zero, or negative. If units is negative, nanos must be negative or zero. For example $-1.75 is represented as units=-1 and nanos=-750,000,000.",
        "units" : "The whole units of the amount. For example if currencyCode is \"USD\", then 1 unit is one US dollar.",
        "currencyCode" : "The 3-letter currency code defined in ISO 4217."
      },
      "candidateVisible" : "Optional.Indicates if compensation information is available to candidates.",
      "frequency" : "string"
    },
    "requisitionId" : "Output only. Can be set on jobs.create.Id used to link data with external systems.",
    "createTime" : "Output only.Date the job was created or the date specified when importing this job.A timestamp in RFC3339 UTC \"Zulu\" format, accurate to nanoseconds. Example: \"2014-10-02T15:01:23.045123456Z\".",
    "creatingUser" : "Optional.Resource name of the user that created the job. It must have the format of \"tenants/*/users/*\".",
    "coordinators" : [ "string" ],
    "name" : "Output only. Required during jobs.patch.The resource name of this Job. This is generated by the service when a job is created. Job name takes the form of \"tenants/*/jobs/*\".",
    "location" : {
      "postalAddress" : {
        "regionCode" : "Required. CLDR region code of the country/region of the address. This is never inferred and it is up to the user to ensure the value is correct. See http://cldr.unicode.org/ and http://www.unicode.org/cldr/charts/30/supplemental/territory_information.html for details.",
        "sortingCode" : "Optional. Additional, country-specific, sorting code. This is not used in most regions. Where it is used, the value is either a string like \"CEDEX\", optionally followed by a number (e.g. \"CEDEX 7\"), or just a number alone, representing the \"sector code\" (Jamaica), \"delivery area indicator\" (Malawi) or \"post office indicator\" (e.g. Côte d'Ivoire).",
        "recipients" : [ "string" ],
        "postalCode" : "Optional. Postal code of the address. Not all countries use or require postal codes to be present, but where they are used, they may trigger additional validation with other parts of the address (e.g. state/zip validation in the U.S.A.).",
        "organization" : "Optional. The name of the organization at the address.",
        "locality" : "Optional. Generally refers to the city/town portion of the address. In regions of the world where localities are not well defined or do not fit into this structure well, leave locality empty and use addressLines.",
        "sublocality" : "Optional. Sublocality of the address. For example, this can be neighborhoods, boroughs, districts.",
        "addressLines" : [ "string" ],
        "languageCode" : "Optional. BCP-47 language code of the contents of this address (if known). This is often the UI language of the input form or is expected to match one of the languages used in the address' country/region, or their transliterated equivalents. This can affect formatting in certain countries, but is not critical to the correctness of the data and will never affect any validation or other non-formatting related operations. If this value is not known, it should be omitted (rather than specifying a possibly incorrect default).",
        "administrativeArea" : "Optional. Highest administrative subdivision which is used for postal addresses of a country or region. For example, this can be a state, a province, an oblast, or a prefecture. Specifically, for Spain this is the province and not the autonomous community (e.g. \"Barcelona\" and not \"Catalonia\"). Many countries don't use an administrative area in postal addresses. E.g. in Switzerland this should be left unpopulated.",
        "revision" : "The schema revision of the PostalAddress. This must be set to 0, which is the latest revision. All new revisions must be backward compatible with old revisions."
      },
      "placeId" : "Optional.The placeId provided by Google Places API to uniquely identify a location."
    },
    "recruiters" : [ "string" ],
    "state" : "string",
    "department" : "Optional.Name of the department which the job is under.",
    "hiringManagers" : [ "string" ]
  }
}
```

</details>

## create_registration



<details><summary>Parameters</summary>

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

### $body

**Type:** object

```json
{
  "registration" : {
    "expireTime" : "Output only.The time until which the Registration is effective. This is set by the server to 7 days after creation time.A timestamp in RFC3339 UTC \"Zulu\" format, accurate to nanoseconds. Example: \"2014-10-02T15:01:23.045123456Z\".",
    "name" : "Output only.The resource name of this Registration. This is generated by the service when a Registration is created. Registration name takes the form of \"tenants/*/registrations/*\".",
    "notificationTypes" : [ "schema_type_none" ],
    "pubsubTopic" : "The name field of a Cloud Pub/Sub Topic that notifications are to be sent to.To register for notifications, the owner of the topic must grant hire-pubsub-publisher@system.gserviceaccount.com the projects.topics.publish permission."
  }
}
```

</details>

## delete_job



<details><summary>Parameters</summary>

### name (required)

Required.The name of the job to delete.

**Type:** string

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## delete_registration



<details><summary>Parameters</summary>

### name (required)

Required. The name of the Registration to be deleted.

**Type:** string

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## get_application



<details><summary>Parameters</summary>

### name (required)

The name of the application to retrieve.

**Type:** string

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## get_candidate



<details><summary>Parameters</summary>

### name (required)

The name of the candidate to retrieve.

**Type:** string

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## get_custom_field_specs



<details><summary>Parameters</summary>

### name (required)

The name of the custom field spec to retrieve.

**Type:** string

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## get_job



<details><summary>Parameters</summary>

### name (required)

Required.The name of the job to delete.

**Type:** string

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## get_user



<details><summary>Parameters</summary>

### name (required)

The name of the application to retrieve.

**Type:** string

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

</details>

## list_applications



<details><summary>Parameters</summary>

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

### filter

Optional filter on applications fields. Attempts to query with an unrecognized filter dimension will result in an INVALID_ARGUMENT error. Supported querying are as follows:
  status.state=[Application.Status.State]
  status.update_time&gt;=[RFS 3339 formatted Timestamp]
For filtering on multiple fields, we only support AND operations. Sample Query:
  status.state=ACTIVE AND status.update_time&gt;="2018-01-02T06:23:10.843Z"

**Type:** string

</details>

## list_candidates



<details><summary>Parameters</summary>

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

### filter

Optional filter on candidate fields. Supported dimensions for querying are as follows:
  applications.status.state=[Application.Status.State]
Attempts to query with an unrecognized filter dimension will result in an INVALID_ARGUMENT error. Sample Query:
  applications.status.state=ACCEPTED

**Type:** string

</details>

## list_custom_field_specs



<details><summary>Parameters</summary>

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

### filter

Optional filter on custom field spec. Attempts to query with an unrecognized filter dimension will result in an INVALID_ARGUMENT error. Supported querying are as follows:
  objectTypes[]=[CustomFieldSpec.ObjectType]
Sample Query:
  objectTypes[]=JOB

**Type:** string

</details>

## list_jobs



<details><summary>Parameters</summary>

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

### filter

Optional.Supported dimensions for querying are as follows:
  state=[Job.State]
Attempts to query with an unrecognized filter dimension will result in an INVALID_ARGUMENT error. Sample Query:
  state=OPEN

**Type:** string

</details>

## update_job



<details><summary>Parameters</summary>

### name (required)

Required.The name of the job to delete.

**Type:** string

### tenant (required)

The name of the tenant. If there is only one tenant, the value "my_tenant" can be used.

**Type:** string

### $body

**Type:** object

```json
{
  "job" : {
    "publishState" : "string",
    "employmentType" : "string",
    "customFields" : { },
    "description" : "Optional.Description of the job.",
    "timeCommitment" : "string",
    "title" : "Required.The human readable job title.",
    "compensationInfo" : {
      "compensation_amount" : {
        "nanos" : "Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If units is positive, nanos must be positive or zero. If units is zero, nanos can be positive, zero, or negative. If units is negative, nanos must be negative or zero. For example $-1.75 is represented as units=-1 and nanos=-750,000,000.",
        "units" : "The whole units of the amount. For example if currencyCode is \"USD\", then 1 unit is one US dollar.",
        "currencyCode" : "The 3-letter currency code defined in ISO 4217."
      },
      "candidateVisible" : "Optional.Indicates if compensation information is available to candidates.",
      "frequency" : "string"
    },
    "requisitionId" : "Output only. Can be set on jobs.create.Id used to link data with external systems.",
    "createTime" : "Output only.Date the job was created or the date specified when importing this job.A timestamp in RFC3339 UTC \"Zulu\" format, accurate to nanoseconds. Example: \"2014-10-02T15:01:23.045123456Z\".",
    "creatingUser" : "Optional.Resource name of the user that created the job. It must have the format of \"tenants/*/users/*\".",
    "coordinators" : [ "string" ],
    "name" : "Output only. Required during jobs.patch.The resource name of this Job. This is generated by the service when a job is created. Job name takes the form of \"tenants/*/jobs/*\".",
    "location" : {
      "postalAddress" : {
        "regionCode" : "Required. CLDR region code of the country/region of the address. This is never inferred and it is up to the user to ensure the value is correct. See http://cldr.unicode.org/ and http://www.unicode.org/cldr/charts/30/supplemental/territory_information.html for details.",
        "sortingCode" : "Optional. Additional, country-specific, sorting code. This is not used in most regions. Where it is used, the value is either a string like \"CEDEX\", optionally followed by a number (e.g. \"CEDEX 7\"), or just a number alone, representing the \"sector code\" (Jamaica), \"delivery area indicator\" (Malawi) or \"post office indicator\" (e.g. Côte d'Ivoire).",
        "recipients" : [ "string" ],
        "postalCode" : "Optional. Postal code of the address. Not all countries use or require postal codes to be present, but where they are used, they may trigger additional validation with other parts of the address (e.g. state/zip validation in the U.S.A.).",
        "organization" : "Optional. The name of the organization at the address.",
        "locality" : "Optional. Generally refers to the city/town portion of the address. In regions of the world where localities are not well defined or do not fit into this structure well, leave locality empty and use addressLines.",
        "sublocality" : "Optional. Sublocality of the address. For example, this can be neighborhoods, boroughs, districts.",
        "addressLines" : [ "string" ],
        "languageCode" : "Optional. BCP-47 language code of the contents of this address (if known). This is often the UI language of the input form or is expected to match one of the languages used in the address' country/region, or their transliterated equivalents. This can affect formatting in certain countries, but is not critical to the correctness of the data and will never affect any validation or other non-formatting related operations. If this value is not known, it should be omitted (rather than specifying a possibly incorrect default).",
        "administrativeArea" : "Optional. Highest administrative subdivision which is used for postal addresses of a country or region. For example, this can be a state, a province, an oblast, or a prefecture. Specifically, for Spain this is the province and not the autonomous community (e.g. \"Barcelona\" and not \"Catalonia\"). Many countries don't use an administrative area in postal addresses. E.g. in Switzerland this should be left unpopulated.",
        "revision" : "The schema revision of the PostalAddress. This must be set to 0, which is the latest revision. All new revisions must be backward compatible with old revisions."
      },
      "placeId" : "Optional.The placeId provided by Google Places API to uniquely identify a location."
    },
    "recruiters" : [ "string" ],
    "state" : "string",
    "department" : "Optional.Name of the department which the job is under.",
    "hiringManagers" : [ "string" ]
  },
  "updateMask" : "Required.A field mask to specify the job fields to be updated. Only top level fields of Jobs are supported.Sample updateMask: {\"paths\": [\"job.description\", \"job.title\"]}A comma-separated list of fully qualified names of fields. Example: \"user.displayName,photo\"."
}
```

</details>

