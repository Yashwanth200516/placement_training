class Shape:
    def area(self):
        return 0
    
class Circle(Shape):
    def __init__(self,r):
        self.r=r

    def area(self):
        return 3.14*self.r**2
    
class Rectangle(Shape):
    def __init__(self,w,h):
        self.w,self.h=w,h

    def area(self):
        return self.w * self.h
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return (1/2)*self.base*self.height
    
shapes=[Circle(5),Rectangle(4,6),Triangle(2,6)]

for shape in shapes:
    print(f"Area: {shape.area()}")