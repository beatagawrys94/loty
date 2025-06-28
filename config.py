# config.py

import os

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp-relay.sendinblue.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "908317001@smtp-brevo.com")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "RM0ymJqpDF417nkg")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "beatka1433@gmail.com")

SKYSCANNER_URL = os.getenv("https://www.skyscanner.pl/transport/loty/wars/bkkt/251226/260114/?adultsv2=2&cabinclass=economy&childrenv2=&ref=home&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false")  # wkleimy stały link jako zmienną
MAX_PRICE = int(os.getenv("MAX_PRICE", "3900"))
MAX_DURATION_HOURS = int(os.getenv("MAX_DURATION_HOURS", "20"))

