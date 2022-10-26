Feature: Show all elements of the page footer
  As a logged in user,
  I want to be able to count and display all the elements that make up the footer of the page

@Regression
  Scenario: Count and display all the elements that make up the footer of the page
    Given That I am logged in, and i want to count and display all elements of the page footer
    When  I scroll down, to the Footer section of the page
    Then I can count the elements that make up the footer and show each one