import os
import io
from azure.storage import blob
from fastapi import FastAPI, HTTPException, File, UploadFile, Request
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from datetime import datetime
from typing import List
from urllib.parse import quote


connection_string = os.environ['STORAGE_CONNECTIONSTRING']
service = BlobServiceClient.from_connection_string(conn_str=connection_string)

# Get a client to interact with a specific container - though it may not yet exist
container_client = service.get_container_client("images")

app = FastAPI()


class Image(BaseModel):
    created_at: datetime = None
    image_url: str


@app.get("/images", response_model=List[Image])
async def list_images(request: Request):
    try:
        blobs = [Image(created_at=b.last_modified,
                       image_url=f"{request.url}/{quote(b.name)}") for b in container_client.list_blobs()]
        blobs.sort(key=lambda a: a.created_at, reverse=True)
    except ResourceNotFoundError:
        raise HTTPException(status_code=404, detail="Container not found")
    return blobs


@app.get("/images/{image_name}")
async def images(image_name):
    try:
        blob_container_client = container_client.get_blob_client(image_name)
        blob = blob_container_client.download_blob()
    except ResourceNotFoundError:
        raise HTTPException(
            status_code=404, detail="Your picture was not found, just try to upload again 🤓")
    return StreamingResponse(blob.chunks())


@app.delete("/images/{image_name}", status_code=204)
async def delete(image_name):
    try:
        blob_container_client = container_client.get_blob_client(image_name)
        blob_container_client.delete_blob()
    except ResourceNotFoundError:
        raise HTTPException(
            status_code=404, detail="Your picture was not found 🤓")
    return {}


@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    container_client.upload_blob(
        file.filename, file.file, blob_type="BlockBlob", overwrite=True)
    return {"filename": file.filename}
