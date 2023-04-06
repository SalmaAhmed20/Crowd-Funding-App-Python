import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
sender_email = os.getenv("SENDER_EMAIL",  None)
assert sender_email is not None, "Failed to get SENDER_EMAIL from ENV VARS"

def sendEmail(recEmail,msg):
    password = os.getenv("PASSWORD",  None)
    assert password is not None, "Failed to get PASSWORD from ENV VARS"
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recEmail, msg)

    print("Email sent successfully!")
    print("Check your inbox or junks/spam")