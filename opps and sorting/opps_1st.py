class computer:
    def config(self):
        print("hii config")


comp1 = 1
comp2 = computer()
computer.config(comp1)# here it run even we assign comp1 int value 1
computer.config(comp2)
#co mp1.config() #here we get erroe com1.config has int value
comp2.config() 