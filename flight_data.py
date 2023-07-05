from flight_search import FlightSearch
from data_manager import DataManager


class FlightData:
    def __init__(self):
        pass

    def manage_data(self, flight_data):
        self.flight_data = flight_data
        self.flight_data_formated = []
        for flight in self.flight_data:
            if flight:
                self.city_to = flight[0]["cityTo"]
                self.price = flight[0]["price"]
                self.link = flight[0]["deep_link"]
                self.outbound_data = [
                    item["local_departure"]
                    for item in flight[0]["route"]
                    if item["return"] == 0
                ]
                self.return_data = [
                    item["local_departure"]
                    for item in flight[0]["route"]
                    if item["return"] == 1
                ]

                self.outbound_date = self.outbound_data[0].split("T")[0]
                self.return_date = self.return_data[0].split("T")[0]

                self.flight_data_formated.append(
                    [
                        self.city_to,
                        self.price,
                        self.outbound_date,
                        self.return_date,
                        self.link,
                    ]
                )

        return self.flight_data_formated
