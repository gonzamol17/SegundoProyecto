Feature: Edit a second address from Address Manage Books
  as a logged user, I want to be able to Select the Manage Address Book option,
  and edit the second address


@Regression, @Sanity
  Scenario: Edit the second address from the Manage Address Book option
    Given I am on login in the Automation test page
    When I click on the Manage Address Book option, and verify that I have an existing address, editing it and saving that data
    Then I verify that the system shows me an edited address message, and the new address is within Address Book Entries