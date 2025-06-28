# main.py

import requests
from datetime import datetime
from config import *
from emailer import send_email

def search_flights():
    url = "https://api.tequila.kiwi.com/v2/search"

    headers = {
        "apikey": "tequila-api-key-niepotrzebny"  # Nie wymagany, ale warto podać dummy
    }

    params = {
        "fly_from": FROM,
        "fly_to": TO,
        "date_from": DEPARTURE_DATE,
        "date_to": DEPARTURE_DATE,
        "return_from": RETURN_DATE,
        "return_to": RETURN_DATE,
        "curr": "PLN",
        "limit": 10,
        "sort": "price",
        "max_flight_duration": MAX_DURATION_HOURS
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Błąd API:", response.status_code)
        return

    data = response.json()

    for flight in data.get("data", []):
        price = flight["price"]
        route = flight["route"]
        duration = flight["fly_duration"]

        if price <= MAX_PRICE:
            booking_link = flight.get("deep_link", "https://www.kiwi.com")
            message = f"Znaleziono lot za {price} zł!\n\nTrasa: {FROM} → {TO}\nWylot: {DEPARTURE_DATE}\nPowrót: {RETURN_DATE}\nCzas lotu: {duration}\n\nRezerwuj: {booking_link}"
            send_email(f"🛫 Lot do Tajlandii za {price} zł!", message)
            print("Wysłano alert!")
            return

    print("Brak lotów spełniających kryteria.")

if __name__ == "__main__":
    search_flights()
