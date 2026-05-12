
num = int(input())
current_num = 1

for row in range(1,num + 1):
    for col in range(1, row + 1):
        if current_num > num:
            break
        print(current_num, end = " ")

        current_num += 1

    print()