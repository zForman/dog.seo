import pytest
import requests


class APIClient:
    def __init__(self, base_address, random_num):
        self.base_address = base_address
        self.random_num = random_num

    def get(self, path='/', params=None):
        if int(self.random_num) > 1:
            url = self.base_address + path + str(self.random_num)
        else:
            url = self.base_address + path
        return requests.get(url=url, params=params)


def pytest_addoption(parser):

    def choice():
        res = []
        for i in range(51):
            res.append(str(i))
        return res

    parser.addoption(
        '--base_url',
        choices=['https://dog.ceo/api/'],
        help='Use the url https://dog.ceo/api/',
        required=True
    )

    parser.addoption(
        '--num',
        default=0,
        choices=choice(),
        help='Use the url https://dog.ceo/api/',
    )


@pytest.fixture(scope='session')
def call_api(request):
    random_num = request.config.getoption('--num')
    base_url = request.config.getoption('--base_url')
    return APIClient(base_address=base_url, random_num=random_num)
