import pytest

from Author import Author
from Book import Book
from Publisher import Publisher


@pytest.fixture
def harry_potter():
    return Book(84765876, "Harry Potter")


@pytest.fixture
def book_1():
    return Book(123456, "  Ship at Sea     ")


@pytest.fixture
def publisher_1():
    return Publisher("Bloomsbury")


@pytest.fixture
def author_1():
    return Author(635, "J.K. Rowling")


@pytest.fixture
def author_2():
    return Author(69, "Bob Smith")


@pytest.fixture
def author_3():
    return Author(10000, "James Watts")


def test_constructor():
    # First we check that the title is a string
    with pytest.raises(ValueError):
        Book(123, 55)
    # Next we check that the title isn't an empty string
    with pytest.raises(ValueError):
        Book(125, "  ")
        Book(555, "")

    with pytest.raises(ValueError):
        Book("test", "Hello")

    with pytest.raises(ValueError):
        Book(-50, "Hello")


def test_publisher(harry_potter, publisher_1, book_1):
    harry_potter.publisher = publisher_1
    assert harry_potter.publisher == publisher_1

    with pytest.raises(ValueError):
        harry_potter.publisher = 10

    book_1.publisher = publisher_1
    assert book_1.publisher == publisher_1


def test_title(harry_potter, book_1):
    assert harry_potter.title == "Harry Potter"
    assert book_1.title == "Ship at Sea"

    with pytest.raises(ValueError):
        harry_potter.title = 12345
        harry_potter.title = "    "


def test_description(harry_potter, book_1):
    harry_potter.description = "   A book about a boy.      "
    assert harry_potter.description == "A book about a boy."

    with pytest.raises(ValueError):
        book_1.description = 69420


def test_add_author(harry_potter, author_1, author_2, author_3):
    harry_potter.add_author(author_1)
    harry_potter.add_author(author_2)
    harry_potter.add_author(author_3)

    with pytest.raises(ValueError):
        harry_potter.add_author(author_1)
        harry_potter.add_author(125)

    harry_potter.remove_author(author_1)
    assert author_1 not in harry_potter.authors

    assert harry_potter.authors == [author_2, author_3]


def test_authors(harry_potter, author_1, author_2, author_3):
    harry_potter.authors = [author_1, author_2, author_3]

    assert harry_potter.authors == [author_1, author_2, author_3]

    with pytest.raises(ValueError):
        harry_potter.authors = 50
        harry_potter.authors = author_1


def test_release_year(harry_potter):
    harry_potter.release_year = 1920

    with pytest.raises(ValueError):
        harry_potter.release_year = -1000


def test_remove_author(harry_potter, author_1, author_2, author_3):
    harry_potter.add_author(author_1)
    harry_potter.add_author(author_2)

    with pytest.raises(ValueError):
        harry_potter.remove_author(author_3)