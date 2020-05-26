#Calculates pay with a 1.5x pay rise for over 40 hours
hrs = input("Please enter the hours. ")
rate = input("Please enter the rate per hour. ")

#quits program if they enter invalid data
try:
    hrs = float(hrs)
    rate = float(rate)
except:
    print("Oops! Not a valid number!")
    quit()

if hrs >= 40:
    x = hrs - 40
    hrs = hrs - x
    pay40 = hrs * rate
    rate = rate * 1.5
    hrs = hrs + x
    hrs = hrs - 40
    pay41 = hrs * rate
    print(pay40 + pay41)
else:
    pay = hrs * rate
    print(pay)