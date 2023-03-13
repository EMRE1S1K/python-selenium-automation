# Created by emreisik at 2/14/23
Feature: Shopping cart check

  Scenario: Add items to cart
    Given Open Amazon page
    When Search for espresso cream drink
    Then search button
    When Select an item
    Then Move item into cart
    And click again
    Then Check if Added to Cart text shown
