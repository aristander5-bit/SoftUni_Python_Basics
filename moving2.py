
free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

total_free_space = free_space_width * free_space_length * free_space_height

while True:
    new_input = input()
    if new_input == "Done":
        print(f"{total_free_space} Cubic meters left.")
        break

    total_free_space -= int(new_input)

    if total_free_space <= 0:
        print(f"No more free space! You need {abs(total_free_space)} Cubic meters more.")
        break






