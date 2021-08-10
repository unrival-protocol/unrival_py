import pytest

@pytest.fixture()
def proof_address():
    return "QmVvzZG1HvFTB2Z8BkPcRwy2Dn1WV3ZpNASbiCSjeCsJGS"

@pytest.fixture()
def a_namespace_address():
    return ''

@pytest.fixture()
def outcomes_list():
    return ''


def root_level_namespace_proof():
    return 'QmXhx5ySSV4wff2w1cZ9axR8nvaxvgZHZwdhCcPMaHhSFh'

@pytest.fixture()
def parts():
    return [
         {
            "name": "proof",
            "type": "proof",
            "protocol": "ipfs",
            "address": "QmVvzZG1HvFTB2Z8BkPcRwy2Dn1WV3ZpNASbiCSjeCsJGS"
         }
    ]

@pytest.fixture()
def insufficient_parts():
    return [
         {
            "name": "proof",
            "type": "proof",
            "protocol": "ipfs",
            "address": "QmVvzZG1HvFTB2Z8BkPcRwy2Dn1WV3ZpNASbiCSjeCsJGS"
         },
         {
            "name": "creator",
            "type": "agent",
            "protocol": "ipfs",
            "address": "some_address"
         },
         {
            "name": "subscriber",
            "type": "agent",
            "protocol": "ipfs",
            "address": "some_other_address"
         }
    ]

@pytest.fixture()
def outcome_address():
    return 'q2lk3j23kl'


@pytest.fixture()
def outcome_prototype():
    return ''

@pytest.fixture()
def namespace_address():
    return 'awklefjklwefjw'

@pytest.fixture()
def agent_address():
    return 'lakjeflk23jfkljwe'
