class Animal:
    
    def sound(self):
        print("This Animal makes Some Sound")


class wild(Animal):
    def wildAnimal(self):
        print("This Animal can't be pet")
    

class Domestic(Animal):
    def domestinAnimal(self):
        print("This animal can be called as pet")

x = wild()
x.sound()
x.wildAnimal()