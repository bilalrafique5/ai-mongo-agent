from pydantic import BaseModel
from typing import Optional

class Person(BaseModel):
    id: Optional[str]
    name:str
    age:int
    # email:str
    
    