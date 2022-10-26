Feature: Check the out of Stock for a particular product
  As a client I want to be able
  to visualize a leyend that says "Out of Stock",
  for products without stock

  @Regression
  Scenario: Display a legend that reports that there is no stock for certain products.
    Given I am on the Automation test store
    When I select a product that I know is out of stock
    Then I visualize a legend that says Out of Stock, and that has a gray background color.
