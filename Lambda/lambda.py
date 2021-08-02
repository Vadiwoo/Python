print("In Python, lambda is small anonymous function which are restricted to single line expression. "
      "They can take any number or arguments and return the results.\nThey are generally used when a function is needed "
      "temporarily for a short period of time.\nThey are written as: lambda arguments: "
      "expression")

print("\n********** lambda functions with no arguments  *********")
zeroArgument = lambda: "Python Lambda Function"

print(zeroArgument())

print("\n********** lambda function  with 2 arguments  *********")

multply_lambda = lambda x, y: x * y

print(multply_lambda(4, 5))

print("\n********** def function  *********")


def multiply_def(x, y): return x * y


print(multiply_def(4, 5))

print(type(multply_lambda))
print(type(multiply_def))

print("The type shows that both lambda and def are both functions. Using lambda functions, we can define and call it\n"
      "immediately at the end of definitions, However we can not  do this using def.")

print("\n********** Lambda function can be invoked immediately , but not def function  *********")
print((lambda x, y: x * y)(5, 7))


def addition(x, y):return x + y(5, 7) # this line doesnt invoked
