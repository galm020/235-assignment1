import pytest

from Author import Author


@pytest.fixture
def default_author():
    return Author(123, "default")


def test_invalid_author_id():
    with pytest.raises(ValueError):
        Author(-10, "Bob")


def test_invalid_author_idtype():
    with pytest.raises(ValueError):
        Author("Bob", "default")


def test_invalid_author_name():
    with pytest.raises(ValueError):
        Author(10, 199)


# Test setters and getters
def test_fullname_getter(default_author):
    assert default_author.author_full_name == "default"


def test_fullname_setter(default_author):
    with pytest.raises(ValueError):
        default_author.author_full_name = 10


