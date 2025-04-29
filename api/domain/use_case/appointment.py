from api.domain.gateway.appointment import AppointmentGateway
from api.domain.entity.appointment import Appointment

class AppointmentService:
    
    def __init__(self, gateway: AppointmentGateway):
        self.gateway = gateway

    def create_appointment(self, appointment , user_id) -> Appointment :
        return self.gateway.create_appointment(appointment, user_id)
    
    def get_appointment_by_user_id(self, user_id) -> list[Appointment]:
        return self.gateway.get_appointment_by_user_id(user_id)
    
    def get_appointments(self, admin_user) -> list[Appointment]:
        return self.gateway.get_appointments(admin_user)
    
    def delete_appointment(self, appointment_id):
        return self.gateway.delete_appointment(appointment_id)
    
    def get_appointment_by_id(self, id):
        return self.gateway.get_appointment_by_id(id)