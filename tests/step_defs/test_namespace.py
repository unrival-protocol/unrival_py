import pytest
from pytest_bdd import scenario, given, when, then

from unrival_py import *

PROTOCOL = "ipfs"

@scenario('../features/Namespace.feature', 'create a root level namespace')

def test_create_root_level_namespace():
    pass

@given("a list of outcomes", target_fixture="root_level_outcomes")
def root_level_outcomes(outcomes_list):
    return outcomes_list

@given("an address of a proof", target_fixture="proof_address")
def root_level_proof(root_level_namespace_proof):
    return root_level_namespace_proof

@given("a namespace can be created using these outcomes and this proof", target_fixture="newly_created_root_namespace")
def create_root_namespace(root_level_outcomes, proof_address):
    namespace_address = create_namespace(root_level_outcomes, proof_address)
    return namespace_address

@then("this namespace has no prototype")
def create_root_namespace(newly_created_root_namespace):
    namespace_string = read(newly_created_root_namespace)
    namespace_parts = parse(namespace_string)
    # after creation, the resulting object should not inherit from namespace
    assert not has_part(namespace_parts, 'prototype', 'namespace')

@scenario('../features/Namespace.feature', 'create a nested namespace')

def test_create_nested_namespace():
    pass

@given("a namespace address", target_fixture="namespace_address")
def a_namespace(a_namespace_address):
    return a_namespace_address

@given("a list of outcomes dependent upon the outcomes associated with this namespace", target_fixture="dependent_outcomes")
def some_dependent_outcomes(outcomes_dependent_upon_namespace):
    return outcomes_dependent_upon_namespace

@given("a new namespace is created using this namespace as its parent", target_fixture="new_nested_namespace")
def parse_whole(top_level):
    namespace_address = create_namespace(dependent_outcomes, )
    namespace_string = read(namespace_address)
    namespace_parts = parse(namespace_string)
    # after creation, the resulting object should inherit from namespace
    assert has_part(namespace_parts, 'prototype', 'namespace')
