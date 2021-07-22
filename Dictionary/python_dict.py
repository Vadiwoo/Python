print('''A dictionary is a collection which is ordered, changeable and does not allow duplicates.
Dictionaries are written in key-values pair\n''')

print("\n********** creating a dictionary  **********")
dict_items = {
    "language": "C",
    "year": 1972,
    "creator": "DennisRitchie"  # BjarneStroustrup,
}
print("\n**********  accessing dictionary items  **********")
print(dict_items)

print("\n********** accessing an item by key   **********")
print(dict_items['year'])

print("\n********** accessing an item by get()  **********")
print(dict_items.get('creator'))

print("\n********** accessing keys of a dictionary  **********")
print(dict_items.keys())

print("\n********** accessing values of a dictionary  **********")
print(dict_items.values())

print("\n********** accessing items of a dictionary  **********")
print(dict_items.items())

print("\n********** adding new key to dictionary  **********")
dict_items['has_pointer'] = 'True'
print(dict_items.keys())

print("\n********** checking if a key exists in a  dictionary  **********")
if "year" in dict_items:
    print("yes")

if "score" in dict_items:
    print("yes")
else:
    print("no")

print("\n********** changing item values in a dictionary  **********")
dict_items['year'] = 1998
print(dict_items)

print("\n********** changing item values in a dictionary  **********")
dict_items.update({'year': 1972})
print(dict_items)

print("\n********** removing  item using key name : using pop()   **********")
dict_items.pop('has_pointer')
print(dict_items)

print("\n********** removing last inserted  item  : using popitem()   **********")
dict_items.popitem()
print(dict_items)

print("\n********** removing item using key name : using del()   **********")
del dict_items['year']
print(dict_items)

print("\n********** removing entire dictionary  : using del()   **********")
del dict_items
# print(dict_items)  # error due to dictionary has been deleted

print("\n********** removing entire dictionary  : using clear()   **********")
dict_items = {
    "language": "C",
    "year": 1972,
    "creator": "DennisRitchie"  # BjarneStroustrup,
}
print(dict_items)
dict_items.clear()
print(dict_items)

print("\nLooping through a dictionary:")
dict_items = {
    "language": "C",
    "year": 1972,
    "creator": "DennisRitchie"  # BjarneStroustrup,
}
print("\ngetting all key names of a dictionary: method 1")
for x in dict_items:
    print(x)

print("\ngetting all key names of a dictionary: method 2")
for x in dict_items.keys():
    print(x)
print("\ngetting all values names of a dictionary ; method 1 ")
for x in dict_items.values():
    print(x)
print("\ngetting all values names of a dictionary: method 2 ")
for x in dict_items:
    print(dict_items[x])

print("\ngetting all key value pairs  of a dictionary")
for x, y in dict_items.items():
    print(x, y)

print("\nCopying a  dictionary : using copy()")
copy_dict = dict_items.copy()
print(copy_dict)

print("\nCopying a  dictionary : using dict()")
copy_dict = dict(dict_items)
print(copy_dict)

print("\nNested Dictionary : method 1 ")
nested_dict = {
    "first": {
        "language": "C",
        "year": 1972,
        "creator": "DennisRitchie"
    },
    "second": {
        "language": "C++",
        "year": 1983,
        "creator": "Bjarne Stroustrup"
    },
    "third": {
        "language": "Java",
        "year": 1995,
        "creator": " James Gosling "
    }
}
print(nested_dict)

print("\nNested Dictionary : method 1 ")
first = {
        "language": "C",
        "year": 1972,
        "creator": "DennisRitchie"
    }
second = {
        "language": "C++",
        "year": 1983,
        "creator": "Bjarne Stroustrup"
}
third =  {
        "language": "Java",
        "year": 1995,
        "creator": " James Gosling "
    }
nested_dict= {
    "first" : first,
    "second": second,
    "third" : third
}
print(nested_dict)


print("\ncreating a Dictionary using fromkeys() method")
languages = ('C', "C++", "Java")
score = 90

new_dict = dict.fromkeys(languages,score)

print(new_dict)

print('''\nsetdefault() method returns the value of the item with the specified key. If the key does not exist, 
the method will insert the key, with the specified value''')
print(dict_items)
x= dict_items.setdefault("score", 95)
print(x)
print(dict_items)
