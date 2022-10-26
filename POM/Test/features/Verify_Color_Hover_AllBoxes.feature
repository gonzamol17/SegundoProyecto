Feature: Check the color of each box in My Account, when hovering it
 As a logged in user, i want to be able to hover over each box,
 and verify that it is displayed with the correct color

@Regression
  Scenario: Verify the color of each box in My Account, when hovering it
    Given I am logged on the Automation page store
    When I am in my account and I hover over each of the boxes
    Then I verify that each box is set in the correct color