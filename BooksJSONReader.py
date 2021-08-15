import json

from Author import Author
from Book import Book
from Publisher import Publisher

"""
read_json_files(): this method opens the files associated with the BooksJSONReader object and reads the contents. 
You can use the built-in Python module json (import json) and very conveniently read the file into a list of dictionaries, 
one dictionary per book. The information required to read books is distributed among two files. The books file 
(comic_books_excerpt.json) contains the information about books. However, to also associate the correct authors with 
every book, we have to read in the authors file as well. The authors file (book_authors_excerpt.json) contains entries 
that connect author ids with author names (and other, for us currently not relevant, author related information). 
The books file contains for every book under the key 'authors' a list of author ids. These can be used to look up the 
respective author name in the authors file. You have to correctly read in the information from both files to create the 
dataset of books and pass our tests.
"""

"""
As a correction to our initial specification, please note that the data files actually contain collections of JSON objects, 
one per line in the data file. Each of these JSON objects is either an author or a book, depending on the data file.
"""


class BooksJSONReader:
    def __init__(self, books_file_name, authors_file_name):
        self.__dataset_of_books = []
        self.__books_file_name = books_file_name
        self.__authors_file_name = authors_file_name

    @property
    def dataset_of_books(self):
        return self.__dataset_of_books

    # @dataset_of_books.setter
    # def dataset_of_books(self, value):
    #     pass

    # book_authors: each line is an object that represents an author
    # comic_books: each line is an object that represents a book
    def read_json_files(self):
        # Dict of authors
        authors = {}
        # List of author objects
        file = open(self.__authors_file_name, "r")

        line = file.readline()

        # Reading the authors
        while line:
            temp_dict = json.loads(line)
            authors[temp_dict["author_id"]] = temp_dict
            line = file.readline()

        file.close()

        file = open(self.__books_file_name, "r")
        line = file.readline()

        # Reading the books
        while line:
            # Dictionary for each JSON line (object)
            temp_dict = json.loads(line)
            book = Book(int(temp_dict["book_id"]), temp_dict["title"])
            temp_publisher = Publisher(temp_dict["publisher"])
            book.publisher = temp_publisher
            temp_description = temp_dict["description"]
            book.description = temp_description
            temp_year = temp_dict["publication_year"]
            temp_pages = temp_dict["num_pages"]

            if len(temp_pages) > 0:
                book.num_pages = temp_pages

            if len(temp_year) > 0:
                book.release_year = int(temp_year)
            # A list of author dictionaries
            temp_authors = temp_dict["authors"]
            for a in temp_authors:
                # Create an author based on id and name
                temp_id = a["author_id"]
                temp_author = Author(int(temp_id), authors[temp_id]["name"])
                book.add_author(temp_author)

            book.ebook = bool(temp_dict["is_ebook"])

            self.__dataset_of_books.append(book)
            line = file.readline()

        file.close()

        # We need to combine the two dictionaries of the JSON files into a list of books

#
# authors_filename = 'book_authors_excerpt.json'
# books_filename = 'comic_books_excerpt.json'
# reader = BooksJSONReader(books_filename, authors_filename)
# reader.read_json_files()
# print(reader.dataset_of_books[0])
# print(reader.dataset_of_books[10])
# print(reader.dataset_of_books[19])
# print(reader.dataset_of_books[4].publisher)
# print(reader.dataset_of_books[15].authors[0])

authors_filename = 'book_authors_excerpt.json'
books_filename = 'comic_books_excerpt.json'
reader = BooksJSONReader(books_filename, authors_filename)
reader.read_json_files()

print(reader.dataset_of_books[4].title)
print(reader.dataset_of_books[4].release_year)
print(reader.dataset_of_books[4].description)