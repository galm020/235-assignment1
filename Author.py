class Author:
    def __init__(self, author_id, author_full_name):
        # Check that the id that has been entered is an integer
        if isinstance(author_id, int):
            # Ensure that the entered author id is a positive integer
            if author_id < 0:
                raise ValueError
            else:
                self.__author_id = author_id

        else:
            raise ValueError

        # Now we have to check that the entered name is a string
        if isinstance(author_full_name, str):
            self.__author_full_name = author_full_name
        else:
            raise ValueError

    @property
    def author_full_name(self):
        return self.__author_full_name

    @author_full_name.setter
    def author_full_name(self, value):
        if isinstance(value, str):
            self.__author_full_name = value
        else:
            raise ValueError
