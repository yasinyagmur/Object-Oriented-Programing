# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title,author,pages,price):
        self.title = title
        # TODO: add properties
        self.author= author
        self.pages= pages
        self.price= price


    # TODO: create instance methods


# TODO: create some book instances
b1 = Book("War and Peace")
b2 = Book("The Catcher in the Rye")

# TODO: print the price of book1


# TODO: try setting the discount


# TODO: properties with double underscores are hidden by the interpreter
