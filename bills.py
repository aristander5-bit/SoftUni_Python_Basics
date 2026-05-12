
months = int(input())

total_electricity = 0
total_water = 0
total_internet = 0
total_others = 0

for _ in range(months):
    electricity_months = float(input())

    total_electricity += electricity_months
    total_water += 20
    total_internet += 15

    month_base = electricity_months + 20 + 15
    other_month = month_base + (month_base * 0.20)

    total_others += other_month

all_total = total_electricity + total_water + total_internet + total_others
avg = all_total / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {avg:.2f} lv")

