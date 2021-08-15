class Publisher:
    # Default value for name is N/A
    def __init__(self, name="N/A"):
        self.__name = "N/A"
        # Strip away any spaces

        if type(name) == str and name.strip() != "":
            if name.strip() != "N/A": self.__name = name.strip()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name="N/A"):
        self.__name = name.strip()

    def __repr__(self):
        return f"<Publisher {self.__name}>"

    def __eq__(self, other):
        if isinstance(other, Publisher):
            return self.__name == other.name

    def __lt__(self, other):
        if isinstance(other, Publisher):
            return self.__name < other.name

    def __hash__(self):
        return hash(self.__name)


