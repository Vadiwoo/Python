print("\n********** Looping through a string **********")
for x in "programming":
    print(x)

print("\n********** Looping through a list **********")
myList = list(("C", "C++", "Java"))
for x in myList:
    print(x)

print("\n********** break : Stopping a for_loop using **********")
for x in myList:
    print(x)
    if x == "C++":
        break
print("\n********** continue : skipping the current iteration and moving to next one **********")
for x in myList:
    if x == "C++":
        continue
    print(x)

print("\n********** range() : the range() function returns sequence of numbers from 0 to specified number(exclusive) "
      "**********")
for x in range(5):
    print(x)

print("\n********** range(x,y) : the range() function with two parameters **********")
for x in range(2,6):
    print(x)

print("\n********** range(x,y, z) : the range() function with three  parameters **********")
for x in range(20,100, 10):
    print(x)

print("\n********** else keyword : specifies a block of code to be executed after the for loop **********")
for x in range(20,100, 10):
    print(x)
else :
    print("Nicely Done") # will not be executed if for loop exists with break statement

print("\n********** Nested Loop **********")
colors = ["red", "orange", "yellow"]
score = list(("book", "pen", "bag"))
for x in colors:
    for y in score:
        print(x, y)
    print("\n")