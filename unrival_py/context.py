class Context:

    def __init__(self, read, parse):
        self.read = read
        self.parse = parse

    def interpret_object(self, context_address, interpretations):
        
        context_string = self.read(context_address)
        context_parts = self.parse(context_string)

        for part in context_parts:
            if 'interpretation' in part and part['interpretation'] != '/interpretation':
                continue
            print('will look at: ')
            print(part)
            print('hoping to find: ' + part['address'])
            print('inside of:')
            print(interpretations)
            if 'address' in part and part['address'] in interpretations:
                return part['value']
        return None

