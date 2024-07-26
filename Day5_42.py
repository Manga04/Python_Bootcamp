# method overloading
class cal:
    def add(self,*args):
        return sum(args)
    # takes inputs:
obj1=cal()
print(obj1.add(1,2))
print(obj1.add(1,2,3))
print(obj1.add(1,2,3,4)) 

#try 
