import smtplib
from twilio.rest import Client




MY_ACCOUNT_SID = "AC5446eb4b4ada70cc13d04a7534d5b49c"
MY_AUTH_TOKEN = "a718be83c808e2d995a2c9240763b8ea"
TWILIO_VERIFIED_NUMBER = "+97254910904"
TWILIO_VIRTUAL_NUMBER = "+14243425567"
MAIL_PROVIDER_SMTP_ADDRESS ="smtp.gmail.com"
MY_EMAIL = "tommyshelbyakabmw@gmail.com"
MY_PASSWORD = "jzlzhjvewxrcbbzm"


class NotificationManager:

    def __init__(self):
        self.client = Client(MY_ACCOUNT_SID, MY_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS,587) as connection:
            try:
                connection.starttls()
            except smtplib.SMTPNotSupportedError:
                print( "Server doesn't support TLS. Using plain-text authentication (not recommended)." )
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
            connection.close()
