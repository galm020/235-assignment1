import json

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
    def __init__(self, books_file_name="", authors_file_name=""):
        self.__dataset_of_books = []

    # book_authors: each line is an object that represents an author
    # comic_books: each line is an object that represents a book
    def read_json_files(self):
        file = open("book_authors_excerpt.json", "r")

        line = file.readline()

        while line:
            self.__dataset_of_books.append(json.loads(line))
            line = file.readline()

        file.close()


b = BooksJSONReader()
b.read_json_files()
