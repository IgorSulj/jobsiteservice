from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import WorkBlankModel

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
    print('Получил данные')
