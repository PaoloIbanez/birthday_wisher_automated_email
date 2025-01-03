##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas
import datetime as dt
import smtplib
import random

# 1. Get today's date
now = dt.datetime.now()
today_month = now.month
today_day = now.day

# 2. Read the birthdays CSV
data = pandas.read_csv("birthdays.csv")

# 3. Loop through rows in the DataFrame to see if any match today's date
for (index, row) in data.iterrows():
    if row["month"] == today_month and row["day"] == today_day:
        # 4. Pick a random letter template
        letter_files = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        chosen_letter = random.choice(letter_files)

        # 5. Read the file and replace [NAME] with person's actual name
        with open(f"letter_templates/{chosen_letter}", "r") as letter_file:
            letter_contents = letter_file.read()
        personalized_letter = letter_contents.replace("[NAME]", row["name"])

        # 6. Send the email
        my_email = "EXAMPLE@gmail.com"
        my_password = "EXAMPLE"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
            )






# my_email = "paolochamba@gmail.com"
# my_password = "ayxy ylra beji iyzt"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # start tls is to secure it
#     connection.starttls()
#     # then we login
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=row["email"],
#                         msg=f"Subject:Monday Motivation\n\n {}")


