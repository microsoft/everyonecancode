import azure.functions as func
from ..app import app
import nest_asyncio

nest_asyncio.apply()

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Each request is redirected to the ASGI handler."""
    return func.AsgiMiddleware(app).handle(req, context)
