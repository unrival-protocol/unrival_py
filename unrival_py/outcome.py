class Outcome:
    def create(prototype, description):
        print('creating goal')
        parts = [
            {
                'name': 'prototype',
                'type': 'outcome',
                'address': prototype,
                'protocol': 'ipfs'
            },
            {
                'name': 'description',
                'type': 'string',
                'value': description
            }
        ]
        return parts

