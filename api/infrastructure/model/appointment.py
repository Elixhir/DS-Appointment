from datetime import datetime, timedelta
from .base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime, nullable=False, index=True)
    clientPhone = Column(Integer, nullable= False)
    service = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    reminder_sent = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="appointments")

    created_at = Column(DateTime, default=datetime.utcnow)