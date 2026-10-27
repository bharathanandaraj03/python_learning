import Basics.conditonal_looping as conditonal_looping 

class Laptop:
    def __init__(self):
        pass
    def cpu(self):
        print("CPU")
    def memory(self):
        print("Memory")


class Desktop:
    def __init__(self):
        pass
    def memory(self,disk):
        print("Disk memory")
        
obj = Laptop()
obj.memory()

conditonal_looping.factorial(2)