class Author:
    def __init__(self, unique_id, full_name):
        # Default values for the id and name
        # self.__unique_id = None
        # self.__full_name = None

        # Check that the id that has been entered is an integer
        if isinstance(unique_id, int):
            # Ensure that the entered author id is a positive integer
            if unique_id < 0:
                raise ValueError
            else:
                self.__unique_id = unique_id

        else:
            raise ValueError

        # Now we have to check that the entered name is a string
        if isinstance(full_name, str):
            if len(full_name.strip()) > 0:
                self.__full_name = full_name
            else:
                raise ValueError
        else:
            raise ValueError

        self.__coAuthor = None

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        if isinstance(value, str):
            self.__full_name = value
        else:
            raise ValueError

    @property
    def unique_id(self):
        return self.__unique_id

    @unique_id.setter
    def unique_id(self, value):
        raise ValueError

    def __repr__(self):
        return f"<Author {self.__full_name}, author id = {self.__unique_id}>"

    def __eq__(self, other):
        if isinstance(other, Author):
            return self.__unique_id == other.unique_id

    def __lt__(self, other):
        if isinstance(other, Author):
            return self.__unique_id < other.unique_id

    def __hash__(self):
        return hash(self.__unique_id)

    def add_coauthor(self, coauthor):
        if isinstance(coauthor, Author):
            self.__coAuthor = coauthor

    def check_if_this_author_coauthored_with(self, author):
        if isinstance(author, Author):
            if self.__coAuthor is not None:
                return author == self.__coAuthor
            else: raise ValueError
