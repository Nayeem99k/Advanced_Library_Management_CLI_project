import json
from datetime import datetime


def return_book(all_books):
    title = input("Enter Book Title to Return: ")
    found_lend = False

    # Load lend books data
    try:
        with open("lend_books.json", "r") as fp:
            lend_books = [json.loads(line) for line in fp]
    except FileNotFoundError:
        lend_books = []

    # Search for the corresponding lend entry
    for lend in lend_books:
        if lend["book_title"] == title:
            borrower_name = lend["borrower_name"]
            lend_books.remove(lend)  # Remove lend entry

            # Update book quantity
            for book in all_books:
                if book["title"] == title:
                    book["quantity"] += 1
                    save_all_books(all_books)
                    found_lend = True
                    break

            # Save updated lend records
            with open("lend_books.json", "w") as fp:
                for lend_entry in lend_books:
                    json.dump(lend_entry, fp)
                    fp.write("\n")

            if found_lend:
                print(f"Book returned successfully by {borrower_name}")
            return all_books

    print("No lend record found for this book")
    return all_books
