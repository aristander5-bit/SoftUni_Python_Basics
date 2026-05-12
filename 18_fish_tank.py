length_cm = int(input())
wight_cm = int(input())
height_cm = int(input())
pct = float(input())

volume_cm = length_cm * wight_cm * height_cm
volume_l = volume_cm / 1000
total_l = volume_l * (1 - pct / 100)

print(total_l)