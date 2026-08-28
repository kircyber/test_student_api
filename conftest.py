import allure
import pytest
from utils import create_logger

from api.api import Api
from api.client import ApiClient

@pytest.fixture
def api():
    client = ApiClient()

    return Api(client)

@pytest.fixture
def logger():
    logger, log_stream = create_logger()

    yield logger, log_stream

    log_content = log_stream.getvalue()

    allure.attach(
        log_content,
        name="API Logs",
        attachment_type=allure.attachment_type.TEXT
    )