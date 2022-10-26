Feature: Item Box
   As a user,
   I want to change the Actual currency, select some products and match if from the
  item box, are those products and with the selected currency


@Regression
  Scenario: Change the currency, select some product and verify to those products are in the currency selected
    Given I am on the Automation test logged
    When  I change the currency and i select two products with that currency
    Then  selecting the item box, i have to view the two selected products and they are in the changed currency.

