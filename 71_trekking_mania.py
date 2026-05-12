
number_of_groups = int(input())
counter_musala = counter_mon_blan = counter_kilimanjaro = counter_k2 = counter_everest = 0
total_climbers = 0

for _ in range(number_of_groups):
    people_of_groups = int(input())
    total_climbers += people_of_groups
    if people_of_groups <= 5:
        counter_musala += people_of_groups
    elif 6 <= people_of_groups <= 12:
        counter_mon_blan += people_of_groups
    elif 13 <= people_of_groups <= 25:
        counter_kilimanjaro += people_of_groups
    elif 26 <= people_of_groups <= 40:
        counter_k2 += people_of_groups
    elif people_of_groups >= 41:
        counter_everest += people_of_groups

print(f"{(counter_musala / total_climbers * 100):.2f}%")
print(f"{(counter_mon_blan / total_climbers * 100):.2f}%")
print(f"{(counter_kilimanjaro / total_climbers * 100):.2f}%")
print(f"{(counter_k2 / total_climbers * 100):.2f}%")
print(f"{(counter_everest / total_climbers * 100):.2f}%")