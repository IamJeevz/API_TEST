import os
import logging
from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
import time
import json

# Configure log file path using environment variable
log_file_path = os.getenv('LOG_FILE', 'requests.log')


# Logging configuration
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Your FastAPI routes and middleware here...

app = FastAPI()

class Resource(BaseModel):
    username: str
    password: str

REQUIRED_USER_AGENT = "ptpl"
REQ_USERNAME = "prudent"
REQ_PASSWORD = "Admin"

@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_time = time.time()

    # Retrieve request parameters
    query_params = dict(request.query_params)
    headers = dict(request.headers)  # Access headers directly using request.headers
    try:
        body = await request.json() if request.method in ("POST", "PUT") else None
    except:
        body = None

    response = await call_next(request)
    process_time = time.time() - request_time

    log_message = (
        f"{request.method} {request.url} - "
        f"Query params: {json.dumps(query_params)} - "
        f"Headers: {json.dumps(headers)} - "
        f"Body: {json.dumps(body)} - "
        f"Status code: {response.status_code} - "
        f"Processing time: {process_time:.4f} seconds"
    )
    logger.info(log_message)
    print("\n" + log_message + "\n")
    return response

@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to Prudent"}

@app.post("/api/v1/resource")
def create_resource(resource: Resource, head: Optional[str] = Header(None)):
    return {
        "message": "Success",
        "header": head,
        "username" : resource.username,
        "password" : resource.password
    }
