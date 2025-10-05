class Book:
    """
    Represents a book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """Initialize a new book with title, author and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """
    Represents a collection of books and methods to manage them.
    """
    def __init__(self):
        """Initialize an empty library collection."""
        self._books = []

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Marks a book as checked out if available."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return  # ✅ no print or return message

    def return_book(self, title):
        """Marks a book as returned."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return  # ✅ no print or return message

    def list_available_books(self):
        """Lists all available (not checked out) books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
