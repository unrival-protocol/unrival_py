import pytest
from pytest_bdd import scenario, given, when, then

from unrival_py import *

@scenario('../features/Object2.feature', 'create object of degree 0')
def test_object_degree_0():
    pass

@given("some parts", target_fixture="create_object_of_degree_0_some_parts")
def some_parts(create_object_of_degree_0_some_parts_data_conf):
    return create_object_of_degree_0_some_parts_data_conf

@given("an object is created using these parts", target_fixture="create_object_of_degree_0_an_object_is_created_using_these_parts")
def create_object_degree_0(create_object_of_degree_0_some_parts, a_protocol):
    parts = parse(create_object_of_degree_0_some_parts)
    new_object_address, new_universe_address = create(parts, a_protocol)
    return new_object_address

@then("it can be proved")
def prove_object_degree_0(create_object_of_degree_0_an_object_is_created_using_these_parts):
    assert prove(create_object_of_degree_0_an_object_is_created_using_these_parts)


@scenario('../features/Object2.feature', 'create object of degree 1')
def test_object_degree_1():
    pass

@given("an interpretation", target_fixture="create_object_of_degree_1_an_interpretation")
def object_degree_1_interpretation(create_object_of_degree_1_an_interpretation_data_conf):
    return create_object_of_degree_1_an_interpretation_data_conf

@given("a proof", target_fixture="create_object_of_degree_1_a_proof")
def object_degree_1_proof(create_object_of_degree_1_a_proof_data_conf):
    return create_object_of_degree_1_a_proof_data_conf

@given("an object is created using these parts", target_fixture="create_object_of_degree_1_an_object_is_created_using_these_parts")
def object_degree_1_create_object(create_object_of_degree_1_an_interpretation_data_conf, create_object_of_degree_1_a_proof_data_conf, a_protocol):
    interpretation_part = make_simple_part('/interpretation', create_object_of_degree_1_an_interpretation_data_conf, a_protocol)
    proof_part = make_simple_part('/proof', create_object_of_degree_1_a_proof_data_conf, a_protocol)
    parts = [interpretation_part, proof_part]
    new_object_address, new_universe_address = create(parts, a_protocol)
    print('======')
    print(new_object_address)
    print('======')
    return (new_object_address, new_universe_address)

@then("it can be proved")
def object_degree_1_prove(create_object_of_degree_1_an_object_is_created_using_these_parts):
    
    assert prove(create_object_of_degree_1_an_object_is_created_using_these_parts[0])

@scenario('../features/Object2.feature', 'create object of degree 2')

def test_object_of_degree_2():
    pass

@given("a proof requiring an object to have 10 parts", target_fixture="create_object_of_degree_2_a_proof_requring_an_object_to_have_10_parts")
def object_degree_2_proof(create_object_of_degree_2_a_proof_requiring_an_object_to_have_10_parts_conf):
    return create_object_of_degree_2_a_proof_requiring_an_object_to_have_10_parts_conf

@given("an object of degree 1 referencing this proof", target_fixture="create_object_of_degree_2_an_object_of_degree_1_referencing_this_proof")
def object_degree_2_object_referencing():
    pass

@given("an interpretation of degree 2", target_fixture="create_object_of_degree_2_an_interpretation_of_degree_2")
def object_degree_2_interpretation():
    pass

@given("a context where the parent can be interpreted", target_fixture="create_object_of_degree_2_a_context_where_the_parent_can_be_interpreted")
def object_degree_2_interpretation():
    pass

@given("an object with 10 parts including these parts is created", target_fixture="create_object_of_degree_2_an_object_with_10_parts_including_these_parts_is_created")
def object_degree_2_with_10_parts(create_object_of_degree_2_an_object_with_10_parts_including_these_parts_is_created_conf):
    return create_object_of_degree_2_an_object_with_10_parts_including_these_parts_is_created_conf

@given("an object without 10 parts including these parts is created", target_fixture="create_object_of_degree_2_an_object_without_10_parts_including_these_parts_is_created")
def object_degree_2_without_10_parts(create_object_of_degree_2_an_object_without_10_parts_including_these_parts_is_created_conf):
    return create_object_of_degree_2_an_object_without_10_parts_including_these_parts_is_created_conf

@then("the object with 10 parts can be proved")
def object_degree_2_can_be_proved(create_object_of_degree_2_an_object_with_10_parts_including_these_parts_is_created):
    assert prove(create_object_of_degree_2_an_object_with_10_parts_including_these_parts_is_created)

@then("the object without 10 parts can\'t be proved")
def object_degree_2_cannot_be_proved(create_object_of_degree_2_an_object_without_10_parts_including_these_parts_is_created):
    with pytest.raises(ValueError):
        prove(create_object_of_degree_2_an_object_without_10_parts_including_these_parts_is_created)

"""
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

"""


"""

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