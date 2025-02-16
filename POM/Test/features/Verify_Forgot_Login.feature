Feature: Forgot Login in the Automation Test Store
  As a user,
  I want to be able to recovery the password, entering my username and email,
  to be able to reset the password.

@Regression
  Scenario Outline: Forgot login in Automation Test Store
    Given I try to enter the Automation test store page, and I don't remember the password
    When I select the forgot password option, and lastname "<lastname>" and email "<email>"
    Then I get a message with result "<message>" for password recovery


      Examples: users
        | lastname | email                      | message    |
        | Molina   | gonzalo.molina@darwoft.com | Successful |
        | Pedrito  | gonzalo.molina@darwoft.com | Failed     |