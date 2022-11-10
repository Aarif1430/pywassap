import asyncio
from unittest.mock import MagicMock, patch

import pytest

from src.hiya import WhatsApp


@pytest.fixture
def whatsapp_mock():
    return MagicMock()


@patch("src.hiya._main.aiohttp.ClientSession")
@patch("src.hiya._main.BaseWhatsApp._post")
def test_reply_to_message(session_post, whatsapp_mock):
    message = {
        "message": "Hello World",
        "recipient_id": "44746967763",
        "message_id": "wamid.HBgMNDQ3NDY5Njc3NjAzFQIAERgSNTVEODk3NTlBMDE3OUZDMDUxAA==",
        "recipient_type": "individual",
    }
    session_post.return_value = {
        "detail": "{'message': '(#131030) Recipient phone number not in allowed list', 'type': 'OAuthException', 'code': 131030,'error_data': {'messaging_product': 'whatsapp', 'details': 'Recipient phone number not in allowed list: Add recipient phone number to recipient list and try again.'}, 'error_subcode': 2655007, 'fbtrace_id': 'AULEzP4yrJyM18_EnZSCGa0'}"  # noqa: E501
    }

    client = WhatsApp()
    response = asyncio.run(client.reply_to_message(**message))

    assert (
        response["detail"]
        == "{'message': '(#131030) Recipient phone number not in allowed list', 'type': 'OAuthException', 'code': 131030,'error_data': {'messaging_product': 'whatsapp', 'details': 'Recipient phone number not in allowed list: Add recipient phone number to recipient list and try again.'}, 'error_subcode': 2655007, 'fbtrace_id': 'AULEzP4yrJyM18_EnZSCGa0'}"  # noqa: E501
    )
