from typing import Optional

from fastapi import FastAPI
from app.user import router as user_router


app = FastAPI(title="Ecommerce APP",
              version="0.0.1")

app.include_router(user_router)

