import pytest

from Author import Author


@pytest.fixture
def default_author():
    return Author(123, "default")


@pytest.fixture
def obama():
    return Author(3675, "Barack Obama")


# @pytest.fixture
# def authors_list1():
#     return Author[Author(5, "Bob"), Author(6, "Bob"), Author(1, "Jan"), Author(112, "Zane")]


def test_invalid_unique_id():
    with pytest.raises(ValueError):
        Author(-10, "Bob")


def test_invalid_unique_idtype():
    with pytest.raises(ValueError):
        Author("Bob", "default")


def test_invalid_author_name():
    with pytest.raises(ValueError):
        Author(10, 199)


# Test setters and getters
def test_fullname_getter(default_author):
    assert default_author.full_name == "default"


def test_fullname_setter(default_author):
    with pytest.raises(ValueError):
        default_author.full_name = 10


# Test the setters and getters of unique id
def test_unique_id_getter(default_author):
    assert default_author.unique_id == 123


def test_unique_id_setter(default_author):
    with pytest.raises(ValueError):
        default_author.unique_id = 10

    assert default_author.unique_id == 123


def test_repr(default_author, obama):
    assert default_author.__repr__() == "<Author default, author id = 123>"
    assert obama.__repr__() == "<Author Barack Obama, author id = 3675>"


def test_equality(default_author, obama):
    assert default_author != obama
    assert obama == obama


def test_lt(default_author, obama):
    assert default_author < obama
    assert obama > default_author

    # for i in range(0, len(authors_list1) - 1):
    #     assert authors_list1[i] < authors_list1[i + 1]


def test_hash():
    pass


def test_add_coauthor():
    pass


def check_if_this_author_coauthored_with():
    pass
