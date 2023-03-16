from typing import Optional
from pydantic import BaseModel


class Users(BaseModel):
    id: Optional[int] = None
    name: str
    path: str
    status: str

