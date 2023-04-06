from helper import generateRandomCode
from helper import sendEmail
from helper import read_file
from email.mime.text import MIMEText
from model import User
import os
from dotenv import load_dotenv

def Load_Users():
    usersF = read_file('data/user.txt')
    users = []
    for userline in usersF:
        userinfo = userline.split(":")
        user = User(int(userinfo[0]), userinfo[1],
                    userinfo[2], userinfo[3], userinfo[4], userinfo[5])
        users.append(user)
    return users

users = Load_Users()

def check_user(email):
    for user in users:
        if user.get_email() == email:
            return True, user
    return False, None


def Verify(email):
    load_dotenv()
    sender_email = os.getenv("SENDER_EMAIL",  None)
    assert sender_email is not None, "Failed to get SENDER_EMAIL from ENV VARS"
    while True:
        verifyCode = generateRandomCode()
        message = MIMEText(f"""\
        Your Verification Code is : {verifyCode}.""")
        message['From']=sender_email
        message['Subject'] = "Verify Crowd-Funding App "
        sendEmail(email, message.as_string())
        inVcode = input("Please Enter Verification Code: ")
        if inVcode == verifyCode:
            print("Welcome to Our system")
            return True
        else:
            print("Wrong code send another one Y(default) or (exit)? ")
            choice = input("#>>")
            if choice == "exit":
                return False
            else:
                continue

