print("""Sets are a  collection  of items which are unordered and un-indexed and immutable. So, we can't access the 
items of a set using index. Immutable means we are not allowed to change  items in a set  after it's creation.
Sets also do not allows to have duplicate items.\n""")

print("\n********** creating a set : duplicate items are not allowed**********")
set_items = {"C", "C++", "Java", "JavaScript", "Python", "C++"} # trying to add duplicate item to a set
print(set_items)

print("\n********** type of a  set **********")
print(type(set_items)) # curly braces indicates this collection is a set

print("\n********** creating a set : using a constructor**********")
set_items = set(("C", "C++", "Java", "JavaScript", "Python", "C++"))
print(set_items)
print(type(set_items))

print("\n********** accessing items of a set **********")
for item in set_items:
    print(item)

print("\n********** checking if an item exists in a set **********")
for item in set_items:
    if item == "C++":
        print(item)
print("\n********** checking if an item exists in a set : output is a boolean value **********")
print("JavaScript" in set_items)

print("\n********** Adding items to a set **********")
set_items.add("Go")
print(set_items)

print("\n********** update() method : can be used to set, list, tuple and dictionaries**********")
print("\n********** adding another set to a set : using update() **********")
new_items= set(("Ruby", "Pearl", "R"))
set_items.update(new_items)
print(set_items)

print("\n********** adding another list to a set : using update() **********")
new_items= list(("Swift", "C#", "SQL"))
set_items.update(new_items)
print(set_items)

print("\n********** Removing items from a set : using remove()**********")
set_items.remove("Swift")
print(set_items)

print("\n********** Removing items from a set : using discard()**********")
set_items.discard("Pearl")
print(set_items)

print("\n********** Removing items from a set : using pop(), last item will be removed**********")
removed_item = set_items.pop()
print(removed_item)
print(set_items)


print("\n********** Removing All items from a set : using clear()**********")
new_items= set(("Swift", "C#", "SQL"))
print(new_items)
new_items.clear()
print(new_items)
new_items.add("SQL") # clear() will remove all items, but the set is still exists, we can add items
print(new_items)

print("\n********** Removing All items from a set : using del()**********")
new_items= set(("Swift", "C#", "SQL"))
print(new_items)
del new_items  # del will remove the set completely.

print("\n********** Joining sets: using union()**********")
set_items = {"C", "C++", "Java", "JavaScript", "Python"}
new_items= set(("Swift", "C#", "SQL"))
set_items.update(new_items) # update will add the second set items into the first one
print(set_items)
set3= set_items.union(new_items) # union will create a new set
print(set3)

print("\n********** Joining sets: using intersection_update() to keep items present in BOTH sets**********")
set_items = {"C", "C++", "Java", "JavaScript", "Python"}
new_items= set(("C++", "C", "SQL"))
set_items.intersection_update(new_items)
print(set_items)

print("\n********** Joining sets: using intersection() to keep items present in BOTH sets, returning  a new "
      "set**********")
set_items = {"C", "C++", "Java", "JavaScript", "Python"}
new_items= set(("C++", "C", "SQL"))
set3= set_items.intersection(new_items)
print(set3)

print("\n********** Joining sets: using symmetric_difference_update() to eliminate duplicates **********")
set_items = {"C", "C++", "Java", "JavaScript", "Python"}
new_items= set(("C++", "C", "SQL"))
set_items.symmetric_difference_update(new_items)
print(set_items)

print("\n********** Joining sets: using symmetric_difference() to eliminate duplicates, returning a new set **********")
set_items = {"C", "C++", "Java", "JavaScript", "Python"}
new_items= set(("C++", "C", "SQL"))
set3 = set_items.symmetric_difference(new_items)
print(set3)

print("\n********** checking for disjoints sets: using disjoint()**********")
set_items = {"C", "C++", "Java", "JavaScript", "Python"}
new_items= set(("C++", "C", "SQL"))
x = set_items.isdisjoint(new_items)
print(x)
print("isdisjoint() returns True if none of the items are present in both sets, otherwise it returns False.")

print("\n********** checking for subsets: using issubset()**********")
set_items = {"C", "C++", "Java", "JavaScript", "Python"}
new_items= set(("C++", "C", "Java"))
x = new_items.issubset(set_items)
print(x)
print("\n********** checking for supersets: using issuperset()**********")
set_items = {"C", "C++", "Java", "JavaScript", "Python"}
new_items= set(("C++", "C", "Java"))
x = set_items.issuperset(new_items)
print(x)