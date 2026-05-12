from math import floor, ceil

sum_days = int(input())
leftover_food = int(input())
day_food_dog_kg = float(input())
day_food_cat_kg = float(input())
day_food_turtle_g = float(input())
day_food_turtle_kg = day_food_turtle_g / 1000

pets_food = (day_food_dog_kg + day_food_cat_kg + day_food_turtle_kg) * sum_days

if pets_food <= leftover_food:
    diff = leftover_food - pets_food
    print(f"{floor (diff)} kilos of food left.")
else:
    diff = pets_food - leftover_food
    print(f"{ceil (diff)} more kilos of food are needed.")