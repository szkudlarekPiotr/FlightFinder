from twilio.rest import Client
import os

TWILIO_ACC_SID = os.environ["TWILIO_ACC_SID"]
TWILIO_AUTH = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = os.environ["TWILIO_FROM_NUMBER"]
MY_NUMBER = os.environ["MY_PHONE_NUMBER"]


class Notification:
    def __init__(self, flight_info):
        (
            self.city_to,
            self.price,
            self.dep_date,
            self.return_date,
            self.link,
        ) = flight_info
        self.client = Client(TWILIO_ACC_SID, TWILIO_AUTH)

    def send_sms(self):
        self.msg_body = (
            f"New cheap flight found! From Warsaw to {self.city_to},"
            f"for only {self.price} £! Departure date: {self.dep_date}\n"
            f"return flight date: {self.return_date}.\n Link: {self.link}"
        )

        self.message = self.client.messages.create(
            body=self.msg_body, from_=TWILIO_PHONE_NUMBER, to=MY_NUMBER
        )
