from flight_search import FlightSearch


class FlightData:
    def __init__(self):
        self.search = FlightSearch()
        self.data = self.search.get_response()

    def manage_data(self):
        for item in self.data:
            if item["data"]:
                self.city_from = item["data"][0]["cityFrom"]
                self.city_to = item["data"][0]["cityTo"]
                self.price = (
                    f"{item['data'][0]['price']} {self.search.parameters['curr']}"
                )
                self.to_departure = item["data"][0]["route"][0][
                    "local_departure"
                ].split("T")
                self.to_departure_date = self.to_departure[0]
                self.to_departure_time = self.to_departure[1].split(".")[0]
                self.return_departure = item["data"][0]["route"][1][
                    "local_departure"
                ].split("T")
                self.return_departure_date = self.return_departure[0]
                self.return_departure_time = self.return_departure[1].split(".")[0]
                self.link = item["data"][0]["deep_link"]
                print(
                    self.city_from,
                    self.city_to,
                    self.price,
                    self.to_departure_date,
                    self.to_departure_time,
                    self.return_departure_date,
                    self.return_departure_time,
                    self.link,
                    sep="\n",
                )
