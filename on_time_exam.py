exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

total_minute_start_exam = (exam_hour * 60) + exam_minute
total_minutes_arrival = (arrival_hour * 60) + arrival_minute

diff = total_minute_start_exam - total_minutes_arrival

if diff == 0:
    print("On time")
elif 0 < diff <= 30:
    print("On time")
    print(f"{diff} minutes before the start")
elif 30 < diff <= 59:
    print("Early")
    print(f"{diff} minutes before the start")
elif diff > 59:
    hours = diff // 60
    minutes = diff % 60
    print("Early")
    if minutes < 10:
        print(f"{hours}:0{minutes} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")
elif -59 <= diff <0:
    print("Late")
    print(f"{abs(diff)} minutes after the start")
elif diff <= -60:
    hours = abs(diff) // 60
    minutes = abs(diff) % 60
    print("Late")
    if minutes < 10:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")