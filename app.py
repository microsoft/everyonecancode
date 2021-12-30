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

app = FastAPI()
cache_header = {"Cache-Control": "max-age=31556952"}

shared_container_client = None

async def get_container_client():
    global shared_container_client
    if not shared_container_client:
        connection_string = os.environ['CUSTOMCONNSTR_STORAGE']
        service = BlobServiceClient.from_connection_string(conn_str=connection_string)

        # Get a client to interact with a specific container - though it may not yet exist
        shared_container_client = service.get_container_client("images")
    return shared_container_client

@app.exception_handler(KeyError)
async def unicorn_exception_handler(request: Request, exc: KeyError):
    if exc.args[0] == 'CUSTOMCONNSTR_STORAGE':
        return JSONResponse(
            status_code=500,
            content={"message": f"Oops! You forgot to set the STORAGE connection string for your Azure Storage Account. You can test locally by setting CUSTOMCONNSTR_STORAGE. 🤓"},
        )
    raise exc

@app.exception_handler(ValueError)
async def unicorn_exception_handler(request: Request, exc: KeyError):
    if exc.args[0] == 'Connection string is either blank or malformed.':
        return JSONResponse(
            status_code=500,
            content={"message": f"Oops! Your connection string is either blank or malformed. 🤓"},
        )
    raise exc
class Image(BaseModel):
    created_at: datetime = None
    image_url: str

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse("/docs")

@app.get("/images", response_model=List[Image])
async def list_images(container_client = Depends(get_container_client)):
    try:
        blobs = [Image(created_at=b.last_modified,
                       image_url=f"/images/{quote(b.name)}") for b in container_client.list_blobs()]
        blobs.sort(key=lambda a: a.created_at, reverse=True)
    except ResourceNotFoundError:
        return JSONResponse(
            status_code=500,
            content={"message": f"Oops! You forgot to create a blob storage container named 'images'. 🤓"},
        )
    return blobs


@app.get("/images/{image_name}")
async def images(image_name, container_client = Depends(get_container_client)):
    try:
        blob_container_client = container_client.get_blob_client(image_name)
        blob = blob_container_client.download_blob()
    except ResourceNotFoundError:
        raise HTTPException(
            status_code=404, detail="Your picture was not found, just try to upload again. 🤓")
    return StreamingResponse(blob.chunks(), headers=cache_header)


@app.delete("/images/{image_name}")
async def delete(image_name, container_client = Depends(get_container_client)):
    try:
        blob_container_client = container_client.get_blob_client(image_name)
        blob_container_client.delete_blob()
    except ResourceNotFoundError:
        raise HTTPException(
            status_code=404, detail="Your picture was not found. 🤓")
    return {}


@app.post("/upload/")
async def upload(file: UploadFile = File(...), container_client = Depends(get_container_client)):
    container_client.upload_blob(
        file.filename, file.file, blob_type="BlockBlob", overwrite=True)
    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
