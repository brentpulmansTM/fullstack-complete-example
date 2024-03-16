from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

import config
import database
import routes.examples

load_dotenv()

app = FastAPI(docs_url=config.documentation_url)

app.include_router(router=routes.examples.app, prefix="/festivals")

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

