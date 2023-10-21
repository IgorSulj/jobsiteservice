from typing import Annotated
from fastapi import FastAPI, File

from models import WorkBlankModel

app = FastAPI()


@app.post("/")
def main(work_blank: WorkBlankModel, files: Annotated[bytes, File()]):
    pass
