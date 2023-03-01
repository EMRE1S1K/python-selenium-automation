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

