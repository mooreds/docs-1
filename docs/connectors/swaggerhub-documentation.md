---
id: swaggerhub-documentation
title: Swaggerhub (version v2.*.*)
sidebar_label: Swaggerhub
---

## delete_api



<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

</details>

## delete_collaboration



<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

</details>

## delete_domain



<details><summary>Parameters</summary>

#### domain (required)

Domain name (case-sensitive)

**Type:** string

#### owner (required)

Domain owner (user or organization, case-sensitive)

**Type:** string

#### force

Force update

**Type:** boolean

</details>

## delete_version_for_api



<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Version identifier (case-sensitive)

**Type:** string

</details>

## delete_version_for_domain



<details><summary>Parameters</summary>

#### domain (required)

Domain name (case-sensitive)

**Type:** string

#### owner (required)

Domain owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Version identifier (case-sensitive)

**Type:** string

#### force

Force update

**Type:** boolean

</details>

## get_collaboration



<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

#### expandTeams

**Type:** boolean

</details>

## get_comments_for_api

Returns all the comments and replies added by collaborators in the specified API version.


<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Version identifier (case-sensitive)

**Type:** string

</details>

## get_comments_for_domain

Returns all the comments and replies added by collaborators in the specified domain version.


<details><summary>Parameters</summary>

#### domain (required)

Domain name (case-sensitive)

**Type:** string

#### owner (required)

Domain owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Version identifier (case-sensitive)

**Type:** string

</details>

## get_definition



<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Version identifier (case-sensitive)

**Type:** string

</details>

## get_definition_for_domain



<details><summary>Parameters</summary>

#### domain (required)

Domain name (case-sensitive)

**Type:** string

#### owner (required)

Domain owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Version identifier (case-sensitive)

**Type:** string

</details>

## get_json_definition



<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Version identifier (case-sensitive)

**Type:** string

</details>

## get_json_for_domain



<details><summary>Parameters</summary>

#### domain (required)

Domain name (case-sensitive)

**Type:** string

#### owner (required)

Domain owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Version identifier (case-sensitive)

**Type:** string

</details>

## get_yaml_definition



<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Version identifier (case-sensitive)

**Type:** string

</details>

## get_yaml_for_domain



<details><summary>Parameters</summary>

#### domain (required)

Domain name (case-sensitive)

**Type:** string

#### owner (required)

Domain owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Version identifier (case-sensitive)

**Type:** string

</details>

## list_apis_for_owner



<details><summary>Parameters</summary>

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

#### limit

Number of results per page

**Type:** integer

#### order

Sort order

**Type:** string

**Potential values:** ASC, DESC

#### page

Page to return

**Type:** integer

#### sort

Sort criteria or result set:
* NAME
* UPATED
* CREATED
* OWNER


**Type:** string

**Potential values:** NAME, UPDATED, CREATED, OWNER

</details>

## list_domains_for_owner



<details><summary>Parameters</summary>

#### owner (required)

Domain owner (user or organization, case-sensitive)

**Type:** string

#### limit

Number of results per page

**Type:** integer

#### order

Sort order

**Type:** string

**Potential values:** ASC, DESC

#### page

Page to return

**Type:** integer

#### sort

Sort criteria or result set:
* NAME
* UPATED
* CREATED
* OWNER


**Type:** string

**Potential values:** NAME, UPDATED, CREATED, OWNER

</details>

## list_versions_for_api



<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

</details>

## list_versions_for_domain



<details><summary>Parameters</summary>

#### domain (required)

Domain name (case-sensitive)

**Type:** string

#### owner (required)

Domain owner (user or organization, case-sensitive)

**Type:** string

</details>

## save_definition

Saves the provided Swagger definition; the owner must match the token owner. The version will be extracted from the Swagger definition itself.

<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

#### $body

The Swagger definition of this API

**Type:** string

#### force

Force update

**Type:** boolean

#### isPrivate

Defines whether the API has to be private

**Type:** boolean

#### version

API version

**Type:** string

</details>

## save_definition_for_domain



<details><summary>Parameters</summary>

#### domain (required)

Domain name (case-sensitive)

**Type:** string

#### owner (required)

Domain owner (user or organization, case-sensitive)

**Type:** string

#### version (required)

Domain version

**Type:** string

#### $body

The Swagger definition of this domain

**Type:** string

#### force

Force update

**Type:** boolean

#### isPrivate

Specifies whether the domain has to be private

**Type:** boolean

</details>

## search_apis



<details><summary>Parameters</summary>

#### limit

Number of results per page

**Type:** integer

#### order

Sort order

**Type:** string

**Potential values:** ASC, DESC

#### page

Page to return

**Type:** integer

#### query

Free text query to match

**Type:** string

#### sort

Sort criteria or result set:
* NAME
* UPATED
* CREATED
* OWNER


**Type:** string

**Potential values:** NAME, UPDATED, CREATED, OWNER

#### state

Matches against published state of the spec:
* UNPUBLISHED - spec is a draft, a work in progress
* PUBLISHED - spec is a stable version ready for consuming from client applications
* ANY - either PUBLISHED or UNPUBLISHED


**Type:** string

**Potential values:** ALL, PUBLISHED, UNPUBLISHED

#### tag

Matches against tags associated with an API

**Type:** array

</details>

## search_apis_and_domains



<details><summary>Parameters</summary>

#### limit

Number of results per page

**Type:** integer

#### order

Sort order

**Type:** string

**Potential values:** ASC, DESC

#### owner

API or Domain owner identifier. Can be username or organization name

**Type:** string

#### page

Page to return

**Type:** integer

#### query

Free text query to match

**Type:** string

#### sort

Sort criteria or result set:
* NAME
* UPATED
* CREATED
* OWNER


**Type:** string

**Potential values:** NAME, UPDATED, CREATED, OWNER

#### specType

Type of Swagger specs to search:
* API - APIs only
* DOMAIN - Domains only
* ANY - Both APIs and Domains


**Type:** string

**Potential values:** API, DOMAIN, ANY

#### state

Matches against published state of the spec:
* UNPUBLISHED - spec is a draft, a work in progress
* PUBLISHED - spec is a stable version ready for consuming from client applications
* ANY - either PUBLISHED or UNPUBLISHED


**Type:** string

**Potential values:** ALL, PUBLISHED, UNPUBLISHED

#### visibility

The visibility of a spec in SwaggerHub:
* PUBLIC - can be viewed by anyone
* PRIVATE - can only be viewed by you or your Org and those that you are collaborating with or have shared it with
* ANY - either PUBLIC or PRIVATE


**Type:** string

**Potential values:** PUBLIC, PRIVATE, ANY

</details>

## search_domains



<details><summary>Parameters</summary>

#### limit

Number of results per page

**Type:** integer

#### order

Sort order

**Type:** string

**Potential values:** ASC, DESC

#### page

Page to return

**Type:** integer

#### query

Free text query to match

**Type:** string

#### sort

Sort criteria or result set:
* NAME
* UPATED
* CREATED
* OWNER


**Type:** string

**Potential values:** NAME, UPDATED, CREATED, OWNER

#### state

Matches against published state of the spec:
* UNPUBLISHED - spec is a draft, a work in progress
* PUBLISHED - spec is a stable version ready for consuming from client applications
* ANY - either PUBLISHED or UNPUBLISHED


**Type:** string

**Potential values:** ALL, PUBLISHED, UNPUBLISHED

#### tag

Matches against tags associated with a domain

**Type:** array

</details>

## update_collaboration



<details><summary>Parameters</summary>

#### api (required)

API name (case-sensitive)

**Type:** string

#### owner (required)

API owner (user or organization, case-sensitive)

**Type:** string

#### $body

**Type:** object

</details>

