from Book import Book
from Review import Review


class User:
    def __init__(self, user_name, password):
        self.__user_name = None

        if isinstance(user_name, str):
            if len(user_name.strip()) > 0:
                self.__user_name = user_name.strip().lower()
            else:
                raise ValueError
        else:
            raise ValueError

        self.__password = None

        if isinstance(password, str):
            if len(password) >= 7:
                self.__password = password
            else:
                raise ValueError
        else:
            raise ValueError

        self.__read_books = []
        self.__reviews = []
        self.__pages_read = 0

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def read_books(self):
        return self.__read_books

    @property
    def reviews(self):
        return self.__reviews

    @property
    def pages_read(self):
        return self.__pages_read

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.__user_name == other.user_name
        else:
            raise ValueError

    def __lt__(self, other):
        if isinstance(other, User):
            return self.__user_name < other.user_name
        else:
            raise ValueError

    def __hash__(self):
        return hash((self.__user_name, self.__password))

    def read_a_book(self, read_book):
        if isinstance(read_book, Book):
            self.__read_books.append(read_book)
            if read_book.num_pages is not None:
                self.__pages_read += read_book.num_pages
            else:
                raise ValueError
        else:
            raise ValueError

    def add_review(self, review):
        if isinstance(review, Review):
            self.__reviews.append(review)
        else:
            raise ValueError


books = [Book(874658, "Harry Potter"), Book(89576, "Lord of the Rings")]
books[0].num_pages = 107
books[1].num_pages = 121
user = User("Martin", "pw12345")
print(user.read_books)
print(user.pages_read)
for book in books:
    user.read_a_book(book)
print(user.read_books)
print(user.pages_read)
