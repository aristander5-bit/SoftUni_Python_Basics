
age_Lily = int(input())
price_washing_machine = float(input())
price_toy = int(input())

saving = 0
coefficient = 1

for year in range(1, age_Lily + 1):
    if year % 2 != 0:
        saving += price_toy
    elif year % 2 == 0:
        saving += (coefficient * 10)
        saving -= 1
        coefficient += 1

if saving >= price_washing_machine:
    print(f"Yes! {(saving - price_washing_machine):.2f}")
else:
    print(f"No! {(price_washing_machine - saving):.2f}")