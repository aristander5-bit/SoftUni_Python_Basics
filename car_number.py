
interval_start = int(input())
interval_end = int(input())

for digit_1 in range(interval_start, interval_end+1):
    for digit_2 in range(interval_start, interval_end+1):
        for digit_3 in range(interval_start, interval_end+1):
            for digit_4 in range(interval_start, interval_end+1):

                if (digit_1 % 2 == 0 and digit_4 % 2 != 0) or (digit_1 % 2 != 0 and digit_4 % 2 == 0):
                    if digit_1 > digit_4:
                        if (digit_2 + digit_3) % 2 == 0:
                            print(f"{digit_1}{digit_2}{digit_3}{digit_4}", end = " ")

