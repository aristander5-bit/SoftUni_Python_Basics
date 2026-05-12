type_flower = input()
total_flowers = int(input())
budget = int(input())
total_amount = 0

price_for_roses = 5
price_for_dahlias = 3.80
price_for_tulips = 2.80
price_for_narcissus = 3
price_for_gladiolus = 2.50

if type_flower == "Roses":
    total_amount = price_for_roses * total_flowers
    if total_flowers > 80:
        total_amount *= 0.90

elif type_flower == "Dahlias":
    total_amount = price_for_dahlias * total_flowers
    if total_flowers > 90:
        total_amount *= 0.85

elif type_flower == "Tulips":
    total_amount = price_for_tulips * total_flowers
    if total_flowers > 80:
        total_amount *= 0.85

elif type_flower == "Narcissus":
    total_amount = price_for_narcissus * total_flowers
    if total_flowers < 120:
        total_amount *= 1.15

elif type_flower == "Gladiolus":
    total_amount = price_for_gladiolus * total_flowers
    if total_flowers < 80:
        total_amount *= 1.20

if budget >= total_amount:
    print(f"Hey, you have a great garden with {total_flowers} {type_flower} and {(budget - total_amount):.2f} leva left.")
else:
    print(f"Not enough money, you need {total_amount - budget:.2f} leva more.")