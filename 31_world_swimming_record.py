world_record_seconds = float(input())
distance = float(input())
time_to_pass_one_meter = float(input())

total_time = distance * time_to_pass_one_meter

water_resistance_seconds = (distance // 15) * 12.5

final_time = total_time + water_resistance_seconds

if final_time < world_record_seconds:
    print(f" Yes, he succeeded! The new world record is {final_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(final_time - world_record_seconds):.2f} seconds slower.")
