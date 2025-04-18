from api.domain.gateway.appointment import AppointmentGateway
from sqlalchemy.orm import Session
from api.infrastructure.model.appointment import Appointment

class AppointmentRepository(AppointmentGateway):
    def __init__(self, db : Session):
        self.db = db
    
    def create_appointment(self, data: Appointment, user_id: int):
        appointment = Appointment(
            date_time=data.date_time,
            service=data.service,
            notes=data.notes,
            user_id=user_id
        )
        self.db.add(appointment)
        self.db.commit()
        self.db.refresh(appointment)
        return appointment