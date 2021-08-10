Feature: Claim

  Scenario: attach a claim to a prospective object
    # object 
    Given a namespace
    And an agent subscribed to this namespace
    And a claim
    And a prospective object of this namespace includes this claim
    And this object is created 
    Then the subscribed agent will be notified of the claim
    And the subscribed agent 
    
    
  Scenario: attach a claim to an existing object
    # in order to prevent 
    Given an object is stored at an updateable address 
    

