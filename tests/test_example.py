import pytest


@pytest.mark.slow
def summarize(num1, num2):
    return num1 + num2


@pytest.fixture(scope='session')
def get_sum_test_data():
    return [(3, 5, 8), (-2, -2, -4), (-1, 5, 4), (3, -5, -2), (0, 5, 5)]


@pytest.fixture(autouse=True)
def setup_and_teardown():
    print('\nFetching data from db')
    yield
    print('\nSaving test run data in db')


def test_sum(get_sum_test_data):
    for data in get_sum_test_data:
        num1 = data[0]
        num2 = data[1]
        expected = data[2]
        assert summarize(num1, num2) == expected


def test_sum_output_type():
    assert type(summarize(1, 2)) is int
