class Agent:
    def create(prototype, public_key):
        print('creating agent')
        parts = [
            {
                'name': 'prototype',
                'type': 'goal',
                'address': prototype,
                'protocol': 'ipfs'
            },
            {
                'name': 'public_key',
                'type': 'public_key',
                'address': public_key,
                'protocol': 'ipfs'
            }
        ]
        return parts

