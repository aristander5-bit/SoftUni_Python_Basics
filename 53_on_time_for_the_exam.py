exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time_total = exam_hour * 60 + exam_min
arrival_time_total = arrival_hour * 60 + arrival_min

diff = exam_time_total - arrival_time_total

if diff < 0:
    print("Late")
elif 0 <= diff <= 30:
    print("On time")
else:
    print("Early")

if diff != 0:
    abs_diff = abs(diff)
    hours = abs_diff // 60
    minutes = abs_diff % 60

    if diff > 0:
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f"{minutes} minutes before the start")
    else:
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours after the start")
        else:
            print(f"{minutes} minutes after the start")