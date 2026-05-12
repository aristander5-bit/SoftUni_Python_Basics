

fuel_type = input()
fuel_liters = float(input())
club_card = input()

price_per_liter = 0

if fuel_type == "Gasoline":
    price_per_liter = 2.22
    if club_card == "Yes":
        price_per_liter -= 0.18
elif fuel_type == "Diesel":
    price_per_liter = 2.33
    if club_card == "Yes":
        price_per_liter -= 0.12
elif fuel_type == "Gas":
    price_per_liter = 0.93
    if club_card == "Yes":
        price_per_liter -= 0.08

total_price = fuel_liters * price_per_liter

if 20 <= fuel_liters <= 25:
    total_price = total_price * 0.92
elif fuel_liters > 25:
    total_price = total_price * 0.90
print(f"{total_price:.2f} lv.")



