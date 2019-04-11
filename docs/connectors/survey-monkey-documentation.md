---
id: survey-monkey-documentation
title: Survey Monkey (version v1.*.*)
sidebar_label: Survey Monkey
---

Survey Monkey Integration

## delete_survey_by_id

Deletes a survey. Public App users need access to the Create/Modify Surveys scope

<details><summary>Parameters</summary>

#### surveyId (required)

id of the survey you are referring to

**Type:** string

</details>

## get_collectors_responses

Returns a list of responses. Public App users need access to the View Responses scope

<details><summary>Parameters</summary>

#### collectorId (required)

id of the survey you are referring to

**Type:** string

#### surveyId (required)

id of the survey you are referring to

**Type:** string

#### custom

The custom value associated with the response

**Type:** string

#### email

Email of the recipient

**Type:** string

#### end_created_at

Responses started before this date

**Type:** string

#### end_modified_at

Surveys must be last modified before this date.

**Type:** string

#### first_name

First Name of the recipient

**Type:** string

#### ip

The IP the response was taken from

**Type:** string

#### last_name

Last Name of the recipient

**Type:** string

#### sort_by

Field used to sort returned survey list title, date_modified, or num_responses

**Type:** string

#### sort_order

ASC or DESC

**Type:** string

#### start_created_at

Responses started after this date

**Type:** string

#### start_modified_at

Surveys must be last modified after this date.

**Type:** string

#### status

completed, partial, overquota, disqualified

**Type:** string

#### total_time_max

The maximum amount of time spent on the response

**Type:** string

#### total_time_min

The minimum amount of time spent on the response

**Type:** string

#### total_time_units

Unit of time for total_time_min and total_time_max second, minute, hour

**Type:** string

</details>

## get_page_details

Returns a page’s details. Public App users need access to the View Surveys scope

<details><summary>Parameters</summary>

#### surveyId (required)

id of the survey you are referring to

**Type:** string

</details>

## get_question_by_id

Returns a question. Requires View Surveys scope

<details><summary>Parameters</summary>

#### pageId (required)

id of the page of the survey you are referring to

**Type:** string

#### questionId (required)

id of the survey question

**Type:** string

#### surveyId (required)

id of the survey you are referring to

**Type:** string

</details>

## get_questions_on_survey_page

Returns a list of questions on a survey page. Public App users need access to the View Surveys scope

<details><summary>Parameters</summary>

#### pageId (required)

id of the page of the survey you are referring to

**Type:** string

#### surveyId (required)

id of the survey you are referring to

**Type:** string

</details>

## get_response_details

Retrieve a full expanded response, including answers to all questions. Public App users need access to the View Response Details scope

<details><summary>Parameters</summary>

#### responseId (required)

response identified by ID

**Type:** string

#### surveyId (required)

id of the survey you are referring to

**Type:** string

#### page_ids

List of survey pages to filter on. Returns all pages if not provided. Comma Separated

**Type:** string

#### question_ids

List of survey questions to filter on. Returns all questions if not provided. Comma Separated

**Type:** string

</details>

## get_responses_in_bulk



<details><summary>Parameters</summary>

#### surveyId (required)

id of the survey you are referring to

**Type:** string

#### email

Email of the recipient

**Type:** string

#### end_created_at

Responses started before this date

**Type:** string

#### end_modified_at

Surveys must be last modified before this date.

**Type:** string

#### first_name

First Name of the recipient

**Type:** string

#### ip

The IP the response was taken from

**Type:** string

#### last_name

Last Name of the recipient

**Type:** string

#### page_ids

List of survey pages to filter on. Returns all pages if not provided

**Type:** string

#### question_ids

List of survey questions to filter on. Returns all questions if not provided

**Type:** string

#### sort_by

Field used to sort returned survey list title, date_modified, or num_responses

**Type:** string

#### sort_order

ASC or DESC

**Type:** string

#### start_created_at

Responses started after this date

**Type:** string

#### start_modified_at

Surveys must be last modified after this date.

**Type:** string

#### status

completed, partial, overquota, disqualified

**Type:** string

#### total_time_max

The maximum amount of time spent on the response

**Type:** string

#### total_time_min

The minimum amount of time spent on the response

**Type:** string

#### total_time_units

second, minute, or hour

**Type:** string

</details>

## get_survey_by_id

Returns a survey’s details. To get an expanded version showing all pages and questions use /surveys/{survey_id}/details. Requires View Surveys scope

<details><summary>Parameters</summary>

#### surveyId (required)

id of the survey you are referring to

**Type:** string

</details>

## get_survey_details

Returns an expanded survey resource with a pages element containing a list of all page objects, each containing a list of questions objects. Public App users need access to the View Surveys scope

<details><summary>Parameters</summary>

#### surveyId (required)

id of the survey you are referring to

**Type:** string

</details>

## get_surveys

Returns a list of surveys owned or shared with the authenticated user. Public App users need access to the View Surveys scope

<details><summary>Parameters</summary>

#### end_modified_at

Surveys must be last modified before this date.

**Type:** string

#### folder_id

Specify the id of a folder to only return surveys in it.

**Type:** string

#### include

shared_with, shared_by, or owned (useful for teams) or use to specify additional fields to return per survey response_count, date_created, date_modified, language, question_count, analyze_url, preview

**Type:** string

#### sort_by

Field used to sort returned survey list title, date_modified, or num_responses

**Type:** string

#### sort_order

ASC or DESC

**Type:** string

#### start_modified_at

Surveys must be last modified after this date.

**Type:** string

#### title

Search survey list by survey title

**Type:** string

</details>

