Feature: Create a User on Automation Test Store
  As a potential client,
  I want to be able to enter the page, create a new user,
  to be able to enter my account and see different products.

@Regression
  Scenario: Create a new user successfully, loading all the fields (mandatory and non-mandatory)
    Given I am on the Automation test store page and I select the option to create a new account
    When I fill in all the fields of the form and I confirm that data
    Then I successfully create my account and verify that I am logged in with my newly created account