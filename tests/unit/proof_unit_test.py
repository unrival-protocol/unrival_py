from unrival_py import get_proofs, make_simple_part, create, parse
import pytest

@pytest.mark.unit
def test_get_proofs(
        proof_unit_test_great_grandparent_proof_data_conf, proof_unit_test_great_grandparent_proof_conf,
        proof_unit_test_grandparent_proof_data_conf, proof_unit_test_grandparent_proof_conf,
        proof_unit_test_parent_proof_data_conf, proof_unit_test_parent_proof_conf,
        proof_unit_test_child_proof_1_data_conf, proof_unit_test_child_proof_1_conf,
        proof_unit_test_child_proof_2_data_conf, proof_unit_test_child_proof_2_conf,
        proof_unit_test_animal_parts_data_conf,
        proof_unit_test_mammal_parts_data_conf,
        proof_unit_test_dog_parts_data_conf,
        proof_unit_test_dalmation_parts_data_conf
):
    great_grandparent_interpretation = make_simple_part('/interpretation', '/animal', 'ipfs')
    great_grandparent_proof = make_simple_part('/proof', proof_unit_test_great_grandparent_proof_data_conf, 'ipfs')
    great_grandparent_parts = [great_grandparent_interpretation, great_grandparent_proof] + parse(proof_unit_test_animal_parts_data_conf)
    great_grandparent_object, great_grandparent_context = create(great_grandparent_parts, 'ipfs')
    grandparent_interpretation = make_simple_part('/interpretation', '/animal/mammal', 'ipfs')
    grandparent_proof = make_simple_part('/proof', proof_unit_test_grandparent_proof_data_conf, 'ipfs')
    grandparent_parts = [
        grandparent_interpretation, grandparent_proof,
        {
            'interpretation': '/context',
            'address': great_grandparent_context,
            'protocol': 'ipfs'
        }
    ] + parse(proof_unit_test_mammal_parts_data_conf) + parse(proof_unit_test_animal_parts_data_conf)
    # creating the 
    grandparent_object, grandparent_context = create(grandparent_parts, 'ipfs')

    parent_interpretation = make_simple_part('/interpretation', '/animal/mammal/dog', 'ipfs')
    parent_proof = make_simple_part('/proof', proof_unit_test_parent_proof_data_conf, 'ipfs')
    parent_parts = [
        parent_interpretation,
        parent_proof,
        {
            'interpretation': '/context',
            'address': grandparent_context,
            'protocol': 'ipfs'
        }
    ] + parse(proof_unit_test_dog_parts_data_conf) + parse(proof_unit_test_mammal_parts_data_conf) + parse(proof_unit_test_animal_parts_data_conf)
    parent_object, parent_context = create(parent_parts, 'ipfs')
    child_interpretation = make_simple_part('/interpretation', '/animal/mammal/dog/dalmation', 'ipfs')
    child_proof_1_conf = make_simple_part('/proof', proof_unit_test_child_proof_1_data_conf, 'ipfs')
    child_proof_2 = make_simple_part('/proof', proof_unit_test_child_proof_2_data_conf, 'ipfs')
    child_parts = [
        child_proof_1_conf,
        child_proof_2,
        child_interpretation,
        {
            'interpretation': '/context',
            'address': parent_context,
            'protocol': 'ipfs'
        }
    ] + parse(proof_unit_test_dalmation_parts_data_conf) + parse(proof_unit_test_dog_parts_data_conf) + parse(proof_unit_test_mammal_parts_data_conf) + parse(proof_unit_test_animal_parts_data_conf)
    child_object, child_context = create(child_parts, 'ipfs')
    print('the child context is: ' + child_context)

    proofs_child_must_satisfy = [
        proof_unit_test_great_grandparent_proof_conf,
        proof_unit_test_grandparent_proof_conf,
        proof_unit_test_parent_proof_conf,
        proof_unit_test_child_proof_1_conf,
        proof_unit_test_child_proof_2_conf
    ]
    child_proofs = get_proofs(child_object)
    assert set(proofs_child_must_satisfy) == set(child_proofs)
