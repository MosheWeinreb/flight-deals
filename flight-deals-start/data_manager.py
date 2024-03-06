import requests
from pprint import pprint
SHEETY_ENDPOINT = "https://api.sheety.co/90b7aa0b5f48a55b01f5992393c38d7c/copyOfFlightDeals/prices"
API_KEY="691880a88b71fa76e32dad581b1842d7"
APP_ID="f56c4413"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}




SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/90b7aa0b5f48a55b01f5992393c38d7c/copyOfFlightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT,headers= headers)
        data = response.json()
        self.destination_data = data["prices"]
        pprint(data)
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

