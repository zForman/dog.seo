import pytest
import mimetypes


@pytest.mark.parametrize('status, expected_extension', [('success', '.json')])
def test_breed_random_img(call_api, pytestconfig, status, expected_extension):
    breed = pytestconfig.getoption('--breed')
    response = call_api.get(path=f'breed/{breed}/images/random')
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    data = response.json()
    assert data['status'] == status
    assert extension == expected_extension
