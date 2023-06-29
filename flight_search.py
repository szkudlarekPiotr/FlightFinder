import requests
import os
from datetime import date, timedelta
from data_manager import DataManager


class FlightSearch:
    def __init__(self):
        self.sheet_data = DataManager().data
        self.sheet = self.sheet_data["prices"]
        self.api_key = os.environ["FLIGHT_API_KEY"]
        self.cities = [item["city"] for item in self.sheet_data["prices"]]
        self.iataCodes = [item["iataCode"] for item in self.sheet_data["prices"]]
        self.prices = [item["lowestPrice"] for item in self.sheet_data["prices"]]
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
        self.auth_header = {"apikey": self.api_key}
        self.possible_outputs = []
        for item in self.sheet:
            self.parameters = {
                "fly_from": "WAW",
                "fly_to": item["iataCode"],
                "price_to": int(item["lowestPrice"]),
                "date_from": self.today,
                "date_to": self.next_week,
                "return_from": self.two_weeks,
                "return_to": self.three_weeks,
                "sort": "price",
                "limit": 1,
                "curr": "GBP",
            }
            self.response = requests.get(
                url=self.endpoint,
                headers=self.auth_header,
                params=self.parameters,
            )
            self.response.raise_for_status()
            data = self.response.json()

            self.possible_outputs.append(data)

        return self.possible_outputs
