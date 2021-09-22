Feature: Context

    Scenario: create context of degree 1
      """
      A context needs to be attached to a server
      A clean server is one that doesn't require agent consent to contextualize
      """
      Given an agent
      And an address of a server
      And a context
      When this server is contextualized by this agent with this context
      Then this agent is listed as a delegate

    Scenario: add interpretation to context without vote
      """
      With only one delegate,
      no vote is required to update a context
      """
      Given a delegate
      Given a context with one delegate
      When this delegate adds an interpretation to this context
      Then this context has this interpretation

    Scenario: successfully add interpretation to context through vote
      """
      With multiple delegates,
      updating a context requires a vote
      """
      Given a context with two delegates
      And one of these delegates attempts to add an interpretation to this context
      When the other delegate is notified that they can vote
      And they vote to allow the interpretation
      Then this interpretation is added to this context

    Scenario: fail to add interpretation to context through vote
      Given a context with two delegates
      And one of these delegates attempts to add an interpretation to this context
      When the other delegate is notified that they can vote
      And they vote not to allow the interpretation
      Then this context is unchanged
      
    Scenario: successfully add delegate to context through vote
      Given a context with two delegates
      And one of these delegates attempts to add an additional delegate
      When the other delegate is notified that they can vote
      And they vote not to allow the interpretation
      Then this context is unchanged

    Scenario: fail to add delegate to context through vote
      Given a 
