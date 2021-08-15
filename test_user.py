import pytest

from Book import Book
from Review import Review
from User import User

"""
Make sure you spelling of everything is correct.
make sure you check password length and type.
Check username type.
make sure you remove whitespace and make username lower case.
make sure all the class variables have read only methods
make sure your string __repr__ method works
check your equality method checks works
check your less than method works
check you hash returns something
check read_a_book(book) adds the book and sums the pages correctly.
makes sure in add_review(review) that review is the correct class
"""


@pytest.fixture
def default_user():
    return User("default", "1234567")


@pytest.fixture
def user_1():
    return User("User name", "ABCDEFGHIJK:")


@pytest.fixture
def bob():
    return User("Bob", "bobiscool123")


@pytest.fixture
def bob2():
    return User("Bob", "bobbutdifferent")


def test_constructor(default_user):
    with pytest.raises(ValueError):
        a = User(123, "hello")
        assert a.user_name is None
        User("   ", "hello")

    assert default_user.password == "1234567"

    with pytest.raises(ValueError):
        User("Test", 555)
        a = User("Test", "Not")
        assert a.password is None


def test_equality(default_user, bob, bob2):
    assert default_user == default_user
    assert bob != default_user
    assert default_user != bob
    assert bob == bob
    assert bob == bob2


def test_read_a_book(bob, bob2):
    # with pytest.raises(ValueError):
    #     bob.read_a_book(123)

    b = Book(12345, "Cool book")
    b.num_pages = 123

    bob.read_a_book(b)
    assert b in bob.read_books
    assert bob.pages_read == 123

    b2 = Book(10, "ABC")

    # with pytest.raises(ValueError):
    #     bob.read_a_book(b2)

    b2.num_pages = 1000
    bob.read_a_book(b2)

    assert bob.pages_read == 1123
    assert b2 in bob.read_books

    b2.num_pages = -100

    # with pytest.raises(ValueError):
    #     bob.read_a_book(b2)


def test_add_review(bob):
    # with pytest.raises(ValueError):
    #     bob.add_review(123)

    r = Review(None, "ABC", 4)
    bob.add_review(r)


def test_usernames():
    u1 = User("       JAMES     ", "ABCDEFGHI")
    assert u1.user_name == "james"
    u2 = User("               ", "                 ")


def test_lt(bob, bob2, default_user, user_1):
    assert sorted([bob, bob2, default_user, user_1]) == [bob, bob2, default_user, user_1]
    assert bob < default_user


def test_hash(bob):
    assert hash(bob) is not None


# def test_repr(bob, user_1):
#     with pytest.raises(ValueError):
#         u = User(None, "ABCDEFGHIJ")
#         assert u.__repr__() == "<User None>"