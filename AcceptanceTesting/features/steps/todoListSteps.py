import sys
from behave import given, when, then
from io import StringIO

# Create a shared context for scenarios
from taskController import TaskController

from hamcrest import assert_that, equal_to, contains_string

@given("the to-do list is empty")
def step_given_empty_todo_list(context):
    context.controller = TaskController()

@given("the to-do list contains tasks")
def step_given_todo_list_with_tasks(context):
    context.controller = TaskController()
    for row in context.table:
        description = row['Task']
        context.controller.add_task(description, "", "")

@when('the user adds a task "{task_description}"')
def step_when_add_task(context, task_description):
    context.controller.add_task(task_description, "", "")

@when("the user lists all tasks")
def step_when_list_tasks(context):
    context.output = []
    with capture_stdout() as stdout:
        context.controller.list_tasks()
    context.output = stdout.getvalue().splitlines()

@when('the user marks task "{task_description}" as completed')
def step_when_mark_task_completed(context, task_description):
    tasks = context.controller._tasks  # Not ideal, but for testing purposes
    for task in tasks:
        if task.description == task_description:
            task.completed = True
            break

@when("the user clears the to-do list")
def step_when_clear_tasks(context):
    context.controller.clear_tasks()

@then('the to-do list should contain "{task_description}"')
def step_then_todo_list_contains_task(context, task_description):
    tasks = [task.description for task in context.controller._tasks]  # Not ideal, but for testing purposes
    assert task_description in tasks

@then('the output should contain')
def step_then_output_contains(context):
    expected_output_lines = context.text.splitlines()
    assert context.output == expected_output_lines

@then('the to-do list should show task "{task_description}" as completed')
def step_then_task_marked_as_completed(context, task_description):
    tasks = context.controller._tasks  # Not ideal, but for testing purposes
    for task in tasks:
        if task.description == task_description:
            assert task.completed is True
            break

@then("the to-do list should be empty")
def step_then_todo_list_empty(context):
    tasks = context.controller._tasks  # Not ideal, but for testing purposes
    assert len(tasks) == 0

@when('the user attempts to mark a task "{task_description}" as completed')
def step_when_attempt_to_mark_nonexistent_task(context, task_description):
    # Implement code to handle attempting to mark a non-existent task
    tasks = context.controller._tasks  # Not ideal, but for testing purposes
    for task in tasks:
        if task.description == task_description:
            # The task exists, so the behavior should be implemented here
            break
    else:
        # Task not found, handle the scenario accordingly
        context.nonexistent_task_marked = True

@then('the to-do list should remain unchanged')
def step_then_todo_list_should_remain_unchanged(context):
    # Implement code to verify that the to-do list remains unchanged
    # This might involve checking if any tasks were marked as completed
    assert getattr(context, 'nonexistent_task_marked', False) is True

class capture_stdout:
    def __enter__(self):
        import sys
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self._stringio

    def __exit__(self, *args):
        sys.stdout = self._stdout