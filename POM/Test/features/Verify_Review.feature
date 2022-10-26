Feature: Give a review to a selected product without code
  As a logged in user, I want to be able
  to select a product and give a rating and a review to that product without code


@Regression, @Sanity
  Scenario: Add a product review without entering a code and verify the validation error
    Given I am on login in the Automation test
    When I select the category, and then the product
    And I select the option to give Review to that product, I give it a score, I enter the name of the user "gonzalo" and a review "Me regalan un shampoo por favor?".
    Then I see the error message, when not completing the code