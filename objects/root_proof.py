#!/usr/bin/env python3
import sys
from unrival_py import *

# address of object to be proved
object_address = sys.argv[1]

# universe in which interpretations should be applied
universe_address = sys.argv[2]

object_string = read(object_address)
universe_string = read(universe_address)
# convert data at address to python list
object_parts = parse(object_string)
universe_parts = parse(universe_string)
proof_queue = []

print('Executing root proof...')

proofs = get_parts(object_parts, '/object/proof')

for proof_hash in proofs:
    proof_queue.append(proof_hash)

print('Own proofs: ')
print(proofs)

namespaces = get_parts(object_parts, '/object/namespace')
for namespace in namespaces:
    print(namespace)
    raise Exception
    possible_interpretations = get_parts(universe_parts, '/object/interpretation')
    # look up interpretation for namespace

if has_prototype(object_parts):
    print('Object has an attached prototype - will try to inherit.')
    prototype_parts = get_parts(object_parts['prototype'])
    if not prototype_is_subset_of_instance():
        print('the prototype parts are not a subset of the instance')
        raise Exception
    while has_prototype(prototype_parts):
        prototype_proof = prototype_parts['proof']
        proof_queue.append(prototype_proof)
        prototype_parts = get_parts(prototype_parts['prototype'])
else:
    print('Object has no attached prototype - will try to create a simple object.')

for proof_address in proof_queue:
    # now apply each proof to the original object address
    print(f"Trying to prove object at address: {object_address} using proof at address: {proof_address}")
    prove(object_address, proof_address, universe_address)
