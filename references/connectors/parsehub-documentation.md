---
id: parsehub-documentation
title: Parsehub (version v1.*.*)
sidebar_label: Parsehub
layout: docs.mustache
---

## cancel_run

This cancels a run and changes its status to cancelled. Any data that was extracted so far will be available.

<details><summary>Parameters</summary>

### run_token (required)

**Type:** string

</details>

## delete_run

This cancels a run if running, and deletes the run and its data.

<details><summary>Parameters</summary>

### run_token (required)

**Type:** string

</details>

## get_data_for_run

This returns the data that was extracted by a run.

<details><summary>Parameters</summary>

### run_token (required)

**Type:** string

### format

The format that you would like to get the data in.

**Type:** string

**Potential values:** csv, json

</details>

## get_last_ready_data

This returns the data for the most recent ready run for a project. You can use this method in order to have a synchronous interface to your project.

<details><summary>Parameters</summary>

### project_token (required)

**Type:** string

### format

The format that you would like to get the data in.

**Type:** string

**Potential values:** csv, json

</details>

## get_project

This will return the project object for a specific project.

<details><summary>Parameters</summary>

### project_token (required)

**Type:** string

### include_options

Includes the "options_json" key in the result returned. For performance reasons, we exclude this key by default.

**Type:** boolean

### offset

**Type:** integer

</details>

## get_run

This returns the run object for a given run token.

<details><summary>Parameters</summary>

### run_token (required)

**Type:** string

</details>

## list_projects

Gets a list of projects in your account.

<details><summary>Parameters</summary>

### include_options

Includes the "options_json" key in the result returned. For performance reasons, we exclude this key by default.

**Type:** boolean

### limit

Specifies how many entries will be returned in projects. Accepts values between 1 and 20 inclusively. Defaults to 20.

**Type:** integer

### offset

**Type:** integer

</details>

## run_project

Start running an instance of the project on the ParseHub cloud. It will create a new run object.

<details><summary>Parameters</summary>

### project_token (required)

**Type:** string

### send_email

If set to anything other than 0, send an email when the run either completes successfully or fails due to an error. Defaults to 0.

**Type:** integer

### start_template

The template to start running with. Defaults to the projects’s start_template (inside the options_json).

**Type:** string

### start_url

The url to start running on. Defaults to the project’s start_site.

**Type:** string

### start_value_override

The starting global scope for this run. This can be used to pass parameters to your run. For example, you can pass {"query": "San Francisco"} to use the query somewhere in your run. Defaults to the project’s start_value.

**Type:** string

</details>

