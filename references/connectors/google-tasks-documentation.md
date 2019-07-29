---
id: google-tasks-documentation
title: Google Tasks (version v1.*.*)
sidebar_label: Google Tasks
layout: docs.mustache
---

## clear_all_completed_tasks

Clears all completed tasks from the specified task list. The affected tasks will be marked as 'hidden' and no longer be returned by default when retrieving all tasks for a task list.

<details><summary>Parameters</summary>

### tasklist (required)

Task list identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_list

Creates a new task list and adds it to the authenticated user's task lists.

<details><summary>Parameters</summary>

### $body

**Type:** object

```json
{
  "kind" : "Type of the resource. This is always \"tasks#taskList\".",
  "etag" : "ETag of the resource.",
  "id" : "Task list identifier.",
  "title" : "Title of the task list.",
  "updated" : "Last modification time of the task list (as a RFC 3339 timestamp).",
  "selfLink" : "URL pointing to this task list. Used to retrieve, update, or delete this task list."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## create_task

Creates a new task on the specified task list.

<details><summary>Parameters</summary>

### tasklist (required)

Task list identifier.

**Type:** string

### $body

**Type:** object

```json
{
  "parent" : "Parent task identifier. This field is omitted if it is a top-level task. This field is read-only. Use the \"move\" method to move the task under a different parent or to the top level.",
  "notes" : "Notes describing the task. Optional.",
  "hidden" : "Flag indicating whether the task is hidden. This is the case if the task had been marked completed when the task list was last cleared. The default is False. This field is read-only.",
  "kind" : "Type of the resource. This is always \"tasks#task\".",
  "completed" : "Completion date of the task (as a RFC 3339 timestamp). This field is omitted if the task has not been completed.",
  "title" : "Title of the task.",
  "selfLink" : "URL pointing to this task. Used to retrieve, update, or delete this task.",
  "deleted" : "Flag indicating whether the task has been deleted. The default if False.",
  "due" : "Due date of the task (as a RFC 3339 timestamp). Optional.",
  "etag" : "ETag of the resource.",
  "links" : [ {
    "link" : "The URL.",
    "description" : "The description. In HTML speak: Everything between  and .",
    "type" : "Type of the link, e.g. \"email\"."
  } ],
  "id" : "Task identifier.",
  "position" : "String indicating the position of the task among its sibling tasks under the same parent task or at the top level. If this string is greater than another task's corresponding position string according to lexicographical ordering, the task is positioned after the other task under the same parent task (or at the top level). This field is read-only. Use the \"move\" method to move the task to another position.",
  "updated" : "Last modification time of the task (as a RFC 3339 timestamp).",
  "status" : "Status of the task. This is either \"needsAction\" or \"completed\"."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### parent

Parent task identifier. If the task is created at the top level, this parameter is omitted. Optional.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### previous

Previous sibling task identifier. If the task is created at the first position among its siblings, this parameter is omitted. Optional.

**Type:** string

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_list

Deletes the authenticated user's specified task list.

<details><summary>Parameters</summary>

### tasklist (required)

Task list identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## delete_task

Deletes the specified task from the task list.

<details><summary>Parameters</summary>

### task (required)

Task identifier.

**Type:** string

### tasklist (required)

Task list identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_list

Returns the authenticated user's specified task list.

<details><summary>Parameters</summary>

### tasklist (required)

Task list identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## get_task

Returns the specified task.

<details><summary>Parameters</summary>

### task (required)

Task identifier.

**Type:** string

### tasklist (required)

Task list identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_lists

Returns all the authenticated user's task lists.

<details><summary>Parameters</summary>

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## list_tasks

Returns all tasks in the specified task list.

<details><summary>Parameters</summary>

### tasklist (required)

Task list identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### completedMax

Upper bound for a task's completion date (as a RFC 3339 timestamp) to filter by. Optional. The default is not to filter by completion date.

**Type:** string

### completedMin

Lower bound for a task's completion date (as a RFC 3339 timestamp) to filter by. Optional. The default is not to filter by completion date.

**Type:** string

### dueMax

Upper bound for a task's due date (as a RFC 3339 timestamp) to filter by. Optional. The default is not to filter by due date.

**Type:** string

### dueMin

Lower bound for a task's due date (as a RFC 3339 timestamp) to filter by. Optional. The default is not to filter by due date.

**Type:** string

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

### showCompleted

Flag indicating whether completed tasks are returned in the result. Optional. The default is True.

**Type:** boolean

### showDeleted

Flag indicating whether deleted tasks are returned in the result. Optional. The default is False.

**Type:** boolean

### showHidden

Flag indicating whether hidden tasks are returned in the result. Optional. The default is False.

**Type:** boolean

### updatedMin

Lower bound for a task's last modification time (as a RFC 3339 timestamp) to filter by. Optional. The default is not to filter by last modification time.

**Type:** string

</details>

## move_task

Moves the specified task to another position in the task list. This can include putting it as a child task under a new parent and/or move it to a different position among its sibling tasks.

<details><summary>Parameters</summary>

### task (required)

Task identifier.

**Type:** string

### tasklist (required)

Task list identifier.

**Type:** string

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### parent

New parent task identifier. If the task is moved to the top level, this parameter is omitted. Optional.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### previous

New previous sibling task identifier. If the task is moved to the first position among its siblings, this parameter is omitted. Optional.

**Type:** string

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_list

Updates the authenticated user's specified task list. This method supports patch semantics.

<details><summary>Parameters</summary>

### tasklist (required)

Task list identifier.

**Type:** string

### $body

**Type:** object

```json
{
  "kind" : "Type of the resource. This is always \"tasks#taskList\".",
  "etag" : "ETag of the resource.",
  "id" : "Task list identifier.",
  "title" : "Title of the task list.",
  "updated" : "Last modification time of the task list (as a RFC 3339 timestamp).",
  "selfLink" : "URL pointing to this task list. Used to retrieve, update, or delete this task list."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## patch_task

Updates the specified task. This method supports patch semantics.

<details><summary>Parameters</summary>

### task (required)

Task identifier.

**Type:** string

### tasklist (required)

Task list identifier.

**Type:** string

### $body

**Type:** object

```json
{
  "parent" : "Parent task identifier. This field is omitted if it is a top-level task. This field is read-only. Use the \"move\" method to move the task under a different parent or to the top level.",
  "notes" : "Notes describing the task. Optional.",
  "hidden" : "Flag indicating whether the task is hidden. This is the case if the task had been marked completed when the task list was last cleared. The default is False. This field is read-only.",
  "kind" : "Type of the resource. This is always \"tasks#task\".",
  "completed" : "Completion date of the task (as a RFC 3339 timestamp). This field is omitted if the task has not been completed.",
  "title" : "Title of the task.",
  "selfLink" : "URL pointing to this task. Used to retrieve, update, or delete this task.",
  "deleted" : "Flag indicating whether the task has been deleted. The default if False.",
  "due" : "Due date of the task (as a RFC 3339 timestamp). Optional.",
  "etag" : "ETag of the resource.",
  "links" : [ {
    "link" : "The URL.",
    "description" : "The description. In HTML speak: Everything between  and .",
    "type" : "Type of the link, e.g. \"email\"."
  } ],
  "id" : "Task identifier.",
  "position" : "String indicating the position of the task among its sibling tasks under the same parent task or at the top level. If this string is greater than another task's corresponding position string according to lexicographical ordering, the task is positioned after the other task under the same parent task (or at the top level). This field is read-only. Use the \"move\" method to move the task to another position.",
  "updated" : "Last modification time of the task (as a RFC 3339 timestamp).",
  "status" : "Status of the task. This is either \"needsAction\" or \"completed\"."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_list

Updates the authenticated user's specified task list.

<details><summary>Parameters</summary>

### tasklist (required)

Task list identifier.

**Type:** string

### $body

**Type:** object

```json
{
  "kind" : "Type of the resource. This is always \"tasks#taskList\".",
  "etag" : "ETag of the resource.",
  "id" : "Task list identifier.",
  "title" : "Title of the task list.",
  "updated" : "Last modification time of the task list (as a RFC 3339 timestamp).",
  "selfLink" : "URL pointing to this task list. Used to retrieve, update, or delete this task list."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

## update_task

Updates the specified task.

<details><summary>Parameters</summary>

### task (required)

Task identifier.

**Type:** string

### tasklist (required)

Task list identifier.

**Type:** string

### $body

**Type:** object

```json
{
  "parent" : "Parent task identifier. This field is omitted if it is a top-level task. This field is read-only. Use the \"move\" method to move the task under a different parent or to the top level.",
  "notes" : "Notes describing the task. Optional.",
  "hidden" : "Flag indicating whether the task is hidden. This is the case if the task had been marked completed when the task list was last cleared. The default is False. This field is read-only.",
  "kind" : "Type of the resource. This is always \"tasks#task\".",
  "completed" : "Completion date of the task (as a RFC 3339 timestamp). This field is omitted if the task has not been completed.",
  "title" : "Title of the task.",
  "selfLink" : "URL pointing to this task. Used to retrieve, update, or delete this task.",
  "deleted" : "Flag indicating whether the task has been deleted. The default if False.",
  "due" : "Due date of the task (as a RFC 3339 timestamp). Optional.",
  "etag" : "ETag of the resource.",
  "links" : [ {
    "link" : "The URL.",
    "description" : "The description. In HTML speak: Everything between  and .",
    "type" : "Type of the link, e.g. \"email\"."
  } ],
  "id" : "Task identifier.",
  "position" : "String indicating the position of the task among its sibling tasks under the same parent task or at the top level. If this string is greater than another task's corresponding position string according to lexicographical ordering, the task is positioned after the other task under the same parent task (or at the top level). This field is read-only. Use the \"move\" method to move the task to another position.",
  "updated" : "Last modification time of the task (as a RFC 3339 timestamp).",
  "status" : "Status of the task. This is either \"needsAction\" or \"completed\"."
}
```

### alt

Data format for the response.

**Type:** string

**Potential values:** json

### fields

Selector specifying which fields to include in a partial response.

**Type:** string

### prettyPrint

Returns response with indentations and line breaks.

**Type:** boolean

### quotaUser

An opaque string that represents a user for quota purposes. Must not exceed 40 characters.

**Type:** string

</details>

