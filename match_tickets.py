budget = float(input())
category = input()
sum_people_group = int(input())

transport_cost = 0

if 1 <= sum_people_group <= 4:
    transport_cost = budget * 0.75
elif 5 <= sum_people_group <= 9:
    transport_cost = budget * 0.60
elif 10 <= sum_people_group <= 24:
    transport_cost = budget * 0.50
elif 25 <= sum_people_group <= 49:
    transport_cost = budget * 0.40
else:
    transport_cost = budget * 0.25

money_left = budget - transport_cost
total_ticket_price = 0

if category == "VIP":
    total_ticket_price = sum_people_group * 499.99
elif category == "Normal":
    total_ticket_price = sum_people_group * 249.99

diff = abs(money_left - total_ticket_price)

if money_left >= total_ticket_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")


