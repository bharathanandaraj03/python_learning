class Exercise2:
    def __init__(self):
        self.s = ""
    def getinput(self):
       self.s = input("Enter input: ")
    def printoutput(self):
        print(f"Entered input is: {self.s}")

class Person:
    def __init__(self,name,age):
       self.name = name
       self.age = age
    def greet(self):
        print(f"Hello my name is: {self.name} ")

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
            print(f"{self.name} says wolf")

class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

s1 = student("Ram",16) 
print(s1.name)
s1.name  = "David"
print(s1.name)
d1 = Dog("Buddy",3)
d1.bark()
    
#classobj = Exercise2()
#classobj.getinput()
#classobj.printoutput()

personobj= Person("John",36)
personobj.greet()