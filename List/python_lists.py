print ("""Lists are a  collection  of items which are ordered and mutable.
Mutable means we can add, remove and  change items in a list after it's creation\n""")

print("\n********** creating list **********")
item_list = ["C", "C++", "Java", "JavaScript", "Python"]
print(item_list)

print("\n********** changing item name in a list **********")
item_list[1] = "C PlusPlus"
print(item_list)

print("\n********** type of a  list **********")
print (type(item_list))

print("\n********** looping through a list : for loop, method 1 **********")
for x in item_list:
    print(x)

print("\n********** looping through a list : for loop method 2 **********")
for x in  range(len(item_list)):
    print(item_list[x])

print("\n********** looping through a list : while loop **********")
x = 0
while (x < len(item_list)):
    print(item_list[x])
    x = x+1

print("\n********** sorting lists  **********")
item_list.sort(reverse=True)
print("sorted list in reverse order :", item_list)

score = [85, 95, 73, 78, 90]
score.sort()
print("sorted list :", score)

print("\n********** copying lists  **********")
copyList = item_list.copy()
print(copyList)

print("\n********** joining   lists  **********")
newlist = item_list + score
print(newlist)

print("\n********** Built-in methods for lists  **********")

print("\n********** append() : adding an item to list **********")
item_list.append("R")
print(item_list)
print("\n********** remove() : removing item from list **********")
item_list.remove("JavaScript")
print(item_list)

print("\n********** clear() : remove all elements from a  list **********")
item_list.clear()
print(item_list)
item_list = copyList

print("\n********** count() : count of elements with the specified value**********")
items = item_list.count('C')
print (items)
counters = [2, 4, 5, 2, 3, 4, 6, 7, 8, 9, 2]
print(counters)
print("Number 2 repeated", counters.count(2), " times.")

print("\n********** extend() add elements to end of list**********")
item_list.extend(score)
print(item_list)

print("\n********** index()  : returns the index of an specified element**********")
print(" Index of Java is :", item_list.index("Java"))

print("\n********** insert()  : insert element at a  specified index**********")
item_list.insert(1, "C#")
print(item_list)

print("\n********** pop()  : removes an element from a  specified index**********")
item_list.pop(1)
print(item_list)
print("\n********** reverse()  : reverse the order of elements of a list **********")
item_list.reverse()
print(item_list)