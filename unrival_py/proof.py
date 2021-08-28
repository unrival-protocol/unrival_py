class Proof:

    def __init__(self, filter_parts, read, parse, interpret_object, get_interpretations, get_context):
        self.filter_parts = filter_parts
        self.interpret_object = interpret_object
        self.read = read
        self.parse = parse
        self.get_interpretations = get_interpretations
        self.get_context = get_context

    def get_proofs(self, object_address):
        """
        Get all proofs an object must satisfy.

        Args:
          object_address (str): address of object to be proved
        Returns:
          list: addresses of all proofs an object must satisfy
        """
        return self._get_proofs(object_address, set(), 0)

    def _get_proofs(self, object_address, proofs, object_parts = None, iteration = 0):
        print('===================')
        print('iteration: ' + str(iteration))
        print('===================')
        print('object address: ' + object_address)
        print('===================')
        print('proofs: ' + str(proofs))
        print('===================')
        if iteration == 4:
            print('too much recursion')
            raise ValueError

        object_string = self.read(object_address)
        object_parts = self.parse(object_string)
        proofs = proofs.union(self.filter_parts(object_parts, '/proof', True))
        interpretations = self.get_interpretations(object_parts, True, True)
        context = self.get_context(None, object_parts, True)
        if not context:
            return proofs
        associated_object = self.interpret_object(context, interpretations)
        if associated_object is None:
            print('No object found associated with ' + object_address)
            return proofs
        proofs = proofs.union(self._get_proofs(associated_object, proofs, context_address, iteration+1))
        print('after the recursive call, proofs is equal to: ')
        print(proofs)
        return list(proofs)
