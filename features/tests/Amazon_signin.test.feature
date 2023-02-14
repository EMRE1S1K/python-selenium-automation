# Created by emreisik at 2/14/23
Feature: Sign in is visible.


  Scenario: Sign in test case..
    Given Get amazon page
    When Check the orders&returns
    Then Verify Sign in text shown
