from datetime import datetime, timedelta
from api.infrastructure.model.appointment import Appointment
from api.infrastructure.database.db_connection import get_db
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from sqlalchemy.orm import joinedload

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

SENDER_EMAIL = os.getenv("GMAIL_USER")
SENDER_PASSWORD = os.getenv("GMAIL_PASSWORD")

def send_appointment_reminder(to_email, appointment_datetime):
    subject = "Recordatorio de cita"
    body = f"""Hola,
Tu cita está próxima. Recuerda que está programada para el día {appointment_datetime.strftime('%Y-%m-%d %H:%M')}."""

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
            print(f"Correo enviado a {to_email}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

def notify_three_days_before():
    print(f"Email: {SENDER_EMAIL}, Password: {SENDER_PASSWORD}")
    db = next(get_db())
    try:
        now = datetime.utcnow()
        appointments = db.query(Appointment)\
            .options(joinedload(Appointment.user))\
            .filter(Appointment.reminder_sent == False).all()

        for appt in appointments:
            print(f"Revisando cita ID {appt.id} para {appt.date_time}")
            if timedelta(0) < (appt.date_time - now) <= timedelta(days=3):
                user = appt.user
                print(f"Usuario: {user}, Email: {user.email if user else 'N/A'}")
                if user and user.email:
                    send_appointment_reminder(user.email, appt.date_time)
                    appt.reminder_sent = True
                    db.commit()
                    print(f"Recordatorio marcado como enviado para cita ID {appt.id}")
                else:
                    print(f"Usuario o email no válido para cita ID {appt.id}")
            else:
                print(f"Cita ID {appt.id} no está dentro del rango de 3 días")

    finally:
        db.close()
