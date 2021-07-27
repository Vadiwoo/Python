print(''' def keyword : python functions are defined with the def keyword *********''')


def python_function():
    print("This statement is inside a function")


print("\n********** calling a function  **********")
python_function()

print("\n********** function with arguments **********")


def calculate_area(x, y):
    return x * y


print("Area 1  is ", +calculate_area(12, 45))
print("Area 2 is ", round(calculate_area(1.2, 4.3), 2))

print("\n********** function with arbitrary arguments, (*args) **********")


def arbitraryArguments(*languages):
    print("The second language is " + languages[1])


languages = ("C", "C++", "Python", "Java")
arbitraryArguments(*languages)
arbitraryArguments("JavaScript", "SQL", "R")

print("\n********** key-value arguments**********")


def keyValueArguments(first, second, third):
    print("The second language is " + second)


keyValueArguments(first="Go", second="Pearl", third="Ruby")

print("\n********** default parameter value **********")


def defaultParameter(language="Python"):
    print("The  language is " + language)


defaultParameter()
defaultParameter("Java")

print("\n********** Passing A List/Tuple/Dictionary as arguments **********")


def collectionAsArguments(collection):
    print("\nThe type of collection is : ", type(collection))
    if type(collection) == dict:
        for x, y in collection.items():
            print(x, ":", y)
    else:
        for x in collection:
            print(x)


languages = tuple(("C", "C++", "Python", "Java"))
collectionAsArguments(languages)

languages = list(("C", "C++", "Python", "Java"))
collectionAsArguments(languages)

languages = set(("C", "C++", "Python", "Java"))
collectionAsArguments(languages)

languages = dict({"first": "C", "second": "C++", "third": "Python", "fourth": "Java"})
collectionAsArguments(languages)

print("\n********** function recursion : function calls itself  : example 1 **********")
print('''In this example below  recursion function that takes a number as argument and 
recurse after decrementing the number by one, and finally prints the  results. ''')


def recursion(n):
    if n > 0:
        result = n + recursion(n - 1)
    else:
        result = 0
    return result


print("\n\nRecursion Results : ")
n = 10
for i in range(n):
    print(" ", recursion(i))

print("\n********** function recursion : function calls itself  : example 2 **********")
print('''A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....''')
print('''In this example below we will print Fibonacci numbers using recursion. ''')


def fibonacciRecursion(n):
    if n <= 1:
        return n
    else:
        return fibonacciRecursion(n - 1) + fibonacciRecursion(n - 2)


print("Fibonacci Series:")
for i in range(10):
    print(" ", fibonacciRecursion(i))
