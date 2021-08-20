#!/usr/bin/env python3
"""interface with Unrival objects using Python"""

from subprocess import PIPE, run, call
from .goal import Goal
from .agent import Agent
from .proof import Proof
from .universe import Universe
import re
import json
import sys

# initialize classes


__version__ = "0.0.3"

def get_root_proof_address():
    with open('./objects/root_proof.py') as f:
        contents = f.read()
        address = store(contents, 'ipfs')
        return address

def read(address, protocol = 'ipfs'):
    if protocol == 'ipfs':
        try:
            command = ['ipfs', 'cat', address]
            result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            output = result.stdout
            return output.strip()
        except Exception:
            raise Exception
    else:
        # TODO add support for other protocols, e.g. DAT
        return NotImplementedError

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
    print(universe_address)
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
    return True


def filter_parts(parts, interpretation, address=True):
    """
    Filter parts by interpretation.  Maps to addresses by default; set address to false to map to parts.

    Args:
      parts (list): A list of parts (object references)
      interpretation (str): The interpretation to filter by
      address (bool): Whether output should be parts or parts mapped to addresses (default)
    Returns:
      list: parts or addresses filtered by interpretation
    """
    filtered_parts = []
    all_parts = json.loads(json.dumps(parts))
    for row in all_parts:
        if 'interpretation' in row and row['interpretation'] == interpretation:
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

def execute(command_string, object_address, universe_address):
    execution = run([sys.executable, "-c", command_string, object_address, universe_address])
    return execution

def has_part(parts, part_key, part_value):
    return any([part[key] == part_value for part in parts])

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
        interpretation_parts = filter_parts(parts, '/object/interpretation', False)
        if (proofs or claims) and not interpretation_parts:
            print('Referencing proofs or claims in an object requires an interpretation to be provided.')
            raise ValueError

        object_address = store(json.dumps(parts), protocol)

        if (proofs or claims):
            # an object necessitates universe expansion if it makes a objective/subjective proof/claim about itself -- i.e. has a proof or a claim
            universe_address = create_universe([universe_address], interpretation_parts, object_address, protocol)
            #print('a newly created universe!')
            #print(universe_address)

        prove(object_address, universe_address)
        return (object_address, universe_address)

    except Exception as e:
        print(e)
        raise ValueError

def create_universe(parents, interpretations, object_address, protocol):
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
    # TODO move this condition to the universe proof
    
    # assign value to interpretations
    valued_interpretations = []
    for interpretation in interpretations:
        interpretation['value'] = object_address
        valued_interpretations.append(interpretation)

    for universe in parents:
        universe_string = read(universe)
        universe_parts = parse(universe_string)
        # TODO add test to make sure no claims or proofs in universe instance
        # TODO add to FAQs - why can't universes have claims?
        assert not (len(filter_parts(universe_parts, '/object/claim')) or len(filter_parts(universe_parts, '/object/proof')))

    if len(parents) == 1:
        parent_string = read(parents[0])
        parent_parts = parse(parent_string)
        universe_parts = parent_parts + valued_interpretations
        # will trigger recursive call of `create`, which will result in infinite recursion if universe has proof or claim parts
        new_universe_address, parent_address = create(universe_parts, parents[0], protocol)
        print('THE NEW UNIVERSE:')
        print(new_universe_address)
        print('THE PARENT ADDRESS:')
        print(parent_address)
        return new_universe_address
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

def lookup_object(universe_address, interpretations):
    return Universe(read, parse).lookup_object(universe_address, interpretations)

def get_proofs(object_address, universe_address):
    return Proof(filter_parts, read, parse, lookup_object).get_proofs(object_address, universe_address)
