print("Good morning! What would you like for breakfast?")
print("You can have eggs or cereal.")
bSelection = input("What is your choice? ")

if (bSelection == "eggs"):
    print("You can have them fried, scrambled, or boiled.")
    eggType = input("How would you like them cooked? ")
    if (eggType == "boiled"):
        print("How would you like your eggs boiled?")
        print("You can have them soft or hard.")
        boilType = input("What is your preference? ")
        if (boilType == "hard"):
            print("Thank you! Your hard boiled eggs will arrive soon.")
        else:
            print("Thank you! Your soft boiled eggs will arrive soon.")
    if (eggType == "fried"):
        print("You can have sunny side up, over easy, over medium, or over hard.")
        fryType = input("How would you like them? ")
        if (fryType == "Sunny side up"):
            print ("Thank you! Your sunny side up fried eggs will arrive soon.")
        elif (fryType == "over easy"):
            print ("Thank you! Your over easy fried eggs will arrive soon.")
        elif (fryType == "over medium"):
            print ("Thank you! Your over medium fried eggs will arrive soon.")
        else:
            print ("Thank you! Your over hard fried eggs will arrive soon.")
if (bSelection == "cereal"):
    print("We have porridge, muesli, Corn Flakes and Rice Bubbles.")
    cType = input("Which cereal would you like? ")
    if (cType == "porridge"):
        print("You can choose between full cream milk or light milk.")
        milkType = input("What milk would you like? ")
        if (milkType == "full cream milk"):
            print("Thank you! Your porridge with full cream milk will arrive soon.")
        else:
            print ("Thank you! Your porridge with light milk will arrive soon.")
print ("Enjoy your breakfast!")
