Feature: Object

  Scenario: create object of degree 0
    Given a protocol
    And some parts
    And an object is created using these parts
    Then it can be proved

  Scenario: create object of degree 1
    Given a protocol
    And an interpretation
    And a proof 
    And an object is created using these parts
    Then it can be proved
    And it can be interpreted

  """
  Scenario: create a parent
    Given an interpretation with one level
    And a proof
    And a universe 
    And parts referencing these objects
    Then an object can be created
    And it can be proved

  Scenario: create a child
    Given an interpretation with multiple levels
    And a proof requiring an object to have exactly 10 parts
    And an object referencing this proof
    And a universe in which the penultimate interpretation level means this object
    And parts referencing these objects
    Then an object can be created
    And it can be proved    
    And it must have exactly 10 parts

  """
