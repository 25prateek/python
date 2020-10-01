# custroctor in inheritance class

class a:
    def __init__(self):
        print("custroctor A")

    def fun1(self):
        print(" fun 1")
    def fun2(self):
        print("fun 2")

class b(a):
    #here we don't have init method/constructor in class b so it call class init method
    def fun3(self):
        print(" fun 3")

    def fun4(self):
            print("fun 4")


s1=b()
#here we don't have init method/constructor in class b so it call class init method
#if we have init method in b then it call b init method

#s1.b