Feature: Create a User on Automation Test Store
  As a potential client,
  I want to be able see alerts on the page, when i try to create a new user without the mandatory fields,
  so that the page informs me which are the mandatory fields.

@Regression
  Scenario: Failure to create a new user, not loading the mandatory fields
    Given I am on the Automation test store page and I select the option to create a new account
    When I do not fill in any mandatory fields, and I confirm that data
    Then I can't create a new account and I can't login to the page and i can see all the red alerts