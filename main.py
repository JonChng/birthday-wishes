##################### Extra Hard Starting Project ######################

import smtplib
import datetime as dt
from random import choice
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]

files = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")
date = dt.datetime.now()

for i, row in birthdays.iterrows():
    current_day = date.day
    current_month = date.month
    if current_month == row["month"] and current_day == row["day"]:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = choice(files)
        print(letter)
        with open(f"letter_templates/{letter}", "r") as file:
            content = file.read()
        content = content.replace("[NAME]", row["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs="aleisurex@gmail.com", msg=f"Subject:Happy Birthday!\n\n{content}")






