
letters_start = input()
letters_end = input()
letters_skip = input()

counter = 0

for n_1 in range(ord(letters_start), ord(letters_end) + 1):
    for n_2 in range(ord(letters_start), ord(letters_end) + 1):
        for n_3 in range(ord(letters_start), ord(letters_end) + 1):

            char_1 = chr(n_1)
            char_2 = chr(n_2)
            char_3 = chr(n_3)

            if char_1 != letters_skip and char_2 != letters_skip and char_3 != letters_skip:
                print(f"{char_1}{char_2}{char_3}", end= " ")
                counter += 1


print(counter)