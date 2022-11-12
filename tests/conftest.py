""" Conftest for pytest. """
import pytest

from pywassap import PyWassap


@pytest.fixture
def client() -> PyWassap:
    test_number = "123456789"
    test_token = "123456789"
    _client = PyWassap(test_number, test_token)
    return _client
