from Book import Book


class ReadingList:
    def __init__(self):
        # read list of type book
        self.__reading_list = []
        self.__n = 0

    @property
    def reading_list(self):
        return self.__reading_list

    # @reading_list.setter
    # def reading_list(self, value):
    #     pass

    def add_book(self, book):
        if isinstance(book, Book):
            if book not in self.__reading_list:
                self.__reading_list.append(book)

    # def add_book(self, *books):
    #     for book in books:
    #         if isinstance(book, Book):
    #             self.__reading_list.append(book)

    def remove_book(self, book):
        if isinstance(book, Book):
            if book in self.__reading_list:
                self.__reading_list.remove(book)

    def select_book_to_read(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.__reading_list):
                return self.__reading_list[index]
            else:
                return None

    def size(self):
        return len(self.__reading_list)

    def first_book_in_list(self):
        if len(self.__reading_list) == 0:
            return None
        else:
            return self.__reading_list[0]

    def __iter__(self):
        self.__n = 0
        return self

    def __next__(self):
        if self.__n < len(self.__reading_list):
            num = self.__n
            self.__n += 1
            return self.__reading_list[num]
        else:
            raise StopIteration


