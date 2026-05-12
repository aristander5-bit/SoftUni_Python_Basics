budget = float(input())
total_video_cards = int(input())
total_processors = int(input())
total_rams = int(input())

price_video_cards = 250
price_processor = (total_video_cards * price_video_cards) * 0.35
price_rams = (total_video_cards * price_video_cards) * 0.10

total_amount = (total_video_cards * price_video_cards) + (total_processors * price_processor) + (total_rams * price_rams)

if total_video_cards > total_processors:
    discount = total_amount * 0.15
    total_amount -= discount

diff = abs(budget - total_amount)

if budget >= total_amount:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")