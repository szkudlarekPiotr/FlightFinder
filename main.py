from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import Notification

flight_data_manager = FlightData()
flight_search_enginge = FlightSearch()
sheet_data_manager = DataManager()
notification_manager = Notification()

sheet_data = sheet_data_manager.get_response()

flight_data = flight_search_enginge.get_response(sheet_data)

fomratted_f_data = flight_data_manager.manage_data(flight_data)

sheet_data_manager.update_price(fomratted_f_data)

for item in fomratted_f_data:
    notification_manager.send_sms(item)
