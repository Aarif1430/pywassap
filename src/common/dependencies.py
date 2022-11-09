""" system module for fastapi dependencies """
from pydantic import BaseModel

from src.hiya import WhatsApp

whatsapp_base = WhatsApp()


class CommonParameters(BaseModel):
    """Common parameters for all endpoints"""

    whatsapp: WhatsApp

    class Config:
        arbitrary_types_allowed = True


def common_parameters() -> CommonParameters:
    """Common parameters for all endpoints"""
    return CommonParameters(
        whatsapp=whatsapp_base,
    )
