# Created by emreisik at 2/14/23
Feature: Amazon cart check

  Scenario: Amazon cart empty
    Given Open Amazon page
    When Click on cart button
    Then Empty Your Amazon Cart is empty text shown