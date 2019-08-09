import pytest
from requests import get
from .get_stack import get_endpoint

ENDPOINT = get_endpoint()

pytest.fixture(scope="module", autouse=True)


def setup():
    # seed data?
    pass


def test_get_request():
    path = ENDPOINT + '/get_request'
    res = get(path)
    assert res.status_code == 200
