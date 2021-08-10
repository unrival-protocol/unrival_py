import pytest
from pytest_bdd import scenario, given, when, then

from unrival_py import *

PROTOCOL = "ipfs"

@scenario('../features/Goal.feature', 'create a goal')

def test_create_goal():
    pass

@given("an outcome", target_fixture="outcome")
def a_proof(outcome_address):
    return outcome_address

@given("an agent", target_fixture="agent")
def satisfying_parts(agent_address):
    return agent_address

@given("a namespace", target_fixture="namespace")
def satisfying_parts(namespace_address):
    return namespace_address

@then("this agent can create a goal based on this outcome assigned to this namespace")
def parse_whole(outcome, agent, namespace):
    goal_address = create_goal(outcome, agent, namespace)
    goal_string = read(goal_address)
    goal_parts = parse(goal_string)
    # after creation, the resulting object should inherit from goal
    assert has_part(goal_parts, 'prototype', 'goal')
