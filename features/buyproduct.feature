Feature: Purchase an item
  Scenario: Purchase an item
    Given Launch Chrome browser
    When Open the Saucedemo page
    And Enter username "standard_user" and password "secret_sauce"
    Then User must successfully login
    Then User adds Sauce Labs Backpack to cart
    Then User clicks on checkout button
    Then User fills checkout information with name "Dante", last name "Perez", postal code "45010"
    Then User finishes the purchase
    Then User sees a success message appears on screen
    Then Close browser