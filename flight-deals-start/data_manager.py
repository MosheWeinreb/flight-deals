import os
SHEETY_ENDPOINT = "https://api.sheety.co/90b7aa0b5f48a55b01f5992393c38d7c/copyOfFlightDeals/prices"
SHEETY_API_KEY = "691880a88b71fa76e32dad581b1842d7"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/90b7aa0b5f48a55b01f5992393c38d7c/copyOfFlightDeals/users"

APP_ID="f56c4413"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": SHEETY_API_KEY,
}




SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/90b7aa0b5f48a55b01f5992393c38d7c/copyOfFlightDeals/prices"


from pprint import pprint
import requests
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get( url=customers_endpoint )
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data





