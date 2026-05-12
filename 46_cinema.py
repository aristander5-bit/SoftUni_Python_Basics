cinema = input()
rows = int(input())
cols = int(input())
income = 0

price_premiere = 12
price_normal = 7.5
price_discount = 5

capacity = rows * cols

if cinema == "Premiere":
    income = price_premiere * capacity
elif cinema == "Normal":
    income = price_normal * capacity
elif cinema == "Discount":
    income = price_discount * capacity

print(f"{income:.2f} leva")