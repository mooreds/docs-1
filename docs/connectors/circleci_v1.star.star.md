---

id: circleci_documentation

title: CircleCI

version: v1.*.*

---

## delete_project_build_cache

Clears the cache for a project.


<details><summary>Parameters</summary>

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## delete_project_checkout_key_by_fingerprint

Delete a checkout key.


<details><summary>Parameters</summary>

#### fingerprint (required)

XXXXXXXXXX


**Type:** string

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## delete_project_envvar_by_name

Deletes the environment variable named ':name'


<details><summary>Parameters</summary>

#### name (required)

XXXXXXXXXX


**Type:** string

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## get_me



*This operation has no parameters*

## get_project_artifacts

List the artifacts produced by a given build.


<details><summary>Parameters</summary>

#### build_num (required)

XXXXXXXXXX


**Type:** integer

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## get_project_by_build_num

Full details for a single build. The response includes all of the fields from the build summary.
This is also the payload for the [notification webhooks](/docs/configuration/#notify), in which case this object is the value to a key named 'payload'.


<details><summary>Parameters</summary>

#### build_num (required)

XXXXXXXXXX


**Type:** integer

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## get_project_by_project

Build summary for each of the last 30 builds for a single git repo.


<details><summary>Parameters</summary>

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

#### filter

Restricts which builds are returned.
Set to "completed", "successful", "failed", "running", or defaults to no filter.


**Type:** string

**Potential values:** completed, successful, failed, running

#### limit

The number of builds to return. Maximum 100, defaults to 30.


**Type:** integer

#### offset

The API returns builds starting from this offset, defaults to 0.


**Type:** integer

</details>

## get_project_checkout_key

Lists checkout keys.


<details><summary>Parameters</summary>

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## get_project_checkout_key_by_fingerprint

Get a checkout key.


<details><summary>Parameters</summary>

#### fingerprint (required)

XXXXXXXXXX


**Type:** string

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## get_project_envvar

Lists the environment variables for :project


<details><summary>Parameters</summary>

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## get_project_envvar_by_name

Gets the hidden value of environment variable :name


<details><summary>Parameters</summary>

#### name (required)

XXXXXXXXXX


**Type:** string

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## get_project_tests

Provides test metadata for a build
Note: [Learn how to set up your builds to collect test metadata](https://circleci.com/docs/test-metadata/)


<details><summary>Parameters</summary>

#### build_num (required)

XXXXXXXXXX


**Type:** integer

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## get_projects



*This operation has no parameters*

## get_recent_builds

Build summary for each of the last 30 recent builds, ordered by build_num.


*This operation has no parameters*

## post_project_by_project

Triggers a new build, returns a summary of the build.


<details><summary>Parameters</summary>

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

#### $body

**Type:** object

</details>

## post_project_cancel

Cancels the build, returns a summary of the build.


<details><summary>Parameters</summary>

#### build_num (required)

XXXXXXXXXX


**Type:** integer

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## post_project_checkout_key

Creates a new checkout key.
Only usable with a user API token.


<details><summary>Parameters</summary>

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

#### $body

The type of key to create. Can be 'deploy-key' or 'github-user-key'.


**Type:** string

**Potential values:** deploy-key, github-user-key

</details>

## post_project_envvar

Creates a new environment variable


<details><summary>Parameters</summary>

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## post_project_retry

Retries the build, returns a summary of the new build.


<details><summary>Parameters</summary>

#### build_num (required)

XXXXXXXXXX


**Type:** integer

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

</details>

## post_project_ssh_key

Create an ssh key used to access external systems that require SSH key-based authentication


<details><summary>Parameters</summary>

#### Content-Type (required)

**Type:** string

**Potential values:** application/json

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

#### $body

**Type:** object

</details>

## post_project_tree_by_branch

Triggers a new build, returns a summary of the build.
Optional build parameters can be set using an experimental API.

Note: For more about build parameters, read about [using parameterized builds](https://circleci.com/docs/parameterized-builds/)


<details><summary>Parameters</summary>

#### branch (required)

The branch name should be url-encoded.


**Type:** string

#### project (required)

XXXXXXXXX


**Type:** string

#### username (required)

XXXXXXXXX


**Type:** string

#### $body

**Type:** object

</details>

## post_user_heroku_key



*This operation has no parameters*

