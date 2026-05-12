sleep_norm = 30000
days_year = 365
minutes_play_working_day = 63
minutes_play_day_off = 127

days_off = int(input())

working_days = days_year - days_off
total_play_time = (working_days * minutes_play_working_day) + (days_off * minutes_play_day_off)

difference = abs(sleep_norm - total_play_time)
hours = difference // 60
minutes = difference % 60

if total_play_time > sleep_norm:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")