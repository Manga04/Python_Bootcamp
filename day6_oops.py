class Myclass:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a//b
    def mod(a,b):
        return a%b
obj1=Myclass
obj2=Myclass
print(obj1.add(4,3))
print(obj1.sub(4,3))
print(obj1.mul(4,3)) 
print(obj1.div(6,3))
print(obj1.mod(15,3))
print(obj2.add(6,3))
print(obj2.sub(7,3))
print(obj2.mul(3,3))
print(obj2.div(9,3))
print(obj2.mod(14,3))