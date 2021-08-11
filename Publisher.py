class Publisher:
    # Default value for name is N/A
    def __init__(self, name="N/A"):
        # Strip away any spaces
        self.__name = name.strip()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name="N/A"):
        self.__name = name.strip()

    def __repr__(self):
        return f"<Publisher {self.__name}>"

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __hash__(self):
        pass