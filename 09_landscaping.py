sq_meters = float(input())
price_per_sq_meter = 7.61
total_initial_price = sq_meters * price_per_sq_meter
discount = total_initial_price * 0.18
final_price = total_initial_price - discount
print(f"{final_price:2f} lv.")
print(f"{discount:2f} lv.")