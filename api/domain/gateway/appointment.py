from abc import ABC,abstractmethod
from api.domain.entity.appointment import Appointment

class AppointmentGateway(ABC):

    @abstractmethod
    def create_appointment(self, appointment, user_id) -> Appointment:
        pass

    @abstractmethod
    def get_appointment_by_user_id(self, user_id) -> list[Appointment]:
        pass

    @abstractmethod
    def get_appointments(self,admin_user) -> list[Appointment]:
        pass

    @abstractmethod
    def delete_appointment(self, appointment_id):
        pass

    @abstractmethod
    def get_appointment_by_id(self, id):
        pass