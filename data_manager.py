import requests
import os
import json


class DataManager:
    def __init__(self):
        self.get_endpoint = (
            "https://api.sheety.co/8bc6d06884cdbc46994cdb6d09466dab/flightPrices/prices"
        )

        self.auth_headers = {"Authorization": os.environ["SHEETY_API_HEADER"]}

        self.get_response = requests.get(
            url=self.get_endpoint, headers=self.auth_headers
        )

        self.get_response.raise_for_status()
        self.data = self.get_response.json()["prices"]

    def upload_data(self, price, row_id):
        self.put_endpoint = f"https://api.sheety.co/8bc6d06884cdbc46994cdb6d09466dab/flightPrices/prices/{row_id}"
        self.payload_dict = {"prices": {"lowestPrice": price}}
        self.payload_json = json.dumps(self.payload_dict)
        self.post_response = requests.put(
            url=self.put_endpoint, headers=self.auth_headers, data=self.payload_json
        )
        self.post_response.raise_for_status()
        print(type(self.payload_json))

    def update_price(self, flights):
        for x in range(len(flights)):
            if flights[x][0] == self.data[x]["city"]:
                print(flights[x][1], self.data[x]["id"])
