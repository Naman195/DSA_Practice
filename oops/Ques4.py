# 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
class Shape:
    def __init__(self):
        pass
    
    def calculateArea(self):
        pass
    
    def calculate_perimeter(self):
        pass
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    
    def calculateArea(self):
        return 3.14 * (self.radius **2)

    def calculate_perimeter(self):
        return (2 * math.pi*self.radius)
class Triangle(Shape):
    def __init__(self, base, Height, side1, side2, side3):
        self.base=base
        self.height = Height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculateArea(self):
        return 0.5*self.base*self.height
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

T1 = Triangle(1,2,0.5,4,3)

print(T1.calculateArea()) 