class Exercise2:
    def __init__(self):
        self.s = ""
    def getinput(self):
       self.s = input("Enter input: ")
    def printoutput(self):
        print(f"Entered input is: {self.s}")

classobj = Exercise2()

classobj.getinput()
classobj.printoutput()