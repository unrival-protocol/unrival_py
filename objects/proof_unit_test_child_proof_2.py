#!/usr/bin/env python3
import sys
from unrival_py import *

# address of object to be proved
object_address = sys.argv[1]
object_string = read(object_address)
object_parts = parse(object_string)

print('Executing dalmation proof.')

# non-authoritative definition

assert has_part(object_parts, 'hyper', True)
print(f'{object_address} is hyper.')
print('Dalmation proof 2/2 satisfied')
