from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.presentation.router.appointment import appointment_router
from api.presentation.router.auth_routers import user_router

app = FastAPI()

app.include_router(appointment_router)
app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)