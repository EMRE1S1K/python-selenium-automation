# Created by emreisik at 2/28/23
Feature: Open amazon product Amazon Essentials Men's Slim-Fit Stretch Jean

  Scenario: Color search
    Given Open Amazon Product page
    Then Verify user can click on all the colors


  Scenario: Mug images and names are present
    Given Open Amazon page
    When Input text black mug
    When Click on search button
    Then Verify that all the mug images visible
    Then Verify product names are present

  Scenario: Verify each top link opens correct page
    Given Open Amazon bestseller page
    Then Verify user can click on all best seller links

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original
