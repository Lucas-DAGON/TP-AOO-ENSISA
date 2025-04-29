class Person:
    """A class representing a person with a name and last_name."""
    def __init__(self, name: str, last_name: int):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def __repr__(self):
        return f"name(name={self.name}, last_name={self.last_name})"


class Book:
    """A class representing a book with a title, and author."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"title: {self.title}, author: {self.author}"

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author})"


class LibraryError(Exception):
    """Base class for Library errors"""
    print("LibraryError: Book not found in the library.")


class Library:
    """A class representing a library with a name, books, and authors."""
    _books: list = []
    _members: list = []
    _borrowed_books: dict = []
    
    def __init__(self, name: str):
        self.name = name
        

    def add_new_book(self, book: Book) -> None:
        """Add a new book to the library."""
        if book not in self._books:
            self._books.append(book)
            print(f"{book} has been added to the library.")
        else:
            print(f"{book} is already in the library.")

    def is_book_available(self, book: Book) -> bool:
        """Check if a book is available in the library."""
        try:
            if book not in self._books:
                raise LibraryError()
        except LibraryError as e:
            print(e)
            return False
        return book in self._books
    
    def borrow_book(self, book: Book, member: Person) -> None:
        """Borrow a book from the library."""
        if self.is_book_available(book):
            self._books.remove(book)
            self._borrowed_books.append(book)
            print(f"{member} borrowed {book}.")
        else:
            print(f"{book} is not available for borrowing.")

    def return_book(self, book: Book) -> None:
        """Return a book to the library."""
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            self._books.append(book)
            print(f"{book} was returned .")
        else:
            print(f"{book} was not borrowed from this library.")

    def add_new_member(self, member: Person) -> None:
        """Add a new member to the library."""
        if member not in self._members:
            self._members.append(member)
            print(f"{member} is now a member of {self.name}.")
        else:
            print(f"{member} is already a member of {self.name}.")

    def print_status(self) -> None:
        """Print the status of the library."""
        print(f"{self.name} status:")
        print("Books available:")
        for book in self._books:
            print(f"- {book}")
        print("Members:")
        for member in self._members:
            print(f"- {member}")
        print("Borrowed books:")
        for book in self._borrowed_books:
            print(f"- {book}")

def main():
    """main function to test the classes."""
    antoine = Person("Antoine", "Dupont")
    print(antoine)
    
    julia = Person("Julia", "Roberts")
    print(julia)
    
    rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
    print(rugby_book)
    
    novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
    print(novel_book)
    
    library = Library("Public library")
    library.print_status()
    
    library.add_new_book(rugby_book)
    library.add_new_book(novel_book)
    library.add_new_member(antoine)
    library.add_new_member(julia)
    library.print_status()
    
    print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
    library.borrow_book(rugby_book, antoine)
    library.print_status()
    
    try:
        library.borrow_book(rugby_book, julia)
    except LibraryError as error:
        print(error)
    
    try:
        library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(novel_book, Person("Simone", "Veil"))
    except LibraryError as error:
        print(error)

    try:
        library.return_book(novel_book)
    except LibraryError as error:
        print(error)

    library.return_book(rugby_book)
    library.borrow_book(novel_book, julia)
    library.print_status()

    library.borrow_book(rugby_book, julia)
    library.print_status()


if __name__ == "__main__":
    main()


