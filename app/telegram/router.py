from fastapi import APIRouter, Header, HTTPException
from app.telegram.schemas import Update
from app.telegram.handler import handle_update
from app.core.config import TELEGRAM_WEBHOOK_SECRET

router = APIRouter()

@router.post("/telegram/webhook")
async def telegram_webhook(
    update: Update,
    x_telegram_bot_api_secret_token: str | None = Header(None),
):
    if x_telegram_bot_api_secret_token != TELEGRAM_WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    handle_update(update)
    return {"ok": True}
