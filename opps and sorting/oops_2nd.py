class computer:
    def __init__(self,cpu,ram):
        print("in init ")
        self.cpu=cpu
        self.ram=ram
        print("config is",cpu,ram)
    def update(self):
        self.ram=8

    def config(self):
        print("config fucn is:",self.cpu,self.ram)
    def compare(self,other):
        if self.ram==other.ram:
            print('hello comparre true')
            return True
        else:
            print('hello compare false')
            return False
comp1=computer("i3",16)
comp2=computer("i5",8)
comp1.config()
comp2.config()
comp1.update()
print(comp1.ram)
print("config3 is  :",comp1.cpu,comp1.ram)
print(comp1.compare(comp2))

#with out init
class co:
    def con(self,ram,size):
        print('hello class co and con object')
        print('ram is here',ram,size)
   

c1=co()
c2=co()
c1.con('rem',12)
c2.con('madb',12)
