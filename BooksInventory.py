from Book import Book


class BooksInventory:
    # TODO: just make price and stock part of Book.py; this makes the tuple redundant -> only need the id after this
    def __init__(self):
        self.__data = {}

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        pass

    def add_book(self, book, price, nr_books_in_stock):
        # and isinstance(price, int) and isinstance(nr_books_in_stock, int)
        if isinstance(book, Book):
            self.__data[(book.book_id, book.title)] = {'price': price, 'stock': nr_books_in_stock}

    def remove_book(self, book_id):
        if isinstance(book_id, int) or isinstance(book_id, str):
            # if book_id in self.__data:
            #     self.__data.pop(book_id)
            for k in self.__data.keys():
                if k[0] == book_id:
                    self.__data.pop(k)
                    break

    def find_book(self, book_id):
        if isinstance(book_id, int) or isinstance(book_id, str):
            # if book_id in self.__data:
            #     return self.__data[book_id]
            for k in self.__data.keys():
                if k[0] == book_id:
                    return self.__data[k]

            return None

    def find_price(self, book_id):
        if isinstance(book_id, int) or isinstance(book_id, str):
            # if book_id in self.__data:
            #     return self.__data[book_id]["price"]
            for k in self.__data.keys():
                if k[0] == book_id:
                    return self.__data[k]["price"]

            return None

    def find_stock_count(self, book_id):
        if isinstance(book_id, int) or isinstance(book_id, str):
            # if book_id in self.__data:
            #     return self.__data[book_id]["stock"]
            for k in self.__data.keys():
                if k[0] == book_id:
                    return self.__data[k]["stock"]

            return None

    def search_book_by_title(self, title):
        pass
