Feature: Create a User on Automation Test Store
  As a potential client,
  I want the page to be able that when trying to create an existing user,
  it informs me that this user already exists on the system.

@Regression
  Scenario: Create an new account for an existing user, completing all the data (mandatory and non-mandatory)
    Given I am on the Automation test store page and I select the option to create a new account
    When I fill in all the fields of the form, with data from an existing user and I confirm that data
    Then The system does not have to create that existing user again, and it has to inform me that already exists