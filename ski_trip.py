days = int(input())
room_type = input()
rating = input()

night = days - 1
total_price = 0

if room_type == "room for one person":
    total_price = night * 18.00
elif room_type == "apartment":
    total_price = night * 25.00
    if night < 10:
        total_price = total_price - total_price * 0.30
    elif 10 <= night <= 15:
        total_price = total_price - total_price * 0.35
    elif night > 15:
        total_price = total_price - total_price * 0.50
elif room_type == "president apartment":
    total_price = night * 35
    if night < 10:
        total_price = total_price - total_price * 0.10
    elif 10 <= night <= 15:
        total_price = total_price - total_price * 0.15
    elif night > 15:
        total_price = total_price - total_price * 0.20
if rating == "positive":
    total_price += total_price * 0.25
elif rating == "negative":
    total_price -= total_price * 0.10

print(f"{total_price:.2f}")
