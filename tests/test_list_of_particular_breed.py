import pytest


@pytest.mark.parametrize('breed', [('bulldog', 3),
                                   ('poodle', 3),
                                   ('retriever', 4),
                                   ('spaniel', 7)])
def test_get_particular_breed(call_api, pytestconfig, breed):
    response = call_api.get(path='breed/{}/list'.format(breed[0]))
    data = response.json()
    assert len(data['message']) == breed[1]
