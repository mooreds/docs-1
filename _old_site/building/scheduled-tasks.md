# Scheduled tasks

In Transposit, you can schedule an operation to run once or periodically.

1. Navigate to **Deploy &gt; Scheduled Tasks** and create a new task.
2. Specify a memorable task name.
3. Select an operation for the task to run.
4. Specify a cron schedule.
5. If necessary, specify parameters to provide your operation when it is run.
6. Save your task.

Cron is a time-based job scheduler typically found on Unix systems. Transposit interprets cron syntax to determine when a task should run.

Note that the specifics of cron syntax vary between implementations. Third-party online tools might help you craft cron schedules, but Transposit's cron schedule widget is authoritative about how a schedule will be interpreted. As you type a cron schedule, Transposit's cron schedule widget will check the schedule for validity and list what the next upcoming runs would be if the schedule was saved.

{% hint style="info" %}
All Transposit cron schedules are interpreted in the UTC timezone.
{% endhint %}

Some sample schedules:

| Syntax | Schedule |
| :--- | :--- |
| `0 0 3 * * ?` | Run every day at 3:00AM UTC |
| `0 0 0 ? * FRI` | Run every Friday at 12:00AM UTC |
| `0 30 16 1 * ?` | Run on the first of the month at 4:30PM UTC |

Once your task has been saved, upcoming runs will execute at their scheduled time.

Your scheduled task runs against the latest version of your service. If you remove an operaton referenced by a task, it will cause your task to fail when it executes.

## Provide keys for tasks

You should provide keys for all data connections before a task executes. Each task references its own set of keys.

## Testing tasks

Click **Run now & show log** to test your task.

A scheduled task can be run manually \(outside the context of its schedule\). You can use this to test the task with the keys and parameters you've provided.

## Editing, disabling, or deleting tasks

A task can be edited and saved at any time. Changes to a task will affect all upcoming runs.

A task can be disabled at any time. A disabled task will never execute until it is scheduled again.

A task can be deleted at any time. A deleted task will never execute again and cannot be restored.

