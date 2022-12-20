#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=12, minutes=45))

# print today's date
now = datetime.now()
print("Today is ", now)

# print today's date one year from now
print("One year from now it will be", str(now + timedelta(days=365)))  # Mi van szokoevben

# create a timedelta that uses more than one argument
print("In two weeks and three days it will be", str(now + timedelta(weeks=2, days=3)))

# calculate the date 1 week ago, formatted as a string
oneWeekAgo = datetime.now() - timedelta(weeks=1)
oneWeekAgoAsString = oneWeekAgo.strftime("%A %B %d %Y")
print("One week ago was", oneWeekAgoAsString)

# How many days until April Fools' Day?
today = date.today()
aprilFoolsDay = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if aprilFoolsDay < today:
    print("April Fools' Day already went by", (today - aprilFoolsDay).days, "days.")
    aprilFoolsDay = aprilFoolsDay.replace(year=today.year + 1)
elif aprilFoolsDay == today:
    print("April Fools' Day is today")
else:
    print("April Fools' Day will be within", (aprilFoolsDay - today).days, "days")

# Now calculate the amount of time until April Fool's Day
timeToAprilFool = aprilFoolsDay - today
print("It's", timeToAprilFool.days, "days until the next April Fools Day!")
