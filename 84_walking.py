
goal = 10000
steps_walked = 0
achieved = False

while True:
    new_input = input()
    if new_input == "Going home":
        steps_to_home = int(input())
        steps_walked += steps_to_home
        if steps_walked < goal:
            print(f"{goal - steps_walked} more steps to reach goal.")
        else:
            achieved = True
        break

    steps_walked += int(new_input)

    if steps_walked >= goal:
        achieved = True
        break

if achieved:
    print("Goal reached! Good job!")
    print(f"{steps_walked - goal} steps over the goal!")

