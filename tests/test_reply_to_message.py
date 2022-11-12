import asyncio
from unittest.mock import patch

from pywassap import PyWassap


def test_reply_to_message(client: PyWassap) -> None:
    message = {
        "message": "Hello World",
        "recipient_id": "1234567890",
        "message_id": "wamid.HBgMNDQ3NDY5Njc3NjAzFQIAERgSNTVEODk3NTlBMDE3OUZDMDUxAA==",
        "recipient_type": "individual",
    }
    with patch("pywassap._main.BasePyWassap._post") as mock_post:
        mock_post.return_value = {
            "detail": "{'message': '(#131030) Recipient phone number not in allowed list', 'type': 'OAuthException', 'code': 131030,'error_data': {'messaging_product': 'whatsapp', 'details': 'Recipient phone number not in allowed list: Add recipient phone number to recipient list and try again.'}, 'error_subcode': 2655007, 'fbtrace_id': 'AULEzP4yrJyM18_EnZSCGa0'}"  # noqa: E501
        }
        response = asyncio.run(client.reply_to_message(**message))

        assert (
            response["detail"]
            == "{'message': '(#131030) Recipient phone number not in allowed list', 'type': 'OAuthException', 'code': 131030,'error_data': {'messaging_product': 'whatsapp', 'details': 'Recipient phone number not in allowed list: Add recipient phone number to recipient list and try again.'}, 'error_subcode': 2655007, 'fbtrace_id': 'AULEzP4yrJyM18_EnZSCGa0'}"  # noqa: E501
        )
