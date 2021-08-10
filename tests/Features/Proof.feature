Feature: Proof

  As an agent
  In order to ensure that objects are what they claim to be 
  I want a way to test their claims

  Scenario: execute proof
    Given an address for a proof
    Then executing the code at this address should return a valid exit code
