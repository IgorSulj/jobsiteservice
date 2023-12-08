from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import PlainTextResponse
from send_email import send_blank
from models import WorkBlankModel

load_dotenv()

app = FastAPI()


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
