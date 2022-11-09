from unittest.mock import MagicMock

import pytest


@pytest.fixture
def whatsapp_mock():
    return MagicMock()
