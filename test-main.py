from typing import List
#, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() 

@app.get("/")
def read_root():
    return {"Hello": "World"}

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id":item_id, "q": q}

