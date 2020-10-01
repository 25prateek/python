
#innerclass oops

class student:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop("dell","i5","8gb")


    def show(self):
        print(self.name,self.roll)
        self.lap.show()

    class laptop:   #inner class
        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=student("prateek",119)
s2=student("aman",10)
s1.show()

l1=student.laptop("hp","i7","16gb")
l1.show()

s2.show()
s2.laptop("lenovo","i3","4gb").show()


#print(l1)
s1.show()
print('lap show ---------------------')
s1.lap.show()