total_chicken_meals = int(input())
total_fish_meals = int(input())
total_vegetarian_meals = int(input())

price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegetarian_menu = 8.15
delivery = 2.50

total_price_chicken_menu = total_chicken_meals * price_chicken_menu
total_price_fish_menu = total_fish_meals * price_fish_menu
total_price_vegetarian_menu = total_vegetarian_meals * price_vegetarian_menu

total_price = total_price_chicken_menu + total_price_fish_menu + total_price_vegetarian_menu
desert_price = total_price * 0.20

final_price = total_price + desert_price + delivery
print(final_price)