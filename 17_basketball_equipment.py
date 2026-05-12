yearly_tax = int(input())
sneakers = yearly_tax - (yearly_tax * 0.40)
equipment = sneakers - (sneakers * 0.20)
ball = equipment * 0.25
accessories = ball * 0.20
total_amount = yearly_tax + sneakers + equipment + ball + accessories
print(total_amount)