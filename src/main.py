
from models import *
from fastapi import FastAPI, HTTPException, Request, Depends, Header, status, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url=None, redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status")
async def _status(request: Request):
    return {
        "status": "All good"
    }