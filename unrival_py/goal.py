class Goal:
    def create(prototype, outcome, agent, namespace):
        print('creating goal')
        parts = [
            {
                'name': 'prototype',
                'type': 'goal',
                'address': prototype,
                'protocol': 'ipfs'
            },
            {
                'name': 'outcome',
                'type': 'outcome',
                'address': outcome,
                'protocol': 'ipfs'
            },
            {
                'name': 'agent',
                'type': 'agent',
                'address': agent,
                'protocol': 'ipfs'
            },
            {
                'name': 'namespace',
                'type': 'namespace',
                'address': namespace,
                'protocol': 'ipfs'
            }
        ]
        return parts

