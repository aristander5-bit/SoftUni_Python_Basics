
sector_last = input()
row_first_sector = int(input())
row_odd_seats = int(input())

total_seats = 0
row_current_sector = row_first_sector

for sector_code in range(ord("A"), ord(sector_last) + 1):
    sector_name = chr(sector_code)

    for row in range(1, row_current_sector + 1):
        if row % 2 != 0:
            seat_this_row = row_odd_seats
        else:
            seat_this_row = row_odd_seats + 2

        for seat_code in range(ord("a"), ord("a") + seat_this_row):
            seat_name = chr(seat_code)

            print(f"{sector_name}{row}{seat_name}")
            total_seats += 1

    row_current_sector += 1

print(f"{total_seats}")

