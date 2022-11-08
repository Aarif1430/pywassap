""" System modules for payments """
import asyncio
import logging
from asyncio import Task
from typing import Any, Dict, Generator, List, Union

from fastapi import APIRouter, Depends, HTTPException
from src.common.dependencies import CommonParameters, common_parameters
from src.models import (
    CreateButton,
    DeleteMedia,
    DownloadMedia,
    QueryMediaUrl,
    ReplyToMessage,
    SendAudio,
    SendButton,
    SendContact,
    SendDocument,
    SendImage,
    SendInteractive,
    SendLocation,
    SendMessage,
    SendMessageResponse,
    SendReplyButton,
    SendSticker,
    SendVideo,
    UploadMedia,
)

router = APIRouter()


logger = logging.getLogger(__name__)


@router.post("/send_message", response_model=SendMessageResponse)
async def send_message(
    message: SendMessage, common: CommonParameters = Depends(common_parameters)
) -> Union[Generator[Any, None, Task[Any]], Any] | HTTPException:
    """Send a message to a user"""
    try:
        return await common.whatsapp.send_text_message(**message.dict())
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/reply_to_message", response_model=SendMessageResponse)
async def reply_to_message(
    message: ReplyToMessage, common: CommonParameters = Depends(common_parameters)
) -> Dict[str, Any]:
    """Reply to a message"""
    try:
        return await common.whatsapp.reply_to_message(**message.dict())
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/send_image", response_model=SendMessageResponse)
async def send_image(image: SendImage, common: CommonParameters = Depends(common_parameters)) -> Dict[str, Any]:
    """Send an image to a user"""
    try:
        return await common.whatsapp.send_image_message(**image.dict())
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
