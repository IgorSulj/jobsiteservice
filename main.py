from fastapi import FastAPI

from models import WorkBlankModel

app = FastAPI()


@app.post("/")
def main(work_blank: WorkBlankModel):
    pass
