import asyncio
from unittest.mock import patch

from pywassap import PyWassap


def test_sending_text_message(client: PyWassap) -> None:
    message = {
        "message": "Hello World",
        "recipient_id": "1234567890",
        "recipient_type": "individual",
    }
    with patch("pywassap._main.BasePyWassap._post") as mock_post:
        mock_post.return_value = {
            "contacts": [{"input": "123456", "wa_id": "123456789"}],
            "messaging_product": "whatsapp",
        }

        response = asyncio.run(client.send_text_message(**message))

        assert response["contacts"] == [{"input": "123456", "wa_id": "123456789"}]
        assert response["messaging_product"] == "whatsapp"
