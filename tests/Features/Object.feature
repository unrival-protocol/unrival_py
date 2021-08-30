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

  Scenario: only objects with proofs are progenerative
    # TODO write this scenario

  Scenario: create object of degree 2
    Given a proof requiring an object to have 10 parts
    And an object of degree 1 referencing this proof
    And a protocol
    And an interpretation of degree 2
    And a context where the parent can be interpreted
    And an object with 10 parts including these parts is created 
    And an object without 10 parts including these parts is created
    Then the object with 10 parts can be proved
    And the object without 10 parts can't be proved
