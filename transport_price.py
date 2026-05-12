n = int(input())
period = input()

if n >= 100:
    total_price = n * 0.06
elif n >= 20:
    total_price = n * 0.09
else:
    if period == "day":
        total_price = 0.70 + (n * 0.79)
    else:
        total_price =0.70 + (n * 0.90)
print(f"{total_price:.2f}")