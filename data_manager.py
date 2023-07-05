import requests
import os

SHEETDB_AUTH = os.environ["SHEETDB_HEADER"]
SHEETDB_ENDPOINT = "https://sheetdb.io/api/v1/0e322pvdjssna"


class DataManager:
    def __init__(self):
        self.auth_header = {"Authorization": SHEETDB_AUTH}

    def get_response(self):
        self.response = requests.get(url=SHEETDB_ENDPOINT, headers=self.auth_header)
        self.response.raise_for_status()
        self.data = self.response.json()
        return self.data

    def upload_data(self, price, city):
        self.put_endpoint = f"{SHEETDB_ENDPOINT}/City/{city}"
        self.payload = {"Lowest Price": price}
        self.put_response = requests.put(
            url=self.put_endpoint, headers=self.auth_header, json=self.payload
        )
        self.put_response.raise_for_status()

    def update_price(self, flights):
        for x in range(len(flights)):
            if any(flights[x][0] in data["City"] for data in self.data):
                self.upload_data(flights[x][1], flights[x][0])
