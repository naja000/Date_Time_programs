import time
import datetime
print("Current date: ",datetime.datetime.now())
print("Current year: ",datetime.date.today().strftime("%Y"))
print("Month of year: ",datetime.date.today().strftime("%B"))
print("Week number of the year: ",datetime.date.today().strftime("%W"))
print("Week day of the week: ",datetime.date.today().strftime("%w"))
print("Day of year: ",datetime.date.today().strftime("%j"))
print("Day of month: ",datetime.date.today().strftime("%d"))
print("Day of week: ",datetime.date.today().strftime("%A"))
print("-------------------------------------------------------------------------")

from datetime import date,timedelta
dt = date.today()-timedelta(7)
print(timedelta(7))
print("Current Date: ",date.today())
print("7 days before current date: ",dt)
print("------------------------------------------------------------------------")

import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(1)
tomorrow = today + datetime.timedelta(1)
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)
print("------------------------------------------------")

def all_sundays(year):
    dt=date(year,1,1)
    print(dt.weekday())
    dt += timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt +=timedelta(days=7)

for s in all_sundays(2020):
    print(s)

print("----------------------------------------------")

from datetime import date
a=date(2000,2,28)
b=date(2002,5,27)
print(b-a)
print("------------------------------------------------")

from calendar import monthrange
year=2022
month=2
print(monthrange(year,month)[1])