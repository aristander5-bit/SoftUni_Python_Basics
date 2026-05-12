price_excursion = float(input())
num_puzzle = int(input())
num_speak_dolls = int(input())
plush_bears = int(input())
num_minion = int(input())
num_trucks = int(input())

puzzle_price = num_puzzle * 2.60
speak_dolls_price = num_speak_dolls * 3
plush_bears_price = plush_bears * 4.10
minion_price = num_minion * 8.20
trucks_price = num_trucks * 2

total_price = (puzzle_price + speak_dolls_price + plush_bears_price + minion_price + trucks_price)

total_toys = (num_puzzle + num_speak_dolls + plush_bears + num_minion + num_trucks)

if total_toys >= 50:
    discount = total = total_price * 0.25
    total_price -= discount

rent = total_price * 0.10
total_price -= rent

if price_excursion <= total_price:
    print(f"Yes! {(total_price - price_excursion):.2f} lv left.")

else:
    print(f"Not enough money! {(price_excursion - total_price):.2f} lv needed.")