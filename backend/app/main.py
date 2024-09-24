from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.application.controllers import categories_router, notes_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=notes_router, prefix="/api/notes")
app.include_router(router=categories_router, prefix="/api/categories")