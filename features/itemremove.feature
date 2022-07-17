Feature: Remove item
  Scenario: Remove item from cart
    Given Launch Chrome browser
    When Open the Saucedemo page
    And Enter username "standard_user" and password "secret_sauce"
    Then User must successfully login
    Then User adds Sauce Labs Backpack and Sauce Labs Bike Light to cart
    Then User removes last item
    Then Last item shouldn't appear in cart
    Then Close browser