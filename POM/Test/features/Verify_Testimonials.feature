Feature: Check all testimonials and print them
  As a user, I want to be able to verify all existing testimonials,
  and print them


@Regression, @Sanity
  Scenario: Verify each of the testimonials and print them
    Given I am on the Automation test
    When I scroll to the bottom of the screen, and check each of the items in the Testimonials section
    Then I verify each existing testimonial, and print them