from pydantic import BaseModel
from typing import Optional

class PersonSchema(BaseModel):
    name:str
    age:int