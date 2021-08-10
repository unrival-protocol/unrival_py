Feature: Object

  As an agent
  In order to coordinate with other agents more effectively
  I want an assurance that other agents and I are referring to the same things when we communicate

  Scenario: create object
    # the simplest possible Unrival object
    Given a proof 
    And a set of parts containing and satisfying this proof
    Then an object can be created from these parts

  Scenario: create object with prototype
    Given a propsective object includes a prototype
    And a name exists equal to the label of this prototype
    And a namespace exists that includes this name
    And this prospective object can pass its prototype's proof
    Then this prospective object can be created

  Scenario: fail to create object due to direct proof failure
    Given a propsective object includes a proof
    And this prospective object can't satisfy this proof
    Then this prospective object can't be created

  Scenario: fail to create object due to immediate ancestor prototype failure
    # indirect proof
    Given a propsective object includes a prototype
    And this prospective object can't satisfy its prototype's proof
    Then this prospective object can't be created

  Scenario: fail to create object due to nth-degree ancestor prototype failure
    # indirect proof
    Given a propsective object includes a prototype
    And this prospective object can't satisfy its prototype's proof
    Then this prospective object can't be created

  Scenario: fail to create object due to claim failure
    Given a propsective object includes a claim
    And this claim can't be substantiated
    Then this prospective object can't be created
  
  
