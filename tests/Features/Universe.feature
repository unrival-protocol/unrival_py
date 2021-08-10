Feature: Universe

  Scenario: get an address for a namespace
    Given a namespace
    And a universe containing this namespace
    Then this address will be returned when this namespace is looked up
    
  Scenario: fail to get an address for a namespace
    Given a namespace
    And a universe not containing this namespace
    Then no address will be returned when this namespace is looked up
    
