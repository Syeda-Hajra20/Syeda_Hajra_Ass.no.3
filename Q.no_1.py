#Assignment#3
#Question no.1
#Write a program that takes a student's score as input and prints their Marksheet on predefined grading criteria.

name=(input("Enter your name: "))
Percentage=int(input("Enter your Percentage: "))

if Percentage >= 90:
    print("Percentage:" , Percentage,"%")
    print("Grade: A+")
    
elif Percentage >= 80:
    print("Percentage:" , Percentage)
    print("Grade: A")

elif Percentage >= 60:
    print("Percentage:" , Percentage)
    print("Grade: B")
     
elif Percentage >= 50:
    print("Percentage:" , Percentage)
    print("Grade: C")

elif Percentage >= 40:
    print("Percentage:" , Percentage)
    print("Grade: D")
    
else:
    print("Percentage:" , Percentage)
    print("Grade: FAIL")
    
  #_________xxxx_________xxxx_________
  