#Assignment#3
#Question no.2
#Create a program that checks if a given year is a leap Year and prints the results.

Year=int(input("Enter the year: "))

if (Year % 400==0) and (Year % 100==0) :
    print(Year,"is a Leap year")
    
elif (Year % 4==0) and (Year % 100 !=0) :
    print(Year,"is a Leap year")
    
else:
    print(Year,"is not a Leap year")  