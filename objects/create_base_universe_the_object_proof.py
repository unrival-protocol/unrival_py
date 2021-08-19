#!/usr/bin/env python3
import sys
from unrival_py import *

object_address = sys.argv[1]
object_string = read(object_address)
object_parts = parse(object_string)

print('Executing object proof...')
assert has_part(object_parts, 'namespace', 'object')
assert has_proof(object_parts, 'QmQBr71HhzUsD3iZK2swBK3orb9x9Em3oSYcm9YHqcMEwT')
