
count_men = int(input())
count_women = int(input())
table_max = int(input())

table_used = 0

for man in range(1, count_men + 1):
    for women in range(1, count_women + 1):

        if table_used < table_max:
            print(f"({man} <-> {women})", end = " ")
            table_used += 1
        else:
            break
    if table_used >= table_max:
        break
