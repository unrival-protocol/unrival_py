from unrival_py import filter_parts, parse
import pytest

@pytest.mark.unit
def test_filter_parts(create_base_object_parts_containing_these_objects_data_conf):
    parts = parse(create_base_object_parts_containing_these_objects_data_conf)
    interpretations = filter_parts(parts, '/object/interpretation', False)
    for interpretation in interpretations:
        assert 'address' in interpretation
        assert 'protocol' in interpretation
        assert 'interpretation' in interpretation
