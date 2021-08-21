import pytest
from pytest_bdd import scenario, given, when, then

from unrival_py import *

@scenario('../features/Universe.feature', 'create base universe')

def test_create_base_universe():
    pass

@given("the universe proof", target_fixture="create_base_universe_the_universe_proof")
def a_namespace(create_base_universe_the_universe_proof_conf):
    return create_base_universe_the_universe_proof_conf

@given("the empty universe", target_fixture="create_base_universe_the_empty_universe")
def empty_universe(create_base_universe_the_empty_universe_conf):
    return create_base_universe_the_empty_universe_conf

@given("the base namespace", target_fixture="create_base_universe_the_base_namespace")
def a_namespace(create_base_universe_the_base_namespace_conf):
    return create_base_universe_the_base_namespace_conf

@given("an interpretation whereby universe inherits from object", target_fixture="create_base_universe_an_interpretation_whereby_universe_inherits_from_object")
def the_universe_proof(create_base_universe_an_interpretation_whereby_universe_inherits_from_object_conf):
    return create_base_universe_an_interpretation_whereby_universe_inherits_from_object_conf

@given("an object is created from these parts", target_fixture="create_base_universe_an_object_is_created_from_these_parts")
def an_object_is_created(create_base_universe_an_object_is_created_from_these_parts_conf):
    return create_base_universe_an_object_is_created_from_these_parts_conf

@then("it can be read and parsed")
def read_and_parse(create_base_universe_an_object_is_created_from_these_parts):
    object_string = read(create_base_universe_an_object_is_created_from_these_parts)
    assert isinstance(object_string, str)
    object_parts = parse(object_string)
    assert isinstance(object_parts, list)

@then("it can be proved")
def prove_universe(create_base_universe_an_object_is_created_from_these_parts, create_base_universe_the_empty_universe_conf):
    assert prove(create_base_universe_an_object_is_created_from_these_parts, create_base_universe_the_empty_universe_conf)

"""
@scenario('../features/Universe.feature', 'create universe with ancestor')

def test_create_universe_with_ancestor():
    pass

@given("a set of parts including a namespace and a universe", target_fixture="create_universe_with_ancestor_parts_with_namespace_and_universe")
def part_namespace_address(create_universe_with_ancestor_parts):
    return create_universe_with_ancestor_parts

@given("a universe has an address associated with this namespace", target_fixture="create_universe_with_namespace_and_universe")
def satisfying_parts(create_universe_with_ancestor_parts_with_namespace_and_universe, create_universe_with_ancestor_universe):
    # assert this universe has a an address
    namespaces = get_part(create_universe_with_ancestor_parts_with_namespace_and_universe, 'namespace')
    for namespace in namespaces:
        # multiple namespaces is used for multiple inheritance

        assert in_universe(create_universe_with_ancestor_universe, namespace)

    return create_universe_with_namespace_universe

@given("an universe is created from these parts", target_fixture="universe_address")
def create_universe(create_base_universe_parts_containing_these_universes_conf):
    universe_hash = create(create_base_universe_parts_containing_these_universes_conf, PROTOCOL)
    return universe_hash


@then("it can be read and parsed")
def read_and_parse(universe_address):
    universe_string = read(universe_address)
    assert isinstance(universe_string, str)
    universe_parts = parse(universe_string)
    assert isinstance(universe_parts, list)

@then("it is a valid unrival universe")
def is_valid_universe(universe_address):
    universe_string = read(universe_address)
    assert isinstance(universe_string, str)
    universe_parts = parse(universe_string)
    assert isinstance(universe_parts, list)


@given("a set of parts referencing and satisfying this proof", target_fixture="create_universe_parts_satisfying_proof")
def satisfying_parts(create_universe_proof, create_universe_parts):
    assert create_universe_proof_address in [part['address'] for part in create_universe_parts]
    return create_universe_parts



@scenario('../features/Universe.feature', 'fail to create universe due to direct proof failure')

def test_fail_to_create_due_to_direct_proof():
    pass

#@given("a proof", target_fixture="proof_address")
#def a_proof(simple_universe):
#    return simple_universe

@given("a set of parts that claim this proof but don't pass its conditions", target_fixture="parts_that_dont_satisfy")
def insufficient_parts(proof, insufficient_parts):
    assert proof in [x['address'] for x in insufficient_parts]
    return insufficient_parts

@then("an unrival universe cannot be created from these parts")
def creation_fails(parts_that_dont_satisfy):
    with pytest.raises(ValueError):
        address = create(parts_that_dont_satisfy, 'ipfs')

# @scenario('../features/Universe.feature', 'instance can\'t be proved because it\'s missings some of prototype\'s parts')

"""
