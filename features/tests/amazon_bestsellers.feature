# Created by emreisik at 2/21/23
Feature: Amazon best sellers page

  Scenario: User can see the best seller button
    Given Open Amazon page
    Then Click on bestsellers button
    Then Verify that bestsellers option has 4 links
