File = open("StudentMarks.txt", "a")
x = 0

while x < 5:
    name = input("Enter the name of student " + str(x + 1) + ": ")
    score = input("Enter the students score: ")
    name = name + " "
    score = score +"\n"
    File.writelines(name)
    File.writelines(score)
    x = x + 1

File.close()