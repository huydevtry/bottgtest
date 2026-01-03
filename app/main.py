from fastapi import FastAPI
from app.api.social import router as social_analyze

app = FastAPI(docs_url=None, redoc_url=None)

app.include_router(social_analyze)