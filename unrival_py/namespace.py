class Namespace:
    def __init__(self):
        pass
    def create(self, prototype, outcomes):
        print('creating goal')
        parts = [
            {
                'name': 'prototype',
                'type': 'namespace',
                'address': prototype,
                'protocol': 'ipfs'
            }
        ]
        for outcome in outcomes:
            outcome = {
                'name': outcome['name'],
                'type': 'outcome',
                'address': outcome['address'],
                'protocol': outcome['protocol']
            }
            parts.append(outcome)
        return parts
