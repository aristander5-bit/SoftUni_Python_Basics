pencils = int(input())
markers = int(input())
cleaning_solution = int(input())
pct_discount= int(input())

total_amound_pencils = pencils * 5.80
total_amound_markers = markers * 7.20
total_amound_cleaning_solution = cleaning_solution * 1.20
total_amound = total_amound_pencils + total_amound_markers + total_amound_cleaning_solution

discount = total_amound * (pct_discount / 100)
total_amound_with_discount = total_amound - discount
print(total_amound_with_discount)
