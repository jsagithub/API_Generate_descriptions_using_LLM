from typing import Union

from fastapi import FastAPI
from generate import generateDescription

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/task_description/{task_title}")
def read_item(task_title: str):
    description = generateDescription(task_title)
    return {"task_title": task_title, "description": description}