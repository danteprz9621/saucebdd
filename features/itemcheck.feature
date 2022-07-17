Feature: Check item detail
  Scenario: Check item detail
    Given Launch Chrome browser
    When Open the Saucedemo page
    And Enter username "standard_user" and password "secret_sauce"
    Then User must successfully login
    Then User adds Sauce Labs Backpack to cart
    Then User clicks on item name
    Then User sees item detail
    Then Close browser