class Proof:

    def __init__(self, filter_parts, read, parse, lookup_object):
        self.filter_parts = filter_parts
        self.lookup_object = lookup_object
        self.read = read
        self.parse = parse

    def get_proofs(self, object_address, universe_address):
        """
        Get all proofs an object must satisfy.

        Args:
          object_address (str): address of object to be proved
        Returns:
          list: addresses of all proofs an object must satisfy
        """
        return self._get_proofs(object_address, set(), universe_address, 0)

    def _get_proofs(self, object_address, proofs, universe_address, iteration):
        print('===================')
        print('iteration: ' + str(iteration))
        print('===================')
        print('object address: ' + object_address)
        print('===================')
        print('proofs: ' + str(proofs))
        print('===================')
        print('universe address: ' + universe_address)
        print('===================')
        object_string = self.read(object_address)
        object_parts = self.parse(object_string)
        # add own proofs
        proofs = proofs.union(self.filter_parts(object_parts, '/object/proof'))
        # get ancestor proofs
        namespaces = self.filter_parts(object_parts, '/object/namespace')
        print('namespaces: ' + str(namespaces))
        if not namespaces:
            return proofs
        for ns in namespaces:
            interpretations = self.filter_parts(object_parts, '/object/interpretation')
            associated_object = self.lookup_object(universe_address, interpretations)
            print('we found it')
            print(associated_object)
            #print(f'the object associated with: universe {universe_address}')
            #print('interpretations: ' + str(interpretations))
            #print(associated_object)
            proofs = proofs.union(self._get_proofs(associated_object, proofs, universe_address, iteration + 1))
        return proofs
