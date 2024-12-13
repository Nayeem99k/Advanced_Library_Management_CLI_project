import json
from datetime import datetime

def lend_book(all_books):
    title = input("Enter Book Title to Lend: ")
    for book in all_books:
        if book["title"] == title:
            if book["quantity"] > 0:
                # Collect borrower's details
                borrower_name = input("Enter Borrower's Name: ")
                borrower_phone = input("Enter Borrower's Phone Number: ")
                due_date = input("Enter Return Due Date (DD-MM-YYYY): ")

                # Create lend record
                lend_info = {
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": title,
                    "due_date": due_date
                }

                # Save lend info to file
                with open("lend_books.json", "a") as fp:
                    json.dump(lend_info, fp)
                    fp.write("\n")

                # Decrease book quantity
                book["quantity"] -= 1
                save_all_books(all_books)
                print(f"Book lent successfully to {borrower_name}. Due date for return: {due_date}")
                return all_books
            else:
                print("There are not enough books available to lend.")
                return all_books
    print("Book not found")
    return all_books
