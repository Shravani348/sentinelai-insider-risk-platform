# backend/app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1 import auth, employees, activity, alerts
import traceback

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="SentinelAI Backend API for Insider Threat Detection"
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "GLOBAL CRASH CAUGHT",
            "error": str(exc),
            "traceback": traceback.format_exc()
        }
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register our endpoints
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(employees.router, prefix=f"{settings.API_V1_STR}/employees", tags=["employees"])
app.include_router(activity.router, prefix=f"{settings.API_V1_STR}/activity", tags=["activity"]) # Added activity router

@app.get("/")
def root():
    return {"status": "online", "message": "SentinelAI API is running securely."}

app.include_router(alerts.router, prefix=f"{settings.API_V1_STR}/alerts", tags=["alerts"])