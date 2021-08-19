Feature: Object

  Scenario: create base object
    Given the object proof
    And a namespace containing the name object
    And the empty universe
    And the base interpretation
    And parts containing these objects
    And a protocol
    And an object is created from these parts
    And it can be proved

  Scenario: create object with ancestor 
    Given a set of parts including a namespace and a universe
    And an interpretation associating the namespace with an object
    And the object located at this address has a proof
    And these parts satisfy this proof
    Then an object can be created from these parts

  Scenario: create object with ancestor and own proof
    Given a set of parts including a namespace and a universe
    And this universe has an address associated with this namespace
    And the object located at this address has a proof
    And these parts satisfy this proof
    Then an object can be created from these parts

  Scenario: fail to create object due to own proof failure
    Given a proof
    And a set of parts containing but not satisfying this proof
    Then an object cannot be created from these parts

  Scenario: fail to create object due to ancestor proof failure
    Given a proof
    And a set of parts containing but not satisfying this proof
    Then an object cannot be created from these parts



  """ 
  Scenario: fail to create object due to non-unique labels
    Given a propsective object includes a proof
    And this prospective object can't satisfy this proof
    Then this prospective object can't be created

  Scenario: fail to create object due to missing parts
    Given a prospective object includes a prototype
    And a name exists equal to the label of this prototype
    And a namespace exists that includes this name
    

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

  """
