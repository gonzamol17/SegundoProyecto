Feature: Make a purchase
  As a client,
  I want to be able to enter the page, select a product,
  and confirm the purchased product.

@Regression
  Scenario: Select and buy a product from the webpage
    Given I am on the Automation test store page logged in, with zero products
    When I select the type of product and its characteristics, confirm the order, and I save the order_id
    Then I verify that the order was processed successfully and i checked the Order_id on a Order History section