#!/usr/bin/env python3
import sys
from unrival_py import *

# address of object to be proved
object_address = sys.argv[1]
object_string = read(object_address)
object_parts = parse(object_string)

print('Executing dog proof.')

# non-authoritative definition


assert has_part(object_parts, 'snout', 'long')
print(f'{object_address} has a long snout.')
assert has_part(object_parts, 'claws', 'non-retractable')
print(f'{object_address} has non-retractable claws.')
assert has_part(object_parts, 'bark', True)
print(f'{object_address} barks.')
assert has_part(object_parts, 'attached_to_man', True)
print(f'{object_address} is attached to man.')
print('Dog proof satisfied.')
