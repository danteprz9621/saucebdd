Feature: Log in failure
  Scenario: Log in with valid user and pwd
    Given Launch Chrome browser
    When Open the Saucedemo page
    And Enter username "locked_out_user" and password "secret_sauce"
    Then User must not be able to login
    Then Close browser