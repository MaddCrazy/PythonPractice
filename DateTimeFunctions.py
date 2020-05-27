from datetime import time
from datetime import date
from datetime import datetime
import calendar


#Playing with time function
theTime = time(3,15)
print("The time is " + str(theTime))
hrs = theTime.hour
print(hrs)
print (theTime.minute)
theTime = theTime.replace(hour = 8)
print(theTime)
theTime = theTime.replace(second = 24)
print(theTime)


#Playing with the date function
theDate = date(1999,11,15)
print(theDate)
month = theDate.month
print(month)
print(theDate.year)
theDate = theDate.replace(day = 17)
print(theDate)
todaysDate = date.today()
print(todaysDate)
print(month)


#finds out the day of the week and month name
day = calendar.day_name[theDate.weekday()]
print(day)
month = theDate.month
month2 = calendar.month_name[month]
print(month2)


#Playing with the datetime function
dateAndTime = datetime(2019,2,25,10,22)
print(dateAndTime)
month = dateAndTime.month
print(month)
print(dateAndTime.minute)
dateAndTime = dateAndTime.replace(year = 2002, month = 11)
print(dateAndTime)
date = dateAndTime.date()
print(date)
print(dateAndTime.time())
dateTimeNow = datetime.today()
print(dateTimeNow)
print(dateTimeNow.date())
timeNow = dateTimeNow.time()
print(timeNow)


#Combined Function Play (commented out because you cannot redefine that date once its been defined)
#aTime = time(10,22,34)
#print(aTime)
#aDate = date(1998,10,9)
#print(aDate)
#aDateTime = datetime.combine(aDate, aTime)
#print(aDateTime)
