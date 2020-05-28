number = input("Please enter a number between 2 and 12: ")
try:
    number = int(number)
    if number == 2:
        print("2\n4 6 8 10 12 14 16 18 20 22 24")
    elif number == 3:
        print("3\n6 9 12 15 18 21 24 27 30 33 36")
    elif number == 4:
        print("4\n8 12 16 20 24 28 32 36 40 44 48")
    elif number == 5:
        print("5\n10 15 20 25 30 35 40 45 50 55 60")
    elif number == 6:
        print("6\n12 18 24 30 36 42 48 54 60 66 72")
    elif number == 7:
        print("7\n14 21 28 35 42 49 56 63 70 77 84")
    elif number == 8:
        print("8\n16 24 32 40 48 56 64 72 80 88 96")
    elif number == 9:
        print("9\n18 27 36 45 54 63 72 81 90 99 108")
    elif number == 10:
        print("10\n20 30 40 50 60 70 80 90 100 110 120")
    elif number == 11:
        print("11\n22 33 44 55 66 77 88 99 110 121 132")
    elif number == 12:
        print("12\n24 36 48 60 72 84 96 108 120 132 144")
    else:
        print("Please pick a number between 2 and 12")
except:
    print("Oops! Not a number.")