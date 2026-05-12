
word = ""
final_result = ""

found_c = False
found_o = False
found_n = False

while True:
    command = input()
    if command == "End":
        break

    symbol = command

    if not (("a" <= symbol <= "z") or ("A" <= symbol <= "Z")):
        continue

    if symbol == "c" and not found_c:
        found_c = True
    elif symbol == "o"and not found_o:
        found_o = True
    elif symbol == "n"and not found_n:
        found_n = True
    else:
        word += symbol

    if found_c and found_o and found_n:
        final_result += word + " "
        word = ""
        found_c = False
        found_o = False
        found_n = False

print(final_result)





