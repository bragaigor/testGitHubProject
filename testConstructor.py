class MyClass:

    # def __init__(self, myVar, anotherVar = 0):
    #     self.myVar = myVar
    #     self.anotherVar = anotherVar

    # Constructor
    def __init__(self, myVar):
        self.myVar = myVar

    def __init__(self, myVar, anotherVar):
        self.myVar = myVar
        self.anotherVar = anotherVar

    def getMyVar(self):
        return self.myVar

    def getMySecondVar(self):
        return self.anotherVar

    def __str__(self):
        return "Hello " + str(self.myVar)

myClass = MyClass(36, 21)
print(myClass.getMyVar())
print(myClass.getMySecondVar())

print(myClass)