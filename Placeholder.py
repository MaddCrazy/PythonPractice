largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        num = int(num)
        #intial number entry
        if largest is None:
            largest = num
        if smallest is None:
            smallest = num
        #check for largest
        if num > largest:
            largest = num
        #check for smallest
        if num < smallest:
            smallest = num
    except:
        if num == "done" : 
            break
        else:
            print("Invalid input")

print("Maximum is" , largest)
print("Minimum is", smallest)