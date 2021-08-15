from Author import Author
from Publisher import Publisher


class Book:
    def __init__(self, book_id, title):
        # We must ensure that the id and title are valid types as well as not negative or empty
        if isinstance(title, str):
            if len(title.strip()) > 0:
                self.__title = title.strip()
            else:
                raise ValueError
        else:
            raise ValueError

        if isinstance(book_id, int):
            if book_id > 0:
                self.__book_id = book_id
            else:
                raise ValueError
        else:
            raise ValueError

        self.__authors = []

        self.__publisher = None
        self.__description = None
        self.__release_year = None
        self.__ebook = None
        self.__num_pages = None

    @property
    def book_id(self):
        return self.__book_id

    @property
    def num_pages(self):
        return self.__num_pages

    @num_pages.setter
    def num_pages(self, value):
        if isinstance(value, int):
            self.__num_pages = value

    #
    # @book_id.setter
    # def book_id(self, value):
    #     pass

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        if isinstance(value, Publisher):
            self.__publisher = value
        else:
            raise ValueError

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            if len(value.strip()) > 0:
                self.__title = value.strip()
            else:
                raise ValueError
        else:
            raise ValueError

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self.__description = value.strip()
        else:
            raise ValueError

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__release_year = value
            else:
                raise ValueError
        else:
            raise ValueError

    @property
    def ebook(self):
        return self.__ebook

    @ebook.setter
    def ebook(self, value):
        if isinstance(value, bool):
            self.__ebook = value
        else:
            raise ValueError

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # if isinstance(value, Author) and isinstance(value, list):
        if isinstance(value, list):
            for val in value:
                if not isinstance(val, Author):
                    raise ValueError
            self.__authors = value
        else:
            raise ValueError

    def __repr__(self):
        return f"<Book {self.__title}, book id = {self.__book_id}>"

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.__book_id < other.book_id

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.__book_id == other.book_id

    def __hash__(self):
        return hash(self.__book_id)

    def add_author(self, author):
        if isinstance(author, Author) and not (author in self.__authors):
            self.__authors.append(author)
        else:
            raise ValueError

    def remove_author(self, author):
        if isinstance(author, Author) and author in self.__authors:
            self.__authors.remove(author)
        # else:
        #     raise ValueError