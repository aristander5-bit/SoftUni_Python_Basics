
num_n = int(input())
total_sum = 0
current_num = 0

for _ in range(num_n):
    current_num = int(input())
    total_sum += current_num

average = total_sum / num_n

print(f"{average:.2f}")
