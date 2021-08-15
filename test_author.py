import pytest

from Author import Author


@pytest.fixture
def default_author():
    return Author(123, "default")


@pytest.fixture
def obama():
    return Author(3675, "Barack Obama")


@pytest.fixture
def author_1():
    return Author(0, "Ben")


@pytest.fixture
def author_2():
    return Author(76, "Jorge")


@pytest.fixture
def author_3():
    return Author(59, "James")


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


def test_blank_author():
    with pytest.raises(ValueError):
        Author(0, " ")


# Test setters and getters
def test_fullname_getter(default_author, obama):
    assert default_author.full_name == "default"
    assert obama.full_name == "Barack Obama"


def test_fullname_setter(default_author, obama):
    with pytest.raises(ValueError):
        default_author.full_name = 10

    default_author.full_name = "Bob"
    assert default_author.full_name == "Bob"

    obama.full_name = "Joe Biden"
    assert obama.full_name == "Joe Biden"


# Test the setters and getters of unique id
def test_unique_id_getter(default_author, obama):
    assert default_author.unique_id == 123
    assert obama.unique_id == 3675


def test_unique_id_setter(default_author):
    with pytest.raises(AttributeError):
        default_author.unique_id = 10
        obama.unique_id = -100

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


def test_hash(obama, default_author):
    assert hash(obama) is not hash(default_author)
    assert hash(obama) == hash(obama)


def test_add_coauthor(default_author, obama):
    ca1 = Author(4, "James")
    ca2 = Author(10, "Zane")

    default_author.add_coauthor(ca1)
    obama.add_coauthor(ca2)

    assert default_author.check_if_this_author_coauthored_with(ca1)
    assert obama.check_if_this_author_coauthored_with(ca2)

    assert ca1.check_if_this_author_coauthored_with(default_author)
    assert ca2.check_if_this_author_coauthored_with(obama)

    # Check that blank coauthors don't cause the test to pass

    with pytest.raises(ValueError):
        ca3 = Author(3, "")
        assert not default_author.check_if_this_author_coauthored_with(ca3)
        assert not obama.check_if_this_author_coauthored_with(ca3)

        assert not ca3.check_if_this_author_coauthored_with(default_author)
        assert not ca3.check_if_this_author_coauthored_with(obama)


def test_sorting(default_author, obama, author_1, author_2, author_3):
    assert sorted([default_author, obama, author_1, author_2, author_3]) == [author_1, author_3, author_2, default_author, obama]
