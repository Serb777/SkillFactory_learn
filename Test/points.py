from math import pi

class Dot:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y

    def __str__(self):
        return f'Dot: {self.x,self.y}'

class Circle:

    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area_circle(self):
        self.area = 2 * pi * self.radius
        print(self.area)
        return self.area
        


p1=Dot(1,2)
p2=Dot(1,2)
circle_1 = Circle(1)
circle_2 = Circle(2)
circle_1.calculate_area_circle()
print(p1==p2)
print(str(p1))
print(p2)
