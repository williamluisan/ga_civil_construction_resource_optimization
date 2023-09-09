from typing import Union
from fastapi import FastAPI

from modules.main import Main

app = FastAPI()

@app.get("/")
def execute():
    return Main.execute();
