from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import WorkBlankModel

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*']
)


@app.post("/")
def main(work_blank: WorkBlankModel):
    print('Получил данные')
