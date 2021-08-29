from unrival_py import filter_parts, parse
import pytest

@pytest.mark.unit
def test_filter_parts(filter_unit_test_filter_parts_data_conf):
    parts = parse(filter_unit_test_filter_parts_data_conf)
    interpretations = filter_parts(parts, '/interpretation', False)
    for interpretation in interpretations:
        assert 'address' in interpretation
        assert 'protocol' in interpretation
        assert interpretation['interpretation'] == '/interpretation'
