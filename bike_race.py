sum_juniors_bikers = int(input())
sum_seniors_bikers = int(input())
trace_type = input()

total_sum = 0

if trace_type == "trail":
    total_sum = (sum_juniors_bikers * 5.50) + (sum_seniors_bikers * 7)
elif trace_type == "cross-country":
    total_sum = (sum_juniors_bikers * 8) + (sum_seniors_bikers * 9.50)
    total_bikers = sum_seniors_bikers + sum_juniors_bikers
    if total_bikers >= 50:
        total_sum -= total_sum * 0.25
elif trace_type == "downhill":
    total_sum = (sum_juniors_bikers * 12.25) + (sum_seniors_bikers * 13.75)
elif trace_type == "road":
    total_sum = (sum_juniors_bikers * 20) + (sum_seniors_bikers * 21.50)

total_sum -= total_sum * 0.05

print(f"{total_sum:.2f}")