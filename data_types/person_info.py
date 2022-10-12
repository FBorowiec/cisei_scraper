from datetime import date
from typing import Dict, Optional

from pydantic import BaseModel


class PersonInfo(BaseModel):
    idx: int
    surname: str
    full_name: str
    age: Optional[int] = None
    trip_date: Optional[date]
    registration_place: str
    url: str
    details: Optional[Dict]
