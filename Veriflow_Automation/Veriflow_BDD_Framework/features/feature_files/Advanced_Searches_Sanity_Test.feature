Feature: Demo 5.0 Explorer Page Advanced Searches Smoke Test

  Scenario: Verify User Login
    Given Open Chrome Browser
    When Navigate to Veriflow Login page at "https://172.17.9.4"
    And Enter username "veriflow"
    And Enter password "veriflow"
    Then Click on Login Tab

  Scenario: Verify Flow Model is Loaded
    Given Verify that Graph is shown on Explorer page
    When Load snapshot Flow Model from the navigation menu
    And Verify that Graph is shown on Explorer page
    Then Click on the Advanced tab at the top left corner


  Scenario Outline: : Verify Advanced Searches Functionality
    When Click into the search box and enter "<query>"
    And Execute the query
    Then Verify "<devices>" and "<paths>" returned

    Examples: Flow Queries
          | query                                                                                    |devices   |paths        |
          | @ny --> @backbone                                                                        |7 Devices |25 Flow Paths|
          | ip dst 100.2.1.102 and port dst 80 @google-rtr,entry --> ip dst 10.2.50.102 @drdmz-acc-1 |6 Devices |2 Flow Paths |
          | ip src 10.3.10.1 and ip dst 8.8.8.8 @ny-acc-fin --> @isp2-rtr --> @google-rtr            |11 Devices|4 Flow Paths |
          | ip dst 8.8.8.8 @ny-acc-fin --> @isp2-rtr --> @google-rtr                                 |12 Devices|2 Flow Paths |
          | vlan 100 and (ether src 00:be:f7:00:80:64 and ether dst 00:be:f7:58:80:64) @region(pr-dc)|5 Devices |25 Flow Paths|

#   Scenario: Verify that browser is closed
#    Then I close the browser
