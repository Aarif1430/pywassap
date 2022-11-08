""" system module for fastapi endpoints """
import logging
import os
from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from mangum import Mangum
from src.routers.router import router as whatsapp_router
from starlette.responses import HTMLResponse

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

app = FastAPI(title="Palavv FastAPI Microservices", openapi_url="/api/v1/openapi.json")
app.include_router(
    whatsapp_router,
    prefix="/api/v1",
    tags=["whatsapp"],
    responses={404: {"description": "Not found"}},
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html() -> Union[HTMLResponse, dict]:
    """Custom swagger UI"""
    if os.environ.get("STAGE") == "dev":
        return get_swagger_ui_html(
            openapi_url=str(app.openapi_url),
            title="Palavv API",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        )
    return {"Not Allowed": "Send requests to appropriate microservices"}


handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn  # type: ignore

    os.environ["STAGE"] = "dev"

    uvicorn.run(
        "server:app",
        host="127.0.0.1",
        port=5000,
        reload=True,
        workers=1,
    )
