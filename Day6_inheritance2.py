'''multiple'''
class father():
    def father_speaking():
        return "father class"
obj1=father
class mother():
    def mother_speaking():
        return "mother class"
obj2=mother    
class kid(father,mother):
    def kid_speaking():
        return "im kid, i have property of father and mother"
obj3=kid
print(obj1.father_speaking())    
print(obj2.mother_speaking())    
print(obj3.kid_speaking())    
