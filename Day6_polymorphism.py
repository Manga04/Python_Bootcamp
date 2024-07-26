'''mehtod over riding'''
class animal:
    def speak():
        return "animal is speaking"
class dog(animal):
    def speak():
        return "bow..."
class puppy(dog):
    def speak():
        return "bow..."
obj1=puppy
print(obj1.speak()) 



   
