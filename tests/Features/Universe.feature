Feature: Universe

  Scenario: create base universe
    Given the universe proof
    And the base namespace
    And an interpretation whereby universe inherits from object
    And an object is created from these parts
    Then it can be read and parsed
    And it can be proved

  Scenario: look up complex object in universe
    Given a universe that assigns a complex object the interpretation /object/example
    And this object's address is looked up
    Then an address is returned that can be parsed

