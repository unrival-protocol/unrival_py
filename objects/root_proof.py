#!/usr/bin/env python3
import sys
from unrival_py import *

# address of object to be proved
object_address = sys.argv[1]
# universe in which interpretations should be applied
universe_address = sys.argv[2]

print('Executing root proof...')

proofs = get_proofs(object_address, universe_address)

for proof_address in proofs:
    # now apply each proof to the original object address
    prove(object_address, universe_address, None, proof_address)
