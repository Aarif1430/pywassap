"""
Unofficial python wrapper for the WhatsApp Cloud API.
"""
import logging
from typing import Any, Dict

import aiohttp

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

BASE_URL = "https://graph.facebook.com/v14.0"
PHONE_NUMBER = "101150499354696"
TOKEN = "EAAKV6NqOF3YBAG7MZCAkHYTaqFXiLj6ePlPcmfqbTxiM91sHyQCdilTa44oZBE2dNZClfHlPG35ZAQ3ijA8ZCos5PICg5yCktvqGsX6wJ9ZBsxmg1Y4w9BLMMbeq2pl9bTxvqIPmOCghGBGLhe2BvxDQLBddKpKu56GbMsYr9Ia0IIdPv8HdtU1ZCZCP2YgrSG3Rh8QjW3IDEAZDZD"  # noqa: E501


class BasePyWassap:
    """
    Base class for WhatsApp
    """

    def __init__(self, phone_number: str, token: str) -> None:
        self.url = f"{BASE_URL}/{phone_number}/messages"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token),
        }

    async def _get(self, *args: Any, **kwargs: Any) -> Dict[str, Any] | Any:
        """
        Make a GET request
        """
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.url, **kwargs) as response:
                return await response.json()

    async def _post(self, *args: Any, **kwargs: Dict[str, Any]) -> Dict[str, Any] | Any:
        """
        Make a POST request
        """
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(self.url, **kwargs) as response:
                return await response.json()

    async def _put(self, *args: Any, **kwargs: Dict[str, Any]) -> Dict[str, Any] | Any:
        """
        Make a PUT request
        """
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.put(self.url, **kwargs) as response:
                return await response.json()

    async def _delete(self, *args: Any, **kwargs: Dict[str, Any]) -> Dict[str, Any] | Any:
        """
        Make a DELETE request
        """
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.delete(self.url, **kwargs) as response:
                return await response.json()


class PyWassap(BasePyWassap):
    def __init__(self, phone_number: str, token: str) -> None:
        super().__init__(phone_number, token)

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
