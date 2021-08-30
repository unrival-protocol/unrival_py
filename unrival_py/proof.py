class Proof:

    def __init__(self, filter_parts, read, parse, interpret_object, get_parent_interpretations, get_context):
        self.filter_parts = filter_parts
        self.interpret_object = interpret_object
        self.read = read
        self.parse = parse
        self.get_parent_interpretations = get_parent_interpretations
        self.get_context = get_context

    def get_proofs(self, object_address):
        """
        Get all proofs an object must satisfy.

        Args:
          object_address (str): address of object to be proved
        Returns:
          list: addresses of all proofs an object must satisfy
        """
        return list(self._get_proofs(object_address, set()))

    def _get_proofs(self, object_address, proofs, object_parts = None):

        object_string = self.read(object_address)
        object_parts = self.parse(object_string)

        # get proofs attached to object
        proofs = proofs.union(self.filter_parts(object_parts, '/proof', True))

        interpretations = self.get_parent_interpretations(object_parts, True)
        context = self.get_context(None, object_parts, True)

        if not context:
            return proofs
        associated_object = self.interpret_object(context, interpretations)
        if associated_object is None:
            return proofs

        return proofs.union(self._get_proofs(associated_object, proofs))
        
