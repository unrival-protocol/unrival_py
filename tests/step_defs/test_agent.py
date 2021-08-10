import pytest
from pytest_bdd import scenario, given, when, then

from unrival_py import *

PROTOCOL = "ipfs"

@scenario('../features/Agent.feature', 'create a whole')

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

@scenario('../features/Agent.feature', 'create agent')

def test_create_agent():
    pass

@given("a private key", target_fixture="agent_private_key")
def use_private_key():
    return 'secret'

@given("an agent with a public key is created using this private key", target_fixture="agent_public_key")
def create_public_key(agent_private_key):
    agent_address = create_agent(agent_private_key)
    object_string = read(agent_address)
    object_parts = parse(object_string)
    public_key = get_part(object_parts, 'public_key')['value']
    return public_key

@then("an unrival agent cannot be created from these parts")
def creation_fails(agent_public_key):
    
        
# @scenario('../features/Agent.feature', 'instance can\'t be proved because it\'s missings some of prototype\'s parts')
