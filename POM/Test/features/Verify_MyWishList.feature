Feature: Verify my Wish List
  As a user logged,
  I want to be able to enter the page, add products to my wish list,
  and then i can go to that section and check my desired products.

@Regression
  Scenario: Verify some product from My Wish List section
    Given I am on the Automation test store logged in
    When  I select a product and add it to my wish list
    Then I enter on My Wish List section, and verify that the product is added