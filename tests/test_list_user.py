import pytest
import requests
import json


def test_random_image(supply_url):
    url = supply_url
    r = requests.get(url)
    print(r.text)

# def test_login_valid(supply_url):
#     url = supply_url + '/login/'
#     data = {'email': 'eve.holt@reqres.in',
#             'password': 'cityslicka'}
#     resp = requests.post(url, data)
#     j = json.loads(resp.text)
#     assert resp.status_code == 207, resp.text
#
#
# @pytest.mark.parametrize('userid, firstname', [(1, 'George'), (2, 'Janet')])
# def test_valid_user(supply_url, userid, firstname):
#     url = supply_url + '/users/' + str(userid)
#     resp = requests.get(url)
#     # print('requests.get:', resp.t)
#     j = json.loads(resp.text)
#     print(j)
#     assert resp.status_code == 200, resp.text
#     assert j['data']['id'] == userid, resp.text
#     assert j['data']['first_name'] == firstname, resp.text
#
#
# def test_list_invaliduser(supply_url):
#     url = supply_url + '/users/50'
#     resp = requests.get(url)
#     assert resp.status_code == 404, resp.text
