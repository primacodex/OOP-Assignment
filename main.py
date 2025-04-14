# main.py

from book import Book
from ebook import Ebook

def main():
    # Create a Book instance
    physical_book = Book("1984", "George Orwell", 328)
    print(physical_book.get_summary())
    print(physical_book.read())

    # Create an Ebook instance
    digital_book = Ebook("The Great Gatsby", "F. Scott Fitzgerald", 180, 1.5)
    print(digital_book.get_summary())
    print(digital_book.read())

if __name__ == "__main__":
    main()