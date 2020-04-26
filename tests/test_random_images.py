import pytest
from cerberus import Validator
from config import API_DOG_RANDOM_IMAGE


schema_list = {
    'message':
    {
        'type': 'list'
    },
    'status':
    {
        'type': 'string'
    }
}
schema_str = {
    'message':
    {
        'type': 'string'
    },
    'status':
    {
        'type': 'string'
    }
}


@pytest.mark.parametrize('path, response_code, content_type', [(API_DOG_RANDOM_IMAGE, 200, 'application/json')])
def test_random_images(call_api, path, content_type, response_code):
    response = call_api.get(path=path)
    data = response.json()
    if type(data['message']) is list:
        assert Validator().validate(data, schema_list)
    else:
        assert Validator().validate(data, schema_str)
    assert response.headers['Content-Type'] == content_type
    assert response.status_code == response_code

