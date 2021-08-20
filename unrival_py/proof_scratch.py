
"""
proofs = filter_parts(object_parts, '/object/proof')

for proof_hash in proofs:
    proof_queue.append(proof_hash)

namespace_parts = filter_parts(object_parts, '/object/namespace', False)

# levels 1..n: proofs referenced by ancestors

    """

    """
while namespaces:
    head = namespaces[0]
    tail = namespaces[1:]
    # get interpretations that we can use to look up parent objects
    interpretations = get_interpretations(universe_parts, head, True)
    # look up object address in universe
    object_address = lookup_object_address(interpretations, universe_parts)
    # get proofs from object
    object_string = read(object_address)
    object_parts = parse(object_string)
    proof_addresses = filter_parts(object_parts, '/object/proof')
    proof_queue += proof_addresses
    namespaces = namespaces[1:]

    possible_interpretations = filter_parts(universe_parts, '/object/interpretation')
    # look up interpretation for namespace

if has_prototype(object_parts):
    print('Object has an attached prototype - will try to inherit.')
    prototype_parts = filter_parts(object_parts['prototype'])
    if not prototype_is_subset_of_instance():
        print('the prototype parts are not a subset of the instance')
        raise Exception
    while has_prototype(prototype_parts):
        prototype_proof = prototype_parts['proof']
        proof_queue.append(prototype_proof)
        prototype_parts = filter_parts(prototype_parts['prototype'])
else:
    print('Object has no attached prototype - will try to create a simple object.')
"""
