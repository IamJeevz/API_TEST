from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
import logging
import time
import json

# Logging configuration
logging.basicConfig(
    filename='requests.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

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
    
    return response

@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to Prudent"}

@app.post("/api/v1/resource")
def create_resource(resource: Resource, user_agent: Optional[str] = Header(None)):
    if user_agent != REQUIRED_USER_AGENT:
        raise HTTPException(status_code=400, detail="Invalid User-Agent header")
        
    if resource.username != REQ_USERNAME:
        raise HTTPException(status_code=400, detail="Invalid username")
        
    if resource.password != REQ_PASSWORD:
        raise HTTPException(status_code=400, detail="Invalid password")

    # Log username and password
    logger.info(f"Username: {resource.username}, Password: {resource.password}")

    return {
        "message": "Success",
        "user_agent": user_agent
    }
