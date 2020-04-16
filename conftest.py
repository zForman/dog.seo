import pytest
from config import \
    API_DOG_LIST_ALL_BREEDS, API_DOG_RANDOM_IMAGE, \
    API_DOG_ARRAY_OF_ALL_IMG, API_DOG_ARRAY_OF_SUB_BREEDS


@pytest.fixture
def get_list_all_breed():
    return API_DOG_LIST_ALL_BREEDS
