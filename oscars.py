
name = input()
points = float(input())
num_evaluators = int(input())


for _ in range(num_evaluators):
    new_evaluator = input()
    given_points = float(input())
    points_for_actor = (len(new_evaluator) * given_points) / 2
    points += points_for_actor

    if points > 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
        break
else:
    print(f"Sorry, {name} you need {(1250.5 - points):.1f} more!")
