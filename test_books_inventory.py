import pytest

from Book import Book
from BooksInventory import BooksInventory


@pytest.fixture()
def default_inventory():
    return BooksInventory()


@pytest.fixture()
def default_book():
    return Book(1234, "Default Book")


@pytest.fixture()
def harry_potter():
    return Book(555, "Harry Potter")


def test_constructor():
    BooksInventory()
    # data = b.data
    # assert data[Book(1234, "Bob")] == "test"


def test_add_book(default_inventory, default_book, harry_potter):
    # First we test that the book we add isn't invalid
    with pytest.raises(ValueError):
        # Value errors are raised in Book
        # Hence, the error raising is handled there
        b = Book(123, "")
        b2 = Book(" ", " ")
        b3 = Book(" ", 91919)
        default_inventory.add_book(b, 10, 100)
        default_inventory.add_book(b2, 10, 100)
        default_inventory.add_book(b3, 10, 100)

    default_inventory.add_book(default_book, "10", "100")
    assert (default_book.book_id, default_book.title) in default_inventory.data
    assert default_inventory.data[(default_book.book_id, default_book.title)] == {"price": "10", "stock": "100"}

    # default_inventory.add_book(harry_potter, 10, 100)
    # assert harry_potter not in default_inventory.data
    # assert default_inventory.find_book(1234) == default_book


def test_remove_book(default_inventory, default_book, harry_potter):
    default_inventory.add_book(default_book, "10", "100")
    # Here, we test that remove book does nothing if the book isn't in the inventory
    default_inventory.remove_book((harry_potter.book_id, harry_potter.title))
    assert (harry_potter.book_id, harry_potter.title) not in default_inventory.data

    default_inventory.add_book(harry_potter, "10", "100")
    default_inventory.add_book(default_book, "10", "100")
    default_inventory.remove_book(harry_potter.book_id)
    assert (harry_potter.book_id, harry_potter.title) not in default_inventory.data
    default_inventory.remove_book(default_book.book_id)
    assert (default_book.book_id, default_book.title) not in default_inventory.data

#
# def test_find_book(default_inventory, default_book):
#     default_inventory.add_book(default_book)
#     assert default_inventory.find_book(1234) == default_book


def test_find_book(default_inventory, harry_potter, default_book):
    # If the book isn't in the inventory, return None
    assert default_inventory.find_book(10) is None
    default_inventory.add_book(harry_potter, 10, 100)
    assert default_inventory.find_book(555) == {"price": 10, "stock": 100}


def test_find_price(default_inventory, harry_potter):
    default_inventory.add_book(harry_potter, 10000, 50)
    assert default_inventory.find_price(555) == 10000
    assert default_inventory.find_price(69) is None


def test_find_stock_count(default_inventory, harry_potter):
    default_inventory.add_book(harry_potter, 10000, 50)
    assert default_inventory.find_stock_count(555) == 50
    assert default_inventory.find_stock_count(69) is None


def test_search_book_by_title(default_inventory, harry_potter, default_book):
    # default_inventory.add_book(harry_potter, 1000, 10)
    # default_inventory.add_book(default_book, 50, 20)
    # assert
    pass