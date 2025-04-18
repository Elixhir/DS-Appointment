from api.presentation.schema.appointment import AppointmentSchema
from api.infrastructure.repository.appointment import AppointmentRepository
from fastapi import Depends,APIRouter
from api.infrastructure.database.db_connection import get_db
from api.domain.use_case.appointment import AppointmentService
from sqlalchemy.orm import Session
from api.infrastructure.model.appointment import Appointment
from api.dependencies.user_auth import get_current_user

def get_appointment_service(db = Depends(get_db)):
    repository = AppointmentRepository(db)
    return AppointmentService(repository)

appointment_router = APIRouter()

@appointment_router.post("/appointment", response_model=AppointmentSchema)
def create_appointment(
    data: AppointmentSchema,
    current_user: dict = Depends(get_current_user),
    appointment_service : AppointmentService = Depends(get_appointment_service)
):
    appointment = appointment_service.create_appointment(data, current_user.id)
    
    return appointment