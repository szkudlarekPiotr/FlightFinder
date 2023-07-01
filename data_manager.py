import requests
import os
from notification_manager import Notification

SHEETY_ATUH = os.environ["SHEETY_API_HEADER"]
SHEETY_ENDPOINT = (
    "https://api.sheety.co/8bc6d06884cdbc46994cdb6d09466dab/flightPrices/prices"
)


class DataManager:
    def __init__(self):
        self.auth_headers = {"Authorization": SHEETY_ATUH}
        self.get_response = requests.get(url=SHEETY_ENDPOINT, headers=self.auth_headers)
        self.get_response.raise_for_status()
        self.data = self.get_response.json()["prices"]

    def upload_data(self, price, row_id):
        self.put_endpoint = f"{SHEETY_ENDPOINT}/{row_id}"
        self.payload_dict = {"price": {"lowestPrice": price}}
        self.post_response = requests.put(
            url=self.put_endpoint, headers=self.auth_headers, json=self.payload_dict
        )
        self.post_response.raise_for_status()

    def update_price(self, flights):
        for x in range(len(flights)):
            if any(flights[x][0] in data["city"] for data in self.data):
                self.city_id = [
                    item["id"] for item in self.data if item["city"] == flights[x][0]
                ]
                self.notification = Notification(flights[x])
                self.notification.send_sms()
                self.upload_data(flights[x][1], *self.city_id)
