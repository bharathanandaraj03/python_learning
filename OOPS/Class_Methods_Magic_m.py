class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
         area = self.width * self.height
         return area

r1 = Rectangle(2,4)
print(r1.area())

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x},{self.y})"

p1 = Point(2,3)
print(p1)