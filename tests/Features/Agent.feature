Feature: Agent

  Scenario: generate public key
    Given a private key
    And a public key is generated from this private key
    Then this private key can be used to verify identity associated with the public key

  
