deposit = float(input())
period = int(input())
interest_rate = float(input())
total_interest = deposit * (interest_rate / 100)
monthly_interest = total_interest / 12
total_amount = deposit + (period * monthly_interest)
print(total_amount)