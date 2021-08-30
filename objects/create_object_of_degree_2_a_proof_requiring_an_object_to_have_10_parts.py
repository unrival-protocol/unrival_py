#!/usr/bin/env python3
import sys
from unrival_py import *

# address of object to be proved
object_address = sys.argv[1]
print('will prove object at address: ' + object_address)
object_string = read(object_address)
object_parts = parse(object_string)
print(len(object_parts))

assert len(object_parts) == 10
