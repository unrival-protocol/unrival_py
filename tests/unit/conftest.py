import pytest
from unrival_py import store
from pytest_bdd import given
import glob
from pathlib import Path

# shared steps
@given("a protocol", target_fixture="a_protocol")
def ipfs():
    return 'ipfs'

# add step fixtures to global namespace
def generate_fixture(path_obj):
    """
    generates a fixture like the following:

    @pytest.fixture()
    def create_base_universe_a_universe_only_containing_the_base_namespace_conf():
        return 'QmcRFfLscQayMdkZ1KT878GZakCJcRfLcaJhaNYEstisNj'
    """
    extension = path_obj.suffix
    @pytest.fixture(scope='module')
    def step():
        with open(path_obj.resolve()) as f:
            data = f.read()
            if path_obj.stem.split('-')[-1] == 'data':
                address = store(data, 'ipfs')
                return address
            return data
    return step

def inject_fixture(name, path_obj):
    print(f'Injecting fixture: {name}.')
    globals()[name] = generate_fixture(path_obj)

# create fixtures from object files
object_files = glob.glob("objects/*")

for f in object_files:
    path_obj = Path(f)
    fixture_name = path_obj.stem + '_conf' # conf is added to specify fixture is loaded from conftest file
    inject_fixture(fixture_name, path_obj)