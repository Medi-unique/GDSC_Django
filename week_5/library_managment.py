
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = True

    def display_details(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)
        print("Availability:", "Available" if self.availability_status else "Not Available")

    def update_availability(self, status):
        self.availability_status = status


class Transaction:
    def __init__(self, book, user):
        self.book = book
        self.user = user

        self.transaction_type = None
        self.transaction_date = None

    def record_transaction(self, transaction_type):
        self.transaction_type = transaction_type
        

    def generate_report(self):
        print("Transaction Type:", self.transaction_type)
        print("Transaction Date:", self.transaction_date)
        print("Book Details:")
        self.book.display_details()
        print("User Details:")
        self.user.display_details()


class User:
    def __init__(self, name, id, contact_info):
        self.name = name
        self.id = id
        self.contact_info = contact_info

    def display_details(self):
        print("User Name:", self.name)
        print("User ID:", self.id)
        print("Contact Info:", self.contact_info)


class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def register_user(self, name, id, contact_info):
        user = User(name, id, contact_info)
        self.users.append(user)

    def borrow_book(self, book_id, user_id):
        book = self._find_book_by_id(book_id)
        user = self._find_user_by_id(user_id)

        if book and user:
            if book.availability_status:
                transaction = Transaction(book, user)
                transaction.record_transaction("Borrowed")
                book.update_availability(False)
                print("Book borrowed successfully.")
            else:
                print("Book is not available for borrowing.")
        else:
            print("Invalid book ID or user ID.")

    def return_book(self, book_id, user_id):
        book = self._find_book_by_id(book_id)
        user = self._find_user_by_id(user_id)

        if book and user:
            if not book.availability_status:
                transaction = Transaction(book, user)
                transaction.record_transaction("Returned")
                book.update_availability(True)
                print("Book returned successfully.")
            else:
                print("Book is already marked as available.")
        else:
            print("Invalid book ID or user ID.")

    def generate_transaction_report(self):
        for transaction in self.transactions:
            transaction.generate_report()

    def _find_book_by_id(self, book_id):
        for book in self.books:
            if book.isbn == book_id:
                return book
        return None

    def _find_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None


