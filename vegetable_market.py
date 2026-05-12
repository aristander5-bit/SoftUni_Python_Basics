

price_kg_vegetable = float(input())
price_kg_fruits = float(input())
total_kg_vegetable = int(input())
total_kg_fruits = int(input())

total_bgn = (price_kg_vegetable * total_kg_vegetable) + (price_kg_fruits * total_kg_fruits)
total_euro = total_bgn / 1.94

print(f"{total_euro:.2f}")