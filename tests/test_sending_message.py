import asyncio
from unittest.mock import MagicMock, patch

import pytest
from src.hiya import WhatsApp


@pytest.fixture
def whatsapp_mock():
    return MagicMock()


@patch("src.hiya._main.BaseWhatsApp._post")
def test_sending_text_message(session_post, whatsapp_mock):
    message = {
        "message": "Hello World",
        "recipient_id": "447469677603",
        "recipient_type": "individual",
    }
    session_post.return_value = {
        "contacts": [{"input": "447469677603", "wa_id": "447469677603"}],
        "messaging_product": "whatsapp",
    }
    client = WhatsApp()
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(client.send_text_message(**message))

    assert response["contacts"] == [{"input": "447469677603", "wa_id": "447469677603"}]
    assert response["messaging_product"] == "whatsapp"
