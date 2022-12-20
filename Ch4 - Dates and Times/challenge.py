# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar


def get_number_of_day():
    print("Which day of the week do you want to count?")
    for i in range(0, 7):
        print(i, ":", calendar.day_name[i])
    print("Or 'exit' to quit")
    day = input("? ")
    if day.lower() == "exit":
        print("Thanks for using this software. Good bye!")
        return day.lower() # Ez talan kicsit csunya, lehet, hogy ezt refaktoralni kellene
    else:
        try:
            index_of_day = int(day)
        except ValueError as ve:
            print(ve)
            index_of_day = -1
        if index_of_day not in range(0, 7):
            print("Invalid input. Try a number between zero and six!")
            get_number_of_day()
        return index_of_day


def get_number_of_month():
    month = input("Enter a month:")
    try:
        number_of_month = int(month)
    except ValueError as ve:
        print(ve)
        number_of_month = -1
    if number_of_month not in range(1, 13):
        print("Invalid input. Try a number between 1 and 12")
        get_number_of_month()
    else:
        return number_of_month


def get_number_of_year():
    year = input("Enter a year:")
    try:
        number_of_year = int(year)
    except ValueError as ve:
        print(ve)
        number_of_year = -1
    if number_of_year not in range(-10000, 10000):
        print("Invalid input. Try a number between -10000 and 10000")
        get_number_of_year()
    else:
        return number_of_year


def day_counter(day, month, year):
    number_of_given_day = 0
    calendar_of_given_month = calendar.monthcalendar(year, month)
    for week in calendar_of_given_month:
        if week[day] != 0:
            number_of_given_day += 1
    return number_of_given_day


numberOfDay = get_number_of_day()
while numberOfDay != "exit":
    numberOfMonth = get_number_of_month()
    numberOfYear = get_number_of_year()
    number_of_given_days_in_given_month = day_counter(numberOfDay, numberOfMonth, numberOfYear)
    print("There are", number_of_given_days_in_given_month, "in the month and year specified")
    numberOfDay = get_number_of_day()
