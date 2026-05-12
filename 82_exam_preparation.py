
max_fails = int(input())
max_fails_counter = max_fails
total_task = 0
total_task_score = 0
last_problem = ""

while max_fails_counter > 0:
    new_task = input()

    if new_task == "Enough":
        print(f"Average score: {(total_task_score / total_task):.2f}")
        print(f"Number of problems: {total_task}")
        print(f"Last problem: {last_problem}")
        break

    last_problem = new_task
    total_task += 1

    task_score = int(input())
    total_task_score += task_score

    if task_score <= 4:
        max_fails_counter -= 1
        if max_fails_counter <= 0:
            print(f"You need a break, {max_fails} poor grades.")
            break
