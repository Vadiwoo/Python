print('''In Python, classes are defined with the 'class' keyword  ''')

print("\n********** creating a class : the basic form *********")


# Creating a class called Book
class Book:
    publisher = "Woo,Inc"


# Creating an object of the class Book
b1 = Book()
print(" Book b1 publisher is : ", b1.publisher)
b2 = Book()
print(" Book b2 publisher is : ", b2.publisher)

print("\n********** creating a class : using the __init__() function *********")
print('''All classes in python have the __init__() function which will be executed when a class is created. ''')
print("\n********** the self parameter *********")
print('''The self parameter is a reference to the current instance of the class. It is actually can be named 
anything. ''')


class Book:
    def __init__(self, title="undecided", name="Woo,Inc"):
        self.publisher = name
        self.title = title

    def title(self):
        print("The title of this book is :", self.title)


# Creating an object of the class Book
b1 = Book()  # object is created with default publisher name
print(" Book b1 publisher is : ", b1.publisher)
print(" Book b1 publisher is : ", b1.title)
b2 = Book("Dragon,Inc")  # object is created with given publisher name
print(" Book b2 publisher is : ", b2.publisher)

print("\n********** Modifying object property *********")
b1.publisher = "New Publisher"
print(" Book b1 publisher is : ", b1.publisher)

print("\n********** Deleting  object property *********")
del b1.publisher
try:
    print(" Book b1 publisher is : ", b1.publisher)
except Exception as e:
    print("ERROR : " + str(e))
