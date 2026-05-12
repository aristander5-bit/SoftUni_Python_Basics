sum_chrysanthemums = int(input())
sum_rosses = int(input())
sum_tulips = int(input())
season = input()
holiday = input()

price_c = 0
price_r = 0
price_t = 0
total_sum_flower = (sum_chrysanthemums \
                   + sum_rosses\
    + sum_tulips)

if season == "Spring" or season == "Summer":
    price_c = 2.00
    price_r = 4.10
    price_t = 2.50
elif season == "Autumn" or season == "Winter":
    price_c = 3.75
    price_r = 4.50
    price_t = 4.15

total_price = (sum_chrysanthemums * price_c) \
    + (sum_rosses * price_r) \
    + (sum_tulips * price_t)

if holiday == "Y":
    total_price = total_price + (total_price * 0.15)
elif holiday == "N":
    total_price = total_price

if season == "Spring" and sum_tulips > 7:
    total_price -= total_price * 0.05

if season == "Winter" and sum_rosses >= 10:
    total_price -= total_price * 0.10

if total_sum_flower > 20:
    total_price -= total_price * 0.20

total_price += 2

print(f"{total_price:.2f}")