#creating a list then printing said list
testList = list()
#using ASCII codes
i = 48
while i >= 48 and i <= 122:
    testList.append(chr(i))
    print(testList[i - 48])
    i += 1


#pre-populated lists
prime = [2, 3, 5, 7, 11, 13]
#adding to the end of the list
prime.append(17)
prime.append(19)
print(prime)
print(prime[0])
print(prime[3])
print(prime[5])
#prints last few numbers
print(prime[-3])
print(prime[-1])
#prints list length
print(len(prime))
#prints from 2 (included) until 7 (not included)
print(prime[2:7])


#mixed type lists
mixed = [1.0, 2, "Three", False, ["another list", 7, 16.245], 3]
print(mixed)


#Editing Lists
#combining lists
Combined = prime + mixed
print(Combined)
#reversing lists
prime.reverse()
print(prime)
#changing lists
prime[4] = "Change"
print(prime)
#inserting into lists
prime.insert(3, "insert")
print(prime)
#removing from lists
prime.remove(prime[7])
print(prime)
#retrieving index on known value
index = prime.index(11)
print(index)
index = prime.index("insert")
print(index)


#looping through a list
i = 0
#while method
while i < len(prime):
    print(prime[i])
    i += 1
#for methof
for eachItem in prime:
    print(eachItem)


#adding to items in a list without editing the original list
index = prime.index(11)
y = 5 + prime[index]
print(y)
index = prime.index("insert")
y = "Testing" + prime[index]
print(y)

#range
#printing a range of a list
for i in range(len(prime)):
    print(prime[i])
for i in range(2,7):
    print(prime[i])
#prints a range of 0 to 6
print(range(0,6))
#prints a list from range 0 to 20 in steps of 2
print(range(0,20,2))
#creates a list of range 2 to 9
test = list(range(2,9))
print(test)

#open a file into a list
fileTemp = open("StudentMarks.txt" , "r")
fileList = list()
for eachLine in fileTemp:
    fileList.append(eachLine)
print(fileList)
print(fileList[2])
fileTemp.close()
