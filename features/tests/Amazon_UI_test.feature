# Created by emreisik at 2/12/23
Feature: Amazon search test

  Scenario Outline: Amazon product search
    Given Open Amazon page
    When Input text <search_word>
    When Click on search button
    Then Verify that text <search_result> is shown
    Examples:
    |search_word  |search_result |
    |coffee       |"coffee"      |
    |table        |"table"       |
    |mug          |"mug"         |


  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias stripbooks
    When Input text Faust
    When Click on search button
    Then Verify books department selected


  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias handmade
    When Input text necklace
    When Click on search button
    Then Verify handmade department selected


