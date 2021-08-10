Feature: Judgment
  
  Scenario: judge a claim to be invalid
    Given a namespace
    And an object of this namespace
    And an agent subscribed to this namespace
    And a claim attached to this object
    When this agent judges this claim to be invalid
    Then this object now has a validity score of -1

  Scenario: judge a claim to be valid
    Given a namespace
    And an object of this namespace
    And an agent subscribed to this namespace
    And a claim attached to this object
    When this agent judges this claim to be valid
    Then this object now has validity score of 1
