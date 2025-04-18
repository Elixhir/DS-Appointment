from abc import ABC,abstractmethod
from api.domain.entity.appointment import Appointment

class AppointmentGateway(ABC):

    @abstractmethod
    def create_appointment(self, appointment, user_id) -> Appointment:
        pass