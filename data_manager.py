import requests
import os


class DataManager:
    def __init__(self):
        self.prices_endpoint = (
            "https://api.sheety.co/8bc6d06884cdbc46994cdb6d09466dab/flightPrices/prices"
        )

        self.auth_headers = {"Authorization": os.environ["SHEETY_API_HEADER"]}

        self.response = requests.get(
            url=self.prices_endpoint, headers=self.auth_headers
        )

        self.response.raise_for_status()
        self.data = self.response.json()
