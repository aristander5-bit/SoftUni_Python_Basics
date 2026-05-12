budget = float(input())
season = input()

destination = ""
place = ""
spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        spent = budget * 0.30
    else:
        place = "Hotel"
        spent = budget * 0.70

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        spent = budget * 0.40
    else:
        place = "Hotel"
        spent = budget * 0.80

else:
    destination = "Europe"
    place = "Hotel"
    spent = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{place} - {spent:.2f}")
