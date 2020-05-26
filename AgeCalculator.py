from datetime import datetime
Year = int(input("Please enter the year your were born: "))
Month = int(input("Please enter the number of the month you were born: "))
Day = int(input("Please enter the day your were born: "))

DateOfBirth = datetime(Year, Month, Day)

Age = datetime.now() - DateOfBirth

print ("You are " + str(Age.days) + " days old")


AgeYears = Age.days/365

print ("Or " + str(AgeYears) + " years old to be less precise")
