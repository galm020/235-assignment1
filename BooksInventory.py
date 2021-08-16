from Book import Book


class BooksInventory:
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
            self.__data[book.book_id] = {'title': book.title, 'price': price, 'stock': nr_books_in_stock}

    def remove_book(self, book_id):
        if isinstance(book_id, int):
            new_id = str(book_id)
            if new_id in self.__data:
                self.__data.pop(str(book_id))

    def find_book(self, book_id):
        if isinstance(book_id, int):
            if book_id in self.__data:
                return self.__data[book_id]
            else:
                return None

    def find_price(self, book_id):
        if isinstance(book_id, int):
            if book_id in self.__data:
                return self.__data[book_id]["price"]
            else:
                return None

    def find_stock_count(self, book_id):
        if isinstance(book_id, int):
            if book_id in self.__data:
                return self.__data[book_id]["stock"]
            else:
                return None

    def search_book_by_title(self, title):
        pass
