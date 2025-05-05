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
    subject = "Appointment reminder"
    body = f"""Hello, thank you for choosing Remodeling DS LLC and request our services.
We would like to remind you that your appointment is coming up, scheduled for {appointment_datetime.strftime('%Y-%m-%d, %H:%M')}."""

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
            if timedelta(0) < (appt.date_time - now) <= timedelta(days=3):
                user = appt.user
                if user and user.email:
                    send_appointment_reminder(user.email, appt.date_time)
                    appt.reminder_sent = True
                    db.commit()

    finally:
        db.close()
