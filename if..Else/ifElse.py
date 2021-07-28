print('''python if..else statements relies on the indentation of the statements. ''')

print("\n********** using if..elif  : finding max and min values of a tuple**********")
mytuple = (2, 5, 7, 3, 6, 10)
max= mytuple[0]
min = mytuple[0]

for i in range(0, len(mytuple)):
    if (mytuple[i]) > max:
        max = mytuple[i]
    elif mytuple[i] < min :
        min = mytuple[i]
print("Maximum Vale is :", +max)
print("Minimum Vale is :", +min)

print("\n********** using else  : the else keyword will execute the code that wasn't caught by if..elif codes**********")

for x in mytuple:
    if x < 5 :
        print('{:> 4d}'.format(x), ": Group 1")
    elif 5 <= x < 10:
        print('{:> 4d}'.format(x), ": Group 2")
    else:
        print('{:> 4d}'.format(x), ": Group 3")
