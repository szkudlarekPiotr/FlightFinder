import requests
import os
from datetime import date, timedelta
from data_manager import DataManager

TEQUILLA_API_KEY = os.environ["FLIGHT_API_KEY"]
TEQUILLA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search?"


class FlightSearch:
    def __init__(self):
        self.api_key = os.environ["FLIGHT_API_KEY"]
        self.auth_header = {"apikey": TEQUILLA_API_KEY}
        self.today_unformated = date.today()
        self.six_weeks = self.today_unformated + timedelta(days=30 * 6)
        self.today = self.today_unformated.strftime("%d/%m/%Y")
        self.six_months = self.six_weeks.strftime("%d/%m/%Y")

    def get_response(self, data):
        self.sheet_data = data
        self.possible_outputs = []
        for item in self.sheet_data:
            self.parameters = {
                "fly_from": "WAW",
                "fly_to": item["IATA Code"],
                "price_to": int(item["Lowest Price"]) - 1,
                "date_from": self.today,
                "date_to": self.six_months,
                "nights_in_dst_from": 4,
                "nights_in_dst_to": 10,
                "sort": "price",
                "limit": 1,
                "curr": "GBP",
            }
            self.response = requests.get(
                url=TEQUILLA_ENDPOINT,
                headers=self.auth_header,
                params=self.parameters,
            )
            self.response.raise_for_status()
            f_data = self.response.json()

            self.possible_outputs.append(f_data["data"])

        return self.possible_outputs
