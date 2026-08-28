import allure
import pytest
from utils.logger import create_logger

from api.api import Api
from api.client import ApiClient

@pytest.fixture
def api(logger):
    client = ApiClient()

    return Api(client, logger)

@pytest.fixture
def logger():
    logger, log_stream = create_logger()

    yield logger

    log_content = log_stream.getvalue()

    allure.attach(
        log_content,
        name="API Logs",
        attachment_type=allure.attachment_type.TEXT
    )