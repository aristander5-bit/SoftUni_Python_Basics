volume_pool_l = int(input())
debit_first_pipe = int(input())
debit_second_pipe = int(input())
worker_absent = float(input())

water_first_pipe = debit_first_pipe * worker_absent
water_second_pipe = debit_second_pipe * worker_absent
total_water = water_first_pipe + water_second_pipe

if total_water <= volume_pool_l:
    total_percentage = (total_water / volume_pool_l) * 100
    percentage_first_pipe = (water_first_pipe / total_water) * 100
    percentage_second_pipe = (water_second_pipe / total_water) * 100
    print(f"The pool is {total_percentage:.2f}% full. Pipe 1: {percentage_first_pipe:.2f}%. Pipe 2: {percentage_second_pipe:.2f}%.")
else:
    overflow = total_water - volume_pool_l
    print(f"For {worker_absent:.2f} hours the pool overflows with {overflow:.2f} liters.")