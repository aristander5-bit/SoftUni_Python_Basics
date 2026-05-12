type_fuel = input()
fuel_liters = float(input())

if type_fuel == "Diesel" or type_fuel == "Gasoline" or type_fuel == "Gas":
    fuel_output = type_fuel.lower()
    if fuel_liters >= 25:
        print(f"You have enough {fuel_output}.")
    else:
        print(f"Fill your tank with {fuel_output}!")
else:
    print("Invalid fuel!")