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
        pass

    def __lt__(self, other):
        pass

    def __hash__(self):
        pass


publisher1 = Publisher("Avatar Press")
print(publisher1)
publisher2 = Publisher("  ")
print(publisher2)
publisher3 = Publisher("  DC Comics ")
print(publisher3)
publisher4 = Publisher(42)
print(publisher4)
