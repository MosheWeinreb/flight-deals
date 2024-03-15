import requests
import os





base_url = "https://api.sheety.co/90b7aa0b5f48a55b01f5992393c38d7c/copyOfFlightDeals/users"

def post_new_row(first_name, last_name, email):
    

  

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=base_url, json=body)
    response.raise_for_status()
    print(response.text)