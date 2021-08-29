#!/usr/bin/env python3
import sys
from unrival_py import *

# address of object to be proved
object_address = sys.argv[1]
object_string = read(object_address)
object_parts = parse(object_string)

print('Executing mammal proof.')

# According to the 7 characteristics of mammals found here: https://www.ck12.org/biology/mammal-overview/lesson/Mammal-Characteristics-MS-LS/

assert has_part(object_parts, 'sweat_glands', True)
print(f'{object_address} has sweat glands.')
assert has_part(object_parts, 'mammary_glands', True)
print(f'{object_address} has mammary glands.')
assert has_part(object_parts, 'hair', True) or has_part(object_parts, 'fur', True)
print(f'{object_address} has hair or fur.')
assert has_part(object_parts, 'number_of_heart_chambers', 4)
print(f'{object_address} has four heart chambers.')
assert has_part(object_parts, 'number_of_middle_ear_bones', 3)
print(f'{object_address} has four middle ear bones.')
assert has_part(object_parts, 'neocortex', True)
print(f'{object_address} has a neocortex.')
assert has_part(object_parts, 'teeth', 'specialized')
print(f'{object_address} has specialized teeth.')
print('Mammal proof satisfied.')
