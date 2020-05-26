subjectFinalMark = int(input("Please enter the student's Subject Final Mark: "))

if (subjectFinalMark > 0 and subjectFinalMark < 50):
    print ("Fail")
elif (subjectFinalMark >= 50 and subjectFinalMark < 60):
    print ("Pass")
elif (subjectFinalMark >= 60 and subjectFinalMark < 75):
    print ("Credit")
elif (subjectFinalMark >=75 and subjectFinalMark < 85):
    print ("Distinction")
elif (subjectFinalMark >=85 and subjectFinalMark <= 100):
    print ("High Distinction")
else:
    print ("Please enter a value between 0 and 100")
    
