#prints each individual element of models
models = ["Ford", "Holden", "Toyota", "Mitsubishi", "Mazda"]
for model in models:
    print (model)
    
#prints each character of the string individually   
aString = "Hello"
for eachCharacter in aString:
    print(eachCharacter)
    
#makes the string upper case then prints it while counting the number of characters in the string  
strAstring = "This is a string with quite a few characters in it. 63 in fact!"
characterCount = 0
UpperCase = ""
for character in strAstring:
    UpperCase = UpperCase + character.capitalize()
    characterCount += 1
print(UpperCase)
print("There are " + str(characterCount) + " characters in the above string.")

#Adds all the numbers from 1 to 10 together
s = 0
for i in range(1,11):
    s = s + i
print(s)

#Bubble Sort
numberList = [11, 2, 43, 8, 13, 44, 75,17,3, 21]
print (numberList)
for passCount in range(len(numberList) - 1, 0, -1):
    for i in range(passCount):
        #if numberList(item1) is greater than numberList(item2) item1 is place into a temporary holder and becomes temp while item2 become item1 and then temp becomes item 2 - thus swapping the placements of item1 and item2 
        if numberList[i] > numberList[i + 1]:
            temp = numberList[i]
            numberList[i] = numberList[i + 1]
            numberList[i + 1] = temp
print (numberList)
