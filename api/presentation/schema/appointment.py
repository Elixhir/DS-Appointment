from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AppointmentSchema(BaseModel):
    date_time: datetime
    service: Optional[str] = None
    clientPhone: int
    notes: Optional[str] = None
        
    class Config:
        from_attributes = True