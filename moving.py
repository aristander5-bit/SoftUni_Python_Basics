
width = int(input())
length = int(input())
height = int(input())

total_volume = width * length * height

space_taken = 0
is_full = False

while True:
    entry = input()

    if entry == "Done":
        break

    boxes = int(entry)
    space_taken += boxes

    if space_taken > total_volume:
        is_full = True
        break

diff = abs(total_volume - space_taken)

if is_full:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")