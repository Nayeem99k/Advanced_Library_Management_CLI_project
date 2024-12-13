import restore_books_file
import add_books
import view_all_books
import update_book_file
import delete_book_file
from datetime import datetime


# Function for lending a book
def lend_book(all_books):
    title = input("Enter the title of the book to lend: ")
    borrower_name = input("Enter borrower's name: ")
    borrower_phone = input("Enter borrower's phone number: ")

    for book in all_books:
        if book["title"].lower() == title.lower() and book["quantity"] > 0:
            return_date = input("Enter return date (YYYY-MM-DD): ")
            return_date = datetime.strptime(return_date, "%Y-%m-%d").date()
            print(f"Book '{title}' lent to {borrower_name}. Return by {return_date}.")
            book["quantity"] -= 1
            save_all_books(all_books)
            return all_books

    print("Sorry, the book is not available to lend.")
    return all_books


# Function for returning a book
def return_book(all_books):
    title = input("Enter the title of the book to return: ")
    borrower_name = input("Enter borrower's name: ")

    for book in all_books:
        if book["title"].lower() == title.lower():
            book["quantity"] += 1
            print(f"Book '{title}' returned by {borrower_name}.")
            save_all_books(all_books)
            return all_books

    print("Book not found.")
    return all_books


# Main program
all_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/Delete")
    print("5. Lend Book")
    print("6. Return Book")

    all_books = restore_books_file.restore_all_books(all_books)

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_book_file.update_books(all_books)
    elif menu == "4":
        delete_book_file.delete_books(all_books)
    elif menu == "5":
        all_books = lend_book(all_books)
    elif menu == "6":
        all_books = return_book(all_books)
    else:
        print("Choose a valid number")
