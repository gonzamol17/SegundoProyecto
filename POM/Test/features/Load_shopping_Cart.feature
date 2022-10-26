Feature: Load some products in the shopping cart
  As a client of WebPage,
  I want to be able to select some products, and add them to my shopping cart
  without confirming the purchase.

@Regression
  Scenario: Load the shopping cart, with some products
    Given I am on the Automation test store page logged in
    When I select some products to add to my shopping cart, without confirming the purchase
    Then I see those products in my shopping cart