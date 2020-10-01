# custroctor in inheritance class

class a:
    def __init__(self):
        print("custroctor A")

    def fun1(self):
        print(" fun 1")
    def fun2(self):
        print("fun 2")

class b(a):
    def __init__(self):
        super(b, self).__init__()
        #or
        super().__init__()
        print("custorctor B")
        '''
        when create object of sub class it will call init of sub class first 
        yha pe b class ka call hua agar uska init nhi hota to bho class a ka init call krta 
        but if it has then bho aapne apko fist priority deta h
        
        if u call super then i call super class first then call sub class 
        
        '''
    def fun3(self):
        print(" fun 3")

    def fun4(self):
            print("fun 4")


class c:
    def __init__(self):
        print("custroctor c")

    def fun1(self):
        print(" fun 1")
    def fun2(self):
        print("fun 2")

class d():
    def __init__(self):
        print("custroctor d")

    def fun3(self):
        print(" fun 3")

    def fun4(self):
            print("fun 4")
class f():
    def __init__(self):
        print("custroctor f")
class e(c,d,f):
    def __init__(self):
        super().__init__()
        super(d,self).__init__() #it shows init of next class mro after the class
        super(f,self).__init__()
        #agar next init class nhi h toh kuch nhi karega print
        '''
        here it call custructor of c becaue it folloe MRO which is left to right 
        it print custructor of left onle giver class here of c 
        
        '''
        print("custroctor E")
s1=b()
print("\n MRO :- method resolution order \n")
s2=e()
'''
note:- like custruct it work for funtion(method) 
both super() and also MRO funtion

supermethod we call i and also super class also

'''