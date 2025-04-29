from api.domain.gateway.appointment import AppointmentGateway
from sqlalchemy.orm import Session
from api.infrastructure.model.appointment import Appointment
from api.infrastructure.model.user import User

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
    
    def get_appointment_by_user_id(self, user_id):
        return self.db.query(Appointment).filter(
            Appointment.user_id == user_id
            ).order_by(Appointment.date_time.asc()).all()
    
    def get_appointments(self, admin_user: User):
        if not admin_user.is_admin:
            raise PermissionError("Access denied: Only admins can view all appointments.")
        return (
            self.db.query(Appointment)
            .order_by(Appointment.date_time.asc())
            .all()
        )
    
    def delete_appointment(self, appointment_id):
        appointment = self.db.query(Appointment).filter(Appointment.id == appointment_id).first()
        if appointment is None:
            raise ValueError("Appointment not found")
        self.db.delete(appointment)
        self.db.commit()
        return {"message": "Appointment deleted successfully"}
    
    def get_appointment_by_id(self, appointment_id: int):
        return self.db.query(Appointment).filter(Appointment.id == appointment_id).first()

    def delete_appointment(self, appointment_id: int):
        appointment = self.get_appointment_by_id(appointment_id)
        if appointment:
            self.db.delete(appointment)
            self.db.commit()
