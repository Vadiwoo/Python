print("""Tuples are a  collection  of items which are ordered and immutable. Immutable means we are not allowed to 
do any operations such as adding , removing or changing  items in a tuple  after it's creation. However we are 
allowed to have duplicate items in tuple\n""")

print("\n********** creating a tuple  **********")
tuple_items = ("C", "C++", "Java", "JavaScript", "Python")
print(tuple_items)

print("\n********** type of a  tuple **********")
print(type(tuple_items))

print("\n********** tuple  with one item : need to add coma after the item**********")
oneItem_tuple = ("C",)
print(type(oneItem_tuple))

oneItem_tuple = "C"
print(type(oneItem_tuple))

print("\n********** creating a tuple with the tuple() constructor **********")
tuple_constructor = tuple(("C", "C++", "Java", "JavaScript", "Python"))
print(tuple_constructor)
print(type(tuple_constructor))

print("\n********** Accessing tuple items : using index**********")
print(tuple_items[2])

print("\n********** Accessing tuple items : using negative index **********")
print(tuple_items[-2])  # -1 refers to last item and -2 refers to second item from last

print("\n********** Accessing tuple items : using index range**********")
print(tuple_items[:2])

print("\n********** Accessing tuple items : using index range**********")
print(tuple_items[2:])

print("\n********** Accessing tuple items : using index range**********")
print(tuple_items[2:4])

print("\n********** Workaround on changing tuple values**********")
print('''\nSince tuple values are immutable, we cannot change the values once they are created. "
      "However,we can convert them to list, change the values and convert them back to tuple.''')
mylist = list(tuple_items)
print(mylist)
mylist.append("Go")
print(mylist)
tuple_items = mylist
print (tuple_items)


print("\n********** Unpacking a tuple**********")
print('''In python, unpacking a tuple  is a process of assigning tuple values to another variable. In the following 
example, we are assigning the tuple values to different description.''')
(DennisRitchie, BjarneStroustrup, JamesGosling, BrendanEich, GuidoVanRossum,Google) = tuple_items
print(Google)
print(JamesGosling)
print("\n********** Unpacking a tuple using asterisk(*) : example 1**********")
(has_pointers, has_pointers, *no_pointers, has_pointers) = tuple_items
print(has_pointers)
print(no_pointers)
print("\n********** Unpacking a tuple using asterisk(*) : example 2 **********")
(B, *A, C) = tuple_items
print("Grade A is for :", A)
print("Grade B is for :", B)
print("Grade B is for :", C)
