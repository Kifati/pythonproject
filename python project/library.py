class Library:
    def __init__(self, data_file):
        self.data_file = data_file
        self.books = self.load_data()

    def load_data(self):
        books = {}
        try:
            with open(self.data_file, 'r') as file:
                for line in file:
                    title, author, available = line.strip().split(',')
                    books[title] = {'author': author, 'available': available == 'True'}
        except FileNotFoundError:
            print("Data file not found. Starting with an empty library.")
        return books

    def save_data(self):
        with open(self.data_file, 'w') as file:
            for title, book_info in self.books.items():
                author = book_info['author']
                available = str(book_info['available'])
                file.write(f"{title},{author},{available}\n")

    def publish_book(self, title, author):
        if title not in self.books:
            self.books[title] = {'author': author, 'available': True}
            self.save_data()
            print(f"Book '{title}' by {author} published successfully.")
        else:
            print("Book already exists in the library.")

    def issue_book(self, title):
        if title in self.books and self.books[title]['available']:
            self.books[title]['available'] = False
            print(f"Book '{title}' issued successfully.")
        elif title in self.books and not self.books[title]['available']:
            print(f"Book '{title}' is not available. It has already been issued.")
        else:
            print("Book not found in the library.")

    def return_book(self, title):
        if title in self.books and not self.books[title]['available']:
            self.books[title]['available'] = True
            print(f"Book '{title}' returned successfully.")
        elif title in self.books and self.books[title]['available']:
            print(f"Book '{title}' is already available in the library.")
        else:
            print("Book not found in the library.")

    def check_book_availability(self, title):
        if title in self.books and self.books[title]['available']:
            print(f"Book '{title}' is available in the library.")
        elif title in self.books and not self.books[title]['available']:
            print(f"Book '{title}' is not available. It has been issued.")
        else:
            print("Book not found in the library.")

def main():
    data_file = "library_data.txt"
    library = Library(data_file)

    while True:
        print("\n****** Library Management System ******")
        print("1. Publish a Book")
        print("2. Issue a Book")
        print("3. Return a Book")
        print("4. Check Book Availability")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            library.publish_book(title, author)
        elif choice == '2':
            title = input("Enter the title of the book to issue: ")
            library.issue_book(title)
        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        elif choice == '4':
            title = input("Enter the title of the book to check availability: ")
            library.check_book_availability(title)
        elif choice == '5':
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
