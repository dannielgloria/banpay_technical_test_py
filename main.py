from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.settings import Settings


app = FastAPI()

# The `app.add_middleware()` function is used to add middleware to the FastAPI application. In this
# case, it is adding the `CORSMiddleware` middleware.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

settings = Settings()

