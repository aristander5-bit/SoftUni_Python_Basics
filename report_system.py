
needed_sum = int(input())
collected_sum = 0
counter = 0
cash_sum = 0
card_sum = 0
cash_count = 0
card_count = 0

while collected_sum < needed_sum:
    command = input()
    if command == "End":
        break

    price = int(command)
    counter += 1

    if counter % 2 != 0:
        if price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            collected_sum += price
            cash_sum += price
            cash_count += 1

    else:
        if price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            collected_sum += price
            card_sum += price
            card_count += 1

if collected_sum >= needed_sum:
    avg_cash = cash_sum / cash_count
    avg_card = card_sum / card_count
    print(f"Average CS: {avg_cash:.2f}")
    print(f"Average CC: {avg_card:.2f}")
else:
    print("Failed to collect required money for charity.")

