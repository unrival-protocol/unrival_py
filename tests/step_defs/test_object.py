import pytest
from pytest_bdd import scenario, given, when, then

from unrival_py import *

"""
@scenario('../features/Object.feature', 'create base object')
def test_create_base_object():
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
    print(create_base_object_parts_containing_these_objects_data_conf)

    parts = parse(create_base_object_parts_containing_these_objects_data_conf)
    object_address, universe_address = create(parts, a_protocol, create_base_object_the_empty_universe)
    return (object_address, universe_address)

@then("it can be proved")
def prove_object(create_base_object_an_object_is_created_from_these_parts, create_base_object_the_object_proof):
    object_address = create_base_object_an_object_is_created_from_these_parts[0]
    universe_address = create_base_object_an_object_is_created_from_these_parts[1]
    assert prove(object_address, universe_address)
    # the above will raise exceptions if proof fails

@scenario('../features/Object.feature', 'create object with ancestor')

def test_create_object_with_ancestor():
    pass

@given("a namespace containing the name example", target_fixture="create_object_with_ancestor_a_namespace_containing_the_name_example")
def ancestor_namespace(ccreate_object_with_ancestor_a_namespace_containing_the_name_example_conf):
    return create_object_with_ancestor_a_namespace_containing_the_name_example_conf

@given("a proof requiring an object to have no more than 10 parts", target_fixture="create_object_with_ancestor_a_proof_requiring_an_object_to_have_no_more_than_10_parts")
def ancestor_universe(create_object_with_ancestor_a_proof_requiring_an_object_to_have_no_more_than_10_parts_conf):
    return create_object_with_ancestor_a_proof_requiring_an_object_to_have_no_more_than_10_parts_conf

@given("an interpretation whereby example inherits from object", target_fixture="create_object_with_ancestor_an_interpretation_whereby_example_inherits_from_object")
def ancestor_proof(create_object_with_ancestor_an_interpretation_whereby_example_inherits_from_object_conf):
    return create_object_with_ancestor_an_interpretation_whereby_example_inherits_from_object_conf


@given("a universe")
def ancestor_universe(create_object_with_ancestor_a_universe_wherein_object_can_be_interpreted_conf):
    return create_object_with_ancestor_a_universe_wherein_object_can_be_interpreted_conf

@given("parts containing these objects", target_fixture="create_object_with_ancestor_parts_containing_these_objects")
def ancestor_parts(create_object_with_ancestor_parts_containing_these_objects_conf):
    return create_object_with_ancestor_parts_containing_these_objects_conf

@given("an object is created from these parts", target_fixture="create_object_with_ancestor_an_object_is_created_from_these_parts")
def ancestor_create(create_object_with_ancestor_parts_containing_these_objects_data_conf, create_object_with_ancestor_a_universe_conf, a_protocol):
    object_hash, universe_hash = create(create_object_with_ancestor_parts_containing_these_objects_data_conf, a_protocol, create_object_with_ancestor_a_universe_conf)
    return object_hash

@then("it can be proved")
def ancestor_prove(create_object_with_ancestor_an_object_is_created_from_these_parts):
    object_address = create_object_with_ancestor_an_object_is_created_from_these_parts[0]
    universe_address = create_object_with_ancestor_an_object_is_created_from_these_parts[1]
    assert prove(object_address, universe_address, None)
    # the above will raise exceptions if proof fails



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
