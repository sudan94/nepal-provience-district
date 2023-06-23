from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src import en
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return ({"ok"})

# districts of nepal api
app.include_router(en.router)