budget = float(input())
season = input()

place = ""
destination = ""
spent = 0

if season == "winter" or budget > 1000:
    place = "Hotel"
else:
    place = "Camp"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent = budget * 0.30
    elif season == "winter":
        spent = budget * 0.70
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent = budget * 0.40
    elif season == "winter":
        spent = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    spent = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{place} - {spent:.2f}")