# Assignment 03
# Question no.3
# Write a program that converts temperatures between Celsius and Fahrenheit based on user input. 

print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
choice = int(input("Enter your choise (1,2, or 3): "))
    
if choice == 1:
        C = float(input("Enter temperature in Celsius: "))
        F = 95*C + 32
        print(f"{C}°C is equal to {F}°F")
        
elif choice == 2:
        F = float(input("Enter temperature in Fahrenheit: "))
        C = 59*(F - 32)
        print(f"{F}°F is equal to {C}°C")
        
elif choice == 3:
        C = float(input("Enter temperature in Celsius: "))
        K = C + 273.15
        print(f"{C}°C is equal to {K}°K")
        
else:
        print("Invalid choice. Please try again.")
        