#!/usr/bin/env python3
"""interface with Unrival objects using Python"""

from subprocess import PIPE, run, call
from .goal import Goal
from .agent import Agent
import re
import json
import sys

__version__ = "0.0.3"

def get_root_proof_address():
    with open('./objects/root_proof.py') as f:
        contents = f.read()
        address = store(contents, 'ipfs')
        return address

def read(address):
    try:
        command = ['ipfs', 'cat', address]
        result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        output = result.stdout
        return output.strip()
    except Exception:
        raise Exception

def parse(object_string):
    return json.loads(object_string)

def prove(object_address, universe_address, object_parts = None, proof_address = None):
    """
    Ensure that all proofs referenced by an object and its ancestors are satisfied by that object.

    Given an object address, return exit code 0 if object's proofs were satisfied, 1 otherwise.

    Args:
      object_address (str): address of object being proved
      object_parts (list): list of objects referenced by object
      proof_address (str): proof to be applied to object
    Returns:
      bool: proof failed or succeeded
    """
    print(f'Attempting to prove object at address: {object_address} within universe at address: {universe_address}')
    if object_parts is None:
        object_string = read(object_address)
        object_parts = parse(object_string)

    if proof_address is None:
        proof_string = read(get_root_proof_address())
    else:
        proof_string = read(proof_address)

    result = execute(proof_string, object_address, universe_address)
    assert result.returncode == 0

def prove_parts(parts, proof_address = None):
    if proof_address is None:
        proof_string = read(get_root_proof_address())
    else:
        proof_string = read(proof_address)
    result = execute(proof_string, object_address)
    assert result.returncode == 0

def execute(command_string, object_address, universe_address):
    execution = run([sys.executable, "-c", command_string, object_address, universe_address])
    return execution

def get_prototype(parts):
    parts = json.loads(json.dumps(parts))
    for row in parts:
        if row['label'] == 'prototype':
            return row['address']
    return None

def get_proof(parts):
    parts = json.loads(json.dumps(parts))
    for row in parts:
        if row['label'] == 'proof':
            return row['address']
    return None

def filter_parts(parts, namespace, address=True):
    """
    Filter parts by namespace.  Maps to addresses by default; set address to false to map to parts.

    Args:
      parts (list): A list of parts (object references)
      namespace (str): The namespace to filter by
      address (bool): Whether output should be addresses (default) or parts
    Returns:
      list: parts or addresses filtered by namespace
    """
    filtered_parts = []
    all_parts = json.loads(json.dumps(parts))
    for row in all_parts:
        if row['namespace'] == namespace:
            if address:
                filtered_parts.append(row['address'])
            else:
                filtered_parts.append(row)
    return filtered_parts

def get_part(parts, part_label):
    """
    Gets a part by its label.  Since part labels are unique, this uniquely determines a part.

    Args:
      parts (list):
      part_label (str): Label of part to return
    Returns:
      dict: Part having part_label
    """
    all_parts = json.loads(json.dumps(parts))
    for row in all_parts:
        if row['label'] == part_label:
            return row
    return None

def get_parents(parts):
    parts = json.loads(json.dumps(parts))
    parents = []
    for row in parts:
        if row['namespace'] == 'object/namespace' and row['prototype'] == True:
            parents.append(row['address'])
    return parents

def has_prototype(parts):
    return get_prototype(parts) is not None

def has_part(parts, part_key, part_value):
    return any([part[key] == part_value for part in parts])

def has_proof(parts, address=None):
    proof = get_proof(parts)

    if address is not None:
        return get_proof(parts) == address

    return get_proof(parts) is not None

def prototype_is_subset_of_instance():
    pass

def store(string, protocol):
    string = string.replace('"', '\\"')
    command = f"echo \"{string}\" | {protocol} add"
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    address_rx = re.compile(r'added (.*?) .*')
    address_matches = address_rx.findall(result.stdout)
    return address_matches[0]

def create(parts, universe_address, protocol):
    """
    Create an object

    Args:
      parts (list): A list of parts (objects) referenced by the object
      universe_address (str): The universe in which the object can be proved
      protocol (str): The protocol to be used for storing the object
    Returns:
      tuple: A tuple containing 1. the address of the created object 2. the address of a universe in which the newly created object can be interpreted
    """
    try:
        proofs = filter_parts(parts, '/object/proof')
        claims = filter_parts(parts, '/object/claim')
        interpretation_parts = filter_parts(parts, '/object/interpretation', True)

        if (proofs or claims) and not interpretation_parts:
            print('Referencing proofs or claims in an object requires an interpretation to be provided.')
            raise ValueError

        object_address = store(json.dumps(parts), protocol)

        if (proofs or claims):
            # an object necessitates universe expansion if it makes a objective/subjective proof/claim about itself -- i.e. has a proof or a claim
            universe_address = create_universe([universe_address], interpretation_parts, protocol)

        prove(object_address, universe_address)

        return (object_address, universe_address)

    except Exception as e:
        print(e)
        raise ValueError

def create_universe(parents, interpretations, protocol):
    """
    Create a universe.
    If count of parents > 1, then the universe being created is the result of a merge.

    Args:
      parents (list): parent universes
      interpretations (list): interpretations to be added to parent, or result of merge of parents in case creation is a merge
      protocol (str): the protocol to use for storing the universe
    Returns:
      str: the address of the created universe
    """
    # no subjective or objective claims may be made about a universe
    for universe in parents:
        universe_string = read(universe)
        universe_parts = parse(universe_string)
        # TODO add test to make sure no claims or proofs in universe instance
        # TODO add to FAQs - why can't universes have claims?
        assert not (len(filter_parts(universe_parts, '/object/claim')) or len(filter_parts(universe_parts, '/object/proof')))

    if len(parents) == 1:
        universe_parts = parents + interpretations
        create(universe_parts, parents[0], protocol)
        # TODO figure out what to create here!!!
        raise NotImplementedError
    else:
        # TODO add scenarios for merging universes
        raise NotImplementedError

def create_agent(prototype, public_key):
    parts = Agent.create(prototype, public_key)
    address = store(str(parts).replace("'", '\\"'))
    return address

def create_namespace(prototype, outcomes):
    parts = Namespace.create(prototype, outcomes)
    address = store(str(parts).replace("'", '\\"'))
    return address

def create_goal(prototype, outcome, agent, namespace):
    parts = Goal.create(outcome, agent, namespace)
    address = store(str(parts).replace("'", '\\"'))
    return address

def create_outcome(prototype, description):
    parts = Outcome.create(prototype, description)
    address = store(str(parts).replace("'", '\\"'))
    return address

