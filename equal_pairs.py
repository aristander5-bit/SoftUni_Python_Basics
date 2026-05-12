
num = int(input())

last_sum = 0
max_diff = 0

for _ in range(num):
    num_1 = int(input())
    num_2 = int(input())
    current_sum = num_1 + num_2

    if _ > 0:
        diff = abs(current_sum - last_sum)

        if diff > max_diff:
            max_diff = diff

    last_sum = current_sum

if max_diff == 0:
    print(f"Yes, value={last_sum}")
else:
    print(f"No, maxdiff={max_diff}")