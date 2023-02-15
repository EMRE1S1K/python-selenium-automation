# Created by emreisik at 2/14/23
Feature: Shopping cart check

  Scenario: Add items to cart
    Given Launch amazon
    When Search for espresso cream drink
    Then search button
    When Add item into cart
    Then Check the item
    And click again
    Then Check if item visible