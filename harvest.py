from math import floor, ceil

X_square_m_grape = int(input())
Y__grape_square_m = float(input())
Z_needed_l_wine = int(input())
num_workers = int(input())

total_grape = X_square_m_grape * Y__grape_square_m
grape_for_wine = total_grape * 0.40
produced_wine = grape_for_wine / 2.5

if produced_wine >= Z_needed_l_wine:
    remaining_wine = produced_wine - Z_needed_l_wine
    wine_per_worker = remaining_wine / num_workers
    print(f"Good harvest this year! Total wine: {ceil (produced_wine)} liters.")
    print(f"{ceil (remaining_wine)} liters left -> {ceil (wine_per_worker)} liters per person.")
else:
    needed_wine = Z_needed_l_wine - produced_wine
    print(f"It will be a tough winter! More {floor (needed_wine)} liters wine needed.")