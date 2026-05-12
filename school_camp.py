season = input()
type_group = input()
sum_students = int(input())
sum_overnight = int(input())

price_per_night = 0
sport = ""

if season == "Winter":
    if type_group == "girls":
        price_per_night = 9.60
        sport = "Gymnastics"
    elif type_group == "boys":
        price_per_night = 9.60
        sport = "Judo"
    elif type_group == "mixed":
        price_per_night = 10
        sport = "Ski"
elif season == "Spring":
    if type_group == "girls":
        price_per_night = 7.20
        sport = "Athletics"
    elif type_group == "boys":
        price_per_night = 7.20
        sport = "Tennis"
    elif type_group == "mixed":
        price_per_night = 9.50
        sport = "Cycling"
elif season == "Summer":
    if type_group == "girls":
        price_per_night = 15
        sport = "Volleyball"
    elif type_group == "boys":
        price_per_night = 15
        sport = "Football"
    elif type_group == "mixed":
        price_per_night = 20
        sport = "Swimming"

total_price = sum_students * price_per_night * sum_overnight

if sum_students >= 50:
    total_price = total_price - (total_price * 0.50)
elif sum_students >= 20:
    total_price = total_price - (total_price * 0.15)
elif sum_students >= 10:
    total_price = total_price - (total_price * 0.05)

print(f"{sport} {total_price:.2f} lv.")