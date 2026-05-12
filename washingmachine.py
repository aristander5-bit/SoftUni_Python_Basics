sum_bottles = int(input())

one_bottle_ml = 750
plate_one_ml = 5
saucepan_one_ml = 15

plate_count = 0
saucepan_count = 0
counter = 0

total = sum_bottles * 750

is_detergent_enough = True

while True:
    command = input()
    if command == "End":
        break

    current_dishes = int(command)
    counter += 1

    if counter % 3 == 0:
        total -= current_dishes * saucepan_one_ml
        saucepan_count += current_dishes
    else:
        total -= current_dishes * plate_one_ml
        plate_count += current_dishes

    if total < 0:
        is_detergent_enough = False
        break

if is_detergent_enough:
    print("Detergent was enough!")
    print(f"{plate_count} dishes and {saucepan_count} pots were washed.")
    print(f"Leftover detergent {total} ml.")
else:
    print(f"Not enough detergent, {abs(total)} ml. more necessary!")







