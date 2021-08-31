import pytest
from pytest_bdd import scenario, given, when, then

from unrival_py import *

@scenario('../features/Object.feature', 'create object of degree 0')
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


@scenario('../features/Object.feature', 'create object of degree 1')
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

@scenario('../features/Object.feature', 'create object of degree 2')

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
    with pytest.raises(AssertionError):
        prove(create_object_of_degree_2_an_object_without_10_parts_including_these_parts_is_created)
