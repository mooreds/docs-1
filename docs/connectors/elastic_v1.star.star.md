---

id: elastic_documentation

title: Elastic

version: v1.*.*

---

## add_document



<details><summary>Parameters</summary>

#### id (required)

**Type:** string

#### index (required)

**Type:** string

#### type (required)

**Type:** string

#### $body

**Type:** object

</details>

## bulk_add_documents



<details><summary>Parameters</summary>

#### $body

**Type:** string

</details>

## cat_indices



<details><summary>Parameters</summary>

#### format (required)

The format of the data, e.g. 'json', 'yaml'. The default is json.

**Type:** string

</details>

## create_index



<details><summary>Parameters</summary>

#### index (required)

**Type:** string

#### $body

**Type:** object

</details>

## delete_index



<details><summary>Parameters</summary>

#### index (required)

**Type:** string

</details>

## get_mapping



<details><summary>Parameters</summary>

#### index (required)

**Type:** string

#### type (required)

**Type:** string

</details>

## put_mapping



<details><summary>Parameters</summary>

#### index (required)

**Type:** string

#### type (required)

**Type:** string

#### $body

**Type:** object

</details>

## search



<details><summary>Parameters</summary>

#### index (required)

**Type:** string

#### type (required)

**Type:** string

#### $body

**Type:** object

#### size

**Type:** string

</details>

