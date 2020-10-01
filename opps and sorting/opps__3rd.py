
#types of variable

class car:

    wheel=5 # class variable
    def __init__(self,name,mil):
        self.name="dell" #instace variable
        self.mil="65" #instance variable

c1=car("bmw",67)
c2=car('rc',88)

print(c1.name,c1.mil,c1.wheel)
c1.mil=96
car.wheel=6
print(c1.name,c1.mil,c1.wheel)
print(c2.name,c2.mil,c2.wheel)