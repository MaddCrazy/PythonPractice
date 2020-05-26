def computepay(h,r):
    if h >= 40:
        x = h - 40
        h = h - x
        pay40 = h * r
        r = r * 1.5
        h = h + x
        h = h - 40
        pay41 = h * r
        pay = pay40 + pay41
        return pay
    else:
        pay = h * r
        return pay

hrs = input("Enter hours: ")
rate = input("Enter rate per hour: ")
hrs = float(hrs)
rate = float(rate)
p = computepay(hrs,rate)
print("Pay",p)

