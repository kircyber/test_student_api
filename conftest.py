import pytest

from api.api import Api
from api.client import ApiClient

@pytest.fixture
def api():
    client = ApiClient()

    return Api(client)