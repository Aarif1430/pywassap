"""
Unofficial python wrapper for the WhatsApp Cloud API.
"""
import logging
from typing import Any, Dict, Union

import aiohttp
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

BASE_URL = "https://graph.facebook.com/v14.0"
PHONE_NUMBER = "101150499354696"
TOKEN = "EAAKV6NqOF3YBAFcczbyNyPhEaB0wX07ExdULZAzJRARmBzm7FjX1USpsSsnhXQAvQMGNEzoCkAh0ZCO8HHVXlqbZCrkHC60OaEG6VZBh2doobxRMA6UWcH4zY2ZBTOpd8PZCA7vpTcBr3oEBlGKLw8B4jzW8fmwuZCHVYE7wJKTH7HwSb1pZAcpuANQW2A151ZAVvGA3hew0G7AZDZD"  # noqa: E501


class BaseWhatsApp:
    """
    Base class for WhatsApp
    """

    def __init__(self) -> None:
        self.url = f"{BASE_URL}/{PHONE_NUMBER}/messages"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(TOKEN),
        }
        self._session = aiohttp.ClientSession(headers=self.headers)

    async def _get(self, *args, **kwargs) -> Union[requests.Response, str]:
        """
        Make a GET request
        """
        async with self._session.get(self.url, *args, **kwargs) as response:
            return await response.json()

    async def _post(self, *args, **kwargs) -> Dict[str, Any]:
        """
        Make a POST request
        """
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(self.url, **kwargs) as response:
                return await response.json()

    async def _put(self, *args, **kwargs) -> requests.Response:
        """
        Make a PUT request
        """
        async with self._session.put(self.url, *args, **kwargs) as response:
            return await response.json()

    async def _delete(self, *args, **kwargs) -> requests.Response:
        """
        Make a DELETE request
        """
        async with self._session.delete(self.url, *args, **kwargs) as response:
            return await response.json()


class WhatsApp(BaseWhatsApp):
    def __init__(self) -> None:
        super().__init__()

    async def send_text_message(
        self, message: str, recipient_id: str, recipient_type: str = "individual"
    ) -> Dict[str, Any]:
        """
        Send a text message to a WhatsApp user
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "text",
            "text": {"preview_url": True, "body": message},
        }
        response = await self._post(json=data)
        if response.get("error"):
            logging.info(f"Message not sent to {recipient_id}")
            logging.info(f"Response: {response}")
            raise Exception(response.get("error"))
        logging.info(f"Message sent to {recipient_id}")
        return response

    async def reply_to_message(
        self,
        message: str,
        recipient_id: str,
        message_id: str,
        recipient_type: str = "individual",
    ) -> Dict[str, Any]:
        """
        Reply to a WhatsApp message
        Args:
            message: Message to be sent e.g. "Hello"
            recipient_id: ID of the recipient e.g. "123456789"
            message_id: ID of the message to be replied to e.g. "123456789"
            recipient_type: Type of the recipient e.g. "individual"
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "text",
            "context": {"message_id": message_id},
            "text": {"preview_url": True, "body": message},
        }
        response = await self._post(json=data)
        if response.get("error"):
            logging.info(f"Message not sent to {recipient_id}")
            logging.info(f"Response: {response}")
            raise Exception(response.get("error"))
        logging.info(f"Message sent to {recipient_id}")
        return response
