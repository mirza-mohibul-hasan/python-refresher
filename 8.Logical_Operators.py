temp = float(input("Enter the Temperature = "))
#and or not use korte hbe 
if temp >= 0 and temp <= 30:
    print("Weather Cold")
    print("You can go out")
elif temp < 0 or temp > 30:
    print("Weather too cold or Hot")
    print("You can't go out")