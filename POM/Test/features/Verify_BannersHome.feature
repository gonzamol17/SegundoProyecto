Feature: Verify the banners on the Home Page
 As a user, I want to be able to verify,
 that the banners displayed on the home page are correct.

@Regression
  Scenario: Verify the banners on the Home Page
    Given I am on the Automation page store
    When I stand on the banners section and check each one
    Then I can verify that the banners shown are correct