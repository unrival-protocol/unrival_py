#!/usr/bin/env python3
"""interface with Unrival objects using Python"""

from subprocess import PIPE, run, call
from .goal import Goal
from .agent import Agent
from .proof import Proof
from .context import Context
from .interpretation import Interpretation
import re
import json
import sys

__version__ = "0.0.3"

def get_root_proof_address():
    with open('./objects/root_proof.py') as f:
        contents = f.read()
        address = store(contents, 'ipfs')
        return address

def get_empty_context_address():
    with open('./objects/empty_context.json') as f:
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

def prove(object_address, object_parts = None, proof_address = None):
    """
    Ensure that all proofs referenced by an object and its ancestors are satisfied by that object.

    Given an object address, return exit code 0 if object's proofs were satisfied, 1 otherwise.

    Args:
      object_address (str): address of object being proved
      proof_address (str): proof to be applied to object
    Returns:
      bool: proof failed or succeeded
    """

    if object_parts is None:
        object_string = read(object_address)
        object_parts = parse(object_string)
    print(f'Attempting proof of object at address: {object_address}')

    if proof_address is None:
        # the root proof will be applied, which requires all ancestor proofs to be satisfied
        proof_string = read(get_root_proof_address())
    else:
        # only the proof supplied will be applied
        proof_string = read(proof_address)

    result = execute(proof_string, object_address)
    print(result)
    assert result.returncode == 0
    return True


def filter_parts(parts, interpretation, address=False):
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
            if address and row['address']:
                filtered_parts.append(row['address'])
            else:
                filtered_parts.append(row)
    return filtered_parts

def get_context(object_address = None, object_parts = None, address=False):
    """
    Get the 
    """
    if not object_address and not object_parts:
        raise ValueError('In order to get context, either object address or parts must be provided.')
    if not object_parts:
        object_string = read(object_address)
        object_parts = parse(object_string)
    try:
        context = next(filter(lambda x : x['interpretation'] == '/context', object_parts))
    except:
        return None
    if address:
        return context['address']
    else:
        return [context]

def get_interpretations(parts, address=False, filter_valued=False):
    interpretations = filter_parts(parts, '/interpretation', address)
    if not filter_valued:
        return interpretations
    return list(filter(lambda x : 'value' not in x, interpretations))


def get_parent_interpretations(parts, filter_valued=False, protocol = 'ipfs'):
    result = []
    for part in parts:
        if 'interpretation' in part and part['interpretation'] == '/interpretation':
            if filter_valued and 'value' in part:
                continue
            interpretation_address = part['address']
            interpretation_string = read(interpretation_address)
            print('int string: ' + interpretation_string)
            arr = interpretation_string.split('/')
            if len(arr) > 2:
                arr.pop()
                parent_address = store('/'.join(arr), protocol)
                result.append(parent_address)
    return result

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

def execute(command_string, object_address):
    execution = run([sys.executable, "-c", command_string, object_address])
    return execution

def has_part(parts, part_key, part_value=None):
    if part_value:
        return any([part_key in part and part[part_key] == part_value for part in parts])
    return any([part_key in part for part in parts])

def store(string, protocol):
    string = string.replace('"', '\\"').strip()
    command = f"echo \"{string}\" | {protocol} add"
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    address_rx = re.compile(r'added (.*?) .*')
    address_matches = address_rx.findall(result.stdout)
    return address_matches[0]

def create(parts, protocol):
    """
    Create an object

    Args:
      parts (list): A list of parts (objects) referenced by the object
      protocol (str): The protocol to be used for storing the object
    Returns:
      tuple: A tuple containing 1. the address of the created object 2. the address of a context in which the newly created object can be interpreted
    """

    object_address = store(json.dumps(parts), protocol)

    context = get_context(None, parts, False)
    interpretation_addresses = filter_parts(parts, '/interpretation', True)

    # interpretation parts below refers to interpretations that need to be assigned values in a new context, so valued interpretations are not included

    interpretation_parts = get_interpretations(parts, False, True)
    if context is None:
        if any([len(read(x).split('/')) > 2 for x in interpretation_addresses]):
            print('If object of degree > 1 references interpretation, it must also reference a context in which it can be interpreted.')
            raise Exception
        context_address = get_empty_context_address()
        context = parse(read(context_address))
    parts.append(context)

    if len(interpretation_parts):
        # set new context, since current context can't interpret new object
        context = create_context(context, interpretation_parts, object_address, protocol)
    prove(object_address)
    return (object_address, context)

def create_context(context_parts, interpretations, object_address, protocol):
    """
    Create a context.

    Args:
      parents (list): parent context
      interpretations (list): interpretations to be added to parent, or result of merge of parents in case creation is a merge
      protocol (str): the protocol to use for storing the context
    Returns:
      str: the address of the created context
    """
    for interpretation in interpretations:
        interpretation['value'] = object_address

    # an assertion may not be added to a context
    assert not (len(filter_parts(context_parts, '/claim')) or len(filter_parts(context_parts, '/proof')))

    context_parts = context_parts + interpretations
    # will trigger recursive call of `create`, which will result in infinite recursion if context has proof or claim parts
    new_context_address, parent_address = create(context_parts, protocol)
    return new_context_address

def resolve_context(address, protocol):
    print('resolve called')
    result = {}
    parts = parse(read(address, protocol))
    for part in parts:
        if 'value' in part and part['value'] and part['interpretation'] == '/interpretation':
            interpretation = read(part['address'])
            result[interpretation] = part['value']
    print('tried to resolve the context')
    print(result)
    return result

def merge_contexts(contexts):
    parts = contexts
    merged_interpretations = set()
    for context in contexts:
        context_address = context['address']
        contextparts = parse(read(context_address))
        interpretations = filter_parts(context_parts)


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

def interpret_object(context_address, interpretation_parts = None, interpretations = None):
    return Context(read, parse, make_simple_part).interpret_object(context_address, interpretation_parts, interpretations)

def get_proofs(object_address):
    return Proof(filter_parts, read, parse, interpret_object, get_parent_interpretations, get_context).get_proofs(object_address)

def make_simple_part(interpretation, string, protocol):
    part = {}
    address = store(string, protocol)
    part['address'] = address
    part['protocol'] = protocol
    part['interpretation'] = interpretation
    return part
