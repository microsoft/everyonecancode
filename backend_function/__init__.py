"""
This module is the entry point for the Azure Function.
It is responsible for handling the HTTP request and passing it to the FastAPI app in the root folder.

Azure Functions do not support streaming repsonses, so we can not stream images from the storage account yet.
Hopefully this will be supported in the future.
"""


import azure.functions as func
from ..app import app
import nest_asyncio

nest_asyncio.apply()

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Each request is redirected to the ASGI handler."""
    return func.AsgiMiddleware(app).handle(req, context)
