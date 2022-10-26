Feature: Switch Between three different windows a capture the url and title
  As a logged user, I want to be able to open new tabs,
  capture the url and the title on each tab and close it,  and return to the home screen and capture the url and title


@Regression, @Sanity
  Scenario: Switch between three different windows and capture url and title, and close it
    Given I am in the Automation test store
    When I click on two components of the web and two new tabs open
    Then I capture the title of each page and the url, I close the tabs and go back to the original tab showing the title