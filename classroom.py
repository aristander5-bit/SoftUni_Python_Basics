w = float(input())
h = float(input())
w_in_cm = w * 100
h_in_cm = h* 100
total_w = w_in_cm // 120
total_h = (h_in_cm - 100) // 70
total = (total_w * total_h) - 3
print(int(total))