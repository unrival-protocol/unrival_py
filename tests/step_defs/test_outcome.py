import pytest
from pytest_bdd import scenario, given, when, then

from unrival_py import *

PROTOCOL = "ipfs"

@scenario('../features/Outcome.feature', 'create an outcome')

def test_create_outcome():
    pass

@given("an address of an outcome", target_fixture="outcome_address")
def outcome_prototype_address(outcome_prototype):
    return outcome_prototype

@given("an outcome ", target_fixture="newly_created_outcome")
def outcome_proof_address(outcome_address):
    description = 'pigs fly'
    address = create_outcome(outcome_address, description)
    return address

@then("this outcome has no prototype")
def create_root_outcome(proof_address):
    outcome_string = read(newly_created_root_outcome)
    outcome_parts = parse(outcome_string)
    # after creation, the resulting object should not inherit from outcome
    assert not has_part(outcome_parts, 'prototype', 'outcome')
