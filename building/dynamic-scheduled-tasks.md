---
id: dynamic-scheduled-tasks
title: Dynamic Scheduled Tasks
layout: docs.mustache
tags: doc
---

You can dynamically schedule an operation to run using a Dynamic Task. These tasks are managed exclusively through JavaScript operations.

## Create a dynamic task

Create a task that runs once at a specified ISO-8601 time string:
```javascript
var moment = require('moment-timezone-with-data.js');
var inFiveMinutes = moment().add(5, "minutes").format();

task.create("this.helloworld")
    .setName("Hello World")            // Note: setName() is optional.
    .runOnce(inFiveMinutes);
```

Create a task that runs an operation in the increment specified:
```javascript
task.create("this.helloworld").runEvery(5, "minutes");
```

Create a task that runs with a cron expression:
```javascript
task.create("this.helloworld").runEvery("0 0/5 0 ? * * *");
```

`task.create()` can also accept operation parameters, similar to [`api.run()`](/docs/references/js-operations/#run). Unlike `api.run()`, it does not accept any options. Currently, the operation specified must be one in your application, i.e you cannot directly invoke a dependency's operation from a dynamic task.

### Creating a task for a specific user

Tasks created while running with the `asUser` option, or tasks created directly by the user through the SDK, will run only with that user's credentials.

The following operations will create a task to return calendar events for user `abcd1234` every hour:

```javascript
// Entry operation:
(params) => {
  return api.run("this.create_task", {}, {asUser: "abcd1234"});
}

// Operation create_task:
(params) => {
  return task.create("this.get_calendar_events").runEvery(1, "hour");
}

// Operation get_calendar_events
(params) => {
  return api.run("google_calendar.get_calendar_events", {calendarId: "primary"});
}
```

### Creating a task for all your users

The following operations will create a task to return calendar events for all of your users every hour:
```javascript
// Entry operation:
(params) => {
  return task.create("this.get_calendar_events_for_everyone").runEvery(1, "hour");
}

// Operation get_calendar_events_for_everyone:
(params) => {
  return api.runForAllUsers("google_calendar.get_calendar_events", {calendarId: "primary"})
}
```

## View your created dynamic tasks

```javascript
task.listTasks();
```

Run `task.listTasks()` to view the dynamic tasks you've created. Note that this will only show you the tasks created in your current context. For example: if you are running the function in your development environment, you will only see tasks you've created in the development context. Likewise, if you create a task while running with the `asUser` option, you can only view that task while running with the same `asUser` option.

`task.listTasks()` will return `runEvery` dynamic tasks, as well as `runOnce` tasks that have not yet executed.

## Delete a dynamic task
```javascript
var uuid = task.create("this.helloworld").runEvery(5, "minutes");
task.delete(uuid);
```

You can delete all tasks (in your current context) by running the following:
```javascript
(params) => {
  task.listTasks().forEach(thisTask => task.delete(thisTask.uuid));
}
```