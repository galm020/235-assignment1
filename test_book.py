import pytest

from Author import Author
from Book import Book
from Publisher import Publisher


@pytest.fixture
def harry_potter():
    return Book(84765876, "Harry Potter")


@pytest.fixture
def publisher_1():
    return Publisher("Bloomsbury")


@pytest.fixture
def author_1():
    return Author(635, "J.K. Rowling")


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