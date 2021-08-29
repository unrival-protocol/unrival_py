#!/usr/bin/env python3
import sys
from unrival_py import *

# address of object to be proved
object_address = sys.argv[1]
object_string = read(object_address)
object_parts = parse(object_string)

assert len(object_parts) == 10
