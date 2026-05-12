from math import ceil

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1 / 8
rest_time = break_duration * 1 / 4

free_time = break_duration - (lunch_time + rest_time)

if free_time >= episode_duration:
    left_time = ceil(free_time - episode_duration)
    print(f"You have enough time to watch {series_name} and left with {left_time} minutes free time.")
else:
    needed_time = ceil(episode_duration - free_time)
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")