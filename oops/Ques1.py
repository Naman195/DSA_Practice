# Ques 1 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class circle:
    def __init__(self, radius):
        self.radius = radius
    
    def areaOfCircle(self):
        return 3.14 * (self.radius **2)
    
    def perimeterOfCircle(self):
        return  2* math.pi*(self.radius**2)

c1 = circle(2)
print(c1.areaOfCircle())
print(c1.perimeterOfCircle())
    