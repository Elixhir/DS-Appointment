from api.domain.gateway.appointment import AppointmentGateway
from api.domain.entity.appointment import Appointment

class AppointmentService:
    
    def __init__(self, gateway: AppointmentGateway):
        self.gateway = gateway

    def create_appointment(self, appointment , user_id) -> Appointment :
        return self.gateway.create_appointment(appointment, user_id)
    