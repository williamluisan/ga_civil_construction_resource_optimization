from fastapi import FastAPI

from modules.main import Main

app = FastAPI()

@app.get("/")
def execute():
    return Main.execute();

@app.get("/pygad")
def execute_pygad():
    return Main.execute_pygad();