class Book:
  """
  A base class representing a book with title and author attributes.
  """

  def __init__(self, title, author):
    """
    Initializes a Book instance with the given title and author.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
    """
    self.title = title
    self.author = author

class EBook(Book):
  """
  A class representing an electronic book, inheriting from Book and adding a file_size attribute.
  """

  def __init__(self, title, author, file_size):
    """
    Initializes an EBook instance with title, author, and file size.

    Args:
      title (str): The title of the ebook.
      author (str): The author of the ebook.
      file_size (int): The file size of the ebook in KB.
    """
    super().__init__(title, author)  # Call base class constructor
    self.file_size = file_size

class PrintBook(Book):
  """
  A class representing a printed book, inheriting from Book and adding a page_count attribute.
  """

  def __init__(self, title, author, page_count):
    """
    Initializes a PrintBook instance with title, author, and page count.

    Args:
      title (str): The title of the printed book.
      author (str): The author of the printed book.
      page_count (int): The page count of the printed book.
    """
    super().__init__(title, author)  # Call base class constructor
    self.page_count = page_count

class Library:
  """
  A class representing a library that manages a collection of books.
  """

  def __init__(self):
    """
    Initializes a Library instance with an empty list to store books.
    """
    self.books = []

  def add_book(self, book):
    """
    Adds a Book, EBook, or PrintBook instance to the library's collection.

    Args:
      book (Book, EBook, or PrintBook): The book instance to add.
    """
    self.books.append(book)

  def list_books(self):
    """
    Prints details of each book in the library.
    """
    for book in self.books:
      # Print book details based on type
      if isinstance(book, EBook):
        print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
      elif isinstance(book, PrintBook):
        print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
      else:
        print(f"Book: {book.title} by {book.author}")