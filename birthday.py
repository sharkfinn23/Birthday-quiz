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
month = str(input("Hi, {0}, what was the name of the month you were born in? " .format(name)))
year = int(input("And what year were you born in, {0}? " .format(name)))
day = int(input("And the day? "))

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

if month == "June" or month == "July" or month == "August":
    season = "summer"

elif month == "March" or month == "April" or month == "May":
    season = "spring"

elif month == "September" or month == "October" or month == "November":
    season = "fall"

elif month == "December" or month == "January" or month == "February":
    season = "winter"
else:
    season = "none"

if year >= 2000:
    yeard = "two thousands"
elif year <= 1980:
    yeard = "stone age"
elif year < 2000 and year >= 1990:
    yeard = "nineties"
elif year < 1990 and year >= 1980:
    yeard = "eighties"
else:
    yeard = "you gave me an invalid year"

if halloween == "yes":
    print("You were born on Halloween!")
else:
    if birthdate == "yes":
        print("Happy birthday!")
    else:
        print("{0}, you are a {1} baby of the {2}." .format(name, season, yeard))
