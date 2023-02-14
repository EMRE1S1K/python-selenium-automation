# Created by emreisik at 2/14/23
Feature: Amazon cart check

  Scenario: Amazon cart empty
    Given Start amazon.com
    When Click on cart button
    Then Verify that cart is empty