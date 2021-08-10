import pytest
from pytest_bdd import scenario, given, when, then

from unrival_py import *

PROTOCOL = "ipfs"

@scenario('../features/Object.feature', 'create a whole')

def test_create_whole():
    pass

@given("a proof", target_fixture="proof")
def a_proof(proof_address):
    return proof_address

@given("a set of parts claiming this proof", target_fixture="parts_satisfying_proof")
def satisfying_parts(proof, parts):
    assert proof in [x['address'] for x in parts]
    return parts

@given("a whole is created from these parts", target_fixture="whole_address")
def create_whole(parts_satisfying_proof):
    whole_hash = create(parts_satisfying_proof, PROTOCOL)
    return whole_hash

@given("it can be read", target_fixture="whole_string")
def read_whole(whole_address):
    print('address: ')
    print(whole_address)    
    whole_string = read(whole_address)
    assert isinstance(whole_string, str)
    print(whole_string)
    return whole_string

@then("it can be parsed")
def parse_whole(whole_string):
    whole_parts = parse(whole_string)
    print(whole_parts)
    assert isinstance(whole_parts, list)

@scenario('../features/Object.feature', 'fail to create a whole')

def test_fail_to_create_whole():
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
