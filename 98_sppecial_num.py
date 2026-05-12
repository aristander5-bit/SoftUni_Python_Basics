
n = int(input())
is_found = False

for number in range(1111, 9999 + 1):
    number_to_str = str(number)
    for digit in number_to_str:
        digit_to_str = int(digit)
        if digit_to_str == 0:
            is_found = False
            break

        elif n % digit_to_str == 0:
            is_found = True
        else:
            is_found = False
            break

    if is_found:
        print(number, end = " ")




