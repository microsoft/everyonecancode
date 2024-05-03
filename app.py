"""
This is a simple FastAPI app developed for AnyoneCanCode that allows you to upload images to Azure Blob Storage.

This app is designed to be deployed to Azure App Service as a Linux container. It uses the Azure Storage SDK for Python to
stream images from Azure Blob Storage to the browser.
"""

import os
from datetime import datetime
from typing import List
from urllib.parse import quote
import uvicorn
from azure.core.exceptions import ResourceNotFoundError
from azure.storage.blob import BlobServiceClient
from fastapi import Depends, FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import RedirectResponse, StreamingResponse, JSONResponse
from pydantic import BaseModel
import openai



app = FastAPI()
cache_header = {"Cache-Control": "max-age=31556952"}

shared_container_client = None
shared_openai_client = None

async def get_container_client():
    """Get a client to interact with the blob storage container."""
    global shared_container_client
    if not shared_container_client:
        connection_string = os.environ["CUSTOMCONNSTR_STORAGE"]
        service = BlobServiceClient.from_connection_string(conn_str=connection_string)

        # Get a client to interact with a specific container - though it may not yet exist
        shared_container_client = service.get_container_client("images")
    return shared_container_client

async def get_openai_client():
    """Get a client to interact with the Azure OpenAI chat API."""
    global shared_openai_client
    if not shared_openai_client:
        chat_api_key = os.environ["CHAT_API_KEY"]
        chat_azure_endpoint = os.environ["CHAT_API_ENDPOINT"]
        chat_azure_deployment = os.environ["AZURE_OPENAI_MODEL_NAME"]

        shared_openai_client = openai.AzureOpenAI(
            api_key=chat_api_key,
            api_version="2023-12-01-preview",
            azure_endpoint=chat_azure_endpoint,
            azure_deployment=chat_azure_deployment
        )
    return shared_openai_client

@app.exception_handler(KeyError)
async def unicorn_exception_handler(request: Request, exc: KeyError):
    """Handle missing environment variables."""
    match exc.args[0]:
      case "CUSTOMCONNSTR_STORAGE":
        return JSONResponse(
            status_code=500,
            content={
                "message": f"Oops! You forgot to set the STORAGE connection string for your Azure Storage Account. You can test locally by setting CUSTOMCONNSTR_STORAGE. 🤓"
            },
        )
      case "CHAT_API_KEY":
        return JSONResponse(
            status_code=500,
            content={
                "message": f"Oops! You forgot to set the CHAT_API_KEY environment variable. 🤓"
            },
        )
      case "CHAT_API_ENDPOINT":
        return JSONResponse(
            status_code=500,
            content={
                "message": f"Oops! You forgot to set the CHAT_API_ENDPOINT environment variable. 🤓"
            },
        )
      case "AZURE_OPENAI_MODEL_NAME":
        return JSONResponse(
            status_code=500,
            content={
                "message": f"Oops! You forgot to set the AZURE_OPENAI_MODEL_NAME environment variable. 🤓"
            },
        )
    raise exc


@app.exception_handler(ValueError)
async def unicorn_exception_handler(request: Request, exc: KeyError):
    if exc.args[0] == "Connection string is either blank or malformed.":
        return JSONResponse(
            status_code=500,
            content={
                "message": f"Oops! Your connection string is either blank or malformed. 🤓"
            },
        )
    raise exc

class Image(BaseModel):
    created_at: datetime = None
    image_url: str

class Prompt(BaseModel):
    message: str


@app.get("/")
async def redirect_to_docs():
    """Redirect to the docs page."""
    return RedirectResponse("/docs")


@app.get("/images", response_model=List[Image])
async def list_images(container_client=Depends(get_container_client)):
    """List all images from a blob storage container."""
    try:
        blobs = [
            Image(created_at=b.last_modified, image_url=f"/images/{quote(b.name)}")
            for b in container_client.list_blobs()
        ]
        blobs.sort(key=lambda a: a.created_at, reverse=True)
    except ResourceNotFoundError:
        return JSONResponse(
            status_code=500,
            content={
                "message": f"Oops! You forgot to create a blob storage container named 'images'. 🤓"
            },
        )
    return blobs


@app.get("/images/{image_name}")
async def images(image_name, container_client=Depends(get_container_client)):
    """Stream an image from the blob storage container."""
    try:
        blob_container_client = container_client.get_blob_client(image_name)
        blob = blob_container_client.download_blob()
    except ResourceNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Your picture was not found, just try to upload again. 🤓",
        )
    return StreamingResponse(blob.chunks(), headers=cache_header)


@app.delete("/images/{image_name}")
async def delete(image_name, container_client=Depends(get_container_client)):
    """Delete an image from the blob storage container."""
    try:
        blob_container_client = container_client.get_blob_client(image_name)
        blob_container_client.delete_blob()
    except ResourceNotFoundError:
        raise HTTPException(status_code=404, detail="Your picture was not found. 🤓")
    return {}


@app.post("/upload/")
async def upload(
    file: UploadFile = File(...), container_client=Depends(get_container_client)
):
    """Upload an image to the blob storage container."""
    container_client.upload_blob(
        file.filename, file.file, blob_type="BlockBlob", overwrite=True
    )
    return {"filename": file.filename}




@app.post("/chat")
async def chat(prompt: Prompt, azOpenAIClient=Depends(get_openai_client)):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt.message}
    ]

    response = azOpenAIClient.chat.completions.create(
                model="gpt-35-turbo",
                messages=messages,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    """Run the app locally for testing."""
    uvicorn.run(app, port=8000)


