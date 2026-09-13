# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
# import os and use it to get the Github repository secrets

email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

import smtplib
import datetime as dt
from random import choice
import pandas

def send_email(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="itsmegift@gmail.com",
                            msg=f"Subject:Happy Birthday!!! \n\n {message}"
                        )

#Choose the Email Template and change name
def create_email(name):
    template_no = choice([1, 2, 3])
    with open(f"letter_templates/letter_{template_no}.txt") as template:
        email_text = template.read()
        updated_email_text = email_text.replace("[NAME]",name)
        send_email(updated_email_text)

# READ THE CSV FILE
birthday_df = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_df.to_dict(orient="records")

now = dt.datetime.now()

for person in birthday_dict:
    if person["month"] == now.month and person["day"] == now.day:
        create_email(person["name"])

date_month_tuple = {(row.day,row.month): row for (index,row) in birthday_df.iterrows()}
print(date_month_tuple)
