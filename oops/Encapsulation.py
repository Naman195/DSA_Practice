class Animal:
    
    def __init__(self, species, color):
        self.__species = species
        self.color = color
        
        
        
    
    def sound(self):
        print("This Animal makes some Sound")
    
tiger = Animal("Tiger", "Black")

print(tiger.__species)
print(tiger.color)
        