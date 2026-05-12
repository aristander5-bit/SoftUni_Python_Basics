
looking_book = input()
book_counter = 0

while True:
    new_book = input()

    if new_book == looking_book:
        print(f"You checked {book_counter} books and found it.")
        break
    if new_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break
    book_counter += 1

