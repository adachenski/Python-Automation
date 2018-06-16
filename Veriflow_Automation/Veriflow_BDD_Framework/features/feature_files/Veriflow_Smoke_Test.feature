Feature: Basic Smoke Test

  Scenario: Verify User Login
    Given Open Chrome Browser
    When Navigate to Veriflow Login page at "https://172.17.9.63"
    And Enter username "ui-admin-1"
    And Enter password "ui-admin-123"
    Then Click on Login Tab

  Scenario: Verify User can go to Resiliency Page
    Given Go to Resiliency page
    Then Verify User is on Resiliency page

  @dontRun
  Scenario: Verify user can click on random device from Top 5 CPU Utilization section
    Given Scroll down to Utilization and Errors section
    When Click on random device from Top 5 CPU Utilization
    And Verify that device is shown on Explorer page
    And Open Device Details and Verify CPU Utilization value
    Then I close the browser


  Scenario Outline: Verify user can click on random device from Utilization and Errors
    Given Scroll down to Utilization and Errors section
    When Click on random device from "<section>"
    And Verify that device is shown on Explorer page
    And Go to Resiliency page
    And Verify User is on Resiliency page
    #And Open Device Details and Verify CPU Utilization value
    Examples: Utilization and Errors
        | section                     | random_device |
        | Top 5 CPU Utilization       | random        |
        | Top 5 Memory Utilization    | random        |
        | Top 5 Utilized Interfaces   | random        |
        | Top 5 CRC Error Count       | random        |
        | Top 5 (Shortest) Uptime     | random        |
        | Top 5 (Longest) Uptime      | random        |


  Scenario: Verify that browser is closed
    Then I close the browser
