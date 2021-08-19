#!/usr/bin/env python3
import sys
from unrival_py import *

object_address = sys.argv[1]
object_string = read(object_address)
object_parts = parse(object_string)

proof_queue = []

print('Executing namespace proof...')
assert has_part(object_parts, 'namespace', 'object/name')
