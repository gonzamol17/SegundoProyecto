Feature: Sort listed products by some criteria
 As a user, I want to be able to select a section of products,
 and to be able to sort them by some criteria and see them listed.

@Regression
  Scenario Outline: Sort paperback products by some criteria
    Given I am on the Automation page
    When select the Books-Paperback products and select sort by "<criteria>"
    Then I verify that the products are ordered by the chosen criteria


      Examples: users
        | criteria   |
        | Name A - Z |