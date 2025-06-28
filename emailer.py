# emailer.py

import smtplib
from email.mime.text import MIMEText
from config import EMAIL_RECEIVER, SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD

def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
