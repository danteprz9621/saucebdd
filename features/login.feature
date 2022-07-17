Feature: Log in
  Scenario: Log in with valid user and pwd
    Given Launch Chrome browser
    When Open the Saucedemo page
    And Enter username "standard_user" and password "secret_sauce"
    Then User must successfully login
    Then Close browser