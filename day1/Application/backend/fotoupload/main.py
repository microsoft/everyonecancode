import os
import io
from fastapi import FastAPI, HTTPException
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError
from fastapi.responses import StreamingResponse


connection_string = os.environ['STORAGE_CONNECTIONSTRING']
service = BlobServiceClient.from_connection_string(conn_str=connection_string)

 # Get a client to interact with a specific container - though it may not yet exist
container_client = service.get_container_client("images")



app = FastAPI()


@app.get("/")
async def root():
    try:
        blobs = [b.name for b in container_client.list_blobs()]
    except ResourceNotFoundError:
        raise HTTPException(status_code=404, detail="Container not found")
    return {"message": "First Microgram!", "files": blobs}

@app.get("/getImage/{image_name}")
async def getImage(image_name):
    blob_container_client = container_client.get_blob_client(image_name)
    blob = blob_container_client.download_blob()
    return StreamingResponse(blob.chunks())

