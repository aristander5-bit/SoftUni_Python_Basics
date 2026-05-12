movie_budget = float(input())
total_spectators = int(input())
spectators_clothes_price = float(input())

decoration = movie_spectators = movie_budget * 0.10

if total_spectators > 150:
    discount = spectators_clothes_price * 0.10
    spectators_clothes_price -= discount

total_amount_needed = decoration + (total_spectators * spectators_clothes_price)

if movie_budget >= total_amount_needed:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - total_amount_needed:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_amount_needed - movie_budget:.2f} leva more.")