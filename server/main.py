from fastapi import FastAPI
from typing import Optional
import json

app = FastAPI()

with open("data.json") as f:
    events = json.load(f)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/")
async def say_hello():
    return {"message": f"Hello user"}


@app.get("/api/events-categories")
def read_events_categories(skip: Optional[int] = 0, limit: Optional[int] = 3):
    return events['events_categories'][skip: skip + limit]


@app.get("/api/events")
def read_events(skip: Optional[int] = 0, limit: Optional[int] = 15):
    return events['allEvents'][skip: skip + limit]
