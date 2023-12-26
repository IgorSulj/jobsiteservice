from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from models import WorkBlankModel
from emailer import send_blank
import env


if env.DEBUG:
    app = FastAPI()
else:
    app = FastAPI(docs_url=None, redoc_url=None)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://localhost:5173',
        'http://localhost:5173',
        'https://rabotavsem.by',
    ],
    allow_methods=['GET', 'POST']
)


@app.post("/")
def main(work_blank: WorkBlankModel):
    send_blank(work_blank)
    return PlainTextResponse()
