#!/usr/bin/python

import datetime as dt

print("\n====================Date===================\n")

current_date = dt.date.today()
print(current_date)

date1 = dt.date(2021, 12, 5)
print(date1)
print("Year:", date1.year)
print("Month:", date1.month)
print("Day:", date1.day)

print("\n====================Time===================\n")

time1 = dt.time(10, 45, 30, 45666)
print(time1)
print("Hour:", time1.hour)
print("Minute:", time1.minute)
print("Seconds:", time1.second)
print("Microseconds:", time1.microsecond)

print("\n====================DateTime===================\n")
datetime_obj = dt.datetime(2021, 11, 28, 23, 55, 59, 8000)
print(datetime_obj)
print("Date:", datetime_obj.date())
print("Time:", datetime_obj.time())

print("\n====================Current datetime===================\n")

current_datetime = dt.datetime.now()
print("Current Date:", current_datetime)

print("\n====================DateTimeDelta===================\n")

next_new_year = dt.datetime(2022, 1, 1)
time_remaining = next_new_year - current_datetime
print("Remaining time:", time_remaining)
print("Remaining time type:", type(time_remaining))

print("\n====================strftime()===================\n")
date_string = current_datetime.strftime("%A, %B %d, %Y")
print("%A, %B %d, %Y -", date_string)

date_string = current_datetime.strftime("%a, %b %d, %y")
print("%a, %b %d, %y -", date_string)

date_string = current_datetime.strftime("%b, %-d %I%p")
print("%b, %-d %I%p -", date_string)

print("\n====================strptime()===================\n")
date_string = "21 June, 2021"
datetime_obj = dt.datetime.strptime(date_string, "%d %B, %Y")
print("21 June, 2021 - %d %B, %y", datetime_obj)

print("\n====================timezone===================\n")

from pytz import timezone
import pytz

utc = pytz.utc
utc_datetime = utc.localize(current_datetime)
print("UTC: ", utc_datetime)

ist = pytz.timezone("Asia/Kolkata")
ist_datetime = ist.localize(current_datetime)
print("IST: ", ist_datetime)

print("\n====================timestamp===================\n")
now = dt.datetime.now()

timestamp = dt.datetime.timestamp(now)
print("Timestamp: ", timestamp)
