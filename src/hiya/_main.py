"""
Unofficial python wrapper for the WhatsApp Cloud API.
"""
import asyncio
import logging
import mimetypes
from typing import Any, Dict, List, Union

import aiohttp
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

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
        self.loop = asyncio.get_event_loop()
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
        self, message: str, recipient_id: str, message_id: str, recipient_type: str = "individual"
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

    def send_template_message(
        self,
        template_name: str,
        language_code: str,
        namespace: str,
        elements: List[Dict[str, Any]],
        recipient_id: str,
        recipient_type: str = "individual",
    ) -> Dict[str, Any]:
        """
        Send a template message to a WhatsApp use
        Args:
            template_name: Name of the template e.g. "generic"
            language_code: Language code e.g. "en_US"
            namespace: Namespace of the template e.g. "my_namespace"
            elements: List of elements to be sent in the template e.g. [{"title": "Title", "description": "Description"}] # noqa: E501
            recipient_id: ID of the recipient e.g. "123456789"
            recipient_type: Type of the recipient e.g. "individual"
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "template",
            "template": {
                "namespace": namespace,
                "name": template_name,
                "language": {"policy": "deterministic", "code": language_code},
                "elements": elements,
            },
        }
        response = self.loop.run_until_complete(self._post(json=data))
        if response.status_code == 200:
            logging.info(f"Message sent to {recipient_id}")
            return response.json()
        logging.info(f"Message not sent to {recipient_id}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()

    def send_location_message(
        self,
        latitude: float,
        longitude: float,
        name: str,
        address: str,
        recipient_id: str,
        recipient_type: str = "individual",
    ) -> Dict[str, Any]:
        """
        Send a location message to a WhatsApp user
        Args:
            latitude: Latitude of the location e.g. 1.2345
            longitude: Longitude of the location e.g. 1.2345
            recipient_id: ID of the recipient e.g. "123456789"
            recipient_type: Type of the recipient e.g. "individual"
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "location",
            "location": {"latitude": latitude, "longitude": longitude, "name": name, "address": address},
        }
        response = self.loop.run_until_complete(self._post(json=data))
        if response.status_code == 200:
            logging.info(f"Message sent to {recipient_id}")
            return response.json()
        logging.info(f"Message not sent to {recipient_id}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()

    def send_image_message(
        self,
        image_url: str,
        caption: str,
        recipient_id: str,
        recipient_type: str = "individual",
        link: bool = False,
    ) -> Dict[str, Any]:
        """
        Send an image message to a WhatsApp user
        Args:
            image_url: URL of the image e.g. "https://example.com/image.png"
            caption: Caption of the image e.g. "Image caption"
            recipient_id: ID of the recipient e.g. "123456789"
            recipient_type: Type of the recipient e.g. "individual"
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "image",
            "image": {"url": image_url, "caption": caption} if link else {"file": image_url, "caption": caption},
        }
        response = self.loop.run_until_complete(self._post(json=data))
        if response.status_code == 200:
            logging.info(f"Message sent to {recipient_id}")
            return response.json()
        logging.info(f"Message not sent to {recipient_id}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()

    def send_audio_message(
        self,
        audio_url: str,
        caption: str,
        recipient_id: str,
        recipient_type: str = "individual",
        link: bool = False,
    ) -> Dict[str, Any]:
        """
        Send an audio message to a WhatsApp user
        Args:
            audio_url: URL of the audio e.g. "https://example.com/audio.mp3"
            caption: Caption of the audio e.g. "Audio caption"
            recipient_id: ID of the recipient e.g. "123456789"
            recipient_type: Type of the recipient e.g. "individual"
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "audio",
            "audio": {"url": audio_url, "caption": caption} if link else {"file": audio_url, "caption": caption},
        }
        response = self.loop.run_until_complete(self._post(json=data))
        if response.status_code == 200:
            logging.info(f"Message sent to {recipient_id}")
            return response.json()
        logging.info(f"Message not sent to {recipient_id}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()

    def send_video_message(
        self,
        video_url: str,
        caption: str,
        recipient_id: str,
        recipient_type: str = "individual",
        link: bool = False,
    ) -> Dict[str, Any]:
        """
        Send a video message to a WhatsApp user
        Args:
            video_url: URL of the video e.g. "https://example.com/video.mp4"
            caption: Caption of the video e.g. "Video caption"
            recipient_id: ID of the recipient e.g. "123456789"
            recipient_type: Type of the recipient e.g. "individual"
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "video",
            "video": {"url": video_url, "caption": caption} if link else {"file": video_url, "caption": caption},
        }
        response = self.loop.run_until_complete(self._post(json=data))
        if response.status_code == 200:
            logging.info(f"Message sent to {recipient_id}")
            return response.json()
        logging.info(f"Message not sent to {recipient_id}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()

    def send_file_message(
        self,
        file_url: str,
        caption: str,
        recipient_id: str,
        recipient_type: str = "individual",
        link: bool = False,
    ) -> Dict[str, Any]:
        """
        Send a file message to a WhatsApp user
        Args:
            file_url: URL of the file e.g. "https://example.com/file.pdf"
            caption: Caption of the file e.g. "File caption"
            recipient_id: ID of the recipient e.g. "123456789"
            recipient_type: Type of the recipient e.g. "individual"
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "file",
            "file": {"url": file_url, "caption": caption} if link else {"file": file_url, "caption": caption},
        }
        response = self.loop.run_until_complete(self._post(json=data))
        if response.status_code == 200:
            logging.info(f"Message sent to {recipient_id}")
            return response.json()
        logging.info(f"Message not sent to {recipient_id}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()

    def send_contact_message(
        self,
        contact_name: str,
        contact_phone: str,
        recipient_id: str,
        recipient_type: str = "individual",
    ) -> Dict[str, Any]:
        """
        Send a contact message to a WhatsApp user
        Args:
            contact_name: Name of the contact e.g. "John Doe"
            contact_phone: Phone number of the contact e.g. "+123456789"
            recipient_id: ID of the recipient e.g. "123456789"
            recipient_type: Type of the recipient e.g. "individual"
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "contact",
            "contact": {"name": contact_name, "phone": contact_phone},
        }
        response = self.loop.run_until_complete(self._post(json=data))
        if response.status_code == 200:
            logging.info(f"Message sent to {recipient_id}")
            return response.json()
        logging.info(f"Message not sent to {recipient_id}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()

    def upload_media(self, media_url: str, media_type: str = None) -> Dict[str, Any]:
        """
        Upload media to WhatsApp
        Args:
            media_url: URL of the media e.g. "https://example.com/image.jpg"
            media_type: Type of the media e.g. "image"
        """
        data = {
            "file": (
                media_url,
                open(media_url, "rb"),
                mimetypes.guess_type(media_url)[0],
            ),
            "messaging_product": "whatsapp",
            "type": media_type or mimetypes.guess_type(media_url)[0],
        }
        """
            Upload media to the WhatsApp channel
            Args:
                media_url: URL of the media e.g. "https://example.com/image.jpg"
            media_type: Type of the media e.g. "image"
        """
        data = {
            "file": (
                media_url,
                open(media_url, "rb"),
                mimetypes.guess_type(media_url)[0],
            ),
            "messaging_product": "whatsapp",
            "type": media_type or mimetypes.guess_type(media_url)[0],
        }
        data = MultipartEncoder(data)
        headers = self.headers
        headers["Content-Type"] = data.content_type  # type: ignore
        response = self.loop.run_until_complete(self._post(data=data, headers=headers))
        if response.status_code == 200:
            logging.info(f"Media uploaded")
            return response.json()
        logging.info(f"Media not uploaded")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()

    def delete_media(self, media_id: str) -> Dict[str, Any]:
        """
        Delete media from WhatsApp
        Args:
            media_id: ID of the media e.g. "123456789"
        """
        response = self.loop.run_until_complete(self._delete(f"{BASE_URL}/{media_id}"))
        if response.status_code == 200:
            logging.info(f"Media deleted")
            return response.json()
        logging.info(f"Media not deleted")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()

    def create_button_template(
        self,
        text: str,
        buttons: List[Dict[str, Any]],
        media_id: str = None,
        media_type: str = None,
        media_link: bool = False,
    ) -> Dict[str, Any]:
        """
        Create a button template
        Args:
            text: Text of the template e.g. "Button template text"
            buttons: List of buttons e.g. [{"type": "link", "text": "Button text", "url": "https://example.com"}]
            media_id: ID of the media e.g. "123456789"
            media_type: Type of the media e.g. "image"
            media_link: Whether the media is a link or not e.g. False
        """
        template = {"type": "button", "text": text, "buttons": buttons, "media": {}}
        if media_id:
            if media_link:
                template["media"] = {"link": media_id}
            template["media"] = {"id": media_id, "type": media_type}
        return template

    def send_button_template(
        self,
        text: str,
        buttons: List[Dict[str, Any]],
        recipient_id: str,
        recipient_type: str = "individual",
        media_id: str = None,
        media_type: str = None,
        media_link: bool = False,
    ) -> Dict[str, Any]:
        """
        Send a button template to a WhatsApp user
        Args:
            text: Text of the template e.g. "Button template text"
            buttons: List of buttons e.g. [{"type": "link", "text": "Button text", "url": "https://example.com"}]
            recipient_id: ID of the recipient e.g. "123456789"
            recipient_type: Type of the recipient e.g. "individual"
            media_id: ID of the media e.g. "123456789"
            media_type: Type of the media e.g. "image"
            media_link: Whether the media is a link or not e.g. False
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "template",
            "template": self.create_button_template(text, buttons, media_id, media_type, media_link),
        }
        response = self.loop.run_until_complete(self._post(json=data))
        if response.status_code == 200:
            logging.info(f"Message sent to {recipient_id}")
            return response.json()
        logging.info(f"Message not sent to {recipient_id}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()

    def send_reply_button_template(
        self,
        text: str,
        buttons: List[Dict[str, Any]],
        recipient_id: str,
        recipient_type: str = "individual",
        media_id: str = None,
        media_type: str = None,
        media_link: bool = False,
        reply_id: str = None,
    ) -> Dict[str, Any]:
        """
        Send a button template to a WhatsApp user
        Args:
            text: Text of the template e.g. "Button template text"
            buttons: List of buttons e.g. [{"type": "link", "text": "Button text", "url": "https://example.com"}]
            recipient_id: ID of the recipient e.g. "123456789"
            recipient_type: Type of the recipient e.g. "individual"
            media_id: ID of the media e.g. "123456789"
            media_type: Type of the media e.g. "image"
            media_link: Whether the media is a link or not e.g. False
            reply_id: ID of the message to reply to e.g. "123456789"
        """
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": recipient_id,
            "type": "template",
            "template": self.create_button_template(text, buttons, media_id, media_type, media_link),
            "reply_id": reply_id,
        }
        response = self.loop.run_until_complete(self._post(json=data))
        if response.status_code == 200:
            logging.info(f"Message sent to {recipient_id}")
            return response.json()
        logging.info(f"Message not sent to {recipient_id}")
        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Response: {response.json()}")
        return response.json()
