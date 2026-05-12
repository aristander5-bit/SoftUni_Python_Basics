
movement_game = int(input())
result = 0
interval_0_9 = 0
interval_10_19 = 0
interval_20_29 = 0
interval_30_39 = 0
interval_40_50 = 0
invalid_num = 0

for _ in range(movement_game):
    current_interval = int(input())

    if 0 <= current_interval <= 9:
        result += current_interval * 0.20
        interval_0_9 += 1
    elif 10 <= current_interval <= 19:
        result += current_interval * 0.30
        interval_10_19 += 1
    elif 20 <= current_interval <= 29:
        result += current_interval * 0.40
        interval_20_29 += 1
    elif 30 <= current_interval <= 39:
        result += 50
        interval_30_39 += 1
    elif 40 <= current_interval <= 50:
        result += 100
        interval_40_50 += 1
    else:
        result /= 2
        invalid_num += 1

perc_0_9 = interval_0_9 / movement_game * 100
perc_10_19 = interval_10_19 / movement_game * 100
perc_20_29 = interval_20_29 / movement_game * 100
perc_30_39 = interval_30_39 / movement_game * 100
perc_40_50 = interval_40_50 / movement_game * 100
perc_invalid = invalid_num / movement_game * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {perc_0_9:.2f}%")
print(f"From 10 to 19: {perc_10_19:.2f}%")
print(f"From 20 to 29: {perc_20_29:.2f}%")
print(f"From 30 to 39: {perc_30_39:.2f}%")
print(f"From 40 to 50: {perc_40_50:.2f}%")
print(f"Invalid numbers: {perc_invalid:.2f}%")




