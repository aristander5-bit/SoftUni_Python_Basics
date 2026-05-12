first = int(input())
second = int(input())
third = int(input())

total_sec = first + second + third

minutes = total_sec // 60
seconds = total_sec % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")