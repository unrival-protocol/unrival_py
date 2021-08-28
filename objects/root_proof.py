#!/usr/bin/env python3
import sys
from unrival_py import *

# address of object to be proved
object_address = sys.argv[1]
print(object_address + ' from root')
# context in which interpretations should be applied

print('Executing root proof...')

proofs = get_proofs(object_address)
print('proofs are:')

for proof_address in proofs:
    # now apply each proof to the original object address
    prove(object_address, None, proof_address)
