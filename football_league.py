
stadium_capacity = int(input())
num_fans = int(input())

count_a = 0
count_b = 0
count_v = 0
count_g = 0

for _ in range(num_fans):
    sector = input()

    if sector == "A":
        count_a += 1
    elif sector == "B":
        count_b += 1
    elif sector == "V":
        count_v += 1
    elif sector == "G":
        count_g += 1

perc_a = (count_a / num_fans) * 100
perc_b = (count_b / num_fans) * 100
perc_v = (count_v / num_fans) * 100
perc_g = (count_g / num_fans) * 100

perc_total = (num_fans / stadium_capacity) * 100

print(f"{perc_a:.2f}%")
print(f"{perc_b:.2f}%")
print(f"{perc_v:.2f}%")
print(f"{perc_g:.2f}%")
print(f"{perc_total:.2f}%")


