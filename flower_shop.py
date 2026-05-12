from math import floor, ceil

num_magnolias = int(input())
num_hyacinth = int(input())
num_rose = int(input())
num_cactus = int(input())
price_gift = float(input())

total_flower = (num_magnolias * 3.25) + (num_hyacinth * 4) + (num_rose * 3.50) + (num_cactus * 8)
tax = total_flower * 0.05
total_profit = total_flower - tax

if total_profit >= price_gift:
    left_sum = total_profit - price_gift
    print(f"She is left with {floor (left_sum)} leva. ")
else:
    needed_sum = price_gift - total_profit
    print(f"She will have to borrow {ceil (needed_sum)} leva.")
