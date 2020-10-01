
#inhetance in opps python

class a:
    def fun1(self):
        print(" fun 1")
    def fun2(self):
        print("fun 2")

class b(a): #single level inheritance
    def fun3(self):
        print(" fun 3")

    def fun4(self):
            print("fun 4")

class c(b): #multi level inheritance
    def fun5(self):
        print(" fun 5")

    def fun6(self):
            print("fun 6")
class d:
    def fun7(self):
        print("fun 7")

class e(d,c): #multiple inheritance
    pass

s1= a()
s2=b()
s3=c()

s4=e()


s1.fun1()

print("single inheritance")

s2.fun1()
s2.fun3()

print("multi level inheritance")

s3.fun1()
s3.fun4()
s3.fun6()

print("multiple inheritance")
s4.fun1()
s4.fun3()
s4.fun5()
s4.fun7()