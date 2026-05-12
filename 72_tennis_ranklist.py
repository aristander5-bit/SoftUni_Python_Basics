from math import floor

total_tournament = int(input())
starting_points = int(input())
wins = 0
points_from_tournament = 0

for _ in range(total_tournament):
    stage = input()

    if stage == "W":
        starting_points += 2000
        points_from_tournament += 2000
        wins +=1
    elif stage == "F":
        starting_points += 1200
        points_from_tournament += 1200
    elif stage == "SF":
        starting_points += 720
        points_from_tournament += 720

print(f"Final points: {starting_points}")
print(f"Average points: {floor(points_from_tournament / total_tournament)}")
print(f"{(wins / total_tournament * 100):.2f}%")

