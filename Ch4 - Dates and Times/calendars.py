#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#

# import the calendar module
import calendar

# create a plain text calendar
myCalendar = calendar.TextCalendar(calendar.MONDAY)
stringCalendar = myCalendar.formatmonth(2022, 12, 0, 0)
# print(stringCalendar)

# create an HTML formatted calendar
htmlCalendar = calendar.HTMLCalendar(calendar.SUNDAY)
htmlCalendarString = htmlCalendar.formatmonth(2022, 1, True)
# htmlFile = open("calendar.html", "w+")
# htmlFile.write(htmlCalendarString)
# htmlFile.close()

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# for i in myCalendar.itermonthdays(2022, 8):
#     print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on:")
for month in range(1, 13):
    cal = calendar.monthcalendar(2022, month)
    weekOne = cal[0]
    weekTwo = cal[1]
    if weekOne[calendar.FRIDAY] != 0:
        meetDay = weekOne[calendar.FRIDAY]
    else:
        meetDay = weekTwo[calendar.FRIDAY]
    print(calendar.month_name[month], meetDay)
