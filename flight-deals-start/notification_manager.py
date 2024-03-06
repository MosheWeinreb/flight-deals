from flight_data import FlightData
from twilio.rest import Client


MY_ACCOUNT_SID = "AC5446eb4b4ada70cc13d04a7534d5b49c"
MY_AUTH_TOKEN = "a718be83c808e2d995a2c9240763b8ea"


class Notification_manager:

    def __init__(self):
        self.client = Client( MY_ACCOUNT_SID, MY_AUTH_TOKEN )
    def send_sms(self, message):
        message = self.client.messages.create(
            body= message,
            from_='+14243425567',
            to=input("enter your phone number"),
        )
        # Prints if successfully sent.
        print(f"message sent to {message}")
        exit()

