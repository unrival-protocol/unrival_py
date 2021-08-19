Feature: Namespace
  
  Scenario: create base namespace
    Given the root proof
    And the namespace proof
    And a namespace containing the name object
    And a universe containing this namespace
    And an interpretation 
    And parts containing these objects
    And an object is created from these parts
    Then it can be read and parsed
    And it can be proved

  """
  Scenario: subscribe to a namespace
    Given an agent
    And a namespace
    When this agent subscribes to this namespace
    Then this agent is in the namespace's subscribers list
  """
