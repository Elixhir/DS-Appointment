from datetime import datetime
from typing import Optional


class Appointment:
    def __init__(
        self,
        client_name: str,
        client_phone: str,
        date_time: datetime,
        service: Optional[str] = None,
        notes: Optional[str] = None,
        reminder_sent: bool = False,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
    ):
        self.id = id
        self.client_name = client_name
        self.client_phone = client_phone
        self.date_time = date_time
        self.service = service
        self.notes = notes
        self.reminder_sent = reminder_sent
        self.created_at = created_at or datetime.utcnow()