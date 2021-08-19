Feature: Universe

  Scenario: create base universe
    Given a universe only containing the base namespace
    And the universe proof
    And a namespace containing the name universe
    And an interpretation whereby universe inherits from object
    And an object is created from these parts
    Then it can be read and parsed
    And it can be proved

  Scenario: get an address for a namespace
    Given a namespace
    And a universe containing this namespace
    Then this address will be returned when this namespace is looked up
    
  Scenario: fail to get an address for a namespace
    Given a namespace
    And a universe not containing this namespace
    Then no address will be returned when this namespace is looked up
