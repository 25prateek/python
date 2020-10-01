# polymorphism duck typing

class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        sum1=self.m1+self.m2
        sum2=other.m1 + other.m2
        #s3=student(sum1,sum2)
        return sum1+sum2
        #return  s3

s1=student(34,87)
s2=student(44,75)
s3=s1+s2
#print(s3.m1)
#print(s3.m2)
print(s3)