'''inheritance'''
class animal:
    def speak():
        return "animal is speaking"
'''single'''
class dog(animal):
    def bark():
        return "bow..."
obj1=animal
obj2=dog
#print(obj1.speak()) 
#print(obj2.bark())   
'''multilevel'''
class puppy(dog):
    def puppy_speaking():
        return "i am puppy"
obj1=animal
obj2=puppy
print(obj1.speak()) 
print(obj2.bark())  
print(obj2.puppy_speaking())  
     
