from api.presentation.schema.appointment import AppointmentSchema
from api.infrastructure.repository.appointment import AppointmentRepository
from fastapi import Depends,APIRouter
from api.infrastructure.database.db_connection import get_db
from api.domain.use_case.appointment import AppointmentService
from api.dependencies.user_auth import get_current_user,get_admin_user
from api.infrastructure.model.user import User

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

@appointment_router.get("/appointments")
def get_appointment_by_user(
    current_user: dict = Depends(get_current_user),
    appointment_service : AppointmentService = Depends(get_appointment_service), 
):
    return appointment_service.get_appointment_by_user_id(current_user.id)

@appointment_router.get("/all_appointments")
def get_all_appointments(
    admin_user: User = Depends(get_admin_user),
    appointment_service: AppointmentService = Depends(get_appointment_service)
):
    return appointment_service.get_appointments(admin_user)

@appointment_router.delete("/appointments/{appointment_id}")
def delete_appointment(
    appointment_id: int,
    appointment_service: AppointmentService = Depends(get_appointment_service)
):
    return appointment_service.delete_appointment(appointment_id)

@appointment_router.get("/appointment")
def get_appointment_by_id(
    appointment_id: int,
    appointment_service: AppointmentService = Depends(get_appointment_service)
):
    return appointment_service.get_appointment_by_id(appointment_id)