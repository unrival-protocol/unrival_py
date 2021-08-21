import pytest
from pytest_bdd import scenario, given, when, then

from unrival_py import *

@scenario('../features/Object.feature', 'create base object')

@pytest.mark.base
def test_create_base_object():
    """
    The base object is the first possible object, which is:
    0. dependent on the root proof, because successful creation of any object requires proof of validity
    1. co-dependent on the creation of the first universe and the first interpretation
    """
    pass

@given("the object proof", target_fixture="create_base_object_the_object_proof")
def a_namespace(create_base_object_the_object_proof_conf):
    return create_base_object_the_object_proof_conf

@given("the empty universe", target_fixture="create_base_object_the_empty_universe")
def the_empty_universe(create_base_object_the_empty_universe_conf):
    return create_base_object_the_empty_universe_conf

@given("the base interpretation", target_fixture="create_base_object_the_base_interpretation")
def the_base_interpretation(create_base_object_the_base_interpretation_conf):
    return create_base_object_the_base_interpretation_conf

@given("parts containing these objects", target_fixture="create_base_object_parts_containing_these_objects")
def parts_containing(create_base_object_parts_containing_these_objects_data_conf):
    return create_base_object_parts_containing_these_objects_data_conf

@given("an object is created from these parts", target_fixture="create_base_object_an_object_is_created_from_these_parts")
def an_object_is_created(create_base_object_parts_containing_these_objects_data_conf, a_protocol, create_base_object_the_empty_universe):
    print('the empty universe:')
    print(create_base_object_the_empty_universe)
    parts = parse(create_base_object_parts_containing_these_objects_data_conf)
    result = create(parts, create_base_object_the_empty_universe, a_protocol)
    return result

@then("it can be proved")
def prove_object(create_base_object_an_object_is_created_from_these_parts, create_base_object_the_object_proof):
    object_address = create_base_object_an_object_is_created_from_these_parts[0]
    universe_address = create_base_object_an_object_is_created_from_these_parts[1]
    assert prove(object_address, universe_address, None, create_base_object_the_object_proof)
    # the above will raise exceptions if proof fails

"""
@scenario('../features/Object.feature', 'create object with ancestor')

def test_create_object_with_ancestor():
    pass

@given("a set of parts including a namespace and a universe", target_fixture="create_object_with_ancestor_parts_with_namespace_and_universe")
def part_namespace_address(create_object_with_ancestor_parts):
    return create_object_with_ancestor_parts

@given("a universe has an address associated with this namespace", target_fixture="create_object_with_namespace_and_universe")
def satisfying_parts(create_object_with_ancestor_parts_with_namespace_and_universe, create_object_with_ancestor_universe):
    # assert this universe has a an address
    namespaces = get_part(create_object_with_ancestor_parts_with_namespace_and_universe, 'namespace')
    for namespace in namespaces:
        # multiple namespaces is used for multiple inheritance

        assert in_universe(create_object_with_ancestor_universe, namespace)

    return create_object_with_namespace_universe

@given("an object is created from these parts", target_fixture="object_address")
def create_object(create_base_object_parts_containing_these_objects_data_conf):
    object_hash = create(create_base_object_parts_containing_these_objects_data_conf, PROTOCOL)
    return object_hash


@then("it can be read and parsed")
def read_and_parse(object_address):
    object_string = read(object_address)
    assert isinstance(object_string, str)
    object_parts = parse(object_string)
    assert isinstance(object_parts, list)

@then("it is a valid unrival object")
def is_valid_object(object_address):
    object_string = read(object_address)
    assert isinstance(object_string, str)
    object_parts = parse(object_string)
    assert isinstance(object_parts, list)


@given("a set of parts referencing and satisfying this proof", target_fixture="create_object_parts_satisfying_proof")
def satisfying_parts(create_object_proof, create_object_parts):
    assert create_object_proof_address in [part['address'] for part in create_object_parts]
    return create_object_parts



@scenario('../features/Object.feature', 'fail to create object due to direct proof failure')

def test_fail_to_create_due_to_direct_proof():
    pass

#@given("a proof", target_fixture="proof_address")
#def a_proof(simple_object):
#    return simple_object

@given("a set of parts that claim this proof but don't pass its conditions", target_fixture="parts_that_dont_satisfy")
def insufficient_parts(proof, insufficient_parts):
    assert proof in [x['address'] for x in insufficient_parts]
    return insufficient_parts

@then("an unrival object cannot be created from these parts")
def creation_fails(parts_that_dont_satisfy):
    with pytest.raises(ValueError):
        address = create(parts_that_dont_satisfy, 'ipfs')

# @scenario('../features/Object.feature', 'instance can\'t be proved because it\'s missings some of prototype\'s parts')

"""
