# Created by emreisik at 2/21/23
Feature: Amazon customer service UI element test case

  Scenario: Check if UI elements present
    Given Open amazon customer service
    Then Verify welcome to amazon customer service is present
    Then Verify that there is 10 shortcut links
    Then Verify that Search our help library is shown
    Then Verify search box is present
    When Verify All help topics is shown
    Then Verify that customer service has 12 links