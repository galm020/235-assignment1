class Author:
    # TODO: Make this code pass hidden test cases -> write unit tests
    def __init__(self, author_id, author_full_name):
        if type(author_id) != int:
            raise ValueError
        elif author_id < 0:
            raise ValueError
        else:
            self.__unique_id = author_id

        if type(author_full_name) != str:
            raise ValueError
        elif len(author_full_name.strip()) == 0:
            raise ValueError
        else:
            self.__full_name = author_full_name

        self.__co_author = None

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        if isinstance(full_name, str):
            if len(full_name.strip() > 0):
                self.__full_name = full_name

    @property
    def unique_id(self):
        return self.__unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        raise AttributeError

    def __eq__(self, other):
        if isinstance(other, Author):
            return self.__unique_id == other.unique_id

    def __repr__(self):
        return f"<Author {self.__full_name}, author id = {self.__unique_id}>"

    def __hash__(self):
        return hash(self.__unique_id)

    def __lt__(self, other):
        if isinstance(other, Author):
            return self.__unique_id < other.unique_id and self.__full_name < other.__full_name

    def add_coauthor(self, coauthor):
        if isinstance(coauthor, Author):
            self.__co_author = coauthor

    def check_if_this_author_coauthored_with(self, author):
        if isinstance(author, Author):
            return self.__co_author == author


author1 = Author(3675, "Barack Obama")
print(author1)
try:
    author2 = Author(123, "  ")
    print(author2)
except ValueError:
    print("ValueError was raised!")
try:
    author3 = Author(42, 42)
    print(author3)
except ValueError:
    print("ValueError was raised!")
author4 = Author(23, "J.R.R. Tolkien")
print(author4.unique_id, author4.full_name)
