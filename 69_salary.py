
num_tabs_open = int(input())
salary = int(input())
have_salary = True

for _ in range(num_tabs_open):
    new_tab = input()
    if new_tab == "Facebook":
        salary -= 150
    elif new_tab == "Instagram":
        salary -= 100
    elif new_tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print(f"You have lost your salary.")
        have_salary = False
        break

if have_salary:
    print(salary)


