from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel, HttpUrl
from app.core.auth import api_key_auth
from app.core.client_insta import login_user, url_media
from app.telegram.handler import handle_update
from app.telegram.schemas import Update
from app.utlils.domain import analyze_domain
from instagrapi import Client


router = APIRouter()

class AnalyzeRequest(BaseModel):
    url: str

@router.post("/social/analyze", dependencies=[Depends(api_key_auth)])
def analyze_api(payload: AnalyzeRequest):
    try:
        url = str(payload.url)
        
        resp = {
            'status': 0,
            'data': {
                "url": url_media(url=url)
            }
        }

        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return resp

@router.post("/telegram/webhook")
async def telegram_webhook(update: Update):
    handle_update(update)
    return {"ok": True}