#!/usr/bin/env python3
import sys
from unrival_py import *

# address of object to be proved
object_address = sys.argv[1]
object_string = read(object_address)
object_parts = parse(object_string)

print('Executing animal proof.')

# According to https://www.biologyonline.com/dictionary/animal

assert has_part(object_parts, 'heterotropic', True)
print(f'{object_address} is heterotropic.')
assert has_part(object_parts, 'motile', True)
print(f'{object_address} is motile.')
assert has_part(object_parts, 'has_cell_wall', False)
print(f'{object_address} does not have a cell wall.')
assert has_part(object_parts, 'has_sensory_organs', True)
print(f'{object_address} has sensory organs.')
assert has_part(object_parts, 'grows_from_blastula', True)
print(f'{object_address} grows from a blastula during embryonic development.')
print('Animal proof satisfied.')
