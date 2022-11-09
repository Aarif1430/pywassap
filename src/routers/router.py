""" System modules for payments """
import logging
from asyncio import Task
from typing import Any, Dict, Generator, Union

from fastapi import APIRouter, Depends, HTTPException

from src.common.dependencies import CommonParameters, common_parameters
from src.models import ReplyToMessage, SendMessage, SendMessageResponse

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
