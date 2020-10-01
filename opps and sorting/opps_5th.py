
 #types of method

class student:

    college="skit"

    def __init__(self,m1,m2,m3):
        self.m1 =  m1
        self.m2=m2
        self.m3=m3
    def avg(self): #instance method-----------------1
        return (self.m1+self.m2 + self.m3)/3
    '''
    instance mathod has two types 
    1 :- accessor(getors) - the only fetch the value then return or print
    2 :- mutators(setors) - they set the value or change the value    
    '''
    def get_m1(self): #accessor / gettors
        return self.m1
    def set_m1(self,value): #mutators
        self.m1=value
        return self.m1

    #classmethod-------------------------------------2
    @classmethod  #decorater for class method
    def get_clgname(cls):
        return cls.college

    #static method----------------------------------------3
    @staticmethod #decoratoe for static method
    def info():
        print("this id prateek learn opps concept")

s1=student(54,67,96)
s2=student(32,66,98)

print(s1.avg())
print(s2.avg())

print(s2.get_m1(),s2.set_m1(10))


print("class method : -",student.get_clgname())

student.info()