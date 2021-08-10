#!/usr/bin/env python3
"""interface with Unrival objects using Python"""
from subprocess import PIPE, run, call
from .goal import Goal
from .agent import Agent
import re
import json
import sys

__version__ = "0.0.3"

ROOT_PROOF_ADDRESS = 'QmYXrp55rLNsA321QFGowjofTBpmGByxntzKLT81Sdbq8j'

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

def prove(parts, proof_address = None):
    if proof_address is None:
        proof_string = read(ROOT_PROOF_ADDRESS)
    else:
        proof_string = read(proof_address)
    result = execute(proof_string, parts)
    assert result.returncode == 0

def execute(command_string, address):
    execution = run([sys.executable, "-c", command_string, address])
    return execution

def get_prototype(parts):
    parts = json.loads(json.dumps(parts))
    for row in parts:
        if row['name'] == 'prototype':
            return row['address']
    return None

def get_proof(parts):
    parts = json.loads(json.dumps(parts))
    for row in parts:
        if row['name'] == 'proof':
            return row['address']
    return None

def get_parts(parts, object_type):
    target_parts = []
    all_parts = json.loads(json.dumps(parts))
    for row in all_parts:
        if row['type'] == object_type:
            target_parts.append(row['address'])
    return target_parts

def get_part(parts, part_name):
    all_parts = json.loads(json.dumps(parts))
    for row in all_parts:
        if row['name'] == part_name:
            return row
    return None

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
    command = f"echo \"{string}\" | {protocol} add"
    result = run(command, stdout=PIPE, stderr=PIPE, u_eniversal_newlines=True, shell=True)
    address_rx = re.compile(r'added (.*?) .*')
    address_matches = address_rx.findall(result.stdout)
    return address_matches[0]

def create(parts, protocol = 'ipfs'):
    #parts_string = json.dumps(parts)
    parts_string = str(parts).replace("'", '\\"')
    address = store(parts_string, protocol)
    try:
        prove(address)
        return address
    except Exception as e:
        raise ValueError

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
