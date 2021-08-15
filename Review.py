import datetime

from Book import Book


class Review:
    def __init__(self, book, review_text, rating):
        if isinstance(book, Book):
            self.__book = book

        if isinstance(review_text, str):
            self.__review_text = review_text.strip()
        else:
            self.__review_text = "N/A"

        if isinstance(rating, int):
            if 1 <= rating <= 5:
                self.__rating = rating
            else:
                raise ValueError
        else:
            raise ValueError

        self.__timestamp = datetime.datetime.now()

    def __repr__(self):
        return f"Review for {self.__book}: {self.__review_text} %n {self.__rating}/10"

    def __eq__(self, other):
        if isinstance(other, Review):
            return self.__book == other.book and self.__review_text == other.review_text and \
                   self.__rating == other.rating \
                   and self.__timestamp == other.timestamp

    @property
    def book(self):
        return self.__book

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp
