"""
birthday.py
Author: Finn
Credit: none
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
todaymonth = month_name[todaymonth]
name = input("Hello, what is your name? ")
month = input("Hi, {0}, what was the name of the month you were born in? " .format(name))
year = input("And what year were you born in, {0}? " .format(name))
day = input("And the day? ")

if month == "October":
    halloweenmonth = "yes"
else:
    halloweenmonth = "no"

if day == "31":
    halloweenday = "yes"
else:
    halloweenday = "no"

if halloweenday == "yes" and halloweenmonth == "yes":
    halloween = "yes"
else:
    halloween = "no"

if todaymonth == month:
    birthmonth = "yes"
else:
    birthmonth = "no"

if todaydate == day:
    birthday = "yes"
else:
    birthday = "no"

if birthday == "yes" and birthmonth == "yes":
    birthdate = "yes"
else:
    birthdate = "no"
if month == "June" or "July" or "August":
    season = "summer"
elif month == "March" or "April" or "May":
    season = "spring"
elif month == "September" or "October" or "November":
    season = "fall"
elif month == "December" or "January" or "February":
    season = "winter"
else:
    season = "You didn't give me a season!"

print(season)
print(birthday)
print(todaymonth)

