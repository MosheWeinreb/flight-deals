# import requests
# from datetime import datetime as dt, timedelta
#
#
# TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
# TEQUILA_API_KEY = "DMMncXGp6pKjarGvpUyNP3iRFU80X2o-"
# CURRENCY = "GBP"
#
# current_datetime = dt.now()
# future_datetime = current_datetime + timedelta(days=1)
#
# current_date_str = current_datetime.strftime("%m/%d/%Y")
# future_date_str = future_datetime.strftime("%m/%d/%Y")
#
# print (current_date_str)
# print (future_date_str)


class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date



