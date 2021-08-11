class Author:
    def __init__(self, author_id, author_full_name):
        self.__full_name = author_full_name
        self.__unique_id = author_id

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass

    def __hash__(self):
        pass

    def add_coauthor(self, coauthor):
        pass

    def check_if_this_author_coauthored_with(self, author):
        pass