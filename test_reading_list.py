import pytest

from Book import Book
from ReadingList import ReadingList


@pytest.fixture
def reading_list_1():
    return ReadingList()


@pytest.fixture
def book_1():
    return Book(12345, "Book 1")


@pytest.fixture
def book_2():
    return Book(67890, "Book 2")


@pytest.fixture
def book_3():
    return Book(5555, "Book 3")


@pytest.fixture
def reading_list_2(book_1, book_2):
    r = ReadingList()
    r.add_book(book_1)
    r.add_book(book_2)
    return r


def test_constructor():
    # We must test that the constructor doesn't accept any parameters
    with pytest.raises(TypeError):
        ReadingList("Bob")

    ReadingList()


def test_add_book(book_1, book_2, reading_list_1):
    # Test: adding a book to a reading list
    reading_list_1.add_book(book_1)
    assert book_1 in reading_list_1.reading_list
    # Test: adding a book to a reading list that is already there
    reading_list_1.add_book(book_1)
    count = 0
    for i in reading_list_1.reading_list:
        if i == book_1:
            count += 1

    assert count == 1

    # Test: adding multiple books to a reading list and seeing what's at the front
    reading_list_1.add_book(book_2)
    assert book_2 in reading_list_1.reading_list


def test_remove_book(book_1, book_2, reading_list_1, reading_list_2):
    # Test: trying to pass in a non Book type; nothing happens
    # Test: removing a book that is not in the reading list
    reading_list_1.remove_book(book_1)
    # Nothing happens

    # Test: removing a book that is in the reading list
    reading_list_1.add_book(book_1)
    assert book_1 in reading_list_1.reading_list
    reading_list_1.remove_book(book_1)
    assert book_1 not in reading_list_1.reading_list

    # Test: adding and removing multiple books from a reading list
    reading_list_1.add_book(book_1)
    reading_list_1.add_book(book_2)
    assert book_1 in reading_list_1.reading_list
    assert book_2 in reading_list_1.reading_list
    reading_list_1.remove_book(book_1)
    reading_list_1.remove_book(book_2)
    reading_list_1.remove_book(book_1)
    assert book_1 not in reading_list_1.reading_list
    assert book_2 not in reading_list_1.reading_list

    # Test: trying to remove a book from an empty reading list

    # Test: removing a book that is in the front-most position

    # Test: seeing what's at the front of a reading list after removing frontmost item
    reading_list_2.remove_book(book_1)
    assert reading_list_2.first_book_in_list() == book_2


def test_select_book_to_read(book_1, book_2, reading_list_1):
    # Test: valid index is given; check that the appropriate book is returned
    reading_list_1.add_book(book_1)
    reading_list_1.add_book(book_2)
    assert reading_list_1.select_book_to_read(0) == book_1
    assert reading_list_1.select_book_to_read(1) == book_2
    assert 0 <= 0 and 1 < len(reading_list_1.reading_list)
    # Test: index is out of bounds; check that None is returned
    assert reading_list_1.select_book_to_read(10) is None
    # Test: index isn't a valid integer; nothing happens
    reading_list_1.select_book_to_read("a")


def test_size(book_1, book_2, reading_list_1):
    # Test: test size when there is nothing in the reading list
    assert reading_list_1.size() == 0
    # Test size when adding items
    reading_list_1.add_book(book_1)
    assert reading_list_1.size() == 1
    reading_list_1.add_book(book_2)
    assert reading_list_1.size() == 2

    reading_list_1.add_book(book_2)
    assert reading_list_1.size() == 2

    # Test size after removing items
    reading_list_1.remove_book(book_2)
    assert reading_list_1.size() == 1
    reading_list_1.remove_book(book_1)
    assert reading_list_1.size() == 0

    reading_list_1.add_book(book_1)
    reading_list_1.add_book(book_2)
    reading_list_1.remove_book(book_1)
    assert reading_list_1.size() == 1
    # Test size == len(reading_list)


def test_first_book_in_list(reading_list_1, reading_list_2, book_1, book_2):
    # Test: test that the first book to read in the list is returned
    assert reading_list_2.first_book_in_list() == book_1
    # Test: test that none is returned if there is nothing in the reading list
    assert reading_list_1.first_book_in_list() is None
    reading_list_2.remove_book(book_1)
    assert reading_list_2.first_book_in_list() == book_2
    reading_list_2.remove_book(book_2)
    assert reading_list_2.first_book_in_list() is None


def test_iteration(reading_list_1, reading_list_2, book_1, book_2, book_3):
    reading_list_2.add_book(book_3)

    for book in reading_list_2:
        print(book)

    for book in reading_list_1:
        print(book)
