price_mackerel_kg = float(input())
price_sprat_kg = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())
price_bonito_kg = price_mackerel_kg + (price_mackerel_kg * 0.60)
price_horse_mackerel_kg = price_sprat_kg + (price_sprat_kg * 0.80)


total_bonito = bonito_kg * price_bonito_kg
total_horse_mackerel = horse_mackerel_kg * price_horse_mackerel_kg
total_mussels = mussels_kg * 7.50

price_total = total_bonito + total_horse_mackerel + total_mussels
print(f"{price_total:.2f}")