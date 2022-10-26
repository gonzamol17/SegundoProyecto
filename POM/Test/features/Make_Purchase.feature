Feature: Make a purchase
  As a client,
  I want to be able to enter the page, select a product,
  and confirm the purchased product.

@Regression
  Scenario: Select and buy a product from the webpage
    Given I am on the Automation test store page logged in, and i have my shopping cart without products
    When I select the type of product, the product and its characteristics, and confirm the order
    Then I verify that the order was processed successfully