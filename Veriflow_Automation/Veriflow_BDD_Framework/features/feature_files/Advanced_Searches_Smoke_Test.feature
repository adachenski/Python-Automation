Feature: Explorer Page Advanced Searches Smoke Test

  Scenario: Verify User Login
    Given Open Chrome Browser
    When Navigate to Veriflow Login page at "https://172.17.10.187"
    And Enter username "veriflow"
    And Enter password "veriflow"
    Then Click on Login Tab

  Scenario: Verify Flow Model is Loaded
    Given Verify that Graph is shown on Explorer page
    Then Load snapshot Flow Model from the navigation menu

  Scenario Outline: : Verify Advanced Searches Functionality
    Given Verify that Graph is shown on Explorer page
    When Click into the search box and enter "<query>"
    And Execute the query
    Then Verify the query

    Examples: Flow Queries
          | query                                                                                       | result    |
          | @ny --> @backbone                                                                           | 4         |
          | ip dst 100.2.1.102 and port dst 80 @google-rtr,entry --> ip dst 10.2.50.102 @drdmz-acc-1    | 5         |
          | ip src 10.3.10.1 and ip dst 8.8.8.8 @ny-acc-fin --> @isp2-rtr --> @google-rtr               | 7         |
          | ip src 10.3.10.1 and ip dst 8.8.8.8 @ny-acc-fin --> @isp2-rtr --> @google-rtr               | 7         |
          | vlan 100 and (ether src 00:be:f7:00:80:64 and ether dst 00:be:f7:58:80:64) @region(pr-dc)   | 9         |