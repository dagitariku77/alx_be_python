class Book:
  """
  This class represents a book in a library.
  """

  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute to track availability

  def check_out(self):
    """
    Marks the book as checked out.
    """
    self._is_checked_out = True

  def return_book(self):
    """
    Marks the book as returned.
    """
    self._is_checked_out = False

  def is_available(self):
    """
    Checks if the book is available.
    """
    return not self._is_checked_out


class Library:
  """
  This class represents a library that manages a collection of books.
  """

  def __init__(self):
    self._books = []  # Private list to store Book instances

  def add_book(self, book):
    """
    Adds a book to the library's collection.
    """
    self._books.append(book)

  def check_out_book(self, title):
    """
    Checks out a book by title if available.
    """
    for book in self._books:
      if book.title == title and book.is_available():
        book.check_out()
        print(f"{title} is checked out successfully.")
        return
    print(f"Sorry, {title} is not available for checkout.")

  def return_book(self, title):
    """
    Returns a book by title.
    """
    for book in self._books:
      if book.title == title:
        book.return_book()
        print(f"{title} is returned successfully.")
        return
    print(f"{title} is not found in the library.")

  def list_available_books(self):
    """
    Prints a list of all available books in the library.
    """
    print("Available books:")
    for book in self._books:
      if book.is_available():
        print(f"{book.title} by {book.author}")