#Assignment#3
#Question no.4
#Develop a program that takes three sides of a triangle as input and determines whether the triangle is equilateral, isosceles, or scalene using conditional statements.
 
A = float(input("Enter side 1 of your Triangle: "))
B = float(input("Enter side 2 of your Triangle: "))
C = float(input("Enter side 3 of your Triangle: "))

if A == B == C:
    print("Your Triangle is 'Equilateral'.")
elif A == B or B == C or A == C:
    print("Your Triangle is 'Isosceles'.")
else:
    print("Your Triangle is 'Scalene'.") 
     