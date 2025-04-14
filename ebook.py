# ebook.py

from book import Book

class Ebook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # Call the parent constructor
        self.file_size = file_size  # Additional attribute for Ebook

    def get_summary(self):
        return f"{self.title} by {self.author}, {self.pages} pages, File size: {self.file_size}MB."

    def read(self):
        return f"You are reading the ebook {self.title} on your device."