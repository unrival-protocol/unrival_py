class Context:

    def __init__(self, read, parse, make_simple_part):
        self.read = read
        self.parse = parse
        self.make_simple_part = make_simple_part

    def interpret_object(self, context_address, interpretation_parts = None, interpretations = None):
        if not interpretation_parts and not interpretations:
            return None
        if not interpretation_parts:
            interpretation_parts = [self.make_simple_part('/interpretation', x, 'ipfs') for x in interpretations]

        context_string = self.read(context_address)
        context_parts = self.parse(context_string)

        for part in context_parts:
            if 'interpretation' in part and part['interpretation'] != '/interpretation':
                continue
            if 'address' in part and part['address'] in interpretation_parts:
                return part['value']


