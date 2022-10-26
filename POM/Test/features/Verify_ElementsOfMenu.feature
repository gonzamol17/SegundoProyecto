Feature: Verify Elements from the menu
  As a client,
  I want to know how many items the menu has,
  and show them all.

@Regression
  Scenario: Check the number of menu items and display them
    Given I am on the Automation test store page login
    When I am on the My Account page, i verify the number of Items that exist in the menu
    Then I return the number of items/columns, and each of the menu items.