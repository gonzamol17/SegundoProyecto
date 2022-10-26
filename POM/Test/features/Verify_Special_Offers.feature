Feature: Verify the products displayed in the Special Offers Section
  As a user I want to be able to enter the Special Offers section,
  and verify that the products shown have the label "Sale" and know the quantity.


@Regression
  Scenario: Verify the quantity of special products and if it has the Sale label
    Given I am on Automation test page
    When I select the Special link
    Then I should see the number of specials products, and if they have the Sale tag