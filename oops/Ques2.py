# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
class Person:
    def __init__(self, name, age, country, dob):
        self.name = name
        self.age = age
        self.country = country
        self.dob = dob
        
        
        
    def showAge(self):
        print(f'{self.name} Age {self.age}')
p1 = Person("Naman", 21, "India", "12/06/2023")
print(p1.showAge())
        