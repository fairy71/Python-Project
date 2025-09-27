class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added '{title}' by {author}.")

    def show_books(self):
        for i, book in enumerate(self.books):
            status = "Available" if book.available else "Checked Out"
            print(f"{i+1}. {book.title} by {book.author} - {status}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"You borrowed '{title}'.")
                return
        print("Book not available.")

library = Library()
library.add_book("Python Crash Course", "Eric Matthes")
library.add_book("Automate the Boring Stuff", "Al Sweigart")
library.show_books()
library.borrow_book("Python Crash Course")
library.show_books()





import tkinter as tk
from tkinter import scrolledtext

def send_message():
    msg = entry.get()
    chat_window.insert(tk.END, "You: " + msg + "\n")
    entry.delete(0, tk.END)
    respond(msg)

def respond(msg):
    response = "I'm just a simple bot."
    if "hello" in msg.lower():
        response = "Hi there!"
    elif "bye" in msg.lower():
        response = "Goodbye!"
    chat_window.insert(tk.END, "Bot: " + response + "\n")

root = tk.Tk()
root.title("AI Chatbot")
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_window.pack()
entry = tk.Entry(root, width=40)
entry.pack()
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()
root.mainloop()
