TASK1:write a function to return the day of the date


import datetime

def find_day(date):
    d = datetime.datetime.strptime(date, "%d-%m-%Y")
    return d.strftime("%A")

date = input("Enter date (dd-mm-yyyy): ")
print("Day is:", find_day(date))


TASK2:take input of hours+ your next notification will be in



from datetime import datetime, timedelta

hours = int(input("Enter hours: "))

current_time = datetime.now()
next_notification = current_time + timedelta(hours=hours)

print("Your next notification will be in:", next_notification)