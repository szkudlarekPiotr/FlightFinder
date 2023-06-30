from flight_search import FlightSearch
from data_manager import DataManager


class FlightData:
    def __init__(self):
        self.search = FlightSearch()
        self.sheet_data = DataManager()
        self.flight_data = self.search.get_response()

    def manage_data(self):
        self.flight_data_formated = []
        if self.flight_data:
            for flight in self.flight_data:
                self.city_to = flight[0]["cityTo"]
                self.price = flight[0]["price"]
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
                self.outbound_time = self.outbound_data[0].split("T")[1].split(".")[0]

                self.return_date = self.return_data[0].split("T")[0]
                self.return_time = self.return_data[0].split("T")[1].split(".")[0]

                self.flight_data_formated.append(
                    [
                        self.city_to,
                        self.price,
                        self.outbound_date,
                        self.outbound_time,
                        self.return_date,
                        self.return_time,
                    ]
                )

        self.sheet_data.update_price(self.flight_data_formated)
