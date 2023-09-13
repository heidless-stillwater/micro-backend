from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() 

class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name='Jamilia', age=23),
    Person(id=2, name='Kamal', age=53),
    Person(id=3, name='Arjuna', age=44)
]

@app.get("/api")
def read_root():
    return DB

