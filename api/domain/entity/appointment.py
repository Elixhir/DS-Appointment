from datetime import datetime
from typing import Optional


class Appointment:
    def __init__(
        self,
        clientPhone: int,
        date_time: datetime,
        service: Optional[str] = None,
        notes: Optional[str] = None,
        reminder_sent: bool = False,
        created_at: Optional[datetime] = None,
        id: Optional[int] = None,
    ):
        self.id = id

        self.date_time = date_time
        self.service = service
        self.clientPhone = clientPhone
        self.notes = notes
        self.reminder_sent = reminder_sent
        self.created_at = created_at or datetime.utcnow()