from fastapi import FastAPI

from modules.main import Main
from modules.pygad import Pygad

app = FastAPI()

@app.get("/")
def execute():
    return Main.execute();

@app.get("/pygad")
def execute_pygad():
    return Main.execute_pygad();