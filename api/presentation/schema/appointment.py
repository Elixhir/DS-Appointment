from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AppointmentSchema(BaseModel):
    date_time: datetime
    service: Optional[str]
    notes: Optional[str]
        
    class Config:
        from_attributes = True