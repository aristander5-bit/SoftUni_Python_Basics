month = input()
total_nights = int(input())

price_apartment = 0
price_studio = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if 7 < total_nights <= 14:
        price_studio *= 0.95
    elif total_nights > 14:
        price_studio *= 0.70

elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if total_nights > 14:
        price_studio *= 0.80

elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77

if total_nights > 14:
    price_apartment *= 0.90  # 10% отстъпка

total_amount_studio = total_nights * price_studio
total_amount_apartment = total_nights * price_apartment

print(f"Apartment: {total_amount_apartment:.2f} lv.")
print(f"Studio: {total_amount_studio:.2f} lv.")