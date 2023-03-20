# Created by emreisik at 2/21/23
Feature: Amazon main page test

  Scenario: User can see hamburger menu
    Given Open Amazon page
    Then Verify hamburger menu icon present

  Scenario: Footer and header has correct amount of links
    Given Open Amazon page
    Then Verify that footer has 42 links
    Then Verify that header has 29 links

  Scenario: Hover Over
    Given Open Amazon page
    When Hover over on language option
    Then Verify user can see Language section

  Scenario: Hover Over NEW
    Given Open new arrivals
    When Hover over on new arrivals option
    Then Verify user can see new deals