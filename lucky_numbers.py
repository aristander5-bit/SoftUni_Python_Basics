
n = int(input())

for digit_1 in range(1, 10):
    for digit_2 in range(1, 10):
        for digit_3 in range(1, 10):
            for digit_4 in range(1, 10):

                sum_first_two = digit_1 + digit_2
                sum_second_two = digit_3 + digit_4

                if sum_first_two == sum_second_two:
                    if n % sum_first_two == 0:
                        print(f"{digit_1}{digit_2}{digit_3}{digit_4}", end = " ")