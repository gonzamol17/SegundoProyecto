Feature: Switch Between two different windows a capture the url and title
  As a logged user, I want to be able to click on a link and open a new tab,
  capture the url and the title of the tab and return to the home screen and capture the url and title


@Regression, @Sanity
  Scenario: Switch between two different windows and capture url and title
    Given I am on login in the Automation test store
    When I click on the "t" link, and i capture the url and the title of the tab
    Then I go back to the initial tab and capture the url and the title of the tab
