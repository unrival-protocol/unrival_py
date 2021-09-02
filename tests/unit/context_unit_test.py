from unrival_py import resolve_context, create, make_simple_part, create_context, parse
import pytest

@pytest.mark.unit
def test_resolve_context(
        context_unit_test_interpretation_1_data_conf,
        empty_context_data_conf,
):
    context_unit_test_interpretation_1_data_conf = context_unit_test_interpretation_1_data_conf.strip()
    # since we won't need to read the values of the interpretations, there's no need to create real addresses

    value = 'some value'
    interpretation_1 = make_simple_part('/interpretation', context_unit_test_interpretation_1_data_conf, 'ipfs')
    context_address = create_context(parse(empty_context_data_conf), [interpretation_1], value, 'ipfs')
    resolved_context = resolve_context(context_address, 'ipfs')
    assert resolved_context[context_unit_test_interpretation_1_data_conf] == value
