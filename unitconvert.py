def lengthconvert():
    print("select length converting option :\n1. Meters to Kilometers\n2. Kilometers to Meters"
          "\n3. Centimeters to Meters\n4. Meters to Centimeters")
    choice = int(input("Enter your choice: "))
    value = float(input("Enter the value to convert: "))
    if choice == 1:
        print(f"{value} meters is equal to {value / 1000} kilometers.")
    elif choice == 2:
        print(f"{value} kilometers is equal to {value * 1000} meters.")
    elif choice == 3:
        print(f"{value} centimeters is equal to {value / 100} meters.")
    elif choice == 4:
        print(f"{value} meters is equal to {value * 100} centimeters.")
    else:
        print("Invalid choice.")

def temperatureconvert():
    print("select temperature converting option :\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius"
          "\n3. Celsius to Kelvin\n4. Kelvin to Celsius")
    choice = int(input("Enter your choice: "))
    value = float(input("Enter the value to convert: "))
    if choice == 1:
        print(f"{value}°C is equal to {(value * 9 / 5) + 32}°F.")
    elif choice == 2:
        print(f"{value}°F is equal to {(value - 32) * 5 / 9}°C.")
    elif choice == 3:
        print(f"{value}°C is equal to {value + 273.15} K.")
    elif choice == 4:
        print(f"{value} K is equal to {value - 273.15}°C.")
    else:
        print("Invalid choice.")

def weightconvert():
    print("select weight converting option :\n1. Kilograms to Grams\n2. Grams to Kilograms"
          "\n3. Square Meters to Square Feet\n4. Square Feet to Square Meters\n5. Square Meters to Square Yards"
          "\n6. Square Yards to Square Meters\n7. Square Meters to Acres\n8. Acres to Square Meters")
    choice = int(input("Enter your choice: "))
    value = float(input("Enter the value to convert: "))
    if choice == 1:
        print(f"{value} kilograms is equal to {value * 1000} grams.")
    elif choice == 2:
        print(f"{value} grams is equal to {value / 1000} kilograms.")
    elif choice == 3:
        print(f"{value} pounds is equal to {value / 2.20462} kilograms.")
    elif choice == 4:
        print(f"{value} kilograms is equal to {value * 2.20462} pounds.")
    else:
        print("Invalid choice.")

def areaconvert():
    print("select area converting option :\n1. Square Meters to Square Kilometers\n2. Square Kilometers to Square Meters"
          "\n3. Centimeters to Meters\n4. Meters to Centimeters")
    choice = int(input("Enter your choice: "))
    value = float(input("Enter the value to convert: "))
    if choice == 1:
        print(f"{value} square meters is equal to {value / 1_000_000} square kilometers.")
    elif choice == 2:
        print(f"{value} square kilometers is equal to {value * 1_000_000} square meters.")
    elif choice == 3:
        print(f"{value} square meters is equal to {value * 10.7639} square feet.")
    elif choice == 4:
        print(f"{value} square feet is equal to {value / 10.7639} square meters.")
    elif choice == 5:
        print(f"{value} square meters is equal to {value * 1.19599} square yards.")
    elif choice == 6:
        print(f"{value} square yards is equal to {value / 1.19599} square meters.")
    elif choice == 7:
        print(f"{value} square meters is equal to {value / 4046.86} acres.")
    elif choice == 8:
        print(f"{value} acres is equal to {value * 4046.86} square meters.")
    else:
        print("Invalid choice.")
def convert():
    while True:
        print(" Select type of units for conversion \n1. Length \n2. Temperature \n3. Weight \n4. Area\n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            lengthconvert()
        elif choice == 2:
            temperatureconvert()
        elif choice == 3:
            weightconvert()
        elif choice == 4:
            areaconvert()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
convert()