from pydantic import BaseModel
from datetime import date

class Festival(BaseModel):
    name: str
    location: str
    startDate: date
    endDate: date
    province: str
    comment: str = None
