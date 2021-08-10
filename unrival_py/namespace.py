class Namespace:
    def create(prototype, outcomes):
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

