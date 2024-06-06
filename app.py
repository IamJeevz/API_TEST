from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Resource(BaseModel):
    name: str

REQUIRED_USER_AGENT = "jeevan"

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/api/v1/resource")
def create_resource(resource: Resource, user_agent: Optional[str] = Header(None)):
    if user_agent != REQUIRED_USER_AGENT:
        raise HTTPException(status_code=400, detail="Invalid User-Agent header")

    return {
        "message": "Success",
        "user_agent": user_agent
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
