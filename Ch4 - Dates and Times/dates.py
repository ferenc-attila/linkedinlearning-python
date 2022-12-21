#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is", today)

    # print out the date's individual components
    print("Date components: day:", today.day, "months:", today.month, "year:", today.year)
    
    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today`s weekday is", today.weekday())
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print("Which is", days[today.weekday()])
    
    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is", today)
    
    # Get the current time
    time = datetime.time(datetime.now())
    print("The current time is", time)
  
if __name__ == "__main__":
    main()
  