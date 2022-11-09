""" System module for model whatsapp """
from typing import Dict, List

from pydantic import BaseModel, Field


class SendMessage(BaseModel):
    message: str = Field(..., example="Hello World")
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")

    class Config:
        schema_extra = {
            "example": {
                "message": "Hello World",
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
            }
        }


class SendMessageResponse(BaseModel):
    messaging_product: str = Field(..., example="whatsapp")
    contacts: List[Dict[str, str]] = Field(
        ..., example=[{"input": "447469677603", "wa_id": "447469677603"}]
    )
    messages: List[Dict[str, str]] = Field(
        ...,
        example=[
            {"id": "wamid.HBgMNDQ3NDY5Njc3NjAzFQIAERgSNTA2MTA1QTg1NEYzQzQxREM4AA=="}
        ],
    )

    class Config:
        schema_extra = {
            "example": {
                "messaging_product": "whatsapp",
                "contacts": [{"input": "447469677603", "wa_id": "447469677603"}],
                "messages": [
                    {
                        "id": "wamid.HBgMNDQ3NDY5Njc3NjAzFQIAERgSNTA2MTA1QTg1NEYzQzQxREM4AA=="
                    }
                ],
            }
        }


class ReplyToMessage(BaseModel):
    message: str = Field(..., example="Hello World")
    recipient_id: str = Field(..., example="5511999999999")
    message_id: str = Field(
        ..., example="wamid.HBgMNDQ3NDY5Njc3NjAzFQIAERgSNTA2MTA1QTg1NEYzQzQxREM4AA=="
    )
    recipient_type: str = Field(..., example="individual")

    class Config:
        schema_extra = {
            "example": {
                "message": "Hello World",
                "recipient_id": "5511999999999",
                "message_id": "wamid.HBgMNDQ3NDY5Njc3NjAzFQIAERgSNTA2MTA1QTg1NEYzQzQxREM4AA==",
                "recipient_type": "individual",
            }
        }


class SendInteractive(BaseModel):
    message: str = Field(..., example="Hello World")
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")
    preview_url: bool = Field(..., example=True)
    interactive_type: str = Field(..., example="quick_reply")
    options: List[Dict[str, str]] = Field(
        ...,
        example=[
            {"title": "Yes", "payload": "yes"},
            {"title": "No", "payload": "no"},
        ],
    )

    class Config:
        schema_extra = {
            "example": {
                "message": "Hello World",
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
                "preview_url": True,
                "interactive_type": "quick_reply",
                "options": [
                    {"title": "Yes", "payload": "yes"},
                    {"title": "No", "payload": "no"},
                ],
            }
        }


class SendImage(BaseModel):
    image_id: str = Field(..., example="5511999999999")
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")
    caption: str = Field(..., example="Hello World")

    class Config:
        schema_extra = {
            "example": {
                "image_id": "5511999999999",
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
                "caption": "Hello World",
            }
        }


class SendAudio(BaseModel):
    audio_id: str = Field(..., example="5511999999999")
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")
    caption: str = Field(..., example="Hello World")

    class Config:
        schema_extra = {
            "example": {
                "audio_id": "5511999999999",
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
                "caption": "Hello World",
            }
        }


class SendVideo(BaseModel):
    video_id: str = Field(..., example="5511999999999")
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")
    caption: str = Field(..., example="Hello World")

    class Config:
        schema_extra = {
            "example": {
                "video_id": "5511999999999",
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
                "caption": "Hello World",
            }
        }


class SendDocument(BaseModel):
    document_id: str = Field(..., example="5511999999999")
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")
    caption: str = Field(..., example="Hello World")

    class Config:
        schema_extra = {
            "example": {
                "document_id": "5511999999999",
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
                "caption": "Hello World",
            }
        }


class SendLocation(BaseModel):
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")
    latitude: float = Field(..., example=-23.5505)
    longitude: float = Field(..., example=-46.6333)

    class Config:
        schema_extra = {
            "example": {
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
                "latitude": -23.5505,
                "longitude": -46.6333,
            }
        }


class SendContact(BaseModel):
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")
    contact_id: str = Field(..., example="5511999999999")

    class Config:
        schema_extra = {
            "example": {
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
                "contact_id": "5511999999999",
            }
        }


class SendSticker(BaseModel):
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")
    sticker_id: str = Field(..., example="5511999999999")

    class Config:
        schema_extra = {
            "example": {
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
                "sticker_id": "5511999999999",
            }
        }


class UploadMedia(BaseModel):
    media_type: str = Field(..., example="image")
    media: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "media_type": "image",
                "media": "image.png",
            }
        }


class DeleteMedia(BaseModel):
    media_id: str = Field(..., example="5511999999999")

    class Config:
        schema_extra = {
            "example": {
                "media_id": "5511999999999",
            }
        }


class CreateButton(BaseModel):
    button_id: str = Field(..., example="5511999999999")
    type: str = Field(..., example="web_url")
    title: str = Field(..., example="Hello World")
    url: str = Field(..., example="https://www.google.com")

    class Config:
        schema_extra = {
            "example": {
                "button_id": "5511999999999",
                "type": "web_url",
                "title": "Hello World",
                "url": "https://www.google.com",
            }
        }


class SendButton(BaseModel):
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")
    button_id: str = Field(..., example="5511999999999")

    class Config:
        schema_extra = {
            "example": {
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
                "button_id": "5511999999999",
            }
        }


class SendReplyButton(BaseModel):
    recipient_id: str = Field(..., example="5511999999999")
    recipient_type: str = Field(..., example="individual")
    button_id: str = Field(..., example="5511999999999")
    message_id: str = Field(..., example="5511999999999")

    class Config:
        schema_extra = {
            "example": {
                "recipient_id": "5511999999999",
                "recipient_type": "individual",
                "button_id": "5511999999999",
                "message_id": "5511999999999",
            }
        }


class QueryMediaUrl(BaseModel):
    media_id: str = Field(..., example="5511999999999")

    class Config:
        schema_extra = {
            "example": {
                "media_id": "5511999999999",
            }
        }


class DownloadMedia(BaseModel):
    media_id: str = Field(..., example="5511999999999")

    class Config:
        schema_extra = {
            "example": {
                "media_id": "5511999999999",
            }
        }
