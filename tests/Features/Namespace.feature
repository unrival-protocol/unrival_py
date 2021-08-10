Feature: Namespace
  
  Scenario: create a namespace
    Given a name
    Then a namespace can be created from this name

  Scenario: create a nested namespace
    Given a namespace
    And a name
    Then a namespace can be created from this name that inherits from this namespace

  Scenario: subscribe to a namespace
    Given an agent
    And a namespace
    When this agent subscribes to this namespace
    Then this agent is in the namespace's subscribers list
