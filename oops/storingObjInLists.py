class Movie(object):
    
    def __init__(self, nm, runtime, hero):
        self.name = nm
        self.runtime = runtime
        self.hero = hero
    
    def display(self):
        print(f"Movie name is {self.name}\n Runtime is {self.runtime}\n Movie Hero is {self.hero}")
    

list_of_movies = []
while True:
    movieName=input("Enter the Name of a Movie : ")
    runtime = input("Enter the Runtime : ")
    hero = input("Enter the Hero Name: ")
    
    obj = Movie(movieName, runtime, hero)
    list_of_movies.append(obj)
    print("Movie added to  the list")
    ans = input("Enter 'Y' for continue")
    if ans != "Y":
        break

print("All movies Info")
for obj in list_of_movies:
    obj.display()
    
    
    