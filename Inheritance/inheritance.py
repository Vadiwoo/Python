print('''Inheritance allows the Child Class to inherit all the properties as well as methods from the Parent Class.''')

print("\n********** Creating a Parent Class  *********")


class IPhone:
    company = 'Apple Inc'

    def __init__(self):
        self.color = 'grey'
        # self.phoneId = id

    def setColor(self, colorName):
        self.color = colorName

    def getColor(self):
        return self.color


# creating instances of class IPhone
iphone1 = IPhone()
print("iphone 1\nCompany: ", iphone1.company,"\nPhone color: ", iphone1.getColor())
iphone2 = IPhone()
iphone2.setColor("red")
print("\niphone 2\nCompany: ", iphone2.company,"\nPhone color: ", iphone2.getColor())

print("\n********** Creating a Child  Class without any properties and methods  *********")


class IPhoneTen(IPhone):
    pass


iphone3 = IPhoneTen()
print("\niphone 3\nCompany: ", iphone1.company, "\nPhone color : ", iphone1.getColor())

print("\n********** Creating a Child  Class  constructor ( __init__() )   *********")


class IPhoneTen(IPhone):
    def __init__(self):
        print("This is IPhone 10")


iphone4 = IPhoneTen()
print("\niphone 4\nCompany: ", iphone4.company, "\nPhone color: ")
try:
    print("\niphone 4\nCompany: ", iphone4.company, "\nPhone color: ", iphone4.getColor())

except Exception as e:
    print("\nERROR : " + str(e))
print("\nPython throws this error because the child's constructor (__init__() function ) overrides the inheritance of "
      "the parent's  constructor (__init__() function")
print("\nTo resolve this issue, we need to call the Parent Class Constructor")

print("\n********** Calling Parent Class Constructor from Child Class  *********")


class IPhoneTen(IPhone):
    name = "IPhone 10"

    def __init__(self):
        IPhone.__init__(self)


iphone5 = IPhoneTen()
print("\niphone 5\nCompany: ", iphone5.company, "\nPhone color : ", iphone5.getColor(), "\nName :", iphone5.name)


print("\n********** The  use of super() function  *********")
print('''We also can use the super() function to make the child class to inherit all the Parents class properties and 
methods.''')


class IPhoneTen(IPhone):
    name = "IPhone 10"

    def __init__(self):
        super().__init__()


iphone6 = IPhoneTen()
iphone6.setColor("Yellow")
print("\niphone 6\nCompany: ", iphone6.company, "\nPhone color: ", iphone6.getColor(), "\nName :", iphone6.name)

print('''\nAdding properties and methods to child classes''')


class IPhoneTen(IPhone):
    name = "IPhone 10"

    def __init__(self):
        super().__init__()
        self.faceRecognition = True # adding property

    def heartRate(self):
        print("HeartRate checking is available.")  # adding method


iphone7 = IPhoneTen()
iphone7.setColor("Orange")
print("\niphone 7  \nCompany: ",iphone7.company,"\nPhone color : ", iphone7.getColor(), "\nName :",iphone7.name, " \nFace Recognition :",iphone7.faceRecognition)
print("\nAdditional Functionality : ")
iphone7.heartRate()
