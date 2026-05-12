tv_show_title = input()
duration_episode = int(input())
duration_break = int(input())

duration_lunch = duration_break * 1 / 8
duration_rest = duration_break * 1 / 4

free_time = duration_break - (duration_lunch + duration_rest)

diff = abs(free_time - duration_episode)

if diff > int(diff):
    diff = int(diff) + 1
else:
    diff = int(diff)

if free_time >= duration_episode:
    print(f"You have enough time to watch {tv_show_title} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_show_title}, you need {diff} more minutes.")
