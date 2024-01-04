Feature: To-Do List Manager

  Suggested Features:
    • Add a task to the to-do list.
    • List all tasks in the to-do list.
    • Mark a task as completed.
    • Clear the entire to-do list.

  Background:
    Given the to-do list is empty

  Scenario: Add a task to the to-do list
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

 Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task       |
      | Buy groceries |
      | Pay bills    |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries
      - Pay bills
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task       | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task       |
      | Buy groceries |
      | Pay bills    |
    When the user clears the to-do list
    Then the to-do list should be empty

Scenario: Mark a non-existent task as completed
    Given the to-do list contains tasks:
      | Task       | Status  |
      | Buy groceries | Pending |
    When the user attempts to mark a task "Go to the gym" as completed
    Then the to-do list should remain unchanged