import mimetypes


def test__get_all_img__by_breed(call_api, pytestconfig):
    url = pytestconfig.getoption('base_url')
    all_img_sub_breed = pytestconfig.getoption('all_img_sub_breed')
    path = f'breed/{all_img_sub_breed}/images'
    response = call_api.get(path=path)
    data = response.json()
    assert response.url == url+path
    assert data['status'] == 'success'
