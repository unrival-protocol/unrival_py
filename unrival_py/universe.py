class Universe:

    def __init__(self, read, parse):
        self.read = read
        self.parse = parse

    def interpret_object(self, universe_address, interpretations):

        universe_string = self.read(universe_address)
        universe_parts = self.parse(universe_string)

        for part in universe_parts:
            if 'interpretation' in part and part['interpretation'] != '/object/interpretation':
                continue
            if 'address' in part and part['address'] in interpretations:
                return part['value']
        return None

