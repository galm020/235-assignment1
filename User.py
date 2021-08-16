from Book import Book
from Review import Review


class User:
    def __init__(self, user_name, password):
        self.__user_name = None

        if isinstance(user_name, str) and user_name:
            self.__user_name = user_name.strip().lower()

        self.__password = None

        if isinstance(password, str) and password:
            if len(password) >= 7:
                self.__password = password


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

    def __lt__(self, other):
        if isinstance(other, User):
            return self.__user_name < other.user_name

    def __hash__(self):
        return hash(self.__user_name)

    def read_a_book(self, read_book):
        if isinstance(read_book, Book):
            self.__read_books.append(read_book)
            if read_book.num_pages is not None and read_book.num_pages >= 0:
                self.__pages_read += read_book.num_pages

    def add_review(self, review):
        if isinstance(review, Review):
            self.__reviews.append(review)

