import requests
import os
from datetime import date, timedelta


class FlightSearch:
    def __init__(self):
        # TODO: move api key to env variables
        self.api_key = os.environ["FLIGHT_API_KEY"]
        self.today_unformated = date.today()
        self.next_week_unformated = self.today_unformated + timedelta(days=7)
        self.two_weeks_unformated = self.today_unformated + timedelta(days=14)
        self.three_weeks_unformated = self.today_unformated + timedelta(days=21)
        self.today = self.today_unformated.strftime("%d/%m/%Y")
        self.next_week = self.next_week_unformated.strftime("%d/%m/%Y")
        self.two_weeks = self.two_weeks_unformated.strftime("%d/%m/%Y")
        self.three_weeks = self.three_weeks_unformated.strftime("%d/%m/%Y")

    def get_response(self):
        self.endpoint = "https://api.tequila.kiwi.com/v2/search?"
        self.parameters = {
            "fly_from": "POZ",
            "fly_to": "WAW",
            "dateFrom": self.today,
            "dateTo": self.next_week,
            "return_from": self.two_weeks,
            "return_to": self.three_weeks,
            "limit": 1,
            "curr": "PLN",
        }
        self.auth_header = {"apikey": self.api_key}
        self.response = requests.get(
            url=self.endpoint,
            headers=self.auth_header,
            params=self.parameters,
        )
        self.response.raise_for_status()
        data = self.response.json()

        return data
