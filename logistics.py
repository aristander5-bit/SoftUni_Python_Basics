

sum_cargo = int(input())

tons_bus = 0
tons_truck = 0
tons_train = 0
total_price = 0
total_tons = 0

for _ in range(sum_cargo):
    current_load = int(input())
    total_tons += current_load

    if current_load <=3:
        tons_bus += current_load
        total_price += current_load * 200
    elif 4 <= current_load <= 11:
        tons_truck += current_load
        total_price += current_load * 175
    elif current_load >= 12:
        tons_train += current_load
        total_price += current_load * 120

average_price = total_price / total_tons

perc_bus = (tons_bus / total_tons * 100)
perc_truck = (tons_truck / total_tons * 100)
perc_train = (tons_train / total_tons * 100)

print(f"{average_price:.2f}")
print(f"{perc_bus:.2f}%")
print(f"{perc_truck:.2f}%")
print(f"{perc_train:.2f}%")

