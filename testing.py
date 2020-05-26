#Read and Write to a text file + sorting a list
L = ["Dozer ", "Dog ", "Bottle ", "Aircraft ", "Glasses ", "Xylophone ", "Zebra ", "Giraffe ", "Elephant ", "Eggplant ", "Sunshine "]
#r+ means read and write
List = open("myWordListooo.txt","r+")
List.writelines(L)
List.close()
#r means read only
List = open("myWordListooo.txt","r")
#a means write only (creates a new file if the file doesnt exist)
New = open("myWordListS.txt","a")
print(List.read())
L.sort()
print(L)
confirmation = input("Is this list satisfactory? ")
if confirmation == "Yes":
    New.writelines(L)
New.close()
List.close()

